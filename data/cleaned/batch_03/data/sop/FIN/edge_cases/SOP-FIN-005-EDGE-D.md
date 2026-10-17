# Edge Case: Vendor Payment Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-FIN-005-EDGE-D",
  "title": "Edge Case: Vendor Payment Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Finance & Accounting",
  "department_code": "FIN",
  "category": "Accounts Payable",
  "subcategory": "Vendor Payment",
  "roles": [
    "Accountant",
    "Finance Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Vendor Payment Procedure",
    "edge case",
    "exception",
    "FIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-FIN-005"
}
```

**Document ID:** SOP-FIN-005-EDGE-D
**Related SOP:** SOP-FIN-005 (Vendor Payment Procedure)
**Department:** Finance & Accounting

## Situation
A vendor payment request is rejected by the Finance Manager, or Accountant accidentally submits the same request twice in MK-Finance360.

## Detection
MK-Finance360 shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Finance Manager (for rejections) or MK-Finance360 itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Finance Manager records a specific rejection reason in MK-Finance360 — a bare 'Rejected' status without a reason is not acceptable practice.
2. Accountant reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Accountant disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Accountant -> Finance Lead -> Finance Manager -> Finance Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-Finance360 flags the second entry automatically; the Accountant or Finance Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Finance Manager initiates the standard reversal process instead of just closing the record.
6. MK-Finance360 retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Accountant

## Approval
Finance Manager

## Escalation
Accountant -> Finance Lead -> Finance Manager -> Finance Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Accountant, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._