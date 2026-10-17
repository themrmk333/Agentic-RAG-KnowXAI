"""Check if text changes during JSON serialization."""

import json
from pathlib import Path
from rag.chunking.models import Chunk, ChunkMetadata, count_words, calculate_token_estimate, calculate_sha256

# Create a test chunk
test_text = """# Heading
This is test content with special characters: é, ñ, 中文
Line 2: Hello "world" with 'quotes'
Tab	separated	columns
End of test."""

test_metadata = ChunkMetadata(
    chunk_id="test_chunk_001",
    batch_id="batch_01",
    source_file="test.md",
    relative_path="test.md",
    filename="test.md",
    extension=".md",
    chunk_index=0,
    total_chunks_for_file=1,
    character_count=len(test_text),
    word_count=count_words(test_text),
    estimated_tokens=calculate_token_estimate(count_words(test_text)),
    source_sha256="abc123",
    chunk_sha256=calculate_sha256(test_text),
    heading_context="",
    chunking_strategy="TextChunker",
)

test_chunk = Chunk(metadata=test_metadata, text=test_text)

print("=" * 70)
print("TESTING JSON SERIALIZATION")
print("=" * 70)

print("\nOriginal chunk text:")
print(f"  Length: {len(test_chunk.text)}")
print(f"  Word count: {count_words(test_chunk.text)}")
print(f"  First 50 chars: {repr(test_chunk.text[:50])}")

# Serialize to JSONL
jsonl_line = test_chunk.to_jsonl_line()
print(f"\nJSONL line length: {len(jsonl_line)}")

# Deserialize back
parsed_obj = json.loads(jsonl_line)
text_from_json = parsed_obj['text']

print(f"\nDeserialized text:")
print(f"  Length: {len(text_from_json)}")
print(f"  Word count: {count_words(text_from_json)}")
print(f"  First 50 chars: {repr(text_from_json[:50])}")

print(f"\nComparison:")
print(f"  Text identical: {test_chunk.text == text_from_json}")
print(f"  Length match: {len(test_chunk.text) == len(text_from_json)}")
print(f"  Word count match: {count_words(test_chunk.text) == count_words(text_from_json)}")

if test_chunk.text != text_from_json:
    print(f"\nDifference found!")
    print(f"  Original: {repr(test_chunk.text)}")
    print(f"  From JSON: {repr(text_from_json)}")
