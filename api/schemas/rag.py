"""Pydantic schemas for the RAG API endpoints."""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, constr


class RAGQueryRequest(BaseModel):
    """Input payload for a RAG query."""
    
    query: constr(min_length=1, max_length=2000, strip_whitespace=True) = Field(
        ..., 
        description="The natural language question or query.",
        examples=["What is the employee leave policy?"]
    )
    
    top_k: int = Field(
        default=5, 
        ge=1, 
        le=20, 
        description="Number of context items to retrieve before reranking."
    )
    
    provider: Optional[str] = Field(
        default=None, 
        description="LLM Provider override (e.g., 'mock', 'gemini', 'openrouter')."
    )
    
    max_context_items: int = Field(
        default=5, 
        ge=1, 
        le=10, 
        description="Maximum number of context chunks to assemble after reranking."
    )


class RAGSourceSchema(BaseModel):
    """Schema for a cited source in the RAG response."""
    
    document_id: int
    chunk_index: int
    title: Optional[str] = None
    source_path: Optional[str] = None
    score: float


class RAGRetrievalStats(BaseModel):
    """Retrieval statistics for the RAG response."""
    
    top_k_requested: int
    candidates_retrieved: int
    results_used: int


class RAGMetadataSchema(BaseModel):
    """Execution metadata and performance metrics."""
    
    provider: str
    model: str
    embedding_model: str
    is_mock: bool
    latency_ms: Dict[str, float] = Field(default_factory=dict)


class RAGQueryResponse(BaseModel):
    """Final structured API response containing the grounded answer."""
    
    query: str
    answer: str
    grounded: bool
    confidence: str
    sources: List[RAGSourceSchema]
    retrieval: RAGRetrievalStats
    metadata: RAGMetadataSchema
