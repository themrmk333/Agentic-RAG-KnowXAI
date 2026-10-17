# SOP: Mobile App Testing Procedure

```json
{
  "document_id": "SOP-QA-010",
  "title": "Mobile App Testing Procedure",
  "document_type": "SOP",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Test Execution",
  "subcategory": "Mobile Test Pass",
  "roles": [
    "QA Engineer",
    "QA Lead"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Mobile App Testing Procedure",
    "Test Execution",
    "Mobile Test Pass",
    "QA",
    "MK-TestHub"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "QA Lead",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-QA-010  
**Department:** QA / Testing  
**Applicable Roles:** QA Engineer, QA Lead  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **mobile app testing procedure** within the QA / Testing department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all QA Engineers and any employee across MK-Infinite-AI who needs to initiate a **Mobile Test Pass** request. It covers the full workflow from initiation through to closure in MK-TestHub.

## Applicable Roles

- Primary actor: **QA Engineer**
- Approver: **QA Lead**
- System of record: **MK-TestHub**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-TestHub.
- The device/OS matrix required for the release must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the mobile test pass being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release.

**Step 2:** the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required.

**Step 3:** The QA Lead reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system.

**Step 5:** the QA Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-TestHub and corrected before sign-off.

**Step 7:** MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. Critical device coverage gaps are flagged to QA Manager before sign-off.

## Expected Result

The mobile test pass is completed, logged in MK-TestHub, and the requester is notified of the outcome. The record remains available in MK-TestHub for future reference and audit.

## Exceptions

- Critical device coverage gaps are flagged to QA Manager before sign-off.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: QA Engineer → QA Lead → QA Manager → QA Director. Escalations should reference the SOP-QA-010 document ID and the relevant ticket/request number.

## Responsible Role

QA Engineer

## Approval Role

QA Lead

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._