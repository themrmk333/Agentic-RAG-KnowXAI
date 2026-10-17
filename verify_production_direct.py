import os
import sys
import httpx
from typing import Dict, Any

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)

from config.settings import get_settings
from agents.graph.workflow import create_workflow

def check_provider():
    settings = get_settings()
    if settings.llm_provider != "local":
        print(f"FAIL: LLM_PROVIDER is {settings.llm_provider}, expected 'local'")
        return False
    if settings.local_llm_model != "llama3.1:8b":
        print(f"FAIL: LOCAL_LLM_MODEL is {settings.local_llm_model}, expected 'llama3.1:8b'")
        return False
    
    try:
        r = httpx.get("http://localhost:11434/api/tags")
        if r.status_code == 200:
            models = [m["name"] for m in r.json().get("models", [])]
            if not ("llama3.1:8b" in models or "llama3.1:latest" in models or "llama3.1" in models):
                 return False
        else:
            return False
    except Exception:
        return False
    return True

from agents.llm.factory import build_provider
from rag.retrieval.pgvector_retriever import PGVectorRetriever

provider = build_provider("local")
retriever = PGVectorRetriever()
app = create_workflow(provider, retriever)

def run_test(query: str, department: str, expected_intent: str, expected_content: str, expect_abstain: bool = False, expected_routing: str = None) -> bool:
    print(f"\n==========================================================")
    print(f"QUERY: '{query}'")
    print(f"USER DEPARTMENT: {department}")
    
    initial_state = {
        "original_query": query,
        "user_context": {"department": department, "role": "Employee"},
        "provider": "local",
        "chat_history": []
    }
    
    final_state = app.invoke(initial_state)
    
    intent = final_state.get("intent", "UNKNOWN")
    agents = final_state.get("plan", [])
    expected_domain = final_state.get("expected_domain", "UNKNOWN")
    docs = final_state.get("context_documents", [])
    
    final_ans = final_state.get("final_answer", {})
    answer = final_ans.get("answer", "")
    grounding = final_ans.get("grounded", False)
    confidence = final_ans.get("confidence", "UNKNOWN")
    provider = final_state.get("provider", "UNKNOWN")
    model = final_state.get("model", "UNKNOWN")
    
    print(f"DETECTED INTENT: {intent}")
    print(f"DETECTED DOMAIN: {expected_domain}")
    print(f"SELECTED AGENT: {agents}")
    print(f"ACCESS CONTEXT: {department}")
    print(f"TOP RETRIEVED DOCS: {len(final_state.get('retrieved_chunks', []))}")
    print(f"FINAL CONTEXT DOCS: {len(docs)}")
    print(f"PROVIDER: {provider}")
    print(f"MODEL: {model}")
    print(f"GROUNDING STATUS: {grounding}")
    print(f"CONFIDENCE: {confidence}")
    print(f"FINAL ANSWER: {answer[:300]}...")
    
    passed = True
    
    if expected_intent and intent != expected_intent:
        print(f"FAIL: Expected intent '{expected_intent}', got '{intent}'")
        passed = False
        
    if expected_routing and not any(expected_routing in a for a in agents):
         print(f"FAIL: Expected agent routing '{expected_routing}', got {agents}")
         passed = False
         
    if expect_abstain:
        if not ("not contain enough information" in answer or "I don't know" in answer or "does not contain" in answer or "I cannot provide" in answer or not grounding):
            print(f"FAIL: Expected abstention, but got grounded answer.")
            passed = False
    else:
        if expected_content and expected_content.lower() not in answer.lower():
            print(f"FAIL: Expected content '{expected_content}' not found in answer.")
            passed = False
            
    if passed:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")
    return passed

def main():
    print("STARTING PRODUCTION VERIFICATION...")
    provider_ok = check_provider()
    
    results = []
    
    r1 = run_test("What is the onboarding process for new hires?", "HR", "hr", "HR Executive")
    results.append(("1. HR Onboarding", r1))
    
    r2 = run_test("How do I reset my IT password?", "HR", "it", "portal", expected_routing="it")
    results.append(("2. IT Password Reset", r2))
    
    r3 = run_test("How do I submit an expense claim?", "HR", "finance", "expense", expected_routing="finance")
    results.append(("3. Finance Expense Claim", r3))
    
    r4 = run_test("What is the sales commission procedure?", "SALES", "sales", "commission", expected_routing="sales")
    results.append(("4. Sales Commission", r4))
    
    r5 = run_test("Hi", "HR", "greeting", "hello", expected_routing="greeting")
    results.append(("5. Greeting", r5))
    
    r6 = run_test("What is the company's policy for employees living on Mars?", "HR", "general", "", expect_abstain=True)
    results.append(("6. Mars policy (Abstain)", r6))
    
    r7 = run_test("Are there any current projects involving cloud migration?", "PROJECT", "project", "", expect_abstain=True)
    results.append(("7. Cloud Migration Projects (Abstain)", r7))

    print("\n================ SUMMARY ================")
    all_passed = all(r[1] for r in results) and provider_ok
    for name, p in results:
        print(f"{name}: {'PASS' if p else 'FAIL'}")
        
    print(f"\nOVERALL: {'PASS' if all_passed else 'FAIL'}")
    
if __name__ == '__main__':
    main()
