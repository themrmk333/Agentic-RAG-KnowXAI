"""
Comprehensive unit and regression tests for Step 4 Local GPU Embedding Generation.

All tests use mock model instances or fast CPU execution.
No live API keys or database connections required.
"""

from __future__ import annotations

import json
import math
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import numpy as np
import pytest
import torch

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import Settings
from rag.embeddings.client import (
    PermanentEmbeddingError,
    ResilientEmbeddingClient,
    TransientEmbeddingError,
)
from rag.embeddings.models import (
    DEFAULT_EMBEDDING_BATCH_SIZE,
    EXPECTED_VECTOR_DIMENSION,
    CheckpointState,
    EmbeddingRecord,
    InputChunk,
    compute_dataset_fingerprint,
    validate_vector,
)
from rag.embeddings.pipeline import Step4EmbeddingPipeline
from rag.embeddings.validator import (
    EmbeddingInputValidator,
    EmbeddingPostValidator,
    EmbeddingVectorValidator,
)


def _make_dummy_chunk(
    chunk_id: str = "batch_01_test_chunk_000000",
    text: str = "This is test chunk text.",
    batch_id: str = "batch_01",
    chunk_index: int = 0,
    total_chunks: int = 1,
) -> dict:
    return {
        "chunk_id": chunk_id,
        "batch_id": batch_id,
        "source_file": "data/test.md",
        "relative_path": "data/test.md",
        "filename": "test.md",
        "extension": ".md",
        "chunk_index": chunk_index,
        "total_chunks_for_file": total_chunks,
        "character_count": len(text),
        "word_count": len(text.split()),
        "estimated_tokens": int(len(text.split()) * 1.3),
        "source_sha256": "a" * 64,
        "chunk_sha256": "b" * 64,
        "heading_context": "",
        "chunking_strategy": "MarkdownChunker",
        "text": text,
        "created_at_utc": "2026-08-27T00:00:00+00:00",
    }


def _make_valid_vector(dim: int = EXPECTED_VECTOR_DIMENSION, val: float = 0.05) -> list[float]:
    return [val] * dim


# ============================================================
# Test 1: Configuration validation
# ============================================================
def test_01_configuration_validation():
    """Verify settings loads model, provider, and dimensions correctly for local embeddings."""
    settings = Settings(
        embedding_provider="local",
        embedding_model="BAAI/bge-small-en-v1.5",
        embedding_dimensions=384,
        pgvector_dimensions=384,
        gemini_api_key="dummy-gemini-key",
    )
    assert settings.embedding_provider == "local"
    assert settings.embedding_model == "BAAI/bge-small-en-v1.5"
    assert settings.embedding_dimensions == 384
    assert settings.pgvector_dimensions == 384
    print("  PASS: test_01_configuration_validation")


# ============================================================
# Test 2: No API key required for local embedding client
# ============================================================
def test_02_no_api_key_required_for_local():
    """Local client initializes cleanly without requiring any API key."""
    mock_model = MagicMock()
    mock_model.encode.return_value = np.zeros((1, 384), dtype=np.float32)

    client = ResilientEmbeddingClient(
        model="BAAI/bge-small-en-v1.5",
        expected_dimension=384,
        device="cpu",
        model_instance=mock_model,
    )
    assert client.model == "BAAI/bge-small-en-v1.5"
    assert client.expected_dimension == 384
    print("  PASS: test_02_no_api_key_required_for_local")


# ============================================================
# Test 3: Input validation on valid chunks
# ============================================================
def test_03_input_validation():
    """Valid chunks JSONL should pass input validation with 0 errors."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        b1 = tmp_path / "batch_01"
        b1.mkdir()
        jsonl = b1 / "chunks.jsonl"

        chunks_data = [
            _make_dummy_chunk(chunk_id=f"batch_01_test_chunk_{i:06d}", chunk_index=i, total_chunks=3)
            for i in range(3)
        ]
        with open(jsonl, mode="w", encoding="utf-8") as f:
            for c in chunks_data:
                f.write(json.dumps(c) + "\n")

        validator = EmbeddingInputValidator(tmp_path)
        chunks, report = validator.validate_and_load()

        assert report["is_valid"] is True
        assert report["total_chunks_loaded"] == 3
        assert report["duplicate_id_count"] == 0
        assert report["empty_text_count"] == 0
        assert len(chunks) == 3
    print("  PASS: test_03_input_validation")


# ============================================================
# Test 4: Duplicate chunk IDs detected
# ============================================================
def test_04_duplicate_chunk_ids():
    """Duplicate chunk IDs in input must be flagged."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        b1 = tmp_path / "batch_01"
        b1.mkdir()
        jsonl = b1 / "chunks.jsonl"

        chunks_data = [
            _make_dummy_chunk(chunk_id="duplicate_id"),
            _make_dummy_chunk(chunk_id="duplicate_id"),
        ]
        with open(jsonl, mode="w", encoding="utf-8") as f:
            for c in chunks_data:
                f.write(json.dumps(c) + "\n")

        validator = EmbeddingInputValidator(tmp_path)
        chunks, report = validator.validate_and_load()

        assert report["is_valid"] is False
        assert report["duplicate_id_count"] == 1
        assert any("duplicate chunk IDs" in e for e in report["errors"])
    print("  PASS: test_04_duplicate_chunk_ids")


# ============================================================
# Test 5: Empty text detected
# ============================================================
def test_05_empty_text():
    """Chunks with empty or whitespace-only text must be flagged."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        b1 = tmp_path / "batch_01"
        b1.mkdir()
        jsonl = b1 / "chunks.jsonl"

        chunks_data = [
            _make_dummy_chunk(chunk_id="c1", text="   "),
        ]
        with open(jsonl, mode="w", encoding="utf-8") as f:
            for c in chunks_data:
                f.write(json.dumps(c) + "\n")

        validator = EmbeddingInputValidator(tmp_path)
        chunks, report = validator.validate_and_load()

        assert report["is_valid"] is False
        assert report["empty_text_count"] == 1
    print("  PASS: test_05_empty_text")


# ============================================================
# Test 6: Batch creation / slicing with local model
# ============================================================
def test_06_batch_creation():
    """Client handles batch slicing and processes all items via model."""
    mock_model = MagicMock()
    mock_model.encode.return_value = np.zeros((5, 384), dtype=np.float32)

    client = ResilientEmbeddingClient(
        model="BAAI/bge-small-en-v1.5",
        expected_dimension=384,
        device="cpu",
        model_instance=mock_model,
    )

    texts = [f"Text {i}" for i in range(5)]
    vectors = client.embed_batch(texts)
    assert len(vectors) == 5
    assert len(vectors[0]) == 384
    assert mock_model.encode.call_count == 1
    print("  PASS: test_06_batch_creation")


# ============================================================
# Test 7: Response count mismatch handled
# ============================================================
def test_07_response_count_mismatch():
    """Model returning fewer vectors than requested raises PermanentEmbeddingError."""
    mock_model = MagicMock()
    mock_model.encode.return_value = np.zeros((2, 384), dtype=np.float32)

    client = ResilientEmbeddingClient(
        model="BAAI/bge-small-en-v1.5",
        expected_dimension=384,
        device="cpu",
        model_instance=mock_model,
    )

    texts = ["T1", "T2", "T3"]
    with pytest.raises(PermanentEmbeddingError, match="returned 2 vectors for 3 input texts"):
        client.embed_batch(texts)
    print("  PASS: test_07_response_count_mismatch")


# ============================================================
# Test 8: Dimension mismatch detected
# ============================================================
def test_08_dimension_mismatch():
    """Vectors with wrong dimension (e.g. 512 instead of 384) raise error."""
    mock_model = MagicMock()
    mock_model.encode.return_value = np.zeros((1, 512), dtype=np.float32)

    client = ResilientEmbeddingClient(
        model="BAAI/bge-small-en-v1.5",
        expected_dimension=384,
        device="cpu",
        model_instance=mock_model,
    )

    with pytest.raises(PermanentEmbeddingError, match="Dimension mismatch"):
        client.embed_batch(["Test text"])
    print("  PASS: test_08_dimension_mismatch")


# ============================================================
# Test 9: NaN detection
# ============================================================
def test_09_nan_detection():
    """Vectors containing float('nan') fail validation."""
    vec = _make_valid_vector(dim=384)
    vec[42] = float("nan")
    ok, msg = validate_vector(vec, expected_dim=384)
    assert not ok
    assert "NaN value encountered at index 42" in msg
    print("  PASS: test_09_nan_detection")


# ============================================================
# Test 10: Infinity detection
# ============================================================
def test_10_infinity_detection():
    """Vectors containing float('inf') fail validation."""
    vec = _make_valid_vector(dim=384)
    vec[100] = float("inf")
    ok, msg = validate_vector(vec, expected_dim=384)
    assert not ok
    assert "Infinity value encountered at index 100" in msg
    print("  PASS: test_10_infinity_detection")


# ============================================================
# Test 11: CUDA requirement check
# ============================================================
def test_11_cuda_device_detection():
    """Requiring CUDA when unavailable or device is cpu raises RuntimeError."""
    mock_model = MagicMock()
    with pytest.raises(RuntimeError, match="CUDA is required"):
        ResilientEmbeddingClient(
            model="BAAI/bge-small-en-v1.5",
            expected_dimension=384,
            device="cpu",
            require_cuda=True,
            model_instance=mock_model,
        )
    print("  PASS: test_11_cuda_device_detection")


# ============================================================
# Test 12: Checkpoint creation & persistence
# ============================================================
def test_12_checkpoint_creation():
    """CheckpointState is serialized and loaded properly with local BAAI model."""
    with tempfile.TemporaryDirectory() as tmp:
        cp_file = Path(tmp) / "checkpoint.json"
        cp = CheckpointState(
            timestamp_utc="2026-08-29T00:00:00+00:00",
            embedding_model="BAAI/bge-small-en-v1.5",
            embedding_dimension=384,
            input_fingerprint="abc123fingerprint",
            total_input_chunks=100,
            completed_chunks_count=50,
            completed_batches_count=1,
            last_completed_batch_id="batch_01",
            completed_chunk_ids=["chunk_1", "chunk_2"],
        )

        with open(cp_file, mode="w", encoding="utf-8") as f:
            json.dump(cp.to_dict(), f)

        with open(cp_file, mode="r", encoding="utf-8") as f:
            loaded = CheckpointState.from_dict(json.load(f))

        assert loaded.embedding_model == "BAAI/bge-small-en-v1.5"
        assert loaded.embedding_dimension == 384
        assert loaded.input_fingerprint == "abc123fingerprint"
        assert loaded.completed_chunks_count == 50
        assert loaded.completed_chunk_ids == ["chunk_1", "chunk_2"]
    print("  PASS: test_12_checkpoint_creation")


# ============================================================
# Test 13: Resume behavior with local model
# ============================================================
def test_13_resume_behavior():
    """Pipeline with resume=True skips already completed chunk IDs."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        chunks_dir = tmp_path / "chunks" / "batch_01"
        chunks_dir.mkdir(parents=True)
        out_dir = tmp_path / "embeddings_step4"

        # 3 input chunks
        c_list = [
            _make_dummy_chunk(chunk_id=f"c_{i}", text=f"Text {i}", chunk_index=i, total_chunks=3)
            for i in range(3)
        ]
        with open(chunks_dir / "chunks.jsonl", mode="w", encoding="utf-8") as f:
            for c in c_list:
                f.write(json.dumps(c) + "\n")

        mock_model = MagicMock()
        mock_model.encode.return_value = np.zeros((1, 384), dtype=np.float32)

        client = ResilientEmbeddingClient(
            model="BAAI/bge-small-en-v1.5",
            expected_dimension=384,
            device="cpu",
            model_instance=mock_model,
        )

        pipeline = Step4EmbeddingPipeline(
            chunks_root=tmp_path / "chunks",
            output_root=out_dir,
            client=client,
            batch_size=1,
            expected_dimension=384,
        )

        # Pre-seed checkpoint with c_0 and c_1 completed
        pipeline._ensure_directories()
        fp = compute_dataset_fingerprint(c_list)
        pre_cp = CheckpointState(
            timestamp_utc="2026-08-29T00:00:00+00:00",
            embedding_model="BAAI/bge-small-en-v1.5",
            embedding_dimension=384,
            input_fingerprint=fp,
            total_input_chunks=3,
            completed_chunks_count=2,
            completed_batches_count=2,
            completed_chunk_ids=["c_0", "c_1"],
        )
        pipeline._save_checkpoint(pre_cp)

        # Also write c_0 and c_1 to jsonl
        emb_b1 = out_dir / "embeddings" / "batch_01"
        emb_b1.mkdir(parents=True)
        with open(emb_b1 / "embeddings.jsonl", mode="w", encoding="utf-8") as f:
            for i in range(2):
                rec = EmbeddingRecord(
                    chunk_id=f"c_{i}",
                    batch_id="batch_01",
                    source_file="data/test.md",
                    relative_path="data/test.md",
                    chunk_index=i,
                    total_chunks_for_file=3,
                    chunk_sha256="b" * 64,
                    embedding_model="BAAI/bge-small-en-v1.5",
                    embedding_dimension=384,
                    embedding=_make_valid_vector(dim=384),
                    created_at_utc="2026-08-29T00:00:00+00:00",
                )
                f.write(rec.to_jsonl_line() + "\n")

        results = pipeline.run(resume=True)

        assert results["validation_summary"]["TOTAL_EMBEDDED_CHUNKS"] == 3
        assert results["validation_summary"]["FINAL_STATUS"] == "PASS"
        # 1 call for test_dimension + 1 call for c_2
        assert mock_model.encode.call_count == 2
    print("  PASS: test_13_resume_behavior")


# ============================================================
# Test 14: Duplicate prevention / idempotency
# ============================================================
def test_14_duplicate_prevention():
    """Running post validator detects duplicate chunk embeddings."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        emb_dir = tmp_path / "embeddings" / "batch_01"
        emb_dir.mkdir(parents=True)

        rec1 = EmbeddingRecord(
            chunk_id="chunk_dup",
            batch_id="batch_01",
            source_file="data/test.md",
            relative_path="data/test.md",
            chunk_index=0,
            total_chunks_for_file=1,
            chunk_sha256="b" * 64,
            embedding_model="BAAI/bge-small-en-v1.5",
            embedding_dimension=384,
            embedding=_make_valid_vector(dim=384),
            created_at_utc="2026-08-29T00:00:00+00:00",
        )

        with open(emb_dir / "embeddings.jsonl", mode="w", encoding="utf-8") as f:
            f.write(rec1.to_jsonl_line() + "\n")
            f.write(rec1.to_jsonl_line() + "\n")  # duplicate

        input_chunk = InputChunk.from_dict(_make_dummy_chunk(chunk_id="chunk_dup"))
        validator = EmbeddingPostValidator(
            embeddings_root=tmp_path / "embeddings",
            input_chunks=[input_chunk],
            expected_dim=384,
        )
        report = validator.validate()

        assert report["is_valid"] is False
        assert report["duplicate_embedding_ids_count"] == 1
        assert report["status"] == "FAIL"
    print("  PASS: test_14_duplicate_prevention")


# ============================================================
# Test 15: Final integrity validation (100% pass condition)
# ============================================================
def test_15_final_integrity_validation():
    """Post validator passes cleanly when all embeddings match 1-to-1."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        emb_dir = tmp_path / "embeddings" / "batch_01"
        emb_dir.mkdir(parents=True)

        input_chunks = []
        with open(emb_dir / "embeddings.jsonl", mode="w", encoding="utf-8") as f:
            for i in range(10):
                cid = f"chunk_{i:04d}"
                raw = _make_dummy_chunk(chunk_id=cid, chunk_index=i, total_chunks=10)
                input_chunks.append(InputChunk.from_dict(raw))

                rec = EmbeddingRecord(
                    chunk_id=cid,
                    batch_id="batch_01",
                    source_file="data/test.md",
                    relative_path="data/test.md",
                    chunk_index=i,
                    total_chunks_for_file=10,
                    chunk_sha256="b" * 64,
                    embedding_model="BAAI/bge-small-en-v1.5",
                    embedding_dimension=384,
                    embedding=_make_valid_vector(dim=384),
                    created_at_utc="2026-08-29T00:00:00+00:00",
                )
                f.write(rec.to_jsonl_line() + "\n")

        validator = EmbeddingPostValidator(
            embeddings_root=tmp_path / "embeddings",
            input_chunks=input_chunks,
            expected_dim=384,
        )
        report = validator.validate()

        assert report["is_valid"] is True
        assert report["status"] == "PASS"
        assert report["total_input_chunks"] == 10
        assert report["total_embedded_chunks"] == 10
        assert report["missing_embeddings_count"] == 0
        assert report["duplicate_embedding_ids_count"] == 0
        assert report["invalid_vectors_count"] == 0
    print("  PASS: test_15_final_integrity_validation")


# ============================================================
# Test 16: Model mismatch invalidates old checkpoint
# ============================================================
def test_16_checkpoint_model_mismatch_invalidation():
    """Checkpoint created with old model (gemini-embedding-001) is rejected when running with BAAI/bge-small-en-v1.5."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        out_dir = tmp_path / "embeddings_step4"
        cp_dir = out_dir / "checkpoints"
        cp_dir.mkdir(parents=True)
        cp_file = cp_dir / "checkpoint.json"

        # Checkpoint with old Gemini model
        old_cp = {
            "timestamp_utc": "2026-08-27T00:00:00+00:00",
            "embedding_model": "gemini-embedding-001",
            "embedding_dimension": 1536,
            "input_fingerprint": "fingerprint_123",
            "total_input_chunks": 100,
            "completed_chunks_count": 50,
            "completed_batches_count": 1,
            "last_completed_batch_id": "batch_01",
            "completed_chunk_ids": ["chunk_1", "chunk_2"],
        }
        with open(cp_file, mode="w", encoding="utf-8") as f:
            json.dump(old_cp, f)

        mock_model = MagicMock()
        client = ResilientEmbeddingClient(
            model="BAAI/bge-small-en-v1.5",
            expected_dimension=384,
            device="cpu",
            model_instance=mock_model,
        )

        pipeline = Step4EmbeddingPipeline(
            chunks_root=tmp_path,
            output_root=out_dir,
            client=client,
            expected_dimension=384,
        )

        # Loading checkpoint with current fingerprint should return None because model does not match
        loaded = pipeline._load_checkpoint("fingerprint_123")
        assert loaded is None
    print("  PASS: test_16_checkpoint_model_mismatch_invalidation")


def run_all_tests():
    print("\n" + "=" * 62)
    print("STEP 4 - UNIT & REGRESSION TESTS (LOCAL BAAI/BGE-SMALL)")
    print("=" * 62)

    tests = [
        test_01_configuration_validation,
        test_02_no_api_key_required_for_local,
        test_03_input_validation,
        test_04_duplicate_chunk_ids,
        test_05_empty_text,
        test_06_batch_creation,
        test_07_response_count_mismatch,
        test_08_dimension_mismatch,
        test_09_nan_detection,
        test_10_infinity_detection,
        test_11_cuda_device_detection,
        test_12_checkpoint_creation,
        test_13_resume_behavior,
        test_14_duplicate_prevention,
        test_15_final_integrity_validation,
        test_16_checkpoint_model_mismatch_invalidation,
    ]

    passed = 0
    failed = 0
    failures = []

    for test_fn in tests:
        name = test_fn.__name__
        try:
            test_fn()
            passed += 1
        except AssertionError as e:
            failed += 1
            failures.append((name, str(e)))
            print(f"  FAIL: {name}")
            print(f"    {e}")
        except Exception as e:
            failed += 1
            failures.append((name, str(e)))
            print(f"  ERROR: {name}")
            print(f"    {e}")

    print("=" * 62)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(tests)} tests")
    if failures:
        print("\nFAILURES:")
        for name, msg in failures:
            print(f"  {name}: {msg[:200]}")
    print("=" * 62)

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
