import pytest
from fastapi.testclient import TestClient

from config.settings import Settings


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setenv("GEMINI_API_KEY", "test-only-placeholder")
    from api.main import create_app

    settings = Settings(_env_file=None)
    return TestClient(create_app(settings))


def test_application_import_and_settings_integration(client: TestClient) -> None:
    assert client.app.title == "Agentic-RAG-KnowXAI"
    assert client.app.version == "0.1.0"
    assert client.app.state.environment == "development"


def test_root_endpoint(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_endpoint(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] in ("healthy", "degraded")
