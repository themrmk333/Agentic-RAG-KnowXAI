"""End-to-end runner for Step 10: Local LLM Integration."""

import logging
import time

from config.settings import get_settings
from services.rag_service import RAGService
from api.schemas.rag import RAGQueryRequest
from database.connection import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_step10_end_to_end():
    """Run real questions against the local LLM via the RAG pipeline."""
    
    settings = get_settings()
    
    if settings.llm_provider != "local":
        logger.error(f"LLM_PROVIDER is '{settings.llm_provider}', but 'local' is required to run this test.")
        return
        
    logger.info("Initializing Local LLM End-to-End RAG Test")
    logger.info(f"Target Local URL: {settings.local_llm_base_url}")
    logger.info(f"Target Local Model: {settings.local_llm_model}")
    
    test_questions = [
        ("What is the IT department's password policy?", "IT"),
        ("How do I submit an expense claim?", "FINANCE"),
        ("What is the onboarding process for new hires?", "HR"),
        ("Are there any current projects involving cloud migration?", "PROJECT"),
    ]
    
    logger.info("\n=======================================================")
    logger.info("STARTING LOCAL LLM QUERY EXECUTION")
    logger.info("=======================================================\n")
    
    total_start = time.perf_counter()
    
    with SessionLocal() as db:
        rag_service = RAGService(db=db)
        
        for query, department in test_questions:
            logger.info(f"\n>>> Query: '{query}'")
            logger.info(f">>> User Department Context: {department}")
            
            start_time = time.perf_counter()
            try:
                # We bypass the API router but go through the RAG service which handles
                # retrieval -> reranking -> grounding -> generation
                request = RAGQueryRequest(query=query, provider="local")
                user_context = {"department": department}
                
                response = rag_service.process_query(
                    request=request,
                    user_context=user_context
                )
                
                latency = (time.perf_counter() - start_time) * 1000.0
                
                logger.info("\n--- RESPONSE ---")
                logger.info(response.answer)
                logger.info("----------------")
                logger.info(f"Grounded: {response.grounded}")
                logger.info(f"Confidence: {response.confidence}")
                logger.info(f"Sources Used: {len(response.sources)}")
                logger.info(f"Latency: {latency:.2f} ms")
                
            except Exception as e:
                logger.error(f"Failed to process query: {e}")
            
    total_latency = (time.perf_counter() - total_start) * 1000.0
    
    logger.info("\n=======================================================")
    logger.info("LOCAL LLM TEST COMPLETE")
    logger.info(f"Total Execution Time: {total_latency:.2f} ms")
    logger.info("=======================================================\n")

if __name__ == "__main__":
    run_step10_end_to_end()
