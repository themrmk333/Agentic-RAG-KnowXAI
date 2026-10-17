"""Chunk validation and consistency checking."""

import json
from pathlib import Path
from typing import List, Dict, Tuple
from collections import defaultdict


class ChunkValidator:
    """Validates chunks and JSONL output."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def validate_jsonl_file(self, filepath: Path) -> Tuple[int, List[str]]:
        """
        Validate JSONL file format and chunk integrity.
        
        Returns: (valid_line_count, error_list)
        """
        valid_count = 0
        invalid_lines = []
        
        try:
            with filepath.open('r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    
                    try:
                        obj = json.loads(line)
                        # Validate required fields
                        required = ['chunk_id', 'batch_id', 'source_file', 'text', 
                                  'word_count', 'estimated_tokens', 'chunk_sha256']
                        missing = [f for f in required if f not in obj]
                        if missing:
                            invalid_lines.append(f"Line {line_num}: missing fields {missing}")
                        else:
                            valid_count += 1
                    except json.JSONDecodeError as e:
                        invalid_lines.append(f"Line {line_num}: {str(e)}")
        except Exception as e:
            self.errors.append(f"Failed to read {filepath}: {str(e)}")
            return 0, invalid_lines
        
        return valid_count, invalid_lines
    
    def check_chunk_id_uniqueness(self, jsonl_files: List[Path]) -> Dict[str, List[str]]:
        """Check that chunk IDs are unique across all files."""
        seen_ids = defaultdict(list)
        duplicates = {}
        
        for filepath in jsonl_files:
            try:
                with filepath.open('r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            chunk_id = obj.get('chunk_id')
                            if chunk_id:
                                seen_ids[chunk_id].append(f"{filepath.name}:{line_num}")
                        except json.JSONDecodeError:
                            pass
            except Exception as e:
                self.errors.append(f"Failed to read {filepath}: {str(e)}")
        
        # Find duplicates
        for chunk_id, locations in seen_ids.items():
            if len(locations) > 1:
                duplicates[chunk_id] = locations
        
        return duplicates
    
    def validate_batch_coverage(self, batch_dirs: List[Path], cleaned_dirs: List[Path]) -> Dict:
        """
        Validate that all cleaned files were processed.
        
        Returns: {
            'total_cleaned_files': int,
            'processed_files': int,
            'unprocessed_files': List[str],
        }
        """
        result = {
            'total_cleaned_files': 0,
            'processed_files': 0,
            'unprocessed_files': [],
        }
        
        processed_paths = set()
        for batch_dir in batch_dirs:
            for chunk_file in batch_dir.glob('*.jsonl'):
                try:
                    with chunk_file.open('r', encoding='utf-8') as f:
                        for line in f:
                            line = line.strip()
                            if not line:
                                continue
                            try:
                                obj = json.loads(line)
                                source = obj.get('relative_path', '')
                                if source:
                                    processed_paths.add(source)
                            except json.JSONDecodeError:
                                pass
                except Exception as e:
                    self.errors.append(f"Failed to read {chunk_file}: {str(e)}")
        
        # Count cleaned files
        for cleaned_dir in cleaned_dirs:
            for source_file in cleaned_dir.rglob('*'):
                if source_file.is_file():
                    result['total_cleaned_files'] += 1
                    rel_path = source_file.relative_to(cleaned_dir).as_posix()
                    if rel_path in processed_paths:
                        result['processed_files'] += 1
                    else:
                        result['unprocessed_files'].append(rel_path)
        
        return result
