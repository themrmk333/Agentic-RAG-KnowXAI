"""Google OAuth/OIDC authentication routes.

Handles:
- Server-side verification of Google ID tokens using google.oauth2.id_token.
- Validates token signature, issuer, audience, expiration, and verified email status.
- Secure account linking: associates Google ID with existing accounts only when email is verified.
- Seamless account provisioning for first-time Google sign-ins.
- Issues standard project JWT tokens upon successful validation.
"""

from __future__ import annotations

import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.exc import DBAPIError, OperationalError
from sqlalchemy.orm import Session

from api.auth import create_access_token
from api.routes.auth import TokenResponseSchema, UserProfileSchema
from config.settings import get_settings
from database.connection import get_db
from database.models import User

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth/google", tags=["oauth"])


class GoogleLoginRequestSchema(BaseModel):
    """Schema for client-provided Google ID token (credential)."""
    credential: str = Field(
        ...,
        description="Google OIDC ID token returned by Google Sign-In button.",
    )


class GoogleConfigResponse(BaseModel):
    """Public configuration indicating whether Google Sign-In is enabled."""
    enabled: bool
    client_id: Optional[str] = None


@router.get("/config", response_model=GoogleConfigResponse)
def get_google_config():
    """Return public Google OAuth client ID if configured."""
    settings = get_settings()
    client_id = settings.google_client_id
    if client_id and client_id.strip() and not client_id.startswith("your-"):
        return GoogleConfigResponse(enabled=True, client_id=client_id.strip())
    return GoogleConfigResponse(enabled=False, client_id=None)


@router.post("", response_model=TokenResponseSchema)
def google_sign_in(
    data: GoogleLoginRequestSchema,
    db: Session = Depends(get_db),
):
    """Authenticate or register user via Google OIDC credential.
    
    Verifies ID token authenticity server-side with Google's public certificates.
    Requires email_verified == True before associating or provisioning accounts.
    """
    settings = get_settings()
    expected_client_id = settings.google_client_id

    if not expected_client_id or not expected_client_id.strip() or expected_client_id.startswith("your-"):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Google Sign-In is not configured on this server. Please contact an administrator.",
        )

    clean_credential = data.credential.strip()
    if not clean_credential:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Google credential token is missing or empty.",
        )

    # 1. Verify token signature, audience, and expiry with Google
    try:
        request_transport = google_requests.Request()
        id_info = id_token.verify_oauth2_token(
            clean_credential,
            request_transport,
            audience=expected_client_id.strip(),
        )
    except ValueError as ve:
        logger.warning(f"Google token verification failed: {ve}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Google authentication failed: {ve}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        logger.error(f"Unexpected error during Google token verification: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed to verify Google identity token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 2. Validate token claims
    google_user_id = id_info.get("sub")
    email = id_info.get("email")
    email_verified = id_info.get("email_verified", False)

    if not google_user_id or not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Google token payload missing required identity claims.",
        )

    if not email_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Google account email is not verified. Please verify your email with Google first.",
        )

    clean_email = email.strip().lower()
    full_name = id_info.get("name") or id_info.get("given_name") or clean_email.split("@")[0]

    try:
        # 3. Lookup user by Google ID first
        user = db.execute(
            select(User).where(User.google_id == google_user_id)
        ).scalar_one_or_none()

        if user:
            # Existing Google-linked user
            logger.info(f"Existing Google user logged in: {user.email} (Google ID: {google_user_id})")
        else:
            # 4. Check if an account already exists with the same email
            existing_email_user = db.execute(
                select(User).where(func.lower(User.email) == clean_email)
            ).scalar_one_or_none()

            if existing_email_user:
                # Safe link: email was verified by Google OIDC
                user = existing_email_user
                user.google_id = google_user_id
                if not user.full_name and full_name:
                    user.full_name = full_name
                db.commit()
                logger.info(f"Linked Google ID {google_user_id} to existing user account {user.email}")
            else:
                # 5. First-time registration via Google Sign-In
                # Generate unique username
                username_base = clean_email.split("@")[0].replace(".", "_")
                username = username_base
                counter = 1
                while db.execute(select(User).where(func.lower(User.username) == username.lower())).scalar_one_or_none():
                    username = f"{username_base}{counter}"
                    counter += 1

                # Generate employee ID from Google sub
                emp_id = f"EMP-G{google_user_id[:6].upper()}"

                user = User(
                    email=clean_email,
                    username=username,
                    full_name=full_name,
                    hashed_password=None,  # Passwordless OAuth account
                    role="Employee",
                    employee_id=emp_id,
                    department="IT Support",  # Default standard department
                    google_id=google_user_id,
                    auth_provider="google",
                )
                db.add(user)
                db.commit()
                db.refresh(user)
                logger.info(f"Created new user from Google Sign-In: {clean_email} (Employee ID: {emp_id})")

        # Check active status
        if getattr(user, "is_active", True) is False:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="This employee account has been deactivated. Please contact your company administrator.",
            )

        # Update last login timestamp
        from datetime import datetime, timezone
        from services.audit_service import log_audit_event
        now_dt = datetime.now(timezone.utc)
        user.last_login_at = now_dt
        db.commit()

        log_audit_event(
            db=db,
            action="USER_LOGIN_SUCCESS",
            actor=user,
            target_user=user,
            resource_type="AUTH",
            summary=f"Employee logged in via Google OAuth: {user.email}",
            status="SUCCESS",
        )

        # 6. Issue standard JWT token with token_version
        access_token = create_access_token(
            data={"sub": user.email},
            token_version=getattr(user, "token_version", 1),
        )
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": user,
        }

    except (OperationalError, DBAPIError) as db_exc:
        db.rollback()
        logger.error(f"Database error during Google sign-in: {db_exc}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database service is currently unavailable. Please try again shortly.",
        )
