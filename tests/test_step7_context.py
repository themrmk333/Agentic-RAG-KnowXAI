"""Step 7 Unit and Integration Tests for Context Reranking and Assembly."""

from __future__ import annotations

import math
from typing import Any, Dict, List
import pytest
from sqlalchemy import func, select

from database.connection import SessionLocal
from database.models import Document, DocumentChunk
from rag.context.context_assembler import AssemblerConfig, ContextAssembler
from rag.context.models import AssembledContext, ContextItem, RerankedResult
from rag.context.reranker import ContextReranker, RerankerConfig
from rag.retrieval.models import RetrievalResult
from rag.retrieval.semantic_retriever import SemanticRetriever


@pytest.fixture(scope="module")
def retriever() -> SemanticRetriever:
    return SemanticRetriever()


@pytest.fixture(scope="module")
def reranker() -> ContextReranker:
    return ContextReranker()


@pytest.fixture(scope="module")
def assembler(retriever: SemanticRetriever, reranker: ContextReranker) -> ContextAssembler:
    return ContextAssembler(retriever=retriever, reranker=reranker)


# ============================================================
# 1. Normal Query Context Assembly End-to-End
# ============================================================
def test_01_normal_query_assembly(assembler: ContextAssembler):
    """Verify normal natural language query produces valid assembled context."""
    query = "What is the annual leave and sick leave policy?"
    context = assembler.assemble(query=query, max_context_items=3)

    assert isinstance(context, AssembledContext)
    assert context.query == query
    assert len(context.items) > 0
    assert len(context.items) <= 3
    assert context.metadata.candidate_count > 0
    assert context.metadata.selected_count == len(context.items)
    assert len(context.formatted_context) > 0

    first = context.items[0]
    assert first.rank == 1
    assert first.document_id > 0
    assert first.chunk_id is not None
    assert first.rerank_score > 0.0
    assert first.semantic_score > 0.0


# ============================================================
# 2. Empty Query Handling
# ============================================================
def test_02_empty_query_handling(assembler: ContextAssembler, reranker: ContextReranker):
    """Verify empty query string is handled safely without crashing."""
    with pytest.raises(ValueError):
        reranker.normalize_query("")

    context = assembler.assemble(query="")
    assert isinstance(context, AssembledContext)
    assert context.items == []
    assert context.metadata.selected_count == 0
    assert context.formatted_context == ""


# ============================================================
# 3. Whitespace-Only Query Handling
# ============================================================
def test_03_whitespace_query_handling(assembler: ContextAssembler, reranker: ContextReranker):
    """Verify whitespace-only queries are handled cleanly."""
    with pytest.raises(ValueError):
        reranker.normalize_query("   \n\t  ")

    context = assembler.assemble(query="   \t\n  ")
    assert isinstance(context, AssembledContext)
    assert context.items == []
    assert context.metadata.selected_count == 0


# ============================================================
# 4. Long Query Handling
# ============================================================
def test_04_long_query_handling(assembler: ContextAssembler, reranker: ContextReranker):
    """Verify excessively long queries are normalized safely without data loss or crash."""
    long_q = "What are the rules and guidelines for travel expense reimbursement and hotel allowance limits? " * 50
    normalized = reranker.normalize_query(long_q)
    assert len(normalized) <= 4096

    context = assembler.assemble(query=long_q, max_context_items=3)
    assert isinstance(context, AssembledContext)
    assert len(context.items) > 0


# ============================================================
# 5. Duplicate Chunk ID Removal
# ============================================================
def test_05_duplicate_chunk_id_removal(assembler: ContextAssembler):
    """Verify duplicate candidate chunks with the same chunk_id are eliminated."""
    candidate1 = RetrievalResult(
        chunk_id="chunk_dup_1",
        document_id=101,
        chunk_index=0,
        content="This is the corporate security and password policy.",
        distance=0.2,
        similarity_score=0.8,
        document_title="Security Policy",
    )
    candidate2 = RetrievalResult(
        chunk_id="chunk_dup_1",  # Duplicate chunk_id
        document_id=101,
        chunk_index=0,
        content="This is the corporate security and password policy.",
        distance=0.22,
        similarity_score=0.78,
        document_title="Security Policy",
    )

    context = assembler.assemble(
        query="corporate security password policy",
        candidates=[candidate1, candidate2],
        max_context_items=5,
    )

    assert context.metadata.candidate_count == 2
    assert context.metadata.selected_count == 1
    assert context.metadata.duplicates_removed == 1
    assert len(context.items) == 1
    assert context.items[0].chunk_id == "chunk_dup_1"


# ============================================================
# 6. Duplicate Text / Near-Duplicate Handling
# ============================================================
def test_06_duplicate_text_handling(assembler: ContextAssembler):
    """Verify candidate chunks with identical or near-identical text are deduplicated."""
    candidate1 = RetrievalResult(
        chunk_id="chunk_a",
        document_id=101,
        chunk_index=0,
        content="Employees must submit travel expenses within 30 days of trip completion via the finance portal.",
        distance=0.15,
        similarity_score=0.85,
    )
    candidate2 = RetrievalResult(
        chunk_id="chunk_b",
        document_id=102,
        chunk_index=0,
        content="Employees must submit travel expenses within 30 days of trip completion via the finance portal.",  # Exact same text
        distance=0.18,
        similarity_score=0.82,
    )

    context = assembler.assemble(
        query="travel expenses submit finance portal",
        candidates=[candidate1, candidate2],
        max_context_items=5,
    )

    assert context.metadata.selected_count == 1
    assert context.metadata.duplicates_removed == 1


# ============================================================
# 7. Deterministic Reranking
# ============================================================
def test_07_deterministic_reranking(reranker: ContextReranker):
    """Verify identical candidate sequences and queries produce identical reranked scores and order."""
    candidates = [
        RetrievalResult(
            chunk_id=f"chunk_{i}",
            document_id=i,
            chunk_index=0,
            content=f"Policy chunk details regarding employee benefits and annual leave package #{i}.",
            distance=0.2 + (i * 0.05),
            similarity_score=0.8 - (i * 0.05),
            document_title=f"Doc Title {i}",
        )
        for i in range(5)
    ]

    run1 = reranker.rerank_candidates(query="annual leave package", candidates=candidates)
    run2 = reranker.rerank_candidates(query="annual leave package", candidates=candidates)

    assert len(run1) == len(run2) == 5
    for r1, r2 in zip(run1, run2):
        assert r1.chunk_id == r2.chunk_id
        assert r1.rerank_score == r2.rerank_score
        assert r1.lexical_score == r2.lexical_score
        assert r1.phrase_score == r2.phrase_score


# ============================================================
# 8. Score Ordering (Highest First)
# ============================================================
def test_08_score_ordering(assembler: ContextAssembler):
    """Verify final assembled context items are strictly ordered by rerank_score descending."""
    context = assembler.assemble(query="corporate travel reimbursement guidelines", max_context_items=5)
    assert len(context.items) > 1

    for i in range(len(context.items) - 1):
        assert context.items[i].rerank_score >= context.items[i + 1].rerank_score
        assert context.items[i].rank == i + 1


# ============================================================
# 9. Context Character Budget Enforcement
# ============================================================
def test_09_context_character_budget(assembler: ContextAssembler):
    """Verify max_characters constraint bounds total assembled text size."""
    small_budget = 600
    context = assembler.assemble(
        query="cybersecurity phishing email reporting procedure",
        max_characters=small_budget,
        max_context_items=10,
    )

    total_chars = sum(len(item.text) for item in context.items)
    # The first item may exceed if it's large alone, but subsequent items will not exceed
    assert context.metadata.total_characters == total_chars
    if len(context.items) > 1:
        assert total_chars <= small_budget or context.metadata.budget_limited > 0


# ============================================================
# 10. Maximum Context Items Limit
# ============================================================
def test_10_maximum_context_items(assembler: ContextAssembler):
    """Verify max_context_items strictly limits the number of returned chunks."""
    # Test with synthetic multi-doc candidates
    synthetic_candidates = [
        RetrievalResult(
            chunk_id=f"synth_chunk_{i}",
            document_id=1000 + i,
            chunk_index=0,
            content=f"Distinct document #{i} with detailed instructions for annual appraisal cycle.",
            distance=0.2,
            similarity_score=0.8,
            document_title=f"Doc #{i}",
        )
        for i in range(10)
    ]

    for limit in [1, 2, 4, 6]:
        context = assembler.assemble(
            query="annual appraisal cycle instructions",
            candidates=synthetic_candidates,
            max_context_items=limit,
        )
        assert len(context.items) == limit
        assert context.metadata.selected_count == limit

    # Also test live query bounds
    live_ctx = assembler.assemble(query="performance review criteria", max_context_items=2)
    assert len(live_ctx.items) <= 2


# ============================================================
# 11. Maximum Chunks Per Document (Diversity Control)
# ============================================================
def test_11_max_chunks_per_document(assembler: ContextAssembler):
    """Verify no single document exceeds max_chunks_per_document."""
    # Create 5 chunks from Doc 100, and 2 from Doc 200
    candidates = [
        RetrievalResult(
            chunk_id=f"chunk_doc100_{i}",
            document_id=100,
            chunk_index=i,
            content=f"Important procedure step {i} for server provisioning and infrastructure deployment.",
            distance=0.1 + (i * 0.01),
            similarity_score=0.9 - (i * 0.01),
            document_title="Server SOP",
        )
        for i in range(5)
    ] + [
        RetrievalResult(
            chunk_id=f"chunk_doc200_{i}",
            document_id=200,
            chunk_index=i,
            content=f"Secondary server configuration details part {i}.",
            distance=0.2 + (i * 0.01),
            similarity_score=0.8 - (i * 0.01),
            document_title="Secondary SOP",
        )
        for i in range(2)
    ]

    context = assembler.assemble(
        query="server provisioning procedure step",
        candidates=candidates,
        max_context_items=5,
        max_chunks_per_document=2,
    )

    doc_counts: Dict[int, int] = {}
    for item in context.items:
        doc_counts[item.document_id] = doc_counts.get(item.document_id, 0) + 1

    assert doc_counts.get(100, 0) <= 2
    assert context.metadata.diversity_filtered >= 3


# ============================================================
# 12. Diversity Across Multiple Documents
# ============================================================
def test_12_multi_document_diversity(assembler: ContextAssembler):
    """Verify diversity mechanism allows high-ranking chunks from distinct documents to enter context."""
    context = assembler.assemble(
        query="How do employees request leave and what are the HR benefits?",
        max_context_items=4,
        max_chunks_per_document=2,
    )
    unique_docs = {item.document_id for item in context.items}
    assert len(unique_docs) >= 2


# ============================================================
# 13. Metadata Preservation
# ============================================================
def test_13_metadata_preservation(assembler: ContextAssembler):
    """Verify original metadata dict is fully preserved in each ContextItem."""
    custom_meta = {"department": "Finance", "access_level": "employee", "confidentiality": "internal"}
    cand = RetrievalResult(
        chunk_id="meta_chunk_1",
        document_id=777,
        chunk_index=2,
        content="Finance expense submission threshold rules.",
        distance=0.2,
        similarity_score=0.8,
        document_title="Finance Policy",
        source_path="data/finance/policy.md",
        metadata=custom_meta,
    )

    context = assembler.assemble(query="finance expense submission", candidates=[cand], max_context_items=1)
    assert len(context.items) == 1
    item = context.items[0]
    assert item.metadata == custom_meta
    assert item.source == "data/finance/policy.md"
    assert item.document_title == "Finance Policy"


# ============================================================
# 14. Document and Chunk Traceability
# ============================================================
def test_14_document_chunk_traceability(assembler: ContextAssembler):
    """Verify all final context items map back to real database documents and chunks."""
    context = assembler.assemble(query="corporate VPN remote access setup", max_context_items=3)

    with SessionLocal() as session:
        for item in context.items:
            doc = session.execute(select(Document).where(Document.id == item.document_id)).scalars().first()
            assert doc is not None
            chunk = session.execute(
                select(DocumentChunk).where(
                    DocumentChunk.document_id == item.document_id,
                    DocumentChunk.chunk_index == item.chunk_index,
                )
            ).scalars().first()
            assert chunk is not None


# ============================================================
# 15. Security & Permission Preservation
# ============================================================
def test_15_permission_preservation(assembler: ContextAssembler):
    """Verify restricted documents cannot enter context without proper user credentials."""
    unauthorized_user = {"role": "Employee", "department": "Marketing"}

    # Executive restricted document
    exec_cand = RetrievalResult(
        chunk_id="exec_chunk_1",
        document_id=888,
        chunk_index=0,
        content="Restricted Board of Directors Compensation and Strategy 2026.",
        distance=0.1,
        similarity_score=0.9,
        metadata={"access_level": "restricted", "allowed_departments": ["Management", "Legal"]},
    )
    public_cand = RetrievalResult(
        chunk_id="public_chunk_1",
        document_id=889,
        chunk_index=0,
        content="Public company holiday calendar and celebration events.",
        distance=0.3,
        similarity_score=0.7,
        metadata={"access_level": "employee"},
    )

    # When query is executed with user_context, candidate is filtered
    context = assembler.assemble(
        query="compensation strategy and holidays",
        candidates=[exec_cand, public_cand],
        user_context=unauthorized_user,
        max_context_items=5,
    )
    assert len(context.items) == 1
    assert context.items[0].chunk_id == "public_chunk_1"


# ============================================================
# 16. Database Read-Only Enforcement
# ============================================================
def test_16_database_read_only_enforcement(assembler: ContextAssembler):
    """Verify Step 7 execution causes zero database modifications."""
    with SessionLocal() as session:
        doc_count_before = session.execute(select(func.count(Document.id))).scalar()
        chunk_count_before = session.execute(select(func.count(DocumentChunk.id))).scalar()

    # Run multiple assembly queries
    assembler.assemble(query="leave policy", max_context_items=5)
    assembler.assemble(query="IT support ticket", max_context_items=5)
    assembler.assemble(query="finance travel claims", max_context_items=5)

    with SessionLocal() as session:
        doc_count_after = session.execute(select(func.count(Document.id))).scalar()
        chunk_count_after = session.execute(select(func.count(DocumentChunk.id))).scalar()

    assert doc_count_before == doc_count_after
    assert chunk_count_before == chunk_count_after


# ============================================================
# 17. No Gemini API Usage
# ============================================================
def test_17_no_gemini_usage(monkeypatch: pytest.MonkeyPatch, assembler: ContextAssembler):
    """Verify context assembly operates completely locally without invoking Gemini."""
    import socket

    # Track outgoing socket connections to ensure no external AI calls
    orig_connect = socket.socket.connect

    def guarded_connect(self, address):
        host, port = address[0], address[1]
        if "generativelanguage.googleapis.com" in str(host):
            raise RuntimeError("Gemini API network connection attempted!")
        return orig_connect(self, address)

    monkeypatch.setattr(socket.socket, "connect", guarded_connect)

    context = assembler.assemble(query="What is the employee sick leave policy?", max_context_items=3)
    assert len(context.items) > 0


# ============================================================
# 18. No OpenRouter API Usage
# ============================================================
def test_18_no_openrouter_usage(monkeypatch: pytest.MonkeyPatch, assembler: ContextAssembler):
    """Verify context assembly operates without making OpenRouter or OpenAI API calls."""
    import socket

    orig_connect = socket.socket.connect

    def guarded_connect(self, address):
        host, port = address[0], address[1]
        if "openrouter.ai" in str(host) or "openai.com" in str(host):
            raise RuntimeError(f"External API network connection attempted to {host}!")
        return orig_connect(self, address)

    monkeypatch.setattr(socket.socket, "connect", guarded_connect)

    context = assembler.assemble(query="cybersecurity incident procedure", max_context_items=3)
    assert len(context.items) > 0
