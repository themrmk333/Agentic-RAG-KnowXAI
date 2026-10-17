"""Read company knowledge files directly from the supplied ZIP archive."""

from __future__ import annotations

import csv
import io
import json
import zipfile
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any, Iterator


SUPPORTED_SUFFIXES = {".csv", ".json", ".md"}
EXCLUDED_PARTS = {"_generator_scripts", "evaluation"}


@dataclass(frozen=True)
class LoadedDocument:
    title: str
    source_path: str
    content_type: str
    text: str
    metadata: dict[str, Any]


def _json_text(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True)
    return str(value)


def _read_csv(raw: bytes) -> str:
    rows = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    return "\n".join(json.dumps(row, ensure_ascii=True, sort_keys=True) for row in rows)


def _read_entry(archive: zipfile.ZipFile, entry: zipfile.ZipInfo) -> str:
    raw = archive.read(entry)
    suffix = PurePosixPath(entry.filename).suffix.lower()
    if suffix == ".json":
        return _json_text(json.loads(raw.decode("utf-8-sig")))
    if suffix == ".csv":
        return _read_csv(raw)
    return raw.decode("utf-8-sig")


def iter_company_documents(
    zip_path: str,
    *,
    include_prefixes: tuple[str, ...] = (),
) -> Iterator[LoadedDocument]:
    """Yield searchable company files without extracting or modifying the ZIP."""

    with zipfile.ZipFile(zip_path) as archive:
        for entry in archive.infolist():
            path = PurePosixPath(entry.filename)
            parts = set(path.parts)
            if entry.is_dir() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
                continue
            if parts.intersection(EXCLUDED_PARTS):
                continue
            relative_path = "/".join(path.parts[1:]) if path.parts and path.parts[0] == "MK_InfinitAI_Dataset" else entry.filename
            if include_prefixes and not relative_path.startswith(include_prefixes):
                continue
            text = _read_entry(archive, entry).strip()
            if not text:
                continue
            yield LoadedDocument(
                title=path.name,
                source_path=relative_path,
                content_type={".json": "application/json", ".csv": "text/csv", ".md": "text/markdown"}[path.suffix.lower()],
                text=text,
                metadata={"archive_path": entry.filename, "format": path.suffix.lower().lstrip(".")},
            )
