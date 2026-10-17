"""Data models and schemas for Step 7 Context Reranking and Assembly."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RerankedResult:
    """Represents a retrieval candidate scored by the multi-factor reranker."""

    chunk_id: str
    document_id: int
    chunk_index: int
    content: str
    original_distance: float
    original_similarity_score: float
    original_rank: int
    semantic_score: float
    lexical_score: float
    phrase_score: float
    quality_score: float
    rerank_score: float
    document_title: Optional[str] = None
    source_path: Optional[str] = None
    content_type: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ContextItem:
    """Represents an assembled, LLM-ready context snippet with provenance and scores."""

    rank: int
    document_id: int
    chunk_id: str
    chunk_index: int
    text: str
    semantic_score: float
    rerank_score: float
    source: Optional[str] = None
    document_title: Optional[str] = None
    original_rank: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)
    character_count: int = 0
    token_count_estimate: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ContextMetadata:
    """Execution metadata and budget statistics for assembled context."""

    candidate_count: int = 0
    selected_count: int = 0
    duplicates_removed: int = 0
    diversity_filtered: int = 0
    budget_limited: int = 0
    min_score_filtered: int = 0
    total_characters: int = 0
    total_tokens_estimated: int = 0
    retrieval_time_ms: float = 0.0
    reranking_time_ms: float = 0.0
    assembly_time_ms: float = 0.0
    total_time_ms: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "candidate_count": self.candidate_count,
            "selected_count": self.selected_count,
            "duplicates_removed": self.duplicates_removed,
            "diversity_filtered": self.diversity_filtered,
            "budget_limited": self.budget_limited,
            "min_score_filtered": self.min_score_filtered,
            "total_characters": self.total_characters,
            "total_tokens_estimated": self.total_tokens_estimated,
            "retrieval_time_ms": round(self.retrieval_time_ms, 2),
            "reranking_time_ms": round(self.reranking_time_ms, 2),
            "assembly_time_ms": round(self.assembly_time_ms, 2),
            "total_time_ms": round(self.total_time_ms, 2),
        }


@dataclass
class AssembledContext:
    """Final assembled context payload ready for downstream LLM generation."""

    query: str
    items: List[ContextItem]
    metadata: ContextMetadata
    formatted_context: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "query": self.query,
            "items": [item.to_dict() for item in self.items],
            "metadata": self.metadata.to_dict(),
            "formatted_context": self.formatted_context,
        }
