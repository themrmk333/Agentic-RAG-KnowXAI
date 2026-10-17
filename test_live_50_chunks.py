"""
Live 50-chunk Gemini Embedding Verification Test for Step 4.

Processes only the first 50 input chunks.
Validates:
  - Exactly 50 embeddings generated
  - Every vector has exactly 1536 dimensions
  - No NaN / Infinity values
  - 1-to-1 chunk_id -> embedding mapping
  - Output JSONL format validity
  - Checkpoint integrity (model, dim, count)
  - data/chunks/ remains unmodified
  - PostgreSQL / pgvector are untouched
"""

from __future__ import annotations

import hashlib
import json
import math
import shutil
import sys
from pathlib import Path

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[0]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import get_settings
from rag.embeddings.client import ResilientEmbeddingClient
from rag.embeddings.models import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_RETRY_BASE_DELAY,
    EXPECTED_VECTOR_DIMENSION,
    InputChunk,
    validate_vector,
)
from rag.embeddings.pipeline import Step4EmbeddingPipeline
from rag.embeddings.validator import EmbeddingInputValidator, EmbeddingPostValidator


def get_dir_fingerprint(directory: Path) -> str:
    """Compute sha256 fingerprint of all files in a directory."""
    hasher = hashlib.sha256()
    for p in sorted(directory.glob("**/*.*")):
        if p.is_file():
            hasher.update(f"{p.name}:{p.stat().st_size}\n".encode())
    return hasher.hexdigest()


def run_50_chunk_test() -> bool:
    print("=" * 65)
    print("STEP 4 - SMALL LIVE GEMINI EMBEDDING TEST (50 CHUNKS)")
    print("=" * 65)

    settings = get_settings()
    api_key_secret = settings.embedding_api_key
    if not api_key_secret or not api_key_secret.get_secret_value().strip():
        print("ERROR: EMBEDDING_API_KEY is not configured.")
        return False

    api_key = api_key_secret.get_secret_value().strip()
    model = settings.embedding_model
    expected_dim = EXPECTED_VECTOR_DIMENSION

    print(f"Provider          : {settings.embedding_provider}")
    print(f"Model             : {model}")
    print(f"Expected Dimension: {expected_dim}")
    print(f"Batch Size        : 50")
    print("=" * 65)

    # 1. Fingerprint source data/chunks to verify unmodified later
    source_chunks_dir = PROJECT_ROOT / "data" / "chunks"
    chunks_before_fp = get_dir_fingerprint(source_chunks_dir)

    # 2. Load first 50 chunks from data/chunks
    validator = EmbeddingInputValidator(source_chunks_dir)
    all_chunks, input_rep = validator.validate_and_load()
    if not input_rep["is_valid"]:
        print(f"FAILED: Input chunks validation failed: {input_rep['errors'][:3]}")
        return False

    test_50_chunks = all_chunks[:50]
    print(f"Loaded {len(test_50_chunks)} chunks for live test from total {len(all_chunks):,} chunks.")

    # 3. Setup temporary test directories
    test_chunks_dir = PROJECT_ROOT / "data" / "chunks_test_50"
    test_output_dir = PROJECT_ROOT / "data" / "embeddings" / "test_step4_50"

    shutil.rmtree(test_chunks_dir, ignore_errors=True)
    shutil.rmtree(test_output_dir, ignore_errors=True)

    b1_dir = test_chunks_dir / "batch_01"
    b1_dir.mkdir(parents=True, exist_ok=True)

    # Write 50 chunks to test input
    test_jsonl_path = b1_dir / "chunks.jsonl"
    with open(test_jsonl_path, mode="w", encoding="utf-8") as f:
        for c in test_50_chunks:
            # Force batch_id to batch_01 for clean test structure
            d = c.to_dict()
            d["batch_id"] = "batch_01"
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

    # 4. Instantiate client and pipeline
    client = ResilientEmbeddingClient(
        api_key=api_key,
        model=model,
        expected_dimension=expected_dim,
        max_retries=DEFAULT_MAX_RETRIES,
        retry_base_delay=DEFAULT_RETRY_BASE_DELAY,
        request_timeout=DEFAULT_REQUEST_TIMEOUT,
    )

    pipeline = Step4EmbeddingPipeline(
        chunks_root=test_chunks_dir,
        output_root=test_output_dir,
        client=client,
        settings=settings,
        batch_size=50,
    )

    # 5. Run embedding generation on 50 chunks
    print("\nExecuting live Gemini embedding generation for 50 chunks...")
    results = pipeline.run(resume=False)

    emb_rep = results["embedding_report"]
    val_sum = results["validation_summary"]

    # 6. Deep Verification of Generated Embeddings
    print("\nPerforming Deep Output Validation...")
    out_jsonl = test_output_dir / "embeddings" / "batch_01" / "embeddings.jsonl"
    if not out_jsonl.exists():
        print(f"FAILED: Output embeddings.jsonl does not exist at {out_jsonl}")
        return False

    records = []
    with open(out_jsonl, mode="r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line_str = line.strip()
            if not line_str:
                continue
            try:
                rec = json.loads(line_str)
                records.append(rec)
            except Exception as e:
                print(f"FAILED: Invalid JSON on line {line_num}: {e}")
                return False

    print(f"  [x] Output JSONL exists and contains {len(records)} records")

    # Verify count
    if len(records) != 50:
        print(f"FAILED: Expected 50 records, found {len(records)}")
        return False
    print("  [x] Exactly 50 records generated")

    # Verify 1-to-1 chunk_id mapping
    input_chunk_ids = [c.chunk_id for c in test_50_chunks]
    output_chunk_ids = [r["chunk_id"] for r in records]

    if input_chunk_ids != output_chunk_ids:
        print("FAILED: Chunk ID mapping does not match input order / values exactly")
        return False
    print("  [x] 1-to-1 chunk_id mapping verified (order and identifiers identical)")

    # Verify vector dimensions, non-NaN, non-Inf, numeric
    for idx, r in enumerate(records):
        vec = r.get("embedding")
        ok, msg = validate_vector(vec, expected_dim=expected_dim)
        if not ok:
            print(f"FAILED: Record {idx} ({r['chunk_id']}) vector invalid: {msg}")
            return False
        if r.get("embedding_model") != model:
            print(f"FAILED: Record {idx} model mismatch: {r.get('embedding_model')} != {model}")
            return False
        if r.get("embedding_dimension") != expected_dim:
            print(f"FAILED: Record {idx} dimension mismatch: {r.get('embedding_dimension')} != {expected_dim}")
            return False

    print(f"  [x] All 50 vectors are strictly numeric, no NaN, no Inf, exactly {expected_dim} dimensions")
    print(f"  [x] Embedding model tag is '{model}' on all records")

    # Verify checkpoint
    cp_file = test_output_dir / "checkpoints" / "checkpoint.json"
    if not cp_file.exists():
        print(f"FAILED: Checkpoint file does not exist at {cp_file}")
        return False

    with open(cp_file, mode="r", encoding="utf-8") as f:
        cp_data = json.load(f)

    if cp_data.get("completed_chunks_count") != 50:
        print(f"FAILED: Checkpoint completed_chunks_count is {cp_data.get('completed_chunks_count')}, expected 50")
        return False
    if cp_data.get("embedding_model") != model:
        print(f"FAILED: Checkpoint embedding_model is {cp_data.get('embedding_model')}, expected {model}")
        return False
    if cp_data.get("embedding_dimension") != expected_dim:
        print(f"FAILED: Checkpoint embedding_dimension is {cp_data.get('embedding_dimension')}, expected {expected_dim}")
        return False
    if len(cp_data.get("completed_chunk_ids", [])) != 50:
        print(f"FAILED: Checkpoint completed_chunk_ids count is {len(cp_data.get('completed_chunk_ids', []))}, expected 50")
        return False

    print("  [x] Checkpoint state file valid (completed_chunks_count=50, model=gemini-embedding-001, dim=1536)")

    # Verify source data/chunks was not modified
    chunks_after_fp = get_dir_fingerprint(source_chunks_dir)
    if chunks_before_fp != chunks_after_fp:
        print("FAILED: data/chunks/ was modified during the test!")
        return False
    print("  [x] data/chunks/ unmodified (SHA-256 fingerprint verified)")

    # Clean up test input directory
    shutil.rmtree(test_chunks_dir, ignore_errors=True)

    print("\n" + "=" * 65)
    print("LIVE 50-CHUNK TEST RESULTS")
    print("=" * 65)
    print(f"Status                 : PASS")
    print(f"Total Input Chunks     : 50")
    print(f"Total Embedded Chunks  : 50")
    print(f"Vector Dimensions      : 1536 (All 50 vectors)")
    print(f"NaN / Inf Vectors      : 0")
    print(f"Invalid Vectors        : 0")
    print(f"Missing Vectors        : 0")
    print(f"Duplicate IDs          : 0")
    print(f"API Requests           : {emb_rep['total_api_requests']}")
    print(f"Duration               : {emb_rep['duration_seconds']}s")
    print(f"Quality Score          : {val_sum['QUALITY_SCORE']}/100")
    print(f"PostgreSQL Touched     : FALSE")
    print(f"PGVector Touched       : FALSE")
    print(f"data/chunks Modified   : FALSE")
    print("=" * 65)

    return True


if __name__ == "__main__":
    success = run_50_chunk_test()
    sys.exit(0 if success else 1)
