from unittest.mock import Mock, patch

from pydantic import BaseModel

from agents.llm.factory import build_provider
from agents.llm.providers import GeminiProvider, OpenAICompatibleProvider
from config.settings import Settings


class Answer(BaseModel):
    answer: str


def make_settings(**overrides: str) -> Settings:
    values = {
        "GEMINI_API_KEY": "native-gemini-key",
        "GEMINI_MODEL": "gemini-2.0-flash",
        "GEMINI_OPENROUTER_MODEL": "google/gemini-2.0-flash-001",
        "NVIDIA_API_KEY": "nvidia-key",
        "DATABASE_URL": "postgresql+psycopg2://user:password@localhost/db",
        **overrides,
    }
    return Settings(_env_file=None, **values)


def test_openrouter_style_gemini_key_uses_openrouter() -> None:
    settings = make_settings(GEMINI_API_KEY="sk-or-test")

    with patch("agents.llm.factory.OpenAICompatibleProvider") as provider_class:
        build_provider("gemini", settings=settings)

    provider_class.assert_called_once_with(
        api_key="sk-or-test",
        base_url="https://openrouter.ai/api/v1",
        model="google/gemini-2.0-flash-001",
    )


def test_native_gemini_key_uses_google_sdk() -> None:
    settings = make_settings()

    with patch("agents.llm.factory.GeminiProvider") as provider_class:
        build_provider("gemini", settings=settings)

    provider_class.assert_called_once_with(api_key="native-gemini-key", model="gemini-2.0-flash")


def test_nvidia_openrouter_key_uses_openrouter_and_agent_model_override() -> None:
    settings = make_settings(NVIDIA_API_KEY="sk-or-test")

    with patch("agents.llm.factory.OpenAICompatibleProvider") as provider_class:
        build_provider("nvidia", model="nvidia/test-model", settings=settings)

    provider_class.assert_called_once_with(
        api_key="sk-or-test",
        base_url="https://openrouter.ai/api/v1",
        model="nvidia/test-model",
    )


def test_openai_compatible_structured_response() -> None:
    completion = Mock()
    completion.choices = [Mock(message=Mock(content='{"answer":"ok"}'))]
    client = Mock()
    client.chat.completions.create.return_value = completion

    with patch("agents.llm.providers.OpenAI", return_value=client):
        provider = OpenAICompatibleProvider(
            api_key="test-key",
            base_url="https://example.test/v1",
            model="test-model",
        )
        result = provider.structured(
            [{"role": "user", "content": "Return JSON"}],
            Answer,
        )

    assert result.answer == "ok"
    client.chat.completions.create.assert_called_once()


def test_gemini_generate_uses_google_client() -> None:
    response = Mock(text="ok")
    client = Mock()
    client.models.generate_content.return_value = response

    with patch("agents.llm.providers.genai.Client", return_value=client):
        provider = GeminiProvider(api_key="test-key", model="gemini-test")
        result = provider.generate("hello")

    assert result.text == "ok"
    client.models.generate_content.assert_called_once()
