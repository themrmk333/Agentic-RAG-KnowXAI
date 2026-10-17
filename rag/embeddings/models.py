"""
Data models, validation helpers, and data structures for Step 4 Embedding Generation.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Sequence


EXPECTED_VECTOR_DIMENSION = 384
DEFAULT_EMBEDDING_BATCH_SIZE = 64
DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_BASE_DELAY = 1.0
DEFAULT_REQUEST_TIMEOUT = 60.0


def utc_now_iso() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def validate_vector(vector: Sequence[float], expected_dim: int = EXPECTED_VECTOR_DIMENSION) -> tuple[bool, str]:
    """
    Validate a single embedding vector.
    Checks:
      - is sequence / list
      - length equals expected_dim
      - all elements are numeric
      - no NaN values
      - no Infinity values
    """
    if not isinstance(vector, (list, tuple)):
        return False, f"Vector must be a list or tuple, got {type(vector).__name__}"
    
    if len(vector) != expected_dim:
        return False, f"Dimension mismatch: expected {expected_dim}, got {len(vector)}"
    
    for idx, val in enumerate(vector):
        if not isinstance(val, (int, float)):
            return False, f"Non-numeric value at index {idx}: {val!r} ({type(val).__name__})"
        if math.isnan(val):
            return False, f"NaN value encountered at index {idx}"
        if math.isinf(val):
            return False, f"Infinity value encountered at index {idx}"
            
    return True, "OK"


def compute_dataset_fingerprint(chunks: Sequence[dict[str, Any] | InputChunk]) -> str:
    """
    Compute a deterministic SHA-256 fingerprint for a sequence of input chunk records.
    Uses chunk_id and chunk_sha256 in order.
    """
    hasher = hashlib.sha256()
    for chunk in chunks:
        if isinstance(chunk, InputChunk):
            cid = chunk.chunk_id
            csha = chunk.chunk_sha256
        elif isinstance(chunk, dict):
            cid = chunk.get("chunk_id", "")
            csha = chunk.get("chunk_sha256", "")
        else:
            cid = getattr(chunk, "chunk_id", "")
            csha = getattr(chunk, "chunk_sha256", "")
        hasher.update(f"{cid}:{csha}\n".encode("utf-8"))
    return hasher.hexdigest()


@dataclass
class InputChunk:
    """Represents a validated input chunk record from data/chunks/."""
    chunk_id: str
    batch_id: str
    source_file: str
    relative_path: str
    filename: str
    extension: str
    chunk_index: int
    total_chunks_for_file: int
    character_count: int
    word_count: int
    estimated_tokens: int
    source_sha256: str
    chunk_sha256: str
    heading_context: str
    chunking_strategy: str
    text: str
    created_at_utc: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> InputChunk:
        return cls(
            chunk_id=data["chunk_id"],
            batch_id=data.get("batch_id", ""),
            source_file=data.get("source_file", data.get("relative_path", "")),
            relative_path=data.get("relative_path", data.get("source_file", "")),
            filename=data.get("filename", ""),
            extension=data.get("extension", ""),
            chunk_index=int(data["chunk_index"]),
            total_chunks_for_file=int(data["total_chunks_for_file"]),
            character_count=int(data["character_count"]),
            word_count=int(data["word_count"]),
            estimated_tokens=int(data["estimated_tokens"]),
            source_sha256=data.get("source_sha256", ""),
            chunk_sha256=data.get("chunk_sha256", ""),
            heading_context=data.get("heading_context", ""),
            chunking_strategy=data.get("chunking_strategy", ""),
            text=data["text"],
            created_at_utc=data.get("created_at_utc", ""),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class EmbeddingRecord:
    """Represents a finalized embedding record saved in data/embeddings/step4/embeddings/."""
    chunk_id: str
    batch_id: str
    source_file: str
    relative_path: str
    chunk_index: int
    total_chunks_for_file: int
    chunk_sha256: str
    embedding_model: str
    embedding_dimension: int
    embedding: list[float]
    created_at_utc: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_jsonl_line(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)


@dataclass
class CheckpointState:
    """State stored in checkpoint.json to enable safe resumption."""
    timestamp_utc: str
    embedding_model: str
    embedding_dimension: int
    input_fingerprint: str
    total_input_chunks: int
    completed_chunks_count: int
    completed_batches_count: int
    last_completed_batch_id: str | None = None
    completed_chunk_ids: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CheckpointState:
        return cls(
            timestamp_utc=data.get("timestamp_utc", utc_now_iso()),
            embedding_model=data.get("embedding_model", ""),
            embedding_dimension=int(data.get("embedding_dimension", EXPECTED_VECTOR_DIMENSION)),
            input_fingerprint=data.get("input_fingerprint", ""),
            total_input_chunks=int(data.get("total_input_chunks", 0)),
            completed_chunks_count=int(data.get("completed_chunks_count", 0)),
            completed_batches_count=int(data.get("completed_batches_count", 0)),
            last_completed_batch_id=data.get("last_completed_batch_id"),
            completed_chunk_ids=data.get("completed_chunk_ids", []),
        )
