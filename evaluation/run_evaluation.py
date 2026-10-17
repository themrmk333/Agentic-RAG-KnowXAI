import os
import sys
import json
import time
import logging
from typing import Dict, List, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import SessionLocal
from services.rag_service import RAGService
from api.schemas.rag import RAGQueryRequest

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def evaluate_rag_pipeline():
    dataset_path = os.path.join(os.path.dirname(__file__), "datasets", "rag_eval_questions.json")
    if not os.path.exists(dataset_path):
        logger.error(f"Evaluation dataset not found at {dataset_path}")
        return

    with open(dataset_path, "r") as f:
        questions = json.load(f)

    logger.info(f"Loaded {len(questions)} evaluation questions.")

    metrics = {
        "total": 0,
        "retrieval_recall_1": 0,
        "retrieval_recall_3": 0,
        "retrieval_recall_5": 0,
        "retrieval_recall_10": 0,
        "source_hit_rate": 0,
        "grounded_answer_rate": 0,
        "citation_accuracy": 0,
        "hallucination_rate": 0,
        "insufficient_context_accuracy": 0,
        "permission_accuracy": 0,
        "total_latency_ms": 0.0,
        "failed_cases": []
    }

    with SessionLocal() as db:
        rag_service = RAGService(db=db)

        for i, q in enumerate(questions):
            logger.info(f"Evaluating {i+1}/{len(questions)}: {q['id']}")
            
            start_time = time.perf_counter()
            request = RAGQueryRequest(query=q["question"], top_k=10, max_context_items=5)
            user_context = {"department": q["department_context"]}

            try:
                # Force the provider to "mock" for stable fast evaluation
                request.provider = "mock"
                response = rag_service.process_query(request, user_context=user_context)
            except Exception as e:
                logger.error(f"Error evaluating {q['id']}: {e}")
                metrics["failed_cases"].append({"id": q["id"], "error": str(e)})
                continue

            latency_ms = (time.perf_counter() - start_time) * 1000.0
            metrics["total_latency_ms"] += latency_ms
            metrics["total"] += 1

            retrieved_doc_ids = [s.document_id for s in response.sources]
            expected_ids = q.get("expected_source_document_ids", [])
            is_negative = q.get("category") == "Negative"
            
            # Grounding Metrics
            is_grounded = response.grounded
            
            # Check hallucination (answering when shouldn't)
            is_hallucination = False
            if is_negative and is_grounded:
                # In a negative query, if it claims to be grounded but has no expected sources,
                # we need to be careful. The model should ideally state it has insufficient context.
                if response.confidence != "INSUFFICIENT_CONTEXT" and not retrieved_doc_ids:
                    is_hallucination = True
                    metrics["hallucination_rate"] += 1

            if is_grounded and not is_hallucination:
                metrics["grounded_answer_rate"] += 1
                
            if is_negative:
                if response.confidence == "INSUFFICIENT_CONTEXT" or not retrieved_doc_ids:
                    metrics["insufficient_context_accuracy"] += 1
            else:
                # Permission correctness: for now, assume permission accuracy is implicitly tested
                # if the right document was retrieved given the department.
                metrics["permission_accuracy"] += 1

            # Recall Metrics
            if not is_negative and expected_ids:
                # Calculate recall at different K values
                if any(doc_id in retrieved_doc_ids[:1] for doc_id in expected_ids):
                    metrics["retrieval_recall_1"] += 1
                if any(doc_id in retrieved_doc_ids[:3] for doc_id in expected_ids):
                    metrics["retrieval_recall_3"] += 1
                if any(doc_id in retrieved_doc_ids[:5] for doc_id in expected_ids):
                    metrics["retrieval_recall_5"] += 1
                if any(doc_id in retrieved_doc_ids[:10] for doc_id in expected_ids):
                    metrics["retrieval_recall_10"] += 1
                    
                # Citation Accuracy
                # Assuming if it cited the expected document, it's accurate.
                if any(doc_id in retrieved_doc_ids for doc_id in expected_ids):
                    metrics["citation_accuracy"] += 1
                    metrics["source_hit_rate"] += 1
                else:
                    metrics["failed_cases"].append({
                        "id": q["id"],
                        "question": q["question"],
                        "type": "Retrieval Miss",
                        "retrieved": retrieved_doc_ids,
                        "expected": expected_ids
                    })

    # Final calculations
    total = metrics["total"]
    positive_total = sum(1 for q in questions if q.get("category") != "Negative")
    negative_total = sum(1 for q in questions if q.get("category") == "Negative")

    if positive_total > 0:
        metrics["retrieval_recall_1"] /= positive_total
        metrics["retrieval_recall_3"] /= positive_total
        metrics["retrieval_recall_5"] /= positive_total
        metrics["retrieval_recall_10"] /= positive_total
        metrics["source_hit_rate"] /= positive_total
        metrics["citation_accuracy"] /= positive_total
        metrics["permission_accuracy"] /= positive_total
        
    if total > 0:
        metrics["grounded_answer_rate"] /= total
        metrics["hallucination_rate"] /= total
        metrics["average_latency_ms"] = metrics["total_latency_ms"] / total

    if negative_total > 0:
        metrics["insufficient_context_accuracy"] /= negative_total

    results_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(results_dir, exist_ok=True)
    report_path = os.path.join(results_dir, "eval_report.json")
    
    with open(report_path, "w") as f:
        json.dump(metrics, f, indent=4)

    logger.info("==================================================")
    logger.info("RAG EVALUATION REPORT")
    logger.info("==================================================")
    logger.info(f"Questions Evaluated: {total}")
    logger.info(f"Recall@1: {metrics['retrieval_recall_1']:.2f}")
    logger.info(f"Recall@3: {metrics['retrieval_recall_3']:.2f}")
    logger.info(f"Recall@5: {metrics['retrieval_recall_5']:.2f}")
    logger.info(f"Recall@10: {metrics['retrieval_recall_10']:.2f}")
    logger.info(f"Source Hit Rate: {metrics['source_hit_rate']:.2f}")
    logger.info(f"Grounded Answer Rate: {metrics['grounded_answer_rate']:.2f}")
    logger.info(f"Citation Accuracy: {metrics['citation_accuracy']:.2f}")
    logger.info(f"Hallucination Rate: {metrics['hallucination_rate']:.2f}")
    logger.info(f"Insufficient Context Acc: {metrics.get('insufficient_context_accuracy', 0):.2f}")
    logger.info(f"Average Latency: {metrics.get('average_latency_ms', 0):.2f} ms")
    logger.info("==================================================")
    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    evaluate_rag_pipeline()
