# Incident Postmortem: Data Pipeline Delay Affecting Dashboards (#20)

```json
{
  "document_id": "COMM-INC-020",
  "title": "Incident Postmortem: Data Pipeline Delay Affecting Dashboards (#20)",
  "document_type": "Incident Report",
  "department": "DATA",
  "category": "Incident Postmortem",
  "roles": [
    "All Employees"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Pipeline Delay Affecting Dashboards",
    "incident",
    "postmortem",
    "DATA"
  ],
  "created_date": "2026-02-26",
  "updated_date": "2026-02-26",
  "version": "1.0",
  "status": "Published",
  "owner": "DATA",
  "source": "synthetic-generated"
}
```

**Department:** DATA  |  **Date:** 2026-02-26  |  **Severity:** Sev-2

## What Happened
An upstream source schema change broke a transformation step, delaying dashboard refresh by several hours.

## Corrective Action
A schema-change detection check was added upstream of the transformation step.


---
_This incident postmortem is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._