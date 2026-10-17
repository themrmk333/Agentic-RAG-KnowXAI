# SOP: Environment Promotion Procedure (Dev → Staging → Prod)

```json
{
  "document_id": "SOP-DEVOPS-011",
  "title": "Environment Promotion Procedure (Dev \u2192 Staging \u2192 Prod)",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Release Management",
  "subcategory": "Promotion Request",
  "roles": [
    "DevOps Engineer",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "DEVOPS"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Environment Promotion Procedure (Dev \u2192 Staging \u2192 Prod)",
    "Release Management",
    "Promotion Request",
    "DEVOPS",
    "MK-CloudOps"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DEVOPS-011
**Department:** DevOps & Cloud
**Applicable Roles:** DevOps Engineer, Engineering Manager
**Access Level:** employee
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **environment promotion procedure (dev → staging → prod)** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all DevOps Engineers and any employee across MK-Infinite-AI who needs to initiate a **Promotion Request** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **DevOps Engineer**
- Approver: **Engineering Manager**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Staging sign-off evidence and change ticket reference must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the promotion request being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the DevOps Engineer logs into MK-CloudOps and navigates to the 'Promotion Request' section.

**Step 2:** the DevOps Engineer selects 'New Promotion Request' and enters the required details, including staging sign-off evidence and change ticket reference.

**Step 3:** the DevOps Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting.

**Step 4:** the DevOps Engineer submits the Promotion Request; MK-CloudOps automatically routes it to the Engineering Manager for review.

**Step 5:** The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Step 6:** On approval, MK-CloudOps updates the status to 'Approved' and notifies the DevOps Engineer by email/in-app notification.

**Step 7:** The approved Promotion Request is processed and the record is retained in MK-CloudOps for audit purposes. Promotions to production require QA sign-off attached to the request.

## Expected Result

The promotion request is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Promotions to production require QA sign-off attached to the request.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-011 document ID and the relevant ticket/request number.

## Responsible Role

DevOps Engineer

## Approval Role

Engineering Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._