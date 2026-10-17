# Project: Agentic RAG Enterprise Knowledge Assistant (PRJ-001)

```json
{
  "document_id": "PRJ-001",
  "title": "Agentic RAG Enterprise Knowledge Assistant",
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
    "Agentic RAG Enterprise Knowledge Assistant",
    "PRJ-001",
    "ENG",
    "DATA",
    "RND",
    "SEC",
    "PMO"
  ],
  "created_date": "2026-02-10",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "In Progress - Beta",
  "owner": "Riya Agarwal",
  "source": "synthetic-generated"
}
```

**Status:** In Progress - Beta  |  **Start Date:** 2026-02-10  |  **Expected Completion:** 2026-11-30  
**Project Manager:** Riya Agarwal  |  **Technical Lead:** Neel Kapoor  
**Teams Involved:** Engineering, Data & Analytics, R&D, Security, PMO

## Overview
An internal AI assistant (Agentic-RAG-KnowXAI) that lets any MK-Infinite-AI employee ask natural-language questions and receive grounded answers retrieved from the company's internal knowledge base, regardless of which department owns the underlying document.

## Business Objective
Reduce time employees spend searching for internal policies, SOPs, and FAQs, and reduce repetitive tickets to IT/HR/Finance helpdesks.

## Problem Statement
Employees currently search across MK-ServiceDesk, MK-HRMS, MK-Finance360, and shared drives separately, with no single place to ask a cross-department question and get a grounded, cited answer.

## Architecture Overview
A retrieval-augmented generation pipeline: documents are chunked and embedded into a PostgreSQL + pgvector store; an intent-detection layer classifies the employee's question; specialist retrieval agents (HR agent, Finance agent, IT agent, etc.) query only the relevant document partitions; an authorization layer filters results by the employee's role/department against each document's access_level metadata before generation; a grounded-answer generator produces the final response with citations.

## Technology Stack

- PostgreSQL + pgvector
- Python (FastAPI) backend
- React frontend
- MK-Auth SSO integration
- MK-CloudOps for hosting
- Embedding model served via internal inference cluster

## Components

- Document ingestion pipeline
- Chunking & embedding service
- Intent detection classifier
- Specialist retrieval agents (per department)
- Authorization/access-control filter
- Grounded answer generator with citation formatting
- Feedback capture loop

## Database
PostgreSQL 16 with the pgvector extension for similarity search; row-level metadata for access_level, department, and confidentiality.

## APIs

- `POST /v1/query — submit a natural-language question`
- `GET /v1/documents/{id} — fetch a cited source document`
- `POST /v1/feedback — submit a thumbs up/down on an answer`

## AI Models
An internal instruction-tuned language model for answer generation, paired with a sentence-embedding model for retrieval.

## RAG Components
Yes — this is the flagship RAG project. Retrieval uses hybrid semantic + keyword search with department-partitioned indices.

## Agent Architecture
A router agent classifies intent and dispatches to specialist agents (HR, Finance, IT, Security, PMO, etc.); a synthesis agent merges results from multiple specialist agents for cross-department questions.

## Security Architecture
All retrieval requests are filtered through the authorization layer using the employee's role and department before any document content is passed to the generation model; audit logs capture every query and every document accessed.

## Development Workflow
Feature branches off `main` in MK-CodeForge, PR review required, merged after QA sign-off on the staging environment.

## Testing Workflow
QA runs a retrieval-accuracy regression suite (grounded-answer precision/recall against a labeled question set) before every release.

## Deployment Workflow
Deployed via MK-CI to a staging environment, validated by QA, then promoted to production via the standard Environment Promotion SOP.

## CI/CD Workflow
MK-CI pipeline: lint -> unit test -> retrieval-accuracy eval -> build container -> deploy to staging -> manual promotion to production.

## Known Issues

- Cross-department questions occasionally retrieve from only one specialist agent instead of merging both.
- Answer citations for very long SOPs sometimes reference the wrong step number.

## Risks

- Retrieval accuracy degrading as the knowledge base grows without periodic re-indexing.
- Authorization bugs could expose restricted documents if role mapping is misconfigured.

## Dependencies

- MK-Auth SSO for identity
- Underlying document sets from every department (this dataset)

## Milestones

| Milestone | Target Date | Status |
|---|---|---|
| Ingestion pipeline live | 2026-03-15 | Done |
| Intent detection v1 | 2026-04-30 | Done |
| Specialist agents for all 18 departments | 2026-07-15 | In Progress |
| Company-wide beta launch | 2026-09-01 | Planned |
| GA release | 2026-11-30 | Planned |

## Current Sprint
Sprint 14: Improving cross-department answer synthesis and citation accuracy.

## Backlog (Upcoming)

- Add voice input support
- Add multi-turn conversation memory
- Expand specialist agents to cover Legal & Compliance edge cases

## Future Roadmap
Post-GA: proactive notifications (e.g., policy changes relevant to the employee), integration with MK-ServiceDesk to auto-file tickets when the assistant can't fully resolve a query.

## Project Terminology

| Term | Definition |
|---|---|
| RAG | Retrieval-Augmented Generation — grounding model answers in retrieved documents. |
| Specialist Agent | A retrieval agent scoped to one department's knowledge. |
| Grounded Answer | A response whose claims are traceable to retrieved source documents. |
| Access Filter | The authorization layer that removes documents the requester isn't permitted to see. |

---
_This project documentation is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._