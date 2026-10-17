# SOP: Container Image Build and Publish

```json
{
  "document_id": "SOP-DEVOPS-010",
  "title": "Container Image Build and Publish",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Containers",
  "subcategory": "Container Image",
  "roles": [
    "DevOps Engineer",
    "Tech Lead"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Container Image Build and Publish",
    "Containers",
    "Container Image",
    "DEVOPS",
    "MK-CloudOps"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Tech Lead",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DEVOPS-010
**Department:** DevOps & Cloud
**Applicable Roles:** DevOps Engineer, Tech Lead
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **container image build and publish** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all DevOps Engineers and any employee across MK-Infinite-AI who needs to initiate a **Container Image** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **DevOps Engineer**
- Approver: **Tech Lead**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Scanning the image for vulnerabilities before publishing to the registry must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the container image being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry.

**Step 2:** the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required.

**Step 3:** The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Container Image in the relevant system.

**Step 5:** the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.

**Step 7:** MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Images with critical vulnerabilities are blocked from publishing automatically.

## Expected Result

The container image is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Images with critical vulnerabilities are blocked from publishing automatically.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-010 document ID and the relevant ticket/request number.

## Responsible Role

DevOps Engineer

## Approval Role

Tech Lead

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._