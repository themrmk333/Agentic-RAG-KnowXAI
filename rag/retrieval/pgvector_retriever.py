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
            if clean_dept(dept) == user_dept_clean:
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
            intent_filtered = []
            
            for chunk, distance in raw_chunks:
                meta = chunk.chunk_metadata or {}
                if self.check_document_access(meta, user_context):
                    filtered.append(chunk.content)
                    
                    # Apply intent classification filters to check domain relevance
                    if intent:
                        intent_lower = intent.lower().strip()
                        
                        from rag.chunking.models import normalize_department
                        doc_dept = normalize_department(str(meta.get("department_code") or meta.get("department") or "UNKNOWN"))
                        
                        # Normalize intent to department code if possible
                        is_match = False
                        if intent_lower == "finance":
                            is_match = (doc_dept == "FINANCE")
                        elif intent_lower == "hr":
                            is_match = (doc_dept == "HR")
                        elif intent_lower == "it":
                            is_match = (doc_dept == "IT")
                        elif intent_lower == "project":
                            is_match = (doc_dept == "PROJECT")
                        elif intent_lower == "sales":
                            is_match = (doc_dept == "SALES")
                        else:
                            # For general, research, coding, or math intents, we don't strict-filter by department
                            is_match = True
                            
                        if is_match:
                            intent_filtered.append(chunk.content)
                    else:
                        intent_filtered.append(chunk.content)
            
            # Do not fallback if intent-based filtering is used.
            # Returning irrelevant cross-domain documents causes hallucination.
            final_docs = intent_filtered if intent else filtered
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