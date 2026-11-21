"""Pydantic schemas for System Infrastructure Health monitoring."""

from __future__ import annotations

from typing import Any, Dict, Literal, Optional
from pydantic import BaseModel, Field

ProviderStatus = Literal[
    "online",
    "offline",
    "degraded",
    "timeout",
    "not_configured",
    "loading",
    "unknown",
]

ProviderRole = Literal["primary", "fallback", "standby", "disabled"]


class ProviderHealthModel(BaseModel):
    """Health and reachability telemetry for an LLM provider."""

    name: str = Field(..., description="Unique provider identifier, e.g. 'groq', 'ollama', 'gemini'")
    display_name: str = Field(..., description="Display label for dashboard cards")
    status: ProviderStatus = Field(..., description="Computed operational health state")
    configured: bool = Field(..., description="Whether credentials or base URLs are configured")
    reachable: bool = Field(..., description="Whether live lightweight ping/check succeeded")
    is_active_selection: bool = Field(..., description="Whether this provider is currently active in routing")
    role: ProviderRole = Field(..., description="Role in application: primary, fallback, standby, or disabled")
    model: str = Field(..., description="Configured model identifier")
    base_url: Optional[str] = Field(None, description="Sanitized endpoint base URL")
    response_latency_ms: Optional[float] = Field(None, description="Round-trip probe latency in milliseconds")
    last_successful_check: Optional[str] = Field(None, description="ISO timestamp of last successful check")
    last_checked_at: str = Field(..., description="ISO timestamp of this evaluation")
    last_error: Optional[str] = Field(None, description="Sanitized error summary, never exposing credentials")
    detail: str = Field(..., description="Human-readable status summary")
    currently_processing: bool = Field(False, description="True if provider is actively handling an inference request")


class DatabaseHealthModel(BaseModel):
    """Health metrics for PostgreSQL and pgvector extension."""

    healthy: bool = Field(..., description="Whether database connection and queries succeed")
    status: ProviderStatus = Field(..., description="Operational status: online, offline, degraded")
    detail: str = Field(..., description="Connection status message")
    pgvector_enabled: bool = Field(..., description="Whether the 'vector' extension is installed in PostgreSQL")
    response_latency_ms: Optional[float] = Field(None, description="Query round-trip latency in milliseconds")
    last_checked_at: str = Field(..., description="ISO timestamp of this evaluation")
    chunk_count: Optional[int] = Field(None, description="Total number of document chunks indexed in database")


class EmbeddingServiceHealthModel(BaseModel):
    """Health metrics for the runtime text embedding model and vector schema."""

    healthy: bool = Field(..., description="Whether embedding service is operational and consistent with DB")
    status: ProviderStatus = Field(..., description="Operational status: online, offline, degraded")
    provider: str = Field(..., description="Embedding provider type: local, openai, or gemini")
    model_name: str = Field(..., description="Runtime embedding model name")
    dimensions: int = Field(..., description="Embedding vector dimensionality produced by model")
    db_vector_dimensions: Optional[int] = Field(None, description="Expected vector dimensionality configured in DB schema")
    schema_consistent: bool = Field(..., description="Whether model dimensions match database vector column schema")
    detail: str = Field(..., description="Status summary or discrepancy details")
    last_checked_at: str = Field(..., description="ISO timestamp of this evaluation")


class RetrievalServiceHealthModel(BaseModel):
    """Health metrics for RAG retrieval dependencies."""

    healthy: bool = Field(..., description="Whether retrieval pipeline dependencies are ready")
    status: ProviderStatus = Field(..., description="Operational status: online, offline, degraded")
    total_chunks: int = Field(0, description="Total searchable chunks available")
    detail: str = Field(..., description="Summary of retrieval system status")
    last_checked_at: str = Field(..., description="ISO timestamp of this evaluation")


class InfrastructureHealthResponse(BaseModel):
    """Unified system infrastructure health response schema."""

    status: Literal["healthy", "degraded", "unhealthy"] = Field(..., description="Overall infrastructure status")
    timestamp: str = Field(..., description="ISO timestamp of evaluation")
    active_primary_provider: str = Field(..., description="Name of primary LLM provider")
    active_fallback_provider: Optional[str] = Field(None, description="Name of fallback LLM provider, if configured")
    database: DatabaseHealthModel
    embedding_service: EmbeddingServiceHealthModel
    retrieval_service: RetrievalServiceHealthModel
    llm_providers: Dict[str, ProviderHealthModel]
    rag_metrics: Optional[Dict[str, Any]] = None
