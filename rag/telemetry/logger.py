"""Telemetry and observability logger for the RAG Pipeline."""

import logging
import json
import uuid
import datetime
from typing import Any, Dict, Optional
from rag.telemetry.metrics import RagMetricsStore

logger = logging.getLogger("rag.telemetry")
logger.setLevel(logging.INFO)

# Optional: Output telemetry to a specific file
import os
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")
os.makedirs(log_dir, exist_ok=True)
fh = logging.FileHandler(os.path.join(log_dir, "rag_observability.log"))
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

class RagTelemetryLogger:
    @staticmethod
    def log_query(
        request_id: str,
        query: str,
        department_context: Optional[str],
        retrieval_count: int,
        retrieval_latency_ms: float,
        reranking_latency_ms: float,
        context_assembly_latency_ms: float,
        generation_latency_ms: float,
        total_latency_ms: float,
        grounded: bool,
        confidence: str,
        source_count: int,
        provider: str,
        model: str
    ):
        """Logs structured telemetry for a RAG execution."""
        
        # We deliberately do NOT log the full query text to prevent secret leakage in logs,
        # unless it is explicitly needed. We log the length for analytics.
        
        event = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "request_id": request_id,
            "query_length": len(query) if query else 0,
            "department_context": department_context or "none",
            "retrieval_count": retrieval_count,
            "latency": {
                "retrieval_ms": round(retrieval_latency_ms, 2),
                "reranking_ms": round(reranking_latency_ms, 2),
                "context_assembly_ms": round(context_assembly_latency_ms, 2),
                "generation_ms": round(generation_latency_ms, 2),
                "total_ms": round(total_latency_ms, 2)
            },
            "generation": {
                "grounded": grounded,
                "confidence": confidence,
                "source_count": source_count,
                "provider": provider,
                "model": model
            }
        }
        
        RagMetricsStore.get_instance().record_success(
            latency_ms=total_latency_ms,
            grounded=grounded
        )
        
        logger.info(json.dumps(event))
