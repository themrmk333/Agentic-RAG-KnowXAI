"""Deterministic local multi-factor reranker for retrieved candidate chunks."""

from __future__ import annotations

import logging
import math
import re
import unicodedata
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Set

from rag.context.models import RerankedResult
from rag.retrieval.models import RetrievalResult

logger = logging.getLogger(__name__)

# Common English stopwords to de-emphasize during lexical matching
STOP_WORDS: Set[str] = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
    "any", "are", "as", "at", "be", "because", "been", "before", "being", "below",
    "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down",
    "during", "each", "few", "for", "from", "further", "had", "has", "have",
    "having", "he", "her", "here", "hers", "herself", "him", "himself", "his",
    "how", "i", "if", "in", "into", "is", "it", "its", "itself", "just", "me",
    "more", "most", "my", "myself", "no", "nor", "not", "of", "off", "on", "once",
    "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own",
    "same", "she", "should", "so", "some", "such", "than", "that", "the", "their",
    "theirs", "them", "themselves", "then", "there", "these", "they", "this",
    "those", "through", "to", "too", "under", "until", "up", "very", "was", "we",
    "were", "what", "when", "where", "which", "while", "who", "whom", "why", "with",
    "would", "you", "your", "yours", "yourself", "yourselves",
}


@dataclass
class RerankerConfig:
    """Configuration for multi-factor reranker scoring weights and thresholds."""

    semantic_weight: float = 0.50
    lexical_weight: float = 0.30
    phrase_weight: float = 0.15
    quality_weight: float = 0.05
    min_score_threshold: float = 0.15
    max_query_length: int = 4096

    def __post_init__(self) -> None:
        total_weight = (
            self.semantic_weight
            + self.lexical_weight
            + self.phrase_weight
            + self.quality_weight
        )
        if not math.isclose(total_weight, 1.0, rel_tol=1e-3):
            # Normalize weights to sum to 1.0 if not exactly 1.0
            if total_weight > 0:
                self.semantic_weight /= total_weight
                self.lexical_weight /= total_weight
                self.phrase_weight /= total_weight
                self.quality_weight /= total_weight


class ContextReranker:
    """Production-grade deterministic local context reranker.
    
    Combines:
      1. Step 6 Dense Semantic Similarity (from BAAI/bge-small-en-v1.5)
      2. Lexical / Keyword BM25-style Term Match
      3. Exact Phrase and Multi-word Match
      4. Chunk Structure & Quality Signals
    """

    def __init__(self, config: Optional[RerankerConfig] = None) -> None:
        self.config = config or RerankerConfig()

    def normalize_query(self, query: str) -> str:
        """Normalize query string: strip extra spaces, normalize unicode, truncate if overly long."""
        if query is None:
            raise TypeError("Query cannot be None")
        if not isinstance(query, str):
            raise TypeError(f"Query must be a string, got {type(query).__name__}")

        # Unicode normalization (NFKC)
        normalized = unicodedata.normalize("NFKC", query)
        # Collapse multiple whitespace characters
        cleaned = re.sub(r"\s+", " ", normalized).strip()

        if not cleaned:
            raise ValueError("Query cannot be empty or contain only whitespace")

        if len(cleaned) > self.config.max_query_length:
            cleaned = cleaned[:self.config.max_query_length].strip()

        return cleaned

    def tokenize(self, text: str) -> List[str]:
        """Extract alphanumeric token sequence, lowercased."""
        return [t.lower() for t in re.findall(r"\b\w+\b", text) if t]

    def extract_keywords(self, text: str) -> Set[str]:
        """Extract informative query keywords (excluding common stopwords)."""
        tokens = self.tokenize(text)
        keywords = {t for t in tokens if len(t) > 1 and t not in STOP_WORDS}
        return keywords if keywords else set(tokens)

    def calculate_lexical_score(self, query: str, candidate: RetrievalResult) -> float:
        """Calculate lexical overlap between query keywords and candidate content/metadata."""
        query_keywords = self.extract_keywords(query)
        if not query_keywords:
            return 0.0

        content_lower = candidate.content.lower()
        title_lower = (candidate.document_title or "").lower()
        meta = candidate.metadata or {}
        meta_text = " ".join(
            str(v).lower() for k, v in meta.items()
            if isinstance(v, (str, int, float)) and k not in ("chunk_id", "source_sha256", "chunk_sha256")
        )

        full_searchable = f"{title_lower} {meta_text} {content_lower}"
        content_tokens = self.tokenize(full_searchable)
        if not content_tokens:
            return 0.0

        token_counts: Dict[str, int] = {}
        for token in content_tokens:
            token_counts[token] = token_counts.get(token, 0) + 1

        matched_count = 0
        total_tf_weight = 0.0

        for kw in query_keywords:
            tf = token_counts.get(kw, 0)
            if tf > 0:
                matched_count += 1
                # Sublinear term frequency scaling
                total_tf_weight += math.log1p(tf)
                # Extra boost if term appears in title
                if kw in title_lower:
                    total_tf_weight += 0.5

        coverage_ratio = matched_count / len(query_keywords)
        # Combine coverage and frequency
        score = 0.6 * coverage_ratio + 0.4 * min(1.0, total_tf_weight / (len(query_keywords) * 2.0))
        return min(1.0, max(0.0, score))

    def calculate_phrase_score(self, query: str, candidate: RetrievalResult) -> float:
        """Calculate exact phrase and n-gram sequence match score."""
        cleaned_query = re.sub(r"[^\w\s]", " ", query.lower()).strip()
        query_words = cleaned_query.split()
        if len(query_words) < 2:
            # For single-word query, fallback to exact word match
            return 1.0 if query.lower() in candidate.content.lower() else 0.0

        content_lower = candidate.content.lower()
        title_lower = (candidate.document_title or "").lower()

        # 1. Exact full query match
        if cleaned_query in content_lower or cleaned_query in title_lower:
            return 1.0

        # 2. Multi-word n-gram matches (bigrams, trigrams)
        bigrams = [f"{query_words[i]} {query_words[i+1]}" for i in range(len(query_words) - 1)]
        matched_bigrams = sum(1 for bg in bigrams if bg in content_lower or bg in title_lower)
        bigram_ratio = matched_bigrams / len(bigrams) if bigrams else 0.0

        trigram_ratio = 0.0
        if len(query_words) >= 3:
            trigrams = [f"{query_words[i]} {query_words[i+1]} {query_words[i+2]}" for i in range(len(query_words) - 2)]
            matched_trigrams = sum(1 for tg in trigrams if tg in content_lower or tg in title_lower)
            trigram_ratio = matched_trigrams / len(trigrams) if trigrams else 0.0

        phrase_score = 0.6 * bigram_ratio + 0.4 * trigram_ratio
        return min(1.0, max(0.0, phrase_score))

    def calculate_quality_score(self, candidate: RetrievalResult) -> float:
        """Calculate chunk content quality based on length, structure, and metadata richness."""
        text_len = len(candidate.content.strip())
        if text_len == 0:
            return 0.0

        # Optimal length curve: 200 - 1500 chars is ideal
        if 200 <= text_len <= 1500:
            length_score = 1.0
        elif text_len < 200:
            length_score = max(0.2, text_len / 200.0)
        else:
            # Penalize excessively verbose chunks slightly
            length_score = max(0.7, 1.0 - (text_len - 1500) / 4000.0)

        # Structure indicators (headings, json, bullets, structured tables)
        structure_score = 0.5
        content = candidate.content
        if "```json" in content or "{" in content and "}" in content:
            structure_score += 0.3
        if "##" in content or "**" in content:
            structure_score += 0.2
        if candidate.document_title:
            structure_score += 0.1
        if candidate.metadata and len(candidate.metadata) > 3:
            structure_score += 0.1

        structure_score = min(1.0, structure_score)
        return 0.5 * length_score + 0.5 * structure_score

    def rerank_candidates(
        self,
        query: str,
        candidates: Sequence[RetrievalResult],
    ) -> List[RerankedResult]:
        """Rerank a sequence of Step 6 candidate results using multi-factor deterministic scoring.
        
        Args:
            query: User search query.
            candidates: Retrieved candidates from Step 6.
            
        Returns:
            List[RerankedResult] ordered deterministically by composite rerank_score DESC.
        """
        if not candidates:
            return []

        cleaned_query = self.normalize_query(query)
        reranked: List[RerankedResult] = []

        for original_idx, cand in enumerate(candidates, 1):
            # 1. Semantic score from Step 6
            sem_score = max(0.0, min(1.0, cand.similarity_score))

            # 2. Lexical score
            lex_score = self.calculate_lexical_score(cleaned_query, cand)

            # 3. Phrase match score
            phrase_score = self.calculate_phrase_score(cleaned_query, cand)

            # 4. Quality score
            qual_score = self.calculate_quality_score(cand)

            # Composite weighted score
            composite = (
                self.config.semantic_weight * sem_score
                + self.config.lexical_weight * lex_score
                + self.config.phrase_weight * phrase_score
                + self.config.quality_weight * qual_score
            )
            composite = round(min(1.0, max(0.0, composite)), 4)

            reranked.append(
                RerankedResult(
                    chunk_id=cand.chunk_id,
                    document_id=cand.document_id,
                    chunk_index=cand.chunk_index,
                    content=cand.content,
                    original_distance=cand.distance,
                    original_similarity_score=cand.similarity_score,
                    original_rank=original_idx,
                    semantic_score=sem_score,
                    lexical_score=round(lex_score, 4),
                    phrase_score=round(phrase_score, 4),
                    quality_score=round(qual_score, 4),
                    rerank_score=composite,
                    document_title=cand.document_title,
                    source_path=cand.source_path,
                    content_type=cand.content_type,
                    metadata=cand.metadata or {},
                )
            )

        # Deterministic sorting:
        # Primary: rerank_score DESC
        # Secondary: semantic_score DESC
        # Tertiary: original_rank ASC
        reranked.sort(
            key=lambda r: (-r.rerank_score, -r.semantic_score, r.original_rank)
        )

        return reranked
