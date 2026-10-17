"""Generic text chunker and legacy character-based chunking."""

from __future__ import annotations
from typing import List
from rag.chunking.chunker import BaseChunker
from rag.chunking.models import Chunk, count_words, calculate_token_estimate, calculate_sha256


def chunk_text(text: str, *, chunk_size: int = 1200, overlap: int = 200) -> list[str]:
    """Legacy character-based chunking function."""
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("chunk_size must be positive and overlap must be smaller than chunk_size")
    normalized = " ".join(text.split())
    if not normalized:
        return []
    chunks = []
    start = 0
    while start < len(normalized):
        end = min(start + chunk_size, len(normalized))
        if end < len(normalized):
            boundary = normalized.rfind(" ", start, end)
            if boundary > start + overlap:
                end = boundary
        chunks.append(normalized[start:end].strip())
        if end >= len(normalized):
            break
        start = end - overlap
    return chunks


class TextChunker(BaseChunker):
    """Generic chunker for plain text, HTML, XML, YAML, LOG, etc."""
    
    def chunk(self, text: str, source_path: str, batch_id: str, source_sha256: str,
              relative_path: str, filename: str, extension: str) -> List[Chunk]:
        """
        Chunk generic text using paragraph and sentence boundaries.
        """
        from rag.chunking.models import extract_metadata_from_text
        
        chunks = []
        
        # Try paragraph boundaries first
        paragraphs = self.split_into_paragraphs(text)
        
        # Merge paragraphs to meet token targets
        merged = self.merge_chunks_to_target(paragraphs)
        
        # Create chunks
        for idx, chunk_text in enumerate(merged):
            extracted_meta = extract_metadata_from_text(chunk_text)
            
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
            
            if extracted_meta:
                for k, v in extracted_meta.items():
                    if hasattr(chunk.metadata, k):
                        setattr(chunk.metadata, k, v)
                        
            chunks.append(chunk)
        
        return chunks if chunks else self._single_chunk(text, batch_id, relative_path,
                                                         filename, extension, source_sha256)
    
    def _single_chunk(self, text: str, batch_id: str, relative_path: str,
                     filename: str, extension: str, source_sha256: str) -> List[Chunk]:
        """Create a single chunk for very small files."""
        from rag.chunking.models import extract_metadata_from_text
        extracted_meta = extract_metadata_from_text(text)
        
        chunk = self.create_chunk(
            text=text,
            chunk_index=0,
            total_chunks=1,
            batch_id=batch_id,
            relative_path=relative_path,
            filename=filename,
            extension=extension,
            source_sha256=source_sha256,
            heading_context="",
        )
        
        if extracted_meta:
            for k, v in extracted_meta.items():
                if hasattr(chunk.metadata, k):
                    setattr(chunk.metadata, k, v)
                    
        return [chunk]
