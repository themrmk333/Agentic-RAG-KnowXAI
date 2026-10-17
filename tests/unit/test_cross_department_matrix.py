"""Comprehensive Cross-Department Universal Routing Matrix and Multi-Turn Verification.

Verifies:
1. ALL 4 DEPARTMENTS (IT Support, Finance & Claims, Human Resources, Project Department)
   can ask questions across ALL 5 MAJOR DOMAINS (IT, Finance, HR, Project, Research).
2. Question intent and specialist agent routing are determined purely by question domain,
   never by user department.
3. In multi-turn conversations, the user's department remains constant while intent
   and specialist agent change per question.
4. Actual document authorization is enforced (public/employee documents accessible across
   departments; restricted documents protected).
"""

import pytest
from typing import Any, List, Dict

from agents import create_workflow, AgentState
from agents.llm import LLMProvider, LLMResponse
from agents.rag import MockRAGRetriever
from agents.schemas.agent_schema import UnderstoodQuery, AgentPlan, FinalAnswer
from rag.retrieval.pgvector_retriever import PGVectorRetriever


class UniversalRoutingMockLLM(LLMProvider):
    """Mock LLM that accurately classifies queries into domain intents according to prompt guidelines."""

    def __init__(self) -> None:
        super().__init__(model="mock-matrix-llm")

    def _classify_intent(self, query: str) -> str:
        q = query.lower()
        if any(w in q for x in ["expense", "reimbursement", "claim", "salary", "billing", "payment", "invoice", "travel limit"] for w in [x]):
            return "finance"
        elif any(w in q for x in ["leave", "attendance", "maternity", "parental", "benefits", "handbook", "holiday"] for w in [x]):
            return "hr"
        elif any(w in q for x in ["password", "wi-fi", "wifi", "laptop", "vpn", "ticket", "support", "credentials", "cybersecurity"] for w in [x]):
            return "it"
        elif any(w in q for x in ["project", "sop", "sophia", "creation procedure", "guideline", "standard operating"] for w in [x]):
            return "project"
        elif any(w in q for x in ["research", "synthesize", "overview documentation", "multi-document"] for w in [x]):
            return "research"
        return "general"

    def _get_specialists(self, intent: str) -> List[str]:
        if intent == "finance":
            return ["finance", "critic"]
        elif intent == "hr":
            return ["hr", "critic"]
        elif intent == "it":
            return ["it", "critic"]
        elif intent == "project":
            return ["project", "critic"]
        elif intent == "research":
            return ["research", "critic", "decision"]
        elif intent == "coding":
            return ["coding", "critic"]
        elif intent == "mathematics":
            return ["mathematics", "critic"]
        return ["research", "critic"]

    def generate(self, prompt: str, *, temperature: float = 0.2) -> LLMResponse:
        return LLMResponse(text="Mock generated text.")

    def chat(self, messages: Any, *, temperature: float = 0.2) -> LLMResponse:
        user_content = ""
        for m in messages:
            if isinstance(m, dict) and m.get("role") == "user":
                user_content = m.get("content", "")
        return LLMResponse(
            text=f"Substantive procedural guidance based on company knowledge base:\n"
                 f"1. Authenticate with your enterprise credentials.\n"
                 f"2. Follow standard protocol described in policy document.\n"
                 f"3. Submit for verification."
        )

    def structured(
        self,
        messages: Any,
        response_model: type,
        *,
        temperature: float = 0.0,
    ) -> Any:
        query_text = ""
        for m in messages:
            if isinstance(m, dict) and m.get("role") == "user":
                query_text = m.get("content", "")

        if response_model == UnderstoodQuery:
            intent = self._classify_intent(query_text)
            return UnderstoodQuery(
                rephrased_query=query_text.replace("User Query: ", "").strip(),
                intent=intent,
                key_terms=["search", "terms"]
            )
        elif response_model == AgentPlan:
            intent = "general"
            for line in query_text.split("\n"):
                if "Intent Category:" in line:
                    intent = line.split("Intent Category:")[-1].strip().lower()
            specialists = self._get_specialists(intent)
            return AgentPlan(
                specialists=specialists,
                justification=f"Planner routing for domain: {intent}"
            )
        elif response_model == FinalAnswer:
            return FinalAnswer(
                answer="To complete this process according to company policy:\n\n"
                       "1. Access the knowledge portal.\n"
                       "2. Complete the standardized submission form.\n"
                       "3. Your departmental lead and respective specialist unit will review the request.",
                confidence=0.95,
                references=["Enterprise KB - General Procedures 2026"],
                errors_encountered=[]
            )

        raise ValueError(f"Unsupported model: {response_model}")


# All 4 Departments × 5 Major Domains = 20 Test Scenarios
ALL_DEPARTMENTS = ["IT Support", "Finance & Claims", "Human Resources", "Project Department"]

DOMAIN_QUERIES = [
    {
        "domain": "it",
        "agent": "it",
        "query": "How do I reset my corporate password and configure laptop Wi-Fi?",
    },
    {
        "domain": "finance",
        "agent": "finance",
        "query": "How do I submit an employee expense claim for reimbursement?",
    },
    {
        "domain": "hr",
        "agent": "hr",
        "query": "What is the company's maternity and annual leave policy?",
    },
    {
        "domain": "project",
        "agent": "project",
        "query": "What is the project creation procedure and Sophia SOP guidelines?",
    },
    {
        "domain": "research",
        "agent": "research",
        "query": "Please synthesize the multi-document overview documentation across departments.",
    },
]

UNIVERSAL_MATRIX_CASES = []
for dept in ALL_DEPARTMENTS:
    for q_item in DOMAIN_QUERIES:
        UNIVERSAL_MATRIX_CASES.append({
            "test_id": f"{dept.replace(' ', '_')}__asks__{q_item['domain'].upper()}",
            "department": dept,
            "query": q_item["query"],
            "expected_intent": q_item["domain"],
            "expected_agent": q_item["agent"],
        })


@pytest.mark.parametrize("tc", UNIVERSAL_MATRIX_CASES, ids=[tc["test_id"] for tc in UNIVERSAL_MATRIX_CASES])
def test_universal_cross_department_matrix_20_scenarios(tc: Dict[str, Any]):
    """Ensure every department can ask every major domain question and receive correct routing."""
    llm = UniversalRoutingMockLLM()
    retriever = MockRAGRetriever()
    workflow = create_workflow(llm, retriever)

    user_context = {
        "id": 200,
        "email": "employee@example.com",
        "username": "employee_user",
        "role": "Employee",
        "department": tc["department"],
    }

    initial_state: AgentState = {
        "original_query": tc["query"],
        "understood_query": None,
        "intent": None,
        "plan": None,
        "relevant_context": None,
        "specialist_results": {},
        "reasoning": None,
        "final_answer": None,
        "errors": [],
        "metadata": {},
        "user_context": user_context,
    }

    final_state = workflow.invoke(initial_state)

    # 1. Authenticated user department must remain constant
    assert final_state["user_context"]["department"] == tc["department"]

    # 2. Detected intent matches question domain, NOT user department
    assert final_state["intent"] == tc["expected_intent"]

    # 3. Specialist agent invoked matches question domain
    assert tc["expected_agent"] in final_state["plan"]
    assert tc["expected_agent"] in final_state["specialist_results"]

    # 4. Final answer is substantive and complete (not heading-only)
    final_ans = final_state["final_answer"]
    assert final_ans is not None
    assert len(final_ans["answer"]) > 50
    assert not final_ans["answer"].strip().startswith("### ") or "\n" in final_ans["answer"]


def test_multi_turn_department_invariance():
    """Verify that in multi-turn conversation, user department remains constant while intent & agent change."""
    llm = UniversalRoutingMockLLM()
    retriever = MockRAGRetriever()
    workflow = create_workflow(llm, retriever)

    user_department = "IT Support"
    user_context = {
        "id": 300,
        "email": "mahesh@example.com",
        "username": "mahesh_koli",
        "role": "Employee",
        "department": user_department,
    }

    # Turn 1: HR Question
    state_1: AgentState = {
        "original_query": "What is the company leave policy?",
        "understood_query": None,
        "intent": None,
        "plan": None,
        "relevant_context": None,
        "specialist_results": {},
        "reasoning": None,
        "final_answer": None,
        "errors": [],
        "metadata": {},
        "user_context": user_context,
    }
    result_1 = workflow.invoke(state_1)
    assert result_1["user_context"]["department"] == "IT Support"
    assert result_1["intent"] == "hr"
    assert "hr" in result_1["plan"]

    # Turn 2: Finance Question
    state_2: AgentState = {
        "original_query": "How do I claim reimbursement for travel expenses?",
        "understood_query": None,
        "intent": None,
        "plan": None,
        "relevant_context": None,
        "specialist_results": {},
        "reasoning": None,
        "final_answer": None,
        "errors": [],
        "metadata": {},
        "user_context": user_context,
    }
    result_2 = workflow.invoke(state_2)
    assert result_2["user_context"]["department"] == "IT Support"
    assert result_2["intent"] == "finance"
    assert "finance" in result_2["plan"]

    # Turn 3: IT Question
    state_3: AgentState = {
        "original_query": "My laptop Wi-Fi is not connecting to the office router.",
        "understood_query": None,
        "intent": None,
        "plan": None,
        "relevant_context": None,
        "specialist_results": {},
        "reasoning": None,
        "final_answer": None,
        "errors": [],
        "metadata": {},
        "user_context": user_context,
    }
    result_3 = workflow.invoke(state_3)
    assert result_3["user_context"]["department"] == "IT Support"
    assert result_3["intent"] == "it"
    assert "it" in result_3["plan"]


def test_document_level_authorization_enforced():
    """Verify that open/employee docs are accessible cross-department, but restricted docs require authorization."""
    retriever = PGVectorRetriever(None, None)

    # General policies
    doc_finance_general = {"access_level": "employee", "department": "Finance & Claims"}
    doc_hr_general = {"access_level": "employee", "department": "Human Resources"}

    # Confidential/restricted document
    doc_finance_confidential = {
        "access_level": "restricted",
        "allowed_departments": ["Finance & Claims"]
    }

    user_it = {"role": "Employee", "department": "IT Support"}
    user_finance = {"role": "Employee", "department": "Finance & Claims"}
    user_admin = {"role": "Admin", "department": "IT Support"}

    # IT user can access general Finance & HR docs
    assert retriever.check_document_access(doc_finance_general, user_it) is True
    assert retriever.check_document_access(doc_hr_general, user_it) is True

    # IT user CANNOT access restricted Finance doc
    assert retriever.check_document_access(doc_finance_confidential, user_it) is False

    # Finance user CAN access restricted Finance doc
    assert retriever.check_document_access(doc_finance_confidential, user_finance) is True

    # Admin CAN access restricted doc regardless of department
    assert retriever.check_document_access(doc_finance_confidential, user_admin) is True
