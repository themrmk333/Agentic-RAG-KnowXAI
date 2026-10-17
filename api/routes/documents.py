"""Document management endpoints for uploading, listing, and deleting company knowledge sources."""

from typing import Any, Dict, List, Optional
from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile, File, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from api.auth import get_admin_user, get_current_user
from database.connection import get_db
from database.models import Document, User
from database.vector_store import vector_store

from rag.loaders.file_loader import load_file
from rag.ingestion.pipeline import ingest_documents
from rag.embeddings.factory import build_embedding_service

router = APIRouter(prefix="/documents", tags=["documents"])


class DocumentResponseSchema(BaseModel):
    id: int
    title: str
    source_path: Optional[str]
    content_type: Optional[str]
    document_metadata: Dict[str, Any]
    created_at: Any

    class Config:
        from_attributes = True


@router.post("/upload", response_model=Dict[str, Any])
async def upload_document(
    file: UploadFile = File(...),
    department: str = Form("General"),
    category: str = Form("SOP"),
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    """Upload a PDF, DOCX, TXT, or ZIP file to the company knowledge base. (Admin only)"""
    filename = file.filename
    content_type = file.content_type
    
    # Validate extension
    suffix = filename.split(".")[-1].lower() if "." in filename else ""
    if suffix not in {"pdf", "docx", "txt", "md", "json", "csv", "zip"}:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported file format. Supported: PDF, DOCX, TXT, MD, JSON, CSV, ZIP."
        )

    try:
        # Read file bytes
        file_content = await file.read()
        
        # Load and parse text content
        extra_meta = {
            "department": department,
            "category": category,
            "uploaded_by": current_user.email
        }
        loaded_docs = load_file(file_content, filename, content_type, extra_meta)
        
        if not loaded_docs:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No extractable text was found in the uploaded file."
            )
            
        # Ingest documents using the tested pipeline
        embedding_service = build_embedding_service()
        chunks_count = ingest_documents(
            loaded_docs,
            embedding_service=embedding_service,
            vector_store=vector_store,
        )
        
        return {
            "status": "success",
            "filename": filename,
            "documents_count": len(loaded_docs),
            "chunks_ingested": chunks_count,
            "detail": f"Successfully parsed and ingested {filename}."
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ingestion pipeline failed: {str(e)}"
        )


@router.get("", response_model=List[DocumentResponseSchema])
def list_documents(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Retrieve list of all company documents currently indexed in the knowledge base."""
    stmt = select(Document).order_by(Document.created_at.desc())
    docs = db.execute(stmt).scalars().all()
    return docs


@router.delete("/{id}")
def delete_document(
    id: int,
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    """Delete a document and purge all its associated pgvector chunks. (Admin only)"""
    doc = db.execute(select(Document).where(Document.id == id)).scalar_one_or_none()
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found."
        )

    try:
        # Purge chunks in vector store
        vector_store.delete_document(doc.id)
        # Purge main document record
        db.delete(doc)
        db.commit()
        return {"status": "success", "detail": f"Document '{doc.title}' and all its vector chunks purged."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to purge document: {str(e)}"
        )
