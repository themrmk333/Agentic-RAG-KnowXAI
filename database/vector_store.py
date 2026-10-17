from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from sqlalchemy import select
from sqlalchemy.orm import Session

from .connection import SessionLocal
from .models import DocumentChunk, DocumentEmbedding


class PGVectorStore:
    """A PostgreSQL + pgvector storage wrapper for RAG embeddings."""

    def __init__(self, session_factory=SessionLocal, dimensions: Optional[int] = None):
        self.session_factory = session_factory
        if dimensions is None:
            try:
                from config.settings import get_settings
                self.dimensions = get_settings().pgvector_dimensions
            except Exception:
                self.dimensions = 384
        else:
            self.dimensions = dimensions

    def _session(self) -> Session:
        return self.session_factory()

    def _validate_embedding(self, embedding: Sequence[float]) -> list[float]:
        values = list(embedding)
        if len(values) != self.dimensions:
            raise ValueError("Embedding dimension does not match PGVECTOR_DIMENSIONS")
        return values

    def add_document_embedding(
        self,
        document_id: int,
        embedding: Sequence[float],
        metadata: Optional[Dict[str, Any]] = None,
        embedding_type: str = "document",
    ) -> DocumentEmbedding:
        metadata = metadata or {}
        values = self._validate_embedding(embedding)
        with self._session() as session:
            item = DocumentEmbedding(
                document_id=document_id,
                embedding_type=embedding_type,
                embedding_metadata=metadata,
                embedding=values,
            )
            session.add(item)
            session.commit()
            session.refresh(item)
            return item

    def add_chunk(
        self,
        document_id: int,
        chunk_index: int,
        content: str,
        embedding: Sequence[float],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> DocumentChunk:
        metadata = metadata or {}
        values = self._validate_embedding(embedding)
        with self._session() as session:
            item = DocumentChunk(
                document_id=document_id,
                chunk_index=chunk_index,
                content=content,
                chunk_metadata=metadata,
                embedding=values,
            )
            session.add(item)
            session.commit()
            session.refresh(item)
            return item

    def add_chunks(
        self,
        document_id: int,
        chunks: Sequence[
            Tuple[int, str, Sequence[float], Optional[Dict[str, Any]]]
        ],
    ) -> int:
        items = []
        for chunk_index, content, embedding, metadata in chunks:
            metadata = metadata or {}
            values = self._validate_embedding(embedding)
            item = DocumentChunk(
                document_id=document_id,
                chunk_index=chunk_index,
                content=content,
                chunk_metadata=metadata,
                embedding=values,
            )
            items.append(item)
        if not items:
            return 0
        with self._session() as session:
            session.add_all(items)
            session.commit()
            return len(items)

    def similarity_search(
        self,
        query_vector: Sequence[float],
        limit: int = 10,
        document_id: Optional[int] = None,
        metadata_filter: Optional[Dict[str, Any]] = None,
    ) -> List[DocumentChunk]:
        with self._session() as session:
            stmt = select(DocumentChunk).where(DocumentChunk.embedding.is_not(None))
            if document_id is not None:
                stmt = stmt.where(DocumentChunk.document_id == document_id)
            if metadata_filter:
                stmt = stmt.where(DocumentChunk.chunk_metadata.contains(metadata_filter))
            stmt = stmt.order_by(DocumentChunk.embedding.cosine_distance(list(query_vector))).limit(limit)
            return list(session.execute(stmt).scalars().all())

    def similarity_search_with_scores(
        self,
        query_vector: Sequence[float],
        limit: int = 10,
        document_id: Optional[int] = None,
        metadata_filter: Optional[Dict[str, Any]] = None,
    ) -> List[Tuple[DocumentChunk, float]]:
        with self._session() as session:
            stmt = select(DocumentChunk, DocumentChunk.embedding.cosine_distance(list(query_vector)).label("distance")).where(DocumentChunk.embedding.is_not(None))
            if document_id is not None:
                stmt = stmt.where(DocumentChunk.document_id == document_id)
            if metadata_filter:
                stmt = stmt.where(DocumentChunk.chunk_metadata.contains(metadata_filter))
            stmt = stmt.order_by("distance").limit(limit)
            rows = session.execute(stmt).all()
            return [(chunk, float(distance)) for chunk, distance in rows]

    def search_document_embeddings(
        self,
        query_vector: Sequence[float],
        limit: int = 5,
        metadata_filter: Optional[Dict[str, Any]] = None,
    ) -> List[Tuple[DocumentEmbedding, float]]:
        with self._session() as session:
            stmt = select(DocumentEmbedding, DocumentEmbedding.embedding.cosine_distance(list(query_vector)).label("distance")).where(DocumentEmbedding.embedding.is_not(None))
            if metadata_filter:
                stmt = stmt.where(DocumentEmbedding.embedding_metadata.contains(metadata_filter))
            stmt = stmt.order_by("distance").limit(limit)
            rows = session.execute(stmt).all()
            return [(item, float(distance)) for item, distance in rows]

    def delete_document(self, document_id: int) -> None:
        with self._session() as session:
            session.query(DocumentChunk).filter(DocumentChunk.document_id == document_id).delete()
            session.query(DocumentEmbedding).filter(DocumentEmbedding.document_id == document_id).delete()
            session.commit()


vector_store = PGVectorStore()
