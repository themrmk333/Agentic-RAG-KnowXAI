import json
import hashlib
from pathlib import Path

# Extract the batch and hash from the chunk ID
chunk_id = 'batch_01_acfac07d_chunk_000000'
parts = chunk_id.split('_')
batch = parts[0] + '_' + parts[1]
source_hash_prefix = parts[2]

print(f"Looking for source file with hash prefix: {source_hash_prefix}")

# Find the source file with this hash
cleaned_root = Path('data/cleaned')
source_files = sorted(cleaned_root.glob('**/*'))

target_file = None
for sf in source_files:
    if sf.is_file():
        with open(sf, 'rb') as f:
            content = f.read()
            file_hash = hashlib.sha256(content).hexdigest()
            if file_hash.startswith(source_hash_prefix):
                target_file = sf
                print(f"Found source file: {target_file}")
                print(f"File size: {len(content)} bytes")
                print(f"Full hash: {file_hash}")
                break

if not target_file:
    print(f"Could not find source file with hash prefix {source_hash_prefix}")
    print("Checking first few files...")
    for sf in list(cleaned_root.glob('**/*'))[:5]:
        if sf.is_file():
            with open(sf, 'rb') as f:
                content = f.read()
                file_hash = hashlib.sha256(content).hexdigest()
                print(f"  {sf.name}: {file_hash[:16]}...")
