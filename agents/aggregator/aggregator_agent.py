"""Aggregator Agent implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.schemas.agent_schema import FinalAnswer
from agents.state import AgentState


class AggregatorAgent:
    """Agent that aggregates reasoning and specialist outputs into a structured FinalAnswer."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Aggregate intermediate reasoning and results into the structured FinalAnswer output."""
        query = state.get("original_query", "")
        reasoning = state.get("reasoning", "")
        errors = state.get("errors", [])
        
        # Prepare context / metadata references
        contexts = state.get("relevant_context", [])
        
        messages = [
            {
                "role": "system",
                "content": (
                    "You are the Aggregator and final answer generation agent for an Enterprise AI Knowledge Assistant.\n"
                    "The retrieved company documents are the ONLY source of truth.\n\n"
                    "CORE DIRECTIVE:\n"
                    "- MAXIMUM INFORMATION FROM THE RETRIEVED COMPANY DATA + ZERO INVENTED INFORMATION.\n"
                    "- Answer the employee's question directly using the retrieved company documents.\n"
                    "- Do NOT invent, assume, estimate, infer, or fabricate dates, deadlines, amounts, percentages, approval levels, employee categories, eligibility rules, policies, procedures, responsibilities, departments, names, contacts, URLs, penalties, exceptions, tax rules, payment methods, timeframes, or steps.\n"
                    "- Do NOT use general world knowledge or add standard/common practices.\n\n"
                    "USE ALL RELEVANT RETRIEVED INFORMATION:\n"
                    "- When multiple retrieved documents answer the question, combine all relevant information, eliminate duplicates, and organize the content cleanly.\n"
                    "- Do NOT unnecessarily claim that information is missing when the retrieved documents provide enough details to answer the user's question.\n\n"
                    "NO META-COMMENTARY:\n"
                    "- Answer the employee's question directly without introductory disclaimers, discussion of the retrieval process, or descriptions of what documents failed to contain.\n"
                    "- Do NOT start with 'The available company knowledge base does not contain enough information...' unless the retrieved context genuinely lacks the information requested.\n\n"
                    "ANSWER FORMAT:\n"
                    "- For procedural questions: Start with a brief direct explanation, then provide the supported steps (using numbered lists), and include relevant conditions/exceptions ONLY if explicitly stated in the retrieved documents.\n"
                    "- Never return only a document title or heading.\n"
                    "- If information is genuinely missing to answer the core question, state briefly: 'The available company knowledge base does not contain enough information to provide a complete answer to this question.' Then provide ONLY the supported facts that are available.\n\n"
                    "METRICS & REFERENCES:\n"
                    "- Compute a confidence score (0.0 to 1.0) strictly based on context alignment.\n"
                    "- List the specific context/source descriptions used under 'references'."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Original Query: {query}\n\n"
                    f"Synthesized Reasoning:\n{reasoning}\n\n"
                    f"References Available:\n" + "\n".join(contexts)
                ),
            },
        ]

        try:
            structured_ans: FinalAnswer = self.llm.structured(
                messages=messages,
                response_model=FinalAnswer,
                temperature=0.1,
            )
            
            # Map FinalAnswer to dict for state storage
            result_dict = {
                "answer": structured_ans.answer,
                "confidence": structured_ans.confidence,
                "references": structured_ans.references,
                "errors_encountered": errors + structured_ans.errors_encountered,
            }
            
            return {"final_answer": result_dict}
        except Exception as e:
            # Fallback output in case structured generation fails
            fallback_dict = {
                "answer": f"Failed to structure final answer. Raw Reasoning:\n\n{reasoning}",
                "confidence": 0.5,
                "references": contexts,
                "errors_encountered": errors + [f"Aggregator structured generation failed: {str(e)}"],
            }
            return {"final_answer": fallback_dict}

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
