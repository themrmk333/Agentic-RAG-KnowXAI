# Incident Postmortem: Email Delivery Delay (#27)

```json
{
  "document_id": "COMM-INC-027",
  "title": "Incident Postmortem: Email Delivery Delay (#27)",
  "document_type": "Incident Report",
  "department": "IT",
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
    "Email Delivery Delay",
    "incident",
    "postmortem",
    "IT"
  ],
  "created_date": "2025-08-02",
  "updated_date": "2025-08-02",
  "version": "1.0",
  "status": "Published",
  "owner": "IT",
  "source": "synthetic-generated"
}
```

**Department:** IT  |  **Date:** 2025-08-02  |  **Severity:** Sev-2

## What Happened
The corporate email relay queue backed up during a bulk send, delaying delivery by up to 40 minutes for some employees.

## Corrective Action
Queue capacity alerts now trigger at 70% instead of 90% utilization.

---
_This incident postmortem is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._