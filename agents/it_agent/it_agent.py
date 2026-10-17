"""IT Support Specialist Agent implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.state import AgentState


class ITAgent:
    """Specialist agent focused on IT support, VPN access, password resets, software/hardware, and tickets."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Execute IT troubleshooting or information retrieval based on query and context."""
        query = state.get("understood_query") or state.get("original_query", "")
        contexts = state.get("relevant_context", [])
        context_str = "\n".join(contexts) if contexts else "No relevant context found."

        system_instruction = (
            "You are an IT Support Specialist Agent. Your goal is to answer queries related to IT support, "
            "VPN configuration, software or hardware issues, support ticket raising procedures, password policies, "
            "network settings, and corporate cybersecurity procedures. Base your answer strictly on the provided context. "
            "Provide clear, complete, and substantive troubleshooting steps or procedures from the context, "
            "never just document titles or section headings. "
            "If the answer is not present in the context, explicitly say that the required IT policy/procedure "
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
            return {"specialist_results": {"it": response.text}}
        except Exception as e:
            return {
                "specialist_results": {"it": f"IT Agent failed: {str(e)}"},
                "errors": [f"IT agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
