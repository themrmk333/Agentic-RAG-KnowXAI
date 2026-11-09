"""Test embedding model loading and runtime generation."""

import math
import numpy as np
import pytest

from rag.retrieval.query_embedder import QueryEmbedder
from config.settings import get_settings


def test_embedding_model_loading_and_inference():
    """Verify configured BAAI/bge-small-en-v1.5 loads without meta tensor error and generates valid embeddings."""
    settings = get_settings()
    embedder = QueryEmbedder.get_instance(model_name=settings.embedding_model)

    assert embedder is not None
    assert embedder.model_name == "BAAI/bge-small-en-v1.5"

    sample_query = "how to on VPN"
    vec = embedder.embed_query(sample_query)

    # 1. Non-empty
    assert vec is not None
    assert len(vec) == 384, f"Expected dimension 384, got {len(vec)}"

    # 2. All finite (no NaNs or Infs)
    for idx, val in enumerate(vec):
        assert isinstance(val, float), f"Element {idx} is not float: {type(val)}"
        assert math.isfinite(val), f"Element {idx} is not finite: {val}"
        assert not math.isnan(val), f"Element {idx} is NaN"

    # 3. Non-zero vector
    norm = np.linalg.norm(vec)
    assert norm > 0.0, "Embedding vector is all zeros"
    # Normalized embeddings should have L2 norm close to 1.0
    assert abs(norm - 1.0) < 1e-3, f"Expected unit normalized vector, got norm={norm}"
