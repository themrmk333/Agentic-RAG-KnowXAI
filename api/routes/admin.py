"""Admin endpoints to compile analytics and monitor platform metrics."""

from typing import Any, Dict, List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from api.auth import get_admin_user
from database.connection import get_db
from database.models import Conversation, Document, DocumentChunk, Message, User

router = APIRouter(prefix="/admin", tags=["admin"])


class AdminStatsSchema(BaseModel):
    total_users: int
    total_documents: int
    total_chunks: int
    total_queries: int
    department_distribution: Dict[str, int]
    recent_queries: List[Dict[str, Any]]


@router.get("/stats", response_model=AdminStatsSchema)
def get_admin_stats(
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """Retrieve system analytics metrics and recent RAG query audits. (Admin only)"""
    # 1. Counts
    total_users = db.query(User).count()
    total_documents = db.query(Document).count()
    total_chunks = db.query(DocumentChunk).count()
    total_queries = db.query(Message).filter(Message.role == "user").count()

    # 2. Department-wise User Distribution
    dept_stmt = select(User.department, func.count(User.id)).group_by(User.department)
    dept_rows = db.execute(dept_stmt).all()
    department_distribution = {}
    for dept, count in dept_rows:
        dept_name = dept or "General"
        department_distribution[dept_name] = count

    # 3. Recent Queries Audit Log
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
            "department": department or "General"
        })

    return {
        "total_users": total_users,
        "total_documents": total_documents,
        "total_chunks": total_chunks,
        "total_queries": total_queries,
        "department_distribution": department_distribution,
        "recent_queries": recent_queries
    }
