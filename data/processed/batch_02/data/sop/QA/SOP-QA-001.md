# SOP: Software Defect Reporting Procedure

```json
{
  "document_id": "SOP-QA-001",
  "title": "Software Defect Reporting Procedure",
  "document_type": "SOP",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Defect Management",
  "subcategory": "Defect Report",
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
    "Software Defect Reporting Procedure",
    "Defect Management",
    "Defect Report",
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

**Document ID:** SOP-QA-001  
**Department:** QA / Testing  
**Applicable Roles:** QA Engineer, QA Lead  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **software defect reporting procedure** within the QA / Testing department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all QA Engineers and any employee across MK-Infinite-AI who needs to initiate a **Defect Report** request. It covers the full workflow from initiation through to closure in MK-TestHub.

## Applicable Roles

- Primary actor: **QA Engineer**
- Approver: **QA Lead**
- System of record: **MK-TestHub**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-TestHub.
- Steps to reproduce, expected vs actual result, and severity must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the defect report being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the QA Engineer logs into MK-TestHub and navigates to the 'Defect Report' section.

**Step 2:** the QA Engineer selects 'New Defect Report' and enters the required details, including steps to reproduce, expected vs actual result, and severity.

**Step 3:** the QA Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting.

**Step 4:** the QA Engineer submits the Defect Report; MK-TestHub automatically routes it to the QA Lead for review.

**Step 5:** The QA Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Step 6:** On approval, MK-TestHub updates the status to 'Approved' and notifies the QA Engineer by email/in-app notification.

**Step 7:** The approved Defect Report is processed and the record is retained in MK-TestHub for audit purposes. Sev-1 defects blocking release are reported to the Engineering Manager immediately.

## Expected Result

The defect report is completed, logged in MK-TestHub, and the requester is notified of the outcome. The record remains available in MK-TestHub for future reference and audit.

## Exceptions

- Sev-1 defects blocking release are reported to the Engineering Manager immediately.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: QA Engineer → QA Lead → QA Manager → QA Director. Escalations should reference the SOP-QA-001 document ID and the relevant ticket/request number.

## Responsible Role

QA Engineer

## Approval Role

QA Lead

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._