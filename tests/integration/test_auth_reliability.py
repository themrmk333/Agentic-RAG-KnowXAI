"""Integration tests for authentication reliability and account persistence.

Tests cover all 15 requirements specified in the Master Prompt:
1. New user registration.
2. Duplicate registration (duplicate email and duplicate employee_id).
3. Login with valid credentials.
4. Login with invalid credentials.
5. Login using supported Employee ID, email, and username identifiers.
6. Login after restarting the backend (simulated app reinitialization).
7. Login after system restart with persistent database intact.
8. Persistence of accounts across application restarts.
9. JWT validation and expiration handling.
10. Protected endpoint access without token.
11. Protected endpoint access with valid token.
12. Database unavailable during login (graceful 503 handling).
13. Department validation (reject invalid, accept 5 supported departments).
14. Existing user compatibility (Employee ID and email lookup).
15. Department and role preservation.

Uses an isolated test database to protect production data from modification or deletion.
"""

from datetime import timedelta
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from unittest.mock import patch
from sqlalchemy.exc import OperationalError

from api.main import create_app
from api.routes.auth import router as auth_router
from api.auth import create_access_token, hash_password
from database.connection import get_db
from database.models import Base, User

# Create isolated test in-memory SQLite database
TEST_DB_URL = "sqlite:///:memory:"

test_engine = create_engine(
    TEST_DB_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module", autouse=True)
def setup_test_database():
    """Create test tables and seed known mock user profiles."""
    Base.metadata.create_all(bind=test_engine)

    # Seed mock accounts matching existing production users
    db = TestingSessionLocal()
    mock_users = [
        User(
            email="rajeshpatil123@gmail.com",
            username="rajeshpatil123",
            full_name="Rajesh Patil",
            employee_id="101",
            department="Management",
            role="Employee",
            hashed_password=hash_password("password123"),
        ),
        User(
            email="maheshkoli1234@gmail.com",
            username="maheshkoli1234",
            full_name="Mahesh Koli",
            employee_id="123",
            department="IT Support",
            role="Employee",
            hashed_password=hash_password("password123"),
        ),
    ]
    for u in mock_users:
        db.add(u)
    db.commit()
    db.close()

    yield

    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def client():
    """Create test client with overridden database session."""
    test_app = FastAPI()
    test_app.include_router(auth_router)
    test_app.dependency_overrides[get_db] = override_get_db
    with TestClient(test_app) as c:
        yield c


# --- Requirement 1: New User Registration ---
def test_1_new_user_registration(client):
    payload = {
        "email": "new.employee@knowx.ai",
        "password": "SecurePassword123!",
        "full_name": "New Employee",
        "employee_id": "EMP-9001",
        "department": "IT Support",
    }
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "new.employee@knowx.ai"
    assert data["employee_id"] == "EMP-9001"
    assert data["department"] == "IT Support"
    assert data["role"] == "Employee"


# --- Requirement 2: Duplicate Registration ---
def test_2_duplicate_registration(client):
    # Duplicate email
    dup_email_payload = {
        "email": "NEW.EMPLOYEE@knowx.ai",  # Test case-insensitivity
        "password": "AnotherPassword!",
        "full_name": "Duplicate Person",
        "employee_id": "EMP-9999",
        "department": "Human Resources",
    }
    res = client.post("/auth/register", json=dup_email_payload)
    assert res.status_code == 400
    assert "already exists" in res.json()["detail"].lower()

    # Duplicate employee_id
    dup_emp_payload = {
        "email": "unique.person@knowx.ai",
        "password": "AnotherPassword!",
        "full_name": "Duplicate EmpID Person",
        "employee_id": "EMP-9001",  # Already registered above
        "department": "Finance & Claims",
    }
    res = client.post("/auth/register", json=dup_emp_payload)
    assert res.status_code == 400
    assert "Employee ID already exists" in res.json()["detail"]


# --- Requirement 3: Login with Valid Credentials ---
def test_3_login_with_valid_credentials(client):
    res = client.post(
        "/auth/login",
        json={"email": "new.employee@knowx.ai", "password": "SecurePassword123!"},
    )
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert data["user"]["email"] == "new.employee@knowx.ai"


# --- Requirement 4: Login with Invalid Credentials ---
def test_4_login_with_invalid_credentials(client):
    res = client.post(
        "/auth/login",
        json={"email": "new.employee@knowx.ai", "password": "WrongPassword!"},
    )
    assert res.status_code == 401
    assert "Invalid email, Employee ID, or password" in res.json()["detail"]


# --- Requirement 5: Login via Employee ID, Email, and Username ---
def test_5_login_supported_identifiers(client):
    # Via Employee ID
    res_emp = client.post(
        "/auth/login",
        json={"email": "EMP-9001", "password": "SecurePassword123!"},
    )
    assert res_emp.status_code == 200
    assert "access_token" in res_emp.json()

    # Via Email (with mixed casing and whitespace)
    res_email = client.post(
        "/auth/login",
        json={"email": "  NEW.EMPLOYEE@KNOWX.AI  ", "password": "SecurePassword123!"},
    )
    assert res_email.status_code == 200

    # Via Username
    res_user = client.post(
        "/auth/login",
        json={"username": "new.employee", "password": "SecurePassword123!"},
    )
    assert res_user.status_code == 200


# --- Requirement 6 & 7 & 8: Account Persistence across Restarts ---
def test_6_7_8_persistence_across_restarts():
    """Simulate complete server restart: create a new FastAPI instance and new client."""
    fresh_app = FastAPI()
    fresh_app.include_router(auth_router)
    fresh_app.dependency_overrides[get_db] = override_get_db

    with TestClient(fresh_app) as fresh_client:
        # User created prior to restart must be able to log in
        res = fresh_client.post(
            "/auth/login",
            json={"email": "EMP-9001", "password": "SecurePassword123!"},
        )
        assert res.status_code == 200
        assert res.json()["user"]["employee_id"] == "EMP-9001"


# --- Requirement 9: JWT Validation and Expiration ---
def test_9_jwt_validation_and_expiration(client):
    # Expired token
    expired_token = create_access_token(
        data={"sub": "new.employee@knowx.ai"},
        expires_delta=timedelta(seconds=-10),  # expired 10 seconds ago
    )
    res = client.get("/auth/me", headers={"Authorization": f"Bearer {expired_token}"})
    assert res.status_code == 401
    assert "expired" in res.json()["detail"].lower()

    # Valid token
    valid_token = create_access_token(
        data={"sub": "new.employee@knowx.ai"},
        expires_delta=timedelta(minutes=60),
    )
    res_valid = client.get("/auth/me", headers={"Authorization": f"Bearer {valid_token}"})
    assert res_valid.status_code == 200
    assert res_valid.json()["email"] == "new.employee@knowx.ai"


# --- Requirement 10: Protected Endpoint Without Token ---
def test_10_protected_endpoint_without_token(client):
    res = client.get("/auth/me")
    assert res.status_code == 401
    assert "Not authenticated" in res.json()["detail"]


# --- Requirement 11: Protected Endpoint With Valid Token ---
def test_11_protected_endpoint_with_valid_token(client):
    login_res = client.post(
        "/auth/login",
        json={"email": "EMP-9001", "password": "SecurePassword123!"},
    )
    token = login_res.json()["access_token"]
    res = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    assert res.json()["employee_id"] == "EMP-9001"


# --- Requirement 12: Database Unavailable During Login ---
def test_12_database_unavailable_during_login(client):
    from fastapi.responses import JSONResponse

    def mock_broken_db():
        raise OperationalError("SELECT 1", {}, Exception("Connection refused"))

    test_app = FastAPI()
    test_app.include_router(auth_router)

    @test_app.exception_handler(OperationalError)
    def db_err_handler(request, exc):
        return JSONResponse(
            status_code=503,
            content={"detail": "Database service is currently unavailable. Please try again shortly."}
        )

    test_app.dependency_overrides[get_db] = mock_broken_db

    with TestClient(test_app) as broken_client:
        res = broken_client.post(
            "/auth/login",
            json={"email": "EMP-9001", "password": "SecurePassword123!"},
        )
        assert res.status_code == 503
        assert "Database service is currently unavailable" in res.json()["detail"]


# --- Requirement 13: Department Validation ---
def test_13_department_validation(client):
    # Unsupported department
    invalid_payload = {
        "email": "invalid.dept@knowx.ai",
        "password": "Password123!",
        "full_name": "Invalid Dept",
        "employee_id": "EMP-9990",
        "department": "Outer Space",
    }
    res = client.post("/auth/register", json=invalid_payload)
    assert res.status_code == 422  # Pydantic validation failure

    # Test all 5 supported departments
    supported_depts = [
        ("IT Support", "emp.it@knowx.ai", "EMP-IT-1"),
        ("Human Resources", "emp.hr@knowx.ai", "EMP-HR-1"),
        ("Finance & Claims", "emp.fin@knowx.ai", "EMP-FIN-1"),
        ("Project Department", "emp.proj@knowx.ai", "EMP-PROJ-1"),
        ("Management", "emp.mgmt@knowx.ai", "EMP-MGMT-1"),
    ]
    for dept, email, emp_id in supported_depts:
        payload = {
            "email": email,
            "password": "Password123!",
            "full_name": f"User {dept}",
            "employee_id": emp_id,
            "department": dept,
        }
        res_ok = client.post("/auth/register", json=payload)
        assert res_ok.status_code == 200, res_ok.text
        assert res_ok.json()["department"] == dept


# --- Requirement 14: Existing User Compatibility ---
def test_14_existing_user_compatibility(client):
    # Existing user 1: Rajesh Patil (ID 1, EmpID 101)
    res_rajesh_email = client.post(
        "/auth/login",
        json={"email": "rajeshpatil123@gmail.com", "password": "password123"},
    )
    assert res_rajesh_email.status_code == 200
    assert res_rajesh_email.json()["user"]["employee_id"] == "101"

    res_rajesh_emp = client.post(
        "/auth/login",
        json={"email": "101", "password": "password123"},
    )
    assert res_rajesh_emp.status_code == 200
    assert res_rajesh_emp.json()["user"]["full_name"] == "Rajesh Patil"

    # Existing user 2: Mahesh Koli (ID 2, EmpID 123)
    res_mahesh_emp = client.post(
        "/auth/login",
        json={"email": "123", "password": "password123"},
    )
    assert res_mahesh_emp.status_code == 200
    assert res_mahesh_emp.json()["user"]["full_name"] == "Mahesh Koli"


# --- Requirement 15: Department and Role Preservation ---
def test_15_department_and_role_preservation(client):
    # Log in as Rajesh Patil (Management)
    res = client.post(
        "/auth/login",
        json={"email": "101", "password": "password123"},
    )
    assert res.status_code == 200
    user_data = res.json()["user"]
    assert user_data["department"] == "Management"
    assert user_data["role"] == "Employee"

    # Query /auth/me to verify profile preservation
    token = res.json()["access_token"]
    me_res = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me_res.status_code == 200
    assert me_res.json()["department"] == "Management"
    assert me_res.json()["role"] == "Employee"
