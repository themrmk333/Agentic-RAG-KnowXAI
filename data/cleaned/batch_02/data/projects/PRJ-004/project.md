# Project: AI-Powered Business Analytics Platform (PRJ-004)

```json
{
  "document_id": "PRJ-004",
  "title": "AI-Powered Business Analytics Platform",
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
    "AI-Powered Business Analytics Platform",
    "PRJ-004",
    "DATA",
    "ENG",
    "PROD"
  ],
  "created_date": "2026-02-20",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "In Progress - Beta",
  "owner": "Riya Agarwal",
  "source": "synthetic-generated"
}
```

**Status:** In Progress - Beta  |  **Start Date:** 2026-02-20  |  **Expected Completion:** 2026-10-31
**Project Manager:** Riya Agarwal  |  **Technical Lead:** Anjali Rao
**Teams Involved:** Data & Analytics, Engineering, Product Management

## Overview
A natural-language analytics layer on top of MK-DataLake that lets business users ask questions about company data and receive charts/summaries without writing SQL.

## Business Objective
Increase self-service analytics adoption across non-technical departments (Sales, Marketing, Finance).

## Problem Statement
Business teams currently depend on the Data & Analytics team for most ad-hoc reporting requests, creating a backlog.

## Architecture Overview
A natural-language-to-SQL translation layer converts business questions into governed queries against MK-DataLake's semantic model; results are auto-visualized; a KPI-governance layer ensures answers use the single agreed definition for each metric.

## Technology Stack

- Python query-translation service
- MK-DataLake (Snowflake-style warehouse)
- Semantic layer / metrics store
- React-based visualization frontend

## Components

- NL-to-SQL translator
- Semantic/metrics layer
- Auto-visualization engine
- Query governance/guardrails

## Database
MK-DataLake warehouse with a governed semantic layer defining approved KPIs.

## APIs

- `POST /v1/analytics/ask`
- `GET /v1/analytics/kpis`
- `GET /v1/analytics/history`

## AI Models
A fine-tuned NL-to-SQL model constrained to the approved semantic layer to prevent ungoverned queries.

## RAG Components
Partially — KPI definitions and metric documentation are retrieved to ground the query translation.

## Agent Architecture
A single translation agent with a validation step that rejects queries falling outside the governed semantic layer.

## Security Architecture
Query results are filtered by the requester's data access level; Restricted-classified fields are never returned to unauthorized users.

## Development Workflow
Feature branches reviewed by Tech Lead and Analytics Lead for any change touching the semantic layer.

## Testing Workflow
QA validates NL-to-SQL translation accuracy against a curated set of business questions before release.

## Deployment Workflow
Staged rollout department by department, starting with Data & Analytics power users.

## CI/CD Workflow
MK-CI pipeline with translation-accuracy gating and semantic-layer regression tests.

## Known Issues

- Ambiguous date-range questions ('last quarter') sometimes default to the wrong fiscal calendar.
- Auto-visualization occasionally picks a suboptimal chart type for categorical comparisons.

## Risks

- Users trusting an incorrect auto-generated answer without verifying against the source KPI definition.
- Semantic layer maintenance becoming a bottleneck as more KPIs are added.

## Dependencies

- MK-DataLake semantic layer completeness
- KPI Governance SOP compliance from Data & Analytics

## Milestones

| Milestone | Target Date | Status |
|---|---|---|
| NL-to-SQL prototype | 2026-04-10 | Done |
| Semantic layer v1 | 2026-06-01 | Done |
| Beta with Sales & Finance | 2026-08-01 | In Progress |
| Company-wide GA | 2026-10-31 | Planned |

## Current Sprint
Sprint 11: Fixing fiscal-calendar date-range interpretation.

## Backlog (Upcoming)

- Add proactive anomaly alerts
- Support scheduled recurring questions

## Future Roadmap
Integrate with the Enterprise Knowledge Assistant so analytics questions can be asked from the same interface.

## Project Terminology

| Term | Definition |
|---|---|
| Semantic Layer | A governed definition layer mapping business terms to underlying data fields. |
| NL-to-SQL | Translating a natural-language question into a structured database query. |
| KPI Governance | Ensuring a single agreed definition and source for each business metric. |

---
_This project documentation is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._