"""Project Specialist Agent implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.state import AgentState


class ProjectAgent:
    """Specialist agent focused on project documentation, project guidelines, SOPs, and team structure."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Execute Project queries based on query and context."""
        query = state.get("understood_query") or state.get("original_query", "")
        contexts = state.get("relevant_context", [])
        context_str = "\n".join(contexts) if contexts else "No relevant context found."

        system_instruction = (
            "You are a Project Specialist Agent. Your goal is to answer queries related to project details, "
            "project documentation, internal Standard Operating Procedures (SOPs), team structures, project guides, "
            "and department-specific guidelines. Base your answer strictly on the provided context. "
            "Provide clear, complete, and substantive explanations or procedures from the context, "
            "never just document titles or section headings. "
            "If the answer is not present in the context, explicitly say that the required project/SOP "
            "information is not available in the company knowledge base."
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
            return {"specialist_results": {"project": response.text}}
        except Exception as e:
            return {
                "specialist_results": {"project": f"Project Agent failed: {str(e)}"},
                "errors": [f"Project agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
