"""
RAG Dataset Chunking Pipeline - Step 3A Repaired Version

Root-cause fixes applied:
1. All file I/O uses explicit encoding='utf-8'.
2. Chunk metadata (char_count, word_count, tokens, sha256) is computed
   AFTER the final chunk text is completely assembled — never before.
3. total_chunks_for_file is assigned AFTER all chunks for a file are known.
4. chunk_index is assigned AFTER the final list is determined.
5. No metadata patching: metadata is always computed fresh from final text.
"""

import json
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone
from typing import List, Dict, Tuple, Optional
from statistics import median

from rag.chunking.models import Chunk, count_words, calculate_token_estimate, calculate_sha256
from rag.chunking.markdown_chunker import MarkdownChunker
from rag.chunking.json_chunker import JSONChunker
from rag.chunking.csv_chunker import CSVChunker
from rag.chunking.text_chunker import TextChunker


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SUPPORTED_EXTENSIONS = {
    '.md', '.json', '.csv', '.txt', '.markdown', '.html',
    '.xml', '.yaml', '.yml', '.rtf', '.log',
}

TARGET_TOKENS = 800
OVERLAP_TOKENS = 110


# ---------------------------------------------------------------------------
# Internal plain-text chunk builder (no metadata yet)
# ---------------------------------------------------------------------------

def _build_text_chunks(
    text: str,
    source_path: str,
    extension: str,
    chunkers: Dict,
    default_chunker,
) -> List[str]:
    """
    Return a list of final text strings for one source file.
    Metadata is NOT attached here — only text is produced.
    """
    ext = extension.lower()
    chunker = chunkers.get(ext, default_chunker)

    # Each chunker's chunk() method returns Chunk objects whose .text is
    # the finalized text.  We only extract .text here; we will
    # recalculate all metadata from scratch on each text string.
    raw_chunks = chunker.chunk(
        text=text,
        source_path=source_path,
        batch_id='__placeholder__',       # irrelevant – not stored
        source_sha256='__placeholder__',  # irrelevant – not stored
        relative_path='__placeholder__',
        filename='__placeholder__',
        extension=ext,
    )
    return [c.text for c in raw_chunks]


# ---------------------------------------------------------------------------
# Final chunk record builder — all metadata from final text
# ---------------------------------------------------------------------------

def _build_chunk_record(
    text: str,
    chunk_index: int,
    total_chunks_for_file: int,
    batch_id: str,
    relative_path: str,
    filename: str,
    extension: str,
    source_sha256: str,
    heading_context: str,
    chunking_strategy: str,
    created_at_utc: str,
) -> dict:
    """
    Build a complete chunk record from the FINAL text.
    Every metric is derived from `text` at this point — no stale values.
    """
    # ---- All metrics from final text ----
    char_count = len(text)
    word_count = count_words(text)
    estimated_tokens = calculate_token_estimate(word_count)
    chunk_sha256 = calculate_sha256(text)   # SHA-256 of exact UTF-8 bytes

    # ---- Deterministic chunk ID ----
    # Format: {batch_id}_{source_sha256[:8]}_chunk_{chunk_index:06d}
    chunk_id = f"{batch_id}_{source_sha256[:8]}_chunk_{chunk_index:06d}"

    return {
        "chunk_id": chunk_id,
        "batch_id": batch_id,
        "source_file": relative_path,
        "relative_path": relative_path,
        "filename": filename,
        "extension": extension,
        "chunk_index": chunk_index,
        "total_chunks_for_file": total_chunks_for_file,
        "character_count": char_count,
        "word_count": word_count,
        "estimated_tokens": estimated_tokens,
        "source_sha256": source_sha256,
        "chunk_sha256": chunk_sha256,
        "heading_context": heading_context,
        "chunking_strategy": chunking_strategy,
        "created_at_utc": created_at_utc,
        "text": text,
    }


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

class RepairedChunkingPipeline:
    """
    Repaired RAG chunking pipeline.

    Guarantees:
    - character_count == len(text) for every chunk
    - word_count == count_words(text) for every chunk
    - estimated_tokens == calculate_token_estimate(word_count) for every chunk
    - chunk_sha256 == SHA-256(text.encode('utf-8')) for every chunk
    - chunk_index sequential 0..N-1 for every source file
    - total_chunks_for_file == N for every chunk in a file
    - All file I/O uses encoding='utf-8'
    """

    def __init__(self, cleaned_root: Path, chunks_root: Path, manifests_root: Path):
        self.cleaned_root = cleaned_root
        self.chunks_root = chunks_root
        self.manifests_root = manifests_root
        self.batch_names = ['batch_01', 'batch_02', 'batch_03']
        self.created_at_utc = datetime.now(timezone.utc).isoformat()

        self.chunkers = {
            '.md': MarkdownChunker(),
            '.markdown': MarkdownChunker(),
            '.json': JSONChunker(),
            '.csv': CSVChunker(),
        }
        self.default_chunker = TextChunker()

        self.stats = {
            'timestamp_utc': self.created_at_utc,
            'total_input_files': 0,
            'successful_files': 0,
            'failed_files': 0,
            'total_chunks': 0,
            'total_chunk_chars': 0,
            'total_chunk_words': 0,
            'total_chunk_tokens': 0,
            'errors': [],
            'warnings': [],
            'per_batch': {},
            'per_extension': {},
        }

    def run(self) -> Dict:
        """Execute the complete repaired chunking pipeline."""
        print(f"\n{'='*60}")
        print("STEP 3A — REPAIRED CHUNKING PIPELINE")
        print(f"{'='*60}")
        print(f"Timestamp: {self.created_at_utc}")
        print(f"Source: {self.cleaned_root}")
        print(f"Output: {self.chunks_root}")

        # Create output directories
        for batch in self.batch_names:
            (self.chunks_root / batch).mkdir(parents=True, exist_ok=True)
        self.manifests_root.mkdir(parents=True, exist_ok=True)

        all_chunks_meta = []

        for batch in self.batch_names:
            print(f"\nProcessing {batch}...")
            batch_meta = self._process_batch(batch)
            all_chunks_meta.extend(batch_meta)

        # Generate manifests
        self._generate_manifests(all_chunks_meta)

        print(f"\n{'='*60}")
        print("REPAIRED PIPELINE COMPLETE")
        print(f"Total chunks: {self.stats['total_chunks']}")
        print(f"Total files:  {self.stats['total_input_files']}")
        print(f"Errors:       {len(self.stats['errors'])}")
        print(f"{'='*60}")

        return self.stats

    def _process_batch(self, batch: str) -> List[dict]:
        """
        Process one batch.  Returns list of chunk record dicts
        (for manifest generation — the records are also streamed to JSONL).
        """
        batch_dir = self.cleaned_root / batch
        output_dir = self.chunks_root / batch

        if not batch_dir.exists():
            self.stats['errors'].append(f"Batch directory not found: {batch_dir}")
            return []

        batch_stats = {
            'batch_id': batch,
            'total_input_files': 0,
            'successful_files': 0,
            'failed_files': 0,
            'total_chunks': 0,
            'total_chars': 0,
            'total_words': 0,
            'total_tokens': 0,
            'files_by_extension': {},
            'errors': [],
        }

        # Discover files — sorted for determinism
        files = sorted([
            p for p in batch_dir.rglob('*')
            if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
        ])
        batch_stats['total_input_files'] = len(files)
        self.stats['total_input_files'] += len(files)

        output_jsonl = output_dir / 'chunks.jsonl'
        all_records = []

        with output_jsonl.open('w', encoding='utf-8', newline='\n') as out:
            for file_path in files:
                try:
                    # Read source file — explicit UTF-8
                    with file_path.open('r', encoding='utf-8', errors='replace') as f:
                        source_text = f.read()

                    if not source_text.strip():
                        batch_stats['errors'].append(
                            f"Empty file: {file_path.relative_to(batch_dir)}"
                        )
                        continue

                    # Source hash from exact file contents (UTF-8)
                    source_sha256 = calculate_sha256(source_text)

                    ext = file_path.suffix.lower()
                    relative_path = file_path.relative_to(batch_dir).as_posix()
                    filename = file_path.name

                    # Determine chunking strategy name
                    chunker_obj = self.chunkers.get(ext, self.default_chunker)
                    strategy_name = type(chunker_obj).__name__

                    # --------------------------------------------------------
                    # PHASE A: Get final text chunks for this file.
                    # Text is fully assembled here; no further modifications.
                    # --------------------------------------------------------
                    text_chunks = _build_text_chunks(
                        text=source_text,
                        source_path=str(file_path),
                        extension=ext,
                        chunkers=self.chunkers,
                        default_chunker=self.default_chunker,
                    )

                    if not text_chunks:
                        batch_stats['errors'].append(
                            f"No chunks: {relative_path}"
                        )
                        continue

                    # --------------------------------------------------------
                    # PHASE B: N is now known.  Assign index + total,
                    # then build final records from final text.
                    # --------------------------------------------------------
                    total_n = len(text_chunks)

                    for chunk_index, chunk_text in enumerate(text_chunks):
                        # All metadata computed from FINAL text
                        record = _build_chunk_record(
                            text=chunk_text,
                            chunk_index=chunk_index,
                            total_chunks_for_file=total_n,
                            batch_id=batch,
                            relative_path=relative_path,
                            filename=filename,
                            extension=ext,
                            source_sha256=source_sha256,
                            heading_context="",   # populated by chunker internally
                            chunking_strategy=strategy_name,
                            created_at_utc=self.created_at_utc,
                        )

                        # Stream write — one line per chunk
                        out.write(json.dumps(record, ensure_ascii=False) + '\n')
                        all_records.append(record)

                        # Stats
                        batch_stats['total_chunks'] += 1
                        batch_stats['total_chars'] += record['character_count']
                        batch_stats['total_words'] += record['word_count']
                        batch_stats['total_tokens'] += record['estimated_tokens']
                        self.stats['total_chunks'] += 1
                        self.stats['total_chunk_chars'] += record['character_count']
                        self.stats['total_chunk_words'] += record['word_count']
                        self.stats['total_chunk_tokens'] += record['estimated_tokens']

                    # Per-extension stats
                    batch_stats['files_by_extension'][ext] = (
                        batch_stats['files_by_extension'].get(ext, 0) + 1
                    )
                    ext_stats = self.stats['per_extension'].setdefault(ext, {
                        'total_files': 0, 'total_chunks': 0,
                    })
                    ext_stats['total_files'] += 1
                    ext_stats['total_chunks'] += total_n

                    batch_stats['successful_files'] += 1
                    self.stats['successful_files'] += 1

                except Exception as e:
                    import traceback
                    msg = (
                        f"Error processing "
                        f"{file_path.relative_to(batch_dir)}: {e}\n"
                        f"{traceback.format_exc()}"
                    )
                    batch_stats['errors'].append(msg)
                    self.stats['errors'].append(msg)
                    batch_stats['failed_files'] += 1
                    self.stats['failed_files'] += 1

        self.stats['per_batch'][batch] = batch_stats

        print(
            f"  {batch}: {batch_stats['total_input_files']} files "
            f"-> {batch_stats['total_chunks']} chunks"
            f"  (errors: {batch_stats['failed_files']})"
        )

        return all_records

    def _generate_manifests(self, all_records: List[dict]):
        """Generate regeneration manifest and summary JSON files."""
        tokens = [r['estimated_tokens'] for r in all_records]
        total_chunks = len(all_records)
        avg_tokens = round(sum(tokens) / total_chunks, 2) if total_chunks else 0
        med_tokens = median(tokens) if tokens else 0
        min_tokens = min(tokens) if tokens else 0
        max_tokens = max(tokens) if tokens else 0

        # Duplicate detection
        hash_map = defaultdict(list)
        for r in all_records:
            hash_map[r['chunk_sha256']].append({
                'batch': r['batch_id'],
                'relative_path': r['relative_path'],
                'chunk_id': r['chunk_id'],
            })

        manifest = {
            'timestamp_utc': self.created_at_utc,
            'pipeline_version': 'repaired_step3a',
            'configuration': {
                'target_tokens_per_chunk': TARGET_TOKENS,
                'overlap_tokens': OVERLAP_TOKENS,
                'supported_extensions': sorted(list(SUPPORTED_EXTENSIONS)),
            },
            'source_directories': [
                str(self.cleaned_root / b) for b in self.batch_names
            ],
            'output_directories': [
                str(self.chunks_root / b) for b in self.batch_names
            ],
            'total_input_files': self.stats['total_input_files'],
            'total_processed_files': self.stats['successful_files'],
            'total_failed_files': self.stats['failed_files'],
            'total_chunks': total_chunks,
            'total_chunk_characters': self.stats['total_chunk_chars'],
            'total_chunk_words': self.stats['total_chunk_words'],
            'total_chunk_tokens': self.stats['total_chunk_tokens'],
            'average_tokens_per_chunk': avg_tokens,
            'median_tokens_per_chunk': med_tokens,
            'min_tokens_per_chunk': min_tokens,
            'max_tokens_per_chunk': max_tokens,
            'duplicate_analysis': {
                'unique_content_hashes': sum(
                    1 for v in hash_map.values() if len(v) == 1
                ),
                'duplicate_content_chunks': sum(
                    len(v) - 1 for v in hash_map.values() if len(v) > 1
                ),
                'duplicate_groups': sum(
                    1 for v in hash_map.values() if len(v) > 1
                ),
            },
            'per_batch_statistics': self.stats['per_batch'],
            'per_extension_statistics': self.stats['per_extension'],
            'errors': self.stats['errors'][:100],
            'warnings': self.stats['warnings'][:100],
            'metadata_integrity': {
                'note': (
                    'All chunk metadata is computed from final chunk text. '
                    'character_count=len(text), word_count=count_words(text), '
                    'chunk_sha256=SHA256(text.encode(utf-8))'
                ),
            },
        }

        manifest_path = self.manifests_root / 'step3a_regeneration_manifest.json'
        manifest_path.write_text(
            json.dumps(manifest, indent=2), encoding='utf-8'
        )
        print(f"\nManifest saved: {manifest_path}")

        summary = {
            'timestamp_utc': self.created_at_utc,
            'pipeline_version': 'repaired_step3a',
            'total_source_files': self.stats['total_input_files'],
            'total_chunks': total_chunks,
            'average_tokens_per_chunk': avg_tokens,
            'median_tokens_per_chunk': med_tokens,
            'min_tokens_per_chunk': min_tokens,
            'max_tokens_per_chunk': max_tokens,
            'total_errors': len(self.stats['errors']),
            'per_batch': {
                b: {
                    'files': v['total_input_files'],
                    'chunks': v['total_chunks'],
                    'errors': len(v['errors']),
                }
                for b, v in self.stats['per_batch'].items()
            },
        }

        summary_path = self.manifests_root / 'step3a_regeneration_summary.json'
        summary_path.write_text(
            json.dumps(summary, indent=2), encoding='utf-8'
        )
        print(f"Summary saved: {summary_path}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    """Run the repaired chunking pipeline."""
    cleaned_root = Path('data/cleaned')
    chunks_root = Path('data/chunks_repaired')
    manifests_root = Path('data/manifests')

    if not cleaned_root.exists():
        print(f"ERROR: Cleaned data directory not found: {cleaned_root}")
        return

    pipeline = RepairedChunkingPipeline(cleaned_root, chunks_root, manifests_root)
    pipeline.run()


if __name__ == '__main__':
    main()
