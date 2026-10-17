"""Research Agent specialist implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.state import AgentState


class ResearchAgent:
    """Specialist agent focused on summarization, search, and fact extraction."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Execute research tasks on the retrieved context and user query."""
        query = state.get("understood_query") or state.get("original_query", "")
        contexts = state.get("relevant_context", [])
        context_str = "\n".join(contexts) if contexts else "No relevant context found."

        system_instruction = (
            "You are a Research Agent. Your goal is to extract facts, summarize information, "
            "and answer queries based strictly on the provided context passages. Do not extrapolate "
            "or invent details. If the context does not contain the answer, clearly state what information "
            "is missing."
        )

        user_content = f"User Query: {query}\n\nRetrieved Context:\n{context_str}"

        try:
            response = self.llm.chat(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.2,
            )
            return {"specialist_results": {"research": response.text}}
        except Exception as e:
            return {
                "specialist_results": {"research": f"Research Agent failed: {str(e)}"},
                "errors": [f"Research agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
