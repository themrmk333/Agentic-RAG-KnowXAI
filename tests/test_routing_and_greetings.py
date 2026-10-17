import pytest
from unittest.mock import MagicMock, patch

from agents.state import AgentState
from agents.llm.providers import LocalProvider
from agents.llm.factory import build_provider
from config.settings import Settings
from agents.query.understanding import QueryUnderstandingAgent

@pytest.fixture
def local_settings():
    return Settings(
        llm_provider="local",
        local_llm_base_url="http://localhost:11434/v1",
        local_llm_model="llama3.1:8b",
        postgres_user="test",
        postgres_password="test",
        postgres_db="test",
        gemini_api_key="test"
    )

def test_build_provider_respects_local(local_settings):
    """Ensure build_provider returns LocalProvider when LLM_PROVIDER=local"""
    provider = build_provider("local", settings=local_settings)
    assert isinstance(provider, LocalProvider)
    assert provider.model == "llama3.1:8b"

def test_query_understanding_general_bypasses_rag():
    """Ensure a general greeting does not execute pgvector retrieval"""
    mock_llm = MagicMock()
    # Mock LLM to return a 'general' intent
    mock_llm.structured.return_value = MagicMock(
        intent="general", 
        rephrased_query="hi"
    )
    
    mock_retriever = MagicMock()
    
    agent = QueryUnderstandingAgent(mock_llm, mock_retriever)
    
    state = AgentState(original_query="hi there", user_context={})
    result = agent.execute(state)
    
    assert result["intent"] == "general"
    assert result["relevant_context"] == []
    # Verify retrieve was NEVER called
    mock_retriever.retrieve.assert_not_called()

def test_query_understanding_it_calls_rag():
    """Ensure an IT question calls retrieval"""
    mock_llm = MagicMock()
    mock_llm.structured.return_value = MagicMock(
        intent="it", 
        rephrased_query="reset password"
    )
    
    mock_retriever = MagicMock()
    mock_retriever.retrieve.return_value = ["Context 1"]
    
    agent = QueryUnderstandingAgent(mock_llm, mock_retriever)
    
    state = AgentState(original_query="how do i reset my password", user_context={})
    result = agent.execute(state)
    
    assert result["intent"] == "it"
    assert len(result["relevant_context"]) == 1
    mock_retriever.retrieve.assert_called_once()
