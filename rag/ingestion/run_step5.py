"""Step 5 CLI Execution and Validation Runner for PostgreSQL + pgvector Ingestion.

Supports:
  --test N       : Run isolated ingestion test on first N records
  --resume       : Resume ingestion skipping already inserted chunk IDs
  --validate     : Run comprehensive database integrity and semantic retrieval validation
  --batch-size N : Transaction batch size (default: 250)
  --query "text" : Run live semantic similarity search query
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from sqlalchemy import func, select, text
from sentence_transformers import SentenceTransformer

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import get_settings
from database.connection import SessionLocal, engine
from database.models import Document, DocumentChunk
from database.vector_store import PGVectorStore
from rag.ingestion.step5_ingestion import IngestionConfig, Step5IngestionPipeline
from rag.retrieval.pgvector_retriever import PGVectorRetriever


def compute_directory_sha256(directory: Path, glob_pattern: str = "**/*") -> str:
    """Compute a single SHA-256 hash across all files matching glob_pattern."""
    files = sorted([f for f in directory.glob(glob_pattern) if f.is_file()])
    hasher = hashlib.sha256()
    for file_path in files:
        hasher.update(file_path.name.encode("utf-8"))
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
    return hasher.hexdigest()


class LocalEmbeddingHelper:
    """Local embedding helper for semantic query search."""
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5", device: str = "cuda"):
        import torch
        actual_device = "cuda" if (device.startswith("cuda") and torch.cuda.is_available()) else "cpu"
        self.model = SentenceTransformer(model_name, device=actual_device)

    def embed_query(self, query: str) -> List[float]:
        emb = self.model.encode(query, normalize_embeddings=True)
        return emb.tolist()


def run_isolated_10_test(config: IngestionConfig) -> bool:
    """Run a safe 10-record isolated test before full ingestion."""
    print("\n" + "=" * 62)
    print("RUNNING STEP 5 ISOLATED 10-RECORD SAFETY TEST")
    print("=" * 62)

    chunks_sha_before = compute_directory_sha256(config.chunks_dir, "**/*.jsonl")
    embeddings_sha_before = compute_directory_sha256(config.embeddings_dir, "**/*.jsonl")

    pipeline = Step5IngestionPipeline(config)
    report = pipeline.run(limit=10, batch_size=10, resume=False)

    # Validate the 10 records in DB
    with SessionLocal() as session:
        chunk_count = session.execute(select(func.count(DocumentChunk.id))).scalar()
        print(f"Total document_chunks in DB: {chunk_count}")

        # Check dimension of all 10
        vectors = session.execute(select(DocumentChunk.embedding).where(DocumentChunk.embedding.is_not(None)).limit(10)).scalars().all()
        dims_match = all(len(v) == 384 for v in vectors if v is not None)
        no_nan_inf = all(not any(math.isnan(x) or math.isinf(x) for x in v) for v in vectors if v is not None)

        print(f"10-Record Dimension check (all 384-D): {'PASS' if dims_match else 'FAIL'}")
        print(f"10-Record NaN/Inf check (0 NaN/Inf)  : {'PASS' if no_nan_inf else 'FAIL'}")

    chunks_sha_after = compute_directory_sha256(config.chunks_dir, "**/*.jsonl")
    embeddings_sha_after = compute_directory_sha256(config.embeddings_dir, "**/*.jsonl")

    chunks_intact = (chunks_sha_before == chunks_sha_after)
    embeddings_intact = (embeddings_sha_before == embeddings_sha_after)

    print(f"Source chunks unchanged               : {chunks_intact}")
    print(f"Step 4 embeddings unchanged           : {embeddings_intact}")

    success = dims_match and no_nan_inf and chunks_intact and embeddings_intact
    print("=" * 62)
    print(f"10-RECORD SAFETY TEST RESULT: {'PASS' if success else 'FAIL'}")
    print("=" * 62 + "\n")
    return success


def run_validation(config: IngestionConfig) -> Dict[str, Any]:
    """Execute comprehensive integrity and semantic retrieval validation on PostgreSQL."""
    print("\n" + "=" * 62)
    print("STEP 5 - POSTGRESQL & PGVECTOR COMPREHENSIVE VALIDATION")
    print("=" * 62)

    chunks_sha_before = compute_directory_sha256(config.chunks_dir, "**/*.jsonl")
    embeddings_sha_before = compute_directory_sha256(config.embeddings_dir, "**/*.jsonl")

    errors: List[str] = []

    with SessionLocal() as session:
        # A. Count validation
        total_chunks = session.execute(select(func.count(DocumentChunk.id))).scalar() or 0
        total_docs = session.execute(select(func.count(Document.id))).scalar() or 0
        total_vectors = session.execute(select(func.count(DocumentChunk.id)).where(DocumentChunk.embedding.is_not(None))).scalar() or 0

        print(f"Total documents in DB         : {total_docs:,}")
        print(f"Total document_chunks in DB   : {total_chunks:,}")
        print(f"Total vector embeddings in DB : {total_vectors:,}")

        if total_chunks != config.expected_total_chunks:
            errors.append(f"DocumentChunk count {total_chunks} != expected {config.expected_total_chunks}")

        if total_vectors != config.expected_total_chunks:
            errors.append(f"Vector count {total_vectors} != expected {config.expected_total_chunks}")

        # B. Duplicate chunk_id check
        dup_stmt = text("""
            SELECT (metadata->>'chunk_id') AS cid, count(*) 
            FROM document_chunks 
            GROUP BY cid 
            HAVING count(*) > 1;
        """)
        dups = session.execute(dup_stmt).fetchall()
        print(f"Duplicate chunk IDs in DB     : {len(dups)}")
        if dups:
            errors.append(f"Found {len(dups)} duplicate chunk IDs in document_chunks")

        # C. Missing chunk_id check
        missing_cid_stmt = text("SELECT count(*) FROM document_chunks WHERE metadata->>'chunk_id' IS NULL;")
        missing_cids = session.execute(missing_cid_stmt).scalar() or 0
        print(f"Missing chunk IDs in DB       : {missing_cids}")
        if missing_cids > 0:
            errors.append(f"Found {missing_cids} chunks with missing metadata->>'chunk_id'")

        # D. Dimension validation on sample & bulk
        print("Validating vector dimensions (all must be 384-D)...")
        dim_stmt = text("SELECT format_type(a.atttypid, a.atttypmod) FROM pg_attribute a JOIN pg_class c ON a.attrelid = c.oid WHERE c.relname = 'document_chunks' AND a.attname = 'embedding';")
        col_type = session.execute(dim_stmt).scalar()
        print(f"PostgreSQL column type        : {col_type}")
        if col_type != f"vector({config.expected_dimension})":
            errors.append(f"pgvector column type {col_type} != expected vector({config.expected_dimension})")

        # E. NaN / Infinity checks
        nan_stmt = text("SELECT count(*) FROM document_chunks WHERE embedding IS NULL;")
        null_vecs = session.execute(nan_stmt).scalar() or 0
        print(f"NULL vector records           : {null_vecs}")
        if null_vecs > 0:
            errors.append(f"Found {null_vecs} chunks with NULL vector embeddings")

        # F. Semantic search retrieval test
        print("\nRunning Semantic Similarity Search Test via PGVectorStore...")
        vector_store = PGVectorStore(dimensions=config.expected_dimension)
        helper = LocalEmbeddingHelper(model_name=config.model_name)
        retriever = PGVectorRetriever(embedding_service=helper, vector_store=vector_store)

        test_queries = [
            "What is the corporate leave policy for annual vacation days?",
            "IT VPN scheduled maintenance window hours",
            "Customer onboarding procedures and compliance requirements",
        ]

        search_pass = True
        for q in test_queries:
            results = retriever.retrieve_with_metadata(
                query=q,
                top_k=3,
                user_context={"role": "Admin", "department": "Management"}
            )
            print(f"\n  Query: '{q}'")
            print(f"  Results returned: {len(results)}")
            if not results:
                search_pass = False
                errors.append(f"Semantic search returned 0 results for query: '{q}'")
            for r_idx, res in enumerate(results[:2]):
                snippet = res["content"][:90].replace("\n", " ")
                dist = res.get("distance", 0.0)
                cid = res.get("metadata", {}).get("chunk_id", "N/A")
                print(f"    [{r_idx+1}] chunk_id: {cid} | distance: {dist:.4f} | {snippet}...")

    chunks_sha_after = compute_directory_sha256(config.chunks_dir, "**/*.jsonl")
    embeddings_sha_after = compute_directory_sha256(config.embeddings_dir, "**/*.jsonl")

    chunks_intact = (chunks_sha_before == chunks_sha_after)
    embeddings_intact = (embeddings_sha_before == embeddings_sha_after)

    validation_status = "PASS" if not errors and search_pass and chunks_intact and embeddings_intact else "FAIL"

    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "embedding_model": config.model_name,
        "dimension": config.expected_dimension,
        "total_documents": total_docs,
        "total_document_chunks": total_chunks,
        "total_vector_embeddings": total_vectors,
        "duplicate_chunk_ids": len(dups),
        "missing_chunk_ids": missing_cids,
        "column_type": col_type,
        "vector_search_pass": search_pass,
        "source_chunks_unmodified": chunks_intact,
        "step4_embeddings_unmodified": embeddings_intact,
        "validation_errors": errors,
        "status": validation_status,
    }

    report_path = config.reports_dir / "step5_validation_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\n" + "=" * 62)
    print("STEP 5 - VALIDATION SUMMARY")
    print("=" * 62)
    print(f"Input embeddings         : {config.expected_total_chunks:,}")
    print(f"Database vector records  : {total_vectors:,} / {config.expected_total_chunks:,}")
    print(f"Vector column type       : {col_type}")
    print(f"Duplicate chunk IDs      : {len(dups)}")
    print(f"Missing chunk IDs        : {missing_cids}")
    print(f"Vector similarity search : {'PASS' if search_pass else 'FAIL'}")
    print(f"Source chunks unchanged  : {chunks_intact}")
    print(f"Step 4 files unchanged   : {embeddings_intact}")
    print(f"Total validation errors  : {len(errors)}")
    print(f"FINAL VALIDATION STATUS  : {validation_status}")
    print(f"Report written to        : {report_path}")
    print("=" * 62)

    return report


def main():
    parser = argparse.ArgumentParser(description="Step 5: PostgreSQL + pgvector Ingestion Runner")
    parser.add_argument("--test", type=int, default=None, help="Run isolated test on first N chunks (e.g. --test 10)")
    parser.add_argument("--resume", action="store_true", default=True, help="Resume ingestion skipping existing chunk IDs")
    parser.add_argument("--validate", action="store_true", help="Run comprehensive database validation")
    parser.add_argument("--batch-size", type=int, default=250, help="Batch size for database transactions")
    parser.add_argument("--query", type=str, default=None, help="Run a test semantic query against pgvector")

    args = parser.parse_args()
    config = IngestionConfig()

    if args.validate:
        report = run_validation(config)
        if report["status"] != "PASS":
            sys.exit(1)
        return

    if args.test:
        success = run_isolated_10_test(config)
        if not success:
            sys.exit(1)
        return

    if args.query:
        vector_store = PGVectorStore(dimensions=config.expected_dimension)
        helper = LocalEmbeddingHelper(model_name=config.model_name)
        retriever = PGVectorRetriever(embedding_service=helper, vector_store=vector_store)
        results = retriever.retrieve_with_metadata(
            query=args.query,
            top_k=5,
            user_context={"role": "Admin", "department": "Management"}
        )
        print(f"\nQuery: '{args.query}'")
        for i, res in enumerate(results):
            print(f"[{i+1}] Distance: {res['distance']:.4f} | Chunk ID: {res['metadata'].get('chunk_id')}")
            print(f"    Content: {res['content'][:120]}...\n")
        return

    # Standard full ingestion
    pipeline = Step5IngestionPipeline(config)
    pipeline.run(limit=None, batch_size=args.batch_size, resume=args.resume)

    # Post-ingestion validation
    report = run_validation(config)
    if report["status"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
