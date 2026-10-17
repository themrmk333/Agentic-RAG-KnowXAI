"""Construct the configured embedding service without exposing credentials."""

from __future__ import annotations

from config.settings import Settings, get_settings

from .gemini_embeddings import GeminiEmbeddingService
from .local_embeddings import LocalEmbeddingService
from .openai_embeddings import OpenAIEmbeddingService


def build_embedding_service(
    settings: Settings | None = None,
) -> LocalEmbeddingService | GeminiEmbeddingService | OpenAIEmbeddingService:
    resolved = settings or get_settings()
    provider = getattr(resolved, "embedding_provider", "local").lower()

    if provider == "local":
        return LocalEmbeddingService(
            model_name=resolved.embedding_model,
            dimensions=resolved.pgvector_dimensions,
        )

    secret = resolved.embedding_api_key
    if secret is None or not secret.get_secret_value().strip():
        raise RuntimeError("EMBEDDING_API_KEY must be configured for the selected embedding endpoint")

    if provider == "gemini" or "gemini" in resolved.embedding_model.lower():
        return GeminiEmbeddingService(
            api_key=secret.get_secret_value().strip(),
            model=resolved.embedding_model,
            dimensions=resolved.pgvector_dimensions,
        )

    base_url = resolved.embedding_base_url or "https://api.openai.com/v1"
    return OpenAIEmbeddingService(
        api_key=secret.get_secret_value().strip(),
        base_url=base_url,
        model=resolved.embedding_model,
        dimensions=resolved.pgvector_dimensions,
    )