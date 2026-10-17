"""API routes for RAG execution."""

import logging
from fastapi import APIRouter, Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import jwt

from api.schemas.rag import RAGQueryRequest, RAGQueryResponse
from database.connection import get_db
from services.rag_service import RAGService
from api.auth import oauth2_scheme, JWT_SECRET_KEY, JWT_ALGORITHM
from database.models import User
from sqlalchemy import select

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/rag", tags=["rag"])

def get_optional_user_context(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> dict:
    """Extract department context if a valid token is provided, else return empty."""
    if not token:
        return {}
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        email = payload.get("sub")
        if email:
            user = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
            if user and getattr(user, "department", None):
                return {"department": user.department, "role": user.role}
    except Exception:
        pass
    return {}

@router.post("/query", response_model=RAGQueryResponse)
def run_rag_query(
    request: RAGQueryRequest,
    db: Session = Depends(get_db),
    user_context: dict = Depends(get_optional_user_context)
):
    """
    Execute a full RAG query.
    
    The user_context is injected automatically via authentication to enforce
    department-level permissions.
    """
    if not request.query or not request.query.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query cannot be empty"
        )
        
    try:
        service = RAGService(db=db)
        response = service.process_query(request=request, user_context=user_context)
        return response
    except ValueError as ve:
        logger.error(f"Validation error in RAG service: {str(ve)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ve)
        )
    except Exception as e:
        logger.exception("Internal error executing RAG pipeline")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal error occurred during generation."
        )
