# Incident Postmortem: Elevated API Error Rate (#11)

```json
{
  "document_id": "COMM-INC-011",
  "title": "Incident Postmortem: Elevated API Error Rate (#11)",
  "document_type": "Incident Report",
  "department": "DEVOPS",
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
    "Elevated API Error Rate",
    "incident",
    "postmortem",
    "DEVOPS"
  ],
  "created_date": "2025-12-21",
  "updated_date": "2025-12-21",
  "version": "1.0",
  "status": "Published",
  "owner": "DEVOPS",
  "source": "synthetic-generated"
}
```

**Department:** DEVOPS  |  **Date:** 2025-12-21  |  **Severity:** Sev-2

## What Happened
A deployment introduced a misconfigured timeout setting on the payment gateway integration, causing elevated 5xx errors for 18 minutes.

## Corrective Action
The auto-scaling policy is now validated against a canary check before full rollout.


---
_This incident postmortem is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._