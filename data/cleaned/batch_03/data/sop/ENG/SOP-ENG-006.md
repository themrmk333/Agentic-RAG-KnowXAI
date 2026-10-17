# SOP: API Key and Secret Rotation

```json
{
  "document_id": "SOP-ENG-006",
  "title": "API Key and Secret Rotation",
  "document_type": "SOP",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Security",
  "subcategory": "Secret Rotation",
  "roles": [
    "Software Engineer",
    "Security Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "API Key and Secret Rotation",
    "Security",
    "Secret Rotation",
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

**Document ID:** SOP-ENG-006
**Department:** Software Engineering / Development
**Applicable Roles:** Software Engineer, Security Manager
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **api key and secret rotation** within the Software Engineering / Development department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Software Engineers and any employee across MK-Infinite-AI who needs to initiate a **Secret Rotation** request. It covers the full workflow from initiation through to closure in MK-CodeForge.

## Applicable Roles

- Primary actor: **Software Engineer**
- Approver: **Security Manager**
- System of record: **MK-CodeForge**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CodeForge.
- Identifying every service referencing the current secret must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the secret rotation being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret.

**Step 2:** the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required.

**Step 3:** The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system.

**Step 5:** the Software Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-CodeForge and corrected before sign-off.

**Step 7:** MK-CodeForge marks the request 'Complete' and the configuration is logged for audit and future reference. Secrets are never committed to MK-CodeForge; violations trigger an automatic Security alert.

## Expected Result

The secret rotation is completed, logged in MK-CodeForge, and the requester is notified of the outcome. The record remains available in MK-CodeForge for future reference and audit.

## Exceptions

- Secrets are never committed to MK-CodeForge; violations trigger an automatic Security alert.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Software Engineer → Tech Lead → Engineering Manager → Engineering Director. Escalations should reference the SOP-ENG-006 document ID and the relevant ticket/request number.

## Responsible Role

Software Engineer

## Approval Role

Security Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._