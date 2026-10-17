# SOP: Firewall / Network Access Change Request

```json
{
  "document_id": "SOP-SEC-010",
  "title": "Firewall / Network Access Change Request",
  "document_type": "SOP",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Network Security",
  "subcategory": "Firewall Change Request",
  "roles": [
    "requester",
    "Security Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Firewall / Network Access Change Request",
    "Network Security",
    "Firewall Change Request",
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

**Document ID:** SOP-SEC-010  
**Department:** Cybersecurity / Information Security  
**Applicable Roles:** requester, Security Manager  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **firewall / network access change request** within the Cybersecurity / Information Security department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all requesters and any employee across MK-Infinite-AI who needs to initiate a **Firewall Change Request** request. It covers the full workflow from initiation through to closure in MK-SecGuard.

## Applicable Roles

- Primary actor: **requester**
- Approver: **Security Manager**
- System of record: **MK-SecGuard**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-SecGuard.
- Source, destination, port, and business justification must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the firewall change request being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the requester logs into MK-SecGuard and navigates to the 'Firewall Change Request' section.

**Step 2:** the requester selects 'New Firewall Change Request' and enters the required details, including source, destination, port, and business justification.

**Step 3:** the requester attaches any supporting documentation and reviews the entry for accuracy before submitting.

**Step 4:** the requester submits the Firewall Change Request; MK-SecGuard automatically routes it to the Security Manager for review.

**Step 5:** The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Step 6:** On approval, MK-SecGuard updates the status to 'Approved' and notifies the requester by email/in-app notification.

**Step 7:** The approved Firewall Change Request is processed and the record is retained in MK-SecGuard for audit purposes. Overly broad rules (any-any) are rejected by default.

## Expected Result

The firewall change request is completed, logged in MK-SecGuard, and the requester is notified of the outcome. The record remains available in MK-SecGuard for future reference and audit.

## Exceptions

- Overly broad rules (any-any) are rejected by default.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Security Analyst → Incident Response Lead → Security Manager → CISO. Escalations should reference the SOP-SEC-010 document ID and the relevant ticket/request number.

## Responsible Role

requester

## Approval Role

Security Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._