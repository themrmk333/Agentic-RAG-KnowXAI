# SOP: Production Incident Response (DevOps)

```json
{
  "document_id": "SOP-DEVOPS-004",
  "title": "Production Incident Response (DevOps)",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Incident Management",
  "subcategory": "Infrastructure Incident",
  "roles": [
    "on-call DevOps Engineer",
    "DevOps Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Production Incident Response (DevOps)",
    "Incident Management",
    "Infrastructure Incident",
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

**Document ID:** SOP-DEVOPS-004  
**Department:** DevOps & Cloud  
**Applicable Roles:** on-call DevOps Engineer, DevOps Manager  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **production incident response (devops)** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all on-call DevOps Engineers and any employee across MK-Infinite-AI who needs to initiate a **Infrastructure Incident** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **on-call DevOps Engineer**
- Approver: **DevOps Manager**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Checking MK-CloudOps monitoring dashboards for alerts and anomalies must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the infrastructure incident being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several.

**Step 2:** the on-call DevOps Engineer performs the standard first-line check: checking MK-CloudOps monitoring dashboards for alerts and anomalies.

**Step 3:** If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type.

**Step 4:** the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.

**Step 5:** If still unresolved, the on-call DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Infrastructure Incident', attaching screenshots or error logs.

**Step 6:** The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.

**Step 7:** the on-call DevOps Engineer confirms the fix works; the ticket is closed in MK-CloudOps with the root cause logged. Sev-1 outages trigger an incident bridge call within 10 minutes.

## Expected Result

The infrastructure incident is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Sev-1 outages trigger an incident bridge call within 10 minutes.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-004 document ID and the relevant ticket/request number.

## Responsible Role

on-call DevOps Engineer

## Approval Role

DevOps Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._