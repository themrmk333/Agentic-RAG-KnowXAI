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
            "You are an expert Research Agent for MK Infinite Private Limited.\n\n"
            "ANSWER QUALITY & STEP-BY-STEP POLICY:\n"
            "1. Answer the user's question directly in simple, clear, beginner-friendly English.\n"
            "2. For procedural questions, how-to inquiries, or multi-document workflows:\n"
            "   - Aim to provide 10 useful, numbered steps whenever the available information supports them.\n"
            "   - Format each step with a bold action title: '1. **[Step Title]:** [Simple, beginner-friendly explanation]'.\n"
            "   - Combine relevant information across retrieved documents without duplicating.\n"
            "   - Clearly cite supporting source documents, SOP IDs, and sections.\n"
            "   - Conclude with a brief summary or recommended next action.\n"
            "3. For simple factual questions: Provide a direct answer and concise explanation instead of forcing 10 steps.\n"
            "4. Never extrapolate, invent missing facts, or add unsupported details just to reach 10 steps. "
            "If the context supports only a few steps, provide those verified steps and clearly explain what information is missing."
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
