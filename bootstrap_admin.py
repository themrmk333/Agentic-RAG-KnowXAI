"""Secure Super Admin Bootstrap Utility for MK Infinite Private Limited.

Allows initial platform setup and secure promotion of the company owner / super admin.
Usage:
    python bootstrap_admin.py --email admin@knowxai.com --password YourSecurePassword123! --name "Company Owner" --emp-id EMP-0001
"""

from __future__ import annotations

import argparse
import getpass
import sys
from datetime import datetime, timezone

from sqlalchemy import func, or_, select

from api.auth import hash_password
from database.connection import SessionLocal, init_db
from database.models import User
from services.audit_service import log_audit_event


def bootstrap_super_admin(
    email: str,
    password: str | None = None,
    full_name: str | None = None,
    employee_id: str | None = None,
    department: str = "Management",
) -> None:
    print("=" * 65)
    print("  MK INFINITE PRIVATE LIMITED — SUPER ADMIN BOOTSTRAP")
    print("=" * 65)

    clean_email = email.strip().lower()
    if not clean_email or "@" not in clean_email:
        print("[ERROR] A valid work email address is required.")
        sys.exit(1)

    # Initialize tables and schema extensions if not yet done
    init_db()

    db = SessionLocal()
    try:
        # Check if user already exists
        existing_user = db.execute(
            select(User).where(func.lower(User.email) == clean_email)
        ).scalar_one_or_none()

        if existing_user:
            print(f"[FOUND] Existing user account located for: {clean_email}")
            print(f"        Current Role: {existing_user.role}")
            print(f"        Current Status: {'Active' if existing_user.is_active else 'Disabled'}")

            # Promote to Super Admin
            existing_user.role = "Super Admin"
            existing_user.is_active = True
            existing_user.failed_login_attempts = 0
            existing_user.locked_until = None
            if full_name:
                existing_user.full_name = full_name.strip()
            if employee_id:
                existing_user.employee_id = employee_id.strip()
            if password:
                existing_user.hashed_password = hash_password(password)

            existing_user.token_version = (getattr(existing_user, "token_version", 1) or 1) + 1
            db.commit()

            log_audit_event(
                db=db,
                action="SUPER_ADMIN_BOOTSTRAP_PROMOTED",
                target_user=existing_user,
                resource_type="USER",
                resource_id=str(existing_user.id),
                summary=f"User {existing_user.email} promoted to Super Admin via secure bootstrap.",
            )
            print()
            print("[SUCCESS] Account successfully elevated to Super Admin!")
            print(f"          Email: {existing_user.email}")
            print(f"          Role: {existing_user.role}")
            print(f"          Status: Active")
            print("=" * 65)
            return

        # User does not exist, prompt for password if not provided
        if not password:
            print(f"[INFO] Account does not exist. Creating new Super Admin account for: {clean_email}")
            pwd1 = getpass.getpass("Enter password for Super Admin: ")
            pwd2 = getpass.getpass("Confirm password: ")
            if pwd1 != pwd2:
                print("[ERROR] Passwords do not match.")
                sys.exit(1)
            password = pwd1

        if len(password.strip()) < 4:
            print("[ERROR] Password must be at least 4 characters long.")
            sys.exit(1)

        # Generate unique username
        username_base = clean_email.split("@")[0]
        username = username_base
        counter = 1
        while db.execute(select(User).where(func.lower(User.username) == username.lower())).scalar_one_or_none():
            username = f"{username_base}{counter}"
            counter += 1

        new_admin = User(
            email=clean_email,
            username=username,
            full_name=full_name.strip() if full_name else "Company Super Administrator",
            hashed_password=hash_password(password),
            employee_id=employee_id.strip() if employee_id else "EMP-SUPER-01",
            department=department.strip(),
            role="Super Admin",
            is_active=True,
            failed_login_attempts=0,
            token_version=1,
            auth_provider="local",
        )
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)

        log_audit_event(
            db=db,
            action="SUPER_ADMIN_BOOTSTRAP_CREATED",
            target_user=new_admin,
            resource_type="USER",
            resource_id=str(new_admin.id),
            summary=f"Super Admin account initialized via bootstrap: {new_admin.email}",
        )

        print()
        print("[SUCCESS] Super Admin account created successfully!")
        print(f"          Email: {new_admin.email}")
        print(f"          Username: {new_admin.username}")
        print(f"          Role: {new_admin.role}")
        print(f"          Employee ID: {new_admin.employee_id}")
        print(f"          Department: {new_admin.department}")
        print("=" * 65)

    except Exception as e:
        db.rollback()
        print(f"[ERROR] Bootstrap failed: {e}")
        sys.exit(1)
    finally:
        db.close()


def main():
    parser = argparse.ArgumentParser(description="Bootstrap MK Infinite Super Admin account.")
    parser.add_argument("--email", type=str, help="Email address of the super admin")
    parser.add_argument("--password", type=str, help="Password for the account (optional if elevating existing user)")
    parser.add_argument("--name", type=str, default="Company Owner", help="Full name")
    parser.add_argument("--emp-id", type=str, default="EMP-SUPER-01", help="Employee ID")
    parser.add_argument("--department", type=str, default="Management", help="Department")

    args = parser.parse_args()

    if not args.email:
        print("--- Interactive Super Admin Setup ---")
        email = input("Super Admin Email: ").strip()
        pwd = getpass.getpass("Super Admin Password (leave blank if existing user): ").strip()
        name = input("Full Name [Company Owner]: ").strip() or "Company Owner"
        emp_id = input("Employee ID [EMP-SUPER-01]: ").strip() or "EMP-SUPER-01"
        bootstrap_super_admin(email=email, password=pwd or None, full_name=name, employee_id=emp_id)
    else:
        bootstrap_super_admin(
            email=args.email,
            password=args.password,
            full_name=args.name,
            employee_id=args.emp_id,
            department=args.department,
        )


if __name__ == "__main__":
    main()
