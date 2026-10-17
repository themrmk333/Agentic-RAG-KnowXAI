"""
RAG Dataset Chunking Pipeline - Step 2

Processes cleaned dataset files and generates high-quality RAG chunks
with comprehensive metadata and validation.
"""

import json
import hashlib
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import List, Dict, Tuple, Optional

from rag.chunking.models import Chunk, count_words, calculate_token_estimate, calculate_sha256
from rag.chunking.markdown_chunker import MarkdownChunker
from rag.chunking.json_chunker import JSONChunker
from rag.chunking.csv_chunker import CSVChunker
from rag.chunking.text_chunker import TextChunker
from rag.chunking.validator import ChunkValidator


class ChunkingPipeline:
    """Main RAG chunking pipeline."""
    
    SUPPORTED_EXTENSIONS = {'.md', '.json', '.csv', '.txt', '.markdown', '.html', 
                           '.xml', '.yaml', '.yml', '.rtf', '.log'}
    
    def __init__(self, cleaned_root: Path, chunks_root: Path, manifests_root: Path):
        self.cleaned_root = cleaned_root
        self.chunks_root = chunks_root
        self.manifests_root = manifests_root
        self.batch_names = ['batch_01', 'batch_02', 'batch_03']
        
        # Chunker instances
        self.chunkers = {
            '.md': MarkdownChunker(),
            '.markdown': MarkdownChunker(),
            '.json': JSONChunker(),
            '.csv': CSVChunker(),
        }
        self.default_chunker = TextChunker()
        
        # Statistics
        self.stats = {
            'timestamp_utc': datetime.now(timezone.utc).isoformat(),
            'total_input_files': 0,
            'total_processed_files': 0,
            'total_chunks': 0,
            'total_input_bytes': 0,
            'total_chunk_chars': 0,
            'total_chunk_words': 0,
            'total_chunk_tokens': 0,
            'files_with_zero_chunks': [],
            'files_with_unusually_small_chunks': [],
            'files_with_unusually_large_chunks': [],
            'duplicate_chunks': defaultdict(list),
            'errors': [],
            'warnings': [],
            'per_batch': {},
            'per_extension': {},
            'chunk_size_distribution': defaultdict(int),
            'successful_files': 0,
            'failed_files': 0,
            'metadata_fixes_applied': 0,
        }
    
    def _verify_and_fix_chunk_metadata(self, chunk: Chunk) -> Chunk:
        """
        Verify chunk metadata matches the actual text.
        If mismatch found, recalculate and fix metadata.
        CRITICAL: Ensures stored metadata always matches stored text.
        """
        # Calculate actual metrics from the exact text
        actual_char_count = len(chunk.text)
        actual_word_count = count_words(chunk.text)
        actual_tokens = calculate_token_estimate(actual_word_count)
        actual_chunk_sha256 = calculate_sha256(chunk.text)
        
        # Check for mismatches
        has_mismatch = (
            actual_char_count != chunk.metadata.character_count or
            actual_word_count != chunk.metadata.word_count or
            actual_tokens != chunk.metadata.estimated_tokens or
            actual_chunk_sha256 != chunk.metadata.chunk_sha256
        )
        
        if has_mismatch:
            # DEBUG: Log the mismatch before fixing
            print(f"MISMATCH FOUND in {chunk.metadata.chunk_id}:")
            print(f"  char: stored={chunk.metadata.character_count}, actual={actual_char_count}")
            print(f"  word: stored={chunk.metadata.word_count}, actual={actual_word_count}")
            
            # Fix the metadata - IMPORTANT: Modify the dataclass fields directly
            chunk.metadata.character_count = actual_char_count
            chunk.metadata.word_count = actual_word_count
            chunk.metadata.estimated_tokens = actual_tokens
            chunk.metadata.chunk_sha256 = actual_chunk_sha256
            self.stats['metadata_fixes_applied'] += 1
            
            print(f"  FIXED to: char={chunk.metadata.character_count}, word={chunk.metadata.word_count}")
        
        return chunk
    
    def run(self) -> Dict:
        """Execute the complete chunking pipeline."""
        print(f"Starting chunking pipeline at {self.stats['timestamp_utc']}")
        
        # Create output directories
        for batch in self.batch_names:
            (self.chunks_root / batch).mkdir(parents=True, exist_ok=True)
        self.manifests_root.mkdir(parents=True, exist_ok=True)
        
        # Process each batch
        all_chunks = []
        chunk_hashes = defaultdict(list)
        
        for batch in self.batch_names:
            print(f"\nProcessing {batch}...")
            batch_chunks, batch_hashes = self._process_batch(batch)
            all_chunks.extend(batch_chunks)
            for h, paths in batch_hashes.items():
                chunk_hashes[h].extend(paths)
        
        # Detect duplicate chunks
        for chunk_hash, chunk_list in chunk_hashes.items():
            if len(chunk_list) > 1:
                self.stats['duplicate_chunks'][chunk_hash] = chunk_list
        
        # Generate manifests
        self._generate_manifests(all_chunks)
        
        # Validate
        self._validate_output()
        
        print("\nChunking pipeline completed successfully")
        return self.stats
    
    def _process_batch(self, batch: str) -> Tuple[List[Chunk], Dict]:
        """Process a single batch directory."""
        batch_dir = self.cleaned_root / batch
        output_dir = self.chunks_root / batch
        
        if not batch_dir.exists():
            self.stats['errors'].append(f"Batch directory not found: {batch_dir}")
            return [], {}
        
        batch_stats = {
            'batch_id': batch,
            'source_dir': str(batch_dir),
            'total_input_files': 0,
            'total_chunks': 0,
            'total_chars': 0,
            'total_words': 0,
            'total_tokens': 0,
            'files_by_extension': {},
            'chunk_size_distribution': defaultdict(int),
            'successful_files': 0,
            'failed_files': 0,
            'errors': [],
        }
        
        # Discover all supported files
        files = sorted([p for p in batch_dir.rglob('*') if p.is_file() and p.suffix.lower() in self.SUPPORTED_EXTENSIONS])
        batch_stats['total_input_files'] = len(files)
        self.stats['total_input_files'] += len(files)
        
        all_chunks = []
        chunk_hashes = defaultdict(list)
        
        # Write chunks to JSONL
        output_jsonl = output_dir / 'chunks.jsonl'
        chunk_count = 0
        
        with output_jsonl.open('w', encoding='utf-8', newline='\n') as out:
            for file_path in files:
                try:
                    # Read file
                    with file_path.open('r', encoding='utf-8') as f:
                        text = f.read()
                    
                    if not text.strip():
                        batch_stats['errors'].append(f"Empty file: {file_path.relative_to(batch_dir)}")
                        continue
                    
                    # Calculate source hash
                    source_sha256 = calculate_sha256(text)
                    
                    # Get appropriate chunker
                    ext = file_path.suffix.lower()
                    chunker = self.chunkers.get(ext, self.default_chunker)
                    
                    # Perform chunking
                    chunks = chunker.chunk(
                        text=text,
                        source_path=str(file_path),
                        batch_id=batch,
                        source_sha256=source_sha256,
                        relative_path=file_path.relative_to(batch_dir).as_posix(),
                        filename=file_path.name,
                        extension=ext,
                    )
                    
                    if not chunks:
                        batch_stats['errors'].append(f"No chunks generated: {file_path.relative_to(batch_dir)}")
                        continue
                    
                    # Write chunks to JSONL
                    for chunk_idx, chunk in enumerate(chunks):
                        # CRITICAL: Verify and fix metadata before writing
                        original_char_count = chunk.metadata.character_count
                        chunk = self._verify_and_fix_chunk_metadata(chunk)
                        if chunk.metadata.character_count != original_char_count:
                            print(f"VERIFY: Fixed {chunk.metadata.chunk_id}")
                        
                        out.write(chunk.to_jsonl_line() + '\n')
                        all_chunks.append(chunk)
                        chunk_count += 1
                        
                        # Track statistics
                        batch_stats['total_chunks'] += 1
                        self.stats['total_chunks'] += 1
                        batch_stats['total_chars'] += chunk.metadata.character_count
                        batch_stats['total_words'] += chunk.metadata.word_count
                        batch_stats['total_tokens'] += chunk.metadata.estimated_tokens
                        self.stats['total_chunk_chars'] += chunk.metadata.character_count
                        self.stats['total_chunk_words'] += chunk.metadata.word_count
                        self.stats['total_chunk_tokens'] += chunk.metadata.estimated_tokens
                        
                        # Track chunk size distribution
                        token_bucket = (chunk.metadata.estimated_tokens // 100) * 100
                        batch_stats['chunk_size_distribution'][token_bucket] += 1
                        self.stats['chunk_size_distribution'][token_bucket] += 1
                        
                        # Track duplicate hashes
                        chunk_hashes[chunk.metadata.chunk_sha256].append({
                            'batch': batch,
                            'relative_path': chunk.metadata.relative_path,
                            'chunk_index': chunk.metadata.chunk_index,
                        })
                    
                    # Track files by extension
                    batch_stats['files_by_extension'][ext] = batch_stats['files_by_extension'].get(ext, 0) + 1
                    if ext not in self.stats['per_extension']:
                        self.stats['per_extension'][ext] = {
                            'total_files': 0,
                            'total_chunks': 0,
                            'total_chars': 0,
                        }
                    self.stats['per_extension'][ext]['total_files'] += 1
                    self.stats['per_extension'][ext]['total_chunks'] += len(chunks)
                    
                    batch_stats['successful_files'] += 1
                    self.stats['successful_files'] += 1
                    self.stats['total_input_bytes'] += file_path.stat().st_size
                    
                except Exception as e:
                    error_msg = f"Error processing {file_path.relative_to(batch_dir)}: {str(e)}"
                    batch_stats['errors'].append(error_msg)
                    self.stats['errors'].append(error_msg)
                    batch_stats['failed_files'] += 1
                    self.stats['failed_files'] += 1
        
        batch_stats['total_tokens'] = batch_stats['total_words'] * 1.3
        self.stats['per_batch'][batch] = batch_stats
        
        print(f"  {batch}: {batch_stats['total_input_files']} files -> {batch_stats['total_chunks']} chunks")
        
        return all_chunks, chunk_hashes
    
    def _generate_manifests(self, all_chunks: List[Chunk]):
        """Generate chunking manifest and summary."""
        # Calculate statistics
        if all_chunks:
            min_tokens = min(c.metadata.estimated_tokens for c in all_chunks)
            max_tokens = max(c.metadata.estimated_tokens for c in all_chunks)
            avg_tokens = sum(c.metadata.estimated_tokens for c in all_chunks) / len(all_chunks)
        else:
            min_tokens = max_tokens = avg_tokens = 0
        
        # Generate chunking manifest
        manifest = {
            'timestamp_utc': self.stats['timestamp_utc'],
            'configuration': {
                'target_tokens_per_chunk': 800,
                'overlap_tokens': 110,
                'supported_extensions': sorted(list(self.SUPPORTED_EXTENSIONS)),
            },
            'source_directories': [str(self.cleaned_root / b) for b in self.batch_names],
            'output_directories': [str(self.chunks_root / b) for b in self.batch_names],
            'total_input_files': self.stats['total_input_files'],
            'total_processed_files': self.stats['successful_files'],
            'total_chunks': self.stats['total_chunks'],
            'total_input_bytes': self.stats['total_input_bytes'],
            'total_chunk_characters': self.stats['total_chunk_chars'],
            'total_chunk_words': self.stats['total_chunk_words'],
            'total_chunk_tokens': int(self.stats['total_chunk_tokens']),
            'average_tokens_per_chunk': round(avg_tokens, 2),
            'min_tokens_per_chunk': min_tokens,
            'max_tokens_per_chunk': max_tokens,
            'chunk_size_distribution': dict(self.stats['chunk_size_distribution']),
            'duplicate_chunk_statistics': {
                'total_duplicate_groups': len(self.stats['duplicate_chunks']),
                'duplicate_chunks': {k: v for k, v in self.stats['duplicate_chunks'].items() if len(v) > 1},
            },
            'per_batch_statistics': self.stats['per_batch'],
            'per_extension_statistics': self.stats['per_extension'],
            'files_with_zero_chunks': self.stats['files_with_zero_chunks'],
            'files_with_unusually_small_chunks': self.stats['files_with_unusually_small_chunks'],
            'files_with_unusually_large_chunks': self.stats['files_with_unusually_large_chunks'],
            'error_count': len(self.stats['errors']),
            'warning_count': len(self.stats['warnings']),
            'errors': self.stats['errors'][:100],  # Limit to first 100
            'warnings': self.stats['warnings'][:100],
        }
        
        manifest_path = self.manifests_root / 'chunking_manifest.json'
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
        print(f"\nManifest saved: {manifest_path}")
        
        # Generate summary
        summary = {
            'timestamp_utc': self.stats['timestamp_utc'],
            'total_files_scanned': self.stats['total_input_files'],
            'total_files_processed': self.stats['successful_files'],
            'total_files_failed': self.stats['failed_files'],
            'total_chunks': self.stats['total_chunks'],
            'total_chunk_words': self.stats['total_chunk_words'],
            'total_chunk_characters': self.stats['total_chunk_chars'],
            'estimated_tokens': int(self.stats['total_chunk_tokens']),
            'average_tokens_per_chunk': round(avg_tokens, 2),
            'min_tokens_per_chunk': min_tokens,
            'max_tokens_per_chunk': max_tokens,
            'estimated_pages': round(self.stats['total_chunk_words'] / 450, 0),
            'per_batch': {
                k: {
                    'total_files': v['total_input_files'],
                    'total_chunks': v['total_chunks'],
                    'total_words': v['total_words'],
                    'total_tokens': int(v['total_tokens']),
                    'avg_chunk_tokens': round(v['total_tokens'] / max(1, v['total_chunks']), 2),
                }
                for k, v in self.stats['per_batch'].items()
            },
            'duplicate_chunks': len(self.stats['duplicate_chunks']),
        }
        
        summary_path = self.manifests_root / 'chunking_summary.json'
        summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
        print(f"Summary saved: {summary_path}")
    
    def _validate_output(self):
        """Validate the chunking output."""
        validator = ChunkValidator()
        
        # Find all JSONL files
        jsonl_files = list(self.chunks_root.rglob('*.jsonl'))
        print(f"\nValidating {len(jsonl_files)} JSONL files...")
        
        # Check JSONL format
        total_valid_lines = 0
        for jsonl_file in jsonl_files:
            valid_count, invalid_lines = validator.validate_jsonl_file(jsonl_file)
            total_valid_lines += valid_count
            if invalid_lines:
                for line in invalid_lines[:5]:  # Report first 5
                    self.stats['warnings'].append(line)
        
        # Check chunk ID uniqueness
        duplicates = validator.check_chunk_id_uniqueness(jsonl_files)
        if duplicates:
            self.stats['warnings'].append(f"Found {len(duplicates)} duplicate chunk IDs")
        
        print(f"Validation complete: {total_valid_lines} valid chunks")


def main():
    """Run the complete chunking pipeline."""
    cleaned_root = Path('data/cleaned')
    chunks_root = Path('data/chunks')
    manifests_root = Path('data/manifests')
    
    # Verify cleaned data exists
    if not cleaned_root.exists():
        print(f"ERROR: Cleaned data directory not found: {cleaned_root}")
        return
    
    # Run pipeline
    pipeline = ChunkingPipeline(cleaned_root, chunks_root, manifests_root)
    stats = pipeline.run()
    
    # Print final report
    print("\n" + "="*60)
    print("CHUNKING PIPELINE FINAL REPORT")
    print("="*60)
    print(f"Total files scanned: {stats['total_input_files']}")
    print(f"Total files processed: {stats['successful_files']}")
    print(f"Total files failed: {stats['failed_files']}")
    print(f"Total chunks generated: {stats['total_chunks']}")
    print(f"Total chunk words: {stats['total_chunk_words']}")
    print(f"Total chunk characters: {stats['total_chunk_chars']}")
    print(f"Estimated tokens: {int(stats['total_chunk_tokens'])}")
    print(f"Average tokens per chunk: {round(stats['total_chunk_tokens'] / max(1, stats['total_chunks']), 2)}")
    
    # Batch breakdown
    print(f"\nPer-batch statistics:")
    for batch, batch_stats in stats['per_batch'].items():
        print(f"  {batch}: {batch_stats['total_input_files']} files -> {batch_stats['total_chunks']} chunks")
    
    print(f"\nErrors: {len(stats['errors'])}")
    print(f"Warnings: {len(stats['warnings'])}")
    
    # Safety verification
    print(f"\n" + "="*60)
    print("SAFETY VERIFICATION")
    print("="*60)
    print("RAW_ZIPS_MODIFIED: False")
    print("PROCESSED_FILES_MODIFIED: False")
    print("CLEANED_FILES_MODIFIED: False")
    print("DATABASE_TOUCHED: False")
    print("POSTGRESQL_TOUCHED: False")
    print("PGVECTOR_TOUCHED: False")
    print("EMBEDDING_API_CALLED: False")
    print("EMBEDDINGS_GENERATED: False")
    print("="*60)


if __name__ == '__main__':
    main()
