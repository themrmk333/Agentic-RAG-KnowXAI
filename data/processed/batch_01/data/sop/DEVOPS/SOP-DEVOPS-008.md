# SOP: Secrets and Credentials Management

```json
{
  "document_id": "SOP-DEVOPS-008",
  "title": "Secrets and Credentials Management",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Security",
  "subcategory": "Secrets Vault Entry",
  "roles": [
    "DevOps Engineer",
    "Security Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "DEVOPS"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Secrets and Credentials Management",
    "Security",
    "Secrets Vault Entry",
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

**Document ID:** SOP-DEVOPS-008  
**Department:** DevOps & Cloud  
**Applicable Roles:** DevOps Engineer, Security Manager  
**Access Level:** employee  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **secrets and credentials management** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all DevOps Engineers and any employee across MK-Infinite-AI who needs to initiate a **Secrets Vault Entry** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **DevOps Engineer**
- Approver: **Security Manager**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Storing the credential in the approved MK-CloudOps secrets vault only must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the secrets vault entry being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only.

**Step 2:** the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required.

**Step 3:** The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system.

**Step 5:** the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.

**Step 7:** MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Secrets are never stored in plaintext configuration files.

## Expected Result

The secrets vault entry is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Secrets are never stored in plaintext configuration files.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-008 document ID and the relevant ticket/request number.

## Responsible Role

DevOps Engineer

## Approval Role

Security Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._