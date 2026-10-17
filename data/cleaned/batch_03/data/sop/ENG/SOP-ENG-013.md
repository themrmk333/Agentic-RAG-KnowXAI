# SOP: Production Incident Response (Engineering)

```json
{
  "document_id": "SOP-ENG-013",
  "title": "Production Incident Response (Engineering)",
  "document_type": "SOP",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Incident Management",
  "subcategory": "Production Incident",
  "roles": [
    "on-call Software Engineer",
    "Engineering Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Production Incident Response (Engineering)",
    "Incident Management",
    "Production Incident",
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

**Document ID:** SOP-ENG-013
**Department:** Software Engineering / Development
**Applicable Roles:** on-call Software Engineer, Engineering Manager
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **production incident response (engineering)** within the Software Engineering / Development department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all on-call Software Engineers and any employee across MK-Infinite-AI who needs to initiate a **Production Incident** request. It covers the full workflow from initiation through to closure in MK-CodeForge.

## Applicable Roles

- Primary actor: **on-call Software Engineer**
- Approver: **Engineering Manager**
- System of record: **MK-CodeForge**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CodeForge.
- Checking MK-CloudOps dashboards and recent deployments for correlation must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the production incident being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the on-call Software Engineer confirms the exact symptom, when it started, and whether it affects one system or several.

**Step 2:** the on-call Software Engineer performs the standard first-line check: checking MK-CloudOps dashboards and recent deployments for correlation.

**Step 3:** If the issue persists, the on-call Software Engineer applies the documented workaround for this issue type.

**Step 4:** the on-call Software Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.

**Step 5:** If still unresolved, the on-call Software Engineer raises a ticket in MK-CodeForge categorised under 'Production Incident', attaching screenshots or error logs.

**Step 6:** The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.

**Step 7:** the on-call Software Engineer confirms the fix works; the ticket is closed in MK-CodeForge with the root cause logged. Sev-1 incidents require a written postmortem within 48 hours.

## Expected Result

The production incident is completed, logged in MK-CodeForge, and the requester is notified of the outcome. The record remains available in MK-CodeForge for future reference and audit.

## Exceptions

- Sev-1 incidents require a written postmortem within 48 hours.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Software Engineer → Tech Lead → Engineering Manager → Engineering Director. Escalations should reference the SOP-ENG-013 document ID and the relevant ticket/request number.

## Responsible Role

on-call Software Engineer

## Approval Role

Engineering Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._