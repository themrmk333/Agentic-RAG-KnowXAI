"""Update vector dimensions from 1536 to 384 for BAAI/bge-small-en-v1.5.

Revision ID: 0002_vector_dim_384
Revises: 0001_rag_documents
Create Date: 2026-08-29
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector

revision = "0002_vector_dim_384"
down_revision = "0001_rag_documents"
branch_labels = None
depends_on = None

NEW_VECTOR_DIMENSIONS = 384


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    
    # Clear old incompatible 1536-D demo rows to allow clean column type alteration
    op.execute("DELETE FROM document_embeddings WHERE embedding IS NOT NULL;")
    op.execute("DELETE FROM document_chunks WHERE embedding IS NOT NULL;")
    
    # Alter column type to vector(384)
    op.execute(f"ALTER TABLE document_chunks ALTER COLUMN embedding TYPE vector({NEW_VECTOR_DIMENSIONS});")
    op.execute(f"ALTER TABLE document_embeddings ALTER COLUMN embedding TYPE vector({NEW_VECTOR_DIMENSIONS});")
    
    # Create HNSW index for high performance cosine similarity search
    op.execute("""
        CREATE INDEX IF NOT EXISTS ix_document_chunks_embedding_cosine 
        ON document_chunks USING hnsw (embedding vector_cosine_ops);
    """)


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_document_chunks_embedding_cosine;")
    op.execute("DELETE FROM document_embeddings WHERE embedding IS NOT NULL;")
    op.execute("DELETE FROM document_chunks WHERE embedding IS NOT NULL;")
    op.execute("ALTER TABLE document_chunks ALTER COLUMN embedding TYPE vector(1536);")
    op.execute("ALTER TABLE document_embeddings ALTER COLUMN embedding TYPE vector(1536);")
