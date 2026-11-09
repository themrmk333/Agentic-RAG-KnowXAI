"""Enterprise Admin Dashboard & Management API for MK Infinite Private Limited.

Implements:
1. Overview & live platform metrics (live DB aggregation).
2. Complete Employee Directory (search, filter, sort, pagination).
3. Detailed Employee Profile (personal, employment, auth security, usage).
4. Employee Management Actions (edit, role update, activate/deactivate, reset password, session revocation, biometrics/Google unlink).
5. Safe Employee Deletion (with multi-factor safeguards, prevents deleting self or last super admin, preserves knowledge).
6. Department Management (list, create, update, transfer, safe delete).
7. Access & Roles Control.
8. Company Activity & Security Audit Logs.
9. Security & Login Activity Monitoring.
10. Reports & Sanitized CSV Export (formula injection protected).
11. Company & Admin Settings.
"""

from __future__ import annotations

import csv
import io
import logging
import secrets
import string
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import case, desc, func, or_, select
from sqlalchemy.orm import Session

from api.auth import (
    hash_password,
    normalize_role,
    require_admin,
    require_super_admin,
)
from database.connection import get_db
from database.models import (
    AuditLog,
    BiometricCredential,
    Conversation,
    Department,
    Document,
    DocumentChunk,
    Message,
    User,
)
from services.audit_service import log_audit_event

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/admin", tags=["admin"])


# ============================================================================
# Schemas
# ============================================================================

class AdminStatsSchema(BaseModel):
    total_users: int
    total_documents: int
    total_chunks: int
    total_queries: int
    department_distribution: Dict[str, int]
    recent_queries: List[Dict[str, Any]]


class OverviewMetricsSchema(BaseModel):
    total_employees: int
    active_accounts: int
    disabled_accounts: int
    joined_this_month: int
    total_departments: int
    total_admins: int
    biometric_enrolled_count: int
    google_linked_count: int
    employee_growth: List[Dict[str, Any]]
    department_distribution: Dict[str, int]
    role_distribution: Dict[str, int]
    auth_methods: Dict[str, int]
    recent_activity: List[Dict[str, Any]]
    recent_employees: List[Dict[str, Any]]


class EmployeeListItemSchema(BaseModel):
    id: int
    employee_id: Optional[str] = None
    full_name: Optional[str] = None
    username: str
    email: str
    department: Optional[str] = None
    job_title: Optional[str] = None
    role: str
    is_active: bool
    auth_provider: str
    has_biometric: bool
    has_google: bool
    created_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None
    is_locked: bool = False


class EmployeeListResponseSchema(BaseModel):
    items: List[EmployeeListItemSchema]
    total_count: int
    page: int
    page_size: int
    total_pages: int


class EmployeeDetailSchema(BaseModel):
    id: int
    employee_id: Optional[str] = None
    full_name: Optional[str] = None
    username: str
    email: str
    department: Optional[str] = None
    job_title: Optional[str] = None
    role: str
    is_active: bool
    auth_provider: str
    created_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None
    security: Dict[str, Any]
    activity: Dict[str, Any]


class EmployeeUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    username: Optional[str] = None
    department: Optional[str] = None
    job_title: Optional[str] = None


class EmployeeRoleUpdateSchema(BaseModel):
    role: str = Field(..., description="Role to assign: super_admin, admin, manager, employee")


class EmployeeStatusUpdateSchema(BaseModel):
    is_active: bool = Field(..., description="Account active status")


class EmployeePasswordResetSchema(BaseModel):
    new_password: Optional[str] = Field(default=None, description="Optional custom password (min 6 chars); auto-generated if omitted.")


class DepartmentItemSchema(BaseModel):
    id: int
    name: str
    code: str
    description: Optional[str] = None
    lead_name: Optional[str] = None
    is_active: bool
    employee_count: int
    created_at: Optional[datetime] = None


class DepartmentCreateSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    code: str = Field(..., min_length=2, max_length=32)
    description: Optional[str] = None
    lead_name: Optional[str] = None


class DepartmentUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lead_name: Optional[str] = None
    is_active: Optional[bool] = None


class DepartmentTransferSchema(BaseModel):
    source_department: str
    target_department: str
    employee_ids: Optional[List[int]] = None


class AuditLogItemSchema(BaseModel):
    id: int
    action: str
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    metadata: Dict[str, Any]
    created_at: Optional[datetime] = None


class AuditLogListResponseSchema(BaseModel):
    items: List[AuditLogItemSchema]
    total_count: int
    page: int
    page_size: int
    total_pages: int


class SecuritySummarySchema(BaseModel):
    locked_accounts: List[Dict[str, Any]]
    failed_attempts_accounts: List[Dict[str, Any]]
    recent_security_events: List[Dict[str, Any]]
    biometric_stats: Dict[str, int]
    oauth_stats: Dict[str, int]


# ============================================================================
# Helpers
# ============================================================================

def sanitize_csv_cell(value: Any) -> str:
    """Prevent CSV formula injection by quoting formulas starting with =, +, -, @."""
    if value is None:
        return ""
    s = str(value).strip()
    if s.startswith(("=", "+", "-", "@", "\t", "\r")):
        return f"'{s}"
    return s


def check_last_super_admin_safeguard(db: Session, target_user: User) -> None:
    """Ensure we do not delete, demote, or deactivate the last active super_admin."""
    norm_role = normalize_role(target_user.role)
    if norm_role == "super_admin":
        # Count other active super admins
        active_super_admins = db.execute(
            select(func.count(User.id)).where(
                User.id != target_user.id,
                User.is_active == True,
                or_(
                    func.lower(User.role) == "super_admin",
                    func.lower(User.role) == "superadmin",
                    func.lower(User.role) == "owner",
                ),
            )
        ).scalar() or 0
        if active_super_admins == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Action denied: Cannot remove, disable, or demote the sole active Super Administrator of the company.",
            )


# ============================================================================
# 1. Overview & Dashboard Analytics
# ============================================================================

@router.get("/overview", response_model=OverviewMetricsSchema)
@router.get("/dashboard", response_model=OverviewMetricsSchema)
def get_dashboard_overview(
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Retrieve comprehensive real-time company analytics for MK Infinite Private Limited."""
    now = datetime.now(timezone.utc)
    first_of_month = datetime(now.year, now.month, 1, tzinfo=timezone.utc)

    # 1. Headline summary counts
    total_employees = db.execute(select(func.count(User.id))).scalar() or 0
    active_accounts = db.execute(select(func.count(User.id)).where(User.is_active == True)).scalar() or 0
    disabled_accounts = db.execute(select(func.count(User.id)).where(User.is_active == False)).scalar() or 0
    joined_this_month = db.execute(select(func.count(User.id)).where(User.created_at >= first_of_month)).scalar() or 0
    total_departments = db.execute(select(func.count(Department.id))).scalar() or 0

    # Total administrators (super_admin or admin)
    total_admins = db.execute(
        select(func.count(User.id)).where(
            or_(
                func.lower(User.role).in_(["admin", "administrator", "super_admin", "superadmin", "owner"])
            )
        )
    ).scalar() or 0

    # Biometric enrolled count
    biometric_enrolled_count = db.execute(
        select(func.count(BiometricCredential.id)).where(BiometricCredential.is_enabled == True)
    ).scalar() or 0

    # Google linked count
    google_linked_count = db.execute(
        select(func.count(User.id)).where(User.google_id != None)
    ).scalar() or 0

    # 2. Department distribution
    dept_rows = db.execute(
        select(User.department, func.count(User.id)).group_by(User.department)
    ).all()
    department_distribution = {}
    for d_name, count in dept_rows:
        department_distribution[d_name or "Unassigned"] = count

    # 3. Role distribution
    role_rows = db.execute(
        select(User.role, func.count(User.id)).group_by(User.role)
    ).all()
    role_distribution = {}
    for r_name, count in role_rows:
        norm = normalize_role(r_name).replace("_", " ").title()
        role_distribution[norm] = role_distribution.get(norm, 0) + count

    # 4. Auth methods breakdown
    both_count = db.execute(
        select(func.count(User.id))
        .join(BiometricCredential, User.id == BiometricCredential.user_id)
        .where(User.google_id != None, BiometricCredential.is_enabled == True)
    ).scalar() or 0
    bio_only = max(0, biometric_enrolled_count - both_count)
    google_only = max(0, google_linked_count - both_count)
    pwd_only = max(0, total_employees - (bio_only + google_only + both_count))

    auth_methods = {
        "Password Only": pwd_only,
        "Face ID Biometric": bio_only,
        "Google OAuth": google_only,
        "Multi-Method (Face + Google)": both_count,
    }

    # 5. Monthly employee growth over the last 6 months
    growth_list = []
    for i in range(5, -1, -1):
        target_month_date = (now - timedelta(days=i * 30)).replace(day=1)
        next_month_date = (target_month_date + timedelta(days=32)).replace(day=1)
        m_label = target_month_date.strftime("%b %Y")
        m_count = db.execute(
            select(func.count(User.id)).where(
                User.created_at >= target_month_date,
                User.created_at < next_month_date,
            )
        ).scalar() or 0
        growth_list.append({"month": m_label, "count": m_count})

    # 6. Recent company audit activity
    recent_logs = db.execute(
        select(AuditLog).order_by(desc(AuditLog.created_at)).limit(10)
    ).scalars().all()
    recent_activity = []
    for log in recent_logs:
        meta = log.audit_metadata or {}
        recent_activity.append({
            "id": log.id,
            "action": log.action,
            "summary": meta.get("summary") or log.action,
            "actor_email": meta.get("actor_email") or "System",
            "actor_name": meta.get("actor_name"),
            "target_email": meta.get("target_email"),
            "status": meta.get("status", "SUCCESS"),
            "timestamp": log.created_at.isoformat() if log.created_at else None,
        })

    # 7. Recent employees joined
    recent_users = db.execute(
        select(User).order_by(desc(User.created_at)).limit(6)
    ).scalars().all()
    recent_employees = []
    for u in recent_users:
        recent_employees.append({
            "id": u.id,
            "employee_id": u.employee_id,
            "full_name": u.full_name or u.username,
            "email": u.email,
            "department": u.department or "General",
            "role": normalize_role(u.role).replace("_", " ").title(),
            "is_active": getattr(u, "is_active", True),
            "created_at": u.created_at.isoformat() if u.created_at else None,
        })

    return {
        "total_employees": total_employees,
        "active_accounts": active_accounts,
        "disabled_accounts": disabled_accounts,
        "joined_this_month": joined_this_month,
        "total_departments": total_departments,
        "total_admins": total_admins,
        "biometric_enrolled_count": biometric_enrolled_count,
        "google_linked_count": google_linked_count,
        "employee_growth": growth_list,
        "department_distribution": department_distribution,
        "role_distribution": role_distribution,
        "auth_methods": auth_methods,
        "recent_activity": recent_activity,
        "recent_employees": recent_employees,
    }


# Backward-compatible stats endpoint
@router.get("/stats", response_model=AdminStatsSchema)
def get_admin_stats(
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Retrieve system analytics metrics and recent RAG query audits. (Admin only)"""
    total_users = db.query(User).count()
    total_documents = db.query(Document).count()
    total_chunks = db.query(DocumentChunk).count()
    total_queries = db.query(Message).filter(Message.role == "user").count()

    dept_stmt = select(User.department, func.count(User.id)).group_by(User.department)
    dept_rows = db.execute(dept_stmt).all()
    department_distribution = {}
    for dept, count in dept_rows:
        dept_name = dept or "General"
        department_distribution[dept_name] = count

    stmt = (
        select(Message.content, Message.created_at, User.email, User.department)
        .join(Conversation, Message.conversation_id == Conversation.id)
        .join(User, Conversation.user_id == User.id)
        .where(Message.role == "user")
        .order_by(Message.created_at.desc())
        .limit(10)
    )
    rows = db.execute(stmt).all()
    
    recent_queries = []
    for content, created_at, email, department in rows:
        recent_queries.append({
            "query": content,
            "timestamp": created_at.isoformat() if created_at else None,
            "user_email": email,
            "department": department or "General",
        })

    return {
        "total_users": total_users,
        "total_documents": total_documents,
        "total_chunks": total_chunks,
        "total_queries": total_queries,
        "department_distribution": department_distribution,
        "recent_queries": recent_queries,
    }


# ============================================================================
# 2. Employee Directory (List & Pagination)
# ============================================================================

@router.get("/employees", response_model=EmployeeListResponseSchema)
def list_employees(
    search: Optional[str] = Query(None, description="Search by name, employee_id, email, username"),
    department: Optional[str] = Query(None, description="Filter by department"),
    role: Optional[str] = Query(None, description="Filter by role"),
    status: Optional[str] = Query(None, description="Filter by status: all, active, disabled, locked"),
    sort_by: str = Query("created_at", description="Column to sort by"),
    sort_order: str = Query("desc", description="Sort order: asc or desc"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page"),
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Retrieve paginated employee directory with advanced server-side search, filtering, and sorting."""
    stmt = select(User)

    # 1. Search filter
    if search and search.strip():
        term = f"%{search.strip().lower()}%"
        stmt = stmt.where(
            or_(
                func.lower(User.full_name).ilike(term),
                func.lower(User.employee_id).ilike(term),
                func.lower(User.email).ilike(term),
                func.lower(User.username).ilike(term),
                func.lower(User.job_title).ilike(term),
            )
        )

    # 2. Department filter
    if department and department.strip() and department.lower() != "all":
        stmt = stmt.where(func.lower(User.department) == department.strip().lower())

    # 3. Role filter
    if role and role.strip() and role.lower() != "all":
        norm_filter = normalize_role(role)
        stmt = stmt.where(
            or_(
                func.lower(User.role) == norm_filter,
                func.lower(User.role) == role.strip().lower(),
            )
        )

    # 4. Status filter
    now = datetime.now(timezone.utc)
    if status == "active":
        stmt = stmt.where(User.is_active == True)
    elif status == "disabled":
        stmt = stmt.where(User.is_active == False)
    elif status == "locked":
        stmt = stmt.where(User.locked_until != None, User.locked_until > now)

    # Count total matching rows
    count_stmt = select(func.count()).select_from(stmt.subquery())
    total_count = db.execute(count_stmt).scalar() or 0

    # 5. Sorting
    sort_col = {
        "id": User.id,
        "name": User.full_name,
        "full_name": User.full_name,
        "employee_id": User.employee_id,
        "email": User.email,
        "username": User.username,
        "department": User.department,
        "role": User.role,
        "created_at": User.created_at,
        "last_login_at": User.last_login_at,
    }.get(sort_by, User.created_at)

    if sort_order.lower() == "asc":
        stmt = stmt.order_by(sort_col.asc())
    else:
        stmt = stmt.order_by(sort_col.desc())

    # 6. Pagination
    offset = (page - 1) * page_size
    stmt = stmt.offset(offset).limit(page_size)
    users = db.execute(stmt).scalars().all()

    # Pre-fetch biometric enrolled IDs for performance
    user_ids = [u.id for u in users]
    enrolled_ids = set()
    if user_ids:
        bio_rows = db.execute(
            select(BiometricCredential.user_id).where(
                BiometricCredential.user_id.in_(user_ids),
                BiometricCredential.is_enabled == True,
            )
        ).all()
        enrolled_ids = {r[0] for r in bio_rows}

    items = []
    for u in users:
        is_locked = bool(u.locked_until and u.locked_until > now)
        items.append(
            EmployeeListItemSchema(
                id=u.id,
                employee_id=u.employee_id,
                full_name=u.full_name,
                username=u.username,
                email=u.email,
                department=u.department,
                job_title=u.job_title,
                role=normalize_role(u.role).replace("_", " ").title(),
                is_active=getattr(u, "is_active", True),
                auth_provider=u.auth_provider,
                has_biometric=u.id in enrolled_ids,
                has_google=bool(u.google_id),
                created_at=u.created_at,
                last_login_at=u.last_login_at,
                is_locked=is_locked,
            )
        )

    total_pages = max(1, (total_count + page_size - 1) // page_size)
    return EmployeeListResponseSchema(
        items=items,
        total_count=total_count,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
    )


# ============================================================================
# 3. Employee Profile & Comprehensive Record
# ============================================================================

@router.get("/employees/{user_id}", response_model=EmployeeDetailSchema)
def get_employee_detail(
    user_id: int,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Retrieve full company record for an employee without exposing security secrets."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee record #{user_id} not found.",
        )

    # 1. Biometric security summary (safe status indicators only)
    now = datetime.now(timezone.utc)
    bio_cred = db.execute(
        select(BiometricCredential).where(BiometricCredential.user_id == user.id)
    ).scalar_one_or_none()

    biometric_info = {
        "enrolled": bio_cred is not None,
        "is_enabled": bio_cred.is_enabled if bio_cred else False,
        "enrolled_at": bio_cred.enrolled_at.isoformat() if bio_cred else None,
        "last_used_at": bio_cred.last_used_at.isoformat() if bio_cred and bio_cred.last_used_at else None,
        "failed_attempts": bio_cred.failed_attempts if bio_cred else 0,
        "is_locked": bool(bio_cred and bio_cred.locked_until and bio_cred.locked_until > now),
    }

    # 2. General security state
    is_account_locked = bool(user.locked_until and user.locked_until > now)
    security_info = {
        "auth_provider": user.auth_provider,
        "has_password": user.hashed_password is not None,
        "has_google": user.google_id is not None,
        "biometric": biometric_info,
        "failed_login_attempts": getattr(user, "failed_login_attempts", 0) or 0,
        "is_locked": is_account_locked,
        "locked_until": user.locked_until.isoformat() if user.locked_until else None,
        "session_version": getattr(user, "token_version", 1),
    }

    # 3. Safe usage & RAG statistics (counts only, no private text)
    conv_count = db.execute(
        select(func.count(Conversation.id)).where(Conversation.user_id == user.id)
    ).scalar() or 0

    msg_count = db.execute(
        select(func.count(Message.id))
        .join(Conversation, Message.conversation_id == Conversation.id)
        .where(Conversation.user_id == user.id)
    ).scalar() or 0

    last_conv = db.execute(
        select(Conversation.updated_at)
        .where(Conversation.user_id == user.id)
        .order_by(desc(Conversation.updated_at))
        .limit(1)
    ).scalar_one_or_none()

    # Recent audit logs affecting this user
    user_audit_logs = db.execute(
        select(AuditLog)
        .where(
            or_(
                AuditLog.resource_id == str(user.id),
                AuditLog.user_id == user.id,
            )
        )
        .order_by(desc(AuditLog.created_at))
        .limit(8)
    ).scalars().all()

    recent_logs = []
    for log in user_audit_logs:
        meta = log.audit_metadata or {}
        recent_logs.append({
            "action": log.action,
            "summary": meta.get("summary") or log.action,
            "actor_email": meta.get("actor_email") or "System",
            "status": meta.get("status", "SUCCESS"),
            "timestamp": log.created_at.isoformat() if log.created_at else None,
        })

    activity_info = {
        "total_conversations": conv_count,
        "total_messages": msg_count,
        "last_activity": last_conv.isoformat() if last_conv else None,
        "recent_logs": recent_logs,
    }

    return EmployeeDetailSchema(
        id=user.id,
        employee_id=user.employee_id,
        full_name=user.full_name,
        username=user.username,
        email=user.email,
        department=user.department,
        job_title=user.job_title,
        role=normalize_role(user.role).replace("_", " ").title(),
        is_active=getattr(user, "is_active", True),
        auth_provider=user.auth_provider,
        created_at=user.created_at,
        last_login_at=user.last_login_at,
        security=security_info,
        activity=activity_info,
    )


# ============================================================================
# 4. Employee Management Actions
# ============================================================================

@router.patch("/employees/{user_id}")
def update_employee_profile(
    user_id: int,
    payload: EmployeeUpdateSchema,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Update employee full name, username, department, or job title."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Employee not found.")

    changes = []
    if payload.full_name is not None:
        clean_name = payload.full_name.strip()
        if not clean_name:
            raise HTTPException(status_code=400, detail="Full name cannot be empty.")
        if clean_name != user.full_name:
            changes.append(f"Full Name: '{user.full_name}' -> '{clean_name}'")
            user.full_name = clean_name

    if payload.username is not None:
        clean_username = payload.username.strip()
        if len(clean_username) < 3:
            raise HTTPException(status_code=400, detail="Username must be at least 3 characters.")
        if clean_username.lower() != user.username.lower():
            # Check unique
            exists = db.execute(
                select(User).where(func.lower(User.username) == clean_username.lower(), User.id != user.id)
            ).scalar_one_or_none()
            if exists:
                raise HTTPException(status_code=400, detail="Username is already taken.")
            changes.append(f"Username: '{user.username}' -> '{clean_username}'")
            user.username = clean_username

    if payload.department is not None:
        clean_dept = payload.department.strip()
        if clean_dept != user.department:
            changes.append(f"Department: '{user.department}' -> '{clean_dept}'")
            user.department = clean_dept

    if payload.job_title is not None:
        clean_title = payload.job_title.strip()
        if clean_title != user.job_title:
            changes.append(f"Job Title: '{user.job_title}' -> '{clean_title}'")
            user.job_title = clean_title

    if not changes:
        return {"message": "No changes made.", "user_id": user.id}

    db.commit()
    db.refresh(user)

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="USER_PROFILE_UPDATED",
        actor=current_user,
        target_user=user,
        resource_type="USER",
        resource_id=str(user.id),
        summary=f"Profile updated for {user.email}: {', '.join(changes)}",
        ip_address=client_ip,
        extra_metadata={"changes": changes},
    )

    return {"message": "Employee profile updated successfully.", "changes": changes}


@router.patch("/employees/{user_id}/role")
def update_employee_role(
    user_id: int,
    payload: EmployeeRoleUpdateSchema,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Update employee system role with server-side privilege escalation safeguards."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Employee not found.")

    target_norm = normalize_role(payload.role)
    actor_norm = normalize_role(current_user.role)

    # Safeguard 1: Only super_admin can assign or change roles to super_admin or admin
    if target_norm in ("super_admin", "admin") and actor_norm != "super_admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Super Administrators can assign Admin or Super Admin privileges.",
        )

    # Safeguard 2: Regular admin cannot modify the role of another admin or super_admin
    if normalize_role(user.role) in ("super_admin", "admin") and actor_norm != "super_admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Regular administrators cannot modify the roles of other administrators.",
        )

    # Safeguard 3: Cannot demote the final super admin
    if normalize_role(user.role) == "super_admin" and target_norm != "super_admin":
        check_last_super_admin_safeguard(db, user)

    old_role = user.role
    # Standard format: Capitalized role
    formatted_role = target_norm.replace("_", " ").title()
    user.role = formatted_role

    # Invalidate existing sessions so new role claims take effect immediately
    user.token_version = (getattr(user, "token_version", 1) or 1) + 1
    db.commit()

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="USER_ROLE_UPDATED",
        actor=current_user,
        target_user=user,
        resource_type="USER",
        resource_id=str(user.id),
        summary=f"Role changed for {user.email} from '{old_role}' to '{formatted_role}'",
        ip_address=client_ip,
        extra_metadata={"old_role": old_role, "new_role": formatted_role},
    )

    return {"message": f"Role updated to {formatted_role}.", "role": formatted_role}


@router.patch("/employees/{user_id}/status")
def update_employee_status(
    user_id: int,
    payload: EmployeeStatusUpdateSchema,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Activate or deactivate an employee account with explicit safeguards."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Employee not found.")

    # Safeguard 1: Cannot deactivate yourself
    if user.id == current_user.id and not payload.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Self-deactivation denied: You cannot deactivate your own active session.",
        )

    # Safeguard 2: Cannot deactivate the last active super_admin
    if not payload.is_active:
        check_last_super_admin_safeguard(db, user)

    # Set status
    user.is_active = payload.is_active

    # When deactivating, revoke all active sessions immediately
    if not payload.is_active:
        user.token_version = (getattr(user, "token_version", 1) or 1) + 1

    db.commit()

    action_label = "USER_ACTIVATED" if payload.is_active else "USER_DEACTIVATED"
    summary_text = f"Employee account {'activated' if payload.is_active else 'deactivated'}: {user.email}"
    client_ip = request.client.host if request.client else "Unknown"

    log_audit_event(
        db=db,
        action=action_label,
        actor=current_user,
        target_user=user,
        resource_type="USER",
        resource_id=str(user.id),
        summary=summary_text,
        ip_address=client_ip,
    )

    return {
        "message": f"Employee account has been {'activated' if payload.is_active else 'deactivated'}.",
        "is_active": user.is_active,
    }


@router.post("/employees/{user_id}/reset-password")
def reset_employee_password(
    user_id: int,
    payload: EmployeePasswordResetSchema,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Securely reset an employee's password. Never displays existing password. Generates temp password if omitted."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Employee not found.")

    if payload.new_password and len(payload.new_password.strip()) >= 6:
        new_pwd = payload.new_password.strip()
    else:
        # Generate high-entropy 12-char alphanumeric temporary password
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        new_pwd = "".join(secrets.choice(chars) for _ in range(12))

    # Securely hash with bcrypt
    user.hashed_password = hash_password(new_pwd)
    # Revoke all active sessions immediately
    user.token_version = (getattr(user, "token_version", 1) or 1) + 1
    # Reset lockout counters
    user.failed_login_attempts = 0
    user.locked_until = None
    db.commit()

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="PASSWORD_RESET_ADMIN",
        actor=current_user,
        target_user=user,
        resource_type="USER",
        resource_id=str(user.id),
        summary=f"Administrative password reset performed for employee: {user.email}",
        ip_address=client_ip,
    )

    return {
        "message": "Password reset successfully. Active sessions revoked.",
        "temporary_password": new_pwd,
        "employee_email": user.email,
    }


@router.post("/employees/{user_id}/revoke-sessions")
def revoke_employee_sessions(
    user_id: int,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Instantly revoke all active JWT sessions and refresh tokens for an employee across all devices."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Employee not found.")

    user.token_version = (getattr(user, "token_version", 1) or 1) + 1
    db.commit()

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="SESSIONS_REVOKED_ADMIN",
        actor=current_user,
        target_user=user,
        resource_type="AUTH",
        resource_id=str(user.id),
        summary=f"All active user sessions revoked across devices for: {user.email}",
        ip_address=client_ip,
    )

    return {"message": "All sessions for this employee have been terminated."}


@router.post("/employees/{user_id}/revoke-biometrics")
def revoke_employee_biometrics(
    user_id: int,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Revoke and purge biometric Face ID enrollment for an employee without exposing templates."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Employee not found.")

    bio = db.execute(select(BiometricCredential).where(BiometricCredential.user_id == user.id)).scalar_one_or_none()
    if not bio:
        return {"message": "Employee has no active biometric enrollment."}

    db.delete(bio)
    db.commit()

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="BIOMETRIC_REVOKED_ADMIN",
        actor=current_user,
        target_user=user,
        resource_type="SECURITY",
        resource_id=str(user.id),
        summary=f"Biometric Face ID enrollment purged for: {user.email}",
        ip_address=client_ip,
    )

    return {"message": "Biometric credential revoked successfully."}


@router.post("/employees/{user_id}/unlink-google")
def unlink_employee_google(
    user_id: int,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Unlink Google identity while strictly ensuring user retains an alternative login password."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Employee not found.")

    if not user.google_id:
        return {"message": "No Google account is currently linked to this employee."}

    # Safeguard: Do not leave account without a login method
    if not user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot unlink Google account: This account has no password set. Please reset/set a password before unlinking Google.",
        )

    user.google_id = None
    user.auth_provider = "local"
    db.commit()

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="GOOGLE_UNLINKED_ADMIN",
        actor=current_user,
        target_user=user,
        resource_type="AUTH",
        resource_id=str(user.id),
        summary=f"Google OAuth credential unlinked for: {user.email}",
        ip_address=client_ip,
    )

    return {"message": "Google account unlinked successfully."}


@router.post("/employees/{user_id}/unlock")
def unlock_employee_account(
    user_id: int,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Clear failed login attempts and unlock temporarily locked employee accounts."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Employee not found.")

    user.failed_login_attempts = 0
    user.locked_until = None

    # Also unlock biometric credential if locked
    bio = db.execute(select(BiometricCredential).where(BiometricCredential.user_id == user.id)).scalar_one_or_none()
    if bio:
        bio.failed_attempts = 0
        bio.locked_until = None

    db.commit()

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="ACCOUNT_UNLOCKED_ADMIN",
        actor=current_user,
        target_user=user,
        resource_type="SECURITY",
        resource_id=str(user.id),
        summary=f"Account lockout cleared for: {user.email}",
        ip_address=client_ip,
    )

    return {"message": "Employee account unlocked successfully."}


# ============================================================================
# 5. Delete Employee Account (Permanent Deletion with Full Safeguards)
# ============================================================================

@router.delete("/employees/{user_id}")
def delete_employee_account(
    user_id: int,
    request: Request,
    current_user: User = Depends(require_super_admin),
    db: Session = Depends(get_db),
):
    """Permanently delete an employee account. Super Admin only. Enforces multi-step security constraints."""
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Employee not found.")

    # Safeguard 1: Prevent deleting the currently logged-in super admin
    if user.id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Self-deletion prohibited: You cannot delete the account you are currently logged in with.",
        )

    # Safeguard 2: Prevent deleting the last active super admin
    check_last_super_admin_safeguard(db, user)

    # Capture details for audit logging before deletion
    target_info = {
        "id": user.id,
        "employee_id": user.employee_id,
        "full_name": user.full_name,
        "email": user.email,
        "department": user.department,
        "role": user.role,
    }

    try:
        # Step A: Delete biometrics credential (also cascades in DB)
        bio = db.execute(select(BiometricCredential).where(BiometricCredential.user_id == user.id)).scalar_one_or_none()
        if bio:
            db.delete(bio)

        # Step B: Preserving business knowledge & audit records:
        # In models.py, foreign keys on Conversation, Task, AuditLog are defined with ON DELETE SET NULL.
        # This keeps conversations and messages available to company knowledge while removing the user.
        db.delete(user)
        db.commit()

        # Step C: Record deletion in audit log
        client_ip = request.client.host if request.client else "Unknown"
        log_audit_event(
            db=db,
            action="USER_DELETED",
            actor=current_user,
            target_employee_id=target_info["employee_id"],
            resource_type="USER",
            resource_id=str(target_info["id"]),
            summary=f"Permanent employee deletion: {target_info['full_name']} ({target_info['email']}) [ID: {target_info['employee_id']}]",
            ip_address=client_ip,
            extra_metadata={"deleted_user": target_info},
        )

        return {
            "message": f"Employee {target_info['full_name']} ({target_info['email']}) deleted permanently.",
            "deleted_id": target_info["id"],
        }

    except Exception as e:
        db.rollback()
        logger.error(f"Error during permanent employee deletion: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete employee account safely: {str(e)}",
        )


# ============================================================================
# 6. Department Management
# ============================================================================

@router.get("/departments", response_model=List[DepartmentItemSchema])
def list_departments(
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Retrieve all company departments with real-time employee counts."""
    departments = db.execute(select(Department).order_by(Department.name)).scalars().all()

    # Pre-fetch employee count per department
    dept_counts = dict(
        db.execute(
            select(User.department, func.count(User.id)).group_by(User.department)
        ).all()
    )

    results = []
    for d in departments:
        # Match count by name or code
        cnt = dept_counts.get(d.name, 0) + dept_counts.get(d.code, 0)
        results.append(
            DepartmentItemSchema(
                id=d.id,
                name=d.name,
                code=d.code,
                description=d.description,
                lead_name=d.lead_name,
                is_active=d.is_active,
                employee_count=cnt,
                created_at=d.created_at,
            )
        )
    return results


@router.post("/departments", response_model=DepartmentItemSchema)
def create_department(
    payload: DepartmentCreateSchema,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Create a new company department."""
    clean_name = payload.name.strip()
    clean_code = payload.code.strip().upper()

    existing = db.execute(
        select(Department).where(
            or_(
                func.lower(Department.name) == clean_name.lower(),
                Department.code == clean_code,
            )
        )
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A department with this name or code already exists.",
        )

    dept = Department(
        name=clean_name,
        code=clean_code,
        description=payload.description.strip() if payload.description else None,
        lead_name=payload.lead_name.strip() if payload.lead_name else None,
        is_active=True,
    )
    db.add(dept)
    db.commit()
    db.refresh(dept)

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="DEPARTMENT_CREATED",
        actor=current_user,
        resource_type="DEPARTMENT",
        resource_id=str(dept.id),
        summary=f"New department established: {dept.name} ({dept.code})",
        ip_address=client_ip,
    )

    return DepartmentItemSchema(
        id=dept.id,
        name=dept.name,
        code=dept.code,
        description=dept.description,
        lead_name=dept.lead_name,
        is_active=dept.is_active,
        employee_count=0,
        created_at=dept.created_at,
    )


@router.patch("/departments/{dept_id}", response_model=DepartmentItemSchema)
def update_department(
    dept_id: int,
    payload: DepartmentUpdateSchema,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Update department information. Propagates rename to assigned employees."""
    dept = db.execute(select(Department).where(Department.id == dept_id)).scalar_one_or_none()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found.")

    old_name = dept.name
    changes = []

    if payload.name is not None and payload.name.strip():
        new_name = payload.name.strip()
        if new_name.lower() != dept.name.lower():
            # Check unique
            exists = db.execute(
                select(Department).where(
                    func.lower(Department.name) == new_name.lower(),
                    Department.id != dept.id,
                )
            ).scalar_one_or_none()
            if exists:
                raise HTTPException(status_code=400, detail="Department name already exists.")

            # Update assigned users
            db.execute(
                select(User).where(User.department == old_name)
            )
            # Mass update users' department string
            for u in db.execute(select(User).where(User.department == old_name)).scalars().all():
                u.department = new_name

            changes.append(f"Name: '{old_name}' -> '{new_name}'")
            dept.name = new_name

    if payload.description is not None:
        dept.description = payload.description.strip()
        changes.append("Description updated")

    if payload.lead_name is not None:
        dept.lead_name = payload.lead_name.strip()
        changes.append(f"Lead: '{dept.lead_name}'")

    if payload.is_active is not None:
        dept.is_active = payload.is_active
        changes.append(f"Active: {payload.is_active}")

    db.commit()
    db.refresh(dept)

    cnt = db.execute(select(func.count(User.id)).where(User.department == dept.name)).scalar() or 0

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="DEPARTMENT_UPDATED",
        actor=current_user,
        resource_type="DEPARTMENT",
        resource_id=str(dept.id),
        summary=f"Department #{dept.id} ({dept.name}) updated: {', '.join(changes)}",
        ip_address=client_ip,
    )

    return DepartmentItemSchema(
        id=dept.id,
        name=dept.name,
        code=dept.code,
        description=dept.description,
        lead_name=dept.lead_name,
        is_active=dept.is_active,
        employee_count=cnt,
        created_at=dept.created_at,
    )


@router.post("/departments/transfer")
def transfer_department_employees(
    payload: DepartmentTransferSchema,
    request: Request,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Transfer employees between departments."""
    src = payload.source_department.strip()
    dst = payload.target_department.strip()

    if src.lower() == dst.lower():
        raise HTTPException(status_code=400, detail="Source and target departments cannot be the same.")

    stmt = select(User).where(User.department == src)
    if payload.employee_ids:
        stmt = stmt.where(User.id.in_(payload.employee_ids))

    users_to_transfer = db.execute(stmt).scalars().all()
    if not users_to_transfer:
        return {"message": "No matching employees found to transfer.", "transferred_count": 0}

    for u in users_to_transfer:
        u.department = dst

    db.commit()

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="DEPARTMENT_TRANSFER",
        actor=current_user,
        resource_type="DEPARTMENT",
        summary=f"Transferred {len(users_to_transfer)} employee(s) from '{src}' to '{dst}'",
        ip_address=client_ip,
    )

    return {
        "message": f"Successfully transferred {len(users_to_transfer)} employee(s) to '{dst}'.",
        "transferred_count": len(users_to_transfer),
    }


@router.delete("/departments/{dept_id}")
def delete_department(
    dept_id: int,
    request: Request,
    current_user: User = Depends(require_super_admin),
    db: Session = Depends(get_db),
):
    """Delete a department. Blocked if active employees remain assigned to it."""
    dept = db.execute(select(Department).where(Department.id == dept_id)).scalar_one_or_none()
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found.")

    # Check if employees are assigned
    assigned_count = db.execute(
        select(func.count(User.id)).where(
            or_(
                User.department == dept.name,
                User.department == dept.code,
            )
        )
    ).scalar() or 0

    if assigned_count > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Cannot delete department '{dept.name}': {assigned_count} employee(s) are currently assigned to it. Please transfer them to another department first.",
        )

    dept_name = dept.name
    db.delete(dept)
    db.commit()

    client_ip = request.client.host if request.client else "Unknown"
    log_audit_event(
        db=db,
        action="DEPARTMENT_DELETED",
        actor=current_user,
        resource_type="DEPARTMENT",
        resource_id=str(dept_id),
        summary=f"Department deleted: '{dept_name}'",
        ip_address=client_ip,
    )

    return {"message": f"Department '{dept_name}' has been deleted."}


# ============================================================================
# 7. Company Activity & Security Audit Logs
# ============================================================================

@router.get("/activity", response_model=AuditLogListResponseSchema)
def list_company_activity(
    action: Optional[str] = Query(None, description="Filter by event action name"),
    actor: Optional[str] = Query(None, description="Filter by actor email or name"),
    target: Optional[str] = Query(None, description="Filter by target email or ID"),
    page: int = Query(1, ge=1),
    page_size: int = Query(15, ge=1, le=100),
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Retrieve filtered, paginated company audit activity logs."""
    stmt = select(AuditLog).order_by(desc(AuditLog.created_at))

    if action and action.strip() and action.lower() != "all":
        stmt = stmt.where(AuditLog.action.ilike(f"%{action.strip()}%"))

    count_stmt = select(func.count()).select_from(stmt.subquery())
    total_count = db.execute(count_stmt).scalar() or 0

    offset = (page - 1) * page_size
    stmt = stmt.offset(offset).limit(page_size)
    logs = db.execute(stmt).scalars().all()

    items = []
    for l in logs:
        meta = l.audit_metadata or {}
        # Filter actor/target in Python if JSON metadata query is database-agnostic
        if actor and actor.strip():
            act_str = f"{meta.get('actor_email', '')} {meta.get('actor_name', '')}".lower()
            if actor.strip().lower() not in act_str:
                continue
        if target and target.strip():
            tar_str = f"{meta.get('target_email', '')} {meta.get('target_employee_id', '')}".lower()
            if target.strip().lower() not in tar_str:
                continue

        items.append(
            AuditLogItemSchema(
                id=l.id,
                action=l.action,
                resource_type=l.resource_type,
                resource_id=l.resource_id,
                metadata=meta,
                created_at=l.created_at,
            )
        )

    total_pages = max(1, (total_count + page_size - 1) // page_size)
    return AuditLogListResponseSchema(
        items=items,
        total_count=total_count,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
    )


# ============================================================================
# 8. Security & Login Activity
# ============================================================================

@router.get("/security", response_model=SecuritySummarySchema)
def get_security_overview(
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Retrieve comprehensive security events, lockout status, and login risk metrics."""
    now = datetime.now(timezone.utc)

    # 1. Accounts currently locked out
    locked_users = db.execute(
        select(User).where(User.locked_until != None, User.locked_until > now)
    ).scalars().all()

    locked_list = []
    for u in locked_users:
        remaining = int((u.locked_until - now).total_seconds()) if u.locked_until else 0
        locked_list.append({
            "id": u.id,
            "employee_id": u.employee_id,
            "email": u.email,
            "full_name": u.full_name,
            "failed_attempts": u.failed_login_attempts,
            "locked_until": u.locked_until.isoformat() if u.locked_until else None,
            "remaining_seconds": max(0, remaining),
        })

    # 2. Accounts with non-zero failed attempts but not yet locked
    failed_users = db.execute(
        select(User).where(User.failed_login_attempts > 0, or_(User.locked_until == None, User.locked_until <= now))
    ).scalars().all()

    failed_list = []
    for u in failed_users:
        failed_list.append({
            "id": u.id,
            "employee_id": u.employee_id,
            "email": u.email,
            "full_name": u.full_name,
            "failed_attempts": u.failed_login_attempts,
            "last_login_at": u.last_login_at.isoformat() if u.last_login_at else None,
        })

    # 3. Recent security audit events
    security_logs = db.execute(
        select(AuditLog)
        .where(
            AuditLog.action.in_([
                "USER_LOGIN_FAILED",
                "USER_ACCOUNT_LOCKED",
                "USER_ROLE_UPDATED",
                "USER_DEACTIVATED",
                "USER_DELETED",
                "PASSWORD_RESET_ADMIN",
                "BIOMETRIC_REVOKED_ADMIN",
            ])
        )
        .order_by(desc(AuditLog.created_at))
        .limit(15)
    ).scalars().all()

    sec_events = []
    for l in security_logs:
        meta = l.audit_metadata or {}
        sec_events.append({
            "id": l.id,
            "action": l.action,
            "summary": meta.get("summary") or l.action,
            "actor_email": meta.get("actor_email") or "System",
            "target_email": meta.get("target_email"),
            "status": meta.get("status", "ALERT"),
            "timestamp": l.created_at.isoformat() if l.created_at else None,
        })

    # 4. Biometric statistics
    total_enrolled = db.execute(select(func.count(BiometricCredential.id))).scalar() or 0
    active_enrolled = db.execute(
        select(func.count(BiometricCredential.id)).where(BiometricCredential.is_enabled == True)
    ).scalar() or 0
    bio_locked = db.execute(
        select(func.count(BiometricCredential.id)).where(
            BiometricCredential.locked_until != None,
            BiometricCredential.locked_until > now,
        )
    ).scalar() or 0

    biometric_stats = {
        "total_enrolled": total_enrolled,
        "active_enabled": active_enrolled,
        "temporarily_locked": bio_locked,
    }

    # 5. OAuth stats
    google_total = db.execute(select(func.count(User.id)).where(User.google_id != None)).scalar() or 0
    oauth_stats = {
        "google_linked": google_total,
    }

    return SecuritySummarySchema(
        locked_accounts=locked_list,
        failed_attempts_accounts=failed_list,
        recent_security_events=sec_events,
        biometric_stats=biometric_stats,
        oauth_stats=oauth_stats,
    )


# ============================================================================
# 9. Reports & Sanitized CSV Export
# ============================================================================

@router.get("/reports/employees")
def export_employees_csv(
    department: Optional[str] = Query(None),
    role: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Generate authorized enterprise CSV directory export with formula-injection sanitization. Never exports secrets."""
    stmt = select(User).order_by(User.id.asc())

    if department and department.strip() and department.lower() != "all":
        stmt = stmt.where(func.lower(User.department) == department.strip().lower())
    if role and role.strip() and role.lower() != "all":
        norm = normalize_role(role)
        stmt = stmt.where(or_(func.lower(User.role) == norm, func.lower(User.role) == role.strip().lower()))
    if status == "active":
        stmt = stmt.where(User.is_active == True)
    elif status == "disabled":
        stmt = stmt.where(User.is_active == False)

    users = db.execute(stmt).scalars().all()

    # Pre-fetch biometric status
    bio_set = set(
        db.execute(
            select(BiometricCredential.user_id).where(BiometricCredential.is_enabled == True)
        ).scalars().all()
    )

    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)

    # Header
    writer.writerow([
        "Employee ID",
        "Full Name",
        "Username",
        "Work Email",
        "Department",
        "Job Title",
        "Role",
        "Account Status",
        "Auth Provider",
        "Biometric Enrolled",
        "Google Linked",
        "Date Joined",
        "Last Login",
    ])

    for u in users:
        writer.writerow([
            sanitize_csv_cell(u.employee_id or f"EMP-{u.id:04d}"),
            sanitize_csv_cell(u.full_name or ""),
            sanitize_csv_cell(u.username),
            sanitize_csv_cell(u.email),
            sanitize_csv_cell(u.department or "General"),
            sanitize_csv_cell(u.job_title or "Employee"),
            sanitize_csv_cell(normalize_role(u.role).replace("_", " ").title()),
            "Active" if getattr(u, "is_active", True) else "Disabled",
            sanitize_csv_cell(u.auth_provider),
            "Enrolled" if u.id in bio_set else "Not Enrolled",
            "Linked" if u.google_id else "Not Linked",
            u.created_at.strftime("%Y-%m-%d %H:%M:%S") if u.created_at else "",
            u.last_login_at.strftime("%Y-%m-%d %H:%M:%S") if u.last_login_at else "Never",
        ])

    csv_data = output.getvalue()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"MK_Infinite_Employees_{timestamp}.csv"

    log_audit_event(
        db=db,
        action="REPORT_EMPLOYEES_EXPORTED",
        actor=current_user,
        resource_type="REPORT",
        summary=f"Employee directory exported to CSV ({len(users)} records) by {current_user.email}",
    )

    return Response(
        content=csv_data,
        media_type="text/csv; charset=utf-8",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"',
            "Cache-Control": "no-cache, no-store, must-revalidate",
        },
    )


# ============================================================================
# 10. Admin & Company Settings
# ============================================================================

@router.get("/settings")
def get_company_settings(
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Retrieve system configuration and company metadata."""
    from config.settings import get_settings
    settings = get_settings()

    return {
        "company": {
            "name": "MK Infinite Private Limited",
            "portal_title": "Agentic RAG KnowXAI Enterprise Portal",
            "system_version": "v1.2.0-Enterprise",
            "copyright": f"© {datetime.now().year} MK Infinite Private Limited. All rights reserved.",
        },
        "security_policy": {
            "token_algorithm": settings.jwt_algorithm,
            "session_timeout_minutes": settings.access_token_expire_minutes,
            "lockout_failed_attempts_threshold": 5,
            "lockout_duration_minutes": 15,
            "password_min_length": 4,
            "biometrics_available": True,
            "google_oauth_configured": bool(
                settings.google_client_id and not settings.google_client_id.startswith("your-")
            ),
        },
        "supported_roles": [
            {"code": "super_admin", "label": "Super Admin (Owner)", "description": "Full enterprise company administration and security management"},
            {"code": "admin", "label": "Administrator", "description": "Operational employee directory, departments, and monitoring control"},
            {"code": "manager", "label": "Department Manager", "description": "Department-level team monitoring and oversight"},
            {"code": "employee", "label": "Employee", "description": "Standard company user with knowledge RAG chat and documents access"},
        ],
    }
