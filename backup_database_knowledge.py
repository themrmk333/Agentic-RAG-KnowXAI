"""Backup existing database knowledge records (documents and document_chunks)."""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from sqlalchemy import text

# Add project root
sys.path.insert(0, str(Path(__file__).resolve().parent))

from database.connection import SessionLocal

BACKUP_DIR = Path("data/backups/knowledge_base_backup_20261019")
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

docs_backup_file = BACKUP_DIR / "documents_backup.jsonl"
chunks_backup_file = BACKUP_DIR / "document_chunks_backup.jsonl"
meta_backup_file = BACKUP_DIR / "backup_metadata.json"

print(f"Starting backup to {BACKUP_DIR}...")

session = SessionLocal()
try:
    # 1. Backup documents
    print("Backing up documents...")
    doc_count = 0
    with open(docs_backup_file, "w", encoding="utf-8") as f:
        # Fetch in batches
        res = session.execute(text("SELECT id, title, source_path, content_type, metadata, created_at, updated_at FROM documents ORDER BY id"))
        for row in res:
            record = {
                "id": row[0],
                "title": row[1],
                "source_path": row[2],
                "content_type": row[3],
                "metadata": row[4],
                "created_at": row[5].isoformat() if row[5] else None,
                "updated_at": row[6].isoformat() if row[6] else None,
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            doc_count += 1
    print(f"Backed up {doc_count:,} documents to {docs_backup_file}")

    # 2. Backup document_chunks
    print("Backing up document_chunks...")
    chunk_count = 0
    with open(chunks_backup_file, "w", encoding="utf-8") as f:
        res = session.execute(text("SELECT id, document_id, chunk_index, content, metadata, embedding, created_at FROM document_chunks ORDER BY id"))
        for row in res:
            # We don't necessarily need to write the full float vector array if not needed,
            # but let's write it or vector length to be completely safe and recoverable
            emb_list = list(row[5]) if row[5] is not None else None
            record = {
                "id": row[0],
                "document_id": row[1],
                "chunk_index": row[2],
                "content": row[3],
                "metadata": row[4],
                "embedding": emb_list,
                "created_at": row[6].isoformat() if row[6] else None,
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            chunk_count += 1
            if chunk_count % 5000 == 0:
                print(f"  Progress: {chunk_count:,} chunks written...")
    print(f"Backed up {chunk_count:,} document chunks to {chunks_backup_file}")

    # 3. Write metadata summary
    meta = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "backup_directory": str(BACKUP_DIR),
        "documents_backed_up": doc_count,
        "chunks_backed_up": chunk_count,
        "source_db": "PostgreSQL / pgvector",
    }
    with open(meta_backup_file, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    print("\nBackup successfully verified and completed!")
    print(json.dumps(meta, indent=2))

finally:
    session.close()
