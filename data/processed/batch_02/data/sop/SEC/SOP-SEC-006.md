# SOP: Data Loss Prevention (DLP) Alert Handling

```json
{
  "document_id": "SOP-SEC-006",
  "title": "Data Loss Prevention (DLP) Alert Handling",
  "document_type": "SOP",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Data Protection",
  "subcategory": "DLP Alert",
  "roles": [
    "Security Analyst",
    "Security Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Loss Prevention (DLP) Alert Handling",
    "Data Protection",
    "DLP Alert",
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

**Document ID:** SOP-SEC-006  
**Department:** Cybersecurity / Information Security  
**Applicable Roles:** Security Analyst, Security Manager  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **data loss prevention (dlp) alert handling** within the Cybersecurity / Information Security department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Security Analysts and any employee across MK-Infinite-AI who needs to initiate a **DLP Alert** request. It covers the full workflow from initiation through to closure in MK-SecGuard.

## Applicable Roles

- Primary actor: **Security Analyst**
- Approver: **Security Manager**
- System of record: **MK-SecGuard**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-SecGuard.
- Reviewing the flagged content and confirming whether it is a genuine policy violation must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the dlp alert being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several.

**Step 2:** the Security Analyst performs the standard first-line check: reviewing the flagged content and confirming whether it is a genuine policy violation.

**Step 3:** If the issue persists, the Security Analyst applies the documented workaround for this issue type.

**Step 4:** the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too.

**Step 5:** If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'DLP Alert', attaching screenshots or error logs.

**Step 6:** The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.

**Step 7:** the Security Analyst confirms the fix works; the ticket is closed in MK-SecGuard with the root cause logged. Confirmed sensitive data exfiltration is escalated to Legal and HR immediately.

## Expected Result

The dlp alert is completed, logged in MK-SecGuard, and the requester is notified of the outcome. The record remains available in MK-SecGuard for future reference and audit.

## Exceptions

- Confirmed sensitive data exfiltration is escalated to Legal and HR immediately.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Security Analyst → Incident Response Lead → Security Manager → CISO. Escalations should reference the SOP-SEC-006 document ID and the relevant ticket/request number.

## Responsible Role

Security Analyst

## Approval Role

Security Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._