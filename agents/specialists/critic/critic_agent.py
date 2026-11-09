"""Critic Agent specialist implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.state import AgentState


class CriticAgent:
    """Specialist agent focused on code review, fact verification, and flaw detection."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Critique the outputs of other specialists and check for logical bugs or inconsistencies."""
        query = state.get("understood_query") or state.get("original_query", "")
        contexts = state.get("relevant_context", [])
        context_str = "\n".join(contexts) if contexts else "No relevant context found."

        specialist_results = state.get("specialist_results", {})
        results_to_review = []
        for agent_name, result in specialist_results.items():
            if agent_name != "critic":
                results_to_review.append(f"[{agent_name.upper()} AGENT OUTPUT]:\n{result}")

        results_str = "\n\n".join(results_to_review) if results_to_review else "No other specialist output is available yet."

        system_instruction = (
            "You are an expert Critic Agent and Quality Validation Specialist for MK Infinite Private Limited.\n\n"
            "Evaluate specialist findings and retrieved context against the 8 Answer Quality Invariants:\n"
            "1. QUERY RELEVANCE: Does the proposed output directly address the user's original query?\n"
            "2. INTENT PRESERVATION: Does the understood/rewritten query faithfully preserve the user's core intent?\n"
            "3. RETRIEVAL GROUNDING: Did retrieval return sufficient relevant evidence from company documents/SOPs?\n"
            "4. STEP-BY-STEP CLARITY: For procedural queries, are the steps clear, beginner-friendly, logically ordered, and formatted with bold action titles (aiming for up to 10 supported steps)?\n"
            "5. FACTUAL GROUNDING: Are all prerequisites, permissions, steps, deadlines, and policies strictly supported by the retrieved context?\n"
            "6. ACCURATE CITATIONS: Do citations reference the exact SOP IDs (e.g., SOP-IT-004, SOP-IT-004-EDGE-B), document titles, and systems of record?\n"
            "7. ZERO FABRICATION: Flag any fabricated steps, fake URLs, imaginary software clients, or repetitive filler content.\n"
            "8. PERMISSION INTEGRITY: Ensure no unauthorized or department-restricted information is improperly disclosed.\n\n"
            "Summarize verified findings, point out any ungrounded assertions or missing details, and guide the Reasoning and Aggregator agents to construct a completely grounded, step-by-step response."
        )

        user_content = (
            f"User Query: {query}\n\n"
            f"Retrieved Context:\n{context_str}\n\n"
            f"Specialist Outputs under Review:\n{results_str}"
        )

        try:
            response = self.llm.chat(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.1,
            )
            return {"specialist_results": {"critic": response.text}}
        except Exception as e:
            return {
                "specialist_results": {"critic": f"Critic Agent failed: {str(e)}"},
                "errors": [f"Critic agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
