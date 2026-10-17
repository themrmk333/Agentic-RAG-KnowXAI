"""Step 5: PostgreSQL + pgvector Ingestion Pipeline for Enterprise RAG.

Safely loads Step 4 local embeddings (BAAI/bge-small-en-v1.5, dim=384)
and source chunk text/metadata into PostgreSQL using pgvector VECTOR(384).
"""

from __future__ import annotations

import json
import math
import os
import re
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from sqlalchemy import func, insert, select, text
from sqlalchemy.orm import Session

from config.settings import get_settings
from database.connection import SessionLocal, engine, get_database_url
from database.models import Document, DocumentChunk

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass
class IngestionConfig:
    """Runtime configuration for Step 5 Ingestion."""
    chunks_dir: Path = PROJECT_ROOT / "data" / "chunks"
    embeddings_dir: Path = PROJECT_ROOT / "data" / "embeddings" / "step4" / "embeddings"
    checkpoint_dir: Path = PROJECT_ROOT / "data" / "embeddings" / "step5" / "checkpoints"
    reports_dir: Path = PROJECT_ROOT / "data" / "embeddings" / "step5" / "reports"
    expected_dimension: int = 384
    expected_total_chunks: int = 21296
    batch_size: int = 1000
    model_name: str = "BAAI/bge-small-en-v1.5"
    provider: str = "local"


@dataclass
class IngestionRecord:
    """Combined chunk + embedding record ready for DB ingestion."""
    chunk_id: str
    batch_id: str
    source_file: str
    chunk_index: int
    content: str
    embedding: List[float]
    metadata: Dict[str, Any] = field(default_factory=dict)
    document_title: str = ""
    document_source_path: str = ""
    content_type: str = "text/markdown"


def extract_frontmatter_metadata(content: str) -> Dict[str, Any]:
    """Extract metadata from JSON frontmatter embedded in chunk content if present."""
    if not content:
        return {}
    match = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except Exception:
            return {}
    return {}


class Step5IngestionPipeline:
    """Manages loading, validation, and idempotent ingestion into PostgreSQL."""

    def __init__(self, config: Optional[IngestionConfig] = None):
        self.config = config or IngestionConfig()
        self.config.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.config.reports_dir.mkdir(parents=True, exist_ok=True)
        self.checkpoint_file = self.config.checkpoint_dir / "checkpoint.json"

    def load_source_chunks(self) -> Dict[str, Dict[str, Any]]:
        """Load all chunks from data/chunks/ indexed by chunk_id."""
        chunks_by_id: Dict[str, Dict[str, Any]] = {}
        jsonl_files = sorted(self.config.chunks_dir.glob("**/chunks.jsonl"))
        if not jsonl_files:
            jsonl_files = sorted(self.config.chunks_dir.glob("*.jsonl"))

        for file_path in jsonl_files:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    record = json.loads(line)
                    chunk_id = record.get("chunk_id")
                    if chunk_id:
                        chunks_by_id[chunk_id] = record
        return chunks_by_id

    def load_embeddings(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Load Step 4 embeddings from data/embeddings/step4/embeddings/."""
        embeddings: List[Dict[str, Any]] = []
        jsonl_files = sorted(self.config.embeddings_dir.glob("**/embeddings.jsonl"))
        if not jsonl_files:
            jsonl_files = sorted(self.config.embeddings_dir.glob("*.jsonl"))

        for file_path in jsonl_files:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    record = json.loads(line)
                    embeddings.append(record)
                    if limit and len(embeddings) >= limit:
                        return embeddings
        return embeddings

    def prepare_ingestion_records(
        self,
        embeddings: List[Dict[str, Any]],
        chunks_by_id: Dict[str, Dict[str, Any]],
    ) -> Tuple[List[IngestionRecord], List[str]]:
        """Validate and join embeddings with source chunks."""
        records: List[IngestionRecord] = []
        validation_errors: List[str] = []
        seen_chunk_ids: Set[str] = set()

        for idx, emb_record in enumerate(embeddings):
            chunk_id = emb_record.get("chunk_id")
            if not chunk_id:
                validation_errors.append(f"Record #{idx}: missing chunk_id")
                continue

            if chunk_id in seen_chunk_ids:
                validation_errors.append(f"Record #{idx}: duplicate chunk_id '{chunk_id}'")
                continue
            seen_chunk_ids.add(chunk_id)

            vec = emb_record.get("embedding")
            if not isinstance(vec, list):
                validation_errors.append(f"Record '{chunk_id}': embedding is not a list")
                continue

            if len(vec) != self.config.expected_dimension:
                validation_errors.append(
                    f"Record '{chunk_id}': dimension {len(vec)} != expected {self.config.expected_dimension}"
                )
                continue

            # Check for NaN / Inf
            has_invalid_num = any(math.isnan(v) or math.isinf(v) for v in vec)
            if has_invalid_num:
                validation_errors.append(f"Record '{chunk_id}': contains NaN or Inf values")
                continue

            source_chunk = chunks_by_id.get(chunk_id)
            if not source_chunk:
                validation_errors.append(f"Record '{chunk_id}': no matching source chunk in data/chunks/")
                continue

            content = source_chunk.get("text", "")
            source_file = emb_record.get("source_file") or source_chunk.get("source_file", "")
            chunk_index = emb_record.get("chunk_index", source_chunk.get("chunk_index", 0))
            batch_id = emb_record.get("batch_id", source_chunk.get("batch_id", "batch_01"))

            # Build rich metadata preserving security and document fields
            frontmatter = extract_frontmatter_metadata(content)
            metadata = {
                "chunk_id": chunk_id,
                "batch_id": batch_id,
                "source_file": source_file,
                "relative_path": source_chunk.get("relative_path", source_file),
                "filename": source_chunk.get("filename", Path(source_file).name),
                "extension": source_chunk.get("extension", Path(source_file).suffix),
                "chunk_index": chunk_index,
                "total_chunks_for_file": emb_record.get("total_chunks_for_file", 1),
                "chunk_sha256": emb_record.get("chunk_sha256", ""),
                "source_sha256": source_chunk.get("source_sha256", ""),
                "heading_context": source_chunk.get("heading_context", ""),
                "chunking_strategy": source_chunk.get("chunking_strategy", "MarkdownChunker"),
                "embedding_model": emb_record.get("embedding_model", self.config.model_name),
                "embedding_dimension": len(vec),
            }

            # Merge frontmatter security and organizational attributes
            for k in [
                "document_id", "title", "document_type", "department", "category",
                "roles", "access_level", "allowed_departments", "confidentiality",
                "keywords", "created_date", "updated_date", "version", "status",
                "owner", "tenant", "tenant_id", "source"
            ]:
                if k in frontmatter:
                    metadata[k] = frontmatter[k]

            doc_title = frontmatter.get("title") or Path(source_file).stem
            doc_source_path = source_file
            content_type = "application/json" if source_file.endswith(".json") else "text/markdown"

            records.append(
                IngestionRecord(
                    chunk_id=chunk_id,
                    batch_id=batch_id,
                    source_file=source_file,
                    chunk_index=chunk_index,
                    content=content,
                    embedding=vec,
                    metadata=metadata,
                    document_title=doc_title,
                    document_source_path=doc_source_path,
                    content_type=content_type,
                )
            )

        return records, validation_errors

    def get_existing_db_chunk_ids(self, session: Session) -> Set[str]:
        """Fetch all chunk_ids currently stored in document_chunks."""
        stmt = text("SELECT (metadata->>'chunk_id') AS chunk_id FROM document_chunks WHERE metadata->>'chunk_id' IS NOT NULL;")
        rows = session.execute(stmt).fetchall()
        return {r[0] for r in rows if r[0]}

    def run(
        self,
        limit: Optional[int] = None,
        batch_size: Optional[int] = None,
        resume: bool = True,
    ) -> Dict[str, Any]:
        """Execute the Step 5 Ingestion Pipeline."""
        start_time = time.time()
        batch_size = batch_size or self.config.batch_size

        print("=" * 62, flush=True)
        print("STEP 5 - POSTGRESQL + PGVECTOR INGESTION PIPELINE", flush=True)
        print("=" * 62, flush=True)
        print(f"Project root      : {PROJECT_ROOT}", flush=True)
        print(f"Chunks directory  : {self.config.chunks_dir}", flush=True)
        print(f"Embeddings dir    : {self.config.embeddings_dir}", flush=True)
        print(f"Model             : {self.config.model_name}", flush=True)
        print(f"Dimension         : {self.config.expected_dimension}", flush=True)
        print(f"Batch size        : {batch_size}", flush=True)
        print(f"Limit / Test mode : {limit or 'FULL (12,730 chunks)'}", flush=True)
        print(f"Resume enabled    : {resume}", flush=True)
        print("=" * 62, flush=True)

        # 1. Load source chunks & embeddings
        print("[1/5] Loading source chunks and embeddings...", flush=True)
        chunks_by_id = self.load_source_chunks()
        print(f"  Loaded {len(chunks_by_id):,} source chunks from {self.config.chunks_dir}", flush=True)

        embeddings = self.load_embeddings(limit=limit)
        print(f"  Loaded {len(embeddings):,} embeddings from {self.config.embeddings_dir}", flush=True)

        # 2. Validate & join
        print("[2/5] Validating embeddings and joining metadata...", flush=True)
        records, errors = self.prepare_ingestion_records(embeddings, chunks_by_id)
        if errors:
            print(f"ERROR: {len(errors)} validation errors detected:", flush=True)
            for err in errors[:10]:
                print(f"  - {err}", flush=True)
            raise ValueError(f"Step 5 Ingestion aborted: {len(errors)} invalid records.")
        print(f"  Validation passed: {len(records):,} records ready for ingestion.", flush=True)

        # 3. Check database connectivity & existing rows
        print("[3/5] Checking database connection and resolving documents...", flush=True)
        doc_cache: Dict[str, int] = {}
        with SessionLocal() as session:
            existing_ids = self.get_existing_db_chunk_ids(session)
            print(f"  Found {len(existing_ids):,} existing chunk IDs in PostgreSQL.", flush=True)

            # Load document cache
            docs = session.execute(select(Document.source_path, Document.id)).all()
            for s_path, d_id in docs:
                if s_path:
                    doc_cache[s_path] = d_id

            # Bulk pre-populate missing Document entities
            unique_new_docs: Dict[str, Tuple[str, str, Dict[str, Any]]] = {}
            for rec in records:
                if rec.document_source_path not in doc_cache and rec.document_source_path not in unique_new_docs:
                    unique_new_docs[rec.document_source_path] = (rec.document_title, rec.content_type, rec.metadata)

            if unique_new_docs:
                print(f"  Bulk inserting {len(unique_new_docs):,} new Document entities...", flush=True)
                new_doc_entities = [
                    Document(
                        title=title,
                        source_path=s_path,
                        content_type=ctype,
                        document_metadata=meta,
                    )
                    for s_path, (title, ctype, meta) in unique_new_docs.items()
                ]
                session.add_all(new_doc_entities)
                session.commit()

                # Refresh doc cache
                docs = session.execute(select(Document.source_path, Document.id)).all()
                for s_path, d_id in docs:
                    if s_path:
                        doc_cache[s_path] = d_id

            print(f"  Document cache loaded with {len(doc_cache):,} documents.", flush=True)

        # Filter records if resuming
        to_insert: List[IngestionRecord] = []
        skipped_count = 0
        for rec in records:
            if resume and rec.chunk_id in existing_ids:
                skipped_count += 1
            else:
                to_insert.append(rec)

        print(f"  Records to insert: {len(to_insert):,} (Skipped already existing: {skipped_count:,})", flush=True)

        if not to_insert:
            print("  All records already present in database. Skipping chunk insertion.", flush=True)

        # 4. Ingest in bulk transactional batches
        inserted_count = 0
        failed_count = 0
        total_batches = (len(to_insert) + batch_size - 1) // batch_size if to_insert else 0

        if to_insert:
            print(f"[4/5] Ingesting {len(to_insert):,} records in batches of {batch_size}...", flush=True)
            
            # Temporarily drop index during large bulk insert to accelerate write speed
            if len(to_insert) > 100:
                print("  Temporarily dropping HNSW index during bulk load for maximum throughput...", flush=True)
                with SessionLocal() as session:
                    session.execute(text("DROP INDEX IF EXISTS ix_document_chunks_embedding_cosine;"))
                    session.commit()

            ingest_start = time.time()
            for b_idx in range(total_batches):
                b_start = b_idx * batch_size
                b_end = min(b_start + batch_size, len(to_insert))
                batch_records = to_insert[b_start:b_end]

                try:
                    with SessionLocal() as session:
                        chunk_dicts = [
                            {
                                "document_id": doc_cache[rec.document_source_path],
                                "chunk_index": rec.chunk_index,
                                "content": rec.content,
                                "chunk_metadata": rec.metadata,
                                "embedding": rec.embedding,
                            }
                            for rec in batch_records
                        ]
                        stmt = insert(DocumentChunk)
                        session.execute(stmt, chunk_dicts)
                        session.commit()
                        inserted_count += len(batch_records)

                    # Progress reporting
                    elapsed = time.time() - ingest_start
                    pct = (inserted_count / len(to_insert) * 100) if to_insert else 100.0
                    speed = inserted_count / elapsed if elapsed > 0 else 0.0
                    print(
                        f"  --> Progress: {inserted_count:,}/{len(to_insert):,} inserted ({pct:.1f}%) | "
                        f"Batch: {b_idx + 1}/{total_batches} | Elapsed: {elapsed:.1f}s | Speed: {speed:.1f} records/s",
                        flush=True
                    )

                except Exception as exc:
                    failed_count += len(batch_records)
                    print(f"ERROR in batch {b_idx + 1}: {exc}", flush=True)
                    raise

            # Recreate HNSW index after bulk load
            if len(to_insert) > 100:
                print("  Rebuilding HNSW index on document_chunks (embedding)...", flush=True)
                idx_t0 = time.time()
                with SessionLocal() as session:
                    session.execute(text("""
                        CREATE INDEX IF NOT EXISTS ix_document_chunks_embedding_cosine 
                        ON document_chunks USING hnsw (embedding vector_cosine_ops);
                    """))
                    session.commit()
                print(f"  HNSW index rebuilt successfully in {time.time() - idx_t0:.2f} s.", flush=True)

        total_time = time.time() - start_time
        avg_throughput = inserted_count / total_time if total_time > 0 else 0.0

        # 5. Write Checkpoint
        checkpoint_data = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "model": self.config.model_name,
            "dimension": self.config.expected_dimension,
            "total_processed": len(records),
            "inserted_count": inserted_count,
            "skipped_count": skipped_count,
            "failed_count": failed_count,
            "status": "COMPLETED",
        }
        with open(self.checkpoint_file, "w", encoding="utf-8") as f:
            json.dump(checkpoint_data, f, indent=2)

        # Generate summary report
        report_data = {
            "embedding_model": self.config.model_name,
            "dimension": self.config.expected_dimension,
            "total_input_embeddings": len(embeddings),
            "total_source_chunks": len(chunks_by_id),
            "records_inserted": inserted_count,
            "records_skipped": skipped_count,
            "records_failed": failed_count,
            "execution_time_seconds": round(total_time, 2),
            "average_throughput_records_sec": round(avg_throughput, 2),
            "status": "PASS",
        }
        report_file = self.config.reports_dir / "step5_ingestion_report.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2)

        print("\n" + "=" * 62, flush=True)
        print("STEP 5 - POSTGRESQL INGESTION RUN COMPLETE", flush=True)
        print("=" * 62, flush=True)
        print(f"Total processed       : {len(records):,}", flush=True)
        print(f"Records inserted      : {inserted_count:,}", flush=True)
        print(f"Records skipped       : {skipped_count:,}", flush=True)
        print(f"Records failed        : {failed_count:,}", flush=True)
        print(f"Ingestion time        : {total_time:.2f} s", flush=True)
        print(f"Average throughput    : {avg_throughput:.1f} records/s", flush=True)
        print(f"Checkpoint status     : VALID ({self.checkpoint_file})", flush=True)
        print(f"Report path           : {report_file}", flush=True)
        print("=" * 62, flush=True)

        return report_data
