"""Manually inspect one chunk from regenerated JSONL."""

import json
from pathlib import Path
from rag.chunking.models import count_words, calculate_token_estimate

chunks_root = Path('data/chunks')
batch_dir = chunks_root / 'batch_01'
jsonl_file = batch_dir / 'chunks.jsonl'

print("Inspecting first chunk from batch_01/chunks.jsonl:")
print()

with open(jsonl_file) as f:
    for line_num, line in enumerate(f):
        if line_num >= 1:  # Just first chunk
            break
        
        line = line.strip()
        if not line:
            continue
        
        obj = json.loads(line)
        
        print(f"Chunk ID: {obj.get('chunk_id')}")
        print(f"Chunk Strategy: {obj.get('chunking_strategy')}")
        print()
        
        text = obj.get('text', '')
        stored_char = obj.get('character_count', 0)
        stored_word = obj.get('word_count', 0)
        stored_token = obj.get('estimated_tokens', 0)
        
        actual_char = len(text)
        actual_word = count_words(text)
        actual_token = calculate_token_estimate(actual_word)
        
        print(f"Stored metadata:")
        print(f"  character_count: {stored_char}")
        print(f"  word_count: {stored_word}")
        print(f"  estimated_tokens: {stored_token}")
        print()
        
        print(f"Actual from text:")
        print(f"  character_count: {actual_char}")
        print(f"  word_count: {actual_word}")
        print(f"  estimated_tokens: {actual_token}")
        print()
        
        print(f"Match: {stored_char == actual_char and stored_word == actual_word and stored_token == actual_token}")
        print()
        
        # Show some text
        print(f"Text first 100 chars:")
        print(f"  {repr(text[:100])}")
