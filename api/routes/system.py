"""System and application metadata endpoints."""

from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from database.connection import get_db
from services.health_service import get_system_infrastructure_health

router = APIRouter()


@router.get("/", tags=["system"])
async def root() -> Dict[str, str]:
    """Return basic application availability metadata."""
    return {"status": "ok"}


@router.get("/ready", tags=["system"])
def readiness(db: Session = Depends(get_db)) -> Dict[str, str]:
    """Lightweight readiness check for orchestration (e.g. k8s)."""
    try:
        db.execute(text("SELECT 1"))
        ext_check = db.execute(text("SELECT extname FROM pg_extension WHERE extname = 'vector'")).scalar()
        if ext_check != 'vector':
            raise HTTPException(status_code=503, detail="pgvector extension missing")
        return {"status": "ready"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database unavailable: {str(e)}")


@router.get("/health", tags=["system"])
def health(
    force_refresh: bool = False,
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """Report detailed application health status for PostgreSQL, pgvector, LLM APIs, and RAG retrieval."""
    res = get_system_infrastructure_health(db, force_refresh=force_refresh)
    return res.model_dump()
