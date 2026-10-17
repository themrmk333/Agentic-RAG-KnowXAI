"""Groundedness and Safety Validator for Step 8."""

from __future__ import annotations

import re
from typing import Dict, List, Optional

from rag.context.models import AssembledContext
from rag.generation.models import GeneratedAnswer, GroundingValidationResult


class GroundingValidator:
    """Validates that a generated answer is grounded in the provided context and safe."""

    def __init__(self, strict_mode: bool = True):
        self.strict_mode = strict_mode

    def _check_insufficient_context_claims(self, answer: str, context: Optional[AssembledContext]) -> bool:
        """Check if answer fabricates information when context is empty."""
        has_context = context is not None and len(context.items) > 0
        
        # Standard phrases that indicate the model safely refused to answer
        refusal_phrases = [
            "insufficient information",
            "insufficient knowledge",
            "cannot answer",
            "does not contain",
            "no enterprise context",
            "not mentioned in the provided document",
        ]
        
        is_refusal = any(phrase in answer.lower() for phrase in refusal_phrases)
        
        if not has_context and not is_refusal:
            # Answer is likely hallucinating since there is no context but it didn't refuse
            return False
            
        return True

    def _check_prompt_leakage(self, answer: str) -> bool:
        """Check for leaked system prompts, markers, or credentials."""
        leak_patterns = [
            r"<enterprise_knowledge_context>",
            r"</enterprise_knowledge_context>",
            r"<user_query>",
            r"</user_query>",
            r"You are an enterprise AI assistant",
            r"STRICT RULES:",
            r"system_instruction",
        ]
        for pattern in leak_patterns:
            if re.search(pattern, answer, re.IGNORECASE):
                return False
        return True

    def _extract_citations(self, answer: str) -> List[int]:
        """Extract [Doc #X] citations from the answer."""
        citations = re.findall(r"\[(?:Doc|Document)\s*#?(\d+)\]", answer, re.IGNORECASE)
        return [int(c) for c in citations]

    def validate(
        self, 
        query: str, 
        answer: GeneratedAnswer, 
        context: Optional[AssembledContext]
    ) -> GroundingValidationResult:
        """Perform comprehensive grounding and safety validation."""
        
        checks: Dict[str, bool] = {
            "query_valid": bool(query and query.strip()),
            "answer_valid": bool(answer and answer.answer.strip()),
            "context_present": context is not None and len(context.items) > 0,
            "no_prompt_leakage": self._check_prompt_leakage(answer.answer),
            "no_hallucination_on_empty": self._check_insufficient_context_claims(answer.answer, context),
            "citations_valid": True,
        }
        
        # Determine base grounding and confidence
        is_grounded = True
        confidence = "HIGH"
        reason = None
        unsupported_claims: List[str] = []
        
        if not checks["answer_valid"]:
            return GroundingValidationResult(
                status="FAIL",
                is_grounded=False,
                confidence="NONE",
                reason="Generated answer is empty.",
                checks=checks
            )
            
        if not checks["no_prompt_leakage"]:
            return GroundingValidationResult(
                status="REJECTED",
                is_grounded=False,
                confidence="NONE",
                reason="Prompt leakage or forbidden markers detected in the answer.",
                checks=checks
            )
            
        if not checks["context_present"]:
            if checks["no_hallucination_on_empty"]:
                # The model correctly stated it couldn't answer
                confidence = "INSUFFICIENT_CONTEXT"
            else:
                # The model hallucinated an answer without context
                is_grounded = False
                confidence = "NONE"
                reason = "Hallucinated response when no context was available."
                checks["no_hallucination_on_empty"] = False
                unsupported_claims.append("Answer generated without supporting context.")
        else:
            # Context is present, check citations
            valid_doc_ids = {item.document_id for item in context.items}
            cited_doc_ids = self._extract_citations(answer.answer)
            
            for doc_id in cited_doc_ids:
                if doc_id not in valid_doc_ids:
                    checks["citations_valid"] = False
                    is_grounded = False
                    confidence = "LOW"
                    reason = f"Fabricated citation detected: Doc #{doc_id}"
                    unsupported_claims.append(f"Cited Doc #{doc_id} which was not in retrieved context.")
                    break
                    
        # Final status evaluation
        status = "PASS"
        if not is_grounded:
            status = "FAIL"
            
        return GroundingValidationResult(
            status=status,
            is_grounded=is_grounded,
            confidence=confidence,
            reason=reason,
            unsupported_claims=unsupported_claims,
            citations_valid=checks["citations_valid"],
            context_used_count=len(context.items) if context else 0,
            total_context_items=len(context.items) if context else 0,
            checks=checks
        )
