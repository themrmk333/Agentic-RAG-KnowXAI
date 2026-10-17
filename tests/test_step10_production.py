import pytest
from fastapi.testclient import TestClient
from config.settings import get_settings

# Re-import main to get the app
from api.main import app

client = TestClient(app, raise_server_exceptions=False)

def test_01_health_readiness_endpoints():
    """Verify that health and readiness probes are active and return 200."""
    # Readiness probe
    response = client.get("/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"

def test_02_cors_middleware_configured():
    """Verify that CORS middleware is injected and reflects the settings."""
    # Test an OPTIONS preflight request
    headers = {
        "Origin": "http://localhost:3000",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "X-Requested-With",
    }
    response = client.options("/ready", headers=headers)
    assert response.status_code == 200
    # Depending on settings, it might echo the origin or allow *
    assert "access-control-allow-origin" in response.headers
    
def test_03_production_global_exception_handler():
    """Verify the global exception handler masks exceptions in production."""
    # We temporarily set the app environment to production
    original_env = app.state.environment
    app.state.environment = "production"
    
    @app.get("/test-error")
    def error_route():
        raise ValueError("Test Secret Error")
        
    response = client.get("/test-error")
    assert response.status_code == 500
    data = response.json()
    assert data["detail"] == "Internal server error"
    assert "Test Secret Error" not in str(data)
    
    app.state.environment = original_env

def test_04_environment_config_loaded():
    """Verify that pydantic settings correctly pick up variables."""
    settings = get_settings()
    assert settings.port >= 1
    assert isinstance(settings.cors_origins, list)
    assert settings.app_env in ["development", "testing", "staging", "production"]
