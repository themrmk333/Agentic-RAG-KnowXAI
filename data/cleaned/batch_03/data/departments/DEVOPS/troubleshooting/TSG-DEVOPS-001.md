# Troubleshooting Guide: Production Incident Response (DevOps)

```json
{
  "document_id": "TSG-DEVOPS-001",
  "title": "Troubleshooting: Production Incident Response (DevOps)",
  "document_type": "Troubleshooting Guide",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
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
    "Production Incident Response (DevOps)",
    "troubleshooting",
    "DEVOPS",
    "MK-CloudOps"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** TSG-DEVOPS-001
**Department:** DevOps & Cloud
**Related SOP:** SOP-DEVOPS-004

## Symptom

An employee is experiencing an issue related to: **Production Incident Response (DevOps)**.

## Diagnostic & Resolution Steps

1. the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several.
2. the on-call DevOps Engineer performs the standard first-line check: checking MK-CloudOps monitoring dashboards for alerts and anomalies.
3. If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type.
4. the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.
5. If still unresolved, the on-call DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Infrastructure Incident', attaching screenshots or error logs.
6. The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.
7. the on-call DevOps Engineer confirms the fix works; the ticket is closed in MK-CloudOps with the root cause logged. Sev-1 outages trigger an incident bridge call within 10 minutes.

## If Still Unresolved

Escalate through: DevOps Engineer -> DevOps Manager -> DevOps Director. Reference document TSG-DEVOPS-001 and, if one exists, the related ticket number in MK-CloudOps.

## Notes

Sev-1 outages trigger an incident bridge call within 10 minutes.

---
_This troubleshooting guide is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._