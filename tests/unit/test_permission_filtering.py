"""Unit tests for RAG document permission filtering."""

from rag.retrieval.pgvector_retriever import PGVectorRetriever


def test_document_permission_filtering():
    # Instantiate retriever with dummy dependencies to test access check logic
    retriever = PGVectorRetriever(None, None)
    
    # 1. Non-restricted document metadata (normal policies/public)
    meta_public = {}
    meta_employee = {"access_level": "employee"}
    
    # 2. Restricted documents
    meta_restricted_it = {
        "access_level": "restricted",
        "allowed_departments": ["IT Support"]
    }
    meta_restricted_finance = {
        "access_level": "restricted",
        "allowed_departments": ["Finance & Claims"]
    }
    
    # User session contexts
    user_it = {"role": "Employee", "department": "IT Support"}
    user_finance = {"role": "Employee", "department": "Finance & Claims"}
    user_admin = {"role": "Admin", "department": "Finance & Claims"}
    user_management = {"role": "Employee", "department": "Management"}
    
    # Verify employee/public access (anyone can retrieve)
    assert retriever.check_document_access(meta_public, user_it) is True
    assert retriever.check_document_access(meta_employee, user_it) is True
    assert retriever.check_document_access(meta_public, user_finance) is True
    assert retriever.check_document_access(meta_employee, user_finance) is True
    
    # Verify IT Restricted access rules
    assert retriever.check_document_access(meta_restricted_it, user_it) is True
    assert retriever.check_document_access(meta_restricted_it, user_finance) is False  # Unauthorized
    assert retriever.check_document_access(meta_restricted_it, user_admin) is True    # Admin override
    assert retriever.check_document_access(meta_restricted_it, user_management) is True  # Management override
    
    # Verify Finance Restricted access rules
    assert retriever.check_document_access(meta_restricted_finance, user_finance) is True
    assert retriever.check_document_access(meta_restricted_finance, user_it) is False  # Unauthorized
    assert retriever.check_document_access(meta_restricted_finance, user_admin) is True
    assert retriever.check_document_access(meta_restricted_finance, user_management) is True
    
    # Verify fuzzy department name matching ('it' matches 'it support', etc.)
    meta_restricted_fuzzy_it = {
        "access_level": "restricted",
        "allowed_departments": ["IT"]
    }
    assert retriever.check_document_access(meta_restricted_fuzzy_it, user_it) is True
