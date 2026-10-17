"""Answer Generation orchestrator for Step 8."""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional

from rag.context.models import AssembledContext
from rag.generation.grounding_validator import GroundingValidator
from rag.generation.models import GenerationRequest, GenerationResponse, SourceReference
from rag.generation.prompt_builder import PromptBuilder
from rag.generation.providers import ProviderFactory

logger = logging.getLogger(__name__)


class AnswerGenerator:
    """Orchestrates the LLM generation and grounding validation pipeline."""

    def __init__(
        self,
        prompt_builder: Optional[PromptBuilder] = None,
        validator: Optional[GroundingValidator] = None,
    ):
        self.prompt_builder = prompt_builder or PromptBuilder()
        self.validator = validator or GroundingValidator()

    def _build_source_references(self, context: Optional[AssembledContext]) -> list[SourceReference]:
        """Convert Step 7 ContextItems to Step 8 SourceReferences."""
        if not context or not context.items:
            return []
            
        sources = []
        for item in context.items:
            sources.append(
                SourceReference(
                    document_id=item.document_id,
                    chunk_id=item.chunk_id,
                    chunk_index=item.chunk_index,
                    document_title=item.document_title,
                    source=item.source,
                    snippet=item.text,
                    semantic_score=item.semantic_score,
                    rerank_score=item.rerank_score,
                    metadata=item.metadata,
                )
            )
        return sources

    def generate_answer(self, request: GenerationRequest) -> GenerationResponse:
        """Run the end-to-end generation pipeline for a given request."""
        
        # 1. Input Validation
        if not request.query or not request.query.strip():
            return GenerationResponse(
                query=request.query or "",
                answer="",
                grounded=False,
                confidence="NONE",
                validation_status="FAIL",
                error="Query cannot be empty or whitespace.",
                failure_reason="INVALID_QUERY"
            )
            
        # 2. Extract Context
        context = request.assembled_context
        
        # 3. Build Prompt
        built_prompt = self.prompt_builder.build(
            query=request.query,
            context=context
        )
        
        # 4. Resolve Provider
        try:
            provider = ProviderFactory.get_provider(
                provider_name=request.provider,
                assembled_context=context
            )
        except Exception as e:
            logger.error(f"Failed to initialize LLM provider: {e}")
            return GenerationResponse(
                query=request.query,
                answer="",
                grounded=False,
                confidence="NONE",
                validation_status="FAIL",
                error=f"Provider initialization failed: {str(e)}",
                failure_reason="PROVIDER_ERROR"
            )

        # 5. Generate Answer
        try:
            generated_answer = provider.generate(
                prompt=built_prompt.user_prompt,
                system_prompt=built_prompt.system_prompt,
                temperature=request.temperature,
                max_tokens=request.max_tokens,
            )
        except Exception as e:
            logger.error(f"LLM generation failed: {e}")
            return GenerationResponse(
                query=request.query,
                answer="",
                grounded=False,
                confidence="NONE",
                validation_status="FAIL",
                error=f"LLM generation failed: {str(e)}",
                failure_reason="GENERATION_ERROR"
            )
            
        # 6. Validate Grounding & Safety
        validation_result = self.validator.validate(
            query=request.query,
            answer=generated_answer,
            context=context
        )
        
        # 7. Compile Final Provenance
        sources = self._build_source_references(context)
        
        # 8. Construct Response
        return GenerationResponse(
            query=request.query,
            answer=generated_answer.answer,
            grounded=validation_result.is_grounded,
            confidence=validation_result.confidence,
            sources=sources,
            context_items_used=len(sources),
            validation_status=validation_result.status,
            validation_result=validation_result,
            generation_metadata={
                "provider": provider.get_name(),
                "model": generated_answer.model_name,
                "latency_ms": generated_answer.latency_ms,
                "prompt_tokens": generated_answer.prompt_tokens,
                "completion_tokens": generated_answer.completion_tokens,
                "total_tokens": generated_answer.total_tokens,
                "is_mock": generated_answer.is_mock,
            },
            error=validation_result.reason if validation_result.status != "PASS" else None,
            failure_reason=validation_result.status if validation_result.status != "PASS" else None,
        )
