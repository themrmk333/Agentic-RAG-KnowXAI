"""API routes for Biometric Authentication (Face Login & Enrollment).

Provides:
- Secure Face Enrollment with mandatory explicit user consent.
- 1-to-1 Facial Verification against encrypted template at rest.
- Account lockout after 5 consecutive failed attempts.
- Biometric status, enable/disable toggle, and permanent deletion.
- In-memory request throttling to deter automated brute-force attacks.
"""

from __future__ import annotations

import logging
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from pydantic import BaseModel, Field
from sqlalchemy import func, or_, select
from sqlalchemy.exc import DBAPIError, OperationalError
from sqlalchemy.orm import Session

from api.auth import create_access_token, get_current_user, normalize_role
from api.routes.auth import TokenResponseSchema, UserProfileSchema
from database.connection import get_db
from database.models import BiometricCredential, User
from services.audit_service import log_audit_event
from services.biometric_service import (
    BiometricLockoutError,
    BiometricSecurityError,
    BiometricService,
    get_biometric_service,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth/biometrics", tags=["biometrics"])

# In-memory rate limiting: max 10 verification requests per minute per IP/identifier
_RATE_LIMIT_WINDOW_SECONDS = 60
_MAX_REQUESTS_PER_WINDOW = 10
_request_timestamps: Dict[str, List[float]] = defaultdict(list)


def _check_rate_limit(key: str) -> None:
    """Enforce basic sliding-window rate limiting in memory."""
    now = time.time()
    timestamps = _request_timestamps[key]
    # Prune old timestamps
    cutoff = now - _RATE_LIMIT_WINDOW_SECONDS
    _request_timestamps[key] = [t for t in timestamps if t > cutoff]
    if len(_request_timestamps[key]) >= _MAX_REQUESTS_PER_WINDOW:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many authentication attempts. Please wait a minute and try again.",
        )
    _request_timestamps[key].append(now)


# ============================================================================
# Request / Response Schemas
# ============================================================================

class BiometricEnrollSchema(BaseModel):
    """Schema for enrolling a face biometric template."""
    image_base64: str = Field(..., description="Base64 encoded webcam probe image (JPEG/PNG).")
    burst_frames: Optional[List[str]] = Field(
        default=None,
        description="Optional sequential frames for burst motion anti-spoofing verification.",
    )
    consent_given: bool = Field(
        ...,
        description="Explicit user consent acknowledging storage of encrypted biometric templates.",
    )


class BiometricVerifySchema(BaseModel):
    """Schema for authenticating via Face Login."""
    identifier: str = Field(
        ...,
        description="Claimed account identifier (email, employee ID, or username).",
    )
    image_base64: str = Field(
        ...,
        description="Base64 encoded live probe frame from webcam.",
    )
    burst_frames: Optional[List[str]] = Field(
        default=None,
        description="Optional secondary frames for burst motion checking.",
    )


class BiometricAdminVerifySchema(BaseModel):
    """Schema for authenticating a corporate Super Admin via Face Login."""
    identifier: Optional[str] = Field(
        default=None,
        description="Optional claimed administrator identifier (email, employee ID, or username). If omitted, 1:N matching across enrolled Super Admins is performed.",
    )
    image_base64: str = Field(
        ...,
        description="Base64 encoded live probe frame from webcam.",
    )
    burst_frames: Optional[List[str]] = Field(
        default=None,
        description="Optional secondary frames for burst motion checking.",
    )


class BiometricToggleSchema(BaseModel):
    """Schema for enabling or disabling biometric login."""
    is_enabled: bool = Field(..., description="Enable or disable Face Login.")


class BiometricStatusResponse(BaseModel):
    """Public/private status of biometric enrollment."""
    is_enrolled: bool
    is_enabled: bool
    enrolled_at: Optional[datetime] = None
    last_used_at: Optional[datetime] = None
    failed_attempts: int = 0
    is_locked: bool = False
    lockout_remaining_seconds: Optional[int] = None
    template_version: Optional[str] = None


class BiometricActionResponse(BaseModel):
    """Standard acknowledgment response for biometric mutations."""
    success: bool
    message: str


# ============================================================================
# API Endpoints
# ============================================================================

@router.post("/enroll", response_model=BiometricActionResponse)
def enroll_face(
    data: BiometricEnrollSchema,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    service: BiometricService = Depends(get_biometric_service),
):
    """Enroll or update the current user's facial biometric template.
    
    Requires explicit user consent and extracts a 512-d feature vector that is
    encrypted at rest with AES-256-GCM bound to the user's ID.
    Raw image data is processed in memory and never stored.
    """
    if not data.consent_given:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Explicit user consent is mandatory for biometric face enrollment under data privacy policies.",
        )

    try:
        # Extract normalized embedding and validate heuristics
        embedding, diagnostics = service.process_and_extract(
            primary_image_base64=data.image_base64,
            burst_images_base64=data.burst_frames,
            enforce_heuristics=True,
        )

        # Encrypt vector bound to current_user.id
        encrypted_template = service.encryption.encrypt_vector(embedding, user_id=current_user.id)

        # Check for existing biometric credential
        cred = db.execute(
            select(BiometricCredential).where(BiometricCredential.user_id == current_user.id)
        ).scalar_one_or_none()

        now_utc = datetime.now(timezone.utc)
        if cred:
            cred.encrypted_template = encrypted_template
            cred.template_version = service.engine.version_tag
            cred.is_enabled = True
            cred.failed_attempts = 0
            cred.locked_until = None
            cred.enrolled_at = now_utc
        else:
            cred = BiometricCredential(
                user_id=current_user.id,
                encrypted_template=encrypted_template,
                template_version=service.engine.version_tag,
                is_enabled=True,
                failed_attempts=0,
                locked_until=None,
                enrolled_at=now_utc,
            )
            db.add(cred)

        db.commit()
        logger.info(f"Successfully enrolled biometric profile for user {current_user.email} (ID: {current_user.id})")
        return BiometricActionResponse(
            success=True,
            message="Facial biometric profile successfully enrolled and encrypted at rest.",
        )

    except BiometricSecurityError as sec_err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Biometric enrollment rejected: {sec_err}",
        )
    except (OperationalError, DBAPIError) as db_exc:
        db.rollback()
        logger.error(f"Database error during biometric enrollment: {db_exc}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database service is currently unavailable. Please try again shortly.",
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Unexpected error during biometric enrollment: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to complete biometric enrollment.",
        )


@router.post("/verify", response_model=TokenResponseSchema)
def verify_face_login(
    request: Request,
    data: BiometricVerifySchema,
    db: Session = Depends(get_db),
    service: BiometricService = Depends(get_biometric_service),
):
    """Authenticate a claimed user via 1-to-1 Face Login.
    
    Validates anti-spoofing heuristics, verifies claimed user's enrolled template,
    enforces 5-attempt lockout, and issues standard JWT access token on match.
    """
    clean_identifier = data.identifier.strip()
    if not clean_identifier:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Claimed account identifier is required.",
        )

    # Rate limiting by client IP and identifier
    client_ip = request.client.host if request.client else "unknown"
    _check_rate_limit(f"{client_ip}:{clean_identifier}")

    clean_lower = clean_identifier.lower()

    # 1. Lookup claimed user
    user = db.execute(
        select(User).where(
            or_(
                func.lower(User.email) == clean_lower,
                User.employee_id == clean_identifier,
                func.lower(User.username) == clean_lower,
            )
        )
    ).scalar_one_or_none()

    if not user:
        # Generic error message to prevent account enumeration
        logger.warning(f"Face login attempted for non-existent identifier: {clean_identifier}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed. Face not recognized or account not enrolled.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 2. Lookup enrolled biometric credential
    cred = db.execute(
        select(BiometricCredential).where(BiometricCredential.user_id == user.id)
    ).scalar_one_or_none()

    if not cred or not cred.is_enabled:
        logger.warning(f"Face login attempted for user {user.email} with no enabled biometric credential")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed. Face login is not enabled for this account.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 2b. Audit template model version compatibility
    if cred.template_version != service.engine.version_tag:
        logger.warning(
            f"Biometric template version mismatch for user {user.email}: "
            f"credential version '{cred.template_version}' vs engine '{service.engine.version_tag}'"
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Biometric profile requires re-enrollment: The facial recognition engine has been upgraded to a "
                f"high-accuracy FaceNet model ('{service.engine.version_tag}'). "
                "Your existing face profile was enrolled under an earlier model version. "
                "Please log in using your User ID and password, then re-enroll your face."
            ),
        )

    now_utc = datetime.now(timezone.utc)

    # 3. Check account lockout status
    if cred.locked_until:
        # Standardize timezone comparison
        locked_until_dt = cred.locked_until
        if locked_until_dt.tzinfo is None:
            locked_until_dt = locked_until_dt.replace(tzinfo=timezone.utc)

        if locked_until_dt > now_utc:
            remaining = int((locked_until_dt - now_utc).total_seconds())
            remaining_mins = max(1, remaining // 60)
            logger.warning(f"Locked account {user.email} attempted face login ({remaining}s remaining)")
            raise HTTPException(
                status_code=status.HTTP_423_LOCKED,
                detail=f"Biometric authentication is temporarily locked due to multiple failed attempts. Please use password login or try again in {remaining_mins} minute(s).",
            )
        else:
            # Lockout expired, reset counter
            cred.locked_until = None
            cred.failed_attempts = 0
            db.commit()

    # 4. Extract probe embedding and check heuristics
    try:
        probe_vector, diagnostics = service.process_and_extract(
            primary_image_base64=data.image_base64,
            burst_images_base64=data.burst_frames,
            enforce_heuristics=True,
        )
    except BiometricSecurityError as sec_err:
        logger.warning(f"Heuristic/quality check failed during face login for user {user.email}: {sec_err}")
        # Count quality/spoof failures toward lockout
        cred.failed_attempts += 1
        if cred.failed_attempts >= 5:
            cred.locked_until = now_utc + timedelta(minutes=15)
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Face verification failed: {sec_err}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        logger.error(f"Error extracting face probe: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid face image payload.",
        )

    # 5. One-to-one cosine similarity verification
    try:
        is_matched, score, threshold = service.verify_probe(
            probe_vector=probe_vector,
            encrypted_template=cred.encrypted_template,
            user_id=user.id,
        )
    except Exception as e:
        logger.error(f"Biometric verification error for user {user.email}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to verify biometric template.",
        )

    if not is_matched:
        cred.failed_attempts += 1
        if cred.failed_attempts >= 5:
            cred.locked_until = now_utc + timedelta(minutes=15)
            db.commit()
            logger.warning(f"User {user.email} reached max failed biometric attempts. Locked for 15 minutes.")
            raise HTTPException(
                status_code=status.HTTP_423_LOCKED,
                detail="Biometric authentication is now locked due to multiple failed attempts. Please use password login.",
            )
        db.commit()
        attempts_left = 5 - cred.failed_attempts
        logger.warning(f"Face verification mismatch for user {user.email} (score: {score}, threshold: {threshold})")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Face does not match the enrolled profile. ({attempts_left} attempts remaining)",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Check active status
    if getattr(user, "is_active", True) is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This employee account has been deactivated. Please contact your company administrator.",
        )

    # 6. Verification Success! Reset lockout counters and update last_used_at
    cred.failed_attempts = 0
    cred.locked_until = None
    cred.last_used_at = now_utc
    user.last_login_at = now_utc
    user.failed_login_attempts = 0
    user.locked_until = None
    db.commit()

    from services.audit_service import log_audit_event
    log_audit_event(
        db=db,
        action="USER_LOGIN_SUCCESS",
        actor=user,
        target_user=user,
        resource_type="AUTH",
        summary=f"Employee logged in via Face ID biometric verification: {user.email}",
        status="SUCCESS",
    )

    logger.info(f"Face login successful for user {user.email} (score: {score})")
    access_token = create_access_token(
        data={"sub": user.email},
        token_version=getattr(user, "token_version", 1),
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }


@router.post("/admin-verify", response_model=TokenResponseSchema)
def verify_admin_face_login(
    request: Request,
    data: BiometricAdminVerifySchema,
    db: Session = Depends(get_db),
    service: BiometricService = Depends(get_biometric_service),
):
    """Authenticate corporate Super Admin via Face ID verification.
    
    Strictly verifies super_admin role server-side.
    Standard employees attempting to authenticate receive a 403 Forbidden access denial.
    Supports 1:1 verification when identifier is provided, or 1:N matching among enrolled Super Admins when omitted.
    """
    client_ip = request.client.host if request.client else "unknown"
    clean_identifier = data.identifier.strip() if data.identifier else None
    _check_rate_limit(f"admin_face:{client_ip}:{clean_identifier or '1_to_n'}")

    # 1. Extract probe embedding & check anti-spoofing heuristics
    try:
        probe_vector, diagnostics = service.process_and_extract(
            primary_image_base64=data.image_base64,
            burst_images_base64=data.burst_frames,
            enforce_heuristics=True,
        )
    except BiometricSecurityError as sec_err:
        logger.warning(f"Super Admin face probe heuristic check failed: {sec_err}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Face verification failed: {sec_err}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        logger.error(f"Error extracting face probe: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid face image payload.",
        )

    now_utc = datetime.now(timezone.utc)

    matched_user: Optional[User] = None
    matched_cred: Optional[BiometricCredential] = None

    if clean_identifier:
        # 1-to-1 Super Admin verification with claimed identifier
        clean_lower = clean_identifier.lower()
        user = db.execute(
            select(User).where(
                or_(
                    func.lower(User.email) == clean_lower,
                    User.employee_id == clean_identifier,
                    func.lower(User.username) == clean_lower,
                )
            )
        ).scalar_one_or_none()

        if not user:
            logger.warning(f"Admin face login attempted for non-existent account: {clean_identifier}")
            log_audit_event(
                db=db,
                action="ADMIN_LOGIN_FAILED",
                resource_type="AUTH",
                summary=f"Admin face login failed: Account '{clean_identifier}' not found",
                status="FAILED",
                ip_address=client_ip,
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid administrator credentials or account not found.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        if getattr(user, "is_active", True) is False:
            log_audit_event(
                db=db,
                action="ADMIN_LOGIN_FAILED",
                target_user=user,
                resource_type="AUTH",
                summary=f"Admin face login blocked for deactivated account: {user.email}",
                status="FAILED",
                ip_address=client_ip,
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="This administrator account has been deactivated. Please contact MK Infinite IT administration.",
            )

        # STRICT ROLE ENFORCEMENT: Standard employees are strictly blocked with 403 Forbidden
        norm_role = normalize_role(user.role)
        if norm_role != "super_admin":
            log_audit_event(
                db=db,
                action="ADMIN_LOGIN_DENIED_UNAUTHORIZED_ROLE",
                actor=user,
                target_user=user,
                resource_type="SECURITY",
                summary=f"Unauthorized admin face login attempt: User {user.email} with role '{user.role}' is not a Super Admin",
                status="ALERT",
                ip_address=client_ip,
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access Denied: This administrative portal is strictly reserved for authorized MK Infinite Company Owners & Super Admins only. Standard employee credentials are not permitted.",
            )

        cred = db.execute(
            select(BiometricCredential).where(BiometricCredential.user_id == user.id)
        ).scalar_one_or_none()

        if not cred or not cred.is_enabled:
            logger.warning(f"Admin face login attempted for Super Admin {user.email} without active biometrics")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication failed. Face login is not enrolled or enabled for this Super Admin account.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Audit template model version compatibility for Super Admin
        if cred.template_version != service.engine.version_tag:
            logger.warning(
                f"Super Admin biometric template version mismatch for {user.email}: "
                f"credential version '{cred.template_version}' vs engine '{service.engine.version_tag}'"
            )
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Biometric profile requires re-enrollment: The face recognition engine has been upgraded to a "
                    f"high-accuracy FaceNet model ('{service.engine.version_tag}'). "
                    "Your enrolled Super Admin face profile was created under an earlier model version. "
                    "Please log in with your Super Admin password, then re-enroll your biometric face profile."
                ),
            )

        if cred.locked_until:
            locked_until_dt = cred.locked_until
            if locked_until_dt.tzinfo is None:
                locked_until_dt = locked_until_dt.replace(tzinfo=timezone.utc)

            if locked_until_dt > now_utc:
                remaining = int((locked_until_dt - now_utc).total_seconds())
                remaining_mins = max(1, remaining // 60)
                raise HTTPException(
                    status_code=status.HTTP_423_LOCKED,
                    detail=f"Biometric authentication is temporarily locked due to multiple failed attempts. Please use password login or retry in {remaining_mins} minute(s).",
                )
            else:
                cred.locked_until = None
                cred.failed_attempts = 0
                db.commit()

        try:
            is_matched, score, threshold = service.verify_probe(
                probe_vector=probe_vector,
                encrypted_template=cred.encrypted_template,
                user_id=user.id,
            )
        except Exception as e:
            logger.error(f"Biometric verification error for Super Admin {user.email}: {e}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to verify biometric template.",
            )

        if not is_matched:
            cred.failed_attempts += 1
            if cred.failed_attempts >= 5:
                cred.locked_until = now_utc + timedelta(minutes=15)
                db.commit()
                log_audit_event(
                    db=db,
                    action="USER_ACCOUNT_LOCKED",
                    target_user=user,
                    resource_type="SECURITY",
                    summary=f"Super Admin account locked for 15 minutes following 5 failed biometric attempts ({user.email})",
                    status="ALERT",
                    ip_address=client_ip,
                )
                raise HTTPException(
                    status_code=status.HTTP_423_LOCKED,
                    detail="Biometric authentication is now locked due to multiple failed attempts. Please use password login.",
                )
            db.commit()
            attempts_left = 5 - cred.failed_attempts
            logger.warning(f"Face verification mismatch for Super Admin {user.email} (score: {score})")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Face does not match the enrolled Super Admin profile. ({attempts_left} attempts remaining)",
                headers={"WWW-Authenticate": "Bearer"},
            )

        matched_user = user
        matched_cred = cred

    else:
        # 1-to-N matching across all active Super Admins with enrolled biometrics
        candidates = db.execute(
            select(User, BiometricCredential)
            .join(BiometricCredential, BiometricCredential.user_id == User.id)
            .where(
                User.is_active == True,
                BiometricCredential.is_enabled == True,
            )
        ).all()

        super_admins = [
            (u, c) for u, c in candidates
            if normalize_role(u.role) == "super_admin"
        ]

        if not super_admins:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication failed. No Super Admin accounts have biometric Face ID enrolled. Please log in with User ID and Password.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Filter out candidates with incompatible template versions to avoid comparing vectors across different models
        compatible_super_admins = [
            (u, c) for u, c in super_admins
            if c.template_version == service.engine.version_tag
        ]

        if not compatible_super_admins:
            logger.info("No Super Admin profiles found matching current template version")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication failed. Face not recognized or account not enrolled. Please log in with User ID and Password.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        best_user: Optional[User] = None
        best_cred: Optional[BiometricCredential] = None
        best_score = -1.0

        for admin_user, admin_cred in compatible_super_admins:
            if admin_cred.locked_until:
                locked_dt = admin_cred.locked_until
                if locked_dt.tzinfo is None:
                    locked_dt = locked_dt.replace(tzinfo=timezone.utc)
                if locked_dt > now_utc:
                    continue
                else:
                    admin_cred.locked_until = None
                    admin_cred.failed_attempts = 0
                    db.commit()

            try:
                is_matched, score, threshold = service.verify_probe(
                    probe_vector=probe_vector,
                    encrypted_template=admin_cred.encrypted_template,
                    user_id=admin_user.id,
                )
                if is_matched and score > best_score:
                    best_score = score
                    best_user = admin_user
                    best_cred = admin_cred
            except Exception as match_err:
                logger.warning(f"Error checking biometric vector for admin {admin_user.email}: {match_err}")
                continue

        if not best_user or not best_cred:
            log_audit_event(
                db=db,
                action="ADMIN_LOGIN_FAILED",
                resource_type="AUTH",
                summary="Super Admin Face Login failed: Probe face does not match any enrolled Super Admin profile",
                status="FAILED",
                ip_address=client_ip,
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Face not recognized. Probe face does not match any enrolled Super Admin profile.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        matched_user = best_user
        matched_cred = best_cred

    # Reset counters and record login for authenticated Super Admin
    matched_cred.failed_attempts = 0
    matched_cred.locked_until = None
    matched_cred.last_used_at = now_utc
    matched_user.failed_login_attempts = 0
    matched_user.locked_until = None
    matched_user.last_login_at = now_utc
    db.commit()

    log_audit_event(
        db=db,
        action="SUPER_ADMIN_LOGIN_SUCCESS",
        actor=matched_user,
        target_user=matched_user,
        resource_type="AUTH",
        summary=f"Super Admin authenticated successfully: {matched_user.email} (Method: Face ID Biometrics)",
        status="SUCCESS",
        ip_address=client_ip,
    )

    access_token = create_access_token(
        data={"sub": matched_user.email},
        token_version=getattr(matched_user, "token_version", 1),
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": matched_user,
    }


@router.get("/status", response_model=BiometricStatusResponse)
def get_biometric_status(
    identifier: Optional[str] = Query(default=None, description="Optional email/employee ID for login lookup"),
    current_user: Optional[User] = Depends(lambda: None),
    db: Session = Depends(get_db),
):
    """Retrieve biometric enrollment status.
    
    If invoked with an active session token, returns the authenticated user's detailed status.
    If invoked with an identifier query param (from login screen), returns public enrollment flags.
    """
    target_user: Optional[User] = None

    if identifier:
        clean_id = identifier.strip()
        clean_lower = clean_id.lower()
        target_user = db.execute(
            select(User).where(
                or_(
                    func.lower(User.email) == clean_lower,
                    User.employee_id == clean_id,
                    func.lower(User.username) == clean_lower,
                )
            )
        ).scalar_one_or_none()
    elif current_user:
        target_user = current_user

    if not target_user:
        return BiometricStatusResponse(
            is_enrolled=False,
            is_enabled=False,
        )

    cred = db.execute(
        select(BiometricCredential).where(BiometricCredential.user_id == target_user.id)
    ).scalar_one_or_none()

    if not cred:
        return BiometricStatusResponse(
            is_enrolled=False,
            is_enabled=False,
        )

    now_utc = datetime.now(timezone.utc)
    is_locked = False
    lockout_remaining: Optional[int] = None

    if cred.locked_until:
        locked_dt = cred.locked_until
        if locked_dt.tzinfo is None:
            locked_dt = locked_dt.replace(tzinfo=timezone.utc)
        if locked_dt > now_utc:
            is_locked = True
            lockout_remaining = int((locked_dt - now_utc).total_seconds())

    return BiometricStatusResponse(
        is_enrolled=True,
        is_enabled=cred.is_enabled,
        enrolled_at=cred.enrolled_at,
        last_used_at=cred.last_used_at,
        failed_attempts=cred.failed_attempts,
        is_locked=is_locked,
        lockout_remaining_seconds=lockout_remaining,
        template_version=cred.template_version,
    )


@router.post("/toggle", response_model=BiometricStatusResponse)
def toggle_biometric_login(
    data: BiometricToggleSchema,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Enable or disable biometric face login for the current authenticated user."""
    cred = db.execute(
        select(BiometricCredential).where(BiometricCredential.user_id == current_user.id)
    ).scalar_one_or_none()

    if not cred:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No biometric credential found. Please enroll your face first.",
        )

    cred.is_enabled = data.is_enabled
    db.commit()
    db.refresh(cred)

    logger.info(f"User {current_user.email} changed biometric is_enabled to {data.is_enabled}")
    return BiometricStatusResponse(
        is_enrolled=True,
        is_enabled=cred.is_enabled,
        enrolled_at=cred.enrolled_at,
        last_used_at=cred.last_used_at,
        failed_attempts=cred.failed_attempts,
        template_version=cred.template_version,
    )


@router.delete("", response_model=BiometricActionResponse)
def delete_biometric_credential(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Permanently delete the enrolled biometric template for the current authenticated user.
    
    This revokes face login immediately and frees all biometric data.
    The user can still log in with their password.
    """
    cred = db.execute(
        select(BiometricCredential).where(BiometricCredential.user_id == current_user.id)
    ).scalar_one_or_none()

    if not cred:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No biometric credential found to delete.",
        )

    db.delete(cred)
    db.commit()

    logger.info(f"Permanently purged biometric credential for user {current_user.email} (ID: {current_user.id})")
    return BiometricActionResponse(
        success=True,
        message="Biometric face profile permanently deleted. You can re-enroll at any time.",
    )
