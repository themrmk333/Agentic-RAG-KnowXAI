"""
Local GPU embedding service using SentenceTransformers and PyTorch.
"""

from __future__ import annotations

import logging
from typing import Sequence

import torch
from sentence_transformers import SentenceTransformer

from .models import EXPECTED_VECTOR_DIMENSION, validate_vector

logger = logging.getLogger(__name__)


class LocalEmbeddingService:
    """
    Local embedding service executing on NVIDIA GPU via CUDA (or CPU fallback if explicitly allowed).
    """

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5",
        device: str | None = None,
        dimensions: int = EXPECTED_VECTOR_DIMENSION,
        normalize_embeddings: bool = True,
        require_cuda: bool = False,
    ) -> None:
        self.model_name = model_name
        self.dimensions = dimensions
        self.normalize_embeddings = normalize_embeddings

        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device.lower()

        if require_cuda and self.device != "cuda":
            raise RuntimeError(
                f"CUDA is required for local GPU embeddings, but CUDA is not available. "
                f"torch.cuda.is_available()={torch.cuda.is_available()}"
            )

        logger.info(
            "Initializing LocalEmbeddingService with model=%s on device=%s",
            self.model_name,
            self.device,
        )

        # Disabling low_cpu_mem_usage prevents transformers from loading weights onto the 'meta' device,
        # which causes the "Cannot copy out of meta tensor; no data!" error during .to(device).
        self._model = SentenceTransformer(
            self.model_name, 
            device=self.device,
            model_kwargs={"low_cpu_mem_usage": False}
        )
        self._model.eval()

    @property
    def model(self) -> str:
        return self.model_name

    def embed(self, texts: Sequence[str], batch_size: int = 64) -> list[list[float]]:
        """
        Embed a sequence of texts using the local model.
        Returns normalized float32 vectors.
        """
        if not texts:
            return []

        text_list = list(texts)
        with torch.inference_mode():
            raw_embeddings = self._model.encode(
                text_list,
                batch_size=batch_size,
                show_progress_bar=False,
                normalize_embeddings=self.normalize_embeddings,
                convert_to_numpy=True,
            )

        vectors: list[list[float]] = []
        for idx, row in enumerate(raw_embeddings):
            vec = [float(v) for v in row]
            ok, msg = validate_vector(vec, expected_dim=self.dimensions)
            if not ok:
                raise ValueError(f"Vector at index {idx} failed validation: {msg}")
            vectors.append(vec)

        return vectors

    def embed_query(self, text: str) -> list[float]:
        """
        Embed a single search query text.
        """
        vectors = self.embed([text], batch_size=1)
        return vectors[0]
