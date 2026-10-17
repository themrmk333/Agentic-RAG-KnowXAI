import os
import sys
import httpx

# Ensure project root is in python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from config.settings import get_settings
from fastapi.testclient import TestClient
from api.main import app
from api.routes.rag import get_optional_user_context

def check_provider():
    settings = get_settings()
    if settings.llm_provider != "local":
        print(f"FAIL: LLM_PROVIDER is {settings.llm_provider}, expected 'local'")
        return False
    if settings.local_llm_model != "llama3.1:8b":
        print(f"FAIL: LOCAL_LLM_MODEL is {settings.local_llm_model}, expected 'llama3.1:8b'")
        return False
    print("PASS: Provider config is LOCAL with llama3.1:8b")
    
    try:
        r = httpx.get("http://localhost:11434/api/tags")
        if r.status_code == 200:
            print("PASS: Ollama endpoint is UP")
            models = [m["name"] for m in r.json().get("models", [])]
            if "llama3.1:8b" in models or "llama3.1:latest" in models or "llama3.1" in models:
                 print("PASS: Llama 3.1 model found in Ollama")
            else:
                 print(f"WARNING: llama3.1 model not found in Ollama tags: {models}")
        else:
            print(f"FAIL: Ollama endpoint returned {r.status_code}")
    except Exception as e:
        print(f"FAIL: Could not reach Ollama at localhost:11434: {e}")
        return False
    return True

client = TestClient(app)

def run_query(query: str, department: str, expected_intent: str, expected_content: str, expect_abstain: bool = False, expected_routing: str = None) -> bool:
    print(f"\n==========================================================")
    print(f"QUERY: '{query}'")
    print(f"USER DEPARTMENT: {department}")
    
    # Mock authentication context
    app.dependency_overrides[get_optional_user_context] = lambda: {"department": department, "role": "Employee"}
    
    payload = {
        "query": query,
        "provider": "local"
    }
    
    response = client.post("/api/v1/rag/query", json=payload)
    app.dependency_overrides.clear()
    
    if response.status_code != 200:
        print(f"FAIL: HTTP {response.status_code} - {response.text}")
        return False
        
    data = response.json()
    metadata = data.get("metadata", {})
    answer = data.get("answer", "")
    
    intent = metadata.get("intent", "UNKNOWN")
    agents = metadata.get("plan", [])
    grounding = metadata.get("grounding_status", "UNKNOWN")
    docs = metadata.get("sources", [])
    
    print(f"DETECTED INTENT: {intent}")
    print(f"SELECTED AGENTS: {agents}")
    print(f"GROUNDING STATUS: {grounding}")
    print(f"TOP DOCS: {docs}")
    print(f"ANSWER: {answer[:200]}...")
    
    passed = True
    
    if expected_intent and intent != expected_intent:
        print(f"FAIL: Expected intent '{expected_intent}', got '{intent}'")
        passed = False
        
    if expected_routing and not any(expected_routing in a for a in agents):
         print(f"FAIL: Expected agent routing '{expected_routing}', got {agents}")
         passed = False
         
    if expect_abstain:
        if not ("not contain enough information" in answer or "I don't know" in answer or "does not contain" in answer or "I cannot provide" in answer):
            print(f"FAIL: Expected abstention, but got answer.")
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
    
    r1 = run_query("What is the onboarding process for new hires?", "HR", "hr", "HR Executive")
    results.append(("1. HR Onboarding", r1))
    
    r2 = run_query("How do I reset my IT password?", "HR", "it", "portal", expected_routing="it")
    results.append(("2. IT Password Reset", r2))
    
    r3 = run_query("How do I submit an expense claim?", "HR", "finance", "receipt", expected_routing="finance")
    results.append(("3. Finance Expense Claim", r3))
    
    r4 = run_query("What is the sales commission procedure?", "SALES", "sales", "commission", expected_routing="sales")
    results.append(("4. Sales Commission", r4))
    
    r5 = run_query("Hi", "HR", "greeting", "hello", expected_routing="greeting")
    results.append(("5. Greeting", r5))
    
    r6 = run_query("What is the company's policy for employees living on Mars?", "HR", "general", "", expect_abstain=True)
    results.append(("6. Mars policy (Abstain)", r6))
    
    r7 = run_query("Are there any current projects involving cloud migration?", "PROJECT", "project", "", expect_abstain=True)
    results.append(("7. Cloud Migration Projects (Abstain)", r7))

    print("\n================ SUMMARY ================")
    all_passed = all(r[1] for r in results) and provider_ok
    for name, p in results:
        print(f"{name}: {'PASS' if p else 'FAIL'}")
        
    print(f"\nOVERALL: {'PASS' if all_passed else 'FAIL'}")
    
if __name__ == '__main__':
    main()
