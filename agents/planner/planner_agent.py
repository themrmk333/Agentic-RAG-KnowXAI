"""Planner Agent implementation."""

from typing import Any, Dict, List
from agents.llm import LLMProvider
from agents.schemas.agent_schema import AgentPlan
from agents.state import AgentState


class PlannerAgent:
    """Agent that determines which specialist agents are required for the query."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider
        self.allowed_specialists = {
            "research",
            "coding",
            "mathematics",
            "critic",
            "decision",
            "it",
            "hr",
            "finance",
            "project",
        }

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Analyze the query and context, decide on specialist routing, and return plan."""
        query = state.get("understood_query") or state.get("original_query", "")
        intent = state.get("intent", "general")
        context_str = "\n".join(state.get("relevant_context", []))

        # Fast-path bypass for general greetings or out-of-domain queries
        if intent == "general":
            return {
                "plan": [],
                "metadata": {"plan_justification": "General intent requires no specialist routing."},
            }

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a Planner Agent. Based on the user's search query, determined intent category, "
                    "and retrieved context, decide which specialist agents are required to fulfill the request.\n"
                    "Select a subset of specialists from the following allowed set: "
                    "['research', 'coding', 'mathematics', 'critic', 'decision', 'it', 'hr', 'finance', 'project'].\n"
                    "Do NOT always select all specialists. Be minimal but sufficient.\n"
                    "Rules:\n"
                    "- Coding tasks: use 'coding' and 'critic'.\n"
                    "- Mathematical tasks: use 'mathematics' and 'critic'.\n"
                    "- IT support, tickets, hardware/software, VPN, credentials: use 'it' and 'critic'.\n"
                    "- HR policies, handbook, leaves, onboarding/offboarding: use 'hr' and 'critic'.\n"
                    "- Salary, claims, reimbursements, billing, financial procedures: use 'finance' and 'critic'.\n"
                    "- Project execution, milestones, tracking, and project delays: use 'project' and 'critic'.\n"
                    "- Company-wide management, executive approvals, decision authority, organizational strategy, and management escalation: use 'decision' and 'critic'; add 'research' when multiple documents are needed.\n"
                    "- Research tasks / multi-document: use 'research', 'critic', and 'decision'.\n"
                    "- Complex tasks: select multiple relevant specialists (e.g., 'research', 'coding', 'critic', 'decision')."
                ),
            },
            {
                "role": "user",
                "content": f"Query: {query}\nIntent Category: {intent}\nRetrieved Context:\n{context_str}",
            },
        ]

        try:
            plan_data: AgentPlan = self.llm.structured(
                messages=messages,
                response_model=AgentPlan,
                temperature=0.0,
            )
            
            # Filter and validate planned specialists
            specialists = [
                s.lower().strip()
                for s in plan_data.specialists
                if s.lower().strip() in self.allowed_specialists
            ]

            # If no valid specialist was selected, fall back based on intent
            if not specialists:
                specialists = self._fallback_plan(intent)

            return {
                "plan": specialists,
                "metadata": {"plan_justification": plan_data.justification},
            }
        except Exception as e:
            # Safe fallback if LLM structured generation fails
            fallback = self._fallback_plan(intent)
            return {
                "plan": fallback,
                "errors": [f"Planning agent failed: {str(e)}. Used fallback plan."],
                "metadata": {"plan_justification": "Fallback due to planning error."},
            }

    def _fallback_plan(self, intent: str) -> List[str]:
        if intent == "coding":
            return ["coding", "critic"]
        elif intent == "mathematics":
            return ["mathematics", "critic"]
        elif intent == "it":
            return ["it", "critic"]
        elif intent == "hr":
            return ["hr", "critic"]
        elif intent == "finance":
            return ["finance", "critic"]
        elif intent == "management":
            return ["decision", "critic"]
        elif intent == "project":
            return ["project", "critic"]
        elif intent == "research":
            return ["research", "critic", "decision"]
        elif intent == "general":
            return []
        else:
            return ["research", "critic"]

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
