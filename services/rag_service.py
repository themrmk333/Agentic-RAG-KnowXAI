"""End-to-End Orchestration Service for the RAG Pipeline."""

import logging
import time
from typing import Any, Dict, Optional

from sqlalchemy.orm import Session

from api.schemas.rag import (
    RAGQueryRequest,
    RAGQueryResponse,
    RAGRetrievalStats,
    RAGMetadataSchema,
    RAGSourceSchema,
)
from rag.retrieval.semantic_retriever import SemanticRetriever
from rag.context.context_assembler import ContextAssembler
from rag.generation.answer_generator import AnswerGenerator
from rag.generation.models import GenerationRequest
from rag.telemetry.logger import RagTelemetryLogger
from rag.telemetry.metrics import RagMetricsStore
import uuid

logger = logging.getLogger(__name__)


class RAGService:
    """Orchestrates Steps 6 (Retrieval), 7 (Context Assembly), and 8 (Generation)."""

    def __init__(self, db: Session):
        self.db = db
        # Initialize the underlying components
        self.retriever = SemanticRetriever(session_factory=lambda: self.db)
        self.assembler = ContextAssembler()
        self.generator = AnswerGenerator()

    def process_query(
        self, 
        request: RAGQueryRequest, 
        user_context: Optional[Dict[str, Any]] = None
    ) -> RAGQueryResponse:
        """
        Execute the full RAG pipeline for the given query.
        
        Args:
            request: The validated API request payload.
            user_context: Optional user or department context (used for filtering, NOT routing).
        
        Returns:
            A structured API response payload.
        """
        latency_tracker = {}
        t_start = time.perf_counter()

        # Steps 6 & 7: Semantic Retrieval & Context Assembly
        # ContextAssembler handles retrieval internally if candidates are not provided.
        t_assembly_start = time.perf_counter()
        
        assembled_context = self.assembler.assemble(
            query=request.query,
            max_context_items=request.max_context_items,
            user_context=user_context,
        )
        
        # We can extract the retrieval metrics from the assembly metadata
        candidates_retrieved = assembled_context.metadata.candidate_count
        
        latency_tracker["retrieval_ms"] = assembled_context.metadata.retrieval_time_ms
        latency_tracker["context_assembly_ms"] = assembled_context.metadata.assembly_time_ms + assembled_context.metadata.reranking_time_ms

        # Step 8: Answer Generation
        t_generation_start = time.perf_counter()
        gen_req = GenerationRequest(
            query=request.query,
            user_context=user_context,
            assembled_context=assembled_context,
            provider=request.provider,
            temperature=0.0,
            max_tokens=None
        )
        
        gen_response = self.generator.generate_answer(gen_req)
        latency_tracker["generation_ms"] = (time.perf_counter() - t_generation_start) * 1000.0
        
        total_latency = (time.perf_counter() - t_start) * 1000.0
        latency_tracker["total_ms"] = total_latency
        
        # Build API Response Sources
        api_sources = []
        if gen_response.sources:
            for src in gen_response.sources:
                api_sources.append(
                    RAGSourceSchema(
                        document_id=src.document_id,
                        chunk_index=src.chunk_index,
                        title=src.document_title,
                        source_path=src.source,
                        score=src.rerank_score or src.semantic_score or 0.0
                    )
                )
                
        # Build Metadata
        meta_dict = gen_response.generation_metadata or {}
        
        request_id = str(uuid.uuid4())
        department_context = user_context.get("department") if user_context else None
        
        # Log telemetry
        RagTelemetryLogger.log_query(
            request_id=request_id,
            query=request.query,
            department_context=department_context,
            retrieval_count=candidates_retrieved,
            retrieval_latency_ms=latency_tracker.get("retrieval_ms", 0.0),
            reranking_latency_ms=assembled_context.metadata.reranking_time_ms,
            context_assembly_latency_ms=assembled_context.metadata.assembly_time_ms,
            generation_latency_ms=latency_tracker.get("generation_ms", 0.0),
            total_latency_ms=latency_tracker.get("total_ms", 0.0),
            grounded=gen_response.grounded,
            confidence=gen_response.confidence,
            source_count=gen_response.context_items_used,
            provider=meta_dict.get("provider", "unknown"),
            model=meta_dict.get("model", "unknown")
        )
        
        return RAGQueryResponse(
            query=gen_response.query,
            answer=gen_response.answer,
            grounded=gen_response.grounded,
            confidence=gen_response.confidence,
            sources=api_sources,
            retrieval=RAGRetrievalStats(
                top_k_requested=request.top_k,
                candidates_retrieved=candidates_retrieved,
                results_used=gen_response.context_items_used
            ),
            metadata=RAGMetadataSchema(
                provider=meta_dict.get("provider", "unknown"),
                model=meta_dict.get("model", "unknown"),
                embedding_model="BAAI/bge-small-en-v1.5",
                is_mock=meta_dict.get("is_mock", False),
                latency_ms=latency_tracker
            )
        )
