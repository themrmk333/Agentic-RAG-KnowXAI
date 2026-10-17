"""Google Gemini embedding service using official google-genai SDK."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from google import genai


class GeminiEmbeddingService:
    """Generate embeddings through official Google Gemini Python SDK."""

    def __init__(
        self,
        *,
        api_key: str,
        model: str = "gemini-embedding-001",
        dimensions: int = 1536,
        client: genai.Client | None = None,
    ) -> None:
        self.model = model
        self.dimensions = dimensions
        self._client = client or genai.Client(api_key=api_key)

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        if not texts:
            return []
        result = self._client.models.embed_content(
            model=self.model,
            contents=list(texts),
            config={"output_dimensionality": self.dimensions},
        )
        raw_items = result.embeddings if result and result.embeddings else []
        vectors: list[list[float]] = []
        for item in raw_items:
            vec = list(item.values) if hasattr(item, "values") else list(item)
            vectors.append(vec)
        if any(len(vector) != self.dimensions for vector in vectors):
            raise ValueError(f"Embedding response dimension does not match expected {self.dimensions}")
        return vectors

    def embed_query(self, text: str) -> list[float]:
        return self.embed([text])[0]
