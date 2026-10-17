# Edge Case: Tax Compliance and Filing Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-FIN-010-EDGE-D",
  "title": "Edge Case: Tax Compliance and Filing Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Finance & Accounting",
  "department_code": "FIN",
  "category": "Tax & Compliance",
  "subcategory": "Tax Filing",
  "roles": [
    "Senior Accountant",
    "Finance Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Tax Compliance and Filing Procedure",
    "edge case",
    "exception",
    "FIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-FIN-010"
}
```

**Document ID:** SOP-FIN-010-EDGE-D
**Related SOP:** SOP-FIN-010 (Tax Compliance and Filing Procedure)
**Department:** Finance & Accounting

## Situation
A tax filing request is rejected by the Finance Director, or Senior Accountant accidentally submits the same request twice in MK-Finance360.

## Detection
MK-Finance360 shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Finance Director (for rejections) or MK-Finance360 itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Finance Director records a specific rejection reason in MK-Finance360 — a bare 'Rejected' status without a reason is not acceptable practice.
2. Senior Accountant reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Senior Accountant disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Accountant -> Finance Lead -> Finance Manager -> Finance Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-Finance360 flags the second entry automatically; the Senior Accountant or Finance Director confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Finance Director initiates the standard reversal process instead of just closing the record.
6. MK-Finance360 retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Senior Accountant

## Approval
Finance Director

## Escalation
Accountant -> Finance Lead -> Finance Manager -> Finance Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Senior Accountant, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._