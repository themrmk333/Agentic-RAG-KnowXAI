# SOP: Rollback Procedure

```json
{
  "document_id": "SOP-DEVOPS-012",
  "title": "Rollback Procedure",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Deployment",
  "subcategory": "Deployment Rollback",
  "roles": [
    "DevOps Engineer",
    "DevOps Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Rollback Procedure",
    "Deployment",
    "Deployment Rollback",
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

**Document ID:** SOP-DEVOPS-012
**Department:** DevOps & Cloud
**Applicable Roles:** DevOps Engineer, DevOps Manager
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **rollback procedure** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all DevOps Engineers and any employee across MK-Infinite-AI who needs to initiate a **Deployment Rollback** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **DevOps Engineer**
- Approver: **DevOps Manager**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Identifying the last known good deployment version in MK-CloudOps must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the deployment rollback being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several.

**Step 2:** the DevOps Engineer performs the standard first-line check: identifying the last known good deployment version in MK-CloudOps.

**Step 3:** If the issue persists, the DevOps Engineer applies the documented workaround for this issue type.

**Step 4:** the DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.

**Step 5:** If still unresolved, the DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Deployment Rollback', attaching screenshots or error logs.

**Step 6:** The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.

**Step 7:** the DevOps Engineer confirms the fix works; the ticket is closed in MK-CloudOps with the root cause logged. Rollbacks are performed without waiting for full root cause analysis.

## Expected Result

The deployment rollback is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Rollbacks are performed without waiting for full root cause analysis.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-012 document ID and the relevant ticket/request number.

## Responsible Role

DevOps Engineer

## Approval Role

DevOps Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._