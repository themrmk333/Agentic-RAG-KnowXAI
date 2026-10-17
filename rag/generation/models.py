"""Strongly typed response models for Step 8: LLM Answer Generation."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional

from rag.context.models import AssembledContext


@dataclass
class SourceReference:
    """Represents a citation to a specific chunk of knowledge used in the answer."""
    
    document_id: int
    chunk_id: str
    chunk_index: int
    document_title: Optional[str] = None
    source: Optional[str] = None
    snippet: str = ""
    semantic_score: float = 0.0
    rerank_score: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class GroundingValidationResult:
    """Contains the results of the factual grounding and safety validation checks."""
    
    status: str  # "PASS", "FAIL", "WARNING", "REJECTED"
    is_grounded: bool
    confidence: str  # "HIGH", "MEDIUM", "LOW", "INSUFFICIENT_CONTEXT"
    reason: Optional[str] = None
    unsupported_claims: List[str] = field(default_factory=list)
    citations_valid: bool = True
    context_used_count: int = 0
    total_context_items: int = 0
    checks: Dict[str, bool] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class GeneratedAnswer:
    """Raw generation output returned by an LLM Provider."""
    
    answer: str
    raw_text: str
    prompt_tokens: Optional[int] = None
    completion_tokens: Optional[int] = None
    total_tokens: Optional[int] = None
    model_name: str = ""
    provider_name: str = ""
    latency_ms: float = 0.0
    finish_reason: Optional[str] = None
    is_mock: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class GenerationRequest:
    """Input payload to the Answer Generator."""
    
    query: str
    assembled_context: Optional[AssembledContext] = None
    user_context: Optional[Dict[str, Any]] = None
    provider: Optional[str] = None
    model: Optional[str] = None
    temperature: float = 0.0
    max_tokens: Optional[int] = None
    stream: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        if self.assembled_context:
            d["assembled_context"] = self.assembled_context.to_dict()
        return d


@dataclass
class GenerationResponse:
    """Final, validated, traceable output from the Step 8 pipeline."""
    
    query: str
    answer: str
    grounded: bool
    confidence: str
    sources: List[SourceReference] = field(default_factory=list)
    context_items_used: int = 0
    validation_status: str = "PASS"
    validation_result: Optional[GroundingValidationResult] = None
    generation_metadata: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    failure_reason: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["sources"] = [s.to_dict() for s in self.sources]
        if self.validation_result:
            d["validation_result"] = self.validation_result.to_dict()
        return d
