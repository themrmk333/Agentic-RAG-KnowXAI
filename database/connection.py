from typing import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from config.settings import get_settings


def get_database_url() -> str:
    database_url = get_settings().database_url
    if database_url is None or not database_url.get_secret_value().strip():
        raise RuntimeError("DATABASE_URL must be configured in the environment or .env file")
    database_url = database_url.get_secret_value().strip()
    if database_url.startswith("postgresql://"):
        return database_url.replace("postgresql://", "postgresql+psycopg2://", 1)
    return database_url


def get_db_echo() -> bool:
    return get_settings().db_echo


engine = create_engine(
    get_database_url(),
    echo=get_db_echo(),
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=10,
    max_overflow=20,
    future=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
    future=True,
)


def init_db() -> None:
    """Initialize PostgreSQL extensions and create application tables."""
    with engine.begin() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))

    from .models import Base

    Base.metadata.create_all(bind=engine)

    with engine.begin() as connection:
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS hashed_password VARCHAR(255);"))
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS role VARCHAR(64) DEFAULT 'Employee';"))
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS employee_id VARCHAR(64);"))
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS department VARCHAR(120);"))
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS job_title VARCHAR(120);"))
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS is_active BOOLEAN DEFAULT TRUE;"))
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS last_login_at TIMESTAMP WITH TIME ZONE;"))
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS failed_login_attempts INTEGER DEFAULT 0;"))
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS locked_until TIMESTAMP WITH TIME ZONE;"))
        connection.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS token_version INTEGER DEFAULT 1;"))

        # Seed standard enterprise departments if empty
        dept_count = connection.execute(text("SELECT count(*) FROM departments;")).scalar()
        if dept_count == 0:
            default_departments = [
                ("IT Support", "IT", "Information Technology, Infrastructure, Security, and Technical Support", "Technical Director"),
                ("Human Resources", "HR", "Talent Acquisition, Employee Relations, People Operations, and Compliance", "HR Director"),
                ("Finance & Claims", "FIN", "Financial Accounting, Payroll, Auditing, and Insurance Claims", "Finance Controller"),
                ("Project Department", "PRJ", "Client Delivery, Engineering Projects, and Technical Solutions", "Project Lead"),
                ("Management", "MGT", "Executive Leadership, Corporate Governance, and Strategic Growth", "Managing Director"),
                ("Admin", "ADM", "Administrative Operations, Office Management, and Corporate Support", "Operations Administrator"),
            ]
            for name, code, desc, lead in default_departments:
                connection.execute(
                    text("""
                        INSERT INTO departments (name, code, description, lead_name, is_active, created_at, updated_at)
                        VALUES (:name, :code, :desc, :lead, TRUE, NOW(), NOW())
                        ON CONFLICT (code) DO NOTHING;
                    """),
                    {"name": name, "code": code, "desc": desc, "lead": lead}
                )

        # Check whether the database already has an Admin department before creating one; avoid duplicate records
        admin_dept = connection.execute(
            text("SELECT id FROM departments WHERE code = 'ADM' OR lower(name) = 'admin';")
        ).scalar()
        if not admin_dept:
            connection.execute(
                text("""
                    INSERT INTO departments (name, code, description, lead_name, is_active, created_at, updated_at)
                    VALUES ('Admin', 'ADM', 'Administrative Operations, Office Management, and Corporate Support', 'Operations Administrator', TRUE, NOW(), NOW())
                    ON CONFLICT (code) DO NOTHING;
                """)
            )


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
