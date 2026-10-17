import os
import sys
import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import SessionLocal
from services.rag_service import RAGService
from api.schemas.rag import RAGQueryRequest

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def worker(query_id: int) -> float:
    with SessionLocal() as db:
        rag_service = RAGService(db=db)
        start = time.perf_counter()
        req = RAGQueryRequest(query=f"concurrency query {query_id}", top_k=5, provider="mock")
        rag_service.process_query(req, user_context={"department": "HR"})
        return (time.perf_counter() - start) * 1000

def run_concurrency_test(workers_list=[2, 5, 10]):
    logger.info(f"Starting concurrency testing for {workers_list} simultaneous workers.")
    
    for max_workers in workers_list:
        logger.info(f"Testing with {max_workers} concurrent requests...")
        start_time = time.perf_counter()
        
        success_count = 0
        error_count = 0
        latencies = []
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(worker, i) for i in range(max_workers)]
            for future in as_completed(futures):
                try:
                    lat = future.result()
                    latencies.append(lat)
                    success_count += 1
                except Exception as e:
                    logger.error(f"Worker failed: {e}")
                    error_count += 1
                    
        total_time = (time.perf_counter() - start_time) * 1000
        avg_lat = sum(latencies) / len(latencies) if latencies else 0.0
        
        logger.info(f"--- Results for {max_workers} concurrent workers ---")
        logger.info(f"Success: {success_count}, Errors: {error_count}")
        logger.info(f"Total Wall Time: {total_time:.2f} ms")
        logger.info(f"Average Request Latency: {avg_lat:.2f} ms")
        logger.info("--------------------------------------------------")

if __name__ == "__main__":
    run_concurrency_test()
