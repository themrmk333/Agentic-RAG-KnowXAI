# SOP: Code Freeze Procedure

```json
{
  "document_id": "SOP-ENG-010",
  "title": "Code Freeze Procedure",
  "document_type": "SOP",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Release Management",
  "subcategory": "Release Branch",
  "roles": [
    "Tech Lead",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ENG"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Code Freeze Procedure",
    "Release Management",
    "Release Branch",
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

**Document ID:** SOP-ENG-010  
**Department:** Software Engineering / Development  
**Applicable Roles:** Tech Lead, Engineering Manager  
**Access Level:** employee  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **code freeze procedure** within the Software Engineering / Development department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Tech Leads and any employee across MK-Infinite-AI who needs to initiate a **Release Branch** request. It covers the full workflow from initiation through to closure in MK-CodeForge.

## Applicable Roles

- Primary actor: **Tech Lead**
- Approver: **Engineering Manager**
- System of record: **MK-CodeForge**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CodeForge.
- Listing all open PRs targeting the release branch must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the release branch being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** The review is scheduled in advance and stakeholders are notified through MK-CodeForge.

**Step 2:** the Tech Lead gathers the required data and documents, including listing all open PRs targeting the release branch.

**Step 3:** The review team examines the Release Branch against the applicable policy or checklist.

**Step 4:** Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.

**Step 5:** The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Step 6:** Remediation actions are tracked in MK-CodeForge with due dates and status.

**Step 7:** The review is closed once all actions are completed, and the outcome is recorded for future audits. Only critical bug fixes are merged after code freeze, with Engineering Manager sign-off.

## Expected Result

The release branch is completed, logged in MK-CodeForge, and the requester is notified of the outcome. The record remains available in MK-CodeForge for future reference and audit.

## Exceptions

- Only critical bug fixes are merged after code freeze, with Engineering Manager sign-off.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Software Engineer → Tech Lead → Engineering Manager → Engineering Director. Escalations should reference the SOP-ENG-010 document ID and the relevant ticket/request number.

## Responsible Role

Tech Lead

## Approval Role

Engineering Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._