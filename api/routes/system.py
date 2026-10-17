"""System and application metadata endpoints."""

from typing import Any, Dict
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from database.connection import get_db
from agents.llm.factory import provider_health
from rag.embeddings.factory import build_embedding_service
from rag.telemetry.metrics import RagMetricsStore

router = APIRouter()


@router.get("/", tags=["system"])
async def root() -> Dict[str, str]:
    """Return basic application availability metadata."""
    return {"status": "ok"}

from fastapi import HTTPException

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
def health(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """Report detailed application health status for PostgreSQL, pgvector, and LLM APIs."""
    # 1. Database Connection and pgvector checks
    db_healthy = False
    db_detail = "connection failed"
    vector_extension = False
    try:
        db.execute(text("SELECT 1"))
        db_healthy = True
        db_detail = "connected"
        
        ext_check = db.execute(text("SELECT extname FROM pg_extension WHERE extname = 'vector'")).scalar()
        if ext_check == 'vector':
            vector_extension = True
    except Exception as e:
        db_detail = str(e)

    # 2. LLM Providers health check
    llm_states = {}
    try:
        llm_states = provider_health()
    except Exception as e:
        llm_states = {"error": f"LLM checks failed: {str(e)}"}

    # 3. Embedding Service check
    embedding_healthy = False
    try:
        service = build_embedding_service()
        service.embed(["health check"])
        embedding_healthy = True
    except Exception:
        pass

    overall_status = "healthy" if db_healthy and vector_extension and embedding_healthy else "degraded"
    
    rag_metrics = RagMetricsStore.get_instance().get_stats()

    return {
        "status": overall_status,
        "database": {
            "healthy": db_healthy,
            "detail": db_detail,
            "pgvector_enabled": vector_extension
        },
        "llm_providers": llm_states,
        "embedding_service": {
            "healthy": embedding_healthy
        },
        "rag_metrics": rag_metrics
    }
