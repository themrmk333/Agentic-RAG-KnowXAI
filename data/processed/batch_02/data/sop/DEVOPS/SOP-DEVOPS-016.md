# SOP: On-call Rotation and Handover

```json
{
  "document_id": "SOP-DEVOPS-016",
  "title": "On-call Rotation and Handover",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Operations",
  "subcategory": "On-call Handover",
  "roles": [
    "outgoing on-call Engineer",
    "DevOps Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "DEVOPS"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "On-call Rotation and Handover",
    "Operations",
    "On-call Handover",
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

**Document ID:** SOP-DEVOPS-016  
**Department:** DevOps & Cloud  
**Applicable Roles:** outgoing on-call Engineer, DevOps Manager  
**Access Level:** employee  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **on-call rotation and handover** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all outgoing on-call Engineers and any employee across MK-Infinite-AI who needs to initiate a **On-call Handover** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **outgoing on-call Engineer**
- Approver: **DevOps Manager**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Open incidents, known issues, and any suppressed alerts must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the on-call handover being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** The review is scheduled in advance and stakeholders are notified through MK-CloudOps.

**Step 2:** the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts.

**Step 3:** The review team examines the On-call Handover against the applicable policy or checklist.

**Step 4:** Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.

**Step 5:** The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Step 6:** Remediation actions are tracked in MK-CloudOps with due dates and status.

**Step 7:** The review is closed once all actions are completed, and the outcome is recorded for future audits. Handover must happen via a written note in MK-CloudOps, not verbally only.

## Expected Result

The on-call handover is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Handover must happen via a written note in MK-CloudOps, not verbally only.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-016 document ID and the relevant ticket/request number.

## Responsible Role

outgoing on-call Engineer

## Approval Role

DevOps Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._