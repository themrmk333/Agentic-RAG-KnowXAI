"""Mathematics Agent specialist implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.state import AgentState


class MathematicsAgent:
    """Specialist agent focused on mathematical derivations, formula application, and verification."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Execute math reasoning tasks on the query and context."""
        query = state.get("understood_query") or state.get("original_query", "")
        contexts = state.get("relevant_context", [])
        context_str = "\n".join(contexts) if contexts else "No relevant context found."

        system_instruction = (
            "You are a Mathematics Agent. Your goal is to solve mathematical problems, "
            "perform step-by-step logic and derivations, and verify calculations. Show all working clearly "
            "using standard mathematical notation."
        )

        user_content = f"User Query: {query}\n\nRelevant Context (if any):\n{context_str}"

        try:
            response = self.llm.chat(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.0,
            )
            return {"specialist_results": {"mathematics": response.text}}
        except Exception as e:
            return {
                "specialist_results": {"mathematics": f"Mathematics Agent failed: {str(e)}"},
                "errors": [f"Mathematics agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
