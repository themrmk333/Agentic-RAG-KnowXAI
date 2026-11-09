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
    """Report detailed application health status for PostgreSQL, pgvector, LLM APIs, and RAG retrieval."""
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
    embedding_detail = "uninitialized"
    try:
        from rag.retrieval.query_embedder import QueryEmbedder
        embedder = QueryEmbedder.get_instance()
        vec = embedder.embed_query("health check")
        if vec and len(vec) == 384:
            embedding_healthy = True
            embedding_detail = f"active ({embedder.model_name}, dim=384, device={embedder.device})"
        else:
            embedding_detail = f"unexpected vector dimension: {len(vec) if vec else 0}"
    except Exception as emb_e:
        embedding_detail = f"failed to load: {str(emb_e)}"
        try:
            service = build_embedding_service()
            vecs = service.embed(["health check"])
            if vecs and len(vecs[0]) == 384:
                embedding_healthy = True
                embedding_detail = "active via fallback embedding factory"
        except Exception:
            pass

    # 4. Retrieval Service check
    retrieval_healthy = False
    retrieval_detail = "uninitialized"
    try:
        from database.models import DocumentChunk
        from sqlalchemy import func, select
        chunk_count = db.execute(select(func.count(DocumentChunk.id))).scalar()
        if db_healthy and vector_extension and embedding_healthy and chunk_count is not None and chunk_count > 0:
            retrieval_healthy = True
            retrieval_detail = f"operational ({chunk_count} indexed chunks)"
        elif chunk_count == 0:
            retrieval_detail = "no indexed chunks available in database"
        else:
            retrieval_detail = "retrieval dependencies degraded"
    except Exception as ret_e:
        retrieval_detail = f"retrieval check failed: {str(ret_e)}"

    overall_status = "healthy" if db_healthy and vector_extension and embedding_healthy and retrieval_healthy else "degraded"
    
    rag_metrics = RagMetricsStore.get_instance().get_stats()

    return {
        "status": overall_status,
        "database": {
            "healthy": db_healthy,
            "detail": db_detail,
            "pgvector_enabled": vector_extension
        },
        "embedding_service": {
            "healthy": embedding_healthy,
            "detail": embedding_detail,
        },
        "retrieval_service": {
            "healthy": retrieval_healthy,
            "detail": retrieval_detail,
        },
        "llm_providers": llm_states,
        "rag_metrics": rag_metrics
    }
