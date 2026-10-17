"""CSV-aware chunker."""

import csv
from io import StringIO
from typing import List
from rag.chunking.chunker import BaseChunker
from rag.chunking.models import Chunk, count_words, calculate_token_estimate, calculate_sha256


class CSVChunker(BaseChunker):
    """Chunker for CSV files that preserves structure."""
    
    def chunk(self, text: str, source_path: str, batch_id: str, source_sha256: str,
              relative_path: str, filename: str, extension: str) -> List[Chunk]:
        """
        Chunk CSV while preserving header and row grouping.
        """
        chunks = []
        
        try:
            reader = csv.reader(StringIO(text))
            rows = list(reader)
        except Exception:
            # Fallback to text chunking if CSV parsing fails
            return self._fallback_text_chunk(text, batch_id, relative_path,
                                           filename, extension, source_sha256)
        
        if not rows:
            return []
        
        # Extract header
        header = rows[0] if rows else []
        data_rows = rows[1:] if len(rows) > 1 else []
        
        # Group rows to meet token targets
        row_groups = self._group_rows_to_target(header, data_rows)
        
        # Create chunks
        for idx, group_text in enumerate(row_groups):
            chunk = self.create_chunk(
                text=group_text,
                chunk_index=idx,
                total_chunks=len(row_groups),
                batch_id=batch_id,
                relative_path=relative_path,
                filename=filename,
                extension=extension,
                source_sha256=source_sha256,
                heading_context="CSV Data",
            )
            chunks.append(chunk)
        
        return chunks if chunks else self._fallback_text_chunk(text, batch_id, relative_path,
                                                               filename, extension, source_sha256)
    
    def _format_row_as_text(self, header: List[str], row: List[str]) -> str:
        """Format a single row as readable text."""
        if not header or not row:
            return ""
        
        lines = []
        for col, val in zip(header, row):
            lines.append(f"{col}: {val}")
        
        return "\n".join(lines)
    
    def _group_rows_to_target(self, header: List[str], rows: List[List[str]]) -> List[str]:
        """Group CSV rows to meet token targets."""
        if not rows:
            return []
        
        result = []
        current_group = []
        current_words = 0
        
        # Always include header in the word count context
        header_text = ", ".join(header)
        header_words = count_words(header_text)
        
        for row in rows:
            row_text = self._format_row_as_text(header, row)
            row_words = count_words(row_text)
            
            # Calculate tokens if we add this row
            total_words = header_words + current_words + row_words
            total_tokens = self.estimate_tokens_for_words(total_words)
            
            # If adding this row would exceed target + buffer
            if current_words > 0 and total_tokens > self.target_tokens * 1.2:
                # Finalize current group
                group_text = header_text + "\n\n" + "\n\n".join(current_group)
                result.append(group_text)
                current_group = [row_text]
                current_words = row_words
            else:
                current_group.append(row_text)
                current_words += row_words
        
        # Add final group
        if current_group:
            group_text = header_text + "\n\n" + "\n\n".join(current_group)
            result.append(group_text)
        
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
