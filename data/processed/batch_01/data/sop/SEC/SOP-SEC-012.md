# SOP: Data Classification and Labeling

```json
{
  "document_id": "SOP-SEC-012",
  "title": "Data Classification and Labeling",
  "document_type": "SOP",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Data Protection",
  "subcategory": "Data Classification",
  "roles": [
    "data owner",
    "Security Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Classification and Labeling",
    "Data Protection",
    "Data Classification",
    "SEC",
    "MK-SecGuard"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-SEC-012  
**Department:** Cybersecurity / Information Security  
**Applicable Roles:** data owner, Security Manager  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **data classification and labeling** within the Cybersecurity / Information Security department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all data owners and any employee across MK-Infinite-AI who needs to initiate a **Data Classification** request. It covers the full workflow from initiation through to closure in MK-SecGuard.

## Applicable Roles

- Primary actor: **data owner**
- Approver: **Security Manager**
- System of record: **MK-SecGuard**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-SecGuard.
- Applying the correct label (Public, Internal, Confidential, Restricted) must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the data classification being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the data owner confirms eligibility and prerequisites: applying the correct label (Public, Internal, Confidential, Restricted).

**Step 2:** the data owner raises a request in MK-SecGuard specifying exactly which Data Classification is required.

**Step 3:** The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Data Classification in the relevant system.

**Step 5:** the data owner is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-SecGuard and corrected before sign-off.

**Step 7:** MK-SecGuard marks the request 'Complete' and the configuration is logged for audit and future reference. Mislabeled Restricted data found during audit is reported as a policy violation.

## Expected Result

The data classification is completed, logged in MK-SecGuard, and the requester is notified of the outcome. The record remains available in MK-SecGuard for future reference and audit.

## Exceptions

- Mislabeled Restricted data found during audit is reported as a policy violation.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Security Analyst → Incident Response Lead → Security Manager → CISO. Escalations should reference the SOP-SEC-012 document ID and the relevant ticket/request number.

## Responsible Role

data owner

## Approval Role

Security Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._