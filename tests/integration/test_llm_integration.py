import os

import pytest

from agents.llm.factory import build_provider
from config.settings import get_settings


pytestmark = pytest.mark.integration


def configured_provider_names() -> list[str]:
    names = []
    settings = get_settings()
    if settings.gemini_api_key and settings.gemini_api_key.get_secret_value().strip():
        names.append("gemini")
    if settings.nvidia_api_key and settings.nvidia_api_key.get_secret_value().strip():
        names.append("nvidia")
    return names


@pytest.mark.parametrize("provider_name", ["gemini", "nvidia"])
def test_live_provider_inference(provider_name: str) -> None:
    if os.getenv("RUN_LLM_INTEGRATION", "").lower() not in {"1", "true", "yes"}:
        pytest.skip("Set RUN_LLM_INTEGRATION=true to run paid provider inference")
    if provider_name not in configured_provider_names():
        pytest.skip(f"{provider_name} credentials are not configured")

    response = build_provider(provider_name).generate("Reply with exactly: ok", temperature=0.0)

    assert response.text.strip()
