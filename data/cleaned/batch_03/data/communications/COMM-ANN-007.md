# Announcement: Production Incident Postmortem: MK-CloudOps Outage

```json
{
  "document_id": "COMM-ANN-007",
  "title": "Production Incident Postmortem: MK-CloudOps Outage",
  "document_type": "Announcement",
  "department": "DevOps",
  "category": "Incident Report",
  "roles": [
    "All Employees"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Production Incident Postmortem: MK-CloudOps Outage",
    "Incident Report",
    "DevOps"
  ],
  "created_date": "2026-06-25",
  "updated_date": "2026-06-25",
  "version": "1.0",
  "status": "Published",
  "owner": "DevOps",
  "source": "synthetic-generated"
}
```

**Department:** DevOps  |  **Category:** Incident Report  |  **Date:** 2026-06-25

A Sev-1 incident on the production API gateway caused 42 minutes of degraded service. Root cause: an auto-scaling policy misconfiguration during a routine deployment. Corrective actions: additional pre-deployment validation checks have been added to the CI/CD pipeline per the IaC Change Procedure.

---
_This announcement is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._