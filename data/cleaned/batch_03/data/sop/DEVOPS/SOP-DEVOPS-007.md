# SOP: Backup and Disaster Recovery Test

```json
{
  "document_id": "SOP-DEVOPS-007",
  "title": "Backup and Disaster Recovery Test",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Disaster Recovery",
  "subcategory": "DR Test",
  "roles": [
    "Site Reliability Engineer",
    "DevOps Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Backup and Disaster Recovery Test",
    "Disaster Recovery",
    "DR Test",
    "DEVOPS",
    "MK-CloudOps"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DEVOPS-007
**Department:** DevOps & Cloud
**Applicable Roles:** Site Reliability Engineer, DevOps Manager
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **backup and disaster recovery test** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Site Reliability Engineers and any employee across MK-Infinite-AI who needs to initiate a **DR Test** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **Site Reliability Engineer**
- Approver: **DevOps Manager**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Restoring a sample backup to a sandbox environment and validating integrity must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the dr test being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** The review is scheduled in advance and stakeholders are notified through MK-CloudOps.

**Step 2:** the Site Reliability Engineer gathers the required data and documents, including restoring a sample backup to a sandbox environment and validating integrity.

**Step 3:** The review team examines the DR Test against the applicable policy or checklist.

**Step 4:** Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.

**Step 5:** The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Step 6:** Remediation actions are tracked in MK-CloudOps with due dates and status.

**Step 7:** The review is closed once all actions are completed, and the outcome is recorded for future audits. DR tests are conducted quarterly and results are reported to Management.

## Expected Result

The dr test is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- DR tests are conducted quarterly and results are reported to Management.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-007 document ID and the relevant ticket/request number.

## Responsible Role

Site Reliability Engineer

## Approval Role

DevOps Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._