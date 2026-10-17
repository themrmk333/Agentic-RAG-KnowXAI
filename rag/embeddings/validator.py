"""
Input and output validators for Step 4 Embedding Generation.
"""

from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path
from typing import Any, Sequence

from .models import (
    EXPECTED_VECTOR_DIMENSION,
    InputChunk,
    compute_dataset_fingerprint,
    utc_now_iso,
    validate_vector,
)


class EmbeddingInputValidator:
    """Validates the input chunk dataset from data/chunks/ before embedding."""

    REQUIRED_FIELDS = (
        "chunk_id",
        "text",
        "chunk_index",
        "total_chunks_for_file",
        "source_sha256",
        "chunk_sha256",
        "character_count",
        "word_count",
        "estimated_tokens",
    )

    def __init__(self, chunks_root: Path | str) -> None:
        self.chunks_root = Path(chunks_root)

    def validate_and_load(self) -> tuple[list[InputChunk], dict[str, Any]]:
        """
        Validate all JSONL files under chunks_root and load input chunks.
        Fails fast or aggregates errors into a detailed report.
        """
        errors: list[str] = []
        warnings: list[str] = []
        chunks: list[InputChunk] = []
        chunk_ids: list[str] = []
        json_error_count = 0
        empty_text_count = 0
        missing_fields_count = 0
        batch_counts: dict[str, int] = {}

        if not self.chunks_root.exists():
            raise FileNotFoundError(f"Chunks directory does not exist: {self.chunks_root}")

        # Find batch folders or direct jsonl files
        jsonl_files = sorted(self.chunks_root.glob("**/chunks.jsonl"))
        if not jsonl_files:
            jsonl_files = sorted(self.chunks_root.glob("*.jsonl"))

        if not jsonl_files:
            raise FileNotFoundError(f"No chunk JSONL files found in {self.chunks_root}")

        for fpath in jsonl_files:
            batch_name = fpath.parent.name if fpath.parent != self.chunks_root else "default"
            file_chunk_count = 0
            with open(fpath, mode="r", encoding="utf-8") as f:
                for line_idx, line in enumerate(f, start=1):
                    raw = line.strip()
                    if not raw:
                        continue
                    try:
                        record = json.loads(raw)
                    except Exception as e:
                        json_error_count += 1
                        errors.append(f"Invalid JSON at {fpath.name}:{line_idx}: {e}")
                        continue

                    # Check required fields
                    missing = [field for field in self.REQUIRED_FIELDS if field not in record]
                    if missing:
                        missing_fields_count += 1
                        errors.append(
                            f"Missing fields {missing} in {fpath.name}:{line_idx} "
                            f"(chunk_id={record.get('chunk_id')})"
                        )
                        continue

                    cid = record["chunk_id"]
                    text = record.get("text", "")

                    if not isinstance(text, str) or not text.strip():
                        empty_text_count += 1
                        errors.append(f"Empty or whitespace text for chunk_id={cid} in {fpath.name}:{line_idx}")
                        continue

                    if not record.get("source_file") and not record.get("relative_path"):
                        errors.append(f"Missing source reference for chunk_id={cid} in {fpath.name}:{line_idx}")

                    # Attach batch_id if missing
                    if "batch_id" not in record or not record["batch_id"]:
                        record["batch_id"] = batch_name

                    try:
                        chunk_obj = InputChunk.from_dict(record)
                        chunks.append(chunk_obj)
                        chunk_ids.append(cid)
                        file_chunk_count += 1
                    except Exception as e:
                        errors.append(f"Failed to instantiate InputChunk for {cid}: {e}")

            batch_counts[batch_name] = file_chunk_count

        # Check duplicate chunk IDs
        id_counts = Counter(chunk_ids)
        duplicates = [cid for cid, count in id_counts.items() if count > 1]
        duplicate_id_count = len(duplicates)
        if duplicate_id_count > 0:
            errors.append(f"Found {duplicate_id_count} duplicate chunk IDs: {duplicates[:10]}")

        dataset_fingerprint = compute_dataset_fingerprint([c.to_dict() for c in chunks])

        report = {
            "timestamp_utc": utc_now_iso(),
            "chunks_root": str(self.chunks_root),
            "total_files_scanned": len(jsonl_files),
            "total_chunks_loaded": len(chunks),
            "batch_counts": batch_counts,
            "json_error_count": json_error_count,
            "missing_fields_count": missing_fields_count,
            "empty_text_count": empty_text_count,
            "duplicate_id_count": duplicate_id_count,
            "error_count": len(errors),
            "warning_count": len(warnings),
            "errors": errors[:50],  # cap to first 50
            "dataset_fingerprint": dataset_fingerprint,
            "is_valid": len(errors) == 0 and len(chunks) > 0,
        }

        return chunks, report


class EmbeddingVectorValidator:
    """Validates individual vectors and batches of vectors."""

    @staticmethod
    def validate_batch(
        vectors: Sequence[Sequence[float]],
        expected_count: int,
        expected_dim: int = EXPECTED_VECTOR_DIMENSION,
    ) -> tuple[bool, str]:
        if len(vectors) != expected_count:
            return False, f"Returned vector count {len(vectors)} != requested count {expected_count}"

        for idx, vec in enumerate(vectors):
            ok, msg = validate_vector(vec, expected_dim=expected_dim)
            if not ok:
                return False, f"Vector {idx} validation failed: {msg}"

        return True, "OK"


class EmbeddingPostValidator:
    """Validates generated embeddings against input chunks."""

    def __init__(
        self,
        embeddings_root: Path | str,
        input_chunks: Sequence[InputChunk],
        expected_dim: int = EXPECTED_VECTOR_DIMENSION,
    ) -> None:
        self.embeddings_root = Path(embeddings_root)
        self.input_chunks = input_chunks
        self.expected_dim = expected_dim

    def validate(self) -> dict[str, Any]:
        """
        Validate all generated embeddings:
          - 1-to-1 match with input chunks
          - No missing embeddings
          - No duplicate embedding IDs
          - Every vector valid (dim=384, no NaN, no Inf)
        """
        errors: list[str] = []
        warnings: list[str] = []

        input_chunk_ids = {c.chunk_id: c for c in self.input_chunks}
        total_input_chunks = len(self.input_chunks)

        embedded_records: dict[str, dict[str, Any]] = {}
        duplicate_embedding_ids: list[str] = []
        invalid_vectors_count = 0
        dim_mismatches_count = 0
        nan_vectors_count = 0
        inf_vectors_count = 0
        json_errors_count = 0
        non_numeric_count = 0

        # Scan embedding jsonl files
        jsonl_files = sorted(self.embeddings_root.glob("**/embeddings.jsonl"))
        if not jsonl_files:
            jsonl_files = sorted(self.embeddings_root.glob("*.jsonl"))

        for fpath in jsonl_files:
            with open(fpath, mode="r", encoding="utf-8") as f:
                for line_idx, line in enumerate(f, start=1):
                    raw = line.strip()
                    if not raw:
                        continue
                    try:
                        record = json.loads(raw)
                    except Exception as e:
                        json_errors_count += 1
                        errors.append(f"Invalid JSON in {fpath.name}:{line_idx}: {e}")
                        continue

                    cid = record.get("chunk_id")
                    if not cid:
                        errors.append(f"Missing chunk_id in {fpath.name}:{line_idx}")
                        continue

                    if cid in embedded_records:
                        duplicate_embedding_ids.append(cid)
                        errors.append(f"Duplicate embedding for chunk_id={cid} in {fpath.name}:{line_idx}")
                        continue

                    if cid not in input_chunk_ids:
                        errors.append(f"Orphan embedding chunk_id={cid} not found in input chunks")
                        continue

                    vector = record.get("embedding")
                    if not isinstance(vector, (list, tuple)):
                        invalid_vectors_count += 1
                        errors.append(f"Invalid vector type for chunk_id={cid}: {type(vector).__name__}")
                        continue

                    if len(vector) != self.expected_dim:
                        dim_mismatches_count += 1
                        errors.append(
                            f"Dimension mismatch for chunk_id={cid}: got {len(vector)}, expected {self.expected_dim}"
                        )

                    has_nan = False
                    has_inf = False
                    has_non_num = False
                    for v in vector:
                        if not isinstance(v, (int, float)):
                            has_non_num = True
                        elif math.isnan(v):
                            has_nan = True
                        elif math.isinf(v):
                            has_inf = True

                    if has_nan:
                        nan_vectors_count += 1
                        errors.append(f"NaN in vector for chunk_id={cid}")
                    if has_inf:
                        inf_vectors_count += 1
                        errors.append(f"Infinity in vector for chunk_id={cid}")
                    if has_non_num:
                        non_numeric_count += 1
                        errors.append(f"Non-numeric value in vector for chunk_id={cid}")

                    if len(vector) != self.expected_dim or has_nan or has_inf or has_non_num:
                        invalid_vectors_count += 1

                    embedded_records[cid] = record

        # Check missing embeddings
        missing_chunk_ids = [cid for cid in input_chunk_ids if cid not in embedded_records]
        if missing_chunk_ids:
            errors.append(f"Missing embeddings for {len(missing_chunk_ids)} chunks (e.g. {missing_chunk_ids[:5]})")

        is_valid = (
            len(errors) == 0
            and len(embedded_records) == total_input_chunks
            and len(missing_chunk_ids) == 0
            and len(duplicate_embedding_ids) == 0
            and invalid_vectors_count == 0
        )

        return {
            "timestamp_utc": utc_now_iso(),
            "total_input_chunks": total_input_chunks,
            "total_embedded_chunks": len(embedded_records),
            "missing_embeddings_count": len(missing_chunk_ids),
            "duplicate_embedding_ids_count": len(duplicate_embedding_ids),
            "invalid_vectors_count": invalid_vectors_count,
            "dimension_mismatches_count": dim_mismatches_count,
            "nan_vectors_count": nan_vectors_count,
            "inf_vectors_count": inf_vectors_count,
            "non_numeric_count": non_numeric_count,
            "json_errors_count": json_errors_count,
            "error_count": len(errors),
            "warning_count": len(warnings),
            "errors": errors[:50],
            "is_valid": is_valid,
            "status": "PASS" if is_valid else "FAIL",
        }
