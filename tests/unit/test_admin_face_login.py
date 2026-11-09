"""Unit and integration tests for Super Admin Face Authentication endpoints.

Tests:
- 1:1 Super Admin face verification (with claimed identifier)
- 1:N Super Admin face discovery (omitted identifier)
- Denial of regular employee credentials (returns 403 Forbidden)
- Rejection of unknown faces (returns 401 Unauthorized)
- Blocked deactivation (returns 403 Forbidden)
- Lockout protection after 5 failed attempts (returns 423 Locked)
- Unenrolled Super Admin handling
- Verification of both /auth/biometrics/admin-verify and /auth/admin-face-login endpoints
"""

import base64
import io
import pytest
from datetime import datetime, timezone
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
from api.routes.biometrics import _request_timestamps


def _generate_valid_test_image_base64(color: tuple = (120, 140, 160)) -> str:
    """Generate a clean test image with texture to pass anti-spoofing heuristics."""
    img = Image.new("RGB", (200, 200), color=color)
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
    _request_timestamps.clear()
    yield
    set_biometric_service(None)
    _request_timestamps.clear()


@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client():
    app = create_app()
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def super_admin_user(db_session):
    """Create a temporary Super Admin user."""
    ts = int(datetime.now(timezone.utc).timestamp())
    email = f"sa_bio_{ts}@knowxai.com"
    user = User(
        email=email,
        username=f"sa_bio_{ts}",
        full_name="Super Admin Face Test",
        hashed_password=hash_password("SuperSecret123!"),
        role="Super Admin",
        employee_id=f"EMP-SA-{ts % 10000}",
        department="Management",
        is_active=True,
        token_version=1,
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
def employee_user(db_session):
    """Create a temporary standard employee user."""
    ts = int(datetime.now(timezone.utc).timestamp())
    email = f"emp_bio_{ts}@knowxai.com"
    user = User(
        email=email,
        username=f"emp_bio_{ts}",
        full_name="Standard Employee Test",
        hashed_password=hash_password("EmpSecret123!"),
        role="Employee",
        employee_id=f"EMP-ST-{ts % 10000}",
        department="IT Support",
        is_active=True,
        token_version=1,
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


def test_super_admin_face_login_success_1_to_1(client, super_admin_user):
    """Verify Super Admin can authenticate via Face ID using their identifier."""
    face_img = _generate_valid_test_image_base64((100, 150, 200))
    admin_token = create_access_token({"sub": super_admin_user.email})

    # Enroll face for Super Admin
    enroll_resp = client.post(
        "/auth/biometrics/enroll",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"image_base64": face_img, "consent_given": True},
    )
    assert enroll_resp.status_code == 200

    # Verify Face Login with claimed identifier via /auth/biometrics/admin-verify
    verify_resp = client.post(
        "/auth/biometrics/admin-verify",
        json={
            "identifier": super_admin_user.email,
            "image_base64": face_img,
        },
    )
    assert verify_resp.status_code == 200
    body = verify_resp.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"
    assert body["user"]["email"] == super_admin_user.email

    # Also test alias /auth/admin-face-login
    alias_resp = client.post(
        "/auth/admin-face-login",
        json={
            "identifier": super_admin_user.email,
            "image_base64": face_img,
        },
    )
    assert alias_resp.status_code == 200
    assert "access_token" in alias_resp.json()


def test_super_admin_face_login_success_1_to_n(client, super_admin_user):
    """Verify Super Admin can authenticate via Face ID without specifying an identifier (1:N matching)."""
    face_img = _generate_valid_test_image_base64((90, 130, 180))
    admin_token = create_access_token({"sub": super_admin_user.email})

    # Enroll face
    enroll_resp = client.post(
        "/auth/biometrics/enroll",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"image_base64": face_img, "consent_given": True},
    )
    assert enroll_resp.status_code == 200

    # Authenticate with NO identifier
    verify_resp = client.post(
        "/auth/biometrics/admin-verify",
        json={
            "image_base64": face_img,
        },
    )
    assert verify_resp.status_code == 200
    body = verify_resp.json()
    assert body["user"]["email"] == super_admin_user.email


def test_admin_face_login_strictly_denies_employee(client, employee_user):
    """Verify regular employees are strictly blocked from Super Admin Face Login with 403 Forbidden."""
    emp_img = _generate_valid_test_image_base64((70, 80, 90))
    emp_token = create_access_token({"sub": employee_user.email})

    # Enroll face for employee
    enroll_resp = client.post(
        "/auth/biometrics/enroll",
        headers={"Authorization": f"Bearer {emp_token}"},
        json={"image_base64": emp_img, "consent_given": True},
    )
    assert enroll_resp.status_code == 200

    # 1. Attempt with employee identifier -> must receive 403 Forbidden
    verify_resp = client.post(
        "/auth/biometrics/admin-verify",
        json={
            "identifier": employee_user.email,
            "image_base64": emp_img,
        },
    )
    assert verify_resp.status_code == 403
    assert "Access Denied" in verify_resp.json()["detail"]
    assert "Super Admin" in verify_resp.json()["detail"]

    # Also test via /auth/admin-face-login
    alias_resp = client.post(
        "/auth/admin-face-login",
        json={
            "identifier": employee_user.email,
            "image_base64": emp_img,
        },
    )
    assert alias_resp.status_code == 403

    # 2. Attempt 1:N discovery with employee face -> must be rejected (401: no super admin matches)
    auto_resp = client.post(
        "/auth/biometrics/admin-verify",
        json={
            "image_base64": emp_img,
        },
    )
    assert auto_resp.status_code == 401


def test_admin_face_login_rejects_unknown_face(client, super_admin_user):
    """Verify non-matching face returns 401 Unauthorized."""
    face_img = _generate_valid_test_image_base64((100, 100, 100))
    wrong_img = _generate_valid_test_image_base64((180, 140, 120))
    admin_token = create_access_token({"sub": super_admin_user.email})

    client.post(
        "/auth/biometrics/enroll",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"image_base64": face_img, "consent_given": True},
    )

    resp = client.post(
        "/auth/biometrics/admin-verify",
        json={
            "identifier": super_admin_user.email,
            "image_base64": wrong_img,
        },
    )
    assert resp.status_code == 401
    assert "Face does not match" in resp.json()["detail"]


def test_admin_face_login_rejects_deactivated_account(client, super_admin_user, db_session):
    """Verify deactivated Super Admin cannot authenticate via Face Login."""
    face_img = _generate_valid_test_image_base64((110, 120, 130))
    admin_token = create_access_token({"sub": super_admin_user.email})

    client.post(
        "/auth/biometrics/enroll",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"image_base64": face_img, "consent_given": True},
    )

    # Deactivate admin
    super_admin_user.is_active = False
    db_session.commit()

    resp = client.post(
        "/auth/biometrics/admin-verify",
        json={
            "identifier": super_admin_user.email,
            "image_base64": face_img,
        },
    )
    assert resp.status_code == 403
    assert "deactivated" in resp.json()["detail"].lower()


def test_admin_face_login_lockout_after_five_failed_attempts(client, super_admin_user):
    """Verify account locks after 5 consecutive failed face verification attempts."""
    face_img = _generate_valid_test_image_base64((55, 65, 75))
    wrong_img = _generate_valid_test_image_base64((180, 140, 120))
    admin_token = create_access_token({"sub": super_admin_user.email})

    client.post(
        "/auth/biometrics/enroll",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"image_base64": face_img, "consent_given": True},
    )

    # 4 failed attempts
    for _ in range(4):
        resp = client.post(
            "/auth/biometrics/admin-verify",
            json={"identifier": super_admin_user.email, "image_base64": wrong_img},
        )
        assert resp.status_code == 401

    # 5th failed attempt triggers 423 Locked
    lock_resp = client.post(
        "/auth/biometrics/admin-verify",
        json={"identifier": super_admin_user.email, "image_base64": wrong_img},
    )
    assert lock_resp.status_code == 423
    assert "locked" in lock_resp.json()["detail"].lower()


def test_admin_face_login_version_mismatch_1_to_1(client, super_admin_user, db_session):
    """Verify 1:1 admin face login returns 409 Conflict when template_version doesn't match engine."""
    face_img = _generate_valid_test_image_base64((55, 65, 75))
    admin_token = create_access_token({"sub": super_admin_user.email})

    client.post(
        "/auth/biometrics/enroll",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"image_base64": face_img, "consent_given": True},
    )

    cred = db_session.execute(
        select(BiometricCredential).where(BiometricCredential.user_id == super_admin_user.id)
    ).scalar_one()
    cred.template_version = "outdated_v0"
    db_session.commit()

    resp = client.post(
        "/auth/biometrics/admin-verify",
        json={"identifier": super_admin_user.email, "image_base64": face_img},
    )
    assert resp.status_code == 409
    assert "re-enrollment" in resp.json()["detail"].lower()


def test_admin_face_login_version_mismatch_1_to_n(client, super_admin_user, db_session):
    """Verify 1:N admin face login safely returns 401 Unauthorized when templates are outdated to prevent enumeration."""
    face_img = _generate_valid_test_image_base64((55, 65, 75))
    admin_token = create_access_token({"sub": super_admin_user.email})

    client.post(
        "/auth/biometrics/enroll",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"image_base64": face_img, "consent_given": True},
    )

    cred = db_session.execute(
        select(BiometricCredential).where(BiometricCredential.user_id == super_admin_user.id)
    ).scalar_one()
    cred.template_version = "outdated_v0"
    db_session.commit()

    resp = client.post(
        "/auth/biometrics/admin-verify",
        json={"image_base64": face_img},
    )
    assert resp.status_code == 401
    assert "Authentication failed" in resp.json()["detail"]

