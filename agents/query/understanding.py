"""Query Understanding Agent implementation."""

import re
import time
from typing import Any, Dict, List, Optional, Tuple
from agents.llm import LLMProvider
from agents.rag import RAGRetriever
from agents.schemas.agent_schema import UnderstoodQuery
from agents.state import AgentState

# Domain regex patterns covering misspellings, technical synonyms, and conversational queries
_IT_PATTERNS = [
    r"\bvpn\b", r"\bvnp\b", r"\bvpnn\b", r"\bwi-?fi\b", r"\bwlan\b", r"\blan\b",
    r"\bnetwork\b", r"\binternet\b", r"\bethernet\b", r"\bpassword\b", r"\bpasscode\b",
    r"\bpasword\b", r"\bpassowrd\b", r"\blogin\b", r"\bcredential(s)?\b", r"\blaptop\b",
    r"\bprinter\b", r"\bmonitor\b", r"\bhardware\b", r"\bsoftware\b", r"\bmk-servicedesk\b",
    r"\bservicedesk\b", r"\bservice\s+desk\b", r"\bticket(s)?\b", r"\btroubleshoot\b",
    r"\btroubleshooting\b", r"\bip\s+address\b", r"\bssh\b", r"\brdp\b", r"\bfirewall\b",
    r"\bantivirus\b", r"\bdriver(s)?\b", r"\bit\s+support\b", r"\bsystem\s+administrator\b",
    r"\bsop-it-\d+\b", r"\btsg\d?-sec-\d+\b"
]

_HR_PATTERNS = [
    r"\bleave\b", r"\bannual\s+leave\b", r"\bsick\s+leave\b", r"\bcasual\s+leave\b",
    r"\bmaternity\b", r"\bpaternity\b", r"\bbereavement\b", r"\bpaid\s+time\s+off\b",
    r"\bpto\b", r"\bholiday(s)?\b", r"\bonboarding\b", r"\boffboarding\b", r"\bresignation\b",
    r"\bhandbook\b", r"\battendance\b", r"\bwork\s+hours\b", r"\bbenefit(s)?\b",
    r"\bmedical\s+insurance\b", r"\bhealth\s+insurance\b", r"\bpol-hr-\d+\b", r"\bhr\s+policy\b"
]

_FINANCE_PATTERNS = [
    r"\bexpense(s)?\b", r"\bclaim(s)?\b", r"\breimbursement(s)?\b", r"\btravel\s+allowance\b",
    r"\bper-?diem\b", r"\bsalary\b", r"\bpayroll\b", r"\binvoice(s)?\b", r"\bbilling\b",
    r"\breceipt(s)?\b", r"\bcredit\s+card\b", r"\bmk-finance360\b", r"\bfinance\s+policy\b",
    r"\bsop-fin-\d+\b", r"\bpol-fin-\d+\b"
]

_PROJECT_PATTERNS = [
    r"\bproject\s+creation\b", r"\bmilestone(s)?\b", r"\bsprint(s)?\b", r"\bdeliverable(s)?\b",
    r"\bproject\s+tracking\b", r"\bsop-sop-\d+\b", r"\bproject\s+sop\b", r"\bproject\s+delay(s)?\b"
]

_PROCEDURAL_PATTERNS = [
    r"\bhow\s+to\b", r"\bhow\s+do\s+i\b", r"\bhow\s+can\s+i\b", r"\bstep(s)?\b",
    r"\bguide\b", r"\bsetup\b", r"\bset\s+up\b", r"\bconnect\b", r"\bturn\s+on\b",
    r"\bon\s+vpn\b", r"\bfix\b", r"\bprocedure\b", r"\binstructions?\b",
    r"\bunable\s+to\b", r"\bcannot\b", r"\bcan't\b", r"\bprocess\b",
    r"\bclaim\b", r"\brequest\b"
]


def classify_intent_rules(
    query: str,
    history: Optional[List[Dict[str, str]]] = None,
) -> Tuple[str, float, bool, str, List[str]]:
    """Deterministic domain classifier and search rewriter based on technical keywords and history.

    Returns:
        (intent, confidence, is_procedural, primary_rewrite, alternative_rewrites)
    """
    q_low = query.lower().strip()

    is_proc = any(bool(re.search(pat, q_low)) for pat in _PROCEDURAL_PATTERNS)

    # 1. Check direct query match for IT
    if any(bool(re.search(pat, q_low)) for pat in _IT_PATTERNS):
        if "vpn" in q_low or "vnp" in q_low:
            if "urgent" in q_low or "emergency" in q_low or "expedite" in q_low:
                primary_rewrite = "Urgent and expedited corporate VPN access request procedure and approvals"
                alts = [
                    "Emergency verbal pre-approval for corporate VPN access",
                    "Retroactive approval and escalation path for expedited corporate VPN access",
                ]
            elif "unable" in q_low or "cannot" in q_low or "fix" in q_low or "issue" in q_low or "troubleshoot" in q_low:
                primary_rewrite = "How to troubleshoot corporate VPN connection failure and step-by-step setup procedure"
                alts = [
                    "Corporate VPN connection troubleshooting prerequisites and error fixes",
                    "Corporate VPN access setup and IT helpdesk request process",
                ]
            else:
                primary_rewrite = "How can an employee set up and connect to the corporate VPN step-by-step"
                alts = [
                    "Corporate VPN access setup prerequisites and request procedure",
                    "Corporate VPN connection verification, inactivity rules, and escalation path",
                ]
        elif "password" in q_low or "passcode" in q_low or "reset" in q_low:
            primary_rewrite = "How can an employee reset a forgotten password or unlock their account"
            alts = [
                "Self-service password reset procedure and account recovery",
                "IT service desk password assistance and security requirements",
            ]
        elif "software" in q_low or "catalogue" in q_low or "license" in q_low:
            primary_rewrite = "How should an employee request new software or application licenses"
            alts = [
                "Software catalogue request and manager approval workflow",
                "Standard approved corporate software installation procedure",
            ]
        elif "lost" in q_low or "stolen" in q_low or "repair" in q_low or "replace" in q_low:
            primary_rewrite = "What should an employee do if their laptop is lost, stolen, or needs repair"
            alts = [
                "Lost device reporting within 1 hour and security protocol",
                "Laptop repair, replacement, and asset register wipe procedure",
            ]
        elif "mfa" in q_low or "multi-factor" in q_low or "authenticator" in q_low:
            primary_rewrite = "How does an employee set up multi-factor authentication (MFA)"
            alts = [
                "MFA registration with authenticator app and backup verification",
                "Re-registering MFA on a new mobile device or phone number",
            ]
        elif "phishing" in q_low or "suspicious" in q_low or "incident" in q_low:
            primary_rewrite = "What should an employee do after receiving a suspicious email or phishing message"
            alts = [
                "Reporting phishing emails to security team",
                "Security incident escalation and device isolation steps",
            ]
        else:
            primary_rewrite = f"IT Department technical support procedure: {query}"
            alts = [
                "Information Technology support ticket prioritisation and resolution",
                "Corporate IT guidelines and service request workflows",
            ]
        return "it", 0.92, True if is_proc or "vpn" in q_low else False, primary_rewrite, alts

    # 2. Check direct query match for HR
    if any(bool(re.search(pat, q_low)) for pat in _HR_PATTERNS):
        if "onboarding" in q_low or "new employee" in q_low or "joining" in q_low or "first week" in q_low:
            primary_rewrite = "What is the onboarding process for a new employee at MK-Infinite-AI"
            alts = [
                "New employee first week induction, laptop setup, and InfinityHR registration",
                "HR onboarding checklist, background verification, and 30-day review",
            ]
        elif "performance" in q_low or "review" in q_low or "appraisal" in q_low:
            primary_rewrite = "How does the annual performance review cycle and evaluation work"
            alts = [
                "Performance appraisal goals, mid-year check-in, and final rating",
                "InfinityHR performance management cycle April to March",
            ]
        elif "resignation" in q_low or "resign" in q_low or "exit" in q_low or "notice period" in q_low:
            primary_rewrite = "What happens when an employee resigns or leaves the company"
            alts = [
                "Notice period rules, knowledge handover plan, and exit interview",
                "Full and final settlement, asset handover, and relieving letter process",
            ]
        else:
            primary_rewrite = "MK-Infinite-AI employee leave policy rules, annual leave entitlements, and application procedure"
            alts = [
                "Paid Annual Leave carry forward and approval rules in InfinityHR",
                "Sick leave, casual leave, and medical certificate requirements",
            ]
        return "hr", 0.93, is_proc, primary_rewrite, alts

    # 3. Check direct query match for Finance
    if any(bool(re.search(pat, q_low)) for pat in _FINANCE_PATTERNS):
        if "payroll" in q_low or "salary" in q_low:
            primary_rewrite = "Employee monthly payroll processing schedule and salary payment date"
            alts = [
                "Salary slip generation and bank account verification in InfinityHR",
                "Finance department payroll cut-off dates and tax deductions",
            ]
        else:
            primary_rewrite = "Employee travel expense reimbursement claim submission procedure in SpendWise"
            alts = [
                "Expense claim submission guidelines and receipt requirements",
                "Finance lead approval process and per-diem policy for expense reimbursement",
            ]
        return "finance", 0.93, is_proc or ("claim" in q_low or "expense" in q_low), primary_rewrite, alts

    # 4. Check direct query match for Project
    if any(bool(re.search(pat, q_low)) for pat in _PROJECT_PATTERNS) or "knowxai" in q_low or "prj-" in q_low:
        if "knowxai" in q_low or "rag" in q_low:
            primary_rewrite = "Project 01 Agentic RAG KnowXAI objectives, architecture, and technology stack"
            alts = [
                "Agentic RAG KnowXAI features, vector database, and LangGraph workflow",
                "KnowXAI development phases, milestones, and testing approach",
            ]
        else:
            primary_rewrite = "Company project creation procedure, milestones, and tracking guidelines"
            alts = [
                "Project initiation, PMO charter, and documentation procedure",
                "Project milestone delivery and ProjectHub tracking guidelines",
            ]
        return "project", 0.91, is_proc, primary_rewrite, alts

    # 5. Check conversation history for follow-up disambiguation
    if history:
        history_text = " ".join([turn.get("content", "").lower() for turn in history[-4:]])
        if any(bool(re.search(pat, history_text)) for pat in _IT_PATTERNS):
            return "it", 0.88, is_proc, f"Corporate VPN and IT support follow-up: {query}", [
                "Corporate VPN access setup SOP-IT-004 follow-up instructions",
                "MK-ServiceDesk IT support procedure and escalation",
            ]
        if any(bool(re.search(pat, history_text)) for pat in _HR_PATTERNS):
            return "hr", 0.88, is_proc, f"Human resources leave policy follow-up: {query}", [
                "Leave policy rules and entitlements POL-HR-001 follow-up",
            ]
        if any(bool(re.search(pat, history_text)) for pat in _FINANCE_PATTERNS):
            return "finance", 0.88, is_proc, f"Expense reimbursement claim follow-up: {query}", [
                "Expense claim and reimbursement procedure SOP-FIN-002 follow-up",
            ]

    # Default general intent
    return "general", 0.50, is_proc, query, []


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
                "rewritten_queries": [],
                "is_procedural": False,
            }

        # Fast-path for greetings
        greetings = {"hi", "hello", "hey", "good morning", "good afternoon", "good evening", "thanks", "thank you"}
        if query.lower().strip() in greetings:
            return {
                "understood_query": query,
                "intent": "general",
                "relevant_context": [],
                "rewritten_queries": [query],
                "is_procedural": False,
                "metadata": {
                    **(state.get("metadata") or {}),
                    "retrieved_count": 0,
                    "authorized_count": 0,
                    "intent_confidence": 0.95,
                },
            }

        conversation_history = state.get("conversation_history") or []
        history_str = ""
        if conversation_history:
            turns = []
            for h in conversation_history[-6:]:
                role = "User" if h.get("role") == "user" else "Assistant"
                turns.append(f"{role}: {h.get('content', '')}")
            history_str = "\nRelevant Conversation History:\n" + "\n".join(turns) + "\n"

        # Apply deterministic rule-based analysis
        rule_intent, rule_conf, rule_proc, rule_rewrite, rule_alts = classify_intent_rules(
            query=query,
            history=conversation_history,
        )

        system_instruction = (
            "You are an expert Query Understanding and Query Rewriting Agent for an Enterprise Knowledge Assistant.\n\n"
            "QUERY REWRITING DIRECTIVES:\n"
            "1. Correct obvious spelling and grammatical mistakes without changing user intent.\n"
            "2. Understand informal language, abbreviations, conversational queries, and Romanized/Hinglish phrasing.\n"
            "   Example: 'how to on VPN' / 'how to on vpn' -> 'How to set up, configure, and connect to corporate VPN access (SOP-IT-004)'\n"
            "   Example: 'VPN connect nhi ho raha, kya karu?' -> 'How can an employee troubleshoot a corporate VPN connection failure?'\n"
            "3. Identify the user's actual underlying information need.\n"
            "4. Expand ambiguous queries and follow-ups using relevant conversation history when provided.\n"
            "   Example: If history discusses VPN access, rewrite 'Explain step 3' to 'Detailed instructions and requirements for step 3 of corporate VPN access setup';\n"
            "   'What about urgent access?' -> 'Procedure and eligibility criteria for urgent or expedited corporate VPN access (SOP-IT-004-EDGE-B)'.\n"
            "5. Strictly preserve all technical terms, error codes, SOP IDs (e.g., SOP-IT-004, SOP-IT-004-EDGE-B), tool names (e.g., MK-ServiceDesk), dates, and numbers.\n"
            "6. Generate 2 to 4 distinct, faceted alternative search queries covering specific angles: requirements, troubleshooting, setup procedures, and policy exceptions.\n"
            "7. Identify whether the user inquiry is procedural (asking for steps, instructions, how-to, setup, or troubleshooting).\n"
            "8. Avoid unnecessary rewriting or distortion if the query is already clear and specific.\n\n"
            "Intent Classification Guidelines:\n"
            "- 'it': Hardware/software issues, credentials, passwords, network, Wi-Fi, internet, printer, VPN, corporate VPN setup, connection troubleshooting, MK-ServiceDesk, corporate cybersecurity policies, or IT support tickets. Questions about connecting or turning on VPN MUST be classified as 'it'.\n"
            "- 'hr': Human Resources topics including leave policy, attendance, maternity/parental leave, onboarding, offboarding, recruitment, employee benefits, handbook, holidays, and employee relations.\n"
            "- 'finance': Questions about salary, payroll, claims, expenses, reimbursement, payment, billing, invoice, travel reimbursement limit, financial claims, and finance policies. Queries containing terms like 'expense', 'reimbursement', or 'claims' MUST be classified as 'finance', NOT 'hr'.\n"
            "- 'project': Project-specific creation, milestones, project documentation, project tracking, and project delays.\n"
            "- 'management': Company-wide initiatives, approval authority, executive decisions, organizational policies, management escalation, and strategic priorities.\n"
            "- 'sales': Sales procedures, commission, client onboarding, sales CRM, or sales processes.\n"
            "- 'coding': Code development, debugging, syntax, or software engineering questions.\n"
            "- 'mathematics': Math calculations, equations, derivations, or statistical analysis.\n"
            "- 'research': Multi-document synthesis or general information research.\n"
            "- 'greeting': Greetings, pleasantries, or simple conversational hello.\n"
            "- 'general': Casual chat or general assistance that doesn't fit other categories."
        )

        user_content = f"User Query: {query}{history_str}"
        messages = [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_content},
        ]

        t_qu_start = time.perf_counter()
        try:
            understood_data: UnderstoodQuery = self.llm.structured(
                messages=messages,
                response_model=UnderstoodQuery,
                temperature=0.0,
            )
            t_llm = (time.perf_counter() - t_qu_start) * 1000.0

            # Intent reconciliation: Ensure strong domain keywords override false general classifications
            final_intent = understood_data.intent.lower().strip()
            if final_intent == "general" and rule_intent != "general":
                final_intent = rule_intent

            is_procedural_final = getattr(understood_data, "is_procedural", False) or rule_proc

            search_query = understood_data.rephrased_query or query
            if (not search_query or search_query.strip() == query) and rule_rewrite:
                search_query = rule_rewrite

            alternative_queries = getattr(understood_data, "alternative_queries", []) or []
            if not alternative_queries and rule_alts:
                alternative_queries = rule_alts

            user_context = state.get("user_context")
            stats = {}
            t_ret_start = time.perf_counter()

            if final_intent == "general":
                retrieved = []
                stats["retrieved_count"] = 0
                stats["authorized_count"] = 0
            else:
                # Multi-query retrieval: Combine primary rewritten query with top alternative queries
                queries_to_retrieve = [search_query]
                for alt in alternative_queries:
                    alt_clean = alt.strip()
                    if alt_clean and alt_clean.lower() != search_query.lower() and alt_clean not in queries_to_retrieve:
                        queries_to_retrieve.append(alt_clean)

                # Limit to 3 query variations to avoid excessive DB latency
                queries_to_retrieve = queries_to_retrieve[:3]

                retrieval_k = 8 if is_procedural_final else 5
                merged_context = []
                seen_chunk_signatures = set()

                for q in queries_to_retrieve:
                    chunks = self.retriever.retrieve(
                        query=q,
                        top_k=retrieval_k,
                        user_context=user_context,
                        stats=stats,
                        intent=final_intent,
                    )
                    for chunk_str in chunks:
                        header_sig = chunk_str.split("\n", 1)[0].strip() if "\n" in chunk_str else chunk_str[:80].strip()
                        if header_sig not in seen_chunk_signatures:
                            seen_chunk_signatures.add(header_sig)
                            merged_context.append(chunk_str)

                    target_limit = 10 if is_procedural_final else 6
                    if len(merged_context) >= target_limit:
                        break

                retrieved = merged_context

            t_ret = (time.perf_counter() - t_ret_start) * 1000.0

            rewritten_list = [search_query]
            if alternative_queries:
                rewritten_list.extend(alternative_queries)

            # Compute justified confidence score
            confidence_score = 0.94 if final_intent == rule_intent else 0.88

            return {
                "understood_query": search_query,
                "intent": final_intent,
                "relevant_context": retrieved,
                "rewritten_queries": rewritten_list,
                "is_procedural": is_procedural_final,
                "metadata": {
                    **(state.get("metadata") or {}),
                    "retrieved_count": len(retrieved),
                    "authorized_count": stats.get("authorized_count", len(retrieved)),
                    "intent_confidence": confidence_score,
                    "timing_query_understanding_ms": round(t_llm, 1),
                    "timing_retrieval_ms": round(t_ret, 1),
                },
            }
        except Exception as e:
            # Deterministic domain fallback prevents dropping to general on network or LLM errors
            t_fallback_start = time.perf_counter()
            user_context = state.get("user_context")
            stats = {}

            fallback_intent = rule_intent
            fallback_search_query = rule_rewrite if rule_rewrite else query
            fallback_alts = rule_alts

            fallback_retrieved = []
            if fallback_intent != "general":
                try:
                    fallback_retrieved = self.retriever.retrieve(
                        query=fallback_search_query,
                        top_k=8 if rule_proc else 5,
                        user_context=user_context,
                        stats=stats,
                        intent=fallback_intent,
                    )
                except Exception as ret_err:
                    state_errors = state.get("errors") or []
                    state_errors.append(f"Retrieval error: {str(ret_err)}")
            else:
                stats["retrieved_count"] = 0
                stats["authorized_count"] = 0

            t_fallback = (time.perf_counter() - t_fallback_start) * 1000.0

            rewritten_list = [fallback_search_query]
            if fallback_alts:
                rewritten_list.extend(fallback_alts)

            return {
                "errors": [f"Query understanding LLM warning: {str(e)}"],
                "understood_query": fallback_search_query,
                "intent": fallback_intent,
                "relevant_context": fallback_retrieved,
                "rewritten_queries": rewritten_list,
                "is_procedural": rule_proc,
                "metadata": {
                    **(state.get("metadata") or {}),
                    "retrieved_count": stats.get("retrieved_count", len(fallback_retrieved)),
                    "authorized_count": stats.get("authorized_count", len(fallback_retrieved)),
                    "intent_confidence": rule_conf,
                    "timing_query_understanding_ms": round(t_fallback, 1),
                    "timing_retrieval_ms": round(t_fallback, 1),
                },
            }

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
