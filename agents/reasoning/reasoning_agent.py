"""Reasoning and Answer Generation Agent implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.state import AgentState


class ReasoningAgent:
    """Agent that synthesizes specialist results and critic reviews into a logical reasoning path."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Synthesize specialist and critic inputs into a coherent reasoning block."""
        query = state.get("understood_query") or state.get("original_query", "")
        contexts = state.get("relevant_context", [])
        context_str = "\n".join(contexts) if contexts else "No relevant context found."

        specialist_results = state.get("specialist_results", {})
        results_list = []
        for name, res in specialist_results.items():
            results_list.append(f"=== {name.upper()} SPECIALIST FINDINGS ===\n{res}")

        specialists_str = "\n\n".join(results_list) if results_list else "No specialist outputs were generated."

        system_instruction = (
            "You are a Reasoning Agent. Your goal is to synthesize the findings from various "
            "specialist agents, strictly adhere to Critic Agent reviews to eliminate any ungrounded assumptions, "
            "remove contradictions where possible, and construct a logical, step-by-step reasoning path.\n"
            "STRICT GROUNDING RULES:\n"
            "- Rely exclusively on facts present in the retrieved company documents.\n"
            "- Combine all relevant information from multiple documents into clear, coherent steps.\n"
            "- Do NOT add details, dates, percentages, amounts, deadlines, or roles from general world knowledge.\n"
            "- Answer directly without unnecessary meta-commentary about the retrieval process or missing details, unless information is genuinely absent.\n"
            "- Ensure that all procedural steps and policy explanations are faithful to the source material."
        )

        user_content = (
            f"Goal: {query}\n\n"
            f"Context Data:\n{context_str}\n\n"
            f"Specialist and Critic Inputs:\n{specialists_str}"
        )

        try:
            response = self.llm.chat(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.2,
            )
            return {"reasoning": response.text}
        except Exception as e:
            return {
                "reasoning": f"Reasoning Agent synthesis failed: {str(e)}",
                "errors": [f"Reasoning agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
