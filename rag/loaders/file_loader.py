"""Document parser and text extractor for multiple file formats."""

from __future__ import annotations

import csv
import io
import json
import zipfile
from typing import Any, List, Optional

import docx
import pypdf

from rag.loaders.company_zip import LoadedDocument


def load_file(
    file_content: bytes,
    filename: str,
    content_type: str,
    extra_metadata: Optional[dict[str, Any]] = None,
) -> List[LoadedDocument]:
    """Parse raw bytes of a file based on its extension/mime-type and return LoadedDocuments."""
    extra_metadata = extra_metadata or {}
    suffix = filename.split(".")[-1].lower() if "." in filename else ""
    loaded_docs: List[LoadedDocument] = []

    if suffix == "zip":
        # Process ZIP file contents
        try:
            with zipfile.ZipFile(io.BytesIO(file_content)) as archive:
                for entry in archive.infolist():
                    if entry.is_dir():
                        continue
                    entry_suffix = entry.filename.split(".")[-1].lower() if "." in entry.filename else ""
                    if entry_suffix not in {"txt", "md", "json", "csv"}:
                        continue
                    
                    # Read zip entry
                    raw = archive.read(entry)
                    text = raw.decode("utf-8-sig", errors="replace").strip()
                    if not text:
                        continue
                    
                    entry_mime = {
                        "json": "application/json",
                        "csv": "text/csv",
                        "md": "text/markdown",
                        "txt": "text/plain"
                    }.get(entry_suffix, "text/plain")

                    meta = {
                        "archive_name": filename,
                        "archive_path": entry.filename,
                        "format": entry_suffix,
                        **extra_metadata
                    }
                    loaded_docs.append(
                        LoadedDocument(
                            title=entry.filename.split("/")[-1],
                            source_path=entry.filename,
                            content_type=entry_mime,
                            text=text,
                            metadata=meta,
                        )
                    )
        except Exception as e:
            raise ValueError(f"Failed to process ZIP archive: {str(e)}")

    elif suffix == "pdf":
        try:
            reader = pypdf.PdfReader(io.BytesIO(file_content))
            text_parts = []
            for page in reader.pages:
                text_parts.append(page.extract_text() or "")
            text = "\n".join(text_parts).strip()
            if not text:
                raise ValueError("PDF file did not contain extractable text.")
            
            meta = {"format": "pdf", **extra_metadata}
            loaded_docs.append(
                LoadedDocument(
                    title=filename,
                    source_path=filename,
                    content_type="application/pdf",
                    text=text,
                    metadata=meta,
                )
            )
        except Exception as e:
            raise ValueError(f"Failed to parse PDF document: {str(e)}")

    elif suffix == "docx":
        try:
            doc = docx.Document(io.BytesIO(file_content))
            text = "\n".join([p.text for p in doc.paragraphs]).strip()
            if not text:
                raise ValueError("DOCX file did not contain extractable text.")
            
            meta = {"format": "docx", **extra_metadata}
            loaded_docs.append(
                LoadedDocument(
                    title=filename,
                    source_path=filename,
                    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    text=text,
                    metadata=meta,
                )
            )
        except Exception as e:
            raise ValueError(f"Failed to parse Word document: {str(e)}")

    else:
        # Fallback to plain text
        try:
            text = file_content.decode("utf-8-sig", errors="replace").strip()
            mime = "text/plain"
            if suffix == "md":
                mime = "text/markdown"
            elif suffix == "json":
                mime = "application/json"
            elif suffix == "csv":
                mime = "text/csv"

            meta = {"format": suffix or "txt", **extra_metadata}
            loaded_docs.append(
                LoadedDocument(
                    title=filename,
                    source_path=filename,
                    content_type=mime,
                    text=text,
                    metadata=meta,
                )
            )
        except Exception as e:
            raise ValueError(f"Failed to decode text document: {str(e)}")

    return loaded_docs
