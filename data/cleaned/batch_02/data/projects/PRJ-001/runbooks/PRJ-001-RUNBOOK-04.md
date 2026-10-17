# PRJ-001 Technical Runbook: Authorization Filter Incident Response

```json
{
  "document_id": "PRJ-001-RUNBOOK-04",
  "title": "Authorization Filter Incident Response",
  "document_type": "Project Technical Runbook",
  "department": "Cross-Department",
  "category": "Project Operations",
  "project_id": "PRJ-001",
  "roles": [
    "on-call Software Engineer",
    "Security Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Authorization Filter Incident Response",
    "PRJ-001",
    "runbook"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** PRJ-001-RUNBOOK-04
**Project:** PRJ-001
**Owner:** Security Manager

## Purpose

This runbook defines the procedure for authorization filter incident response within PRJ-001.

## Procedure

**Step 1:** the on-call Software Engineer confirms the exact symptom, when it started, and whether it affects one system or several.

**Step 2:** the on-call Software Engineer performs the standard first-line check: checking whether any restricted document was returned to an unauthorized role in the affected time window.

**Step 3:** If the issue persists, the on-call Software Engineer applies the documented workaround for this issue type.

**Step 4:** the on-call Software Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.

**Step 5:** If still unresolved, the on-call Software Engineer raises a ticket in the project's internal tooling categorised under 'Authorization Filter Bug', attaching screenshots or error logs.

**Step 6:** The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.

**Step 7:** the on-call Software Engineer confirms the fix works; the ticket is closed in the project's internal tooling with the root cause logged. Any confirmed exposure of a restricted document is treated as a Sev-1 security incident, not a normal bug.

## Notes
Any confirmed exposure of a restricted document is treated as a Sev-1 security incident, not a normal bug.

---
_This runbook is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._