import logging
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

import bcrypt
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session

from config.settings import get_settings
from database.connection import get_db
from database.models import User

logger = logging.getLogger(__name__)

settings = get_settings()
JWT_SECRET_KEY = settings.jwt_secret_key.get_secret_value()
JWT_ALGORITHM = settings.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login", auto_error=False)


def hash_password(password: str) -> str:
    """Hash password securely using bcrypt."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify standard plain-text password matches hashed value."""
    if not plain_password or not hashed_password:
        return False
    try:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except Exception as e:
        logger.warning(f"Password verification encountered error: {e}")
        return False


def normalize_role(role: Optional[str]) -> str:
    """Normalize role strings across variations (e.g. 'super_admin', 'Super Admin', 'Admin', 'Employee')."""
    if not role:
        return "employee"
    r = role.strip().lower().replace(" ", "_").replace("-", "_")
    if r in ("super_admin", "superadmin", "owner", "super_administrator"):
        return "super_admin"
    if r in ("admin", "administrator"):
        return "admin"
    if r in ("manager", "dept_manager", "lead"):
        return "manager"
    return "employee"


def create_access_token(
    data: Dict[str, Any],
    expires_delta: Optional[timedelta] = None,
    token_version: Optional[int] = None,
) -> str:
    """Generate JWT access token with stable secret and configurable expiration."""
    to_encode = data.copy()
    now_utc = datetime.now(timezone.utc)
    if expires_delta:
        expire = now_utc + expires_delta
    else:
        expire = now_utc + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    if token_version is not None and "token_version" not in to_encode:
        to_encode["token_version"] = token_version
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


async def get_current_user(
    token: Optional[str] = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    """FastAPI dependency to extract and validate current authenticated user."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        email: Optional[str] = payload.get("sub")
        if email is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session token has expired. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise credentials_exception

    user = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if user is None:
        raise credentials_exception

    # Enforce account active status
    if getattr(user, "is_active", True) is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Your employee account has been deactivated. Please contact your company administrator.",
        )

    # Enforce session / token revocation via token_version check
    token_ver = payload.get("token_version")
    if token_ver is not None and getattr(user, "token_version", None) is not None:
        if token_ver != user.token_version:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session token has been revoked. Please log in again.",
                headers={"WWW-Authenticate": "Bearer"},
            )

    return user


async def require_admin(current_user: User = Depends(get_current_user)) -> User:
    """FastAPI dependency verifying current user possesses Admin or Super Admin role."""
    norm = normalize_role(current_user.role)
    if norm not in ("admin", "super_admin"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator privileges required to access this resource.",
        )
    return current_user


async def require_super_admin(current_user: User = Depends(get_current_user)) -> User:
    """FastAPI dependency verifying current user possesses Super Admin (Company Owner) role."""
    norm = normalize_role(current_user.role)
    if norm != "super_admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Super Administrator privileges required to perform this operation.",
        )
    return current_user


# Backward-compatible alias for existing endpoints and tests
get_admin_user = require_admin
