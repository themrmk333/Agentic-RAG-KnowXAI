

"""HR Policy Specialist Agent implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.state import AgentState


class HRAgent:
    """Specialist agent focused on HR policies, employee handbook, benefits, leaves, and attendance."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Execute HR policy query resolution based on query and context."""
        query = state.get("understood_query") or state.get("original_query", "")
        contexts = state.get("relevant_context", [])
        context_str = "\n".join(contexts) if contexts else "No relevant context found."

        system_instruction = (
            "You are an expert HR Policy Specialist Agent for MK Infinite Private Limited.\n\n"
            "ANSWER QUALITY & STEP-BY-STEP POLICY:\n"
            "1. Answer the user's question directly in simple, beginner-friendly English.\n"
            "2. For procedural questions and how-to workflows (e.g. applying for leave, onboarding, offboarding, grievance filing):\n"
            "   - Aim to provide 10 useful, numbered steps whenever the available information supports them.\n"
            "   - Format each step with a bold action title: '1. **[Step Title]:** [Simple, beginner-friendly explanation]'.\n"
            "   - Include eligibility, required documentation, approval workflow, portal submission, verification, and HR contact points.\n"
            "   - Cite relevant HR policies, SOP IDs, handbook sections, and portals.\n"
            "   - Conclude with a brief summary or recommended next action.\n"
            "3. For simple factual questions (e.g. leave allowances, holiday dates): Provide a direct answer and concise explanation instead of forcing 10 steps.\n"
            "4. Never repeat information, invent missing rules, or add unsupported details just to reach 10 steps. "
            "If documentation supports only a few steps, provide those verified steps and clearly explain what information is missing.\n"
            "5. Never return only document titles or headings. If required information is unavailable, explicitly state that it is not present in the company knowledge base."
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
            return {"specialist_results": {"hr": response.text}}
        except Exception as e:
            return {
                "specialist_results": {"hr": f"HR Agent failed: {str(e)}"},
                "errors": [f"HR agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
