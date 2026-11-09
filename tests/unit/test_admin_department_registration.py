"""Unit and regression tests for Admin Department option on registration."""

from __future__ import annotations

from datetime import datetime, timezone
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import func, select, text

from api.auth import create_access_token, hash_password
from api.main import create_app
from database.connection import SessionLocal, init_db
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


def test_admin_department_registration_and_no_privilege_escalation(client, db_session):
    """
    Verify:
    1. A user can register with department='Admin'.
    2. Department is normalized to 'Admin'.
    3. The role is strictly 'Employee' (no automatic admin privileges).
    4. Login works and returns valid token.
    5. The user is rejected from Admin Portal endpoints (403 Forbidden).
    """
    ts = int(datetime.now(timezone.utc).timestamp() * 1000)
    email = f"admin.dept.user_{ts}@knowxai.com"
    password = "SafePassword123!"
    emp_id = f"EMP-ADM-{ts % 100000}"

    reg_payload = {
        "email": email,
        "password": password,
        "full_name": "Admin Dept Employee",
        "employee_id": emp_id,
        "department": "Admin",
    }
    reg_resp = client.post("/auth/register", json=reg_payload)
    assert reg_resp.status_code == 200, reg_resp.text
    user_data = reg_resp.json()

    assert user_data["email"] == email
    assert user_data["department"] == "Admin"
    assert user_data["role"] == "Employee"

    # Login with credentials
    login_resp = client.post("/auth/login", json={"email": email, "password": password})
    assert login_resp.status_code == 200
    token_data = login_resp.json()
    token = token_data["access_token"]
    assert token

    # Attempt to access Admin Portal dashboard -> MUST BE FORBIDDEN (403)
    headers = {"Authorization": f"Bearer {token}"}
    admin_resp = client.get("/admin/dashboard", headers=headers)
    assert admin_resp.status_code == 403, "Department 'Admin' should not grant admin access"

    # Cleanup test user
    u = db_session.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if u:
        db_session.delete(u)
        db_session.commit()


def test_database_admin_department_idempotency_and_no_duplicates(db_session):
    """Verify Admin department exists and init_db() does not create duplicate records."""
    # Ensure init_db executes cleanly
    init_db()

    # Query all records matching code 'ADM' or name 'Admin'
    admin_depts = db_session.execute(
        select(Department).where((Department.code == "ADM") | (func.lower(Department.name) == "admin"))
    ).scalars().all()

    assert len(admin_depts) == 1, f"Expected exactly 1 Admin department, found {len(admin_depts)}"
    dept = admin_depts[0]
    assert dept.name == "Admin"
    assert dept.code == "ADM"
    assert dept.is_active is True

    # Re-run init_db again and verify still exactly 1
    init_db()
    admin_depts_after = db_session.execute(
        select(Department).where((Department.code == "ADM") | (func.lower(Department.name) == "admin"))
    ).scalars().all()
    assert len(admin_depts_after) == 1


def test_super_admin_unaffected_and_department_in_list(client, db_session):
    """Verify super_admin remains fully functional and Admin department appears in department list."""
    # 1. Super admin access
    ts = int(datetime.now(timezone.utc).timestamp() * 1000)
    email = f"sa_check_{ts}@knowxai.com"
    sa_user = User(
        email=email,
        username=f"sa_user_{ts}",
        full_name="Super Admin Check",
        hashed_password=hash_password("SuperSecret123!"),
        role="Super Admin",
        employee_id=f"EMP-SA-{ts % 100000}",
        department="Management",
        is_active=True,
        token_version=1,
    )
    db_session.add(sa_user)
    db_session.commit()
    db_session.refresh(sa_user)

    try:
        token = create_access_token(data={"sub": sa_user.email}, token_version=sa_user.token_version)
        headers = {"Authorization": f"Bearer {token}"}

        # Check dashboard
        dash_resp = client.get("/admin/dashboard", headers=headers)
        assert dash_resp.status_code == 200

        # Check departments list
        depts_resp = client.get("/admin/departments", headers=headers)
        assert depts_resp.status_code == 200
        dept_names = [d["name"] for d in depts_resp.json()]
        assert "Admin" in dept_names
        assert "IT Support" in dept_names
        assert "Human Resources" in dept_names
        assert "Finance & Claims" in dept_names
        assert "Project Department" in dept_names
        assert "Management" in dept_names
    finally:
        u = db_session.execute(select(User).where(User.id == sa_user.id)).scalar_one_or_none()
        if u:
            db_session.delete(u)
            db_session.commit()
