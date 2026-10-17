import os
import sys
import json
import io
from unittest.mock import patch
from typing import Any, Dict, List

# Ensure project root is in python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from config.settings import get_settings
from agents.llm.factory import build_provider
from rag.embeddings.factory import build_embedding_service
from rag.retrieval.pgvector_retriever import PGVectorRetriever
from agents.graph.workflow import create_workflow

def trace_query(query: str, user_dept: str):
    print("=" * 80)
    print(f"DIAGNOSTIC TRACE FOR QUERY: {query}")
    print("=" * 80)
    
    print("\n--- STAGE 1 — RAW QUERY ---")
    print(f"QUERY: {query}")
    print(f"USER DEPARTMENT: {user_dept}")
    print(f"USER ROLE: Employee")
    
    # We will monkey patch or trace methods
    
    # STAGE 2: Query Understanding
    original_qu_execute = None
    
    # Initialize components
    settings = get_settings()
    llm = build_provider(settings.llm_provider)
    embedding_service = build_embedding_service()
    from database.vector_store import PGVectorStore
    vector_store = PGVectorStore()
    retriever = PGVectorRetriever(embedding_service, vector_store)
    
    workflow = create_workflow(llm, retriever)
    
    initial_state = {
        "original_query": query,
        "errors": [],
        "specialist_results": {},
        "user_context": {
            "id": 1,
            "email": "test@example.com",
            "username": "testuser",
            "role": "Employee",
            "department": user_dept,
        }
    }
    
    # Hook into llm.structured to see Stage 2 and Stage 3
    original_structured = llm.structured
    
    def mock_structured(*args, **kwargs):
        response_model = kwargs.get("response_model")
        result = original_structured(*args, **kwargs)
        
        if response_model.__name__ == "UnderstoodQuery":
            print("\n--- STAGE 2 — QUERY UNDERSTANDING ---")
            print(f"intent: {result.intent}")
            print(f"confidence: {getattr(result, 'confidence', 'N/A')}")
            print(f"entities: {getattr(result, 'entities', 'N/A')}")
            print(f"keywords: {getattr(result, 'keywords', 'N/A')}")
            print(f"department: {getattr(result, 'department', 'N/A')}")
        
        elif response_model.__name__ == "AgentPlan":
            print("\n--- STAGE 3 — AGENT SELECTION ---")
            print(f"selected_agents: {result.specialists}")
            print(f"routing_reason: {result.justification}")
            print(f"routing_confidence: {getattr(result, 'confidence', 'N/A')}")
            
        return result
    
    llm.structured = mock_structured
    
    # Hook into embedding to see Stage 4
    original_embed_query = embedding_service.embed_query
    def mock_embed_query(text):
        print("\n--- STAGE 4 — QUERY EMBEDDING ---")
        try:
            vec = original_embed_query(text)
            print(f"embedding_model: {getattr(embedding_service, 'model_name', 'N/A')}")
            print(f"embedding_dimension: {len(vec)}")
            print(f"device: {getattr(embedding_service, 'device', 'N/A')}")
            print(f"embedding_success: True")
            return vec
        except Exception as e:
            print(f"embedding_success: False, error={e}")
            raise e
            
    embedding_service.embed_query = mock_embed_query
    
    # Hook into vector_store to see Stage 5
    if hasattr(vector_store, "similarity_search_with_scores"):
        original_ssws = vector_store.similarity_search_with_scores
        def mock_ssws(*args, **kwargs):
            results = original_ssws(*args, **kwargs)
            print("\n--- STAGE 5 — RAW RETRIEVAL ---")
            for rank, (chunk, score) in enumerate(results, 1):
                meta = chunk.chunk_metadata or {}
                # Try parsing content for metadata if it's JSON
                try:
                    data = json.loads(chunk.content)
                    title = data.get("title", "N/A")
                    dept = data.get("department") or data.get("owner") or "N/A"
                    doc_type = data.get("document_type", "N/A")
                    category = data.get("category", "N/A")
                except:
                    title = "N/A"
                    dept = "N/A"
                    doc_type = "N/A"
                    category = "N/A"
                    
                print(f"rank {rank}")
                print(f"document_id: {meta.get('document_id', 'N/A')}")
                print(f"title: {title}")
                print(f"department: {dept}")
                print(f"department_code: {meta.get('department_code', 'N/A')}")
                print(f"document_type: {doc_type}")
                print(f"category: {category}")
                print(f"semantic_score: {score}\n")
            return results
        vector_store.similarity_search_with_scores = mock_ssws
    
    # We also want Stage 6 (Domain / Intent Filter), Stage 7 (Reranking), etc.
    # Stage 6 is inside pgvector_retriever.py retrieve method.
    original_retrieve = retriever.retrieve
    def mock_retrieve(*args, **kwargs):
        intent = kwargs.get("intent")
        top_k = kwargs.get("top_k", 5)
        print("\n--- STAGE 6 — DOMAIN / INTENT FILTER ---")
        print(f"intent: {intent}")
        print(f"expected_domain: {intent}")
        
        # We need to peek into the filtered list.
        # Let's run it and just capture the output
        results = original_retrieve(*args, **kwargs)
        
        for idx, res in enumerate(results):
            try:
                data = json.loads(res)
                title = data.get("title", "N/A")
                dept = data.get("department") or data.get("owner") or "N/A"
            except:
                title = "N/A"
                dept = "N/A"
            print(f"document_id: N/A")
            print(f"title: {title}")
            print(f"department: {dept}")
            print(f"department_code: N/A")
            print(f"score: N/A\n")
            
        return results
    retriever.retrieve = mock_retrieve

    print("\n[Executing workflow...]")
    final_state = workflow.invoke(initial_state)
    
    print("\n--- STAGE 13 — FINAL API RESPONSE ---")
    print(f"query: {query}")
    final_ans = final_state.get("final_answer") or {}
    print(f"answer: {final_ans.get('answer', 'N/A')}")
    print(f"intent: {final_state.get('intent', 'N/A')}")
    print(f"plan: {final_state.get('plan', [])}")
    print(f"confidence: {final_ans.get('confidence', 'N/A')}")
    print(f"sources: {final_ans.get('references', [])}")


if __name__ == '__main__':
    trace_query("What is the onboarding process for new hires?", "HR")
    trace_query("What is the IT department's password policy?", "HR")
    trace_query("How do I submit an expense claim?", "HR")
    trace_query("hi", "HR")
    trace_query("What is the company's policy for employees living on Mars?", "HR")
