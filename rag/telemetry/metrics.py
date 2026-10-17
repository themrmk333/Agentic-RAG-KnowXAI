"""In-memory telemetry metrics store for the RAG API."""

import collections
from typing import Dict, Any

class RagMetricsStore:
    _instance = None
    
    def __init__(self):
        self.recent_latencies = collections.deque(maxlen=100)
        self.error_count = 0
        self.total_queries = 0
        self.total_grounded = 0
        
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = RagMetricsStore()
        return cls._instance
        
    def record_success(self, latency_ms: float, grounded: bool):
        self.total_queries += 1
        self.recent_latencies.append(latency_ms)
        if grounded:
            self.total_grounded += 1
            
    def record_error(self):
        self.error_count += 1
        
    def get_stats(self) -> Dict[str, Any]:
        avg_latency = sum(self.recent_latencies) / len(self.recent_latencies) if self.recent_latencies else 0.0
        return {
            "total_queries": self.total_queries,
            "error_count": self.error_count,
            "average_latency_ms": round(avg_latency, 2),
            "grounding_rate": round(self.total_grounded / self.total_queries, 2) if self.total_queries > 0 else 1.0,
            "recent_requests_tracked": len(self.recent_latencies)
        }
