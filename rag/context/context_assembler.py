"""Context assembly engine with duplicate suppression, diversity control, and context budget management."""

from __future__ import annotations

import hashlib
import logging
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Set

from rag.context.models import AssembledContext, ContextItem, ContextMetadata, RerankedResult
from rag.context.reranker import ContextReranker, RerankerConfig
from rag.retrieval.models import RetrievalResult
from rag.retrieval.semantic_retriever import SemanticRetriever

logger = logging.getLogger(__name__)


@dataclass
class AssemblerConfig:
    """Configuration for duplicate control, diversity limits, and context budget."""

    max_context_items: int = 5
    max_characters: int = 8000
    max_tokens_estimate: int = 2000
    max_chunks_per_document: int = 2
    min_score_threshold: float = 0.15
    candidate_fetch_top_k: int = 15
    token_character_ratio: float = 4.0  # Approx 4 chars per token


class ContextAssembler:
    """Production context assembly engine.
    
    Transforms retrieved candidate chunks into an LLM-ready, diversity-controlled,
    deduplicated, budget-bounded context payload.
    """

    def __init__(
        self,
        retriever: Optional[SemanticRetriever] = None,
        reranker: Optional[ContextReranker] = None,
        config: Optional[AssemblerConfig] = None,
    ) -> None:
        self.retriever = retriever or SemanticRetriever()
        self.reranker = reranker or ContextReranker()
        self.config = config or AssemblerConfig()

    def _estimate_tokens(self, text: str) -> int:
        """Estimate token count based on word and character heuristics."""
        if not text:
            return 0
        words = len(text.split())
        chars = len(text)
        # Blend word count heuristic (1.3x words) and char heuristic (chars / 4)
        return max(int(words * 1.3), int(chars / self.config.token_character_ratio))

    def _is_near_duplicate(self, text1: str, text2: str, threshold: float = 0.90) -> bool:
        """Check if two texts are near-duplicates using character 5-gram Jaccard similarity."""
        if text1 == text2:
            return True

        # Quick length check
        len1, len2 = len(text1), len(text2)
        if len1 == 0 or len2 == 0:
            return False
        if min(len1, len2) / max(len1, len2) < 0.7:
            return False

        # Substring containment check for large overlap
        if len1 > 100 and len2 > 100:
            if text1 in text2 or text2 in text1:
                return True

        # N-gram Jaccard similarity
        n = 5
        if len1 < n or len2 < n:
            return text1.strip().lower() == text2.strip().lower()

        ngrams1 = {text1[i : i + n] for i in range(len1 - n + 1)}
        ngrams2 = {text2[i : i + n] for i in range(len2 - n + 1)}

        intersection = len(ngrams1 & ngrams2)
        union = len(ngrams1 | ngrams2)

        return (intersection / union) >= threshold if union > 0 else False

    def assemble(
        self,
        query: str,
        candidates: Optional[Sequence[RetrievalResult]] = None,
        user_context: Optional[Dict[str, Any]] = None,
        document_id_filter: Optional[int] = None,
        metadata_filter: Optional[Dict[str, Any]] = None,
        max_context_items: Optional[int] = None,
        max_characters: Optional[int] = None,
        max_chunks_per_document: Optional[int] = None,
    ) -> AssembledContext:
        """Assemble final context for a query.
        
        Args:
            query: User query string.
            candidates: Optional pre-retrieved candidates. If None, queries SemanticRetriever.
            user_context: Optional user context for permission checks.
            document_id_filter: Optional document filter.
            metadata_filter: Optional metadata filter.
            max_context_items: Override default max context items.
            max_characters: Override default max characters.
            max_chunks_per_document: Override default max chunks per doc.
            
        Returns:
            AssembledContext: Strongly typed LLM-ready context container.
        """
        start_time = time.perf_counter()

        # Handle empty/whitespace query
        if not isinstance(query, str) or not query.strip():
            logger.warning("Empty or invalid query passed to assemble context")
            return AssembledContext(
                query=query if isinstance(query, str) else "",
                items=[],
                metadata=ContextMetadata(
                    candidate_count=0,
                    selected_count=0,
                    total_time_ms=0.0,
                ),
                formatted_context="",
            )

        limit_items = max_context_items or self.config.max_context_items
        limit_chars = max_characters or self.config.max_characters
        limit_chunks_per_doc = max_chunks_per_document or self.config.max_chunks_per_document

        # 1. Retrieve candidates if not provided
        t_retrieval_start = time.perf_counter()
        if candidates is None:
            raw_candidates = self.retriever.retrieve_results(
                query=query,
                top_k=max(self.config.candidate_fetch_top_k, limit_items * 3),
                document_id=document_id_filter,
                metadata_filter=metadata_filter,
                user_context=user_context,
            )
        else:
            raw_candidates = [
                c for c in candidates
                if user_context is None or self.retriever.check_document_access(c.metadata, user_context)
            ]
        t_retrieval_ms = (time.perf_counter() - t_retrieval_start) * 1000.0

        candidate_count = len(raw_candidates)

        # 2. Rerank candidates
        t_rerank_start = time.perf_counter()
        reranked_results: List[RerankedResult] = self.reranker.rerank_candidates(
            query=query,
            candidates=raw_candidates,
        )
        t_rerank_ms = (time.perf_counter() - t_rerank_start) * 1000.0

        # 3. Filtering and Budget Assembly
        t_assembly_start = time.perf_counter()

        seen_chunk_ids: Set[str] = set()
        seen_content_hashes: Set[str] = set()
        seen_contents: List[str] = []
        doc_chunk_counts: Dict[int, int] = {}

        selected_items: List[ContextItem] = []
        duplicates_removed = 0
        diversity_filtered = 0
        budget_limited = 0
        min_score_filtered = 0

        current_total_chars = 0
        current_total_tokens = 0

        for r in reranked_results:
            # Check min score threshold
            if r.rerank_score < self.config.min_score_threshold:
                min_score_filtered += 1
                continue

            # Duplicate Check 1: Chunk ID
            if r.chunk_id in seen_chunk_ids:
                duplicates_removed += 1
                continue

            # Duplicate Check 2: Content Hash
            content_hash = hashlib.sha256(r.content.strip().encode("utf-8")).hexdigest()
            if content_hash in seen_content_hashes:
                duplicates_removed += 1
                continue

            # Duplicate Check 3: Near-duplicate text similarity
            is_near_dup = False
            for past_content in seen_contents:
                if self._is_near_duplicate(r.content, past_content):
                    is_near_dup = True
                    break
            if is_near_dup:
                duplicates_removed += 1
                continue

            # Diversity Control: Max chunks per document
            doc_id = r.document_id
            if doc_chunk_counts.get(doc_id, 0) >= limit_chunks_per_doc:
                diversity_filtered += 1
                continue

            # Budget Control: Max items
            if len(selected_items) >= limit_items:
                budget_limited += 1
                break

            # Budget Control: Character & Token budget
            item_chars = len(r.content)
            item_tokens = self._estimate_tokens(r.content)

            if current_total_chars + item_chars > limit_chars and len(selected_items) > 0:
                budget_limited += 1
                continue

            if current_total_tokens + item_tokens > self.config.max_tokens_estimate and len(selected_items) > 0:
                budget_limited += 1
                continue

            # Accept item
            seen_chunk_ids.add(r.chunk_id)
            seen_content_hashes.add(content_hash)
            seen_contents.append(r.content)
            doc_chunk_counts[doc_id] = doc_chunk_counts.get(doc_id, 0) + 1

            current_total_chars += item_chars
            current_total_tokens += item_tokens

            final_rank = len(selected_items) + 1
            selected_items.append(
                ContextItem(
                    rank=final_rank,
                    document_id=r.document_id,
                    chunk_id=r.chunk_id,
                    chunk_index=r.chunk_index,
                    text=r.content,
                    semantic_score=r.semantic_score,
                    rerank_score=r.rerank_score,
                    source=r.source_path,
                    document_title=r.document_title,
                    original_rank=r.original_rank,
                    metadata=r.metadata,
                    character_count=item_chars,
                    token_count_estimate=item_tokens,
                )
            )

        # 4. Generate LLM-ready Formatted Context String
        formatted_blocks: List[str] = []
        for item in selected_items:
            title_part = f"Document: {item.document_title}" if item.document_title else f"Document #{item.document_id}"
            source_part = f" | Source: {item.source}" if item.source else ""
            header = f"[{title_part}{source_part} | Chunk: {item.chunk_index} | Rerank Score: {item.rerank_score:.4f}]"
            formatted_blocks.append(f"{header}\n{item.text.strip()}")

        formatted_context = "\n\n---\n\n".join(formatted_blocks)

        t_assembly_ms = (time.perf_counter() - t_assembly_start) * 1000.0
        total_time_ms = (time.perf_counter() - start_time) * 1000.0

        metadata = ContextMetadata(
            candidate_count=candidate_count,
            selected_count=len(selected_items),
            duplicates_removed=duplicates_removed,
            diversity_filtered=diversity_filtered,
            budget_limited=budget_limited,
            min_score_filtered=min_score_filtered,
            total_characters=current_total_chars,
            total_tokens_estimated=current_total_tokens,
            retrieval_time_ms=t_retrieval_ms,
            reranking_time_ms=t_rerank_ms,
            assembly_time_ms=t_assembly_ms,
            total_time_ms=total_time_ms,
        )

        return AssembledContext(
            query=query,
            items=selected_items,
            metadata=metadata,
            formatted_context=formatted_context,
        )
