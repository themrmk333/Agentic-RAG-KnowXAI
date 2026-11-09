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
            "You are an expert Reasoning Agent for MK Infinite Private Limited.\n\n"
            "SYNTHESIS & STEP-BY-STEP REASONING DIRECTIVES:\n"
            "1. Synthesize specialist findings and strictly follow Critic Agent reviews to eliminate any ungrounded assertions or assumptions.\n"
            "2. For procedural, how-to, or troubleshooting questions:\n"
            "   - Construct a logical, step-by-step guide aiming for 10 numbered steps whenever supported by the evidence.\n"
            "   - Format each step with bold action titles: '1. **[Step Title]:** [Simple, beginner-friendly explanation]'.\n"
            "   - Cover prerequisites, required accounts/eligibility, request process, approval chain, configuration/provisioning, connection testing, verification, and troubleshooting/escalation.\n"
            "   - Include citations to relevant SOP IDs (e.g. SOP-IT-004, SOP-IT-004-EDGE-B), document titles, and systems of record.\n"
            "   - Conclude with a concise summary or recommended next action.\n"
            "3. For factual questions: Provide a direct answer and concise explanation instead of forcing 10 steps.\n"
            "4. Ground all claims in the retrieved company documents. Never invent missing steps, URLs, or policies.\n"
            "5. If only a few steps are supported by the documentation, explain those verified steps and clearly identify what details are missing."
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
