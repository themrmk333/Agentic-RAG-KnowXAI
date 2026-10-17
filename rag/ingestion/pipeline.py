"""Company ZIP to PostgreSQL + pgvector ingestion pipeline."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path
from typing import Any

from database.models import Document
from database.vector_store import PGVectorStore

from rag.chunking.text_chunker import chunk_text
from rag.embeddings.openai_embeddings import OpenAIEmbeddingService
from rag.loaders.company_zip import LoadedDocument, iter_company_documents


def ingest_documents(
    documents: Iterable[LoadedDocument],
    *,
    embedding_service: OpenAIEmbeddingService,
    vector_store: PGVectorStore,
    chunk_size: int = 1200,
    overlap: int = 200,
) -> int:
    """Persist documents and their chunks, returning the number of chunks written."""

    chunks_written = 0
    for loaded in documents:
        chunks = chunk_text(loaded.text, chunk_size=chunk_size, overlap=overlap)
        if not chunks:
            continue
        embeddings = embedding_service.embed(chunks)
        with vector_store.session_factory() as session:
            document = Document(
                title=loaded.title,
                source_path=loaded.source_path,
                content_type=loaded.content_type,
                document_metadata=loaded.metadata,
            )
            session.add(document)
            session.flush()
            document_id = document.id
            session.commit()
        chunks_to_add = []
        for index, (content, embedding) in enumerate(zip(chunks, embeddings, strict=True)):
            chunks_to_add.append((
                index,
                content,
                embedding,
                {**loaded.metadata, "source_path": loaded.source_path},
            ))
        count = vector_store.add_chunks(document_id, chunks_to_add)
        chunks_written += count
    return chunks_written


def ingest_zip(
    zip_path: str | Path,
    *,
    embedding_service: OpenAIEmbeddingService,
    vector_store: PGVectorStore,
    include_prefixes: tuple[str, ...] = (),
    chunk_size: int = 1200,
    overlap: int = 200,
) -> int:
    return ingest_documents(
        iter_company_documents(str(zip_path), include_prefixes=include_prefixes),
        embedding_service=embedding_service,
        vector_store=vector_store,
        chunk_size=chunk_size,
        overlap=overlap,
    )
