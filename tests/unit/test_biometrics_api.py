"""Unit and integration tests for Biometric Authentication API routes."""

import base64
import io
import pytest
from datetime import datetime, timedelta, timezone
from fastapi.testclient import TestClient
from PIL import Image
from sqlalchemy import select

from api.auth import create_access_token, hash_password
from api.main import create_app
from database.connection import SessionLocal
from database.models import BiometricCredential, User
from services.biometric_service import (
    BiometricService,
    MockFaceEngine,
    set_biometric_service,
)


def _generate_valid_test_image_base64(color: tuple = (120, 140, 160)) -> str:
    """Generate a clean test image with texture to pass anti-spoofing heuristics."""
    img = Image.new("RGB", (200, 200), color=color)
    # Add varying pixel noise so variance > 15
    pixels = img.load()
    for x in range(0, 200, 4):
        for y in range(0, 200, 4):
            pixels[x, y] = ((x * 7) % 256, (y * 11) % 256, (x + y) % 256)
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    return base64.b64encode(buf.getvalue()).decode("ascii")


@pytest.fixture(autouse=True)
def setup_mock_biometrics():
    """Ensure MockFaceEngine is used during API tests."""
    mock_service = BiometricService(engine=MockFaceEngine())
    set_biometric_service(mock_service)
    yield
    set_biometric_service(None)



@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_user(db_session):
    """Create a temporary employee user for biometric testing."""
    email = f"bio_test_{datetime.now(timezone.utc).timestamp()}@knowxai.com"
    user = User(
        email=email,
        username=f"biotest_{int(datetime.now(timezone.utc).timestamp())}",
        full_name="Biometric Test User",
        employee_id=f"EMP-BIO-{int(datetime.now(timezone.utc).timestamp())}",
        department="IT Support",
        hashed_password=hash_password("SecureBioPass123!"),
        role="Employee",
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    yield user
    # Cleanup
    db_session.execute(
        select(BiometricCredential).where(BiometricCredential.user_id == user.id)
    )
    db_session.delete(user)
    db_session.commit()


@pytest.fixture
def auth_headers(test_user):
    token = create_access_token({"sub": test_user.email})
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


def test_enrollment_requires_explicit_consent(client, auth_headers):
    """Consent checkbox must be True; False must be rejected with HTTP 400."""
    img_b64 = _generate_valid_test_image_base64()
    response = client.post(
        "/auth/biometrics/enroll",
        headers=auth_headers,
        json={
            "image_base64": img_b64,
            "consent_given": False,
        },
    )
    assert response.status_code == 400
    assert "Explicit user consent is mandatory" in response.json()["detail"]


def test_successful_enrollment_and_status(client, auth_headers, test_user):
    """User can enroll face and status reflects active biometric credential."""
    img_b64 = _generate_valid_test_image_base64((100, 150, 200))
    response = client.post(
        "/auth/biometrics/enroll",
        headers=auth_headers,
        json={
            "image_base64": img_b64,
            "consent_given": True,
        },
    )
    assert response.status_code == 200
    assert response.json()["success"] is True

    # Check status endpoint with identifier
    status_resp = client.get(f"/auth/biometrics/status?identifier={test_user.email}")
    assert status_resp.status_code == 200
    status_data = status_resp.json()
    assert status_data["is_enrolled"] is True
    assert status_data["is_enabled"] is True
    assert status_data["is_locked"] is False


def test_face_verification_success_and_jwt_issuance(client, auth_headers, test_user):
    """1:1 face verification matching the enrolled face returns valid JWT."""
    img_b64 = _generate_valid_test_image_base64((100, 150, 200))
    # 1. Enroll
    enroll_resp = client.post(
        "/auth/biometrics/enroll",
        headers=auth_headers,
        json={"image_base64": img_b64, "consent_given": True},
    )
    assert enroll_resp.status_code == 200

    # 2. Verify with matching image
    verify_resp = client.post(
        "/auth/biometrics/verify",
        json={
            "identifier": test_user.email,
            "image_base64": img_b64,
        },
    )
    assert verify_resp.status_code == 200
    body = verify_resp.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"
    assert body["user"]["email"] == test_user.email


def test_face_verification_lockout_after_failed_attempts(client, auth_headers, test_user, db_session):
    """Failed face verification increments failed_attempts and locks out after 5 attempts."""
    enrolled_img = _generate_valid_test_image_base64((50, 50, 50))
    diff_img = _generate_valid_test_image_base64((220, 220, 220))

    # Enroll
    client.post(
        "/auth/biometrics/enroll",
        headers=auth_headers,
        json={"image_base64": enrolled_img, "consent_given": True},
    )

    # Fail 4 times
    for i in range(4):
        fail_resp = client.post(
            "/auth/biometrics/verify",
            json={"identifier": test_user.email, "image_base64": diff_img},
        )
        assert fail_resp.status_code == 401

    # 5th failure triggers lockout
    lock_resp = client.post(
        "/auth/biometrics/verify",
        json={"identifier": test_user.email, "image_base64": diff_img},
    )
    assert lock_resp.status_code == 423
    assert "locked due to multiple failed attempts" in lock_resp.json()["detail"]


def test_toggle_and_delete_biometric_credential(client, auth_headers, test_user):
    """User can disable face login and permanently delete biometric data."""
    img_b64 = _generate_valid_test_image_base64()
    # Enroll
    client.post(
        "/auth/biometrics/enroll",
        headers=auth_headers,
        json={"image_base64": img_b64, "consent_given": True},
    )

    # Toggle off
    toggle_resp = client.post(
        "/auth/biometrics/toggle",
        headers=auth_headers,
        json={"is_enabled": False},
    )
    assert toggle_resp.status_code == 200
    assert toggle_resp.json()["is_enabled"] is False

    # Attempt login while disabled -> rejected
    verify_resp = client.post(
        "/auth/biometrics/verify",
        json={"identifier": test_user.email, "image_base64": img_b64},
    )
    assert verify_resp.status_code == 401
    assert "not enabled" in verify_resp.json()["detail"]

    # Delete credential
    del_resp = client.delete("/auth/biometrics", headers=auth_headers)
    assert del_resp.status_code == 200
    assert del_resp.json()["success"] is True

    # Status check confirms unenrolled
    status_resp = client.get(f"/auth/biometrics/status?identifier={test_user.email}")
    assert status_resp.json()["is_enrolled"] is False


def test_face_verification_version_mismatch_returns_409(client, auth_headers, test_user, db_session):
    """If template_version in DB doesn't match current engine version_tag, return 409 Conflict and do not lock out."""
    img_b64 = _generate_valid_test_image_base64()
    # Enroll
    enroll_resp = client.post(
        "/auth/biometrics/enroll",
        headers=auth_headers,
        json={"image_base64": img_b64, "consent_given": True},
    )
    assert enroll_resp.status_code == 200

    # Manually simulate an older model template version in DB
    cred = db_session.execute(
        select(BiometricCredential).where(BiometricCredential.user_id == test_user.id)
    ).scalar_one()
    cred.template_version = "legacy_v0_model"
    db_session.commit()

    # Attempt face verification -> must receive 409 Conflict with re-enrollment prompt
    verify_resp = client.post(
        "/auth/biometrics/verify",
        json={"identifier": test_user.email, "image_base64": img_b64},
    )
    assert verify_resp.status_code == 409
    body = verify_resp.json()
    assert "re-enrollment" in body["detail"].lower()

    # Ensure failed_attempts counter was NOT incremented on model version mismatch
    db_session.refresh(cred)
    assert cred.failed_attempts == 0

