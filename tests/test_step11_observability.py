import pytest
from rag.telemetry.metrics import RagMetricsStore
from rag.telemetry.logger import RagTelemetryLogger
import os
import json

def test_telemetry_metrics_store():
    store = RagMetricsStore.get_instance()
    initial_queries = store.total_queries
    
    # Simulate a query
    store.record_success(latency_ms=250.5, grounded=True)
    stats = store.get_stats()
    
    assert store.total_queries == initial_queries + 1
    assert stats["total_queries"] == initial_queries + 1
    assert stats["average_latency_ms"] > 0
    assert stats["recent_requests_tracked"] > 0

def test_telemetry_logger_output(tmpdir, monkeypatch):
    import logging
    # Patch logger to output to temp directory
    log_file = os.path.join(str(tmpdir), "test_observability.log")
    
    logger = logging.getLogger("rag.telemetry")
    fh = logging.FileHandler(log_file)
    logger.addHandler(fh)
    
    RagTelemetryLogger.log_query(
        request_id="test-req-123",
        query="What is the password policy?",
        department_context="IT",
        retrieval_count=5,
        retrieval_latency_ms=10.0,
        reranking_latency_ms=2.0,
        context_assembly_latency_ms=5.0,
        generation_latency_ms=100.0,
        total_latency_ms=117.0,
        grounded=True,
        confidence="HIGH",
        source_count=1,
        provider="mock",
        model="mock-deterministic"
    )
    
    fh.flush()
    assert os.path.exists(log_file)
    
    with open(log_file, "r") as f:
        content = f.read()
        assert "test-req-123" in content
        assert "retrieval_ms" in content
        
    logger.removeHandler(fh)
