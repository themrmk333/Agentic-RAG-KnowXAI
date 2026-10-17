"""Chat endpoints to invoke the Agentic RAG workflow and manage user conversations."""

from typing import Any, Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from api.auth import get_current_user
from database.connection import get_db
from database.models import Conversation, Message, User
from database.vector_store import PGVectorStore

from agents.llm.factory import build_provider
from config.settings import get_settings
from rag.embeddings.factory import build_embedding_service
from rag.retrieval.pgvector_retriever import PGVectorRetriever
from agents.graph.workflow import create_workflow

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequestSchema(BaseModel):
    query: str
    conversation_id: Optional[int] = None


class ChatResponseSchema(BaseModel):
    conversation_id: int
    answer: str
    confidence: float
    references: List[str]
    errors: List[str]
    intent: str
    agent: Optional[str] = None
    user_department: Optional[str] = None


class MessageSchema(BaseModel):
    id: int
    role: str
    content: str
    created_at: Any

    class Config:
        from_attributes = True


class ConversationSchema(BaseModel):
    id: int
    title: Optional[str]
    created_at: Any
    updated_at: Any

    class Config:
        from_attributes = True


class RenameConversationSchema(BaseModel):
    title: str


@router.post("", response_model=ChatResponseSchema)
def ask_question(
    data: ChatRequestSchema,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Ask a question to the Agentic RAG workflow. Results are saved in conversation history."""
    query_text = data.query.strip()
    if not query_text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query content cannot be empty."
        )

    # 1. Fetch or create conversation
    if data.conversation_id:
        conversation = db.execute(
            select(Conversation).where(
                Conversation.id == data.conversation_id,
                Conversation.user_id == current_user.id
            )
        ).scalar_one_or_none()
        if not conversation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Conversation not found or access denied."
            )
    else:
        # Create new conversation
        title = query_text[:50] + ("..." if len(query_text) > 50 else "")
        conversation = Conversation(
            user_id=current_user.id,
            title=title
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)

    # 2. Save user message to database
    user_msg = Message(
        conversation_id=conversation.id,
        role="user",
        content=query_text
    )
    db.add(user_msg)
    db.commit()

    # 3. Initialize and run RAG workflow
    try:
        settings = get_settings()
        llm = build_provider(settings.llm_provider)
        
        from rag.retrieval.semantic_retriever import SemanticRetriever
        retriever = SemanticRetriever(session_factory=lambda: db)
        
        workflow = create_workflow(llm, retriever)
        
        initial_state = {
            "original_query": query_text,
            "errors": [],
            "specialist_results": {},
            "user_context": {
                "id": current_user.id,
                "email": current_user.email,
                "username": current_user.username,
                "role": current_user.role,
                "department": current_user.department,
            }
        }
        
        final_state = workflow.invoke(initial_state)
        
        user_dept = current_user.department or "General"
        intent = final_state.get("intent", "general")
        plan = final_state.get("plan") or []

        # Determine specialist agent name
        specialist_names = [p for p in plan if p not in ("critic", "decision")]
        if specialist_names:
            primary_agent = f"{specialist_names[0].capitalize()} Agent"
        elif intent and intent != "general":
            primary_agent = f"{intent.capitalize()} Agent"
        else:
            primary_agent = "General Assistant"

        # Log safe debugging info
        if settings.debug:
            selected_agents = ", ".join([f"{p.upper()} Agent" for p in plan]) or primary_agent
            
            meta = final_state.get("metadata") or {}
            retrieved_count = meta.get("retrieved_count", 0)
            authorized_count = meta.get("authorized_count", 0)
            
            print("\n[DEBUG LOG]", flush=True)
            print(f"User department:      {user_dept}", flush=True)
            print(f"Question domain:      {intent.upper()}", flush=True)
            print(f"Selected agent:       {selected_agents}", flush=True)
            print(f"RAG domain:           {intent.upper()}", flush=True)
            print(f"Documents retrieved:  {retrieved_count}", flush=True)
            print(f"Authorized documents: {authorized_count}\n", flush=True)

        final_ans = final_state.get("final_answer") or {}
        answer = final_ans.get("answer", "No answer could be compiled.")
        confidence = final_ans.get("confidence", 0.0)
        references = final_ans.get("references", [])
        errors = final_state.get("errors", [])
        
        # 4. Save assistant response as a Message
        assistant_msg = Message(
            conversation_id=conversation.id,
            role="assistant",
            content=answer
        )
        db.add(assistant_msg)
        db.commit()

        return {
            "conversation_id": conversation.id,
            "answer": answer,
            "confidence": confidence,
            "references": references,
            "errors": errors,
            "intent": intent,
            "agent": primary_agent,
            "user_department": user_dept
        }
    except Exception as e:
        # Save error message so the chat UI isn't broken
        error_msg = f"An error occurred while compiling your answer: {str(e)}"
        assistant_msg = Message(
            conversation_id=conversation.id,
            role="assistant",
            content=error_msg
        )
        db.add(assistant_msg)
        db.commit()
        
        return {
            "conversation_id": conversation.id,
            "answer": error_msg,
            "confidence": 0.0,
            "references": [],
            "errors": [str(e)],
            "intent": "general",
            "agent": "General Assistant",
            "user_department": current_user.department or "General"
        }


@router.get("/conversations", response_model=List[ConversationSchema])
def list_conversations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Retrieve all conversations belonging to the current user."""
    stmt = select(Conversation).where(Conversation.user_id == current_user.id).order_by(Conversation.updated_at.desc())
    convs = db.execute(stmt).scalars().all()
    return convs


@router.get("/conversations/{id}", response_model=List[MessageSchema])
def get_conversation_messages(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Retrieve all messages inside a specific conversation."""
    conversation = db.execute(
        select(Conversation).where(
            Conversation.id == id,
            Conversation.user_id == current_user.id
        )
    ).scalar_one_or_none()
    
    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found or access denied."
        )
        
    stmt = select(Message).where(Message.conversation_id == id).order_by(Message.created_at.asc())
    messages = db.execute(stmt).scalars().all()
    return messages


@router.put("/conversations/{id}", response_model=ConversationSchema)
def rename_conversation(
    id: int,
    data: RenameConversationSchema,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Rename conversation title."""
    conversation = db.execute(
        select(Conversation).where(
            Conversation.id == id,
            Conversation.user_id == current_user.id
        )
    ).scalar_one_or_none()
    
    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found or access denied."
        )
        
    conversation.title = data.title.strip()
    db.commit()
    db.refresh(conversation)
    return conversation


@router.delete("/conversations/{id}")
def delete_conversation(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a conversation and all its messages."""
    conversation = db.execute(
        select(Conversation).where(
            Conversation.id == id,
            Conversation.user_id == current_user.id
        )
    ).scalar_one_or_none()
    
    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found or access denied."
        )
        
    db.delete(conversation)
    db.commit()
    return {"status": "success", "detail": "Conversation deleted successfully."}
