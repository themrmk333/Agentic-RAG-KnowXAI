"""Coding Agent specialist implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.state import AgentState


class CodingAgent:
    """Specialist agent focused on code generation, software design, and script explanation."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Execute coding tasks based on user query and context."""
        query = state.get("understood_query") or state.get("original_query", "")
        contexts = state.get("relevant_context", [])
        context_str = "\n".join(contexts) if contexts else "No relevant context found."

        system_instruction = (
            "You are a Coding Agent. Your goal is to write clean, efficient, and well-commented code, "
            "explain scripts, and design robust software architectures/APIs. Support your answer with "
            "code blocks (markdown formatted) where appropriate."
        )

        user_content = f"User Query: {query}\n\nRelevant Context (if any):\n{context_str}"

        try:
            response = self.llm.chat(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.2,
            )
            return {"specialist_results": {"coding": response.text}}
        except Exception as e:
            return {
                "specialist_results": {"coding": f"Coding Agent failed: {str(e)}"},
                "errors": [f"Coding agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
