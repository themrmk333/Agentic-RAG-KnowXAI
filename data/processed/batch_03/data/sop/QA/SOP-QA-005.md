# SOP: Release Sign-off / Go-No-Go Procedure

```json
{
  "document_id": "SOP-QA-005",
  "title": "Release Sign-off / Go-No-Go Procedure",
  "document_type": "SOP",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Release Management",
  "subcategory": "Release Readiness Report",
  "roles": [
    "QA Lead",
    "QA Manager"
  ],
  "access_level": "manager",
  "allowed_departments": [
    "QA"
  ],
  "confidentiality": "Confidential",
  "keywords": [
    "Release Sign-off / Go-No-Go Procedure",
    "Release Management",
    "Release Readiness Report",
    "QA",
    "MK-TestHub"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "QA Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-QA-005  
**Department:** QA / Testing  
**Applicable Roles:** QA Lead, QA Manager  
**Access Level:** manager  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **release sign-off / go-no-go procedure** within the QA / Testing department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all QA Leads and any employee across MK-Infinite-AI who needs to initiate a **Release Readiness Report** request. It covers the full workflow from initiation through to closure in MK-TestHub.

## Applicable Roles

- Primary actor: **QA Lead**
- Approver: **QA Manager**
- System of record: **MK-TestHub**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-TestHub.
- Open defect count by severity and outstanding test coverage gaps must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the release readiness report being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** The review is scheduled in advance and stakeholders are notified through MK-TestHub.

**Step 2:** the QA Lead gathers the required data and documents, including open defect count by severity and outstanding test coverage gaps.

**Step 3:** The review team examines the Release Readiness Report against the applicable policy or checklist.

**Step 4:** Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.

**Step 5:** The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Step 6:** Remediation actions are tracked in MK-TestHub with due dates and status.

**Step 7:** The review is closed once all actions are completed, and the outcome is recorded for future audits. A single open Sev-1 defect is sufficient to block sign-off.

## Expected Result

The release readiness report is completed, logged in MK-TestHub, and the requester is notified of the outcome. The record remains available in MK-TestHub for future reference and audit.

## Exceptions

- A single open Sev-1 defect is sufficient to block sign-off.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: QA Engineer → QA Lead → QA Manager → QA Director. Escalations should reference the SOP-QA-005 document ID and the relevant ticket/request number.

## Responsible Role

QA Lead

## Approval Role

QA Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._