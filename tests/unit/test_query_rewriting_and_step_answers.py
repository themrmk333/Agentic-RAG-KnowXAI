"""Comprehensive unit tests for Query Rewriting, Step-by-Step answers, and answer quality policies."""

import pytest
from unittest.mock import MagicMock
from typing import Any, Dict, List

from agents.state import AgentState
from agents.schemas.agent_schema import UnderstoodQuery, AgentPlan, FinalAnswer
from agents.query.understanding import QueryUnderstandingAgent
from agents.planner.planner_agent import PlannerAgent
from agents.it_agent.it_agent import ITAgent
from agents.hr_agent.hr_agent import HRAgent
from agents.finance_agent.finance_agent import FinanceAgent
from agents.project_agent.project_agent import ProjectAgent
from agents.specialists.research.research_agent import ResearchAgent
from agents.specialists.coding.coding_agent import CodingAgent
from agents.specialists.mathematics.mathematics_agent import MathematicsAgent
from agents.specialists.critic.critic_agent import CriticAgent
from agents.specialists.decision.decision_agent import DecisionAgent
from agents.reasoning.reasoning_agent import ReasoningAgent
from agents.aggregator.aggregator_agent import AggregatorAgent
from agents.llm import LLMProvider, LLMResponse
from agents.rag.interface import MockRAGRetriever
from rag.context.context_assembler import ContextAssembler, AssemblerConfig
from rag.retrieval.models import RetrievalResult


class FlexibleMockLLM(LLMProvider):
    """Mock LLM providing custom responses for query understanding, specialists, and aggregator."""

    def __init__(self, chat_response: str = "Mock response", structured_obj: Any = None):
        super().__init__(model="test-mock")
        self.chat_response = chat_response
        self.structured_obj = structured_obj
        self.chat_history: List[Any] = []
        self.structured_history: List[Any] = []

    def generate(self, prompt: str, *, temperature: float = 0.2) -> LLMResponse:
        return LLMResponse(text=self.chat_response)

    def chat(self, messages: Any, *, temperature: float = 0.2) -> LLMResponse:
        self.chat_history.append(messages)
        return LLMResponse(text=self.chat_response)

    def structured(self, messages: Any, response_model: type, *, temperature: float = 0.0) -> Any:
        self.structured_history.append((messages, response_model))
        if self.structured_obj is not None:
            return self.structured_obj

        if response_model == UnderstoodQuery:
            return UnderstoodQuery(
                rephrased_query="How can an employee configure and access the corporate VPN?",
                intent="it",
                key_terms=["VPN", "access", "corporate", "SOP-IT-004"],
                alternative_queries=[
                    "Corporate VPN connection troubleshooting procedure",
                    "VPN authentication and connectivity errors",
                    "Corporate VPN setup and access requirements"
                ],
                is_procedural=True
            )
        elif response_model == AgentPlan:
            return AgentPlan(
                specialists=["it", "critic"],
                justification="Procedural IT support query requires IT specialist and Critic verification."
            )
        elif response_model == FinalAnswer:
            return FinalAnswer(
                answer="""### Corporate VPN Access — Step-by-Step Guide

**Prerequisites & Scope:**
- Active MK-Infinite-AI account and MK-ServiceDesk access.
- Manager approval confirming business need for remote network connectivity.

1. **Verify Prerequisites:** Confirm manager approval and documented remote access justification.
2. **Access Service Portal:** Log in to MK-ServiceDesk using your corporate credentials.
3. **Submit VPN Request:** Navigate to IT Service Catalog and open the 'VPN Access' request form.
4. **Attach Required Information:** Provide Employee ID, department name, and specific access requirements.
5. **System Administrator Review:** The request is reviewed under the principle of least privilege.
6. **Network Provisioning:** Once approved, the IT engineer provisions VPN credentials and endpoint profile.
7. **Client Configuration:** Follow the configuration parameters sent to your registered corporate email.
8. **Connect and Authenticate:** Launch VPN client and authenticate using your MFA credentials.
9. **Verify Connection:** Open internal corporate intranet or services to confirm tunnel status.
10. **Troubleshooting & Policy Closure:** Report any errors in MK-ServiceDesk. Note that credentials expire after 90 days of inactivity; escalate via IT Engineer -> IT Manager -> IT Director (SOP-IT-004).

**Source Documentation:**
- SOP-IT-004: Corporate VPN Access Setup

**Summary & Next Steps:**
Submit your request via MK-ServiceDesk and ensure manager approval is documented.""",
                confidence=0.95,
                references=["SOP-IT-004"],
                errors_encountered=[]
            )
        raise ValueError(f"Unsupported model: {response_model}")


# ==============================================================================
# 1. QUERY REWRITING TESTS
# ==============================================================================

def test_query_rewriting_normal_clear_query():
    """Verify that clear queries are preserved and faceted search queries are generated."""
    mock_retriever = MockRAGRetriever()
    llm = FlexibleMockLLM()
    agent = QueryUnderstandingAgent(llm, mock_retriever)

    state: AgentState = {
        "original_query": "What are the standard annual leave allowances?",
        "conversation_history": [],
    }
    result = agent.execute(state)

    assert result["understood_query"] != ""
    assert len(result["rewritten_queries"]) >= 1
    assert result["intent"] in ["it", "hr", "finance", "general"]


def test_query_rewriting_misspelled_and_informal():
    """Verify informal language, typos, and Hinglish queries are rewritten to clear search queries."""
    mock_retriever = MockRAGRetriever()
    # Mocking UnderstoodQuery for informal Hinglish input
    custom_understood = UnderstoodQuery(
        rephrased_query="How can an employee troubleshoot a corporate VPN connection failure?",
        intent="it",
        key_terms=["VPN", "troubleshoot", "connection failure"],
        alternative_queries=[
            "Corporate VPN connection troubleshooting procedure",
            "VPN authentication and connectivity errors",
            "Corporate VPN setup and access requirements",
            "Relevant VPN troubleshooting SOPs and escalation procedures"
        ],
        is_procedural=True
    )
    llm = FlexibleMockLLM(structured_obj=custom_understood)
    agent = QueryUnderstandingAgent(llm, mock_retriever)

    # Hinglish query: "VPN connect nhi ho raha, kya karu?"
    state: AgentState = {
        "original_query": "VPN connect nhi ho raha, kya karu?",
        "conversation_history": [],
    }
    result = agent.execute(state)

    assert result["understood_query"] == "How can an employee troubleshoot a corporate VPN connection failure?"
    assert len(result["rewritten_queries"]) == 5  # Primary + 4 alternative queries
    assert result["is_procedural"] is True
    assert "VPN authentication and connectivity errors" in result["rewritten_queries"]


def test_query_rewriting_ambiguous_and_conversation_history():
    """Verify follow-up queries like 'Explain step 3' and 'What about urgent access?' use history."""
    mock_retriever = MockRAGRetriever()

    custom_understood = UnderstoodQuery(
        rephrased_query="Detailed instructions and approval requirements for step 3 of corporate VPN access setup",
        intent="it",
        key_terms=["step 3", "VPN", "System Administrator", "SOP-IT-004"],
        alternative_queries=["System Administrator VPN approval requirements"],
        is_procedural=True
    )
    llm = FlexibleMockLLM(structured_obj=custom_understood)
    agent = QueryUnderstandingAgent(llm, mock_retriever)

    history = [
        {"role": "user", "content": "How do I request corporate VPN access?"},
        {"role": "assistant", "content": "Follow SOP-IT-004: 1. Confirm prerequisites, 2. Submit in MK-ServiceDesk, 3. System Administrator review."}
    ]

    state: AgentState = {
        "original_query": "Explain step 3",
        "conversation_history": history,
    }
    result = agent.execute(state)

    # Verify conversation history was sent in the prompt to the LLM
    call_messages = llm.structured_history[0][0]
    user_prompt = call_messages[1]["content"]
    assert "Relevant Conversation History:" in user_prompt
    assert "How do I request corporate VPN access?" in user_prompt
    assert result["understood_query"] == "Detailed instructions and approval requirements for step 3 of corporate VPN access setup"


# ==============================================================================
# 2. STEP-BY-STEP ANSWER QUALITY TESTS (10 USEFUL STEPS)
# ==============================================================================

def test_it_setup_and_troubleshooting_10_step_answer():
    """Verify ITAgent generates a clear, numbered 10-step guide for corporate VPN setup."""
    sop_content = """[Document: SOP-IT-004 | Source: data/sop/IT/SOP-IT-004.md | Chunk: 1]
Document ID: SOP-IT-004 | Corporate VPN Access Setup
Preconditions: Requester has active account and MK-ServiceDesk access with manager approval.
Step 1: Confirm eligibility and prerequisites (manager approval).
Step 2: Raise request in MK-ServiceDesk specifying required VPN Access.
Step 3: System Administrator reviews under least-privilege principles.
Step 4: Assigned engineer provisions VPN Access.
Step 5: Employee is notified and tests functionality.
Step 6: Log any issues in MK-ServiceDesk for correction.
Step 7: MK-ServiceDesk marks Complete; credentials revoked after 90 days inactivity.
Escalation: IT Support Engineer -> IT Manager -> IT Director."""

    mock_llm_response = """### Corporate VPN Access — 10-Step Setup Guide

**Prerequisites & Required Information:**
- Valid employee account and MK-ServiceDesk access.
- Documented manager approval and Employee ID.

1. **Verify Prerequisites:** Ensure you have active manager approval and business need for remote access.
2. **Access Service Portal:** Log in to MK-ServiceDesk portal.
3. **Locate Service Catalog:** Search for 'Corporate VPN Access Setup' (SOP-IT-004).
4. **Complete Request Form:** Provide your Employee ID, department, and business justification.
5. **Supervisor Sign-off:** Confirm your manager has approved the automated ticket notification.
6. **System Administrator Review:** The System Administrator evaluates access under least-privilege rules.
7. **Credential Provisioning:** The IT technical team configures your VPN tunnel profile.
8. **Client Configuration:** Follow the setup instructions sent to your corporate email.
9. **Test Connection:** Connect to the VPN client and verify intranet portal reachability.
10. **Troubleshooting & Inactivity Policy:** If issues arise, report them in MK-ServiceDesk. Note credentials expire after 90 days inactivity; escalate to IT Engineer -> IT Manager -> IT Director.

**Source Documents:** SOP-IT-004 (Corporate VPN Access Setup)
**Next Steps:** Open a ticket in MK-ServiceDesk to begin."""

    llm = FlexibleMockLLM(chat_response=mock_llm_response)
    it_agent = ITAgent(llm)

    state: AgentState = {
        "original_query": "How do I access the corporate VPN?",
        "understood_query": "How can an employee configure and access the corporate VPN?",
        "relevant_context": [sop_content],
        "specialist_results": {},
    }
    res = it_agent.execute(state)
    answer = res["specialist_results"]["it"]

    # Check 10 numbered steps present
    for i in range(1, 11):
        assert f"{i}. **" in answer, f"Step {i} not found in answer"
    assert "SOP-IT-004" in answer
    assert "MK-ServiceDesk" in answer
    assert "Prerequisites" in answer


def test_it_urgent_access_edge_case():
    """Verify urgent/expedited VPN access request explains SOP-IT-004-EDGE-B."""
    edge_b_content = """[Document: SOP-IT-004-EDGE-B | Source: data/sop/IT/edge_cases/SOP-IT-004-EDGE-B.md | Chunk: 1]
Document ID: SOP-IT-004-EDGE-B | Corporate VPN Access Setup — Urgent / Expedited Path
Scenario: Genuine business emergency (production outage, safety, regulatory deadline).
Deviation Procedure:
1. Employee documents business impact of waiting.
2. Employee contacts System Administrator directly (phone/in-person) for verbal pre-approval.
3. On verbal pre-approval, proceed with minimum necessary action, logging all steps.
4. File formal request in MK-ServiceDesk within 24 hours marked 'Emergency — Retroactive Approval'.
5. System Administrator formally reviews and signs off within 2 business days.
6. Escalation to IT Director if emergency justification is insufficient."""

    mock_llm_response = """### Urgent Corporate VPN Access (SOP-IT-004-EDGE-B) — Emergency Procedure

For genuine business emergencies where standard approval delays would cause material harm:

1. **Document Justification:** Record the business impact and why standard timeline cannot be met.
2. **Obtain Verbal Pre-Approval:** Contact System Administrator directly via phone or in-person.
3. **Execute Emergency Access:** Perform minimum necessary action and log every action taken.
4. **File Retroactive Ticket:** Submit ticket in MK-ServiceDesk within 24 hours marked 'Emergency — Retroactive Approval'.
5. **Formal Sign-Off:** System Administrator signs off within 2 business days; escalate to IT Director if disputed.

**Citations:** SOP-IT-004-EDGE-B"""

    llm = FlexibleMockLLM(chat_response=mock_llm_response)
    it_agent = ITAgent(llm)

    state: AgentState = {
        "original_query": "What about urgent VPN access?",
        "understood_query": "Procedure and eligibility criteria for urgent corporate VPN access exceptions (SOP-IT-004-EDGE-B)",
        "relevant_context": [edge_b_content],
        "specialist_results": {},
    }
    res = it_agent.execute(state)
    answer = res["specialist_results"]["it"]

    assert "SOP-IT-004-EDGE-B" in answer
    assert "Verbal" in answer or "verbal" in answer
    assert "24 hours" in answer or "24h" in answer


def test_hr_policy_procedural_and_factual():
    """Verify procedural HR queries give steps while factual queries answer directly."""
    # 1. Procedural query
    procedural_resp = """### Leave Application Workflow — Step-by-Step

1. **Check Balance:** Verify your accrued leave balance in HR portal.
2. **Submit Notice:** Submit leave request 7 days in advance.
3. **Manager Approval:** Await manager approval within 48 hours.
4. **Handover Note:** Share handover notes with team lead.
5. **HR Confirmation:** Receive formal approval email from HR Operations."""

    llm_proc = FlexibleMockLLM(chat_response=procedural_resp)
    hr_agent_proc = HRAgent(llm_proc)
    state_proc: AgentState = {
        "original_query": "How do I apply for annual leave?",
        "understood_query": "Step-by-step process for applying for annual leave",
        "relevant_context": ["[Document: HR-001 | Content: Annual leave submission guidelines]"],
        "specialist_results": {},
    }
    res_proc = hr_agent_proc.execute(state_proc)
    assert "1. **" in res_proc["specialist_results"]["hr"]

    # 2. Simple factual query
    factual_resp = "Employees are entitled to 26 weeks of paid maternity leave as per company policy."
    llm_fact = FlexibleMockLLM(chat_response=factual_resp)
    hr_agent_fact = HRAgent(llm_fact)
    state_fact: AgentState = {
        "original_query": "How many weeks of maternity leave do we get?",
        "understood_query": "Maternity leave duration policy",
        "relevant_context": ["[Document: HR-002 | Content: Maternity leave is 26 weeks.]"],
        "specialist_results": {},
    }
    res_fact = hr_agent_fact.execute(state_fact)
    # Ensure factual query doesn't force fake 10 steps
    assert "10. **" not in res_fact["specialist_results"]["hr"]
    assert "26 weeks" in res_fact["specialist_results"]["hr"]


def test_finance_reimbursement_procedural():
    """Verify FinanceAgent provides structured steps for expense reimbursement."""
    finance_resp = """### Corporate Expense Reimbursement Procedure

1. **Eligibility Check:** Ensure expenses comply with travel and meal allowance caps.
2. **Collect Invoices:** Retain all itemized GST invoices and receipts.
3. **Portal Access:** Log into Finance ERP portal.
4. **Create Expense Claim:** Select 'Travel & Entertainment' category.
5. **Upload Receipts:** Attach digitized receipts for all claims above $25.
6. **Submit to Manager:** Forward to reporting manager for authorization.
7. **Manager Sign-off:** Manager reviews within 3 business days.
8. **Finance Audit:** Finance team audits invoices for compliance.
9. **Payment Processing:** Approved claims are batched for next pay cycle.
10. **Payout Verification:** Verify deposit on payroll slip; report discrepancies to Finance Support."""

    llm = FlexibleMockLLM(chat_response=finance_resp)
    finance_agent = FinanceAgent(llm)
    state: AgentState = {
        "original_query": "How do I submit my travel expenses?",
        "understood_query": "Step-by-step procedure for employee travel expense reimbursement",
        "relevant_context": ["[Document: FIN-003 | Content: Travel expense guidelines]"],
        "specialist_results": {},
    }
    res = finance_agent.execute(state)
    assert "1. **" in res["specialist_results"]["finance"]
    assert "10. **" in res["specialist_results"]["finance"]


def test_project_procedure_workflow():
    """Verify ProjectAgent provides step-by-step guidance for project documentation."""
    project_resp = """### Project Creation & Milestone Sign-off Workflow

1. **Project Charter:** Complete the initial Project Initiation Document (PID).
2. **Stakeholder Alignment:** Review deliverables with project sponsor.
3. **Repository Setup:** Provision Jira board and Git repository.
4. **Sprint Cadence:** Establish 2-week sprint backlog.
5. **Milestone Review:** Conduct phase-gate review with technical lead."""

    llm = FlexibleMockLLM(chat_response=project_resp)
    project_agent = ProjectAgent(llm)
    state: AgentState = {
        "original_query": "What is the procedure for new project initiation?",
        "understood_query": "Procedure for initiating a new technical project",
        "relevant_context": ["[Document: SOP-PRJ-001 | Content: Project Initiation SOP]"],
        "specialist_results": {},
    }
    res = project_agent.execute(state)
    assert "1. **" in res["specialist_results"]["project"]


def test_coding_and_mathematics_agents():
    """Verify CodingAgent provides structured steps with code and MathAgent gives step derivations."""
    # Coding test
    coding_resp = """### FastAPI Health Endpoint Setup

1. **Install Dependencies:** `pip install fastapi uvicorn`
2. **Define App:** Instantiate FastAPI app.
3. **Create Route:**
```python
@app.get("/health")
def health():
    return {"status": "ok"}
```
4. **Test Endpoint:** Run `uvicorn main:app --reload` and query `/health`."""

    llm_code = FlexibleMockLLM(chat_response=coding_resp)
    coding_agent = CodingAgent(llm_code)
    state_code: AgentState = {
        "original_query": "How to create a health check endpoint in FastAPI?",
        "understood_query": "How to create a health check endpoint in FastAPI",
        "relevant_context": [],
        "specialist_results": {},
    }
    res_code = coding_agent.execute(state_code)
    assert "```python" in res_code["specialist_results"]["coding"]

    # Mathematics test
    math_resp = """### Compound Interest Calculation — Step-by-Step

1. **Identify Formula:** A = P(1 + r/n)^(nt)
2. **Substitute Variables:** P=1000, r=0.05, n=1, t=2
3. **Compute Intermediate:** (1 + 0.05) = 1.05
4. **Exponentiate:** 1.05^2 = 1.1025
5. **Final Result:** A = 1000 * 1.1025 = $1,102.50"""

    llm_math = FlexibleMockLLM(chat_response=math_resp)
    math_agent = MathematicsAgent(llm_math)
    state_math: AgentState = {
        "original_query": "Calculate compound interest for $1000 at 5% for 2 years",
        "understood_query": "Calculate compound interest for $1000 at 5% for 2 years",
        "relevant_context": [],
        "specialist_results": {},
    }
    res_math = math_agent.execute(state_math)
    assert "$1,102.50" in res_math["specialist_results"]["mathematics"]


# ==============================================================================
# 3. EDGE CASES & RETRIEVAL INTEGRITY TESTS
# ==============================================================================

def test_no_relevant_documents_acknowledged():
    """Verify agent acknowledges missing information honestly without hallucinating."""
    no_info_resp = "The available company knowledge base does not contain information regarding extraterrestrial travel policies."
    llm = FlexibleMockLLM(chat_response=no_info_resp)
    research_agent = ResearchAgent(llm)

    state: AgentState = {
        "original_query": "What is the policy for space shuttle travel?",
        "understood_query": "Company space shuttle travel policy",
        "relevant_context": [],
        "specialist_results": {},
    }
    res = research_agent.execute(state)
    assert "not contain" in res["specialist_results"]["research"].lower()


def test_conflicting_source_documents_handled():
    """Verify Critic and Decision agents flag conflicting documents."""
    critic_resp = """CRITIQUE & VALIDATION SUMMARY:
- Warning: Conflict detected between Policy 2024 (20 days leave) and Policy 2026 (25 days leave).
- Grounding: Policy 2026 is the superseding active revision."""

    llm = FlexibleMockLLM(chat_response=critic_resp)
    critic_agent = CriticAgent(llm)

    state: AgentState = {
        "original_query": "How many days leave do I get?",
        "understood_query": "Annual leave entitlement",
        "relevant_context": [
            "[Document: Policy-2024 | Leave: 20 days]",
            "[Document: Policy-2026 | Leave: 25 days]"
        ],
        "specialist_results": {"hr": "Employees get 20 or 25 days."},
    }
    res = critic_agent.execute(state)
    assert "Conflict" in res["specialist_results"]["critic"] or "conflict" in res["specialist_results"]["critic"]


def test_long_procedure_multi_chunk_preservation():
    """Verify ContextAssembler preserves multiple chunks from the same document in natural order."""
    assembler = ContextAssembler(config=AssemblerConfig(max_chunks_per_document=6, max_context_items=10))

    # Simulate 5 chunks belonging to the same document in scrambled arrival order
    candidates = [
        RetrievalResult(
            chunk_id="chunk_3",
            document_id=101,
            chunk_index=3,
            content="Step 7-8: Verification and signoff.",
            distance=0.15,
            similarity_score=0.85,
            document_title="Corporate VPN SOP",
            source_path="/docs/vpn.md",
            content_type="text/markdown",
            metadata={"title": "Corporate VPN SOP"}
        ),
        RetrievalResult(
            chunk_id="chunk_1",
            document_id=101,
            chunk_index=1,
            content="Preconditions: Manager approval required.",
            distance=0.10,
            similarity_score=0.90,
            document_title="Corporate VPN SOP",
            source_path="/docs/vpn.md",
            content_type="text/markdown",
            metadata={"title": "Corporate VPN SOP"}
        ),
        RetrievalResult(
            chunk_id="chunk_2",
            document_id=101,
            chunk_index=2,
            content="Step 1-6: Submit ticket in MK-ServiceDesk.",
            distance=0.12,
            similarity_score=0.88,
            document_title="Corporate VPN SOP",
            source_path="/docs/vpn.md",
            content_type="text/markdown",
            metadata={"title": "Corporate VPN SOP"}
        ),
    ]

    assembled = assembler.assemble(query="corporate VPN access procedure", candidates=candidates)

    # Verify all 3 chunks preserved (not filtered by diversity limit)
    assert len(assembled.items) == 3

    # Verify chunks are sorted by chunk_index in ascending procedural order!
    indices = [item.chunk_index for item in assembled.items]
    assert indices == [1, 2, 3], f"Expected chronological [1, 2, 3], got {indices}"


def test_aggregator_retains_steps_without_shortening():
    """Verify Aggregator preserves complete step-by-step guidance and document references."""
    llm = FlexibleMockLLM()  # returns FinalAnswer with 10 steps
    aggregator = AggregatorAgent(llm)

    state: AgentState = {
        "original_query": "How do I access the corporate VPN?",
        "reasoning": "Synthesized 10 steps for VPN access setup under SOP-IT-004.",
        "relevant_context": ["[Document: SOP-IT-004 | Source: /docs/vpn.md | Content: VPN Setup]"],
        "errors": [],
    }

    result = aggregator.execute(state)
    final_ans = result["final_answer"]

    assert "### Corporate VPN Access — Step-by-Step Guide" in final_ans["answer"]
    # Verify steps are present
    assert "1. **" in final_ans["answer"]
    assert "10. **" in final_ans["answer"]
    assert "SOP-IT-004" in final_ans["references"]
