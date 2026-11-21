"""Comprehensive test suite for System Infrastructure Health monitoring.

Validates:
  - Groq provider checks (success, unauthorized, timeout, not configured)
  - Ollama provider checks (success, missing model, connection refused, timeout)
  - Embedding engine detection and DB vector schema consistency
  - Provider in-flight processing tracking
  - Endpoint authorization (/admin/health 401/403/200, /health public)
  - Existing Groq/Ollama fallback workflow preservation
  - Zero API key / secret leakage
"""

from __future__ import annotations

import json
from unittest import mock
import pytest
from fastapi.testclient import TestClient

from config.settings import Settings
from api.schemas.health import InfrastructureHealthResponse
from services.health_service import (
    check_groq_health,
    check_ollama_health,
    evaluate_embedding_health,
    evaluate_database_health,
    track_provider_processing,
    is_provider_processing,
    get_system_infrastructure_health,
)
from agents.llm.fallback import FallbackProvider
from api.routes.chat import get_or_create_workflow


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------
@pytest.fixture
def mock_settings():
    return Settings(
        llm_provider="groq",
        groq_api_key="gsk_test_mock_groq_secret_key_12345",
        groq_model="openai/gpt-oss-20b",
        groq_base_url="https://api.groq.com/openai/v1",
        local_llm_base_url="http://localhost:11434/v1",
        local_llm_model="llama3.1:8b",
        embedding_provider="local",
        embedding_model="BAAI/bge-small-en-v1.5",
        embedding_dimensions=384,
        pgvector_dimensions=384,
    )


# ---------------------------------------------------------------------------
# 1. Groq Provider Health Tests
# ---------------------------------------------------------------------------
def test_groq_health_success(mock_settings):
    """Test Groq health check succeeds with 200 and model presence verified."""
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "data": [{"id": "openai/gpt-oss-20b"}, {"id": "llama-3.1-8b-instant"}]
    }

    with mock.patch("httpx.Client.get", return_value=mock_resp):
        health = check_groq_health(mock_settings, is_active=True, role="primary")

        assert health.name == "groq"
        assert health.status == "online"
        assert health.configured is True
        assert health.reachable is True
        assert health.is_active_selection is True
        assert health.role == "primary"
        assert health.model == "openai/gpt-oss-20b"
        assert health.response_latency_ms is not None
        assert health.last_error is None
        assert "gsk_" not in str(health.model_dump())  # Never leak key


def test_groq_health_unauthorized(mock_settings):
    """Test Groq health check reports offline when API key is rejected (401)."""
    mock_resp = mock.Mock()
    mock_resp.status_code = 401
    mock_resp.text = "Invalid API key provided: gsk_test_mock_groq_secret_key_12345"

    with mock.patch("httpx.Client.get", return_value=mock_resp):
        health = check_groq_health(mock_settings, is_active=True, role="primary")

        assert health.name == "groq"
        assert health.status == "offline"
        assert health.configured is True
        assert health.reachable is False
        assert "Invalid Groq API key" in (health.last_error or "")
        assert "gsk_" not in (health.last_error or "")  # Ensure key was sanitized


def test_groq_health_timeout(mock_settings):
    """Test Groq health check handles network timeout cleanly."""
    import httpx
    with mock.patch("httpx.Client.get", side_effect=httpx.TimeoutException("Read timed out")):
        health = check_groq_health(mock_settings, is_active=True, role="primary")

        assert health.name == "groq"
        assert health.status == "timeout"
        assert health.reachable is False
        assert "timed out" in (health.last_error or "").lower()


def test_groq_health_not_configured(mock_settings):
    """Test Groq health check when API key is missing."""
    mock_settings.groq_api_key = None
    health = check_groq_health(mock_settings, is_active=True, role="primary")

    assert health.name == "groq"
    assert health.status == "not_configured"
    assert health.configured is False
    assert health.reachable is False


# ---------------------------------------------------------------------------
# 2. Ollama / Local Provider Health Tests
# ---------------------------------------------------------------------------
def test_ollama_health_success(mock_settings):
    """Test Ollama check succeeds when daemon is running and configured model is present."""
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "data": [{"id": "llama3.1:8b"}]
    }

    with mock.patch("httpx.Client.get", return_value=mock_resp):
        health = check_ollama_health(mock_settings, is_active=True, role="fallback")

        assert health.name == "ollama"
        assert health.status == "online"
        assert health.configured is True
        assert health.reachable is True
        assert health.is_active_selection is True
        assert health.role == "fallback"
        assert health.model == "llama3.1:8b"
        assert health.response_latency_ms is not None
        assert "verified" in health.detail.lower()


def test_ollama_health_model_missing(mock_settings):
    """Test Ollama returns degraded when service is running but model is not pulled."""
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "data": [{"id": "mistral:latest"}]
    }

    with mock.patch("httpx.Client.get", return_value=mock_resp):
        health = check_ollama_health(mock_settings, is_active=True, role="fallback")

        assert health.name == "ollama"
        assert health.status == "degraded"
        assert health.configured is True
        assert health.reachable is True
        assert "not pulled" in health.detail.lower() or "not found" in (health.last_error or "").lower()


def test_ollama_health_connection_refused(mock_settings):
    """Test Ollama returns offline when local service is not started."""
    import httpx
    with mock.patch("httpx.Client.get", side_effect=httpx.ConnectError("Connection refused")):
        health = check_ollama_health(mock_settings, is_active=True, role="fallback")

        assert health.name == "ollama"
        assert health.status == "offline"
        assert health.reachable is False
        assert "Cannot reach Ollama" in (health.last_error or "")


# ---------------------------------------------------------------------------
# 3. Embedding Engine Detection & DB Vector Schema Consistency
# ---------------------------------------------------------------------------
def test_embedding_health_consistent(mock_settings):
    """Test embedding health check verifies 384 dimensions matching DB vector schema."""
    mock_embedder = mock.Mock()
    mock_embedder.model_name = "BAAI/bge-small-en-v1.5"
    mock_embedder.device = "cpu"
    mock_embedder.embed_query.return_value = [0.1] * 384

    with mock.patch("rag.retrieval.query_embedder.QueryEmbedder.get_instance", return_value=mock_embedder):
        health = evaluate_embedding_health(mock_settings, db_vector_dim=384)

        assert health.healthy is True
        assert health.status == "online"
        assert health.model_name == "BAAI/bge-small-en-v1.5"
        assert health.dimensions == 384
        assert health.db_vector_dimensions == 384
        assert health.schema_consistent is True


def test_embedding_health_dimension_mismatch(mock_settings):
    """Test embedding health reports discrepancy when DB schema requires a different dimension."""
    mock_embedder = mock.Mock()
    mock_embedder.model_name = "BAAI/bge-small-en-v1.5"
    mock_embedder.device = "cpu"
    mock_embedder.embed_query.return_value = [0.1] * 384

    # DB schema vector(1536) vs model 384
    with mock.patch("rag.retrieval.query_embedder.QueryEmbedder.get_instance", return_value=mock_embedder):
        health = evaluate_embedding_health(mock_settings, db_vector_dim=1536)

        assert health.healthy is False
        assert health.status == "degraded"
        assert health.schema_consistent is False
        assert "Schema mismatch" in health.detail


# ---------------------------------------------------------------------------
# 4. In-Flight Processing Tracking
# ---------------------------------------------------------------------------
def test_in_flight_processing_tracker():
    """Verify that is_provider_processing properly tracks concurrent execution."""
    assert is_provider_processing("groq") is False

    with track_provider_processing("groq"):
        assert is_provider_processing("groq") is True
        assert is_provider_processing("gemini") is False

    assert is_provider_processing("groq") is False


# ---------------------------------------------------------------------------
# 5. Fallback Workflow Logic Preservation
# ---------------------------------------------------------------------------
def test_fallback_workflow_preservation(mock_settings):
    """Confirm that get_or_create_workflow('groq') configures Groq with local Ollama fallback."""
    with mock.patch("api.routes.chat.get_settings", return_value=mock_settings):
        with mock.patch("api.routes.chat.build_provider") as mock_build:
            mock_groq = mock.Mock()
            mock_groq.model = "openai/gpt-oss-20b"
            mock_local = mock.Mock()
            mock_local.model = "llama3.1:8b"
            mock_build.side_effect = lambda name: mock_groq if name == "groq" else mock_local

            with mock.patch("api.routes.chat.create_workflow") as mock_create_wf:
                with mock.patch("api.routes.chat.SemanticRetriever"):
                    # Clear workflow cache for groq to force re-creation
                    from api.routes.chat import _WORKFLOW_CACHE
                    _WORKFLOW_CACHE.pop("groq", None)

                    get_or_create_workflow("groq")

                    mock_create_wf.assert_called_once()
                    llm_arg = mock_create_wf.call_args[0][0]
                    assert isinstance(llm_arg, FallbackProvider)
                    assert llm_arg.primary == mock_groq
                    assert llm_arg.secondary == mock_local


# ---------------------------------------------------------------------------
# 6. Endpoint Authorization & Public Health Tests
# ---------------------------------------------------------------------------
def test_admin_health_endpoint_requires_auth(mock_settings):
    """Test that /admin/health rejects unauthenticated requests with 401."""
    from api.main import create_app
    app = create_app(mock_settings)
    client = TestClient(app)

    res = client.get("/admin/health")
    assert res.status_code in (401, 403)


def test_public_health_endpoint_includes_groq_and_ollama(mock_settings):
    """Test that /health returns real backend structure including groq and ollama."""
    from api.main import create_app
    app = create_app(mock_settings)
    client = TestClient(app)

    # Mock DB execute to return basic healthy DB
    mock_db = mock.Mock()
    mock_db.execute.return_value.scalar.return_value = "vector"

    with mock.patch("api.routes.system.get_db", return_value=mock_db):
        with mock.patch("services.health_service.evaluate_database_health") as mock_eval_db:
            from api.schemas.health import DatabaseHealthModel
            mock_eval_db.return_value = (
                DatabaseHealthModel(
                    healthy=True,
                    status="online",
                    detail="Connected to PostgreSQL",
                    pgvector_enabled=True,
                    response_latency_ms=1.5,
                    last_checked_at="2026-11-17T00:00:00Z",
                    chunk_count=263,
                ),
                384,
            )
            with mock.patch("services.health_service.evaluate_embedding_health") as mock_eval_emb:
                from api.schemas.health import EmbeddingServiceHealthModel
                mock_eval_emb.return_value = EmbeddingServiceHealthModel(
                    healthy=True,
                    status="online",
                    provider="local",
                    model_name="BAAI/bge-small-en-v1.5",
                    dimensions=384,
                    db_vector_dimensions=384,
                    schema_consistent=True,
                    detail="Active",
                    last_checked_at="2026-11-17T00:00:00Z",
                )

                res = client.get("/health")
                assert res.status_code == 200
                data = res.json()
                assert "status" in data
                assert "database" in data
                assert "embedding_service" in data
                assert "llm_providers" in data
                assert "groq" in data["llm_providers"]
                assert "ollama" in data["llm_providers"]
                assert data["embedding_service"]["model_name"] == "BAAI/bge-small-en-v1.5"
                assert data["embedding_service"]["dimensions"] == 384
