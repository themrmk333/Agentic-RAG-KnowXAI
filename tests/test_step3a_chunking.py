"""
Step 3A — Regression Tests for Chunking Integrity

Tests cover:
  1.  character_count after chunk creation
  2.  word_count after chunk creation
  3.  token estimate after chunk creation
  4.  SHA-256 integrity
  5.  chunk_index generation (sequential 0..N-1)
  6.  total_chunks_for_file correctness
  7.  deterministic chunk IDs (same input → same ID)
  8.  Markdown chunking
  9.  JSON chunking
  10. CSV chunking
  11. Generic text chunking
  12. JSONL serialization / deserialization
  13. UTF-8 encoding integrity (multi-byte chars)
  14. Pipeline metadata independence (metadata != pre-merge values)
"""

import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

# Ensure project root is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from rag.chunking.models import Chunk, ChunkMetadata, count_words, calculate_token_estimate, calculate_sha256
from rag.chunking.chunker import BaseChunker
from rag.chunking.markdown_chunker import MarkdownChunker
from rag.chunking.json_chunker import JSONChunker
from rag.chunking.csv_chunker import CSVChunker
from rag.chunking.text_chunker import TextChunker
from rag.chunking.pipeline_repaired import RepairedChunkingPipeline, _build_chunk_record


# ============================================================
# Helpers
# ============================================================

DUMMY_ARGS = {
    'source_path': 'test_file.md',
    'batch_id': 'batch_01',
    'source_sha256': 'a' * 64,
    'relative_path': 'test_file.md',
    'filename': 'test_file.md',
    'extension': '.md',
}


def _chunk(chunker, text, ext='.md'):
    args = {**DUMMY_ARGS, 'extension': ext}
    return chunker.chunk(text=text, **{k: v for k, v in args.items()})


def verify_chunk_integrity(chunk: Chunk, label: str = ''):
    """Assert that all metadata fields match the actual text."""
    t = chunk.text
    assert len(t) == chunk.metadata.character_count, (
        f"{label} char_count mismatch: "
        f"len(text)={len(t)}, stored={chunk.metadata.character_count}"
    )
    wc = count_words(t)
    assert wc == chunk.metadata.word_count, (
        f"{label} word_count mismatch: "
        f"actual={wc}, stored={chunk.metadata.word_count}"
    )
    tok = calculate_token_estimate(wc)
    assert tok == chunk.metadata.estimated_tokens, (
        f"{label} token mismatch: actual={tok}, stored={chunk.metadata.estimated_tokens}"
    )
    sha = calculate_sha256(t)
    assert sha == chunk.metadata.chunk_sha256, (
        f"{label} sha256 mismatch:\n"
        f"  actual={sha}\n"
        f"  stored={chunk.metadata.chunk_sha256}"
    )


def verify_index_integrity(chunks, label: str = ''):
    """Assert sequential index and correct total_chunks_for_file."""
    n = len(chunks)
    for i, c in enumerate(chunks):
        assert c.metadata.chunk_index == i, (
            f"{label} chunk_index at position {i} is "
            f"{c.metadata.chunk_index}, expected {i}"
        )
        assert c.metadata.total_chunks_for_file == n, (
            f"{label} total_chunks_for_file for chunk {i} is "
            f"{c.metadata.total_chunks_for_file}, expected {n}"
        )


# ============================================================
# Test 1: character_count
# ============================================================
def test_01_character_count():
    """character_count == len(text) for every chunk."""
    texts = [
        "Hello world",
        "A" * 500,
        "Multi\nline\ntext with newlines\n\nand blank lines.",
        "Unicode: café, naïve, Ångström — em-dash – en-dash",
        "",  # empty -> single chunk of empty text skipped by pipeline
    ]
    chunker = TextChunker()
    for text in texts:
        if not text.strip():
            continue
        for chunk in _chunk(chunker, text, '.txt'):
            verify_chunk_integrity(chunk, f"test_01 text={repr(text[:30])}")
    print("  PASS: test_01_character_count")


# ============================================================
# Test 2: word_count
# ============================================================
def test_02_word_count():
    """word_count == count_words(text) for every chunk."""
    samples = [
        "one two three",
        "  spaces   between   words  ",
        "hyphen-word and another-word",
        "numbers 123 and 456 here",
    ]
    chunker = TextChunker()
    for text in samples:
        for chunk in _chunk(chunker, text, '.txt'):
            wc = count_words(chunk.text)
            assert wc == chunk.metadata.word_count, (
                f"test_02 word_count mismatch: actual={wc}, "
                f"stored={chunk.metadata.word_count}"
            )
    print("  PASS: test_02_word_count")


# ============================================================
# Test 3: token estimate
# ============================================================
def test_03_token_estimate():
    """estimated_tokens == calculate_token_estimate(word_count)."""
    chunker = TextChunker()
    text = "This is a sentence. " * 20
    for chunk in _chunk(chunker, text, '.txt'):
        wc = count_words(chunk.text)
        expected_tok = calculate_token_estimate(wc)
        assert chunk.metadata.estimated_tokens == expected_tok, (
            f"test_03 token mismatch: expected={expected_tok}, "
            f"stored={chunk.metadata.estimated_tokens}"
        )
    print("  PASS: test_03_token_estimate")


# ============================================================
# Test 4: SHA-256 integrity
# ============================================================
def test_04_sha256_integrity():
    """chunk_sha256 == SHA256(text.encode('utf-8'))."""
    texts_with_unicode = [
        "Basic ASCII text",
        "Café – naïve – résumé",
        "日本語テスト",
        "Emoji 🚀🎯",
        "Mixed: café and 日本語 and emoji 🚀",
    ]
    chunker = TextChunker()
    for text in texts_with_unicode:
        for chunk in _chunk(chunker, text, '.txt'):
            expected = hashlib.sha256(chunk.text.encode('utf-8')).hexdigest()
            assert chunk.metadata.chunk_sha256 == expected, (
                f"test_04 sha256 mismatch for text={repr(text[:30])}"
            )
    print("  PASS: test_04_sha256_integrity")


# ============================================================
# Test 5: chunk_index sequential
# ============================================================
def test_05_chunk_index_sequential():
    """chunk_index values are 0, 1, 2, ..., N-1."""
    # Create text long enough to generate multiple chunks
    chunker = TextChunker()
    paragraph = "Word " * 100  # 100 words per paragraph
    text = "\n\n".join([paragraph] * 10)  # 10 paragraphs = ~1000 words
    chunks = _chunk(chunker, text, '.txt')
    verify_index_integrity(chunks, "test_05")
    print(f"  PASS: test_05_chunk_index_sequential ({len(chunks)} chunks)")


# ============================================================
# Test 6: total_chunks_for_file
# ============================================================
def test_06_total_chunks_for_file():
    """total_chunks_for_file == N on every chunk."""
    chunker = MarkdownChunker()
    # Build markdown with many sections to force multiple chunks
    sections = []
    for i in range(20):
        sections.append(f"## Section {i}\n\n" + "Content word. " * 100)
    text = "\n\n".join(sections)
    chunks = _chunk(chunker, text, '.md')
    n = len(chunks)
    for c in chunks:
        assert c.metadata.total_chunks_for_file == n, (
            f"test_06 total mismatch: stored={c.metadata.total_chunks_for_file}, n={n}"
        )
    print(f"  PASS: test_06_total_chunks_for_file (N={n})")


# ============================================================
# Test 7: Deterministic chunk IDs
# ============================================================
def test_07_deterministic_chunk_ids():
    """Same input -> same chunk IDs on repeated calls."""
    chunker = MarkdownChunker()
    text = "# Title\n\nSome content here.\n\n## Section\n\nMore content."
    chunks_a = _chunk(chunker, text, '.md')
    chunks_b = _chunk(chunker, text, '.md')

    assert len(chunks_a) == len(chunks_b), "test_07: different number of chunks"
    for a, b in zip(chunks_a, chunks_b):
        assert a.metadata.chunk_id == b.metadata.chunk_id, (
            f"test_07: non-deterministic chunk_id: {a.metadata.chunk_id} != {b.metadata.chunk_id}"
        )
        assert a.text == b.text, f"test_07: non-deterministic text"
    print(f"  PASS: test_07_deterministic_chunk_ids ({len(chunks_a)} chunks)")


# ============================================================
# Test 8: Markdown chunking
# ============================================================
def test_08_markdown_chunking():
    """Markdown chunker preserves headings and produces valid chunks."""
    md_text = """# Main Title

Introduction paragraph with some text here.

## Section One

Content for section one. This has multiple sentences.
More sentences in section one.

### Subsection 1.1

Content under subsection.

## Section Two

Content for section two.
"""
    chunker = MarkdownChunker()
    chunks = _chunk(chunker, md_text, '.md')
    assert len(chunks) >= 1, "test_08: no chunks produced"
    for c in chunks:
        verify_chunk_integrity(c, "test_08")
    verify_index_integrity(chunks, "test_08")
    print(f"  PASS: test_08_markdown_chunking ({len(chunks)} chunks)")


# ============================================================
# Test 9: JSON chunking
# ============================================================
def test_09_json_chunking():
    """JSON chunker produces valid chunks with correct metadata."""
    json_text = json.dumps({
        "id": 1,
        "name": "Test Document",
        "description": "A test document for chunking",
        "sections": [
            {"title": "Section A", "content": "Content A"},
            {"title": "Section B", "content": "Content B"},
        ],
        "metadata": {
            "created": "2024-01-01",
            "author": "Test Author",
        },
    }, indent=2)
    chunker = JSONChunker()
    chunks = _chunk(chunker, json_text, '.json')
    assert len(chunks) >= 1, "test_09: no chunks produced"
    for c in chunks:
        verify_chunk_integrity(c, "test_09")
    verify_index_integrity(chunks, "test_09")
    print(f"  PASS: test_09_json_chunking ({len(chunks)} chunks)")


# ============================================================
# Test 10: CSV chunking
# ============================================================
def test_10_csv_chunking():
    """CSV chunker preserves headers and groups rows correctly."""
    lines = ["Name,Department,Salary,Location"]
    for i in range(30):
        lines.append(f"Employee{i},Department{i % 5},{50000 + i * 1000},City{i}")
    csv_text = "\n".join(lines)
    chunker = CSVChunker()
    chunks = _chunk(chunker, csv_text, '.csv')
    assert len(chunks) >= 1, "test_10: no chunks produced"
    for c in chunks:
        verify_chunk_integrity(c, "test_10")
    verify_index_integrity(chunks, "test_10")
    print(f"  PASS: test_10_csv_chunking ({len(chunks)} chunks)")


# ============================================================
# Test 11: Generic text chunking
# ============================================================
def test_11_text_chunking():
    """TextChunker produces correct metadata for plain text."""
    text = "\n\n".join(["Paragraph " + str(i) + ". " + "word " * 50 for i in range(15)])
    chunker = TextChunker()
    chunks = _chunk(chunker, text, '.txt')
    assert len(chunks) >= 1, "test_11: no chunks produced"
    for c in chunks:
        verify_chunk_integrity(c, "test_11")
    verify_index_integrity(chunks, "test_11")
    print(f"  PASS: test_11_text_chunking ({len(chunks)} chunks)")


# ============================================================
# Test 12: JSONL serialization / deserialization
# ============================================================
def test_12_jsonl_roundtrip():
    """Chunk survives JSONL serialization without data loss."""
    chunker = MarkdownChunker()
    text = "# Test\n\nContent with unicode: café, naïve — em-dash.\n\n## More\n\nAdditional content."
    chunks = _chunk(chunker, text, '.md')

    for c in chunks:
        line = c.to_jsonl_line()
        assert '\n' not in line, "test_12: JSONL line contains newline"
        obj = json.loads(line)
        assert obj['text'] == c.text, "test_12: text changed after roundtrip"
        assert obj['character_count'] == c.metadata.character_count
        assert obj['word_count'] == c.metadata.word_count
        assert obj['estimated_tokens'] == c.metadata.estimated_tokens
        assert obj['chunk_sha256'] == c.metadata.chunk_sha256

        # Verify sha from deserialized text
        recalc = hashlib.sha256(obj['text'].encode('utf-8')).hexdigest()
        assert obj['chunk_sha256'] == recalc, (
            f"test_12: sha256 mismatch after roundtrip"
        )
    print(f"  PASS: test_12_jsonl_roundtrip ({len(chunks)} chunks)")


# ============================================================
# Test 13: UTF-8 multi-byte character integrity
# ============================================================
def test_13_utf8_integrity():
    """Multi-byte UTF-8 characters are handled correctly."""
    # Each of these has multi-byte chars
    texts = [
        "café résumé naïve Ångström",
        "Chinese: 中文 日本語 한국어",
        "Emoji: 🚀 🎯 ✅ ❌",
        "Em-dash — and en-dash – and ellipsis…",
        "Curly quotes: \u201cHello\u201d and \u2018world\u2019",
    ]
    chunker = TextChunker()
    for text in texts:
        chunks = _chunk(chunker, text, '.txt')
        for c in chunks:
            # The key test: character_count must match Python's len()
            assert len(c.text) == c.metadata.character_count, (
                f"test_13 char mismatch for {repr(text[:30])}: "
                f"len={len(c.text)}, stored={c.metadata.character_count}"
            )
            # SHA must match
            expected_sha = hashlib.sha256(c.text.encode('utf-8')).hexdigest()
            assert c.metadata.chunk_sha256 == expected_sha, (
                f"test_13 sha mismatch for {repr(text[:30])}"
            )
    print("  PASS: test_13_utf8_integrity")


# ============================================================
# Test 14: Pipeline metadata independence
# ============================================================
def test_14_pipeline_metadata_independence():
    """
    Verify that _build_chunk_record computes metadata from the text
    provided — not from any cached/pre-merge value.
    """
    # Simulate a text that would have been different before stripping
    final_text = "This is the final stripped text."
    pre_merge_text = "   This is the final stripped text.   \n\n"
    # If metadata were computed from pre_merge_text, char count would differ
    record = _build_chunk_record(
        text=final_text,
        chunk_index=0,
        total_chunks_for_file=1,
        batch_id='batch_01',
        relative_path='test.txt',
        filename='test.txt',
        extension='.txt',
        source_sha256='a' * 64,
        heading_context='',
        chunking_strategy='TextChunker',
        created_at_utc='2024-01-01T00:00:00+00:00',
    )

    assert record['character_count'] == len(final_text), (
        f"test_14: char_count={record['character_count']}, "
        f"expected={len(final_text)}"
    )
    expected_sha = hashlib.sha256(final_text.encode('utf-8')).hexdigest()
    assert record['chunk_sha256'] == expected_sha, "test_14: sha256 computed from wrong text"

    # Verify it does NOT match the pre_merge_text metrics
    assert record['character_count'] != len(pre_merge_text), (
        "test_14: metadata appears to come from pre-merge text"
    )
    print("  PASS: test_14_pipeline_metadata_independence")


# ============================================================
# Test 15: repaired pipeline on temp directory
# ============================================================
def test_15_repaired_pipeline_integrity():
    """
    End-to-end: run RepairedChunkingPipeline on a temp directory,
    then verify every chunk record has consistent metadata.
    """
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        cleaned = tmp_path / 'cleaned'
        chunks_out = tmp_path / 'chunks'
        manifests = tmp_path / 'manifests'

        # Create small synthetic batch
        batch_dir = cleaned / 'batch_01'
        batch_dir.mkdir(parents=True)

        (batch_dir / 'doc1.md').write_text(
            "# Title\n\nIntro paragraph.\n\n## Section\n\nContent here.",
            encoding='utf-8',
        )
        (batch_dir / 'data.json').write_text(
            json.dumps({"key": "value", "items": [1, 2, 3]}), encoding='utf-8'
        )
        # CSV
        (batch_dir / 'table.csv').write_text(
            "Name,Value\nAlice,10\nBob,20\nCarol,30", encoding='utf-8'
        )
        # Plain text with unicode
        (batch_dir / 'notes.txt').write_text(
            "Café résumé naïve.\n\nSecond paragraph.", encoding='utf-8'
        )

        # Run pipeline
        pipeline = RepairedChunkingPipeline(cleaned, chunks_out, manifests)
        stats = pipeline.run()

        # Verify
        jsonl = chunks_out / 'batch_01' / 'chunks.jsonl'
        assert jsonl.exists(), "test_15: chunks.jsonl not created"

        with open(jsonl, encoding='utf-8') as f:
            records = [json.loads(line) for line in f if line.strip()]

        assert len(records) > 0, "test_15: no records in output"

        for rec in records:
            text = rec['text']
            # character_count
            assert rec['character_count'] == len(text), (
                f"test_15 char_count mismatch: {rec['chunk_id']}"
            )
            # word_count
            assert rec['word_count'] == count_words(text), (
                f"test_15 word_count mismatch: {rec['chunk_id']}"
            )
            # tokens
            assert rec['estimated_tokens'] == calculate_token_estimate(rec['word_count']), (
                f"test_15 token mismatch: {rec['chunk_id']}"
            )
            # sha256
            expected_sha = hashlib.sha256(text.encode('utf-8')).hexdigest()
            assert rec['chunk_sha256'] == expected_sha, (
                f"test_15 sha mismatch: {rec['chunk_id']}"
            )

        # Verify index integrity per (batch_id, relative_path)
        from collections import defaultdict
        groups = defaultdict(list)
        for rec in records:
            key = (rec['batch_id'], rec['relative_path'])
            groups[key].append(rec)

        for key, grp in groups.items():
            grp_sorted = sorted(grp, key=lambda r: r['chunk_index'])
            n = len(grp_sorted)
            for i, r in enumerate(grp_sorted):
                assert r['chunk_index'] == i, (
                    f"test_15 index mismatch at {key}: expected {i}, got {r['chunk_index']}"
                )
                assert r['total_chunks_for_file'] == n, (
                    f"test_15 total mismatch at {key}: expected {n}, got {r['total_chunks_for_file']}"
                )

        print(f"  PASS: test_15_repaired_pipeline_integrity ({len(records)} records)")


# ============================================================
# Runner
# ============================================================

def run_all_tests():
    tests = [
        test_01_character_count,
        test_02_word_count,
        test_03_token_estimate,
        test_04_sha256_integrity,
        test_05_chunk_index_sequential,
        test_06_total_chunks_for_file,
        test_07_deterministic_chunk_ids,
        test_08_markdown_chunking,
        test_09_json_chunking,
        test_10_csv_chunking,
        test_11_text_chunking,
        test_12_jsonl_roundtrip,
        test_13_utf8_integrity,
        test_14_pipeline_metadata_independence,
        test_15_repaired_pipeline_integrity,
    ]

    print("\n" + "=" * 60)
    print("STEP 3A — REGRESSION TESTS")
    print("=" * 60)

    passed = 0
    failed = 0
    failures = []

    for test_fn in tests:
        name = test_fn.__name__
        try:
            test_fn()
            passed += 1
        except AssertionError as e:
            failed += 1
            failures.append((name, str(e)))
            print(f"  FAIL: {name}")
            print(f"    {e}")
        except Exception as e:
            failed += 1
            failures.append((name, str(e)))
            print(f"  ERROR: {name}")
            print(f"    {e}")

    print(f"\n{'='*60}")
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(tests)} tests")
    if failures:
        print("\nFAILURES:")
        for name, msg in failures:
            print(f"  {name}: {msg[:200]}")
    print("=" * 60)

    return failed == 0


# Support both direct run and pytest discovery
class TestChunkingIntegrity:
    def test_01(self): test_01_character_count()
    def test_02(self): test_02_word_count()
    def test_03(self): test_03_token_estimate()
    def test_04(self): test_04_sha256_integrity()
    def test_05(self): test_05_chunk_index_sequential()
    def test_06(self): test_06_total_chunks_for_file()
    def test_07(self): test_07_deterministic_chunk_ids()
    def test_08(self): test_08_markdown_chunking()
    def test_09(self): test_09_json_chunking()
    def test_10(self): test_10_csv_chunking()
    def test_11(self): test_11_text_chunking()
    def test_12(self): test_12_jsonl_roundtrip()
    def test_13(self): test_13_utf8_integrity()
    def test_14(self): test_14_pipeline_metadata_independence()
    def test_15(self): test_15_repaired_pipeline_integrity()


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
