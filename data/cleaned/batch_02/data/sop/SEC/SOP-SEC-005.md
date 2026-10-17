# SOP: Vulnerability Scanning and Remediation

```json
{
  "document_id": "SOP-SEC-005",
  "title": "Vulnerability Scanning and Remediation",
  "document_type": "SOP",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Vulnerability Management",
  "subcategory": "Vulnerability Scan Report",
  "roles": [
    "Security Engineer",
    "Security Manager"
  ],
  "access_level": "manager",
  "allowed_departments": [
    "SEC"
  ],
  "confidentiality": "Confidential",
  "keywords": [
    "Vulnerability Scanning and Remediation",
    "Vulnerability Management",
    "Vulnerability Scan Report",
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

**Document ID:** SOP-SEC-005
**Department:** Cybersecurity / Information Security
**Applicable Roles:** Security Engineer, Security Manager
**Access Level:** manager
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **vulnerability scanning and remediation** within the Cybersecurity / Information Security department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Security Engineers and any employee across MK-Infinite-AI who needs to initiate a **Vulnerability Scan Report** request. It covers the full workflow from initiation through to closure in MK-SecGuard.

## Applicable Roles

- Primary actor: **Security Engineer**
- Approver: **Security Manager**
- System of record: **MK-SecGuard**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-SecGuard.
- Scanning production and staging environments on the scheduled cadence must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the vulnerability scan report being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** The review is scheduled in advance and stakeholders are notified through MK-SecGuard.

**Step 2:** the Security Engineer gathers the required data and documents, including scanning production and staging environments on the scheduled cadence.

**Step 3:** The review team examines the Vulnerability Scan Report against the applicable policy or checklist.

**Step 4:** Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.

**Step 5:** The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Step 6:** Remediation actions are tracked in MK-SecGuard with due dates and status.

**Step 7:** The review is closed once all actions are completed, and the outcome is recorded for future audits. Critical vulnerabilities must be remediated within 7 days per policy.

## Expected Result

The vulnerability scan report is completed, logged in MK-SecGuard, and the requester is notified of the outcome. The record remains available in MK-SecGuard for future reference and audit.

## Exceptions

- Critical vulnerabilities must be remediated within 7 days per policy.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Security Analyst → Incident Response Lead → Security Manager → CISO. Escalations should reference the SOP-SEC-005 document ID and the relevant ticket/request number.

## Responsible Role

Security Engineer

## Approval Role

Security Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._