"""Test suite for Step 10: Local LLM Integration."""

import os
from unittest import mock
import pytest

from config.settings import Settings
from rag.context.models import AssembledContext, ContextItem
from rag.generation.providers import ProviderFactory, LocalLLMProvider
from rag.generation.models import GenerationRequest
from rag.generation.answer_generator import AnswerGenerator
from agents.llm.factory import build_provider, provider_health
from agents.llm.providers import LocalProvider


@pytest.fixture
def mock_settings():
    """Fixture providing settings configured for Local LLM."""
    return Settings(
        llm_provider="local",
        local_llm_base_url="http://localhost:11434/v1",
        local_llm_model="llama3.1",
        gemini_api_key=None,
        nvidia_api_key=None
    )


@pytest.fixture
def empty_context():
    return AssembledContext(
        query="What is the password policy?",
        items=[],
        metadata={},
        formatted_context=""
    )


@pytest.fixture
def sample_context():
    return AssembledContext(
        query="What is the password policy?",
        items=[
            ContextItem(
                document_id="doc-123",
                chunk_id="chunk-1",
                chunk_index=0,
                document_title="IT Policy",
                source="it_policy.pdf",
                text="The password policy requires 14 characters.",
                semantic_score=0.9,
                rank=1,
                rerank_score=0.95,
                metadata={"department": "IT"}
            )
        ],
        metadata={},
        formatted_context="The password policy requires 14 characters."
    )


def test_rag_local_provider_initialization(mock_settings):
    """Test that the ProviderFactory selects LocalLLMProvider correctly."""
    with mock.patch("rag.generation.providers.get_settings", return_value=mock_settings):
        provider = ProviderFactory.get_provider(provider_name="local", assembled_context=None)
        assert isinstance(provider, LocalLLMProvider)
        assert provider.base_url == mock_settings.local_llm_base_url
        assert provider.model_name == mock_settings.local_llm_model
        assert provider.get_name() == "local"
        assert provider.is_available() is True


def test_provider_factory_fallback(mock_settings):
    """Test ProviderFactory provider resolution logic."""
    with mock.patch("rag.generation.providers.get_settings", return_value=mock_settings):
        # 1. provider=None, settings.llm_provider="local" -> LocalLLMProvider
        provider = ProviderFactory.get_provider(provider_name=None)
        assert isinstance(provider, LocalLLMProvider)
        assert provider.get_name() == "local"

        # 2. explicit "mock" -> MockLLMProvider
        provider = ProviderFactory.get_provider(provider_name="mock")
        assert provider.get_name() == "mock"

        # 3. explicit "local" -> LocalLLMProvider
        provider = ProviderFactory.get_provider(provider_name="local")
        assert provider.get_name() == "local"

        # 4. Invalid provider -> ValueError
        with pytest.raises(ValueError, match="Unknown provider"):
            ProviderFactory.get_provider(provider_name="invalid_xyz")

        # 5. explicit "openrouter" -> OpenAICompatibleProvider
        # Mock settings to have openrouter valid
        mock_settings.llm_provider = "local"
        mock_settings.gemini_api_key = mock.Mock()
        mock_settings.gemini_api_key.get_secret_value.return_value = "sk-or-1234"
        mock_settings.openrouter_base_url = "https://openrouter.ai/api/v1"
        mock_settings.gemini_openrouter_model = "google/gemini-pro"
        
        provider = ProviderFactory.get_provider(provider_name="openrouter")
        assert provider.get_name() == "openai_compatible"


def test_agent_local_provider_initialization(mock_settings):
    """Test that the agent factory selects LocalProvider correctly."""
    provider = build_provider("local", settings=mock_settings)
    assert isinstance(provider, LocalProvider)
    assert provider.model == mock_settings.local_llm_model


@mock.patch("openai.resources.chat.completions.Completions.create")
def test_rag_local_provider_generation_success(mock_create, mock_settings, sample_context):
    """Test successful generation with LocalLLMProvider."""
    # Setup mock response
    mock_choice = mock.Mock()
    mock_choice.message.content = "The policy requires 14 characters."
    mock_choice.finish_reason = "stop"
    
    mock_response = mock.Mock()
    mock_response.choices = [mock_choice]
    mock_response.usage.prompt_tokens = 10
    mock_response.usage.completion_tokens = 8
    mock_response.usage.total_tokens = 18
    mock_create.return_value = mock_response

    provider = LocalLLMProvider(
        base_url=mock_settings.local_llm_base_url,
        model_name=mock_settings.local_llm_model,
        assembled_context=sample_context
    )
    
    answer = provider.generate("Tell me the password policy.", temperature=0.1)
    
    assert answer.answer == "The policy requires 14 characters."
    assert answer.provider_name == "local"
    assert answer.model_name == mock_settings.local_llm_model
    assert answer.is_mock is False


def test_rag_local_provider_insufficient_context(mock_settings, empty_context):
    """Test that the local provider refuses to hallucinate without context."""
    provider = LocalLLMProvider(
        base_url=mock_settings.local_llm_base_url,
        model_name=mock_settings.local_llm_model,
        assembled_context=empty_context
    )
    
    answer = provider.generate("Tell me the password policy.")
    
    assert "I don't have enough information" in answer.answer
    assert answer.prompt_tokens == 0


@mock.patch("openai.resources.chat.completions.Completions.create")
def test_rag_local_provider_connection_error(mock_create, mock_settings, sample_context):
    """Test that connection errors are mapped to clean application errors."""
    import httpx
    mock_create.side_effect = httpx.ConnectError("Failed to connect to localhost:11434")

    provider = LocalLLMProvider(
        base_url=mock_settings.local_llm_base_url,
        model_name=mock_settings.local_llm_model,
        assembled_context=sample_context
    )
    
    with pytest.raises(RuntimeError) as exc_info:
        provider.generate("Tell me the password policy.")
        
    assert "Local LLM service is unavailable" in str(exc_info.value)
    assert "start Ollama" in str(exc_info.value)


@mock.patch("openai.resources.chat.completions.Completions.create")
def test_agent_local_provider_connection_error(mock_create, mock_settings):
    """Test that connection errors in the agent provider are mapped cleanly."""
    import httpx
    mock_create.side_effect = httpx.ConnectError("Failed to connect to localhost:11434")

    provider = LocalProvider(
        base_url=mock_settings.local_llm_base_url,
        model=mock_settings.local_llm_model
    )
    
    with pytest.raises(RuntimeError) as exc_info:
        provider.generate("Tell me the password policy.")
        
    assert "Local LLM service is unavailable" in str(exc_info.value)
    assert "start Ollama" in str(exc_info.value)


@mock.patch("openai.resources.chat.completions.Completions.create")
def test_provider_health_check_local(mock_create, mock_settings):
    """Test health check logic for local provider."""
    # When httpx fails, healthy is False
    import httpx
    mock_create.side_effect = httpx.ConnectError("Connection refused")
    
    health = provider_health(settings=mock_settings)
    assert "local" in health
    assert health["local"]["configured"] is True
    assert health["local"]["healthy"] is False
    
    # When it succeeds
    mock_choice = mock.Mock()
    mock_choice.message.content = "ok"
    mock_response = mock.Mock()
    mock_response.choices = [mock_choice]
    mock_create.side_effect = None
    mock_create.return_value = mock_response
    
    health = provider_health(settings=mock_settings)
    assert health["local"]["healthy"] is True
