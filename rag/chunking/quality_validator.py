"""
Comprehensive RAG chunk quality validation and analysis.
This is a read-only validation module that does NOT modify any chunk files.

FIXES applied in this version:
1. All open() calls use encoding='utf-8' explicitly.
2. Index validation keys on (batch_id, relative_path) — not just relative_path.
   This prevents false positives when the same file exists in multiple batches.
3. Content-consistency recalculation uses the same count_words / calculate_token_estimate
   functions as the pipeline — no divergence.
"""

import json
import re
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Dict, List, Tuple, Any
from statistics import median, quantiles

from rag.chunking.models import count_words, calculate_token_estimate, calculate_sha256


class ChunkQualityValidator:
    """Comprehensive chunk quality validation without modifications."""

    # Chunk size thresholds
    VERY_SMALL_TOKENS = 50
    SMALL_TOKENS = 150
    NORMAL_TOKENS_MIN = 151
    NORMAL_TOKENS_MAX = 1200
    LARGE_TOKENS = 1200
    VERY_LARGE_TOKENS = 2000

    def __init__(self, chunks_root: Path, cleaned_root: Path, manifests_root: Path):
        self.chunks_root = chunks_root
        self.cleaned_root = cleaned_root
        self.manifests_root = manifests_root
        self.batch_names = ['batch_01', 'batch_02', 'batch_03']

        self.report = {
            'timestamp_utc': datetime.now(timezone.utc).isoformat(),
            'source_directories': [str(cleaned_root / b) for b in self.batch_names],
            'input_chunk_files': [],
            'total_chunks_discovered': 0,
            'total_chunks_expected': 0,
            'validation_results': {
                'json_validation': {},
                'metadata_validation': {},
                'source_traceability': {},
                'hash_validation': {},
                'chunk_id_validation': {},
                'index_validation': {},
                'text_validation': {},
                'content_consistency': {},
            },
            'error_count': 0,
            'warning_count': 0,
            'errors': [],
            'warnings': [],
            'duplicate_analysis': {
                'unique_chunks': 0,
                'duplicate_chunks': 0,
                'duplicate_groups': 0,
                'cross_batch_duplicates': 0,
                'cross_batch_group_count': 0,
            },
            'token_distribution': {},
            'per_batch': {},
            'source_coverage': {},
            'chunking_strategy_distribution': {},
            'quality_score': 0,
            'final_status': 'UNKNOWN',
        }

    def validate(self) -> Dict:
        """Execute complete validation."""
        print("Starting Step 3: Final RAG Chunk Quality Validation")

        # Phase 1: Discovery
        self._phase_discover_chunks()

        # Phase 2: Validation
        self._phase_json_validation()
        self._phase_metadata_validation()
        self._phase_source_traceability()
        self._phase_hash_validation()
        self._phase_chunk_id_validation()
        self._phase_index_validation()
        self._phase_text_validation()
        self._phase_content_consistency()

        # Phase 3: Analysis
        self._phase_token_distribution()
        self._phase_duplicate_analysis()
        self._phase_source_coverage()
        self._phase_chunking_strategy()

        # Phase 4: Quality Score
        self._calculate_quality_score()

        return self.report

    # ------------------------------------------------------------------
    # Phase 1: Chunk Discovery
    # ------------------------------------------------------------------

    def _phase_discover_chunks(self):
        """Discover and count all chunk files."""
        print("\n1. CHUNK DISCOVERY")

        jsonl_files = []
        total_lines = 0

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if batch_dir.exists():
                batch_files = sorted(batch_dir.glob('*.jsonl'))
                for jsonl_file in batch_files:
                    jsonl_files.append(jsonl_file)
                    # Count non-blank lines using utf-8
                    with open(jsonl_file, encoding='utf-8') as f:
                        lines = sum(1 for line in f if line.strip())
                    total_lines += lines
                    self.report['input_chunk_files'].append({
                        'path': str(jsonl_file),
                        'batch': batch,
                        'line_count': lines,
                        'size_bytes': jsonl_file.stat().st_size,
                    })

        self.report['total_chunks_discovered'] = total_lines
        print(f"  Discovered {len(jsonl_files)} JSONL files with {total_lines} total chunks")

    # ------------------------------------------------------------------
    # Phase 2: JSON Validation
    # ------------------------------------------------------------------

    def _phase_json_validation(self):
        """Validate JSON structure."""
        print("\n2. JSON VALIDATION")

        valid_count = 0
        invalid_count = 0
        malformed_lines = []
        blank_lines = 0

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        line = line.strip()
                        if not line:
                            blank_lines += 1
                            continue
                        try:
                            json.loads(line)
                            valid_count += 1
                        except json.JSONDecodeError as e:
                            invalid_count += 1
                            malformed_lines.append({
                                'file': jsonl_file.name,
                                'line': line_num,
                                'error': str(e),
                            })

        self.report['validation_results']['json_validation'] = {
            'valid_json_count': valid_count,
            'invalid_json_count': invalid_count,
            'blank_lines': blank_lines,
            'malformed_lines_sample': malformed_lines[:5],
        }

        if invalid_count > 0:
            self.report['error_count'] += 1
            self.report['errors'].append(f"Found {invalid_count} malformed JSON lines")

        print(f"  Valid JSON: {valid_count}")
        print(f"  Invalid JSON: {invalid_count}")
        print(f"  Blank lines: {blank_lines}")

    # ------------------------------------------------------------------
    # Phase 3: Metadata Validation
    # ------------------------------------------------------------------

    def _phase_metadata_validation(self):
        """Validate metadata completeness."""
        print("\n3. METADATA VALIDATION")

        required_fields = {
            'chunk_id', 'batch_id', 'relative_path', 'filename', 'extension',
            'chunk_index', 'total_chunks_for_file', 'text', 'character_count',
            'word_count', 'estimated_tokens', 'source_sha256', 'chunk_sha256',
            'chunking_strategy', 'created_at_utc',
        }

        chunks_missing_fields = 0
        type_errors = []

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            missing = required_fields - set(obj.keys())
                            if missing:
                                chunks_missing_fields += 1
                                if len(type_errors) < 5:
                                    type_errors.append({
                                        'chunk_id': obj.get('chunk_id', 'UNKNOWN'),
                                        'missing_fields': sorted(list(missing)),
                                    })
                            # Type checking
                            if 'chunk_index' in obj and not isinstance(obj['chunk_index'], int):
                                if len(type_errors) < 5:
                                    type_errors.append({
                                        'chunk_id': obj.get('chunk_id'),
                                        'error': (
                                            f"chunk_index is "
                                            f"{type(obj['chunk_index']).__name__}, expected int"
                                        ),
                                    })
                        except json.JSONDecodeError:
                            pass

        self.report['validation_results']['metadata_validation'] = {
            'chunks_missing_required_fields': chunks_missing_fields,
            'type_errors_sample': type_errors,
        }

        if chunks_missing_fields > 0:
            self.report['error_count'] += 1
            self.report['errors'].append(
                f"Found {chunks_missing_fields} chunks missing required fields"
            )

        print(f"  Chunks with missing fields: {chunks_missing_fields}")
        print(f"  Type errors found: {len(type_errors)}")

    # ------------------------------------------------------------------
    # Phase 4: Source Traceability
    # ------------------------------------------------------------------

    def _phase_source_traceability(self):
        """Verify chunks are traceable to source files."""
        print("\n4. SOURCE TRACEABILITY")

        missing_sources = []
        verified_sources = 0

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            cleaned_batch_dir = self.cleaned_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            batch_id = obj.get('batch_id')
                            rel_path = obj.get('relative_path')

                            if batch_id and batch_id != batch:
                                self.report['warnings'].append(
                                    f"Batch ID mismatch: chunk has {batch_id}, "
                                    f"file is in {batch}"
                                )
                                self.report['warning_count'] += 1

                            if rel_path:
                                source_file = cleaned_batch_dir / rel_path
                                if not source_file.exists():
                                    missing_sources.append({
                                        'batch': batch,
                                        'relative_path': rel_path,
                                        'chunk_id': obj.get('chunk_id'),
                                    })
                                else:
                                    verified_sources += 1
                        except json.JSONDecodeError:
                            pass

        self.report['validation_results']['source_traceability'] = {
            'verified_sources': verified_sources,
            'missing_sources': len(missing_sources),
            'missing_sources_sample': missing_sources[:5],
        }

        if missing_sources:
            self.report['error_count'] += 1
            self.report['errors'].append(
                f"Found {len(missing_sources)} chunks with missing source files"
            )

        print(f"  Verified sources: {verified_sources}")
        print(f"  Missing sources: {len(missing_sources)}")

    # ------------------------------------------------------------------
    # Phase 5: Hash Validation
    # ------------------------------------------------------------------

    def _phase_hash_validation(self):
        """Verify SHA-256 hashes — all file I/O uses utf-8."""
        print("\n5. HASH VALIDATION")

        chunk_hash_mismatches = []
        source_hash_mismatches = []
        hashes_verified = 0

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            cleaned_batch_dir = self.cleaned_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            stored_source_sha = obj.get('source_sha256')
                            rel_path = obj.get('relative_path')
                            stored_chunk_sha = obj.get('chunk_sha256')
                            text = obj.get('text', '')

                            # ---- Verify chunk SHA from text ----
                            recalc_chunk_sha = calculate_sha256(text)
                            if stored_chunk_sha != recalc_chunk_sha:
                                if len(chunk_hash_mismatches) < 10:
                                    chunk_hash_mismatches.append({
                                        'chunk_id': obj.get('chunk_id'),
                                        'type': 'chunk_hash_mismatch',
                                        'stored_sha': stored_chunk_sha,
                                        'calculated_sha': recalc_chunk_sha,
                                    })
                            else:
                                hashes_verified += 1

                            # ---- Verify source SHA from file ----
                            if rel_path and stored_source_sha and cleaned_batch_dir.exists():
                                source_file = cleaned_batch_dir / rel_path
                                if source_file.exists():
                                    with open(source_file, 'r', encoding='utf-8',
                                              errors='replace') as sf:
                                        source_text = sf.read()
                                    recalc_source_sha = calculate_sha256(source_text)
                                    if stored_source_sha != recalc_source_sha:
                                        if len(source_hash_mismatches) < 10:
                                            source_hash_mismatches.append({
                                                'chunk_id': obj.get('chunk_id'),
                                                'type': 'source_hash_mismatch',
                                                'stored_source_sha': stored_source_sha,
                                                'calculated_source_sha': recalc_source_sha,
                                                'relative_path': rel_path,
                                            })
                        except json.JSONDecodeError:
                            pass

        all_mismatches = chunk_hash_mismatches + source_hash_mismatches
        self.report['validation_results']['hash_validation'] = {
            'hashes_verified': hashes_verified,
            'hash_mismatches': len(all_mismatches),
            'chunk_hash_mismatches': len(chunk_hash_mismatches),
            'source_hash_mismatches': len(source_hash_mismatches),
            'mismatches_sample': all_mismatches[:10],
        }

        if all_mismatches:
            self.report['error_count'] += 1
            self.report['errors'].append(
                f"Found {len(all_mismatches)} hash mismatches "
                f"(chunk={len(chunk_hash_mismatches)}, "
                f"source={len(source_hash_mismatches)})"
            )

        print(f"  Hashes verified: {hashes_verified}")
        print(f"  Hash mismatches: {len(all_mismatches)}")

    # ------------------------------------------------------------------
    # Phase 6: Chunk ID Validation
    # ------------------------------------------------------------------

    def _phase_chunk_id_validation(self):
        """Verify chunk IDs are unique and deterministic."""
        print("\n6. CHUNK ID VALIDATION")

        chunk_ids = Counter()
        duplicate_ids = []
        invalid_ids = []
        id_pattern = re.compile(r'^batch_\d{2}_[a-f0-9]{8}_chunk_\d{6}$')

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            chunk_id = obj.get('chunk_id', '')
                            chunk_ids[chunk_id] += 1
                            if not id_pattern.match(chunk_id):
                                if len(invalid_ids) < 5:
                                    invalid_ids.append(chunk_id)
                        except json.JSONDecodeError:
                            pass

        for chunk_id, count in chunk_ids.items():
            if count > 1:
                duplicate_ids.append({'chunk_id': chunk_id, 'count': count})

        self.report['validation_results']['chunk_id_validation'] = {
            'total_unique_ids': len(chunk_ids),
            'duplicate_ids': len(duplicate_ids),
            'invalid_id_format': len(invalid_ids),
            'duplicate_ids_sample': duplicate_ids[:5],
            'invalid_ids_sample': invalid_ids[:5],
        }

        if duplicate_ids:
            self.report['error_count'] += 1
            self.report['errors'].append(
                f"Found {len(duplicate_ids)} duplicate chunk IDs"
            )

        print(f"  Total unique chunk IDs: {len(chunk_ids)}")
        print(f"  Duplicate IDs: {len(duplicate_ids)}")
        print(f"  Invalid ID format: {len(invalid_ids)}")

    # ------------------------------------------------------------------
    # Phase 7: Index Validation
    # CRITICAL FIX: Key on (batch_id, relative_path) not just relative_path.
    # The same relative_path can legitimately appear in multiple batches
    # (the same file is present in batch_01, batch_02, and batch_03).
    # Grouping by relative_path alone causes false index errors.
    # ------------------------------------------------------------------

    def _phase_index_validation(self):
        """Verify chunk indexes are sequential and consistent."""
        print("\n7. INDEX VALIDATION")

        index_errors = []
        # Key: (batch_id, relative_path) — NOT just relative_path
        files_by_source = defaultdict(list)

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            rel_path = obj.get('relative_path', '')
                            batch_id = obj.get('batch_id', batch)
                            chunk_idx = obj.get('chunk_index', -1)
                            total_chunks = obj.get('total_chunks_for_file', 0)

                            # Use (batch_id, relative_path) as the key
                            key = (batch_id, rel_path)
                            files_by_source[key].append({
                                'chunk_id': obj.get('chunk_id'),
                                'index': chunk_idx,
                                'total': total_chunks,
                            })
                        except json.JSONDecodeError:
                            pass

        # Verify sequences
        for (batch_id, source_path), chunks in files_by_source.items():
            if not chunks:
                continue

            sorted_chunks = sorted(chunks, key=lambda x: x['index'])
            actual_count = len(sorted_chunks)

            # Check stored total_chunks_for_file is correct
            for chunk in sorted_chunks:
                if chunk['total'] != actual_count:
                    if len(index_errors) < 20:
                        index_errors.append({
                            'batch': batch_id,
                            'source': source_path,
                            'stored_total': chunk['total'],
                            'actual_count': actual_count,
                            'chunk_id': chunk['chunk_id'],
                        })

            # Check indexes are sequential 0..N-1
            expected_total = sorted_chunks[0]['total']
            if actual_count != expected_total:
                if len(index_errors) < 20:
                    index_errors.append({
                        'batch': batch_id,
                        'source': source_path,
                        'error': 'total_count_mismatch',
                        'expected_chunks': expected_total,
                        'actual_chunks': actual_count,
                    })

            for i, chunk in enumerate(sorted_chunks):
                if chunk['index'] != i:
                    if len(index_errors) < 20:
                        index_errors.append({
                            'batch': batch_id,
                            'source': source_path,
                            'error': 'index_out_of_sequence',
                            'expected_index': i,
                            'actual_index': chunk['index'],
                            'chunk_id': chunk['chunk_id'],
                        })

        self.report['validation_results']['index_validation'] = {
            'files_checked': len(files_by_source),
            'index_errors': len(index_errors),
            'errors_sample': index_errors[:10],
        }

        if index_errors:
            self.report['error_count'] += 1
            self.report['errors'].append(
                f"Found {len(index_errors)} index consistency errors"
            )

        print(f"  Files checked: {len(files_by_source)}")
        print(f"  Index errors: {len(index_errors)}")

    # ------------------------------------------------------------------
    # Phase 8: Text Validation
    # ------------------------------------------------------------------

    def _phase_text_validation(self):
        """Validate chunk text content."""
        print("\n8. TEXT VALIDATION")

        empty_text = 0
        whitespace_only = 0
        invalid_encoding = 0
        suspicious_content = 0

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            text = obj.get('text', '')

                            if not text:
                                empty_text += 1
                            elif not text.strip():
                                whitespace_only += 1

                            if '\ufffd' in text:
                                invalid_encoding += 1

                            if len(text) > 100:
                                unique_chars = len(set(text))
                                if unique_chars < 20:
                                    suspicious_content += 1
                        except json.JSONDecodeError:
                            pass

        self.report['validation_results']['text_validation'] = {
            'empty_text': empty_text,
            'whitespace_only': whitespace_only,
            'invalid_encoding_indicators': invalid_encoding,
            'suspicious_repetitive_content': suspicious_content,
        }

        if empty_text > 0 or whitespace_only > 0:
            self.report['error_count'] += 1
            self.report['errors'].append(
                f"Found {empty_text + whitespace_only} chunks with empty/whitespace-only text"
            )

        print(f"  Empty text: {empty_text}")
        print(f"  Whitespace-only: {whitespace_only}")
        print(f"  Invalid encoding indicators: {invalid_encoding}")
        print(f"  Suspicious repetitive content: {suspicious_content}")

    # ------------------------------------------------------------------
    # Phase 9: Content Consistency
    # ------------------------------------------------------------------

    def _phase_content_consistency(self):
        """Verify stored metadata matches actual content (independent recomputation)."""
        print("\n9. CONTENT CONSISTENCY")

        char_count_mismatches = 0
        word_count_mismatches = 0
        token_count_mismatches = 0
        mismatch_samples = []

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            text = obj.get('text', '')
                            stored_char = obj.get('character_count', 0)
                            stored_words = obj.get('word_count', 0)
                            stored_tokens = obj.get('estimated_tokens', 0)

                            # Independent recalculation
                            actual_chars = len(text)
                            actual_words = count_words(text)
                            actual_tokens = calculate_token_estimate(actual_words)

                            char_ok = actual_chars == stored_char
                            word_ok = actual_words == stored_words
                            token_ok = actual_tokens == stored_tokens

                            if not char_ok:
                                char_count_mismatches += 1
                            if not word_ok:
                                word_count_mismatches += 1
                            if not token_ok:
                                token_count_mismatches += 1

                            if (not char_ok or not word_ok or not token_ok) and len(mismatch_samples) < 5:
                                mismatch_samples.append({
                                    'chunk_id': obj.get('chunk_id'),
                                    'stored_chars': stored_char,
                                    'actual_chars': actual_chars,
                                    'stored_words': stored_words,
                                    'actual_words': actual_words,
                                    'stored_tokens': stored_tokens,
                                    'actual_tokens': actual_tokens,
                                })
                        except json.JSONDecodeError:
                            pass

        self.report['validation_results']['content_consistency'] = {
            'character_count_mismatches': char_count_mismatches,
            'word_count_mismatches': word_count_mismatches,
            'token_count_mismatches': token_count_mismatches,
            'mismatch_samples': mismatch_samples,
        }

        total_mismatches = char_count_mismatches + word_count_mismatches + token_count_mismatches
        if total_mismatches > 0:
            self.report['error_count'] += 1
            self.report['errors'].append(
                f"Content consistency mismatches: "
                f"char={char_count_mismatches}, "
                f"words={word_count_mismatches}, "
                f"tokens={token_count_mismatches}"
            )

        print(f"  Character count mismatches: {char_count_mismatches}")
        print(f"  Word count mismatches: {word_count_mismatches}")
        print(f"  Token count mismatches: {token_count_mismatches}")

    # ------------------------------------------------------------------
    # Phase 10: Token Distribution
    # ------------------------------------------------------------------

    def _phase_token_distribution(self):
        """Analyze token distribution."""
        print("\n10. TOKEN DISTRIBUTION ANALYSIS")

        all_tokens = []
        all_chars = []
        all_words = []
        size_buckets = Counter()

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            tokens = obj.get('estimated_tokens', 0)
                            chars = obj.get('character_count', 0)
                            words = obj.get('word_count', 0)

                            all_tokens.append(tokens)
                            all_chars.append(chars)
                            all_words.append(words)

                            if tokens < self.VERY_SMALL_TOKENS:
                                size_buckets['VERY_SMALL'] += 1
                            elif tokens < self.SMALL_TOKENS:
                                size_buckets['SMALL'] += 1
                            elif tokens <= self.NORMAL_TOKENS_MAX:
                                size_buckets['NORMAL'] += 1
                            elif tokens < self.VERY_LARGE_TOKENS:
                                size_buckets['LARGE'] += 1
                            else:
                                size_buckets['VERY_LARGE'] += 1
                        except json.JSONDecodeError:
                            pass

        all_tokens.sort()
        distribution = {
            'total_chunks': len(all_tokens),
            'total_characters': sum(all_chars),
            'total_words': sum(all_words),
            'total_tokens': sum(all_tokens),
            'average_tokens': round(sum(all_tokens) / len(all_tokens), 2) if all_tokens else 0,
            'median_tokens': median(all_tokens) if all_tokens else 0,
            'min_tokens': min(all_tokens) if all_tokens else 0,
            'max_tokens': max(all_tokens) if all_tokens else 0,
            'stdev_tokens': self._calculate_stdev(all_tokens),
        }

        if len(all_tokens) >= 4:
            p25, p75 = quantiles(all_tokens, n=4)[1:3]
            distribution['p25_tokens'] = p25
            distribution['p75_tokens'] = p75
        if len(all_tokens) >= 20:
            distribution['p90_tokens'] = quantiles(all_tokens, n=10)[8]
            distribution['p95_tokens'] = quantiles(all_tokens, n=20)[18]
            distribution['p99_tokens'] = quantiles(all_tokens, n=100)[97]

        distribution['size_distribution'] = dict(size_buckets)
        distribution['size_distribution_percent'] = {
            k: round(v / len(all_tokens) * 100, 2) if all_tokens else 0
            for k, v in size_buckets.items()
        }

        self.report['token_distribution'] = distribution

        print(f"  Total chunks: {distribution['total_chunks']}")
        print(f"  Average tokens/chunk: {distribution['average_tokens']}")
        print(f"  Median tokens/chunk: {distribution['median_tokens']}")
        print(f"  Min/Max: {distribution['min_tokens']}/{distribution['max_tokens']}")
        print(f"  Size distribution: {dict(size_buckets)}")

    # ------------------------------------------------------------------
    # Phase 11: Duplicate Analysis
    # ------------------------------------------------------------------

    def _phase_duplicate_analysis(self):
        """Analyze duplicate chunks."""
        print("\n11. DUPLICATE ANALYSIS")

        chunk_hashes = defaultdict(list)

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            chunk_sha = obj.get('chunk_sha256', '')
                            if chunk_sha:
                                chunk_hashes[chunk_sha].append({
                                    'batch': batch,
                                    'relative_path': obj.get('relative_path'),
                                    'chunk_id': obj.get('chunk_id'),
                                })
                        except json.JSONDecodeError:
                            pass

        unique_chunks = sum(1 for v in chunk_hashes.values() if len(v) == 1)
        duplicate_chunks = sum(
            len(v) - 1 for v in chunk_hashes.values() if len(v) > 1
        )
        duplicate_groups = sum(1 for v in chunk_hashes.values() if len(v) > 1)

        # Cross-batch duplicates
        cross_batch_groups = []
        for chunk_sha, locations in chunk_hashes.items():
            if len(locations) > 1:
                batches = {loc['batch'] for loc in locations}
                if len(batches) > 1:
                    cross_batch_groups.append({
                        'chunk_sha': chunk_sha,
                        'batches': sorted(list(batches)),
                        'count': len(locations),
                    })

        total = unique_chunks + duplicate_chunks
        self.report['duplicate_analysis'] = {
            'unique_chunks': unique_chunks,
            'duplicate_chunks': duplicate_chunks,
            'duplicate_groups': duplicate_groups,
            'duplicate_percentage': (
                round(duplicate_chunks / total * 100, 2) if total > 0 else 0
            ),
            'cross_batch_duplicate_groups': len(cross_batch_groups),
            'cross_batch_duplicates': sum(
                g['count'] - 1 for g in cross_batch_groups
            ),
            'cross_batch_groups_sample': cross_batch_groups[:5],
        }

        print(f"  Unique chunks: {unique_chunks}")
        print(f"  Duplicate chunks: {duplicate_chunks}")
        print(f"  Duplicate groups: {duplicate_groups}")
        print(
            f"  Duplicate percentage: "
            f"{self.report['duplicate_analysis']['duplicate_percentage']}%"
        )
        print(f"  Cross-batch duplicate groups: {len(cross_batch_groups)}")

    # ------------------------------------------------------------------
    # Phase 12: Source Coverage
    # ------------------------------------------------------------------

    def _phase_source_coverage(self):
        """Analyze source file coverage."""
        print("\n12. SOURCE FILE COVERAGE")

        cleaned_files = set()
        represented_files = set()

        # Count cleaned files
        for batch in self.batch_names:
            cleaned_batch_dir = self.cleaned_root / batch
            if cleaned_batch_dir.exists():
                for file in cleaned_batch_dir.rglob('*'):
                    if file.is_file():
                        rel = file.relative_to(cleaned_batch_dir).as_posix()
                        cleaned_files.add((batch, rel))

        # Count represented files in chunks
        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            rel_path = obj.get('relative_path', '')
                            batch_id = obj.get('batch_id', batch)
                            if rel_path:
                                represented_files.add((batch_id, rel_path))
                        except json.JSONDecodeError:
                            pass

        missing_files = cleaned_files - represented_files

        self.report['source_coverage'] = {
            'total_cleaned_files': len(cleaned_files),
            'files_represented_in_chunks': len(represented_files),
            'files_with_zero_chunks': len(missing_files),
            'coverage_percentage': (
                round(len(represented_files) / len(cleaned_files) * 100, 2)
                if cleaned_files else 100.0
            ),
            'missing_files_sample': [
                {'batch': b, 'relative_path': p}
                for b, p in sorted(list(missing_files))[:5]
            ],
        }

        print(f"  Total cleaned files: {len(cleaned_files)}")
        print(f"  Files in chunks: {len(represented_files)}")
        print(f"  Files with zero chunks: {len(missing_files)}")
        print(f"  Coverage: {self.report['source_coverage']['coverage_percentage']}%")

    # ------------------------------------------------------------------
    # Phase 13: Chunking Strategy
    # ------------------------------------------------------------------

    def _phase_chunking_strategy(self):
        """Analyze chunking strategy distribution."""
        print("\n13. CHUNKING STRATEGY ANALYSIS")

        strategy_counts = Counter()
        extension_strategy_map = defaultdict(Counter)

        for batch in self.batch_names:
            batch_dir = self.chunks_root / batch
            if not batch_dir.exists():
                continue
            for jsonl_file in sorted(batch_dir.glob('*.jsonl')):
                with open(jsonl_file, encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            strategy = obj.get('chunking_strategy', 'UNKNOWN')
                            ext = obj.get('extension', 'UNKNOWN')
                            strategy_counts[strategy] += 1
                            extension_strategy_map[ext][strategy] += 1
                        except json.JSONDecodeError:
                            pass

        self.report['chunking_strategy_distribution'] = {
            'strategy_counts': dict(strategy_counts),
            'extension_strategy_map': {
                k: dict(v) for k, v in extension_strategy_map.items()
            },
        }

        print(f"  Strategies used: {dict(strategy_counts)}")

    # ------------------------------------------------------------------
    # Phase 14: Quality Score
    # ------------------------------------------------------------------

    def _calculate_quality_score(self):
        """Calculate overall quality score."""
        print("\n14. QUALITY SCORE CALCULATION")

        score = 100.0

        if self.report['validation_results']['json_validation']['invalid_json_count'] > 0:
            score -= 10

        if self.report['validation_results']['metadata_validation']['chunks_missing_required_fields'] > 0:
            score -= 15

        if self.report['validation_results']['source_traceability']['missing_sources'] > 0:
            score -= 10

        if self.report['validation_results']['hash_validation']['hash_mismatches'] > 0:
            score -= 10

        if self.report['validation_results']['chunk_id_validation']['duplicate_ids'] > 0:
            score -= 15

        if self.report['validation_results']['chunk_id_validation']['invalid_id_format'] > 0:
            score -= 5

        if self.report['validation_results']['index_validation']['index_errors'] > 0:
            score -= 10

        if self.report['validation_results']['text_validation']['empty_text'] > 0:
            score -= 5

        if self.report['validation_results']['content_consistency']['character_count_mismatches'] > 0:
            score -= 10

        if self.report['duplicate_analysis'].get('duplicate_percentage', 0) > 50:
            score -= 5

        if self.report['source_coverage']['coverage_percentage'] < 100:
            score -= 5

        # Bonus for zero critical errors
        if (self.report['error_count'] == 0 and
                self.report['validation_results']['chunk_id_validation']['duplicate_ids'] == 0):
            score = min(100, score + 5)

        self.report['quality_score'] = max(0, score)

        # Determine final status
        if self.report['error_count'] == 0:
            if self.report['warning_count'] == 0:
                self.report['final_status'] = 'PASS'
            else:
                self.report['final_status'] = 'PASS_WITH_WARNINGS'
        else:
            self.report['final_status'] = 'FAIL'

        print(f"  Quality score: {self.report['quality_score']}/100")
        print(f"  Final status: {self.report['final_status']}")

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _calculate_stdev(values):
        """Calculate standard deviation."""
        if len(values) < 2:
            return 0
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return round(variance ** 0.5, 2)
