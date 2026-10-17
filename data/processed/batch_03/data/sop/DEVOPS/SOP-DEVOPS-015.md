# SOP: Patch Management for Infrastructure

```json
{
  "document_id": "SOP-DEVOPS-015",
  "title": "Patch Management for Infrastructure",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Patch Management",
  "subcategory": "Patch Deployment",
  "roles": [
    "DevOps Engineer",
    "Security Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Patch Management for Infrastructure",
    "Patch Management",
    "Patch Deployment",
    "DEVOPS",
    "MK-CloudOps"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DEVOPS-015  
**Department:** DevOps & Cloud  
**Applicable Roles:** DevOps Engineer, Security Manager  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **patch management for infrastructure** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all DevOps Engineers and any employee across MK-Infinite-AI who needs to initiate a **Patch Deployment** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **DevOps Engineer**
- Approver: **Security Manager**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Testing the patch in staging before production rollout must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the patch deployment being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the DevOps Engineer confirms eligibility and prerequisites: testing the patch in staging before production rollout.

**Step 2:** the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Patch Deployment is required.

**Step 3:** The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Patch Deployment in the relevant system.

**Step 5:** the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.

**Step 7:** MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Critical security patches are applied within 72 hours of release.

## Expected Result

The patch deployment is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Critical security patches are applied within 72 hours of release.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-015 document ID and the relevant ticket/request number.

## Responsible Role

DevOps Engineer

## Approval Role

Security Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._