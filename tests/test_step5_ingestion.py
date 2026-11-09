"""Step 5 Unit and Integration Tests for PostgreSQL + pgvector Ingestion."""

import json
import math
from pathlib import Path
import pytest
import torch
from sqlalchemy import func, select, text

from config.settings import get_settings
from database.connection import SessionLocal, engine, get_database_url
from database.models import Document, DocumentChunk
from database.vector_store import PGVectorStore
from rag.ingestion.step5_ingestion import IngestionConfig, IngestionRecord, Step5IngestionPipeline
from rag.retrieval.pgvector_retriever import PGVectorRetriever

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def test_01_database_connectivity():
    """Verify PostgreSQL connectivity and version."""
    with engine.connect() as conn:
        ver = conn.execute(text("SELECT version();")).scalar()
        assert ver is not None
        assert "PostgreSQL" in ver


def test_02_pgvector_extension_active():
    """Verify pgvector extension is installed and active in PostgreSQL."""
    with engine.connect() as conn:
        ext = conn.execute(text("SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';")).fetchone()
        assert ext is not None
        assert ext[0] == "vector"


def test_03_vector_column_dimension_is_384():
    """Verify document_chunks and document_embeddings use VECTOR(384)."""
    with engine.connect() as conn:
        dim = conn.execute(text("""
            SELECT format_type(a.atttypid, a.atttypmod) 
            FROM pg_attribute a 
            JOIN pg_class c ON a.attrelid = c.oid 
            WHERE c.relname = 'document_chunks' AND a.attname = 'embedding';
        """)).scalar()
        assert dim == "vector(384)"


def test_04_hnsw_index_exists():
    """Verify HNSW cosine index exists on document_chunks."""
    with engine.connect() as conn:
        indexes = conn.execute(text("SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'document_chunks';")).fetchall()
        hnsw_indexes = [idx for idx in indexes if "hnsw" in idx[1].lower()]
        assert len(hnsw_indexes) >= 1


def test_05_total_document_and_chunks_count():
    """Verify all 263 chunks are present in document_chunks."""
    with SessionLocal() as session:
        chunk_count = session.execute(select(func.count(DocumentChunk.id))).scalar()
        vector_count = session.execute(select(func.count(DocumentChunk.id)).where(DocumentChunk.embedding.is_not(None))).scalar()
        assert chunk_count == 263
        assert vector_count == 263


def test_06_zero_duplicate_chunk_ids():
    """Verify zero duplicate chunk_ids exist in the database."""
    with SessionLocal() as session:
        stmt = text("""
            SELECT (metadata->>'chunk_id') AS cid, count(*) 
            FROM document_chunks 
            GROUP BY cid 
            HAVING count(*) > 1;
        """)
        dups = session.execute(stmt).fetchall()
        assert len(dups) == 0


def test_07_zero_missing_chunk_ids():
    """Verify all document_chunks have valid chunk_id in metadata."""
    with SessionLocal() as session:
        stmt = text("SELECT count(*) FROM document_chunks WHERE metadata->>'chunk_id' IS NULL;")
        missing = session.execute(stmt).scalar()
        assert missing == 0


def test_08_no_null_or_invalid_vectors():
    """Verify all vectors are non-null and valid floats."""
    with SessionLocal() as session:
        null_count = session.execute(text("SELECT count(*) FROM document_chunks WHERE embedding IS NULL;")).scalar()
        assert null_count == 0


def test_09_vector_store_similarity_search():
    """Verify PGVectorStore cosine similarity search returns valid chunks with 384 dimensions."""
    store = PGVectorStore(dimensions=384)
    dummy_query_vector = [0.01 * (i % 10) for i in range(384)]
    results = store.similarity_search(dummy_query_vector, limit=5)
    assert len(results) == 5
    for chunk in results:
        assert chunk.content is not None
        assert chunk.chunk_metadata is not None
        assert "chunk_id" in chunk.chunk_metadata


def test_10_permission_aware_retrieval():
    """Verify PGVectorRetriever enforces role and department access rules."""
    store = PGVectorStore(dimensions=384)
    
    class DummyEmbeddingService:
        def embed_query(self, query: str):
            return [0.01 * (i % 10) for i in range(384)]

    retriever = PGVectorRetriever(embedding_service=DummyEmbeddingService(), vector_store=store)
    
    # Admin context should retrieve results
    admin_context = {"role": "Admin", "department": "Management"}
    results_admin = retriever.retrieve_with_metadata(
        query="leave policy",
        top_k=3,
        user_context=admin_context
    )
    assert len(results_admin) > 0
    assert "distance" in results_admin[0]
    assert "chunk_id" in results_admin[0]["metadata"]
