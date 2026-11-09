"""Unit tests for Google OAuth authentication endpoint."""

from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select

from api.main import create_app
from database.connection import SessionLocal
from database.models import User


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def test_google_config_endpoint(client):
    """Config endpoint returns status of Google OAuth integration."""
    resp = client.get("/auth/google/config")
    assert resp.status_code == 200
    assert "enabled" in resp.json()


def test_google_sign_in_unconfigured(client, monkeypatch):
    """Sign-in returns 503 if GOOGLE_CLIENT_ID is not configured."""
    from config.settings import get_settings
    settings = get_settings()
    monkeypatch.setattr(settings, "google_client_id", None)

    resp = client.post("/auth/google", json={"credential": "sample_token"})
    assert resp.status_code == 503
    assert "Google Sign-In is not configured" in resp.json()["detail"]


@patch("google.oauth2.id_token.verify_oauth2_token")
def test_google_sign_in_success_new_user(mock_verify, client, monkeypatch, db_session):
    """Valid Google token provisions a new user with verified email."""
    from config.settings import get_settings
    settings = get_settings()
    monkeypatch.setattr(settings, "google_client_id", "valid-google-client-id.apps.googleusercontent.com")

    test_google_id = "google_sub_12345678"
    test_email = "newgoogleuser@example.com"

    mock_verify.return_value = {
        "sub": test_google_id,
        "email": test_email,
        "email_verified": True,
        "name": "Google Test Employee",
    }

    try:
        resp = client.post("/auth/google", json={"credential": "mock_valid_token"})
        assert resp.status_code == 200
        data = resp.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert data["user"]["email"] == test_email
        assert data["user"]["full_name"] == "Google Test Employee"

        # Verify DB entry
        user = db_session.execute(select(User).where(User.google_id == test_google_id)).scalar_one_or_none()
        assert user is not None
        assert user.auth_provider == "google"
    finally:
        # Cleanup
        u = db_session.execute(select(User).where(User.email == test_email)).scalar_one_or_none()
        if u:
            db_session.delete(u)
            db_session.commit()


@patch("google.oauth2.id_token.verify_oauth2_token")
def test_google_sign_in_unverified_email_rejected(mock_verify, client, monkeypatch):
    """Google accounts with unverified emails must be rejected."""
    from config.settings import get_settings
    settings = get_settings()
    monkeypatch.setattr(settings, "google_client_id", "valid-client-id.apps.googleusercontent.com")

    mock_verify.return_value = {
        "sub": "sub_unverified",
        "email": "unverified@example.com",
        "email_verified": False,
    }

    resp = client.post("/auth/google", json={"credential": "token_unverified"})
    assert resp.status_code == 400
    assert "email is not verified" in resp.json()["detail"]


@patch("google.oauth2.id_token.verify_oauth2_token")
def test_google_sign_in_invalid_token(mock_verify, client, monkeypatch):
    """Invalid Google ID token returns 401 Unauthorized."""
    from config.settings import get_settings
    settings = get_settings()
    monkeypatch.setattr(settings, "google_client_id", "valid-client-id.apps.googleusercontent.com")

    mock_verify.side_effect = ValueError("Token signature verification failed")

    resp = client.post("/auth/google", json={"credential": "tampered_token"})
    assert resp.status_code == 401
    assert "Google authentication failed" in resp.json()["detail"]
