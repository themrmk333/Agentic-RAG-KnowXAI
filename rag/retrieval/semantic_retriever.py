"""Semantic vector retriever engine using PostgreSQL + pgvector and local BAAI/bge-small-en-v1.5 embeddings."""

from __future__ import annotations

import logging
import time
from typing import Any, Dict, List, Optional, Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from agents.rag.interface import RAGRetriever
from database.connection import SessionLocal
from database.models import Document, DocumentChunk
from database.vector_store import PGVectorStore
from rag.retrieval.models import RetrievalResponse, RetrievalResult
from rag.retrieval.query_embedder import QueryEmbedder

logger = logging.getLogger(__name__)

MAX_TOP_K = 100


class SemanticRetriever(RAGRetriever):
    """Production-grade semantic retrieval engine.
    
    Translates search queries into 384-dimensional dense vectors via QueryEmbedder,
    performs HNSW-accelerated cosine vector similarity search on PostgreSQL,
    and returns rich structured results linked to parent documents.
    """

    def __init__(
        self,
        embedder: Optional[QueryEmbedder] = None,
        session_factory=SessionLocal,
        vector_store: Optional[PGVectorStore] = None,
    ) -> None:
        self.embedder = embedder or QueryEmbedder.get_instance()
        self.session_factory = session_factory
        self.vector_store = vector_store or PGVectorStore(session_factory=session_factory)

    def _session(self) -> Session:
        return self.session_factory()

    def validate_top_k(self, top_k: Any) -> int:
        """Validate that top_k is a positive integer within allowable range."""
        if top_k is None or isinstance(top_k, bool) or not isinstance(top_k, int):
            raise TypeError(f"top_k must be a positive integer, got {type(top_k).__name__} ({top_k!r})")
        if top_k < 1:
            raise ValueError(f"top_k must be at least 1, got {top_k}")
        if top_k > MAX_TOP_K:
            logger.warning("top_k (%d) exceeds max (%d); capping to %d", top_k, MAX_TOP_K, MAX_TOP_K)
            return MAX_TOP_K
        return top_k

    def check_document_access(self, metadata: Optional[Dict[str, Any]], user_context: Optional[Dict[str, Any]]) -> bool:
        """Evaluate access permissions for a chunk/document based on enterprise security policy.
        
        Rules:
          - Public / non-restricted documents are accessible to all.
          - Restricted documents require a valid user_context.
          - Admin and Management roles have global read access.
          - Department-restricted documents require matching user department.
        """
        if not metadata:
            return True

        access_level = str(metadata.get("access_level", "employee")).lower().strip()

        # If document is not restricted, accessible to all employees by default
        if access_level != "restricted":
            return True

        # Restricted documents require user context
        if not user_context:
            return False

        user_role = str(user_context.get("role", "Employee")).lower().strip()
        user_dept = str(user_context.get("department", "")).lower().strip()

        # Global access for Admin / Management
        if user_role in ("admin", "management") or user_dept == "management":
            return True

        allowed_depts = metadata.get("allowed_departments", [])
        if isinstance(allowed_depts, str):
            allowed_depts = [allowed_depts]

        def clean_dept(dept: str) -> str:
            d = dept.lower().strip()
            for suffix in [" support", " department", " & claims"]:
                d = d.replace(suffix, "")
            return d.strip()

        user_dept_clean = clean_dept(user_dept)
        for dept in allowed_depts:
            if clean_dept(str(dept)) == user_dept_clean:
                return True

        return False

    def retrieve_results(
        self,
        query: str,
        top_k: int = 5,
        document_id: Optional[int] = None,
        metadata_filter: Optional[Dict[str, Any]] = None,
        user_context: Optional[Dict[str, Any]] = None,
    ) -> List[RetrievalResult]:
        """Perform semantic search and return structured RetrievalResult objects.
        
        Args:
            query: Natural language query string.
            top_k: Number of top results to retrieve (must be >= 1).
            document_id: Optional parent document ID filter.
            metadata_filter: Optional JSON metadata containment filter.
            user_context: Optional user credentials/department for permission filtering.
            
        Returns:
            List[RetrievalResult] ordered by ascending cosine distance (most relevant first).
        """
        validated_top_k = self.validate_top_k(top_k)
        query_vector = self.embedder.embed_query(query)

        # Over-fetch when access control filtering is requested to ensure top_k items are returned
        fetch_limit = validated_top_k * 4 if user_context is not None else validated_top_k

        try:
            with self._session() as session:
                distance_expr = DocumentChunk.embedding.cosine_distance(query_vector).label("distance")
                stmt = (
                    select(DocumentChunk, Document, distance_expr)
                    .join(Document, DocumentChunk.document_id == Document.id, isouter=True)
                    .where(DocumentChunk.embedding.is_not(None))
                )

                if document_id is not None:
                    stmt = stmt.where(DocumentChunk.document_id == document_id)

                if metadata_filter:
                    stmt = stmt.where(DocumentChunk.chunk_metadata.contains(metadata_filter))

                stmt = stmt.order_by("distance").limit(fetch_limit)
                rows = session.execute(stmt).all()

        except Exception as e:
            logger.error("Database query failure during semantic vector search: %s", e)
            raise RuntimeError(f"Database vector retrieval failed: {e}") from e

        results: List[RetrievalResult] = []
        for chunk, doc, dist in rows:
            dist_val = float(dist)
            sim_score = max(0.0, 1.0 - dist_val)
            meta = chunk.chunk_metadata or {}

            # Permission check
            if user_context is not None and not self.check_document_access(meta, user_context):
                continue

            chunk_cid = meta.get("chunk_id") or f"chunk_{chunk.document_id}_{chunk.chunk_index}"
            doc_title = doc.title if doc else meta.get("title")
            src_path = doc.source_path if doc else meta.get("source_file") or meta.get("relative_path")
            c_type = doc.content_type if doc else meta.get("document_type")

            results.append(
                RetrievalResult(
                    chunk_id=str(chunk_cid),
                    document_id=chunk.document_id,
                    chunk_index=chunk.chunk_index,
                    content=chunk.content,
                    distance=dist_val,
                    similarity_score=sim_score,
                    document_title=doc_title,
                    source_path=src_path,
                    content_type=c_type,
                    metadata=meta,
                )
            )

            if len(results) >= validated_top_k:
                break

        return results[:validated_top_k]

    def retrieve_response(
        self,
        query: str,
        top_k: int = 5,
        document_id: Optional[int] = None,
        metadata_filter: Optional[Dict[str, Any]] = None,
        user_context: Optional[Dict[str, Any]] = None,
    ) -> RetrievalResponse:
        """Perform semantic retrieval and return a complete RetrievalResponse with timing stats."""
        validated_top_k = self.validate_top_k(top_k)
        total_start = time.perf_counter()

        # Measure embedding time
        embed_start = time.perf_counter()
        query_vector = self.embedder.embed_query(query)
        embedding_time_ms = (time.perf_counter() - embed_start) * 1000.0

        # Measure database retrieval time
        db_start = time.perf_counter()
        results = self.retrieve_results(
            query=query,
            top_k=validated_top_k,
            document_id=document_id,
            metadata_filter=metadata_filter,
            user_context=user_context,
        )
        retrieval_time_ms = (time.perf_counter() - db_start) * 1000.0
        total_time_ms = (time.perf_counter() - total_start) * 1000.0

        return RetrievalResponse(
            query=query,
            top_k=validated_top_k,
            results=results,
            total_results=len(results),
            embedding_time_ms=embedding_time_ms,
            retrieval_time_ms=retrieval_time_ms,
            total_time_ms=total_time_ms,
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        user_context: Optional[Dict[str, Any]] = None,
        stats: Optional[Dict[str, Any]] = None,
        intent: Optional[str] = None,
    ) -> List[str]:
        """Protocol implementation of RAGRetriever.retrieve returning list of text content strings."""
        if not isinstance(query, str) or not query.strip() or top_k <= 0:
            if stats is not None:
                stats["retrieved_count"] = 0
                stats["authorized_count"] = 0
            return []

        # Over-fetch for deduplication and intent filtering
        raw_candidates = self.retrieve_results(
            query=query,
            top_k=max(15, top_k * 3),
            user_context=user_context,
        )

        # Optional intent-based keyword/metadata filtering for domain relevance
        if intent:
            intent_lower = intent.lower().strip()
            intent_matched: List[RetrievalResult] = []
            for r in raw_candidates:
                content_lower = r.content.lower()
                doc_dept = str(r.metadata.get("department", "")).lower()
                is_match = False
                if intent_lower == "finance":
                    is_match = any(x in doc_dept or x in content_lower for x in ["finance", "expense", "reimbursement", "claim", "payment", "billing", "invoice"])
                elif intent_lower == "hr":
                    is_match = any(x in doc_dept or x in content_lower for x in ["hr", "human resources", "leave", "attendance", "benefits", "policy", "handbook"])
                elif intent_lower == "it":
                    is_match = any(x in doc_dept or x in content_lower for x in ["it", "wi-fi", "wifi", "vpn", "laptop", "printer", "credentials", "support", "password"])
                elif intent_lower == "project":
                    is_match = any(x in doc_dept or x in content_lower for x in ["project", "sop", "sophia", "creation procedure"])
                else:
                    is_match = True

                if is_match:
                    intent_matched.append(r)

            # Do not fallback to all documents if we strictly filtered by intent.
            # Returning irrelevant cross-domain documents causes hallucination.
            candidates = intent_matched
        else:
            candidates = raw_candidates

        from rag.context.context_assembler import ContextAssembler
        assembler = ContextAssembler(retriever=self)
        
        assembled = assembler.assemble(
            query=query,
            candidates=candidates,
            user_context=user_context,
            max_context_items=top_k
        )

        if stats is not None:
            stats["retrieved_count"] = len(raw_candidates)
            stats["authorized_count"] = assembled.metadata.selected_count

        formatted_blocks = []
        for item in assembled.items:
            title_part = f"Document: {item.document_title}" if item.document_title else f"Document #{item.document_id}"
            source_part = f" | Source: {item.source}" if item.source else ""
            header = f"[{title_part}{source_part} | Chunk: {item.chunk_index} | Rerank Score: {item.rerank_score:.4f}]"
            formatted_blocks.append(f"{header}\n{item.text.strip()}")

        return formatted_blocks

    def retrieve_with_metadata(
        self,
        query: str,
        top_k: int = 5,
        user_context: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """Retrieve results formatted as dictionary items with content, metadata, distance, and similarity."""
        if not isinstance(query, str) or not query.strip() or top_k <= 0:
            return []

        results = self.retrieve_results(query=query, top_k=top_k, user_context=user_context)
        return [
            {
                "content": r.content,
                "metadata": r.metadata,
                "distance": r.distance,
                "similarity_score": r.similarity_score,
                "document_id": r.document_id,
                "document_title": r.document_title,
                "chunk_index": r.chunk_index,
                "chunk_id": r.chunk_id,
                "source_path": r.source_path,
            }
            for r in results
        ]
