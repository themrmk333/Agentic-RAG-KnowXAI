"""Chunk data models and structures."""

from dataclasses import dataclass, field, asdict
from typing import Optional, List
import hashlib
import json
from datetime import datetime, timezone


@dataclass
class ChunkMetadata:
    """Metadata for a single chunk."""
    chunk_id: str
    batch_id: str
    source_file: str
    relative_path: str
    filename: str
    extension: str
    chunk_index: int
    total_chunks_for_file: int
    character_count: int
    word_count: int
    estimated_tokens: int
    source_sha256: str
    chunk_sha256: str
    
    # --- New Enterprise Metadata Fields ---
    document_id: Optional[str] = None
    department: Optional[str] = None
    department_code: Optional[str] = None
    category: Optional[str] = None
    title: Optional[str] = None
    document_type: Optional[str] = None
    access_level: Optional[str] = None
    roles: Optional[List[str]] = field(default_factory=list)
    version: Optional[str] = None
    effective_date: Optional[str] = None
    source_identifier: Optional[str] = None
    # ----------------------------------------
    
    heading_context: str = ""
    chunking_strategy: str = "structure-aware"
    created_at_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    
    def to_dict(self):
        return asdict(self)


@dataclass
class Chunk:
    """Complete chunk with text and metadata."""
    metadata: ChunkMetadata
    text: str
    
    def to_jsonl_line(self) -> str:
        """Serialize chunk to JSONL line."""
        obj = {
            **self.metadata.to_dict(),
            "text": self.text
        }
        return json.dumps(obj, ensure_ascii=False)
    
    @staticmethod
    def from_jsonl_line(line: str) -> 'Chunk':
        """Deserialize chunk from JSONL line."""
        obj = json.loads(line)
        text = obj.pop("text")
        meta = ChunkMetadata(**obj)
        return Chunk(metadata=meta, text=text)


def calculate_token_estimate(word_count: int) -> int:
    """Estimate tokens from word count. Using 1 word ≈ 1.3 tokens."""
    return max(1, round(word_count * 1.3))


def count_words(text: str) -> int:
    """Count words in text using simple regex."""
    import re
    return len(re.findall(r'\b\w+\b', text, flags=re.UNICODE))


def calculate_sha256(text: str) -> str:
    """Calculate SHA-256 hash of text."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def normalize_department(dept: str) -> str:
    """Canonical normalization for department codes."""
    if not dept:
        return "UNKNOWN"
    d = dept.strip().upper()
    
    # HR
    if d in ["HR", "HUMAN RESOURCES", "HUMAN RESOURCE"]:
        return "HR"
    
    # IT
    if d in ["IT", "IT SUPPORT", "INFORMATION TECHNOLOGY", "INFO TECH", "TECH"]:
        return "IT"
    
    # FINANCE
    if d in ["FIN", "FINANCE", "FINANCE & ACCOUNTING", "ACCOUNTING"]:
        return "FINANCE"
        
    # SALES
    if d in ["SALES", "SALES DEPT", "SALES DEPARTMENT"]:
        return "SALES"
        
    # LEGAL
    if d in ["LEGAL", "LEGAL & COMPLIANCE"]:
        return "LEGAL"
        
    # PROJECT / PMO
    if d in ["PROJECT", "PMO", "PROJECT MANAGEMENT"]:
        return "PROJECT"
        
    # DEVOPS
    if d in ["DEVOPS", "DEVOPS & CLOUD", "CLOUD"]:
        return "DEVOPS"
        
    # Others
    if d in ["MKT", "MARKETING"]:
        return "MARKETING"
        
    if d in ["ENG", "ENGINEERING"]:
        return "ENGINEERING"

    if d in ["PROD", "PRODUCT"]:
        return "PRODUCT"

    if d in ["SEC", "SECURITY"]:
        return "SECURITY"
        
    if d in ["PROC", "PROCUREMENT"]:
        return "PROCUREMENT"
        
    if d in ["MGMT", "MANAGEMENT", "EXEC", "EXECUTIVE"]:
        return "MANAGEMENT"
        
    return d

def extract_metadata_from_text(text: str) -> dict:
    """Extract metadata from markdown headers or JSON blocks."""
    import re
    meta = {}
    
    # Look for Document ID (e.g. SOP-SALES-010 or FAQ-SALES-010)
    doc_match = re.search(r'\b(SOP|FAQ|POL|FORM|TICKET)-[A-Z]+-\d+\b', text)
    if doc_match:
        meta['document_id'] = doc_match.group(0)
        
    # Look for explicit metadata lines
    cat_match = re.search(r'\*\*Category:\*\*\s*([^|*\n]+)', text, re.IGNORECASE)
    if cat_match:
        meta['category'] = cat_match.group(1).strip()
        
    access_match = re.search(r'\*\*Access Level:\*\*\s*([^|*\n]+)', text, re.IGNORECASE)
    if access_match:
        meta['access_level'] = access_match.group(1).strip().lower()
        
    roles_match = re.search(r'\*\*Roles?:\*\*\s*([^|*\n]+)', text, re.IGNORECASE)
    if roles_match:
        roles_str = roles_match.group(1).strip()
        meta['roles'] = [r.strip() for r in roles_str.split(',')]
        
    # Extract department from document ID if possible (e.g., SOP-SALES-010 -> SALES)
    if 'document_id' in meta:
        parts = meta['document_id'].split('-')
        if len(parts) >= 2:
            dept = parts[1]
            meta['department'] = dept
            meta['department_code'] = normalize_department(dept)
    
    return meta

