"""JSON-aware chunker."""

import json
from typing import List, Any, Dict
from rag.chunking.chunker import BaseChunker
from rag.chunking.models import Chunk, count_words, calculate_token_estimate, calculate_sha256


class JSONChunker(BaseChunker):
    """Chunker for JSON files that preserves structure."""
    
    def chunk(self, text: str, source_path: str, batch_id: str, source_sha256: str,
              relative_path: str, filename: str, extension: str) -> List[Chunk]:
        """
        Chunk JSON while preserving structure.
        """
        chunks = []
        
        try:
            data = json.loads(text)
            sections = self._flatten_json(data)
        except json.JSONDecodeError:
            # If JSON is invalid, fall back to text chunking
            return self._fallback_text_chunk(text, batch_id, relative_path, 
                                            filename, extension, source_sha256)
        
        # Merge sections to meet token targets
        merged = self._merge_sections_to_target(sections)
        
        # Create chunks
        for idx, section_text in enumerate(merged):
            chunk = self.create_chunk(
                text=section_text,
                chunk_index=idx,
                total_chunks=len(merged),
                batch_id=batch_id,
                relative_path=relative_path,
                filename=filename,
                extension=extension,
                source_sha256=source_sha256,
                heading_context="",
            )
            chunks.append(chunk)
        
        return chunks if chunks else self._fallback_text_chunk(text, batch_id, relative_path,
                                                                filename, extension, source_sha256)
    
    def _flatten_json(self, obj: Any, prefix: str = "") -> List[str]:
        """Convert JSON structure into readable text chunks."""
        sections = []
        
        if isinstance(obj, dict):
            for key, value in obj.items():
                current_prefix = f"{prefix}/{key}" if prefix else key
                if isinstance(value, (dict, list)):
                    # Recurse into nested structures
                    sections.extend(self._flatten_json(value, current_prefix))
                else:
                    # Leaf node: format as "Key: Value"
                    text = f"{key}: {value}"
                    sections.append(text)
        
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                current_prefix = f"{prefix}[{idx}]"
                if isinstance(item, (dict, list)):
                    sections.extend(self._flatten_json(item, current_prefix))
                else:
                    sections.append(f"{current_prefix}: {item}")
        
        else:
            # Scalar value
            sections.append(f"{prefix}: {obj}")
        
        return sections
    
    def _merge_sections_to_target(self, sections: List[str]) -> List[str]:
        """Merge sections to meet token targets."""
        if not sections:
            return []
        
        result = []
        current = []
        current_words = 0
        
        for section in sections:
            section_words = count_words(section)
            section_tokens = self.estimate_tokens_for_words(section_words)
            
            # If adding section would exceed target + buffer
            if current_words > 0 and self.estimate_tokens_for_words(current_words + section_words) > self.target_tokens * 1.2:
                result.append('\n'.join(current))
                current = [section]
                current_words = section_words
            else:
                current.append(section)
                current_words += section_words
        
        if current:
            result.append('\n'.join(current))
        
        return result
    
    def _fallback_text_chunk(self, text: str, batch_id: str, relative_path: str,
                            filename: str, extension: str, source_sha256: str) -> List[Chunk]:
        """Fallback to text chunking."""
        paragraphs = self.split_into_paragraphs(text)
        merged = self.merge_chunks_to_target(paragraphs)
        
        chunks = []
        for idx, chunk_text in enumerate(merged):
            chunk = self.create_chunk(
                text=chunk_text,
                chunk_index=idx,
                total_chunks=len(merged),
                batch_id=batch_id,
                relative_path=relative_path,
                filename=filename,
                extension=extension,
                source_sha256=source_sha256,
                heading_context="",
            )
            chunks.append(chunk)
        
        return chunks
