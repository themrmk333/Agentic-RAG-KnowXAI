"""Authentication endpoints for registration, login, and user profile verification."""

import logging
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel, EmailStr, field_validator
from sqlalchemy import func, or_, select
from sqlalchemy.exc import DBAPIError, OperationalError
from sqlalchemy.orm import Session

from api.auth import create_access_token, get_current_user, hash_password, verify_password
from database.connection import get_db
from database.models import User

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])

# Standard enterprise supported departments
SUPPORTED_DEPARTMENTS = {
    "it": "IT Support",
    "it support": "IT Support",
    "hr": "Human Resources",
    "human resources": "Human Resources",
    "finance": "Finance & Claims",
    "finance & claims": "Finance & Claims",
    "project": "Project Department",
    "project department": "Project Department",
    "management": "Management",
}


def normalize_department(dept_raw: str) -> Optional[str]:
    """Validate and normalize department against enterprise supported departments."""
    if not dept_raw:
        return None
    key = dept_raw.strip().lower()
    return SUPPORTED_DEPARTMENTS.get(key)


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    employee_id: str
    department: str

    @field_validator("password")
    @classmethod
    def validate_password_length(cls, v: str) -> str:
        if len(v.strip()) < 4:
            raise ValueError("Password must be at least 4 characters long.")
        return v

    @field_validator("full_name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        name = v.strip()
        if not name:
            raise ValueError("Full name is required.")
        return name

    @field_validator("employee_id")
    @classmethod
    def validate_employee_id(cls, v: str) -> str:
        emp_id = v.strip()
        if not emp_id:
            raise ValueError("Employee ID is required.")
        return emp_id

    @field_validator("department")
    @classmethod
    def validate_dept(cls, v: str) -> str:
        norm = normalize_department(v)
        if not norm:
            raise ValueError(
                "Invalid department. Supported departments are: "
                "IT Support, Human Resources, Finance & Claims, Project Department, Management."
            )
        return norm


class UserLoginSchema(BaseModel):
    email: str
    password: str


class UserProfileSchema(BaseModel):
    id: int
    email: str
    username: str
    full_name: Optional[str]
    role: str
    employee_id: Optional[str]
    department: Optional[str]


class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str
    user: Optional[UserProfileSchema] = None


@router.post("/register", response_model=UserProfileSchema)
def register(data: UserRegisterSchema, db: Session = Depends(get_db)):
    """Register a new employee. Password will be securely hashed with bcrypt."""
    clean_email = data.email.strip().lower()
    clean_emp_id = data.employee_id.strip()

    try:
        # 1. Check if email already exists (case-insensitive)
        existing_email = db.execute(
            select(User).where(func.lower(User.email) == clean_email)
        ).scalar_one_or_none()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="An account with this email already exists.",
            )

        # 2. Check if employee_id already exists
        existing_emp = db.execute(
            select(User).where(User.employee_id == clean_emp_id)
        ).scalar_one_or_none()
        if existing_emp:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="An account with this Employee ID already exists.",
            )

        # 3. Generate unique username
        username_base = clean_email.split("@")[0]
        username = username_base
        counter = 1
        while db.execute(select(User).where(func.lower(User.username) == username.lower())).scalar_one_or_none():
            username = f"{username_base}{counter}"
            counter += 1

        # 4. Hash password securely
        hashed = hash_password(data.password)

        user = User(
            email=clean_email,
            username=username,
            full_name=data.full_name.strip(),
            hashed_password=hashed,
            employee_id=clean_emp_id,
            department=data.department,
            role="Employee",  # Default role
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        logger.info(f"Successfully registered new user: {clean_email} (Employee ID: {clean_emp_id})")
        return user

    except (OperationalError, DBAPIError) as db_exc:
        db.rollback()
        logger.error(f"Database error during registration: {db_exc}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database service is currently unavailable. Please try again shortly.",
        )


@router.post("/login", response_model=TokenResponseSchema)
async def login(
    request: Request,
    db: Session = Depends(get_db),
):
    """Authenticate employee and return JWT access token. Supports email, username, or Employee ID."""
    identifier = None
    password = None

    content_type = request.headers.get("content-type", "")
    if "application/json" in content_type:
        try:
            body = await request.json()
            identifier = body.get("email") or body.get("username") or body.get("employee_id") or body.get("identifier")
            password = body.get("password")
        except Exception:
            pass
    else:
        try:
            form_data = await request.form()
            identifier = form_data.get("username") or form_data.get("email") or form_data.get("employee_id")
            password = form_data.get("password")
        except Exception:
            pass

    if not identifier or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email/Employee ID and password are required.",
        )

    clean_identifier = str(identifier).strip()
    clean_lower = clean_identifier.lower()

    try:
        # Search for user across email (case-insensitive), employee_id, and username (case-insensitive)
        user = db.execute(
            select(User).where(
                or_(
                    func.lower(User.email) == clean_lower,
                    User.employee_id == clean_identifier,
                    func.lower(User.username) == clean_lower,
                )
            )
        ).scalar_one_or_none()

    except (OperationalError, DBAPIError) as db_exc:
        logger.error(f"Database error during login: {db_exc}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database service is currently unavailable. Please try again shortly.",
        )

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email, Employee ID, or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Issue token containing stable user email claim
    access_token = create_access_token(data={"sub": user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }


@router.get("/me", response_model=UserProfileSchema)
def get_me(current_user: User = Depends(get_current_user)):
    """Fetch current employee session user profile."""
    return current_user
