# Project: Secure Computer Vision / Intelligent Automation Platform (PRJ-005)

```json
{
  "document_id": "PRJ-005",
  "title": "Secure Computer Vision / Intelligent Automation Platform",
  "document_type": "Project Documentation",
  "department": "Cross-Department",
  "category": "Active Project",
  "roles": [
    "All Employees"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Secure Computer Vision / Intelligent Automation Platform",
    "PRJ-005",
    "RND",
    "ENG",
    "SEC",
    "FIN"
  ],
  "created_date": "2026-01-20",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "In Progress - Pilot",
  "owner": "Riya Agarwal",
  "source": "synthetic-generated"
}
```

**Status:** In Progress - Pilot  |  **Start Date:** 2026-01-20  |  **Expected Completion:** 2026-12-01
**Project Manager:** Riya Agarwal  |  **Technical Lead:** Isha Bhatt
**Teams Involved:** R&D, Engineering, Security, Finance & Accounting

## Overview
A computer-vision platform automating document processing (invoices, ID verification, asset inspection photos) with strict security and data-handling controls.

## Business Objective
Automate manual document/image review workflows in Finance, Procurement, and IT Asset Management.

## Problem Statement
Manual review of invoices, vendor documents, and asset photos is slow and inconsistent across departments.

## Architecture Overview
Document/image inputs pass through an OCR and object-detection pipeline; extracted structured data is validated against business rules (e.g., three-way match for invoices) before being written to the relevant system (MK-Finance360, IT Asset Register); all processing occurs within an isolated, access-controlled environment given the sensitivity of the source documents.

## Technology Stack

- Python computer-vision pipeline
- OCR engine
- Object detection model
- MK-CloudOps isolated processing environment
- MK-Finance360 / MK-ProcureX integration connectors

## Components

- Document ingestion & OCR
- Object detection / classification model
- Business-rule validation engine
- Secure storage & redaction module
- System-of-record integration connectors

## Database
An isolated, encrypted document store separate from general-purpose systems, with strict retention limits.

## APIs

- `POST /v1/documents/process`
- `GET /v1/documents/{id}/extraction-result`
- `POST /v1/documents/{id}/redact`

## AI Models
An OCR model plus a fine-tuned object-detection/classification model for document type and field extraction.

## RAG Components
Not primary — this project focuses on vision/extraction rather than text retrieval, though extracted metadata is indexed for search.

## Agent Architecture
A pipeline architecture rather than a conversational agent: ingest -> extract -> validate -> route to system of record.

## Security Architecture
Processes only within an isolated MK-CloudOps environment with restricted access; documents containing personal data are automatically flagged for redaction before wider storage, per the Data Protection Policy.

## Development Workflow
Security-reviewed feature branches; any change touching the extraction pipeline requires a Security sign-off given data sensitivity.

## Testing Workflow
QA validates extraction accuracy against a labeled document set and runs a dedicated security regression pass before release.

## Deployment Workflow
Deployed to the isolated processing environment only; no direct external network access.

## CI/CD Workflow
MK-CI pipeline with mandatory Security gate before any production deployment.

## Known Issues

- Handwritten vendor invoices have lower OCR accuracy than typed/digital invoices.
- Object detection occasionally misclassifies damaged asset photos, requiring manual override.

## Risks

- Handling of sensitive personal or financial document images if isolation controls are misconfigured.
- Regulatory exposure if extracted data retention exceeds the approved schedule.

## Dependencies

- Security sign-off on the isolated processing environment
- Finance three-way match business rules

## Milestones

| Milestone | Target Date | Status |
|---|---|---|
| OCR pipeline v1 | 2026-03-20 | Done |
| Invoice extraction pilot with Finance | 2026-06-15 | Done |
| Asset inspection photo pilot with IT | 2026-09-01 | In Progress |
| Full production rollout | 2026-12-01 | Planned |

## Current Sprint
Sprint 10: Improving handwritten invoice OCR accuracy.

## Backlog (Upcoming)

- Add ID-verification workflow for vendor onboarding
- Add multi-language OCR support

## Future Roadmap
Extend to automated contract clause extraction in partnership with Legal & Compliance.

## Project Terminology

| Term | Definition |
|---|---|
| OCR | Optical Character Recognition — extracting text from scanned images. |
| Redaction | Removing or masking sensitive information from a document before wider storage. |
| Three-way Match | Validating invoice, purchase order, and goods receipt agree before payment. |

---
_This project documentation is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._