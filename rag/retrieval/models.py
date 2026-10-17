"""Data models and schemas for Step 6 Semantic Retrieval."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RetrievalResult:
    """Represents a single retrieved document chunk with semantic scores and metadata."""

    chunk_id: str
    document_id: int
    chunk_index: int
    content: str
    distance: float
    similarity_score: float
    document_title: Optional[str] = None
    source_path: Optional[str] = None
    content_type: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class RetrievalResponse:
    """Structured response container for semantic retrieval queries."""

    query: str
    top_k: int
    results: List[RetrievalResult]
    total_results: int
    embedding_time_ms: float
    retrieval_time_ms: float
    total_time_ms: float

    def to_dict(self) -> Dict[str, Any]:
        return {
            "query": self.query,
            "top_k": self.top_k,
            "results": [r.to_dict() for r in self.results],
            "total_results": self.total_results,
            "embedding_time_ms": round(self.embedding_time_ms, 2),
            "retrieval_time_ms": round(self.retrieval_time_ms, 2),
            "total_time_ms": round(self.total_time_ms, 2),
        }
