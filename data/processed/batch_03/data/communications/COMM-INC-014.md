# Incident Postmortem: Authentication Service Brief Outage (#14)

```json
{
  "document_id": "COMM-INC-014",
  "title": "Incident Postmortem: Authentication Service Brief Outage (#14)",
  "document_type": "Incident Report",
  "department": "SEC",
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
    "Authentication Service Brief Outage",
    "incident",
    "postmortem",
    "SEC"
  ],
  "created_date": "2026-01-29",
  "updated_date": "2026-01-29",
  "version": "1.0",
  "status": "Published",
  "owner": "SEC",
  "source": "synthetic-generated"
}
```

**Department:** SEC  |  **Date:** 2026-01-29  |  **Severity:** Sev-2

## What Happened
A certificate rotation was not completed in time, causing SSO login failures for approximately 12 minutes.

## Corrective Action
Certificate expiry alerts now fire 30 days in advance instead of 7.


---
_This incident postmortem is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._