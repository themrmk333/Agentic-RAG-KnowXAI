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


_MODEL_CACHE: dict[tuple[str, str], SentenceTransformer] = {}


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

        cache_key = (self.model_name, self.device)
        if cache_key in _MODEL_CACHE:
            self._model = _MODEL_CACHE[cache_key]
        else:
            logger.info(
                "Initializing LocalEmbeddingService with model=%s on device=%s",
                self.model_name,
                self.device,
            )
            load_kwargs = {
                "low_cpu_mem_usage": False,
                "torch_dtype": torch.float32,
            }
            try:
                try:
                    model = SentenceTransformer(
                        self.model_name,
                        device=self.device,
                        model_kwargs=load_kwargs,
                        local_files_only=True,
                    )
                except Exception:
                    model = SentenceTransformer(
                        self.model_name,
                        device=self.device,
                        model_kwargs=load_kwargs,
                    )
            except Exception as initial_err:
                logger.warning(
                    "Primary device load on %s failed (%s). Retrying with CPU fallback and full weight loading.",
                    self.device,
                    initial_err,
                )
                model = SentenceTransformer(
                    self.model_name,
                    device="cpu",
                    model_kwargs=load_kwargs,
                )
                self.device = "cpu"
            model.eval()
            _MODEL_CACHE[cache_key] = model
            self._model = model

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
