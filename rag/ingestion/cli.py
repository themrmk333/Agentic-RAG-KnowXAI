"""Command-line entry point for company ZIP ingestion."""

from __future__ import annotations

import argparse

from config.settings import get_settings
from database.vector_store import vector_store
from rag.embeddings.factory import build_embedding_service
from rag.ingestion.pipeline import ingest_zip


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest company knowledge into PostgreSQL + pgvector")
    parser.add_argument("zip_path")
    parser.add_argument("--prefix", action="append", default=[], help="Optional archive-relative path prefix")
    parser.add_argument("--chunk-size", type=int, default=1200)
    parser.add_argument("--overlap", type=int, default=200)
    args = parser.parse_args()
    settings = get_settings()
    count = ingest_zip(
        args.zip_path,
        embedding_service=build_embedding_service(settings),
        vector_store=vector_store,
        include_prefixes=tuple(args.prefix),
        chunk_size=args.chunk_size,
        overlap=args.overlap,
    )
    print(f"CHUNKS_INGESTED: {count}")


if __name__ == "__main__":
    main()