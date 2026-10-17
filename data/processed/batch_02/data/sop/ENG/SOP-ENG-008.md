# SOP: Third-Party Library Approval

```json
{
  "document_id": "SOP-ENG-008",
  "title": "Third-Party Library Approval",
  "document_type": "SOP",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Dependency Management",
  "subcategory": "Library Approval Request",
  "roles": [
    "Software Engineer",
    "Security Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ENG"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Third-Party Library Approval",
    "Dependency Management",
    "Library Approval Request",
    "ENG",
    "MK-CodeForge"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-ENG-008  
**Department:** Software Engineering / Development  
**Applicable Roles:** Software Engineer, Security Manager  
**Access Level:** employee  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **third-party library approval** within the Software Engineering / Development department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Software Engineers and any employee across MK-Infinite-AI who needs to initiate a **Library Approval Request** request. It covers the full workflow from initiation through to closure in MK-CodeForge.

## Applicable Roles

- Primary actor: **Software Engineer**
- Approver: **Security Manager**
- System of record: **MK-CodeForge**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CodeForge.
- The library name, licence type, and known vulnerability scan results must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the library approval request being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section.

**Step 2:** the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results.

**Step 3:** the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting.

**Step 4:** the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review.

**Step 5:** The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Step 6:** On approval, MK-CodeForge updates the status to 'Approved' and notifies the Software Engineer by email/in-app notification.

**Step 7:** The approved Library Approval Request is processed and the record is retained in MK-CodeForge for audit purposes. GPL-licensed libraries require Legal review before approval.

## Expected Result

The library approval request is completed, logged in MK-CodeForge, and the requester is notified of the outcome. The record remains available in MK-CodeForge for future reference and audit.

## Exceptions

- GPL-licensed libraries require Legal review before approval.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Software Engineer → Tech Lead → Engineering Manager → Engineering Director. Escalations should reference the SOP-ENG-008 document ID and the relevant ticket/request number.

## Responsible Role

Software Engineer

## Approval Role

Security Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._