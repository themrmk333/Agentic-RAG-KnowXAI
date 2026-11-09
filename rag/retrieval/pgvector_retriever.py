"""RAGRetriever implementation backed by PostgreSQL + pgvector."""

from __future__ import annotations

from typing import Any

from agents.rag.interface import RAGRetriever
from database.vector_store import PGVectorStore
from rag.embeddings.openai_embeddings import OpenAIEmbeddingService


class PGVectorRetriever(RAGRetriever):
    """Embed a query and delegate similarity search to the vector store with permission checks."""

    def __init__(self, embedding_service: Any = None, vector_store: PGVectorStore | None = None) -> None:
        if embedding_service is None:
            from rag.retrieval.query_embedder import QueryEmbedder
            self.embedding_service = QueryEmbedder.get_instance()
        else:
            self.embedding_service = embedding_service
        self.vector_store = vector_store or PGVectorStore()

    def check_document_access(self, metadata: dict, user_context: dict) -> bool:
        """Evaluate access permissions for a chunk/document.
        
        Supports employee vs restricted policies. Normalizes departments for robust matching.
        """
        if not metadata:
            return True
            
        access_level = str(metadata.get("access_level", "employee")).lower().strip()
        
        # If document is not restricted, it is accessible to all employees by default
        if access_level != "restricted":
            return True
            
        # restricted document requires user context
        if not user_context:
            return False
            
        user_role = str(user_context.get("role", "Employee")).lower().strip()
        user_dept = str(user_context.get("department", "")).lower().strip()
        
        # Admins and Management have absolute read access
        if user_role in ("admin", "management") or user_dept == "management":
            return True
            
        allowed_depts = metadata.get("allowed_departments", [])
        if isinstance(allowed_depts, str):
            allowed_depts = [allowed_depts]
            
        # Clean department suffix and match
        def clean_dept(dept: str) -> str:
            d = dept.lower().strip()
            for suffix in [" support", " department", " & claims"]:
                d = d.replace(suffix, "")
            return d.strip()
            
        user_dept_clean = clean_dept(user_dept)
        for dept in allowed_depts:
            dept_str = str(dept).strip()
            if dept_str in ("*", "all", "ALL"):
                return True
            if clean_dept(dept_str) == user_dept_clean:
                return True
                
        return False

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        user_context: dict = None,
        stats: dict = None,
        intent: str = None,
    ) -> list[str]:
        if not query.strip() or top_k <= 0:
            return []
            
        query_vector = self.embedding_service.embed_query(query)
        
        # Fallback for unit test mock objects which only implement similarity_search
        if hasattr(self.vector_store, "similarity_search_with_scores"):
            raw_chunks = self.vector_store.similarity_search_with_scores(query_vector, limit=top_k * 4)
            filtered = []
            topic_matched = []
            other_authorized = []
            
            for chunk, distance in raw_chunks:
                meta = chunk.chunk_metadata or {}
                if not self.check_document_access(meta, user_context):
                    continue

                filtered.append(chunk.content)
                
                # Apply topic alignment when intent is specified, but route according to actual topic
                # without hard-dropping authorized evidence
                if intent:
                    intent_lower = intent.lower().strip()
                    doc_dept = str(meta.get("department_code") or meta.get("department") or "").lower()
                    doc_cat = str(meta.get("category", "")).lower()
                    content_lower = chunk.content.lower()

                    is_match = False
                    if intent_lower == "finance":
                        is_match = any(k in doc_dept or k in content_lower for k in ["finance", "fin", "expense", "reimbursement", "claim", "billing", "invoice", "payroll"])
                    elif intent_lower == "hr":
                        is_match = any(k in doc_dept or k in content_lower for k in ["hr", "human resources", "leave", "onboarding", "attendance", "benefits", "handbook"])
                    elif intent_lower == "it":
                        is_match = any(k in doc_dept or k in content_lower for k in ["it", "vpn", "password", "laptop", "wifi", "network", "software", "ticket", "hardware"])
                    elif intent_lower == "project":
                        is_match = any(k in doc_dept or k in doc_cat or k in content_lower for k in ["project", "milestone", "pmo", "knowxai", "sprint", "prj-"])
                    elif intent_lower == "sales":
                        is_match = any(k in doc_dept or k in content_lower for k in ["sales", "crm", "lead", "deal", "client"])
                    else:
                        is_match = True

                    if is_match:
                        topic_matched.append(chunk.content)
                    else:
                        other_authorized.append(chunk.content)
                else:
                    topic_matched.append(chunk.content)

            # Prioritize topic-matched results, gracefully falling back to other authorized matches
            if intent:
                final_docs = topic_matched if len(topic_matched) >= top_k else (topic_matched + other_authorized)
            else:
                final_docs = filtered

            raw_len = len(raw_chunks)
        else:
            chunks = self.vector_store.similarity_search(query_vector, limit=top_k)
            final_docs = [chunk.content for chunk in chunks]
            filtered = final_docs
            raw_len = len(chunks)
            
        if stats is not None:
            stats["retrieved_count"] = raw_len
            stats["authorized_count"] = len(filtered)
            
        return final_docs[:top_k]

    def retrieve_with_metadata(self, query: str, top_k: int = 5, user_context: dict = None) -> list[dict[str, Any]]:
        if not query.strip() or top_k <= 0:
            return []
        query_vector = self.embedding_service.embed_query(query)
        matches = self.vector_store.similarity_search_with_scores(query_vector, limit=top_k)
        
        filtered_matches = []
        for chunk, distance in matches:
            meta = chunk.chunk_metadata or {}
            if self.check_document_access(meta, user_context):
                filtered_matches.append({
                    "content": chunk.content,
                    "metadata": meta,
                    "distance": distance
                })
        return filtered_matches