"""Provider construction and secret-safe health checks."""

from __future__ import annotations

from typing import Any

from config.settings import Settings, get_settings

from .providers import (
    GeminiProvider,
    LLMProvider,
    OpenAICompatibleProvider,
    LocalProvider,
    ProviderConfigurationError,
    is_openrouter_key,
)


def _secret(secret: Any) -> str | None:
    if secret is None:
        return None
    value = secret.get_secret_value()
    return value.strip() or None


def build_provider(provider: str, *, model: str | None = None, settings: Settings | None = None) -> LLMProvider:
    """Build a provider, allowing each agent to select its own model."""

    resolved = settings or get_settings()
    provider_name = provider.lower().strip()

    if provider_name == "local":
        return LocalProvider(
            base_url=resolved.local_llm_base_url,
            model=model or resolved.local_llm_model,
        )

    if provider_name == "gemini":
        api_key = _secret(resolved.gemini_api_key)
        if not api_key:
            raise ProviderConfigurationError("GEMINI_API_KEY is not configured")
        selected_model = model or resolved.gemini_model
        if is_openrouter_key(api_key):
            return OpenAICompatibleProvider(
                api_key=api_key,
                base_url=resolved.openrouter_base_url,
                model=model or resolved.gemini_openrouter_model,
            )
        if "/" in selected_model or "llama" in selected_model.lower():
            selected_model = "gemini-2.0-flash"
        return GeminiProvider(api_key=api_key, model=selected_model)

    if provider_name == "nvidia":
        api_key = _secret(resolved.nvidia_api_key)
        if not api_key:
            raise ProviderConfigurationError("NVIDIA_API_KEY is not configured")
        base_url = resolved.openrouter_base_url if is_openrouter_key(api_key) else resolved.nvidia_base_url
        return OpenAICompatibleProvider(
            api_key=api_key,
            base_url=base_url,
            model=model or (resolved.nvidia_openrouter_model if is_openrouter_key(api_key) else resolved.nvidia_model),
        )

    if provider_name == "openrouter":
        api_key = _secret(resolved.gemini_api_key)
        if not api_key:
            raise ProviderConfigurationError("OpenRouter API key (via GEMINI_API_KEY) is not configured")
        return OpenAICompatibleProvider(
            api_key=api_key,
            base_url=resolved.openrouter_base_url,
            model=model or resolved.gemini_openrouter_model,
        )

    raise ProviderConfigurationError(f"Unsupported provider: {provider_name}")


_HEALTH_CACHE: dict[str, dict[str, str | bool]] = {}
_HEALTH_CACHE_TIME: float = 0.0


def provider_health(*, settings: Settings | None = None) -> dict[str, dict[str, str | bool]]:
    """Run minimal inference checks for configured providers without leaking secrets."""
    global _HEALTH_CACHE, _HEALTH_CACHE_TIME
    import time
    now = time.time()
    if _HEALTH_CACHE and (now - _HEALTH_CACHE_TIME < 30.0):
        return _HEALTH_CACHE

    resolved = settings or get_settings()
    results: dict[str, dict[str, str | bool]] = {}
    for name, configured in (("gemini", resolved.gemini_api_key), ("openrouter", resolved.gemini_api_key), ("nvidia", resolved.nvidia_api_key), ("local", "always_configured")):
        if name != "local" and not _secret(configured):
            results[name] = {"configured": False, "healthy": False, "detail": "not configured"}
            continue
        try:
            healthy, detail = build_provider(name, settings=resolved).health_check()
            results[name] = {"configured": True, "healthy": healthy, "detail": detail}
        except ProviderConfigurationError:
            results[name] = {"configured": True, "healthy": False, "detail": "invalid configuration"}
        except Exception:
            results[name] = {"configured": True, "healthy": False, "detail": "inference request failed"}

    _HEALTH_CACHE = results
    _HEALTH_CACHE_TIME = now
    return results