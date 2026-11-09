"""PDF Knowledge Base Loader and Semantic Chunker for MK-Infinite-AI Demo Knowledge Base.

Extracts text from the 16 PDF documents, preserving:
- Document titles from manifest and headers
- Category (Company Overview, Department, Project)
- Canonical department names and codes
- Project codes and sponsors
- Page numbers per chunk
- Exact section heading contexts
- Complete Q&A pairs (keeping all 10 numbered steps intact in a single chunk)
- Access-control metadata (access_level, confidentiality, allowed_departments)
"""

from __future__ import annotations

import csv
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pypdf

from rag.chunking.models import calculate_sha256, calculate_token_estimate, count_words

logger = logging.getLogger(__name__)

# Canonical mapping for all 16 knowledge base documents
DOCUMENT_METADATA_REGISTRY: Dict[str, Dict[str, Any]] = {
    "00_MK_Infinite_AI_Company_Overview.pdf": {
        "department_code": "ALL",
        "department": "Company-wide",
        "category": "Company Overview",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "01_HR_Department.pdf": {
        "department_code": "HR",
        "department": "Human Resources",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "02_IT_Department.pdf": {
        "department_code": "IT",
        "department": "Information Technology",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "03_Finance_Department.pdf": {
        "department_code": "FINANCE",
        "department": "Finance",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "04_Project_Management_Department.pdf": {
        "department_code": "PROJECT",
        "department": "Project Management Office",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "05_Sales_Department.pdf": {
        "department_code": "SALES",
        "department": "Sales",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "06_Marketing_Department.pdf": {
        "department_code": "MARKETING",
        "department": "Marketing",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "07_Customer_Support_Department.pdf": {
        "department_code": "SUPPORT",
        "department": "Customer Support",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "08_Research_Development_Department.pdf": {
        "department_code": "RND",
        "department": "Research & Development",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "09_Operations_Department.pdf": {
        "department_code": "OPERATIONS",
        "department": "Operations",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "10_Admin_Facilities_Department.pdf": {
        "department_code": "ADMIN",
        "department": "Admin & Facilities",
        "category": "Department",
        "project_code": None,
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "11_Project_01_Agentic_RAG_KnowXAI.pdf": {
        "department_code": "PROJECT",
        "department": "Project Management Office",
        "category": "Project",
        "project_code": "PRJ-2026-001",
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "12_Project_02_AI_Customer_Support_Assistant.pdf": {
        "department_code": "PROJECT",
        "department": "Project Management Office",
        "category": "Project",
        "project_code": "PRJ-2026-002",
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "13_Project_03_Intelligent_HR_Management_System.pdf": {
        "department_code": "PROJECT",
        "department": "Project Management Office",
        "category": "Project",
        "project_code": "PRJ-2026-003",
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "14_Project_04_Smart_Expense_Management_System.pdf": {
        "department_code": "PROJECT",
        "department": "Project Management Office",
        "category": "Project",
        "project_code": "PRJ-2026-004",
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
    "15_Project_05_Predictive_Business_Analytics.pdf": {
        "department_code": "PROJECT",
        "department": "Project Management Office",
        "category": "Project",
        "project_code": "PRJ-2026-005",
        "access_level": "employee",
        "confidentiality": "internal",
        "allowed_departments": ["*"],
    },
}


@dataclass
class ParsedPDFChunk:
    chunk_id: str
    chunk_index: int
    total_chunks_for_file: int
    content: str
    metadata: Dict[str, Any]


@dataclass
class ParsedPDFDocument:
    filename: str
    relative_path: str
    title: str
    category: str
    department_code: str
    department: str
    project_code: Optional[str]
    total_pages: int
    metadata: Dict[str, Any]
    chunks: List[ParsedPDFChunk] = field(default_factory=list)


class PDFKnowledgeLoader:
    """Extracts, cleans, and chunks enterprise PDF knowledge base documents."""

    def __init__(self, knowledge_base_dir: Path | str) -> None:
        self.base_dir = Path(knowledge_base_dir)
        self.manifest_file = self.base_dir / "MANIFEST.csv"
        self.manifest_info: Dict[str, Dict[str, str]] = {}
        if self.manifest_file.exists():
            with open(self.manifest_file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.manifest_info[row["Filename"]] = row

    @staticmethod
    def _clean_headers_from_pages(reader: pypdf.PdfReader) -> List[Tuple[int, str]]:
        pages_text: List[Tuple[int, str]] = []
        for idx, page in enumerate(reader.pages):
            raw = page.extract_text() or ""
            lines = raw.split("\n")
            page_num = idx + 1
            body_lines = []
            for l in lines:
                line_str = l.strip()
                if line_str == "MK-INFINITE-AI PRIVATE LIMITED":
                    continue
                if "DEMO / FICTIONAL" in line_str:
                    continue
                m = re.match(r"^Page\s+(\d+)$", line_str, re.IGNORECASE)
                if m:
                    page_num = int(m.group(1))
                    continue
                body_lines.append(l)
            pages_text.append((page_num, "\n".join(body_lines).strip()))
        return pages_text

    @staticmethod
    def _get_toc_headings(page2_text: str) -> List[str]:
        lines = page2_text.split("\n")
        headings = []
        for l in lines:
            line = l.strip()
            m = re.match(r"^(\d+\.\s+[A-Za-z\s&,()/-]+?)(?:\s*\.{2,}|\s*$)", line)
            if m:
                headings.append(m.group(1).strip())
        return headings

    def parse_document(self, pdf_path: Path) -> ParsedPDFDocument:
        reader = pypdf.PdfReader(str(pdf_path))
        manifest_row = self.manifest_info.get(pdf_path.name, {})
        doc_reg = DOCUMENT_METADATA_REGISTRY.get(pdf_path.name, {})

        title = manifest_row.get("Title") or pdf_path.stem.replace("_", " ")
        category = doc_reg.get("category", manifest_row.get("Document category", "Department"))
        dept_code = doc_reg.get("department_code", "GENERAL")
        dept_name = doc_reg.get("department", "General")
        prj_code = doc_reg.get("project_code")

        pages = self._clean_headers_from_pages(reader)
        cover_page_num, cover_text = pages[0]
        toc_page_num, toc_text = pages[1]
        toc_headings = self._get_toc_headings(toc_text)

        # Annotated body text from page 3 onwards
        content_parts = []
        for p_num, p_text in pages[2:]:
            content_parts.append(f"\n[PAGE_{p_num}]\n" + p_text)
        full_content = "\n".join(content_parts)

        # 1. Document Overview / Metadata chunk
        cover_clean = re.sub(r"DEMO CONTENT - FICTIONAL DATA.*", "", cover_text, flags=re.DOTALL).strip()
        raw_chunks = [{
            "text": f"# {title}\n\n{cover_clean}",
            "heading_context": "Document Overview & Metadata",
            "page_start": 1,
            "page_end": 2,
            "is_qa": False,
            "section_name": "Overview",
        }]

        # 2. Separate into Narrative and Q&A
        qa_heading = None
        for h in toc_headings:
            if any(k in h.lower() for k in ["questions and answers", "faqs", "frequently asked"]):
                qa_heading = h
                break

        if qa_heading:
            qa_pos = full_content.find(qa_heading)
            if qa_pos != -1:
                narrative_text = full_content[:qa_pos]
                qa_text = full_content[qa_pos:]
            else:
                m = re.search(r"(?:Department Questions and Answers|Project Questions and Answers|Frequently Asked Questions|General Employee FAQs)", full_content, re.IGNORECASE)
                if m:
                    narrative_text = full_content[:m.start()]
                    qa_text = full_content[m.start():]
                else:
                    narrative_text = full_content
                    qa_text = ""
        else:
            narrative_text = full_content
            qa_text = ""

        # 3. Narrative sections by exact TOC headings
        narrative_headings = [h for h in toc_headings if h != qa_heading and "demo assumptions" not in h.lower()]
        if narrative_headings:
            escaped_headings = [re.escape(h) for h in narrative_headings]
            split_pattern = r"(?=\n(?:" + "|".join(escaped_headings) + r"))"
            raw_sections = re.split(split_pattern, narrative_text)

            for sec in raw_sections:
                sec = sec.strip()
                if not sec:
                    continue
                p_matches = re.findall(r"\[PAGE_(\d+)\]", sec)
                p_start = int(p_matches[0]) if p_matches else 3
                p_end = int(p_matches[-1]) if p_matches else p_start
                clean_sec = re.sub(r"\[PAGE_\d+\]\n*", "", sec).strip()
                if len(clean_sec) < 30:
                    continue
                lines = clean_sec.split("\n")
                first_line = lines[0].strip()

                raw_chunks.append({
                    "text": clean_sec,
                    "heading_context": first_line,
                    "page_start": p_start,
                    "page_end": p_end,
                    "is_qa": False,
                    "section_name": first_line,
                })

        # 4. Q&A items (keeping full 10 steps intact per question)
        if qa_text:
            trailing_heading = "15. Demo Assumptions Register"
            if trailing_heading in qa_text:
                t_pos = qa_text.find(trailing_heading)
                actual_qa_text = qa_text[:t_pos]
                trailing_text = qa_text[t_pos:]
            else:
                actual_qa_text = qa_text
                trailing_text = ""

            qa_items = re.split(r"(?=(?:Question|FAQ)\s+\d+\s*:)", actual_qa_text)
            for item in qa_items:
                item = item.strip()
                if not item:
                    continue
                p_matches = re.findall(r"\[PAGE_(\d+)\]", item)
                p_start = int(p_matches[0]) if p_matches else 3
                p_end = int(p_matches[-1]) if p_matches else p_start
                clean_item = re.sub(r"\[PAGE_\d+\]\n*", "", item).strip()
                if len(clean_item) < 30:
                    continue
                first_line = clean_item.split("\n")[0].strip()
                is_qa = bool(re.match(r"^(?:Question|FAQ)\s+\d+", first_line, re.IGNORECASE))
                if not is_qa:
                    continue
                raw_chunks.append({
                    "text": clean_item,
                    "heading_context": first_line,
                    "page_start": p_start,
                    "page_end": p_end,
                    "is_qa": True,
                    "section_name": first_line,
                })

            if trailing_text:
                p_matches = re.findall(r"\[PAGE_(\d+)\]", trailing_text)
                p_start = int(p_matches[0]) if p_matches else 3
                p_end = int(p_matches[-1]) if p_matches else p_start
                clean_trailing = re.sub(r"\[PAGE_\d+\]\n*", "", trailing_text).strip()
                if len(clean_trailing) > 30:
                    raw_chunks.append({
                        "text": clean_trailing,
                        "heading_context": clean_trailing.split("\n")[0].strip(),
                        "page_start": p_start,
                        "page_end": p_end,
                        "is_qa": False,
                        "section_name": "Demo Assumptions Register",
                    })

        # Filter out any tiny residual noise (< 30 tokens)
        valid_chunks = []
        for rc in raw_chunks:
            wc = count_words(rc["text"])
            tok = calculate_token_estimate(wc)
            if tok >= 30:
                valid_chunks.append(rc)

        # Assemble finalized ParsedPDFChunk objects with complete metadata
        total_chunks = len(valid_chunks)
        final_chunks: List[ParsedPDFChunk] = []
        file_slug = pdf_path.stem.lower()

        for c_idx, rc in enumerate(valid_chunks):
            chunk_text = rc["text"]
            wc = count_words(chunk_text)
            tok = calculate_token_estimate(wc)
            c_sha = calculate_sha256(chunk_text)
            chunk_id = f"{file_slug}_chunk_{c_idx:06d}"

            meta: Dict[str, Any] = {
                "chunk_id": chunk_id,
                "batch_id": "new_knowledge_base",
                "source_file": pdf_path.name,
                "relative_path": f"new_knowledge_base/MK_Infinite_AI_Demo_Knowledge_Base/{pdf_path.name}",
                "filename": pdf_path.name,
                "title": title,
                "category": category,
                "department": dept_name,
                "department_code": dept_code,
                "project_code": prj_code,
                "page_start": rc["page_start"],
                "page_end": rc["page_end"],
                "pages": list(range(rc["page_start"], rc["page_end"] + 1)),
                "heading_context": rc["heading_context"],
                "section_name": rc["section_name"],
                "is_qa": rc["is_qa"],
                "chunk_index": c_idx,
                "total_chunks_for_file": total_chunks,
                "character_count": len(chunk_text),
                "word_count": wc,
                "estimated_tokens": tok,
                "chunk_sha256": c_sha,
                "access_level": doc_reg.get("access_level", "employee"),
                "confidentiality": doc_reg.get("confidentiality", "internal"),
                "allowed_departments": doc_reg.get("allowed_departments", ["*"]),
                "roles": ["employee", "manager", "admin", "lead", "super_admin"],
                "chunking_strategy": "PDFKnowledgeChunker",
            }

            final_chunks.append(
                ParsedPDFChunk(
                    chunk_id=chunk_id,
                    chunk_index=c_idx,
                    total_chunks_for_file=total_chunks,
                    content=chunk_text,
                    metadata=meta,
                )
            )

        doc_metadata = {
            "title": title,
            "filename": pdf_path.name,
            "category": category,
            "department": dept_name,
            "department_code": dept_code,
            "project_code": prj_code,
            "total_pages": len(reader.pages),
            "total_chunks": total_chunks,
            "access_level": doc_reg.get("access_level", "employee"),
            "confidentiality": doc_reg.get("confidentiality", "internal"),
            "allowed_departments": doc_reg.get("allowed_departments", ["*"]),
        }

        return ParsedPDFDocument(
            filename=pdf_path.name,
            relative_path=f"new_knowledge_base/MK_Infinite_AI_Demo_Knowledge_Base/{pdf_path.name}",
            title=title,
            category=category,
            department_code=dept_code,
            department=dept_name,
            project_code=prj_code,
            total_pages=len(reader.pages),
            metadata=doc_metadata,
            chunks=final_chunks,
        )

    def load_all(self) -> List[ParsedPDFDocument]:
        """Load and chunk all 16 PDFs in the knowledge base directory."""
        pdf_files = sorted(self.base_dir.glob("*.pdf"))
        if not pdf_files:
            raise FileNotFoundError(f"No PDF files found in {self.base_dir}")

        documents: List[ParsedPDFDocument] = []
        for pdf_path in pdf_files:
            logger.info("Parsing and chunking %s...", pdf_path.name)
            doc = self.parse_document(pdf_path)
            documents.append(doc)

        return documents
