"""Unit and integration tests for Enterprise Admin API endpoints."""

from __future__ import annotations

import io
from datetime import datetime, timezone
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select

from api.auth import create_access_token, hash_password
from api.main import create_app
from database.connection import SessionLocal
from database.models import Department, User


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
    email = f"superadmin_{int(datetime.now(timezone.utc).timestamp())}@knowxai.com"
    user = User(
        email=email,
        username=f"superadmin_{int(datetime.now(timezone.utc).timestamp())}",
        full_name="MK Super Admin",
        hashed_password=hash_password("SuperSecret123!"),
        role="Super Admin",
        employee_id=f"EMP-SA-{int(datetime.now(timezone.utc).timestamp()) % 10000}",
        department="Management",
        is_active=True,
        token_version=1,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    yield user
    # Cleanup
    u = db_session.execute(select(User).where(User.id == user.id)).scalar_one_or_none()
    if u:
        db_session.delete(u)
        db_session.commit()


@pytest.fixture
def employee_user(db_session):
    email = f"emp_{int(datetime.now(timezone.utc).timestamp())}@knowxai.com"
    user = User(
        email=email,
        username=f"emp_{int(datetime.now(timezone.utc).timestamp())}",
        full_name="Regular Employee",
        hashed_password=hash_password("EmpSecret123!"),
        role="Employee",
        employee_id=f"EMP-{int(datetime.now(timezone.utc).timestamp()) % 10000}",
        department="IT Support",
        is_active=True,
        token_version=1,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    yield user
    # Cleanup
    u = db_session.execute(select(User).where(User.id == user.id)).scalar_one_or_none()
    if u:
        db_session.delete(u)
        db_session.commit()


def test_employee_cannot_access_admin_dashboard(client, employee_user):
    token = create_access_token(data={"sub": employee_user.email}, token_version=employee_user.token_version)
    headers = {"Authorization": f"Bearer {token}"}

    resp = client.get("/admin/dashboard", headers=headers)
    assert resp.status_code == 403
    assert "Administrator privileges required" in resp.json()["detail"]


def test_super_admin_can_access_dashboard(client, super_admin_user):
    token = create_access_token(data={"sub": super_admin_user.email}, token_version=super_admin_user.token_version)
    headers = {"Authorization": f"Bearer {token}"}

    resp = client.get("/admin/dashboard", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "total_employees" in data
    assert "active_accounts" in data
    assert "department_distribution" in data
    assert "employee_growth" in data


def test_list_employees_pagination_and_search(client, super_admin_user, employee_user):
    token = create_access_token(data={"sub": super_admin_user.email}, token_version=super_admin_user.token_version)
    headers = {"Authorization": f"Bearer {token}"}

    # Search for regular employee
    resp = client.get(f"/admin/employees?search={employee_user.email}", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["total_count"] >= 1
    emails = [item["email"] for item in data["items"]]
    assert employee_user.email in emails


def test_employee_detail_profile(client, super_admin_user, employee_user):
    token = create_access_token(data={"sub": super_admin_user.email}, token_version=super_admin_user.token_version)
    headers = {"Authorization": f"Bearer {token}"}

    resp = client.get(f"/admin/employees/{employee_user.id}", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == employee_user.email
    assert data["role"] == "Employee"
    assert "security" in data
    assert "activity" in data
    assert "hashed_password" not in data


def test_update_employee_status_and_self_deactivation_safeguard(client, super_admin_user, employee_user):
    token = create_access_token(data={"sub": super_admin_user.email}, token_version=super_admin_user.token_version)
    headers = {"Authorization": f"Bearer {token}"}

    # 1. Deactivate employee
    resp = client.patch(f"/admin/employees/{employee_user.id}/status", json={"is_active": False}, headers=headers)
    assert resp.status_code == 200
    assert resp.json()["is_active"] is False

    # 2. Verify deactivated employee cannot log in
    emp_token = create_access_token(data={"sub": employee_user.email})
    bad_resp = client.get("/auth/me", headers={"Authorization": f"Bearer {emp_token}"})
    assert bad_resp.status_code == 403

    # 3. Safeguard: Super admin cannot deactivate self
    self_resp = client.patch(f"/admin/employees/{super_admin_user.id}/status", json={"is_active": False}, headers=headers)
    assert self_resp.status_code == 400
    assert "Self-deactivation denied" in self_resp.json()["detail"]


def test_admin_password_reset(client, super_admin_user, employee_user, db_session):
    token = create_access_token(data={"sub": super_admin_user.email}, token_version=super_admin_user.token_version)
    headers = {"Authorization": f"Bearer {token}"}

    resp = client.post(
        f"/admin/employees/{employee_user.id}/reset-password",
        json={"new_password": "NewSecretPassword99!"},
        headers=headers,
    )
    assert resp.status_code == 200
    assert "Password reset successfully" in resp.json()["message"]

    # Verify new password works
    login_resp = client.post(
        "/auth/login",
        json={"email": employee_user.email, "password": "NewSecretPassword99!"},
    )
    assert login_resp.status_code == 200
    assert "access_token" in login_resp.json()


def test_department_management_and_safeguards(client, super_admin_user, employee_user, db_session):
    token = create_access_token(data={"sub": super_admin_user.email}, token_version=super_admin_user.token_version)
    headers = {"Authorization": f"Bearer {token}"}

    code = f"T{int(datetime.now(timezone.utc).timestamp()) % 1000}"
    name = f"Test Department {code}"

    # 1. Create department
    create_resp = client.post(
        "/admin/departments",
        json={"name": name, "code": code, "description": "Unit test department", "lead_name": "Lead Test"},
        headers=headers,
    )
    assert create_resp.status_code == 200
    dept_id = create_resp.json()["id"]

    try:
        # 2. Assign employee to department
        employee_user.department = name
        db_session.commit()

        # 3. Attempt to delete department while employee assigned -> MUST BE BLOCKED
        del_resp = client.delete(f"/admin/departments/{dept_id}", headers=headers)
        assert del_resp.status_code == 400
        assert "Cannot delete department" in del_resp.json()["detail"]

        # 4. Transfer employee away
        transfer_resp = client.post(
            "/admin/departments/transfer",
            json={"source_department": name, "target_department": "IT Support"},
            headers=headers,
        )
        assert transfer_resp.status_code == 200

        # 5. Now delete department -> SUCCEEDS
        del_resp2 = client.delete(f"/admin/departments/{dept_id}", headers=headers)
        assert del_resp2.status_code == 200
    finally:
        d = db_session.execute(select(Department).where(Department.id == dept_id)).scalar_one_or_none()
        if d:
            db_session.delete(d)
            db_session.commit()


def test_csv_export_sanitizes_formula_injection(client, super_admin_user, db_session):
    token = create_access_token(data={"sub": super_admin_user.email}, token_version=super_admin_user.token_version)
    headers = {"Authorization": f"Bearer {token}"}

    # Inject formula character in temporary user full name
    formula_email = f"formula_{int(datetime.now(timezone.utc).timestamp())}@knowxai.com"
    user = User(
        email=formula_email,
        username=f"formula_{int(datetime.now(timezone.utc).timestamp())}",
        full_name="=SUM(A1:A10)",
        role="Employee",
        department="IT Support",
        is_active=True,
    )
    db_session.add(user)
    db_session.commit()

    try:
        resp = client.get("/admin/reports/employees", headers=headers)
        assert resp.status_code == 200
        assert resp.headers["content-type"].startswith("text/csv")
        csv_text = resp.text
        # Ensure =SUM has been prefixed with single quote
        assert "'=SUM(A1:A10)" in csv_text
    finally:
        u = db_session.execute(select(User).where(User.email == formula_email)).scalar_one_or_none()
        if u:
            db_session.delete(u)
            db_session.commit()


def test_admin_login_success(client, super_admin_user):
    """Verify authorized Super Admin can authenticate via /auth/admin-login."""
    resp = client.post(
        "/auth/admin-login",
        json={"email": super_admin_user.email, "password": "SuperSecret123!"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert data["user"]["email"] == super_admin_user.email


def test_admin_login_invalid_password(client, super_admin_user):
    """Verify invalid password returns 401 Unauthorized."""
    resp = client.post(
        "/auth/admin-login",
        json={"email": super_admin_user.email, "password": "WrongPassword!"},
    )
    assert resp.status_code == 401
    assert "Invalid administrator" in resp.json()["detail"]


def test_admin_login_non_existent_account(client):
    """Verify non-existent administrator account returns 401 Unauthorized."""
    resp = client.post(
        "/auth/admin-login",
        json={"email": "nonexistent_admin@mkinfinite.com", "password": "AnyPassword123!"},
    )
    assert resp.status_code == 401
    assert "Invalid administrator" in resp.json()["detail"]


def test_admin_login_denies_normal_employee(client, employee_user):
    """Verify standard employee credentials are strictly blocked by /auth/admin-login with 403 Forbidden."""
    resp = client.post(
        "/auth/admin-login",
        json={"email": employee_user.email, "password": "EmpSecret123!"},
    )
    assert resp.status_code == 403
    assert "Access Denied" in resp.json()["detail"]
    assert "Super Admin" in resp.json()["detail"]


def test_standard_login_and_registration_remain_functional(client, db_session):
    """Verify existing standard login and registration flow continues to function perfectly."""
    ts = int(datetime.now(timezone.utc).timestamp())
    test_email = f"std_user_{ts}@knowxai.com"
    test_emp_id = f"STD-{ts % 10000}"

    # 1. Register new employee
    reg_resp = client.post(
        "/auth/register",
        json={
            "email": test_email,
            "password": "StdPassword123!",
            "full_name": "Standard Employee Test",
            "employee_id": test_emp_id,
            "department": "Human Resources",
        },
    )
    assert reg_resp.status_code == 200
    user_data = reg_resp.json()
    assert user_data["email"] == test_email
    assert user_data["role"] == "Employee"

    try:
        # 2. Standard Login
        login_resp = client.post(
            "/auth/login",
            json={"email": test_email, "password": "StdPassword123!"},
        )
        assert login_resp.status_code == 200
        token_data = login_resp.json()
        assert "access_token" in token_data

        # 3. Verify standard employee cannot access admin API
        admin_resp = client.get(
            "/admin/overview",
            headers={"Authorization": f"Bearer {token_data['access_token']}"},
        )
        assert admin_resp.status_code == 403
    finally:
        u = db_session.execute(select(User).where(User.email == test_email)).scalar_one_or_none()
        if u:
            db_session.delete(u)
            db_session.commit()

