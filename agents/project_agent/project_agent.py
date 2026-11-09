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
            "You are an expert Project Specialist Agent for MK Infinite Private Limited.\n\n"
            "ANSWER QUALITY & STEP-BY-STEP POLICY:\n"
            "1. Answer the user's question directly in simple, beginner-friendly English.\n"
            "2. For procedural questions and project workflows (e.g. project creation SOPs, milestone sign-off, delay escalation, sprint cadence):\n"
            "   - Aim to provide 10 useful, numbered steps whenever the available information supports them.\n"
            "   - Format each step with a bold action title: '1. **[Step Title]:** [Simple, beginner-friendly explanation]'.\n"
            "   - Include initiation preconditions, stakeholder alignment, documentation templates, tracking systems, milestone reviews, verification, and closure.\n"
            "   - Cite relevant Project SOP IDs, guidelines, and project management tools.\n"
            "   - Conclude with a brief summary or recommended next action.\n"
            "3. For simple factual questions (e.g. project owner, milestone date): Provide a direct answer and concise explanation instead of forcing 10 steps.\n"
            "4. Never repeat information, invent missing processes, or add unsupported details just to reach 10 steps. "
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
            return {"specialist_results": {"project": response.text}}
        except Exception as e:
            return {
                "specialist_results": {"project": f"Project Agent failed: {str(e)}"},
                "errors": [f"Project agent execution error: {str(e)}"],
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
