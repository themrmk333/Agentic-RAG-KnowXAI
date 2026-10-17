# SOP: Test Automation Script Development

```json
{
  "document_id": "SOP-QA-004",
  "title": "Test Automation Script Development",
  "document_type": "SOP",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Test Automation",
  "subcategory": "Automation Script",
  "roles": [
    "QA Automation Engineer",
    "QA Lead"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Test Automation Script Development",
    "Test Automation",
    "Automation Script",
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

**Document ID:** SOP-QA-004  
**Department:** QA / Testing  
**Applicable Roles:** QA Automation Engineer, QA Lead  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **test automation script development** within the QA / Testing department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all QA Automation Engineers and any employee across MK-Infinite-AI who needs to initiate a **Automation Script** request. It covers the full workflow from initiation through to closure in MK-TestHub.

## Applicable Roles

- Primary actor: **QA Automation Engineer**
- Approver: **QA Lead**
- System of record: **MK-TestHub**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-TestHub.
- Adding the script to the MK-TestHub automation pipeline with tagging must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the automation script being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the QA Automation Engineer confirms eligibility and prerequisites: adding the script to the MK-TestHub automation pipeline with tagging.

**Step 2:** the QA Automation Engineer raises a request in MK-TestHub specifying exactly which Automation Script is required.

**Step 3:** The QA Lead reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Automation Script in the relevant system.

**Step 5:** the QA Automation Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-TestHub and corrected before sign-off.

**Step 7:** MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. Flaky automated tests are quarantined and tracked for a fix within one sprint.

## Expected Result

The automation script is completed, logged in MK-TestHub, and the requester is notified of the outcome. The record remains available in MK-TestHub for future reference and audit.

## Exceptions

- Flaky automated tests are quarantined and tracked for a fix within one sprint.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: QA Engineer → QA Lead → QA Manager → QA Director. Escalations should reference the SOP-QA-004 document ID and the relevant ticket/request number.

## Responsible Role

QA Automation Engineer

## Approval Role

QA Lead

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._