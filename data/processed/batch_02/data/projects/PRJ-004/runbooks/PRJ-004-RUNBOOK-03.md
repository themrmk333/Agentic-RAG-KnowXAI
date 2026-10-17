# PRJ-004 Technical Runbook: Fiscal Calendar Date-Range Bug Resolution Procedure

```json
{
  "document_id": "PRJ-004-RUNBOOK-03",
  "title": "Fiscal Calendar Date-Range Bug Resolution Procedure",
  "document_type": "Project Technical Runbook",
  "department": "Cross-Department",
  "category": "Project Operations",
  "project_id": "PRJ-004",
  "roles": [
    "Software Engineer",
    "Tech Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Fiscal Calendar Date-Range Bug Resolution Procedure",
    "PRJ-004",
    "runbook"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Tech Lead",
  "source": "synthetic-generated"
}
```

**Document ID:** PRJ-004-RUNBOOK-03  
**Project:** PRJ-004  
**Owner:** Tech Lead

## Purpose

This runbook defines the procedure for fiscal calendar date-range bug resolution procedure within PRJ-004.

## Procedure

**Step 1:** the Software Engineer confirms the exact symptom, when it started, and whether it affects one system or several.

**Step 2:** the Software Engineer performs the standard first-line check: checking whether the query used the company fiscal calendar or the default calendar.

**Step 3:** If the issue persists, the Software Engineer applies the documented workaround for this issue type.

**Step 4:** the Software Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.

**Step 5:** If still unresolved, the Software Engineer raises a ticket in the project's internal tooling categorised under 'Date-Range Interpretation Bug', attaching screenshots or error logs.

**Step 6:** The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.

**Step 7:** the Software Engineer confirms the fix works; the ticket is closed in the project's internal tooling with the root cause logged. Fiscal calendar bugs are treated as high priority given their impact on Finance-facing metrics.

## Notes
Fiscal calendar bugs are treated as high priority given their impact on Finance-facing metrics.

---
_This runbook is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._