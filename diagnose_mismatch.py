"""Diagnostic script to understand metadata mismatch root cause."""

import json
from pathlib import Path
from rag.chunking.models import count_words, calculate_token_estimate, calculate_sha256

# Check a few failing chunks from each chunker type
chunks_root = Path('data/chunks')
cleaned_root = Path('data/cleaned')

failing_chunks = {
    'markdown': 'batch_01_acfac07d_chunk_000000',  # MarkdownChunker
    'json': 'batch_01_2ac52650_chunk_000000',  # JSONChunker (need to verify)
    'csv': 'batch_01_cb56bfe1_chunk_000000',  # CSVChunker (need to verify)
}

print("=" * 70)
print("ANALYZING METADATA MISMATCH ROOT CAUSE")
print("=" * 70)

for batch_dir in sorted(chunks_root.glob('batch_*')):
    jsonl_file = batch_dir / 'chunks.jsonl'
    if not jsonl_file.exists():
        continue
    
    print(f"\nAnalyzing {batch_dir.name}...")
    
    with open(jsonl_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            obj = json.loads(line)
            chunk_id = obj.get('chunk_id')
            text = obj.get('text', '')
            strategy = obj.get('chunking_strategy', '')
            
            # Check for mismatch
            stored_char = obj.get('character_count', 0)
            stored_word = obj.get('word_count', 0)
            stored_token = obj.get('estimated_tokens', 0)
            
            actual_char = len(text)
            actual_word = count_words(text)
            actual_token = calculate_token_estimate(actual_word)
            
            has_mismatch = (actual_char != stored_char or 
                           actual_word != stored_word or 
                           actual_token != stored_token)
            
            if has_mismatch and chunk_id in failing_chunks.values():
                print(f"\n  Chunk: {chunk_id}")
                print(f"  Strategy: {strategy}")
                print(f"  Character count: stored={stored_char}, actual={actual_char}, diff={actual_char - stored_char}")
                print(f"  Word count: stored={stored_word}, actual={actual_word}, diff={actual_word - stored_word}")
                print(f"  Token count: stored={stored_token}, actual={actual_token}, diff={actual_token - stored_token}")
                print(f"  Text length check: len(text)={len(text)}")
                print(f"  Text starts: {repr(text[:80])}")
                print(f"  Text ends: {repr(text[-80:])}")
                print(f"  Text contains newlines: {chr(10) in text}")
                print(f"  Text contains tabs: {chr(9) in text}")
                
                # Try to find the source file
                rel_path = obj.get('relative_path', '')
                batch_id = obj.get('batch_id', '')
                source_file = cleaned_root / batch_id / rel_path
                
                if source_file.exists():
                    print(f"  Source file found: {source_file}")
                    with open(source_file, 'r', encoding='utf-8') as sf:
                        source_text = sf.read()
                    print(f"  Source file size: {len(source_text)} characters")
                else:
                    print(f"  Source file not found: {source_file}")

print("\n" + "=" * 70)
print("DIAGNOSIS COMPLETE")
print("=" * 70)
