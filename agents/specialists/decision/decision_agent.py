"""Decision Agent specialist implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.state import AgentState


class DecisionAgent:
    """Specialist agent focused on trade-off analysis, option selection, and recommendations."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Execute decision logic and trade-off analysis based on specialist results."""
        query = state.get("understood_query") or state.get("original_query", "")
        contexts = state.get("relevant_context", [])
        context_str = "\n".join(contexts) if contexts else "No relevant context found."

        specialist_results = state.get("specialist_results", {})
        results_to_analyze = []
        for agent_name, result in specialist_results.items():
            if agent_name != "decision":
                results_to_analyze.append(f"[{agent_name.upper()} AGENT OUTPUT]:\n{result}")

        results_str = "\n\n".join(results_to_analyze) if results_to_analyze else "No other specialist output is available yet."

        system_instruction = (
            "You are a Decision Agent. Your goal is to analyze options, evaluate trade-offs based "
            "on constraints, and make a final, justified recommendation. Resolve any contradictions "
            "between specialists, using the Critic Agent's review as guidance."
        )

        user_content = (
            f"User Query / Goal: {query}\n\n"
            f"Context Constraints:\n{context_str}\n\n"
            f"Specialist Findings and Reviews:\n{results_str}"
        )

        try:
            response = self.llm.chat(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.1,
            )
            return {"specialist_results": {"decision": response.text}}
        except Exception as e:
            return {
                "specialist_results": {"decision": f"Decision Agent failed: {str(e)}"},
                "errors": [f"Decision agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
