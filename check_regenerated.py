"""Check if verification worked on regenerated chunks."""

import json
from pathlib import Path
from rag.chunking.models import count_words, calculate_token_estimate

chunks_root = Path('data/chunks')
batch_dir = chunks_root / 'batch_01'
jsonl_file = batch_dir / 'chunks.jsonl'

target_id = 'batch_01_acfac07d_chunk_000000'

print("Checking regenerated chunk:")

with open(jsonl_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        obj = json.loads(line)
        if obj.get('chunk_id') == target_id:
            text = obj.get('text', '')
            stored_char = obj.get('character_count', 0)
            stored_word = obj.get('word_count', 0)
            stored_token = obj.get('estimated_tokens', 0)
            
            actual_char = len(text)
            actual_word = count_words(text)
            actual_token = calculate_token_estimate(actual_word)
            
            print(f"Chunk ID: {target_id}")
            print(f"Stored metrics:")
            print(f"  character_count: {stored_char}")
            print(f"  word_count: {stored_word}")
            print(f"  estimated_tokens: {stored_token}")
            print()
            print(f"Actual metrics from text:")
            print(f"  character_count: {actual_char}")
            print(f"  word_count: {actual_word}")
            print(f"  estimated_tokens: {actual_token}")
            print()
            print(f"Match: char={stored_char == actual_char}, word={stored_word == actual_word}, token={stored_token == actual_token}")
            break
