"""Enterprise Audit Logging Service for MK Infinite Private Limited.

Captures, persists, and queries security, user management, and operational audit events.
Strictly ensures no secrets, passwords, tokens, or raw biometric data are recorded.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from sqlalchemy import desc, func, select
from sqlalchemy.orm import Session

from database.models import AuditLog, User

logger = logging.getLogger(__name__)

# Sensitive keys that must NEVER be persisted in audit logs
FORBIDDEN_AUDIT_KEYS = {
    "password",
    "hashed_password",
    "new_password",
    "temporary_password",
    "token",
    "access_token",
    "refresh_token",
    "secret",
    "key",
    "jwt",
    "encrypted_template",
    "raw_image",
    "image_base64",
    "burst_frames",
    "credential",
}


def sanitize_audit_metadata(data: Dict[str, Any] | None) -> Dict[str, Any]:
    """Sanitize metadata by stripping any forbidden security fields."""
    if not data:
        return {}
    clean: Dict[str, Any] = {}
    for k, v in data.items():
        if any(bad in k.lower() for bad in FORBIDDEN_AUDIT_KEYS):
            clean[k] = "[REDACTED]"
        elif isinstance(v, dict):
            clean[k] = sanitize_audit_metadata(v)
        else:
            clean[k] = v
    return clean


def log_audit_event(
    db: Session,
    action: str,
    actor: Optional[User] = None,
    target_user: Optional[User] = None,
    target_employee_id: Optional[str] = None,
    resource_type: str = "USER",
    resource_id: Optional[str] = None,
    summary: str = "",
    status: str = "SUCCESS",
    ip_address: Optional[str] = None,
    extra_metadata: Optional[Dict[str, Any]] = None,
) -> AuditLog:
    """Safely record an audit log event in the database."""
    safe_meta = sanitize_audit_metadata(extra_metadata or {})
    safe_meta.update({
        "summary": summary,
        "status": status,
        "actor_email": actor.email if actor else "System",
        "actor_role": getattr(actor, "role", "System") if actor else "System",
        "actor_name": getattr(actor, "full_name", "") if actor else "",
        "target_email": target_user.email if target_user else None,
        "target_employee_id": target_employee_id or (getattr(target_user, "employee_id", None) if target_user else None),
        "target_name": getattr(target_user, "full_name", "") if target_user else None,
        "ip_address": ip_address or "Internal",
    })

    audit_entry = AuditLog(
        user_id=actor.id if actor else None,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id or (str(target_user.id) if target_user else None),
        audit_metadata=safe_meta,
    )

    try:
        db.add(audit_entry)
        db.commit()
        db.refresh(audit_entry)
        return audit_entry
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to record audit log event ({action}): {e}", exc_info=True)
        return audit_entry
