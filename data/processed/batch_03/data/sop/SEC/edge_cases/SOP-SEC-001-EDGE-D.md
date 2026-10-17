# Edge Case: Phishing Email Reporting Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-SEC-001-EDGE-D",
  "title": "Edge Case: Phishing Email Reporting Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Phishing",
  "subcategory": "Phishing Report",
  "roles": [
    "employee",
    "Security Analyst"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Phishing Email Reporting Procedure",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Analyst",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-001"
}
```

**Document ID:** SOP-SEC-001-EDGE-D  
**Related SOP:** SOP-SEC-001 (Phishing Email Reporting Procedure)  
**Department:** Cybersecurity / Information Security

## Situation
A phishing report request is rejected by the Security Analyst, or employee accidentally submits the same request twice in MK-SecGuard.

## Detection
MK-SecGuard shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Security Analyst (for rejections) or MK-SecGuard itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Security Analyst records a specific rejection reason in MK-SecGuard — a bare 'Rejected' status without a reason is not acceptable practice.
2. employee reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If employee disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Security Analyst -> Incident Response Lead -> Security Manager -> CISO) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-SecGuard flags the second entry automatically; the employee or Security Analyst confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Security Analyst initiates the standard reversal process instead of just closing the record.
6. MK-SecGuard retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
employee

## Approval
Security Analyst

## Escalation
Security Analyst -> Incident Response Lead -> Security Manager -> CISO

## Expected Result
Rejections always carry a documented reason and a clear next step for employee, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._