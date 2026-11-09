"""Comprehensive validation test suite covering the 8 critical bug fix requirements."""

import pytest
from agents.query.understanding import QueryUnderstandingAgent, classify_intent_rules
from agents.planner.planner_agent import PlannerAgent
from rag.retrieval.query_embedder import QueryEmbedder
from rag.retrieval.semantic_retriever import SemanticRetriever
from agents.graph.workflow import create_workflow
from agents.llm import LLMProvider
from database.connection import SessionLocal


class MockTestingLLM(LLMProvider):
    """Deterministic LLM for testing workflow routing, agent selection, and prompt flows."""
    def __init__(self, model: str = "mock-testing"):
        super().__init__(model)

    def generate(self, prompt: str, *, temperature: float = 0.2):
        return self.chat([{"role": "user", "content": prompt}], temperature=temperature)

    def chat(self, messages, *, temperature: float = 0.2):
        from agents.llm.providers import LLMResponse
        last_content = messages[-1].get("content", "")
        # Check system prompt role
        sys_prompt = messages[0].get("content", "") if messages else ""
        
        if "IT Support Specialist" in sys_prompt:
            return LLMResponse(
                text=(
                    "### Corporate VPN Access Setup & Troubleshooting Guide\n\n"
                    "1. **Confirm Preconditions:** Verify active MK-Infinite-AI account and MK-ServiceDesk access.\n"
                    "2. **Obtain Manager Approval:** Ensure valid business need for remote access has manager endorsement.\n"
                    "3. **Submit Request in MK-ServiceDesk:** Navigate to MK-ServiceDesk and select Corporate VPN Access Setup (SOP-IT-004).\n"
                    "4. **Specify Required Access Profile:** Enter employee ID, department, and specific network resources required.\n"
                    "5. **System Administrator Security Review:** The System Administrator reviews request under least-privilege principles.\n"
                    "6. **IT Engineer Provisioning:** Once approved, the IT engineer configures VPN credentials in the gateway.\n"
                    "7. **Receive Notification:** Employee is notified via MK-ServiceDesk with client connection instructions.\n"
                    "8. **Connect to Corporate VPN:** Launch the corporate client and enter authorized credentials.\n"
                    "9. **Test & Verify Internal Access:** Verify access to company intranet and internal tools; log any issues in MK-ServiceDesk.\n"
                    "10. **Inactivity Policy & Escalation:** Note that credentials revoke after 90 days of inactivity. Escalate delays to IT Support Engineer -> IT Manager -> IT Director."
                ),
                raw=None
            )
        elif "Critic Agent" in sys_prompt:
            return LLMResponse(
                text="The specialist findings strictly adhere to SOP-IT-004. Preconditions, request steps, approval roles, and escalation are grounded in retrieved evidence.",
                raw=None
            )
        elif "Reasoning Agent" in sys_prompt:
            return LLMResponse(
                text=(
                    "### Verified Corporate VPN Access Procedure\n\n"
                    "1. **Verify Prerequisites:** Active company account, manager approval, and valid business need.\n"
                    "2. **Gather Required Details:** Employee ID, department, and specific access requirements.\n"
                    "3. **Open MK-ServiceDesk Portal:** Access the corporate service desk portal.\n"
                    "4. **Submit VPN Access Request:** Fill out ticket under SOP-IT-004.\n"
                    "5. **Manager Endorsement:** Ensure manager approves the submitted ticket.\n"
                    "6. **System Administrator Review:** Approver validates need-basis justification.\n"
                    "7. **Technical Configuration:** Engineer provisions user gateway configuration.\n"
                    "8. **Receive Credentials:** User receives connection parameters.\n"
                    "9. **Connection Verification:** User tests internal network reachability.\n"
                    "10. **Inactivity Expiry & Escalation:** Inactivity revokes credentials after 90 days. Escalation: IT Support Engineer -> IT Manager -> IT Director."
                ),
                raw=None
            )
        return LLMResponse(text="Standard response.", raw=None)

    def structured(self, messages, response_model, *, temperature: float = 0.0):
        from agents.schemas.agent_schema import UnderstoodQuery, AgentPlan, FinalAnswer
        last_content = messages[-1].get("content", "")
        
        if response_model == UnderstoodQuery:
            intent, conf, is_proc, rewrite, alts = classify_intent_rules(last_content)
            return UnderstoodQuery(
                rephrased_query=rewrite,
                intent=intent,
                key_terms=["vpn", "corporate", "sop-it-004"],
                alternative_queries=alts,
                is_procedural=is_proc
            )
        elif response_model == AgentPlan:
            # Planner
            if "Intent Category: it" in last_content or "vpn" in last_content.lower():
                return AgentPlan(
                    specialists=["it", "critic"],
                    justification="IT queries require IT specialist and Critic verification."
                )
            elif "Intent Category: hr" in last_content or "leave" in last_content.lower():
                return AgentPlan(
                    specialists=["hr", "critic"],
                    justification="HR queries require HR specialist."
                )
            elif "Intent Category: finance" in last_content or "expense" in last_content.lower():
                return AgentPlan(
                    specialists=["finance", "critic"],
                    justification="Finance queries require Finance specialist."
                )
            return AgentPlan(specialists=[], justification="General intent.")
        elif response_model == FinalAnswer:
            return FinalAnswer(
                answer=(
                    "### Corporate VPN Access Setup & Troubleshooting\n\n"
                    "1. **Verify Prerequisites:** Ensure you have an active MK-Infinite-AI account and manager approval.\n"
                    "2. **Access MK-ServiceDesk:** Log in to the corporate MK-ServiceDesk portal.\n"
                    "3. **Select VPN Access Request:** Navigate to IT Support -> Network -> Corporate VPN Access (SOP-IT-004).\n"
                    "4. **Provide Required Details:** Input your Employee ID, department, and justification.\n"
                    "5. **Submit for Approval:** Submit the ticket for System Administrator review.\n"
                    "6. **Security Review:** System Administrator reviews and approves under least-privilege principles.\n"
                    "7. **Gateway Provisioning:** The assigned IT engineer configures your VPN access.\n"
                    "8. **Receive Credentials:** You will be notified with your connection settings.\n"
                    "9. **Test Connection:** Connect to the VPN and verify access to internal services.\n"
                    "10. **Inactivity & Escalation:** Inactivity revokes credentials after 90 days. Escalate delays to IT Support Engineer -> IT Manager -> IT Director."
                ),
                confidence=0.92,
                references=["SOP-IT-004: Corporate VPN Access Setup", "MK-ServiceDesk"],
                errors_encountered=[]
            )
        return response_model()


@pytest.fixture
def retriever():
    return SemanticRetriever(session_factory=SessionLocal)


@pytest.fixture
def mock_llm():
    return MockTestingLLM()


# =========================================================================
# REQUIREMENT 1: "how to on VPN"
# =========================================================================
def test_req_01_how_to_on_vpn(retriever, mock_llm):
    wf = create_workflow(mock_llm, retriever)
    res = wf.invoke({
        "original_query": "how to on VPN",
        "conversation_history": [],
        "errors": [],
        "specialist_results": {},
        "user_context": {"id": 1, "role": "Employee", "department": "IT Support"}
    })
    
    assert res["intent"] == "it", f"Expected intent 'it', got {res['intent']}"
    assert "it" in res.get("plan", []), f"Expected 'it' in plan, got {res.get('plan')}"
    assert res.get("is_procedural") is True
    
    final_ans = res.get("final_answer", {})
    ans_text = final_ans.get("answer", "")
    assert len(ans_text) > 150
    assert "1. **" in ans_text
    assert "10. **" in ans_text
    assert "SOP-IT-004" in " ".join(final_ans.get("references", [])) or "SOP-IT-004" in ans_text


# =========================================================================
# REQUIREMENT 2: "how to on vpn"
# =========================================================================
def test_req_02_how_to_on_vpn_lowercase(retriever, mock_llm):
    wf = create_workflow(mock_llm, retriever)
    res = wf.invoke({
        "original_query": "how to on vpn",
        "conversation_history": [],
        "errors": [],
        "specialist_results": {},
        "user_context": {"id": 1, "role": "Employee", "department": "IT Support"}
    })
    
    assert res["intent"] == "it"
    assert "it" in res.get("plan", [])
    assert res.get("is_procedural") is True


# =========================================================================
# REQUIREMENT 3: "I am unable to connect to the corporate VPN. How do I fix it?"
# =========================================================================
def test_req_03_unable_to_connect_vpn(retriever, mock_llm):
    wf = create_workflow(mock_llm, retriever)
    res = wf.invoke({
        "original_query": "I am unable to connect to the corporate VPN. How do I fix it?",
        "conversation_history": [],
        "errors": [],
        "specialist_results": {},
        "user_context": {"id": 1, "role": "Employee", "department": "IT Support"}
    })
    
    assert res["intent"] == "it"
    assert "it" in res.get("plan", [])
    assert res.get("is_procedural") is True
    final_ans = res.get("final_answer", {})
    assert len(final_ans.get("answer", "")) > 100


# =========================================================================
# REQUIREMENT 4: "How do I request urgent VPN access?"
# =========================================================================
def test_req_04_urgent_vpn_access(retriever, mock_llm):
    intent, conf, is_proc, rewrite, alts = classify_intent_rules("How do I request urgent VPN access?")
    assert intent == "it"
    assert is_proc is True
    assert "SOP-IT-004-EDGE-B" in rewrite or "urgent" in rewrite.lower()
    assert conf >= 0.85 and conf <= 0.98


# =========================================================================
# REQUIREMENT 5: "What is the leave policy?"
# =========================================================================
def test_req_05_leave_policy(retriever, mock_llm):
    intent, conf, is_proc, rewrite, alts = classify_intent_rules("What is the leave policy?")
    assert intent == "hr"
    assert "POL-HR-001" in rewrite or "leave" in rewrite.lower()
    
    # Verify retrieval against pgvector
    results = retriever.retrieve("What is the leave policy?", top_k=3, intent="hr")
    assert len(results) > 0
    joined = " ".join(results)
    assert "leave" in joined.lower()


# =========================================================================
# REQUIREMENT 6: "How do I claim employee expenses?"
# =========================================================================
def test_req_06_employee_expenses(retriever, mock_llm):
    intent, conf, is_proc, rewrite, alts = classify_intent_rules("How do I claim employee expenses?")
    assert intent == "finance"
    assert is_proc is True
    assert "SOP-FIN-002" in rewrite or "expense" in rewrite.lower()
    
    # Verify retrieval against pgvector
    results = retriever.retrieve("How do I claim employee expenses?", top_k=3, intent="finance")
    assert len(results) > 0
    joined = " ".join(results)
    assert "expense" in joined.lower() or "travel" in joined.lower() or "reimbursement" in joined.lower()


# =========================================================================
# REQUIREMENT 7: Question absent from knowledge base
# =========================================================================
def test_req_07_absent_knowledge_base_question(retriever):
    results = retriever.retrieve_results(
        query="What is the secret recipe for chocolate lava cake in the Antarctica cafeteria?",
        top_k=5
    )
    # Cosine distance should be high and similarity low for absent knowledge
    assert all(r.similarity_score < 0.65 for r in results) or len(results) == 0


# =========================================================================
# REQUIREMENT 8: Unauthorized user asking about restricted documents
# =========================================================================
def test_req_08_access_control_restricted_documents(retriever):
    # Restricted document metadata
    restricted_meta = {
        "access_level": "restricted",
        "allowed_departments": ["FIN", "LEGAL"]
    }
    
    # Unauthorized user: Marketing employee
    unauthorized_user = {"role": "Employee", "department": "Marketing"}
    has_access = retriever.check_document_access(restricted_meta, unauthorized_user)
    assert has_access is False, "Unauthorized user must not be granted access to restricted document"
    
    # Authorized user: Finance employee
    authorized_user = {"role": "Employee", "department": "Finance"}
    assert retriever.check_document_access(restricted_meta, authorized_user) is True
    
    # Global admin user
    admin_user = {"role": "Admin", "department": "Management"}
    assert retriever.check_document_access(restricted_meta, admin_user) is True
