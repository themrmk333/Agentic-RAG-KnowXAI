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


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
