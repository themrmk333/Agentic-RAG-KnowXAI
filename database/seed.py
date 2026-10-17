from __future__ import annotations

from sqlalchemy import select

from .connection import SessionLocal
from .models import Document, User
import bcrypt

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def seed_demo_data() -> None:
    with SessionLocal() as session:
        existing_user = session.execute(select(User).where(User.email == "admin@example.com")).scalar_one_or_none()
        if existing_user is None:
            user = User(
                email="admin@example.com",
                username="admin",
                full_name="System Administrator",
                hashed_password=hash_password("Admin@123"),
                role="Admin",
                employee_id="EMP-001",
                department="Management",
            )
            session.add(user)
            session.flush()
        else:
            if not existing_user.hashed_password:
                existing_user.hashed_password = hash_password("Admin@123")
            if existing_user.role != "Admin":
                existing_user.role = "Admin"
            if not existing_user.employee_id:
                existing_user.employee_id = "EMP-001"
            if not existing_user.department:
                existing_user.department = "Management"

        existing_document = session.execute(select(Document).where(Document.title == "KnowXAI System Overview")).scalar_one_or_none()
        if existing_document is None:
            document = Document(
                title="KnowXAI System Overview",
                source_path="/docs/overview.md",
                content_type="text/markdown",
                metadata={"source": "seed", "category": "overview"},
            )
            session.add(document)
            session.commit()
            print("Seed data initialized.")
        else:
            session.commit()
            print("Seed data already exists.")


if __name__ == "__main__":
    seed_demo_data()
