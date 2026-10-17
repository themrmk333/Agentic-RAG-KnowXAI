import json
from pathlib import Path

chunks_root = Path('data/chunks')
batch_dir = chunks_root / 'batch_01'
jsonl_file = batch_dir / 'chunks.jsonl'

target_id = 'batch_01_acfac07d_chunk_000000'

with open(jsonl_file) as f:
    for line in f:
        line_stripped = line.strip()
        if not line_stripped:
            continue
        
        obj = json.loads(line_stripped)
        if obj.get('chunk_id') == target_id:
            text = obj.get('text', '')
            print(f"Chunk {target_id}:")
            print(f"  Raw line length: {len(line_stripped)}")
            print(f"  Parsed text field length: {len(text)}")
            print(f"  character_count field: {obj.get('character_count')}")
            print(f"  word_count field: {obj.get('word_count')}")
            print(f"  estimated_tokens field: {obj.get('estimated_tokens')}")
            print()
            print(f"First 50 chars: {repr(text[:50])}")
            print(f"Last 50 chars: {repr(text[-50:])}")
            
            # Check if there's a null terminator or other issue
            print(f"Text contains null: {chr(0) in text}")
            print(f"Text ends with newline: {text.endswith(chr(10))}")
            break
