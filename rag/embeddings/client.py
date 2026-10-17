"""
Resilient local embedding client using SentenceTransformers with CUDA GPU acceleration
and strict dimension and vector validation.
"""

from __future__ import annotations

import logging
from typing import Any, Sequence

import torch
from sentence_transformers import SentenceTransformer

from .models import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_RETRY_BASE_DELAY,
    EXPECTED_VECTOR_DIMENSION,
    validate_vector,
)

logger = logging.getLogger(__name__)


class PermanentEmbeddingError(Exception):
    """Raised when an unrecoverable error occurs (e.g. dimension mismatch, invalid vector)."""
    pass


class TransientEmbeddingError(Exception):
    """Raised when a temporary retriable error occurs."""
    pass


class ResilientEmbeddingClient:
    """
    Local GPU embedding client using SentenceTransformers providing:
      - CUDA acceleration on NVIDIA GPUs
      - Fast failure for dimension / NaN / Infinity errors
      - Strict vector validation (dimension=384, no NaN, no Inf)
      - In-memory model caching
    """

    def __init__(
        self,
        model: str = "BAAI/bge-small-en-v1.5",
        expected_dimension: int = EXPECTED_VECTOR_DIMENSION,
        device: str | None = None,
        max_retries: int = DEFAULT_MAX_RETRIES,
        retry_base_delay: float = DEFAULT_RETRY_BASE_DELAY,
        request_timeout: float = DEFAULT_REQUEST_TIMEOUT,
        require_cuda: bool = False,
        api_key: str | None = None,  # accepted for backward compatibility
        base_url: str | None = None,  # accepted for backward compatibility
        model_instance: Any = None,
    ) -> None:
        self.model = model.strip() if model else "BAAI/bge-small-en-v1.5"
        self.expected_dimension = expected_dimension
        self.max_retries = max_retries
        self.retry_base_delay = retry_base_delay
        self.request_timeout = request_timeout
        self.api_key = api_key
        self.base_url = base_url

        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device.lower()

        if require_cuda and (not self.device.startswith("cuda") or not torch.cuda.is_available()):
            raise RuntimeError(
                f"CUDA is required for local GPU embeddings, but CUDA is not available. "
                f"device={self.device}, torch.cuda.is_available()={torch.cuda.is_available()}"
            )

        if model_instance is not None:
            self._model = model_instance
        else:
            logger.info("Loading local embedding model '%s' on %s...", self.model, self.device)
            self._model = SentenceTransformer(self.model, device=self.device)
            self._model.eval()

    def test_dimension(self, sample_text: str = "Dimension validation test") -> tuple[bool, int, str]:
        """
        Execute a lightweight test embedding request to verify device and vector dimension.
        Returns (is_valid, actual_dimension, message).
        """
        try:
            vectors = self.embed_batch([sample_text])
            if not vectors:
                return False, 0, "No vectors returned from test embedding request"
            actual_dim = len(vectors[0])
            if actual_dim != self.expected_dimension:
                return (
                    False,
                    actual_dim,
                    f"Dimension mismatch: expected {self.expected_dimension}, received {actual_dim}",
                )
            return True, actual_dim, "OK"
        except Exception as e:
            return False, 0, f"Dimension test failed: {e}"

    def embed_batch(self, texts: Sequence[str]) -> list[list[float]]:
        """
        Embed a batch of texts using the local SentenceTransformer model.
        Returns normalized float lists.
        """
        if not texts:
            return []

        text_list = list(texts)

        try:
            with torch.inference_mode():
                raw_embeddings = self._model.encode(
                    text_list,
                    batch_size=len(text_list),
                    show_progress_bar=False,
                    normalize_embeddings=True,
                    convert_to_numpy=True,
                )

            if len(raw_embeddings) != len(text_list):
                raise PermanentEmbeddingError(
                    f"Model returned {len(raw_embeddings)} vectors for {len(text_list)} input texts"
                )

            vectors: list[list[float]] = []
            for idx, item in enumerate(raw_embeddings):
                vec = [float(v) for v in item]
                ok, msg = validate_vector(vec, expected_dim=self.expected_dimension)
                if not ok:
                    raise PermanentEmbeddingError(
                        f"Vector at index {idx} failed validation: {msg}"
                    )
                vectors.append(vec)

            return vectors

        except PermanentEmbeddingError:
            raise
        except Exception as e:
            logger.error("Local embedding generation failed: %s", e)
            raise PermanentEmbeddingError(f"Local embedding generation error: {e}") from e
