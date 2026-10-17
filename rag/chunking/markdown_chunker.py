"""Markdown-aware chunker."""

import re
from typing import List, Tuple
from rag.chunking.chunker import BaseChunker
from rag.chunking.models import Chunk, count_words, calculate_token_estimate, calculate_sha256, extract_metadata_from_text


class MarkdownChunker(BaseChunker):
    """Chunker for Markdown files that preserves heading hierarchy."""
    
    def chunk(self, text: str, source_path: str, batch_id: str, source_sha256: str,
              relative_path: str, filename: str, extension: str) -> List[Chunk]:
        """
        Chunk Markdown while preserving heading hierarchy and structure.
        """
        chunks = []
        
        # Split by heading levels to maintain hierarchy
        sections = self._split_by_headings(text)
        
        # Process each section, potentially splitting large ones
        processed_sections = []
        for heading_context, section_text in sections:
            subsections = self._process_section(section_text, heading_context)
            processed_sections.extend(subsections)
        
        # Merge sections to meet token targets
        merged = self._merge_sections_to_target(processed_sections)
        
        # Create chunks with metadata - CRITICAL: calculate metadata from FINAL text only
        for idx, (text_chunk, heading_ctx) in enumerate(merged):
            # Ensure text is the absolute final version - no post-processing
            final_text = text_chunk  # This is the stripped, finalized text from _merge_sections_to_target
            
            # Extract metadata from this specific chunk
            extracted_meta = extract_metadata_from_text(final_text)
            
            # Create chunk with metadata calculated from exact final text
            chunk = self.create_chunk(
                text=final_text,
                chunk_index=idx,
                total_chunks=len(merged),
                batch_id=batch_id,
                relative_path=relative_path,
                filename=filename,
                extension=extension,
                source_sha256=source_sha256,
                heading_context=heading_ctx,
            )
            
            # Assign extracted metadata to the chunk's metadata
            if extracted_meta:
                for k, v in extracted_meta.items():
                    if hasattr(chunk.metadata, k):
                        setattr(chunk.metadata, k, v)
                        
            chunks.append(chunk)
        
        return chunks if chunks else self._fallback_chunk(text, batch_id, relative_path, 
                                                           filename, extension, source_sha256)
    
    def _split_by_headings(self, text: str) -> List[Tuple[str, str]]:
        """Split text by heading level, preserving hierarchy and hard boundaries."""
        sections = []
        # Pattern: lines starting with # (1 or more) OR exactly --- for hard boundaries
        parts = re.split(r'^(#{1,6}\s+.*?|---+)$', text, flags=re.MULTILINE)
        
        i = 0
        current_heading = ""
        current_content = ""
        heading_stack = []
        
        while i < len(parts):
            part = parts[i]
            if part.startswith('#'):
                # This is a heading
                if current_content.strip() or current_heading:
                    sections.append((current_heading, current_content))
                current_heading = part
                heading_stack = [part]
                current_content = ""
            elif part.startswith('---'):
                # Hard boundary
                if current_content.strip() or current_heading:
                    sections.append((current_heading, current_content))
                current_heading = "HARD_BOUNDARY"
                current_content = ""
            else:
                # This is content
                current_content += part
            i += 1
        
        if current_heading or current_content.strip():
            sections.append((current_heading, current_content))
        
        return sections
    
    def _process_section(self, section_text: str, heading_context: str) -> List[Tuple[str, str]]:
        """Process a section, splitting if too large."""
        tokens = self.estimate_tokens(section_text)
        
        # If small enough, return as is
        if tokens <= self.target_tokens * 1.5:
            return [(section_text, heading_context)]
        
        # Split by paragraph boundaries
        paragraphs = self.split_into_paragraphs(section_text)
        merged = self.merge_chunks_to_target(paragraphs)
        
        return [(chunk, heading_context) for chunk in merged]
    
    def _merge_sections_to_target(self, sections: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """Merge sections to meet token targets while preserving heading context. Never merge across hard boundaries."""
        result = []
        current_text = ""
        current_heading = ""
        current_words = 0
        
        for section_text, heading in sections:
            # If the heading indicates a hard boundary or a distinct record (like an FAQ), we must start a new chunk
            is_hard_boundary = heading == "HARD_BOUNDARY"
            is_independent_record = heading.startswith("## FAQ") or heading.startswith("## SOP") or heading.startswith("## POL")
            
            if is_hard_boundary or is_independent_record:
                if current_text.strip():
                    result.append((current_text.strip(), current_heading))
                current_text = section_text if not is_hard_boundary else ""
                current_heading = heading if not is_hard_boundary else ""
                current_words = count_words(current_text)
                continue
                
            section_words = count_words(section_text)
            
            # If adding section would exceed target + buffer
            if current_words > 0 and self.estimate_tokens_for_words(current_words + section_words) > self.target_tokens * 1.2:
                result.append((current_text.strip(), current_heading))
                current_text = section_text
                current_heading = heading
                current_words = section_words
            else:
                if current_text:
                    current_text += "\n\n" + section_text
                else:
                    current_text = section_text
                if heading:
                    current_heading = heading
                current_words += section_words
        
        if current_text.strip():
            result.append((current_text.strip(), current_heading))
        
        return result if result else [(sections[0][0] if sections else "", "")]
    
    def _fallback_chunk(self, text: str, batch_id: str, relative_path: str,
                        filename: str, extension: str, source_sha256: str) -> List[Chunk]:
        """Fallback chunking if no sections found."""
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
