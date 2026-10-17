"""Step 6 Unit and Integration Tests for Semantic Vector Retrieval Engine."""

from __future__ import annotations

import math
from typing import Any, Dict, List
import pytest
from sqlalchemy import func, select, text

from database.connection import SessionLocal, engine
from database.models import Document, DocumentChunk
from rag.embeddings.models import validate_vector
from rag.retrieval.models import RetrievalResponse, RetrievalResult
from rag.retrieval.query_embedder import QueryEmbedder
from rag.retrieval.semantic_retriever import SemanticRetriever


@pytest.fixture(scope="module")
def embedder() -> QueryEmbedder:
    """Fixture providing a shared QueryEmbedder instance."""
    return QueryEmbedder.get_instance()


@pytest.fixture(scope="module")
def retriever(embedder: QueryEmbedder) -> SemanticRetriever:
    """Fixture providing a SemanticRetriever instance."""
    return SemanticRetriever(embedder=embedder)


# ============================================================
# 1. Query Validation
# ============================================================
def test_01_query_validation(embedder: QueryEmbedder):
    """Verify safe query validation accepts valid strings and handles long queries."""
    valid_query = "What is the annual leave policy?"
    cleaned = embedder.validate_query_text(valid_query)
    assert cleaned == valid_query

    # Long query handling
    long_query = "leave " * 1000
    cleaned_long = embedder.validate_query_text(long_query)
    assert len(cleaned_long) <= 4096

    # Non-string types must raise TypeError
    with pytest.raises(TypeError):
        embedder.validate_query_text(None)  # type: ignore

    with pytest.raises(TypeError):
        embedder.validate_query_text(12345)  # type: ignore

    with pytest.raises(TypeError):
        embedder.validate_query_text(["query"])  # type: ignore


# ============================================================
# 2. Empty Query Handling
# ============================================================
def test_02_empty_and_whitespace_query_handling(embedder: QueryEmbedder, retriever: SemanticRetriever):
    """Verify empty and whitespace queries are rejected cleanly."""
    with pytest.raises(ValueError, match="empty or contain only whitespace"):
        embedder.validate_query_text("")

    with pytest.raises(ValueError, match="empty or contain only whitespace"):
        embedder.validate_query_text("   \n\t  ")

    with pytest.raises(ValueError):
        embedder.embed_query("")

    # Retriever protocol retrieve should safely return empty list for empty/whitespace query
    assert retriever.retrieve("") == []
    assert retriever.retrieve("   ") == []
    assert retriever.retrieve_with_metadata("") == []


# ============================================================
# 3. Query Embedding Generation
# ============================================================
def test_03_query_embedding_generation(embedder: QueryEmbedder):
    """Verify local BAAI/bge-small-en-v1.5 model produces valid float vectors."""
    query = "cybersecurity incident reporting procedure"
    vec = embedder.embed_query(query)
    assert isinstance(vec, list)
    assert len(vec) == 384
    assert all(isinstance(x, float) for x in vec)


# ============================================================
# 4. Query Vector Dimension = 384
# ============================================================
def test_04_query_vector_dimension(embedder: QueryEmbedder):
    """Verify query vector dimension is strictly 384."""
    assert embedder.dimensions == 384
    vec = embedder.embed_query("expense reimbursement guidelines")
    assert len(vec) == 384


# ============================================================
# 5. Invalid Vector Detection
# ============================================================
def test_05_invalid_vector_detection():
    """Verify validate_vector rejects dimension mismatches, NaNs, and Infs."""
    # Dimension mismatch
    ok, msg = validate_vector([0.1] * 128, expected_dim=384)
    assert not ok
    assert "Dimension mismatch" in msg

    # NaN detection
    bad_nan = [0.1] * 384
    bad_nan[10] = float("nan")
    ok, msg = validate_vector(bad_nan, expected_dim=384)
    assert not ok
    assert "NaN" in msg

    # Inf detection
    bad_inf = [0.1] * 384
    bad_inf[50] = float("inf")
    ok, msg = validate_vector(bad_inf, expected_dim=384)
    assert not ok
    assert "Infinity" in msg

    # Non-numeric
    bad_type = [0.1] * 384
    bad_type[0] = "string"  # type: ignore
    ok, msg = validate_vector(bad_type, expected_dim=384)
    assert not ok
    assert "Non-numeric" in msg


# ============================================================
# 6. PostgreSQL Connection & pgvector Extension
# ============================================================
def test_06_database_connectivity_and_extension():
    """Verify database connection and pgvector extension version."""
    with engine.connect() as conn:
        ver = conn.execute(text("SELECT version();")).scalar()
        assert ver is not None
        assert "PostgreSQL" in ver

        ext_ver = conn.execute(text("SELECT extversion FROM pg_extension WHERE extname = 'vector';")).scalar()
        assert ext_ver is not None
        assert ext_ver == "0.8.2"


# ============================================================
# 7. pgvector Cosine Search
# ============================================================
def test_07_pgvector_cosine_search(retriever: SemanticRetriever):
    """Verify pgvector cosine distance search executes against PostgreSQL."""
    query = "employee health insurance benefits"
    results = retriever.retrieve_results(query=query, top_k=5)
    assert len(results) == 5
    for r in results:
        assert isinstance(r, RetrievalResult)
        assert r.chunk_id is not None
        assert r.document_id > 0
        assert len(r.content) > 0
        assert r.distance >= 0.0


# ============================================================
# 8. Top-K Retrieval Behavior
# ============================================================
def test_08_top_k_behavior(retriever: SemanticRetriever):
    """Verify configurable top_k returns exact requested count up to available chunks."""
    query = "travel expense reimbursement workflow"

    # top_k = 1
    res_1 = retriever.retrieve_results(query, top_k=1)
    assert len(res_1) == 1

    # top_k = 3
    res_3 = retriever.retrieve_results(query, top_k=3)
    assert len(res_3) == 3

    # top_k = 10
    res_10 = retriever.retrieve_results(query, top_k=10)
    assert len(res_10) == 10

    # Invalid top_k validation
    with pytest.raises(TypeError):
        retriever.retrieve_results(query, top_k="five")  # type: ignore

    with pytest.raises(TypeError):
        retriever.retrieve_results(query, top_k=True)  # type: ignore

    with pytest.raises(ValueError):
        retriever.retrieve_results(query, top_k=0)

    with pytest.raises(ValueError):
        retriever.retrieve_results(query, top_k=-5)


# ============================================================
# 9. Result Ordering (Most Relevant First)
# ============================================================
def test_09_result_ordering(retriever: SemanticRetriever):
    """Verify results are strictly ordered with ascending cosine distance (descending similarity)."""
    query = "workstation VPN setup and multi-factor authentication"
    results = retriever.retrieve_results(query=query, top_k=10)
    assert len(results) > 1

    for i in range(len(results) - 1):
        # Cosine distance must be non-decreasing
        assert results[i].distance <= results[i + 1].distance
        # Similarity score must be non-increasing
        assert results[i].similarity_score >= results[i + 1].similarity_score


# ============================================================
# 10. Result Schema & Typing
# ============================================================
def test_10_result_schema(retriever: SemanticRetriever):
    """Verify structured result contains all required fields with proper types."""
    query = "remote work policy eligibility"
    response = retriever.retrieve_response(query=query, top_k=3)

    assert isinstance(response, RetrievalResponse)
    assert response.query == query
    assert response.top_k == 3
    assert response.total_results == 3
    assert response.embedding_time_ms > 0
    assert response.retrieval_time_ms > 0
    assert response.total_time_ms > 0

    first = response.results[0]
    assert isinstance(first.chunk_id, str)
    assert isinstance(first.document_id, int)
    assert isinstance(first.chunk_index, int)
    assert isinstance(first.content, str)
    assert isinstance(first.distance, float)
    assert isinstance(first.similarity_score, float)
    assert isinstance(first.metadata, dict)
    assert "chunk_id" in first.metadata

    # to_dict verification
    d = first.to_dict()
    assert "chunk_id" in d
    assert "document_id" in d
    assert "distance" in d
    assert "similarity_score" in d


# ============================================================
# 11. Document and Chunk Relationship Mapping
# ============================================================
def test_11_document_chunk_relationship(retriever: SemanticRetriever):
    """Verify retrieved chunks remain correctly linked to their parent documents in PostgreSQL."""
    query = "parental leave and maternity benefits"
    results = retriever.retrieve_results(query=query, top_k=5)

    with SessionLocal() as session:
        for r in results:
            doc = session.execute(select(Document).where(Document.id == r.document_id)).scalar_one_or_none()
            assert doc is not None
            assert doc.id == r.document_id
            if r.document_title:
                assert r.document_title == doc.title


# ============================================================
# 12. Score and Distance Validity
# ============================================================
def test_12_score_and_distance_validity(retriever: SemanticRetriever):
    """Verify distance values are in valid cosine range [0, 2] and similarities are [0, 1]."""
    query = "fire safety and emergency evacuation plan"
    results = retriever.retrieve_results(query=query, top_k=5)

    for r in results:
        assert 0.0 <= r.distance <= 2.0
        assert 0.0 <= r.similarity_score <= 1.0
        # Check similarity formula: similarity = max(0.0, 1.0 - distance)
        expected_sim = max(0.0, 1.0 - r.distance)
        assert math.isclose(r.similarity_score, expected_sim, abs_tol=1e-6)


# ============================================================
# 13. Edge Cases: Long Queries and Intent Filtering
# ============================================================
def test_13_edge_cases_and_filters(retriever: SemanticRetriever):
    """Verify long queries and intent/permission filtering behave correctly."""
    # Long query
    long_q = "What is the procedure for requesting a new developer laptop and configuring SSH keys? " * 5
    res = retriever.retrieve_results(long_q, top_k=3)
    assert len(res) == 3

    # Protocol retrieve with admin context
    admin_ctx = {"role": "Admin", "department": "Management"}
    passages = retriever.retrieve("executive board meeting schedule", top_k=3, user_context=admin_ctx)
    assert len(passages) <= 3

    # Protocol retrieve with stats
    stats: Dict[str, Any] = {}
    passages = retriever.retrieve("annual bonus structure", top_k=3, stats=stats)
    assert "retrieved_count" in stats
    assert "authorized_count" in stats


# ============================================================
# 14. Database Read-Only Verification
# ============================================================
def test_14_database_read_only(retriever: SemanticRetriever):
    """Verify retrieval operations perform no INSERT, UPDATE, or DELETE mutations."""
    with SessionLocal() as session:
        doc_count_before = session.execute(select(func.count(Document.id))).scalar()
        chunk_count_before = session.execute(select(func.count(DocumentChunk.id))).scalar()

    # Perform multiple retrieval queries
    retriever.retrieve_results("data retention policy", top_k=5)
    retriever.retrieve_results("code review standards", top_k=5)
    retriever.retrieve_results("employee onboarding checklist", top_k=5)

    with SessionLocal() as session:
        doc_count_after = session.execute(select(func.count(Document.id))).scalar()
        chunk_count_after = session.execute(select(func.count(DocumentChunk.id))).scalar()

    assert doc_count_before == doc_count_after == 3897
    assert chunk_count_before == chunk_count_after == 12730


# ============================================================
# 15. HNSW Index Verification
# ============================================================
def test_15_hnsw_index_verification():
    """Verify ix_document_chunks_embedding_cosine exists and uses HNSW with vector_cosine_ops."""
    with engine.connect() as conn:
        indexes = conn.execute(text("""
            SELECT indexname, indexdef 
            FROM pg_indexes 
            WHERE tablename = 'document_chunks' AND indexname = 'ix_document_chunks_embedding_cosine';
        """)).fetchall()

        assert len(indexes) == 1
        idx_def = indexes[0][1].lower()
        assert "hnsw" in idx_def
        assert "vector_cosine_ops" in idx_def
        assert "embedding" in idx_def


# ============================================================
# 16. Database Integrity Regression Counts
# ============================================================
def test_16_database_integrity_regression_counts():
    """Verify exact counts: 3897 documents, 12730 chunks, 12730 embeddings, 0 missing."""
    with SessionLocal() as session:
        doc_count = session.execute(select(func.count(Document.id))).scalar()
        chunk_count = session.execute(select(func.count(DocumentChunk.id))).scalar()
        embedding_count = session.execute(
            select(func.count(DocumentChunk.id)).where(DocumentChunk.embedding.is_not(None))
        ).scalar()
        missing_count = session.execute(
            select(func.count(DocumentChunk.id)).where(DocumentChunk.embedding.is_(None))
        ).scalar()

        assert doc_count == 3897
        assert chunk_count == 12730
        assert embedding_count == 12730
        assert missing_count == 0
