# SOP: Service Deployment Procedure

```json
{
  "document_id": "SOP-DEVOPS-001",
  "title": "Service Deployment Procedure",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Deployment",
  "subcategory": "Deployment",
  "roles": [
    "DevOps Engineer",
    "DevOps Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Service Deployment Procedure",
    "Deployment",
    "Deployment",
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

**Document ID:** SOP-DEVOPS-001
**Department:** DevOps & Cloud
**Applicable Roles:** DevOps Engineer, DevOps Manager
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **service deployment procedure** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all DevOps Engineers and any employee across MK-Infinite-AI who needs to initiate a **Deployment** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **DevOps Engineer**
- Approver: **DevOps Manager**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Verifying the build passed all MK-CI pipeline gates must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the deployment being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the DevOps Engineer confirms eligibility and prerequisites: verifying the build passed all MK-CI pipeline gates.

**Step 2:** the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Deployment is required.

**Step 3:** The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Deployment in the relevant system.

**Step 5:** the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.

**Step 7:** MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Production deployments outside business hours require prior sign-off.

## Expected Result

The deployment is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Production deployments outside business hours require prior sign-off.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-001 document ID and the relevant ticket/request number.

## Responsible Role

DevOps Engineer

## Approval Role

DevOps Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._