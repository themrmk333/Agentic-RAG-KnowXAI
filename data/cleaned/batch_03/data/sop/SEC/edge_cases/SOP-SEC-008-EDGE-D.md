# Edge Case: Security Awareness Training Assignment — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-SEC-008-EDGE-D",
  "title": "Edge Case: Security Awareness Training Assignment \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Training",
  "subcategory": "Training Assignment",
  "roles": [
    "Security Analyst",
    "HR Business Partner"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Security Awareness Training Assignment",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "HR Business Partner",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-008"
}
```

**Document ID:** SOP-SEC-008-EDGE-D
**Related SOP:** SOP-SEC-008 (Security Awareness Training Assignment)
**Department:** Cybersecurity / Information Security

## Situation
A training assignment request is rejected by the HR Business Partner, or Security Analyst accidentally submits the same request twice in MK-SecGuard.

## Detection
MK-SecGuard shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The HR Business Partner (for rejections) or MK-SecGuard itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the HR Business Partner records a specific rejection reason in MK-SecGuard — a bare 'Rejected' status without a reason is not acceptable practice.
2. Security Analyst reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Security Analyst disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Security Analyst -> Incident Response Lead -> Security Manager -> CISO) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-SecGuard flags the second entry automatically; the Security Analyst or HR Business Partner confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the HR Business Partner initiates the standard reversal process instead of just closing the record.
6. MK-SecGuard retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Security Analyst

## Approval
HR Business Partner

## Escalation
Security Analyst -> Incident Response Lead -> Security Manager -> CISO

## Expected Result
Rejections always carry a documented reason and a clear next step for Security Analyst, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._