# SOP: Auto-scaling Configuration Procedure

```json
{
  "document_id": "SOP-DEVOPS-006",
  "title": "Auto-scaling Configuration Procedure",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Cloud Infrastructure",
  "subcategory": "Auto-scaling Policy",
  "roles": [
    "DevOps Engineer",
    "Cloud Architect"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Auto-scaling Configuration Procedure",
    "Cloud Infrastructure",
    "Auto-scaling Policy",
    "DEVOPS",
    "MK-CloudOps"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Cloud Architect",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DEVOPS-006
**Department:** DevOps & Cloud
**Applicable Roles:** DevOps Engineer, Cloud Architect
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **auto-scaling configuration procedure** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all DevOps Engineers and any employee across MK-Infinite-AI who needs to initiate a **Auto-scaling Policy** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **DevOps Engineer**
- Approver: **Cloud Architect**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Target CPU/memory thresholds and min/max instance counts must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the auto-scaling policy being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the DevOps Engineer confirms eligibility and prerequisites: target CPU/memory thresholds and min/max instance counts.

**Step 2:** the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Auto-scaling Policy is required.

**Step 3:** The Cloud Architect reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Auto-scaling Policy in the relevant system.

**Step 5:** the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.

**Step 7:** MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Scaling policies are load-tested before being applied to production.

## Expected Result

The auto-scaling policy is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Scaling policies are load-tested before being applied to production.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-006 document ID and the relevant ticket/request number.

## Responsible Role

DevOps Engineer

## Approval Role

Cloud Architect

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._