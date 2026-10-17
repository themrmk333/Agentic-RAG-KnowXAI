"""Query Understanding Agent implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.rag import RAGRetriever
from agents.schemas.agent_schema import UnderstoodQuery
from agents.state import AgentState


class QueryUnderstandingAgent:
    """Agent that rephrases, classifies, and retrieves initial contexts for user queries."""

    def __init__(self, llm_provider: LLMProvider, retriever: RAGRetriever) -> None:
        self.llm = llm_provider
        self.retriever = retriever

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Analyze the original query, run retrieval, and return updated state attributes."""
        query = state.get("original_query", "").strip()
        if not query:
            return {
                "errors": ["Empty user query received in query understanding."],
                "understood_query": "",
                "intent": "general",
                "relevant_context": [],
            }
            
        # Fast-path for greetings
        greetings = {"hi", "hello", "hey", "good morning", "good evening", "thanks", "thank you"}
        if query.lower().strip() in greetings:
            return {
                "understood_query": query,
                "intent": "general",
                "relevant_context": [],
                "metadata": {
                    **(state.get("metadata") or {}),
                    "retrieved_count": 0,
                    "authorized_count": 0,
                }
            }

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a Query Understanding Agent. Your role is to rephrase the query to be search-optimized, "
                    "determine its intent classification ('coding', 'mathematics', 'research', 'it', 'hr', 'finance', 'project', 'management', 'sales', 'greeting', or 'general'), "
                    "and extract key search terms for retrieval.\n\n"
                    "Intent Classification Guidelines:\n"
                    "- 'finance': Any questions about salary, payroll, claims, expenses, reimbursement, payment, billing, invoice, travel reimbursement limit, financial claims, and finance policies. CRITICAL: Queries containing terms like 'expense', 'reimbursement', or 'claims' MUST be classified as 'finance', NOT 'hr' (even if they mention 'employee expense').\n"
                    "- 'hr': Human Resources topics including leave policy, attendance, maternity/parental leave, onboarding, offboarding, recruitment, employee benefits, handbook, holidays, and employee relations.\n"
                    "- 'it': Hardware/software issues, credentials, passwords, network, Wi-Fi, internet, printer, VPN, credentials, laptop setup, corporate cybersecurity policies, or IT support tickets.\n"
                    "- 'project': Project-specific creation, milestones, project documentation, project tracking, and project delays.\n"
                    "- 'management': Company-wide initiatives, approval authority, executive decisions, organizational policies, management escalation, and strategic priorities. Do not classify these as 'project' unless the query specifically concerns project execution.\n"
                    "- 'sales': Sales procedures, commission, client onboarding, sales CRM, or sales processes.\n"
                    "- 'coding': Code development, debugging, syntax, or software engineering questions.\n"
                    "- 'mathematics': Math calculations, equations, derivations, or statistical analysis.\n"
                    "- 'research': Multi-document synthesis or general information research.\n"
                    "- 'greeting': Greetings, pleasantries, or simple conversational hello.\n"
                    "- 'general': Casual chat or general assistance that doesn't fit other categories."
                ),
            },
            {"role": "user", "content": f"User Query: {query}"},
        ]

        try:
            understood_data: UnderstoodQuery = self.llm.structured(
                messages=messages,
                response_model=UnderstoodQuery,
                temperature=0.0,
            )
            
            search_query = understood_data.rephrased_query or query
            user_context = state.get("user_context")
            stats = {}
            if understood_data.intent == "general":
                retrieved = []
                stats["retrieved_count"] = 0
                stats["authorized_count"] = 0
            else:
                retrieved = self.retriever.retrieve(
                    query=search_query,
                    top_k=5,
                    user_context=user_context,
                    stats=stats,
                    intent=understood_data.intent,
                )
            
            return {
                "understood_query": understood_data.rephrased_query,
                "intent": understood_data.intent,
                "relevant_context": retrieved,
                "metadata": {
                    **(state.get("metadata") or {}),
                    "retrieved_count": stats.get("retrieved_count", 0),
                    "authorized_count": stats.get("authorized_count", 0),
                }
            }
        except Exception as e:
            user_context = state.get("user_context")
            stats = {}
            fallback_retrieved = self.retriever.retrieve(
                query=query,
                top_k=3,
                user_context=user_context,
                stats=stats,
            )
            return {
                "errors": [f"Query understanding failed: {str(e)}"],
                "understood_query": query,
                "intent": "general",
                "relevant_context": fallback_retrieved,
                "metadata": {
                    **(state.get("metadata") or {}),
                    "retrieved_count": stats.get("retrieved_count", 0),
                    "authorized_count": stats.get("authorized_count", 0),
                }
            }
        
    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
