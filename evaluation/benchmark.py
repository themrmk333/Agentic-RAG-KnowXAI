import os
import sys
import time
import statistics
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import SessionLocal
from services.rag_service import RAGService
from api.schemas.rag import RAGQueryRequest

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def run_benchmark(num_queries=30):
    logger.info(f"Starting sequential benchmark with {num_queries} queries.")
    latencies = []
    
    with SessionLocal() as db:
        rag_service = RAGService(db=db)
        
        # Warmup
        req = RAGQueryRequest(query="warmup query", top_k=5, provider="mock")
        rag_service.process_query(req)
        
        for i in range(num_queries):
            start = time.perf_counter()
            req = RAGQueryRequest(query=f"benchmark query {i}", top_k=10, provider="mock")
            rag_service.process_query(req, user_context={"department": "IT"})
            latencies.append((time.perf_counter() - start) * 1000)
            
    avg_latency = statistics.mean(latencies)
    p95_latency = statistics.quantiles(latencies, n=100)[94] if len(latencies) >= 2 else max(latencies)
    p99_latency = statistics.quantiles(latencies, n=100)[98] if len(latencies) >= 2 else max(latencies)
    min_latency = min(latencies)
    max_latency = max(latencies)
    
    logger.info("==================================================")
    logger.info("BENCHMARK RESULTS (Sequential)")
    logger.info("==================================================")
    logger.info(f"Total Queries: {num_queries}")
    logger.info(f"Average Latency: {avg_latency:.2f} ms")
    logger.info(f"P95 Latency: {p95_latency:.2f} ms")
    logger.info(f"P99 Latency: {p99_latency:.2f} ms")
    logger.info(f"Min Latency: {min_latency:.2f} ms")
    logger.info(f"Max Latency: {max_latency:.2f} ms")
    logger.info("==================================================")

if __name__ == "__main__":
    run_benchmark(30)
