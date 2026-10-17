# Edge Case: Privileged Access Management (PAM) Request — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-SEC-014-EDGE-D",
  "title": "Edge Case: Privileged Access Management (PAM) Request \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Access Control",
  "subcategory": "Privileged Access Request",
  "roles": [
    "requester",
    "Security Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Privileged Access Management (PAM) Request",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-014"
}
```

**Document ID:** SOP-SEC-014-EDGE-D  
**Related SOP:** SOP-SEC-014 (Privileged Access Management (PAM) Request)  
**Department:** Cybersecurity / Information Security

## Situation
A privileged access request request is rejected by the Security Manager, or requester accidentally submits the same request twice in MK-SecGuard.

## Detection
MK-SecGuard shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Security Manager (for rejections) or MK-SecGuard itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Security Manager records a specific rejection reason in MK-SecGuard — a bare 'Rejected' status without a reason is not acceptable practice.
2. requester reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If requester disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Security Analyst -> Incident Response Lead -> Security Manager -> CISO) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-SecGuard flags the second entry automatically; the requester or Security Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Security Manager initiates the standard reversal process instead of just closing the record.
6. MK-SecGuard retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
requester

## Approval
Security Manager

## Escalation
Security Analyst -> Incident Response Lead -> Security Manager -> CISO

## Expected Result
Rejections always carry a documented reason and a clear next step for requester, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._