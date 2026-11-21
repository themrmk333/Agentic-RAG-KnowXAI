"""Comprehensive System Infrastructure Health Service.

Evaluates real-time health for:
  - LLM Providers (Groq primary, Ollama/local fallback, Gemini, NVIDIA, OpenRouter)
  - Embedding Engine (runtime model, dimensionality, database vector schema verification)
  - PostgreSQL & pgvector extension
  - Search & Retrieval dependencies
Includes lightweight non-inference probes, thread-safe request tracking,
rate-limiting, timeout controls, and zero secret leakage.
"""

from __future__ import annotations

import logging
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import httpx
from sqlalchemy import text
from sqlalchemy.orm import Session

from api.schemas.health import (
    DatabaseHealthModel,
    EmbeddingServiceHealthModel,
    InfrastructureHealthResponse,
    ProviderHealthModel,
    ProviderRole,
    ProviderStatus,
    RetrievalServiceHealthModel,
)
from config.settings import Settings, get_settings
from rag.telemetry.metrics import RagMetricsStore

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# In-Flight LLM Request Tracker (Thread-Safe)
# ---------------------------------------------------------------------------
_ACTIVE_IN_FLIGHT_LOCK = threading.Lock()
_ACTIVE_IN_FLIGHT_COUNTS: Dict[str, int] = {
    "groq": 0,
    "local": 0,
    "ollama": 0,
    "gemini": 0,
    "nvidia": 0,
    "openrouter": 0,
}


@contextmanager
def track_provider_processing(provider_name: str):
    """Context manager to track live in-flight LLM requests."""
    key = provider_name.lower().strip()
    with _ACTIVE_IN_FLIGHT_LOCK:
        _ACTIVE_IN_FLIGHT_COUNTS[key] = _ACTIVE_IN_FLIGHT_COUNTS.get(key, 0) + 1
        if key == "local":
            _ACTIVE_IN_FLIGHT_COUNTS["ollama"] = _ACTIVE_IN_FLIGHT_COUNTS.get("ollama", 0) + 1
        elif key == "ollama":
            _ACTIVE_IN_FLIGHT_COUNTS["local"] = _ACTIVE_IN_FLIGHT_COUNTS.get("local", 0) + 1
    try:
        yield
    finally:
        with _ACTIVE_IN_FLIGHT_LOCK:
            if key in _ACTIVE_IN_FLIGHT_COUNTS and _ACTIVE_IN_FLIGHT_COUNTS[key] > 0:
                _ACTIVE_IN_FLIGHT_COUNTS[key] -= 1
            if key == "local" and _ACTIVE_IN_FLIGHT_COUNTS.get("ollama", 0) > 0:
                _ACTIVE_IN_FLIGHT_COUNTS["ollama"] -= 1
            elif key == "ollama" and _ACTIVE_IN_FLIGHT_COUNTS.get("local", 0) > 0:
                _ACTIVE_IN_FLIGHT_COUNTS["local"] -= 1


def is_provider_processing(provider_name: str) -> bool:
    """Return whether a provider currently has an active request executing."""
    key = provider_name.lower().strip()
    with _ACTIVE_IN_FLIGHT_LOCK:
        return _ACTIVE_IN_FLIGHT_COUNTS.get(key, 0) > 0


# ---------------------------------------------------------------------------
# Last Successful Check Timestamps (Persistent in process memory)
# ---------------------------------------------------------------------------
_LAST_SUCCESS_TIMESTAMPS: Dict[str, str] = {}

# ---------------------------------------------------------------------------
# Health Evaluation Cache
# ---------------------------------------------------------------------------
_CACHE_LOCK = threading.Lock()
_CACHED_RESPONSE: Optional[InfrastructureHealthResponse] = None
_CACHED_AT: float = 0.0
_CACHE_TTL_SECONDS: float = 15.0
_MIN_REFRESH_INTERVAL_SECONDS: float = 2.0  # Rate limit force refresh


def _sanitize_error(error_msg: str) -> str:
    """Remove potential API keys or sensitive auth tokens from error strings."""
    if not error_msg:
        return "Unknown error"
    # Redact common API key patterns (Groq, OpenAI, Google, OpenRouter, hex)
    sanitized = re.sub(r"gsk_[A-Za-z0-9_-]{10,}", "[REDACTED_GROQ_KEY]", error_msg)
    sanitized = re.sub(r"sk-[A-Za-z0-9_-]{10,}", "[REDACTED_KEY]", sanitized)
    sanitized = re.sub(r"Bearer\s+[A-Za-z0-9_.-]+", "Bearer [REDACTED]", sanitized, flags=re.IGNORECASE)
    sanitized = re.sub(r"key=[A-Za-z0-9_-]{10,}", "key=[REDACTED]", sanitized, flags=re.IGNORECASE)
    return sanitized.strip()


def _get_secret_val(secret: Any) -> Optional[str]:
    if secret is None:
        return None
    val = secret.get_secret_value()
    return val.strip() if val and val.strip() else None


# ---------------------------------------------------------------------------
# Lightweight Provider Health Probes
# ---------------------------------------------------------------------------
def check_groq_health(
    settings: Settings,
    is_active: bool,
    role: ProviderRole,
) -> ProviderHealthModel:
    """Validate Groq provider using authenticated lightweight /models probe."""
    now_iso = datetime.now(timezone.utc).isoformat()
    api_key = _get_secret_val(settings.groq_api_key)
    base_url = settings.groq_base_url.rstrip("/")
    model = settings.groq_model
    currently_proc = is_provider_processing("groq")

    if not api_key:
        return ProviderHealthModel(
            name="groq",
            display_name="Groq Cloud",
            status="not_configured",
            configured=False,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=None,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("groq"),
            last_checked_at=now_iso,
            last_error="GROQ_API_KEY is not configured in environment.",
            detail="Provider not configured",
            currently_processing=currently_proc,
        )

    t0 = time.perf_counter()
    try:
        # Lightweight authenticated check via /models endpoint (no inference tokens consumed)
        with httpx.Client(timeout=3.0) as client:
            resp = client.get(
                f"{base_url}/models",
                headers={"Authorization": f"Bearer {api_key}"},
            )
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)

        if resp.status_code == 200:
            data = resp.json().get("data", [])
            available_ids = [m.get("id") for m in data if isinstance(m, dict)]
            model_present = model in available_ids or any(model.split("/")[-1] in aid for aid in available_ids)

            _LAST_SUCCESS_TIMESTAMPS["groq"] = now_iso
            status: ProviderStatus = "online"
            detail = f"Operational ({latency_ms}ms, {len(available_ids)} models available)"
            if not model_present and available_ids:
                status = "degraded"
                detail = f"Operational but model '{model}' not found in available list"

            return ProviderHealthModel(
                name="groq",
                display_name="Groq Cloud",
                status=status,
                configured=True,
                reachable=True,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=now_iso,
                last_checked_at=now_iso,
                last_error=None,
                detail=detail,
                currently_processing=currently_proc,
            )
        elif resp.status_code == 401:
            return ProviderHealthModel(
                name="groq",
                display_name="Groq Cloud",
                status="offline",
                configured=True,
                reachable=False,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("groq"),
                last_checked_at=now_iso,
                last_error="Authentication failed: Invalid Groq API key (HTTP 401).",
                detail="Invalid API key",
                currently_processing=currently_proc,
            )
        elif resp.status_code == 429:
            return ProviderHealthModel(
                name="groq",
                display_name="Groq Cloud",
                status="degraded",
                configured=True,
                reachable=True,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("groq"),
                last_checked_at=now_iso,
                last_error="Groq API rate limit or quota exceeded (HTTP 429).",
                detail="Rate limit exceeded",
                currently_processing=currently_proc,
            )
        else:
            return ProviderHealthModel(
                name="groq",
                display_name="Groq Cloud",
                status="offline",
                configured=True,
                reachable=False,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("groq"),
                last_checked_at=now_iso,
                last_error=f"Groq returned unexpected HTTP status {resp.status_code}.",
                detail=f"HTTP {resp.status_code} error",
                currently_processing=currently_proc,
            )
    except httpx.TimeoutException:
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        return ProviderHealthModel(
            name="groq",
            display_name="Groq Cloud",
            status="timeout",
            configured=True,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=latency_ms,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("groq"),
            last_checked_at=now_iso,
            last_error="Connection to Groq API timed out after 3.0s.",
            detail="Request timeout",
            currently_processing=currently_proc,
        )
    except Exception as exc:
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        clean_err = _sanitize_error(str(exc))
        return ProviderHealthModel(
            name="groq",
            display_name="Groq Cloud",
            status="offline",
            configured=True,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=latency_ms,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("groq"),
            last_checked_at=now_iso,
            last_error=f"Network error: {clean_err}",
            detail="Connection failed",
            currently_processing=currently_proc,
        )


def check_ollama_health(
    settings: Settings,
    is_active: bool,
    role: ProviderRole,
) -> ProviderHealthModel:
    """Validate Ollama local LLM service and verify configured model availability."""
    now_iso = datetime.now(timezone.utc).isoformat()
    base_url = settings.local_llm_base_url.rstrip("/")
    model = settings.local_llm_model
    currently_proc = is_provider_processing("ollama") or is_provider_processing("local")

    if not base_url:
        return ProviderHealthModel(
            name="ollama",
            display_name="Ollama (Local LLM)",
            status="not_configured",
            configured=False,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=None,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("ollama"),
            last_checked_at=now_iso,
            last_error="LOCAL_LLM_BASE_URL is not configured.",
            detail="Provider not configured",
            currently_processing=currently_proc,
        )

    t0 = time.perf_counter()
    try:
        # First attempt /v1/models (OpenAI compatibility endpoint on Ollama)
        with httpx.Client(timeout=3.0) as client:
            resp = client.get(f"{base_url}/models")
            if resp.status_code != 200:
                # Fallback to Ollama native /api/tags if /v1/models returns non-200
                root_url = base_url.replace("/v1", "").rstrip("/")
                resp = client.get(f"{root_url}/api/tags")

        latency_ms = round((time.perf_counter() - t0) * 1000, 1)

        if resp.status_code == 200:
            json_body = resp.json()
            available_models: List[str] = []

            # Extract model names from either /v1/models or /api/tags structure
            if "data" in json_body and isinstance(json_body["data"], list):
                available_models = [m.get("id", "") for m in json_body["data"] if isinstance(m, dict)]
            elif "models" in json_body and isinstance(json_body["models"], list):
                available_models = [m.get("name", "") for m in json_body["models"] if isinstance(m, dict)]

            # Check model presence (exact match or prefix match like llama3.1 vs llama3.1:8b)
            model_target = model.lower()
            model_found = any(
                m.lower() == model_target
                or m.lower().startswith(f"{model_target}:")
                or model_target.startswith(f"{m.lower()}:")
                for m in available_models
            )

            _LAST_SUCCESS_TIMESTAMPS["ollama"] = now_iso
            _LAST_SUCCESS_TIMESTAMPS["local"] = now_iso

            if model_found:
                status: ProviderStatus = "online"
                detail = f"Operational ({latency_ms}ms, model '{model}' verified)"
                last_err = None
            else:
                status = "degraded"
                detail = f"Ollama running ({latency_ms}ms) but configured model '{model}' not pulled"
                last_err = f"Configured model '{model}' not found in local models: {available_models}"

            return ProviderHealthModel(
                name="ollama",
                display_name="Ollama (Local LLM)",
                status=status,
                configured=True,
                reachable=True,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=now_iso,
                last_checked_at=now_iso,
                last_error=last_err,
                detail=detail,
                currently_processing=currently_proc,
            )
        else:
            return ProviderHealthModel(
                name="ollama",
                display_name="Ollama (Local LLM)",
                status="offline",
                configured=True,
                reachable=False,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("ollama"),
                last_checked_at=now_iso,
                last_error=f"Ollama returned HTTP status {resp.status_code}.",
                detail="Unexpected HTTP response",
                currently_processing=currently_proc,
            )
    except httpx.TimeoutException:
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        return ProviderHealthModel(
            name="ollama",
            display_name="Ollama (Local LLM)",
            status="timeout",
            configured=True,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=latency_ms,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("ollama"),
            last_checked_at=now_iso,
            last_error="Connection to Ollama service timed out after 3.0s.",
            detail="Request timeout",
            currently_processing=currently_proc,
        )
    except Exception as exc:
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        clean_err = _sanitize_error(str(exc))
        return ProviderHealthModel(
            name="ollama",
            display_name="Ollama (Local LLM)",
            status="offline",
            configured=True,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=latency_ms,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("ollama"),
            last_checked_at=now_iso,
            last_error=f"Cannot reach Ollama at {base_url}. Service may not be started.",
            detail="Service unreachable",
            currently_processing=currently_proc,
        )


def check_gemini_health(
    settings: Settings,
    is_active: bool,
    role: ProviderRole,
) -> ProviderHealthModel:
    """Validate Gemini provider."""
    now_iso = datetime.now(timezone.utc).isoformat()
    api_key = _get_secret_val(settings.gemini_api_key)
    model = settings.gemini_model
    currently_proc = is_provider_processing("gemini")

    if not api_key:
        return ProviderHealthModel(
            name="gemini",
            display_name="Google Gemini",
            status="not_configured",
            configured=False,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url="https://generativelanguage.googleapis.com",
            response_latency_ms=None,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("gemini"),
            last_checked_at=now_iso,
            last_error="GEMINI_API_KEY is not configured.",
            detail="Provider not configured",
            currently_processing=currently_proc,
        )

    t0 = time.perf_counter()
    try:
        # Lightweight check: list models
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
        with httpx.Client(timeout=3.0) as client:
            resp = client.get(url)
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)

        if resp.status_code == 200:
            _LAST_SUCCESS_TIMESTAMPS["gemini"] = now_iso
            return ProviderHealthModel(
                name="gemini",
                display_name="Google Gemini",
                status="online",
                configured=True,
                reachable=True,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url="https://generativelanguage.googleapis.com",
                response_latency_ms=latency_ms,
                last_successful_check=now_iso,
                last_checked_at=now_iso,
                last_error=None,
                detail=f"Operational ({latency_ms}ms)",
                currently_processing=currently_proc,
            )
        else:
            return ProviderHealthModel(
                name="gemini",
                display_name="Google Gemini",
                status="offline",
                configured=True,
                reachable=False,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url="https://generativelanguage.googleapis.com",
                response_latency_ms=latency_ms,
                last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("gemini"),
                last_checked_at=now_iso,
                last_error=f"Gemini API returned HTTP status {resp.status_code}.",
                detail="Authentication or quota error",
                currently_processing=currently_proc,
            )
    except httpx.TimeoutException:
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        return ProviderHealthModel(
            name="gemini",
            display_name="Google Gemini",
            status="timeout",
            configured=True,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url="https://generativelanguage.googleapis.com",
            response_latency_ms=latency_ms,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("gemini"),
            last_checked_at=now_iso,
            last_error="Connection timed out after 3.0s.",
            detail="Request timeout",
            currently_processing=currently_proc,
        )
    except Exception as exc:
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        return ProviderHealthModel(
            name="gemini",
            display_name="Google Gemini",
            status="offline",
            configured=True,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url="https://generativelanguage.googleapis.com",
            response_latency_ms=latency_ms,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("gemini"),
            last_checked_at=now_iso,
            last_error=_sanitize_error(str(exc)),
            detail="Connection failed",
            currently_processing=currently_proc,
        )


def check_nvidia_health(
    settings: Settings,
    is_active: bool,
    role: ProviderRole,
) -> ProviderHealthModel:
    """Validate NVIDIA NIM provider."""
    now_iso = datetime.now(timezone.utc).isoformat()
    api_key = _get_secret_val(settings.nvidia_api_key)
    base_url = settings.nvidia_base_url.rstrip("/")
    model = settings.nvidia_model
    currently_proc = is_provider_processing("nvidia")

    if not api_key:
        return ProviderHealthModel(
            name="nvidia",
            display_name="NVIDIA NIM",
            status="not_configured",
            configured=False,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=None,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("nvidia"),
            last_checked_at=now_iso,
            last_error="NVIDIA_API_KEY is not configured.",
            detail="Provider not configured",
            currently_processing=currently_proc,
        )

    t0 = time.perf_counter()
    try:
        with httpx.Client(timeout=3.0) as client:
            resp = client.get(f"{base_url}/models", headers={"Authorization": f"Bearer {api_key}"})
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        if resp.status_code == 200:
            _LAST_SUCCESS_TIMESTAMPS["nvidia"] = now_iso
            return ProviderHealthModel(
                name="nvidia",
                display_name="NVIDIA NIM",
                status="online",
                configured=True,
                reachable=True,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=now_iso,
                last_checked_at=now_iso,
                last_error=None,
                detail=f"Operational ({latency_ms}ms)",
                currently_processing=currently_proc,
            )
        else:
            return ProviderHealthModel(
                name="nvidia",
                display_name="NVIDIA NIM",
                status="offline",
                configured=True,
                reachable=False,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("nvidia"),
                last_checked_at=now_iso,
                last_error=f"NVIDIA API returned HTTP {resp.status_code}.",
                detail="Endpoint check failed",
                currently_processing=currently_proc,
            )
    except Exception as exc:
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        return ProviderHealthModel(
            name="nvidia",
            display_name="NVIDIA NIM",
            status="offline",
            configured=True,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=latency_ms,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("nvidia"),
            last_checked_at=now_iso,
            last_error=_sanitize_error(str(exc)),
            detail="Connection failed",
            currently_processing=currently_proc,
        )


def check_openrouter_health(
    settings: Settings,
    is_active: bool,
    role: ProviderRole,
) -> ProviderHealthModel:
    """Validate OpenRouter provider."""
    now_iso = datetime.now(timezone.utc).isoformat()
    api_key = _get_secret_val(settings.gemini_api_key)
    base_url = settings.openrouter_base_url.rstrip("/")
    model = settings.gemini_openrouter_model
    currently_proc = is_provider_processing("openrouter")

    from agents.llm.providers import is_openrouter_key

    is_openrouter = bool(api_key and is_openrouter_key(api_key))

    if not is_openrouter:
        return ProviderHealthModel(
            name="openrouter",
            display_name="OpenRouter Gateway",
            status="not_configured",
            configured=False,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=None,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("openrouter"),
            last_checked_at=now_iso,
            last_error="OpenRouter key is not configured.",
            detail="Provider not configured",
            currently_processing=currently_proc,
        )

    t0 = time.perf_counter()
    try:
        with httpx.Client(timeout=3.0) as client:
            resp = client.get(f"{base_url}/models", headers={"Authorization": f"Bearer {api_key}"})
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        if resp.status_code == 200:
            _LAST_SUCCESS_TIMESTAMPS["openrouter"] = now_iso
            return ProviderHealthModel(
                name="openrouter",
                display_name="OpenRouter Gateway",
                status="online",
                configured=True,
                reachable=True,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=now_iso,
                last_checked_at=now_iso,
                last_error=None,
                detail=f"Operational ({latency_ms}ms)",
                currently_processing=currently_proc,
            )
        else:
            return ProviderHealthModel(
                name="openrouter",
                display_name="OpenRouter Gateway",
                status="offline",
                configured=True,
                reachable=False,
                is_active_selection=is_active,
                role=role,
                model=model,
                base_url=base_url,
                response_latency_ms=latency_ms,
                last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("openrouter"),
                last_checked_at=now_iso,
                last_error=f"OpenRouter returned HTTP {resp.status_code}.",
                detail="Endpoint check failed",
                currently_processing=currently_proc,
            )
    except Exception as exc:
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        return ProviderHealthModel(
            name="openrouter",
            display_name="OpenRouter Gateway",
            status="offline",
            configured=True,
            reachable=False,
            is_active_selection=is_active,
            role=role,
            model=model,
            base_url=base_url,
            response_latency_ms=latency_ms,
            last_successful_check=_LAST_SUCCESS_TIMESTAMPS.get("openrouter"),
            last_checked_at=now_iso,
            last_error=_sanitize_error(str(exc)),
            detail="Connection failed",
            currently_processing=currently_proc,
        )


# ---------------------------------------------------------------------------
# Database & Embedding Health Evaluation
# ---------------------------------------------------------------------------
def evaluate_database_health(db: Session) -> Tuple[DatabaseHealthModel, Optional[int]]:
    """Inspect PostgreSQL connectivity, latency, pgvector extension, and indexed chunks."""
    now_iso = datetime.now(timezone.utc).isoformat()
    t0 = time.perf_counter()
    try:
        db.execute(text("SELECT 1"))
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)

        ext_check = db.execute(text("SELECT extname FROM pg_extension WHERE extname = 'vector'")).scalar()
        pgvector_ok = ext_check == "vector"

        # Query total indexed chunks
        chunk_count = None
        try:
            chunk_count = db.execute(text("SELECT count(*) FROM document_chunks")).scalar()
        except Exception:
            pass

        # Query vector column dimension from pg_attribute
        db_dim = None
        try:
            col_type = db.execute(text("""
                SELECT format_type(atttypid, atttypmod)
                FROM pg_attribute
                WHERE attrelid = 'document_chunks'::regclass
                  AND attname = 'embedding'
                  AND NOT attisdropped
            """)).scalar()
            if col_type and "vector(" in col_type:
                match = re.search(r"vector\((\d+)\)", col_type)
                if match:
                    db_dim = int(match.group(1))
        except Exception:
            pass

        status: ProviderStatus = "online" if pgvector_ok else "degraded"
        detail = "Connected to PostgreSQL database with pgvector extension." if pgvector_ok else "Connected, but pgvector extension is missing."

        db_model = DatabaseHealthModel(
            healthy=pgvector_ok,
            status=status,
            detail=detail,
            pgvector_enabled=pgvector_ok,
            response_latency_ms=latency_ms,
            last_checked_at=now_iso,
            chunk_count=chunk_count,
        )
        return db_model, db_dim
    except Exception as exc:
        latency_ms = round((time.perf_counter() - t0) * 1000, 1)
        clean_err = _sanitize_error(str(exc))
        db_model = DatabaseHealthModel(
            healthy=False,
            status="offline",
            detail=f"Database connection failed: {clean_err}",
            pgvector_enabled=False,
            response_latency_ms=latency_ms,
            last_checked_at=now_iso,
            chunk_count=None,
        )
        return db_model, None


def evaluate_embedding_health(
    settings: Settings,
    db_vector_dim: Optional[int],
) -> EmbeddingServiceHealthModel:
    """Validate runtime embedding model and verify consistency against database vector schema."""
    now_iso = datetime.now(timezone.utc).isoformat()
    runtime_model = settings.embedding_model
    configured_dim = settings.embedding_dimensions
    provider = getattr(settings, "embedding_provider", "local")

    # Target DB dimension is either queried from pg_attribute or settings
    expected_db_dim = db_vector_dim or settings.pgvector_dimensions
    schema_consistent = configured_dim == expected_db_dim

    # Verify query embedder can produce the expected vector
    emb_healthy = False
    detail = "Initializing embedder check..."
    try:
        from rag.retrieval.query_embedder import QueryEmbedder
        embedder = QueryEmbedder.get_instance()
        vec = embedder.embed_query("health check")
        actual_len = len(vec) if vec else 0

        if actual_len == configured_dim and schema_consistent:
            emb_healthy = True
            detail = f"Active ({runtime_model}, dim={actual_len}, device={embedder.device}, schema=vector({expected_db_dim}))"
        elif actual_len != configured_dim:
            detail = f"Embedding dimension mismatch: Model produces {actual_len}d but configured for {configured_dim}d"
        else:
            detail = f"Schema mismatch: Model produces {configured_dim}d but database vector column requires {expected_db_dim}d"
    except Exception as exc:
        clean_err = _sanitize_error(str(exc))
        detail = f"Embedder initialization failed: {clean_err}"

    status: ProviderStatus = "online" if emb_healthy else ("degraded" if schema_consistent is False else "offline")

    return EmbeddingServiceHealthModel(
        healthy=emb_healthy,
        status=status,
        provider=provider,
        model_name=runtime_model,
        dimensions=configured_dim,
        db_vector_dimensions=expected_db_dim,
        schema_consistent=schema_consistent,
        detail=detail,
        last_checked_at=now_iso,
    )


# ---------------------------------------------------------------------------
# Master Infrastructure Health Orchestrator
# ---------------------------------------------------------------------------
def get_system_infrastructure_health(
    db: Session,
    *,
    settings: Optional[Settings] = None,
    force_refresh: bool = False,
) -> InfrastructureHealthResponse:
    """Evaluate or retrieve cached full infrastructure health data."""
    global _CACHED_RESPONSE, _CACHED_AT

    now_ts = time.time()
    resolved_settings = settings or get_settings()

    # Cache check
    with _CACHE_LOCK:
        if _CACHED_RESPONSE is not None and not force_refresh:
            if now_ts - _CACHED_AT < _CACHE_TTL_SECONDS:
                return _CACHED_RESPONSE
        # Enforce rate limit on force_refresh to avoid flooding APIs
        if force_refresh and (now_ts - _CACHED_AT < _MIN_REFRESH_INTERVAL_SECONDS) and _CACHED_RESPONSE is not None:
            return _CACHED_RESPONSE

    # 1. Database & pgvector check
    db_health, db_vector_dim = evaluate_database_health(db)

    # 2. Embedding Engine check
    embedding_health = evaluate_embedding_health(resolved_settings, db_vector_dim)

    # 3. Retrieval Service check
    now_iso = datetime.now(timezone.utc).isoformat()
    total_chunks = db_health.chunk_count or 0
    retrieval_healthy = db_health.healthy and embedding_health.healthy and total_chunks > 0
    retrieval_status: ProviderStatus = "online" if retrieval_healthy else "degraded"
    retrieval_detail = (
        f"Operational ({total_chunks} indexed document chunks ready for retrieval)"
        if retrieval_healthy
        else ("No indexed document chunks found" if total_chunks == 0 else "Retrieval dependencies degraded")
    )
    retrieval_health = RetrievalServiceHealthModel(
        healthy=retrieval_healthy,
        status=retrieval_status,
        total_chunks=total_chunks,
        detail=retrieval_detail,
        last_checked_at=now_iso,
    )

    # 4. Resolve Active Provider Roles based on runtime selection and fallback configuration
    primary_name = resolved_settings.llm_provider.lower().strip()
    fallback_name: Optional[str] = None
    if primary_name == "groq":
        fallback_name = "ollama"

    def get_role_and_active(pname: str) -> Tuple[bool, ProviderRole]:
        if pname == primary_name:
            return True, "primary"
        if pname == fallback_name or (primary_name == "groq" and pname in ("ollama", "local")):
            return True, "fallback"
        return False, "standby"

    # 5. Execute Lightweight Provider Checks Concurrently
    providers: Dict[str, ProviderHealthModel] = {}
    check_tasks = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        # Groq
        g_active, g_role = get_role_and_active("groq")
        check_tasks.append(
            executor.submit(check_groq_health, resolved_settings, g_active, g_role)
        )

        # Ollama / Local
        o_active, o_role = get_role_and_active("ollama")
        check_tasks.append(
            executor.submit(check_ollama_health, resolved_settings, o_active, o_role)
        )

        # Gemini
        gem_active, gem_role = get_role_and_active("gemini")
        check_tasks.append(
            executor.submit(check_gemini_health, resolved_settings, gem_active, gem_role)
        )

        # NVIDIA
        nv_active, nv_role = get_role_and_active("nvidia")
        check_tasks.append(
            executor.submit(check_nvidia_health, resolved_settings, nv_active, nv_role)
        )

        # OpenRouter
        or_active, or_role = get_role_and_active("openrouter")
        check_tasks.append(
            executor.submit(check_openrouter_health, resolved_settings, or_active, or_role)
        )

        for future in as_completed(check_tasks):
            try:
                res = future.result()
                providers[res.name] = res
            except Exception as e:
                logger.error("Provider health task raised unexpected exception: %s", e)

    # Ensure "local" key is also available for backward compatibility with older tests/consumers
    if "ollama" in providers and "local" not in providers:
        local_copy = providers["ollama"].model_copy()
        local_copy.name = "local"
        providers["local"] = local_copy

    # 6. Overall Application Status
    primary_p = providers.get(primary_name)
    fallback_p = providers.get(fallback_name) if fallback_name else None

    llm_operational = False
    if primary_p and primary_p.status == "online":
        llm_operational = True
    elif fallback_p and fallback_p.status == "online":
        # Operating on fallback
        llm_operational = True

    overall_status: Any = "healthy"
    if not db_health.healthy or not embedding_health.healthy:
        overall_status = "degraded"
    if not llm_operational:
        overall_status = "unhealthy" if not db_health.healthy else "degraded"

    rag_metrics = RagMetricsStore.get_instance().get_stats()

    response = InfrastructureHealthResponse(
        status=overall_status,
        timestamp=now_iso,
        active_primary_provider=primary_name,
        active_fallback_provider=fallback_name,
        database=db_health,
        embedding_service=embedding_health,
        retrieval_service=retrieval_health,
        llm_providers=providers,
        rag_metrics=rag_metrics,
    )

    with _CACHE_LOCK:
        _CACHED_RESPONSE = response
        _CACHED_AT = time.time()

    return response
