# PRJ-002 Technical Runbook: Tool-Calling Gateway Incident Response

```json
{
  "document_id": "PRJ-002-RUNBOOK-02",
  "title": "Tool-Calling Gateway Incident Response",
  "document_type": "Project Technical Runbook",
  "department": "Cross-Department",
  "category": "Project Operations",
  "project_id": "PRJ-002",
  "roles": [
    "on-call DevOps Engineer",
    "DevOps Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Tool-Calling Gateway Incident Response",
    "PRJ-002",
    "runbook"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** PRJ-002-RUNBOOK-02
**Project:** PRJ-002
**Owner:** DevOps Manager

## Purpose

This runbook defines the procedure for tool-calling gateway incident response within PRJ-002.

## Procedure

**Step 1:** the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several.

**Step 2:** the on-call DevOps Engineer performs the standard first-line check: checking gateway concurrency metrics against the current capacity limits.

**Step 3:** If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type.

**Step 4:** the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.

**Step 5:** If still unresolved, the on-call DevOps Engineer raises a ticket in the project's internal tooling categorised under 'Gateway Latency Incident', attaching screenshots or error logs.

**Step 6:** The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.

**Step 7:** the on-call DevOps Engineer confirms the fix works; the ticket is closed in the project's internal tooling with the root cause logged. Sustained gateway latency above SLA for more than 15 minutes triggers an automatic capacity scale-up.

## Notes
Sustained gateway latency above SLA for more than 15 minutes triggers an automatic capacity scale-up.

---
_This runbook is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._