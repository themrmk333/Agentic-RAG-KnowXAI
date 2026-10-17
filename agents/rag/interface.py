"""Defines the abstract interface for the RAG Retriever.

This protocol ensures decoupling from database-specific drivers like PostgreSQL/pgvector or Qdrant.
"""

from typing import List, Protocol


class RAGRetriever(Protocol):
    """Protocol for RAG retrieval."""

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        user_context: dict = None,
        stats: dict = None,
        intent: str = None,
    ) -> List[str]:
        """Retrieve the top k most relevant context passages matching the query.

        Args:
            query: The search query string.
            top_k: Number of relevant context snippets to retrieve.
            user_context: Optional context of the authenticated user for permission checks.
            stats: Optional dictionary to capture retrieval count statistics.
            intent: Optional determined intent category for domain filtering.

        Returns:
            A list of relevant text snippets/documents.
        """
        ...


class MockRAGRetriever:
    """A mock implementation of the RAGRetriever interface for testing and fallback."""

    def __init__(self, mock_documents: List[str] = None) -> None:
        self.mock_documents = mock_documents or [
            "Mock document 1: Python LangGraph is used for building stateful, multi-actor applications.",
            "Mock document 2: PostgreSQL with pgvector supports vector similarity searches.",
            "Mock document 3: The sum of angles in a triangle is always 180 degrees.",
            "Mock document 4: A Critic Agent reviews specialist results for accuracy and flaws.",
        ]

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        user_context: dict = None,
        stats: dict = None,
        intent: str = None,
    ) -> List[str]:
        """Return a subset of mock documents that match keywords, or all of them."""
        query_words = set(query.lower().split())
        matched = []
        for doc in self.mock_documents:
            # Simple keyword matching to simulate retrieval relevance
            if any(word in doc.lower() for word in query_words):
                matched.append(doc)
        
        # Fallback to returning some documents if no keyword matches
        if not matched:
            matched = self.mock_documents[:top_k]
            
        return matched[:top_k]
