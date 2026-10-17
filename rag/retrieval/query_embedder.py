"""Query embedding component using local BAAI/bge-small-en-v1.5 model."""

from __future__ import annotations

import logging
import math
from functools import lru_cache
from typing import Optional, Sequence

import torch
from sentence_transformers import SentenceTransformer

from config.settings import get_settings
from rag.embeddings.models import EXPECTED_VECTOR_DIMENSION, validate_vector

logger = logging.getLogger(__name__)

DEFAULT_MODEL_NAME = "BAAI/bge-small-en-v1.5"
MAX_QUERY_LENGTH = 4096


class QueryEmbedder:
    """Production-grade local query embedding service.
    
    Loads the BAAI/bge-small-en-v1.5 model once and produces validated
    384-dimensional normalized float vectors for vector search.
    """

    _instance: Optional["QueryEmbedder"] = None

    def __init__(
        self,
        model_name: str = DEFAULT_MODEL_NAME,
        device: Optional[str] = None,
        dimensions: int = EXPECTED_VECTOR_DIMENSION,
        normalize_embeddings: bool = True,
    ) -> None:
        self.model_name = model_name
        self.dimensions = dimensions
        self.normalize_embeddings = normalize_embeddings

        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device.lower()

        logger.info(
            "Initializing QueryEmbedder with model=%s on device=%s (expected dimension=%d)",
            self.model_name,
            self.device,
            self.dimensions,
        )

        try:
            # Pass model_kwargs to prevent accelerate meta tensor bugs
            self._model = SentenceTransformer(
                self.model_name, 
                device=self.device,
                model_kwargs={"torch_dtype": torch.float32}
            )
            self._model.eval()
        except Exception as e:
            logger.error("Failed to load local embedding model '%s': %s", self.model_name, e)
            raise RuntimeError(f"Failed to load embedding model '{self.model_name}': {e}") from e

    @classmethod
    def get_instance(
        cls,
        model_name: Optional[str] = None,
        device: Optional[str] = None,
        dimensions: Optional[int] = None,
    ) -> "QueryEmbedder":
        """Singleton accessor to prevent reloading model weights repeatedly."""
        if cls._instance is None:
            settings = None
            try:
                settings = get_settings()
            except Exception:
                pass

            resolved_model = model_name or (settings.embedding_model if settings else DEFAULT_MODEL_NAME)
            resolved_dim = dimensions or (settings.pgvector_dimensions if settings else EXPECTED_VECTOR_DIMENSION)

            cls._instance = cls(
                model_name=resolved_model,
                device=device,
                dimensions=resolved_dim,
            )
        return cls._instance

    def validate_query_text(self, query: str) -> str:
        """Validate search query input.
        
        Raises:
            TypeError: if query is not a string.
            ValueError: if query is empty or whitespace-only.
        """
        if query is None:
            raise TypeError("Query cannot be None; must be a valid string")
        if not isinstance(query, str):
            raise TypeError(f"Query must be a string, got {type(query).__name__}")

        cleaned = query.strip()
        if not cleaned:
            raise ValueError("Query cannot be empty or contain only whitespace")

        if len(cleaned) > MAX_QUERY_LENGTH:
            logger.warning(
                "Query length (%d) exceeds max recommended length (%d); truncating safely.",
                len(cleaned),
                MAX_QUERY_LENGTH,
            )
            cleaned = cleaned[:MAX_QUERY_LENGTH]

        return cleaned

    def embed_query(self, query: str) -> list[float]:
        """Embed a validated search query string into a 384-dimensional vector.
        
        Returns:
            list[float]: A validated 384-dimensional vector suitable for pgvector.
            
        Raises:
            TypeError / ValueError: On invalid query string.
            ValueError: On invalid vector dimension, NaN, or Inf values.
            RuntimeError: On embedding failure.
        """
        validated_text = self.validate_query_text(query)

        try:
            with torch.inference_mode():
                raw = self._model.encode(
                    [validated_text],
                    batch_size=1,
                    show_progress_bar=False,
                    normalize_embeddings=self.normalize_embeddings,
                    convert_to_numpy=True,
                )
        except Exception as e:
            logger.error("Error during query embedding generation: %s", e)
            raise RuntimeError(f"Embedding generation failed for query: {e}") from e

        if raw is None or len(raw) == 0:
            raise RuntimeError("Model returned empty embedding output")

        vector = [float(v) for v in raw[0]]

        # Strict validation
        is_valid, msg = validate_vector(vector, expected_dim=self.dimensions)
        if not is_valid:
            logger.error("Query vector failed validation: %s", msg)
            raise ValueError(f"Query vector validation failed: {msg}")

        return vector

    def embed_batch(self, queries: Sequence[str]) -> list[list[float]]:
        """Embed multiple search queries in a batch."""
        if not queries:
            return []

        validated_queries = [self.validate_query_text(q) for q in queries]

        try:
            with torch.inference_mode():
                raw_matrix = self._model.encode(
                    validated_queries,
                    batch_size=min(len(validated_queries), 64),
                    show_progress_bar=False,
                    normalize_embeddings=self.normalize_embeddings,
                    convert_to_numpy=True,
                )
        except Exception as e:
            logger.error("Error during batch query embedding generation: %s", e)
            raise RuntimeError(f"Batch embedding generation failed: {e}") from e

        vectors: list[list[float]] = []
        for idx, row in enumerate(raw_matrix):
            vec = [float(v) for v in row]
            is_valid, msg = validate_vector(vec, expected_dim=self.dimensions)
            if not is_valid:
                raise ValueError(f"Query vector at index {idx} failed validation: {msg}")
            vectors.append(vec)

        return vectors
