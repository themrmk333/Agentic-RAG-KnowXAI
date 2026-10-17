# SOP: New Repository Setup

```json
{
  "document_id": "SOP-ENG-003",
  "title": "New Repository Setup",
  "document_type": "SOP",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Version Control",
  "subcategory": "Repository",
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
    "New Repository Setup",
    "Version Control",
    "Repository",
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

**Document ID:** SOP-ENG-003
**Department:** Software Engineering / Development
**Applicable Roles:** Software Engineer, Engineering Manager
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **new repository setup** within the Software Engineering / Development department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Software Engineers and any employee across MK-Infinite-AI who needs to initiate a **Repository** request. It covers the full workflow from initiation through to closure in MK-CodeForge.

## Applicable Roles

- Primary actor: **Software Engineer**
- Approver: **Engineering Manager**
- System of record: **MK-CodeForge**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CodeForge.
- Repository name, visibility, and initial branch protection rules must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the repository being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules.

**Step 2:** the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required.

**Step 3:** The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Repository in the relevant system.

**Step 5:** the Software Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-CodeForge and corrected before sign-off.

**Step 7:** MK-CodeForge marks the request 'Complete' and the configuration is logged for audit and future reference. All new repositories must enable required status checks before merge.

## Expected Result

The repository is completed, logged in MK-CodeForge, and the requester is notified of the outcome. The record remains available in MK-CodeForge for future reference and audit.

## Exceptions

- All new repositories must enable required status checks before merge.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Software Engineer → Tech Lead → Engineering Manager → Engineering Director. Escalations should reference the SOP-ENG-003 document ID and the relevant ticket/request number.

## Responsible Role

Software Engineer

## Approval Role

Engineering Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._