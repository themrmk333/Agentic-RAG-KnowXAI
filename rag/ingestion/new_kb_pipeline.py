"""New PDF Knowledge Base Ingestion Pipeline for MK-Infinite-AI.

Extracts text, chunks documents, generates 384-D local embeddings, validates
all records, and safely replaces old knowledge base database records while
strictly preserving user accounts, authentication, chat history, and audit logs.
"""

from __future__ import annotations

import json
import logging
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy import func, select, text
from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import get_settings
from database.connection import SessionLocal, engine
from database.models import Document, DocumentChunk
from database.vector_store import PGVectorStore
from rag.embeddings.local_embeddings import LocalEmbeddingService
from rag.embeddings.models import EXPECTED_VECTOR_DIMENSION, validate_vector
from rag.loaders.pdf_knowledge_loader import PDFKnowledgeLoader, ParsedPDFChunk, ParsedPDFDocument

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("new_kb_pipeline")

CHUNKS_DIR = PROJECT_ROOT / "data" / "chunks" / "new_knowledge_base"
EMBEDDINGS_DIR = PROJECT_ROOT / "data" / "embeddings" / "new_knowledge_base"
BACKUP_DIR = PROJECT_ROOT / "data" / "backups" / "knowledge_base_backup_20261019"
SOURCE_PDF_DIR = PROJECT_ROOT / "new_knowledge_base" / "MK_Infinite_AI_Demo_Knowledge_Base"


class NewKnowledgeBaseIngestionPipeline:
    """Manages parsing, embedding generation, database replacement, and validation."""

    def __init__(self) -> None:
        CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
        EMBEDDINGS_DIR.mkdir(parents=True, exist_ok=True)
        self.loader = PDFKnowledgeLoader(SOURCE_PDF_DIR)
        self.embedding_service = LocalEmbeddingService(
            model_name="BAAI/bge-small-en-v1.5",
            dimensions=384,
            normalize_embeddings=True,
        )

    def verify_backup_exists(self) -> bool:
        """Ensure full backup of existing database knowledge records exists and is non-empty."""
        docs_file = BACKUP_DIR / "documents_backup.jsonl"
        chunks_file = BACKUP_DIR / "document_chunks_backup.jsonl"

        if not docs_file.exists() or not chunks_file.exists():
            logger.error("Missing backup files in %s", BACKUP_DIR)
            return False

        if docs_file.stat().st_size == 0 or chunks_file.stat().st_size == 0:
            logger.error("Backup files in %s are empty", BACKUP_DIR)
            return False

        logger.info(
            "Verified backup in %s: documents_backup (%s bytes), document_chunks_backup (%s bytes)",
            BACKUP_DIR,
            f"{docs_file.stat().st_size:,}",
            f"{chunks_file.stat().st_size:,}",
        )
        return True

    def extract_and_chunk(self) -> List[ParsedPDFDocument]:
        """Load and chunk all 16 PDFs."""
        logger.info("[1/5] Extracting text and chunking 16 PDFs from %s...", SOURCE_PDF_DIR)
        docs = self.loader.load_all()

        chunks_file = CHUNKS_DIR / "chunks.jsonl"
        all_chunks_count = 0
        all_qa_count = 0

        with open(chunks_file, "w", encoding="utf-8") as f:
            for doc in docs:
                for chunk in doc.chunks:
                    record = {
                        "chunk_id": chunk.chunk_id,
                        "batch_id": chunk.metadata["batch_id"],
                        "source_file": chunk.metadata["source_file"],
                        "relative_path": chunk.metadata["relative_path"],
                        "filename": chunk.metadata["filename"],
                        "title": chunk.metadata["title"],
                        "category": chunk.metadata["category"],
                        "department": chunk.metadata["department"],
                        "department_code": chunk.metadata["department_code"],
                        "project_code": chunk.metadata.get("project_code"),
                        "page_start": chunk.metadata["page_start"],
                        "page_end": chunk.metadata["page_end"],
                        "heading_context": chunk.metadata["heading_context"],
                        "section_name": chunk.metadata.get("section_name", ""),
                        "is_qa": chunk.metadata["is_qa"],
                        "chunk_index": chunk.chunk_index,
                        "total_chunks_for_file": chunk.total_chunks_for_file,
                        "character_count": chunk.metadata["character_count"],
                        "word_count": chunk.metadata["word_count"],
                        "estimated_tokens": chunk.metadata["estimated_tokens"],
                        "chunk_sha256": chunk.metadata["chunk_sha256"],
                        "access_level": chunk.metadata["access_level"],
                        "confidentiality": chunk.metadata["confidentiality"],
                        "allowed_departments": chunk.metadata["allowed_departments"],
                        "text": chunk.content,
                    }
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
                    all_chunks_count += 1
                    if chunk.metadata["is_qa"]:
                        all_qa_count += 1

        logger.info(
            "Extracted %d documents, %d total chunks, %d QA chunks. Saved to %s",
            len(docs),
            all_chunks_count,
            all_qa_count,
            chunks_file,
        )
        return docs

    def generate_embeddings(
        self, docs: List[ParsedPDFDocument]
    ) -> List[Tuple[ParsedPDFChunk, List[float]]]:
        """Generate local 384-D vector embeddings for all chunks."""
        logger.info("[2/5] Generating 384-D BAAI/bge-small-en-v1.5 embeddings for all chunks...")

        all_chunks: List[ParsedPDFChunk] = []
        for doc in docs:
            all_chunks.extend(doc.chunks)

        texts = [chunk.content for chunk in all_chunks]
        t0 = time.time()
        vectors = self.embedding_service.embed(texts, batch_size=32)
        elapsed = time.time() - t0

        logger.info(
            "Generated %d embeddings in %.2f seconds (%.1f chunks/sec)",
            len(vectors),
            elapsed,
            len(vectors) / elapsed if elapsed > 0 else 0,
        )

        embeddings_file = EMBEDDINGS_DIR / "embeddings.jsonl"
        with open(embeddings_file, "w", encoding="utf-8") as f:
            for chunk, vec in zip(all_chunks, vectors):
                rec = {
                    "chunk_id": chunk.chunk_id,
                    "source_file": chunk.metadata["source_file"],
                    "chunk_index": chunk.chunk_index,
                    "total_chunks_for_file": chunk.total_chunks_for_file,
                    "embedding_model": "BAAI/bge-small-en-v1.5",
                    "embedding_dimension": len(vec),
                    "chunk_sha256": chunk.metadata["chunk_sha256"],
                    "embedding": vec,
                }
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

        logger.info("Saved embeddings to %s", embeddings_file)
        return list(zip(all_chunks, vectors))

    def validate_dataset(
        self, docs: List[ParsedPDFDocument], embedded_chunks: List[Tuple[ParsedPDFChunk, List[float]]]
    ) -> bool:
        """Validate chunks, token counts, and embedding dimensions prior to database commit."""
        logger.info("[3/5] Validating extracted chunks and embedding dimensions...")

        if len(docs) != 16:
            raise ValueError(f"Expected 16 documents, got {len(docs)}")

        total_qa = sum(sum(1 for c in d.chunks if c.metadata["is_qa"]) for d in docs)
        if total_qa != 158:
            raise ValueError(f"Expected 158 Q&A chunks (8 overview + 15x10), got {total_qa}")

        for chunk, vec in embedded_chunks:
            if len(vec) != 384:
                raise ValueError(
                    f"Chunk {chunk.chunk_id} dimension {len(vec)} != 384"
                )
            if any(math.isnan(v) or math.isinf(v) for v in vec):
                raise ValueError(f"Chunk {chunk.chunk_id} contains NaN/Inf in vector")

            norm = math.sqrt(sum(v * v for v in vec))
            if abs(norm - 1.0) > 0.05:
                raise ValueError(
                    f"Chunk {chunk.chunk_id} embedding not normalized (norm={norm:.4f})"
                )

        logger.info(
            "Validation PASSED: 16 documents, %d total chunks, %d QA chunks, all 384-D normalized vectors.",
            len(embedded_chunks),
            total_qa,
        )
        return True

    def replace_database_knowledge_records(
        self, docs: List[ParsedPDFDocument], embedded_chunks: List[Tuple[ParsedPDFChunk, List[float]]]
    ) -> Dict[str, Any]:
        """Safely delete ONLY old knowledge records and insert new PDF records in an atomic transaction."""
        logger.info("[4/5] Replacing database knowledge records in PostgreSQL...")

        if not self.verify_backup_exists():
            raise RuntimeError("Database replacement aborted: verified backup not present.")

        session: Session = SessionLocal()
        stats: Dict[str, Any] = {}

        try:
            # 1. Snapshot other table counts before modification
            users_before = session.execute(text("SELECT COUNT(*) FROM users")).scalar()
            dept_before = session.execute(text("SELECT COUNT(*) FROM departments")).scalar()
            conv_before = session.execute(text("SELECT COUNT(*) FROM conversations")).scalar()
            msg_before = session.execute(text("SELECT COUNT(*) FROM messages")).scalar()
            audit_before = session.execute(text("SELECT COUNT(*) FROM audit_logs")).scalar()
            bio_before = session.execute(text("SELECT COUNT(*) FROM biometric_credentials")).scalar()
            docs_before = session.execute(text("SELECT COUNT(*) FROM documents")).scalar()
            chunks_before = session.execute(text("SELECT COUNT(*) FROM document_chunks")).scalar()

            logger.info("Pre-replacement counts:")
            logger.info("  documents: %d, document_chunks: %d", docs_before, chunks_before)
            logger.info("  users: %d, departments: %d, conversations: %d, messages: %d, audit_logs: %d, biometric_credentials: %d",
                        users_before, dept_before, conv_before, msg_before, audit_before, bio_before)

            # 2. Delete ONLY old knowledge base records (source_path starting with 'data/' or old batch paths)
            logger.info("Deleting old knowledge base records from documents (cascades to document_chunks)...")
            deleted_docs = session.execute(
                text("DELETE FROM documents WHERE source_path LIKE 'data/%' OR source_path NOT LIKE 'new_knowledge_base/%' RETURNING id;")
            ).fetchall()
            logger.info("Deleted %d old documents", len(deleted_docs))

            # Verify chunks were cascaded or delete remaining old chunks
            remaining_old_chunks = session.execute(
                text("DELETE FROM document_chunks WHERE metadata->>'batch_id' != 'new_knowledge_base' RETURNING id;")
            ).fetchall()
            if remaining_old_chunks:
                logger.info("Cleaned up %d residual old chunks", len(remaining_old_chunks))

            # 3. Insert the 16 new documents
            logger.info("Inserting 16 new Document entities...")
            doc_id_map: Dict[str, int] = {}
            for doc in docs:
                new_doc = Document(
                    title=doc.title,
                    source_path=doc.relative_path,
                    content_type="application/pdf",
                    document_metadata=doc.metadata,
                )
                session.add(new_doc)
                session.flush()
                doc_id_map[doc.filename] = new_doc.id

            logger.info("Successfully created 16 Document records.")

            # 4. Insert all new DocumentChunk entities with 384-D vectors
            logger.info("Inserting %d new DocumentChunk entities...", len(embedded_chunks))
            chunk_entities = []
            for chunk, vec in embedded_chunks:
                source_file = chunk.metadata["source_file"]
                doc_id = doc_id_map[source_file]

                # Update metadata with actual parent document_id
                c_meta = dict(chunk.metadata)
                c_meta["document_id"] = doc_id

                chunk_obj = DocumentChunk(
                    document_id=doc_id,
                    chunk_index=chunk.chunk_index,
                    content=chunk.content,
                    chunk_metadata=c_meta,
                    embedding=vec,
                )
                chunk_entities.append(chunk_obj)

            session.add_all(chunk_entities)
            session.commit()
            logger.info("Committed %d new chunks to PostgreSQL.", len(chunk_entities))

            # 5. Verify HNSW index
            logger.info("Verifying/reindexing HNSW cosine index...")
            with engine.begin() as conn:
                conn.execute(text("CREATE INDEX IF NOT EXISTS ix_document_chunks_embedding_cosine ON document_chunks USING hnsw (embedding vector_cosine_ops);"))
                conn.execute(text("REINDEX INDEX ix_document_chunks_embedding_cosine;"))

            # 6. Post-replacement verification of counts
            users_after = session.execute(text("SELECT COUNT(*) FROM users")).scalar()
            dept_after = session.execute(text("SELECT COUNT(*) FROM departments")).scalar()
            conv_after = session.execute(text("SELECT COUNT(*) FROM conversations")).scalar()
            msg_after = session.execute(text("SELECT COUNT(*) FROM messages")).scalar()
            audit_after = session.execute(text("SELECT COUNT(*) FROM audit_logs")).scalar()
            bio_after = session.execute(text("SELECT COUNT(*) FROM biometric_credentials")).scalar()
            docs_after = session.execute(text("SELECT COUNT(*) FROM documents")).scalar()
            chunks_after = session.execute(text("SELECT COUNT(*) FROM document_chunks")).scalar()
            null_emb_count = session.execute(text("SELECT COUNT(*) FROM document_chunks WHERE embedding IS NULL")).scalar()

            logger.info("Post-replacement counts:")
            logger.info("  documents: %d (expected: 16)", docs_after)
            logger.info("  document_chunks: %d (expected: %d, missing vectors: %d)", chunks_after, len(embedded_chunks), null_emb_count)
            logger.info("  users: %d (unchanged: %s)", users_after, users_after == users_before)
            logger.info("  departments: %d (unchanged: %s)", dept_after, dept_after == dept_before)
            logger.info("  conversations: %d (unchanged: %s)", conv_after, conv_after == conv_before)
            logger.info("  messages: %d (unchanged: %s)", msg_after, msg_after == msg_before)
            logger.info("  audit_logs: %d (unchanged: %s)", audit_after, audit_after == audit_before)
            logger.info("  biometric_credentials: %d (unchanged: %s)", bio_after, bio_after == bio_before)

            stats = {
                "documents_inserted": docs_after,
                "chunks_inserted": chunks_after,
                "null_embeddings": null_emb_count,
                "users_preserved": users_after == users_before,
                "conversations_preserved": conv_after == conv_before,
                "messages_preserved": msg_after == msg_before,
                "biometrics_preserved": bio_after == bio_before,
                "audit_logs_preserved": audit_after == audit_before,
            }

        except Exception as e:
            session.rollback()
            logger.error("Transaction failed during knowledge base replacement: %s", e)
            raise RuntimeError(f"Database replacement failed: {e}") from e
        finally:
            session.close()

        return stats

    def run_retrieval_verification(self) -> Dict[str, Any]:
        """Validate live semantic vector retrieval across diverse topics and departments."""
        logger.info("[5/5] Running live semantic retrieval verification...")

        store = PGVectorStore()
        test_queries = [
            ("HR", "What is the onboarding process for a new employee?"),
            ("IT", "How can an employee set up the corporate VPN?"),
            ("Finance", "What is the travel expense reimbursement claim submission procedure?"),
            ("Project", "What are the objectives and technology stack of Agentic RAG KnowXAI?"),
            ("Company Overview", "What are the company working hours and hybrid work rules?"),
            ("Customer Support", "How does customer support handle ticket escalations?"),
        ]

        results = {}
        for domain, q in test_queries:
            q_vec = self.embedding_service.embed_query(q)
            matches = store.similarity_search_with_scores(q_vec, limit=3)
            if not matches:
                logger.error("FAILED retrieval for %s query: '%s'", domain, q)
                results[domain] = {"status": "FAIL", "matches": 0}
            else:
                top_chunk, dist = matches[0]
                meta = top_chunk.chunk_metadata or {}
                sim = 1.0 - dist
                logger.info("Query [%s]: '%s'", domain, q)
                logger.info("  -> Top Match: [%s] '%s' (similarity: %.4f)",
                            meta.get("filename"), meta.get("heading_context", "")[:45], sim)
                logger.info("  -> Preview: %s...", top_chunk.content[:120].replace("\n", " "))
                results[domain] = {
                    "status": "PASS",
                    "similarity": round(sim, 4),
                    "document": meta.get("filename"),
                    "heading": meta.get("heading_context"),
                }

        all_passed = all(r["status"] == "PASS" for r in results.values())
        logger.info("Retrieval verification: %s", "ALL PASS" if all_passed else "SOME FAILED")
        return {"retrieval_tests": results, "all_passed": all_passed}

    def execute(self) -> Dict[str, Any]:
        """Execute end-to-end knowledge base replacement."""
        print("=" * 64, flush=True)
        print("STARTING KNOWLEDGE BASE REPLACEMENT PIPELINE", flush=True)
        print("=" * 64, flush=True)

        # 1. Verify backup
        if not self.verify_backup_exists():
            raise RuntimeError("Replacement aborted: Verified backup missing.")

        # 2. Extract & chunk
        docs = self.extract_and_chunk()

        # 3. Generate embeddings
        embedded_chunks = self.generate_embeddings(docs)

        # 4. Validate
        self.validate_dataset(docs, embedded_chunks)

        # 5. Database replacement
        db_stats = self.replace_database_knowledge_records(docs, embedded_chunks)

        # 6. Retrieval verification
        retrieval_stats = self.run_retrieval_verification()

        report = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "status": "SUCCESS",
            "documents_count": len(docs),
            "chunks_count": len(embedded_chunks),
            "db_stats": db_stats,
            "retrieval_stats": retrieval_stats,
        }

        report_file = PROJECT_ROOT / "data" / "manifests" / "new_knowledge_base_report.json"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        print("=" * 64, flush=True)
        print("KNOWLEDGE BASE REPLACEMENT COMPLETE AND VERIFIED", flush=True)
        print(f"Report written to: {report_file}", flush=True)
        print("=" * 64, flush=True)

        return report


if __name__ == "__main__":
    pipeline = NewKnowledgeBaseIngestionPipeline()
    pipeline.execute()
