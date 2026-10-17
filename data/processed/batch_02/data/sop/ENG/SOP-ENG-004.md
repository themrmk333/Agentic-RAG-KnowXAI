# SOP: Production Hotfix Deployment

```json
{
  "document_id": "SOP-ENG-004",
  "title": "Production Hotfix Deployment",
  "document_type": "SOP",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Release Management",
  "subcategory": "Hotfix Request",
  "roles": [
    "Software Engineer",
    "Engineering Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Production Hotfix Deployment",
    "Release Management",
    "Hotfix Request",
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

**Document ID:** SOP-ENG-004  
**Department:** Software Engineering / Development  
**Applicable Roles:** Software Engineer, Engineering Manager  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **production hotfix deployment** within the Software Engineering / Development department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Software Engineers and any employee across MK-Infinite-AI who needs to initiate a **Hotfix Request** request. It covers the full workflow from initiation through to closure in MK-CodeForge.

## Applicable Roles

- Primary actor: **Software Engineer**
- Approver: **Engineering Manager**
- System of record: **MK-CodeForge**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CodeForge.
- The incident ID, root cause summary, and rollback plan must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the hotfix request being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section.

**Step 2:** the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan.

**Step 3:** the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting.

**Step 4:** the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review.

**Step 5:** The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Step 6:** On approval, MK-CodeForge updates the status to 'Approved' and notifies the Software Engineer by email/in-app notification.

**Step 7:** The approved Hotfix Request is processed and the record is retained in MK-CodeForge for audit purposes. Hotfixes bypass the normal sprint cycle but still require a peer review.

## Expected Result

The hotfix request is completed, logged in MK-CodeForge, and the requester is notified of the outcome. The record remains available in MK-CodeForge for future reference and audit.

## Exceptions

- Hotfixes bypass the normal sprint cycle but still require a peer review.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Software Engineer → Tech Lead → Engineering Manager → Engineering Director. Escalations should reference the SOP-ENG-004 document ID and the relevant ticket/request number.

## Responsible Role

Software Engineer

## Approval Role

Engineering Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._