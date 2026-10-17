# Troubleshooting Guide: Production Incident Response (Engineering)

```json
{
  "document_id": "TSG-ENG-001",
  "title": "Troubleshooting: Production Incident Response (Engineering)",
  "document_type": "Troubleshooting Guide",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Incident Management",
  "roles": [
    "All Employees"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Production Incident Response (Engineering)",
    "troubleshooting",
    "ENG",
    "MK-CodeForge"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** TSG-ENG-001  
**Department:** Software Engineering / Development  
**Related SOP:** SOP-ENG-013

## Symptom

An employee is experiencing an issue related to: **Production Incident Response (Engineering)**.

## Diagnostic & Resolution Steps

1. the on-call Software Engineer confirms the exact symptom, when it started, and whether it affects one system or several.
2. the on-call Software Engineer performs the standard first-line check: checking MK-CloudOps dashboards and recent deployments for correlation.
3. If the issue persists, the on-call Software Engineer applies the documented workaround for this issue type.
4. the on-call Software Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.
5. If still unresolved, the on-call Software Engineer raises a ticket in MK-CodeForge categorised under 'Production Incident', attaching screenshots or error logs.
6. The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.
7. the on-call Software Engineer confirms the fix works; the ticket is closed in MK-CodeForge with the root cause logged. Sev-1 incidents require a written postmortem within 48 hours.

## If Still Unresolved

Escalate through: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director. Reference document TSG-ENG-001 and, if one exists, the related ticket number in MK-CodeForge.

## Notes

Sev-1 incidents require a written postmortem within 48 hours.

---
_This troubleshooting guide is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._