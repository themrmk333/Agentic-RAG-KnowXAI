# Troubleshooting Guide: Rollback Procedure

```json
{
  "document_id": "TSG-DEVOPS-002",
  "title": "Troubleshooting: Rollback Procedure",
  "document_type": "Troubleshooting Guide",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Deployment",
  "roles": [
    "All Employees"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Rollback Procedure",
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

**Document ID:** TSG-DEVOPS-002  
**Department:** DevOps & Cloud  
**Related SOP:** SOP-DEVOPS-012

## Symptom

An employee is experiencing an issue related to: **Rollback Procedure**.

## Diagnostic & Resolution Steps

1. the DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several.
2. the DevOps Engineer performs the standard first-line check: identifying the last known good deployment version in MK-CloudOps.
3. If the issue persists, the DevOps Engineer applies the documented workaround for this issue type.
4. the DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.
5. If still unresolved, the DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Deployment Rollback', attaching screenshots or error logs.
6. The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.
7. the DevOps Engineer confirms the fix works; the ticket is closed in MK-CloudOps with the root cause logged. Rollbacks are performed without waiting for full root cause analysis.

## If Still Unresolved

Escalate through: DevOps Engineer -> DevOps Manager -> DevOps Director. Reference document TSG-DEVOPS-002 and, if one exists, the related ticket number in MK-CloudOps.

## Notes

Rollbacks are performed without waiting for full root cause analysis.

---
_This troubleshooting guide is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._