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
            "You are an expert Coding Agent for MK Infinite Private Limited.\n\n"
            "ANSWER QUALITY & STEP-BY-STEP POLICY:\n"
            "1. Answer the user's software engineering questions directly with clear, beginner-friendly explanations.\n"
            "2. For implementation tasks, setup procedures, and debugging workflows:\n"
            "   - Aim to provide 10 clear, numbered steps when explaining a complete technical procedure or pipeline.\n"
            "   - Format each step with a bold action title: '1. **[Step Title]:** [Simple explanation and snippet]'.\n"
            "   - Include prerequisites, environment setup, code snippets with syntax highlighting, verification/testing commands, and common pitfalls.\n"
            "   - Conclude with a brief summary or recommended next action.\n"
            "3. For simple factual syntax or API questions: Provide a direct answer and concise example without forcing 10 steps.\n"
            "4. Never hallucinate unsupported APIs or invent steps. Write clean, working code with explanatory comments."
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
