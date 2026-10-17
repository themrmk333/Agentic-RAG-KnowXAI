"""Base chunker class and utilities."""

import re
from typing import List, Tuple
from pathlib import Path
from abc import ABC, abstractmethod
from rag.chunking.models import Chunk, ChunkMetadata, count_words, calculate_token_estimate, calculate_sha256


class BaseChunker(ABC):
    """Base class for all chunkers."""
    
    TARGET_TOKENS = 800
    OVERLAP_TOKENS = 110
    
    def __init__(self, target_tokens: int = TARGET_TOKENS, overlap_tokens: int = OVERLAP_TOKENS):
        self.target_tokens = target_tokens
        self.overlap_tokens = overlap_tokens
    
    @abstractmethod
    def chunk(self, text: str, source_path: str, batch_id: str, source_sha256: str, 
              relative_path: str, filename: str, extension: str) -> List[Chunk]:
        """
        Split text into chunks.
        
        Returns list of Chunk objects with complete metadata.
        """
        pass
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate tokens in text."""
        words = count_words(text)
        return calculate_token_estimate(words)
    
    def estimate_tokens_for_words(self, word_count: int) -> int:
        """Estimate tokens from word count."""
        return calculate_token_estimate(word_count)
    
    def split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences, preserving sentence boundaries."""
        # Simple sentence splitter: split on . ! ? followed by space or end
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def split_into_paragraphs(self, text: str) -> List[str]:
        """Split text into paragraphs."""
        # Paragraphs are separated by blank lines
        paragraphs = re.split(r'\n\n+', text)
        return [p.strip() for p in paragraphs if p.strip()]
    
    def split_into_lines(self, text: str) -> List[str]:
        """Split text into lines."""
        lines = text.split('\n')
        return [line for line in lines if line.strip()]
    
    def merge_chunks_to_target(self, text_pieces: List[str]) -> List[str]:
        """
        Merge text pieces until target token count is reached.
        
        Returns list of merged chunks respecting piece boundaries.
        """
        chunks = []
        current = []
        current_words = 0
        
        for piece in text_pieces:
            piece_words = count_words(piece)
            piece_tokens = self.estimate_tokens_for_words(piece_words)
            
            # If adding this piece would exceed target + some buffer (1.2x), start new chunk
            if current_words > 0 and self.estimate_tokens_for_words(current_words + piece_words) > self.target_tokens * 1.2:
                chunks.append('\n\n'.join(current))
                current = [piece]
                current_words = piece_words
            else:
                current.append(piece)
                current_words += piece_words
        
        if current:
            chunks.append('\n\n'.join(current))
        
        return chunks
    
    def create_chunk(self, text: str, chunk_index: int, total_chunks: int,
                     batch_id: str, relative_path: str, filename: str, extension: str,
                     source_sha256: str, heading_context: str = "") -> Chunk:
        """Create a Chunk object with metadata."""
        word_count = count_words(text)
        token_estimate = self.estimate_tokens_for_words(word_count)
        chunk_sha256 = calculate_sha256(text)
        
        # Deterministic chunk ID
        chunk_id = f"{batch_id}_{source_sha256[:8]}_chunk_{chunk_index:06d}"
        
        metadata = ChunkMetadata(
            chunk_id=chunk_id,
            batch_id=batch_id,
            source_file=str(relative_path),
            relative_path=str(relative_path),
            filename=filename,
            extension=extension,
            chunk_index=chunk_index,
            total_chunks_for_file=total_chunks,
            character_count=len(text),
            word_count=word_count,
            estimated_tokens=token_estimate,
            source_sha256=source_sha256,
            chunk_sha256=chunk_sha256,
            heading_context=heading_context,
            chunking_strategy=self.__class__.__name__,
        )
        
        return Chunk(metadata=metadata, text=text)
