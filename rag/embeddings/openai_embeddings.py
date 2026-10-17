"""OpenAI-compatible embedding service for configured providers."""

from __future__ import annotations

from collections.abc import Sequence

from openai import OpenAI


class OpenAIEmbeddingService:
    """Generate embeddings through OpenAI, NVIDIA NIM, or OpenRouter endpoints."""

    def __init__(self, *, api_key: str, base_url: str, model: str, dimensions: int) -> None:
        self.model = model
        self.dimensions = dimensions
        self._client = OpenAI(api_key=api_key, base_url=base_url)

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        if not texts:
            return []
        result = self._client.embeddings.create(model=self.model, input=list(texts))
        vectors = [list(item.embedding) for item in result.data]
        if any(len(vector) != self.dimensions for vector in vectors):
            raise ValueError("Embedding response dimension does not match PGVECTOR_DIMENSIONS")
        return vectors

    def embed_query(self, text: str) -> list[float]:
        return self.embed([text])[0]
