# SOP: Multi-Factor Authentication (MFA) Enrollment

```json
{
  "document_id": "SOP-SEC-002",
  "title": "Multi-Factor Authentication (MFA) Enrollment",
  "document_type": "SOP",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Access Security",
  "subcategory": "MFA Enrollment",
  "roles": [
    "employee",
    "Security Analyst"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "SEC"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Multi-Factor Authentication (MFA) Enrollment",
    "Access Security",
    "MFA Enrollment",
    "SEC",
    "MK-SecGuard"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Analyst",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-SEC-002
**Department:** Cybersecurity / Information Security
**Applicable Roles:** employee, Security Analyst
**Access Level:** employee
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **multi-factor authentication (mfa) enrollment** within the Cybersecurity / Information Security department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all employees and any employee across MK-Infinite-AI who needs to initiate a **MFA Enrollment** request. It covers the full workflow from initiation through to closure in MK-SecGuard.

## Applicable Roles

- Primary actor: **employee**
- Approver: **Security Analyst**
- System of record: **MK-SecGuard**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-SecGuard.
- Installing the MK-Authenticator app and scanning the enrollment QR code must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the mfa enrollment being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the employee confirms eligibility and prerequisites: installing the MK-Authenticator app and scanning the enrollment QR code.

**Step 2:** the employee raises a request in MK-SecGuard specifying exactly which MFA Enrollment is required.

**Step 3:** The Security Analyst reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the MFA Enrollment in the relevant system.

**Step 5:** the employee is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-SecGuard and corrected before sign-off.

**Step 7:** MK-SecGuard marks the request 'Complete' and the configuration is logged for audit and future reference. Accounts without MFA enabled after the grace period are automatically locked.

## Expected Result

The mfa enrollment is completed, logged in MK-SecGuard, and the requester is notified of the outcome. The record remains available in MK-SecGuard for future reference and audit.

## Exceptions

- Accounts without MFA enabled after the grace period are automatically locked.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Security Analyst → Incident Response Lead → Security Manager → CISO. Escalations should reference the SOP-SEC-002 document ID and the relevant ticket/request number.

## Responsible Role

employee

## Approval Role

Security Analyst

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._