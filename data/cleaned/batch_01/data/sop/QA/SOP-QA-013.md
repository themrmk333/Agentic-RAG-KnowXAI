# SOP: Security Regression Testing Coordination

```json
{
  "document_id": "SOP-QA-013",
  "title": "Security Regression Testing Coordination",
  "document_type": "SOP",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Security Testing",
  "subcategory": "Security Test Pass",
  "roles": [
    "QA Engineer",
    "Security Analyst"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Security Regression Testing Coordination",
    "Security Testing",
    "Security Test Pass",
    "QA",
    "MK-TestHub"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Analyst",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-QA-013
**Department:** QA / Testing
**Applicable Roles:** QA Engineer, Security Analyst
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **security regression testing coordination** within the QA / Testing department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all QA Engineers and any employee across MK-Infinite-AI who needs to initiate a **Security Test Pass** request. It covers the full workflow from initiation through to closure in MK-TestHub.

## Applicable Roles

- Primary actor: **QA Engineer**
- Approver: **Security Analyst**
- System of record: **MK-TestHub**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-TestHub.
- Known vulnerability classes to test (OWASP Top 10) for this release must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the security test pass being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** The review is scheduled in advance and stakeholders are notified through MK-TestHub.

**Step 2:** the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release.

**Step 3:** The review team examines the Security Test Pass against the applicable policy or checklist.

**Step 4:** Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.

**Step 5:** The Security Analyst discusses the findings with the relevant department and agrees remediation actions.

**Step 6:** Remediation actions are tracked in MK-TestHub with due dates and status.

**Step 7:** The review is closed once all actions are completed, and the outcome is recorded for future audits. Any new high-severity finding blocks release until remediated.

## Expected Result

The security test pass is completed, logged in MK-TestHub, and the requester is notified of the outcome. The record remains available in MK-TestHub for future reference and audit.

## Exceptions

- Any new high-severity finding blocks release until remediated.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: QA Engineer → QA Lead → QA Manager → QA Director. Escalations should reference the SOP-QA-013 document ID and the relevant ticket/request number.

## Responsible Role

QA Engineer

## Approval Role

Security Analyst

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._