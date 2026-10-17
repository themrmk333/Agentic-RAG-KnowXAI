# Edge Case: Marketing Budget Tracking Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-MKT-008-EDGE-D",
  "title": "Edge Case: Marketing Budget Tracking Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Marketing",
  "department_code": "MKT",
  "category": "Budget Management",
  "subcategory": "Marketing Budget Tracker",
  "roles": [
    "Marketing Manager",
    "Marketing Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Marketing Budget Tracking Procedure",
    "edge case",
    "exception",
    "MKT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Marketing Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-MKT-008"
}
```

**Document ID:** SOP-MKT-008-EDGE-D
**Related SOP:** SOP-MKT-008 (Marketing Budget Tracking Procedure)
**Department:** Marketing

## Situation
A marketing budget tracker request is rejected by the Marketing Director, or Marketing Manager accidentally submits the same request twice in MK-MarketHub.

## Detection
MK-MarketHub shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Marketing Director (for rejections) or MK-MarketHub itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Marketing Director records a specific rejection reason in MK-MarketHub — a bare 'Rejected' status without a reason is not acceptable practice.
2. Marketing Manager reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Marketing Manager disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-MarketHub flags the second entry automatically; the Marketing Manager or Marketing Director confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Marketing Director initiates the standard reversal process instead of just closing the record.
6. MK-MarketHub retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Marketing Manager

## Approval
Marketing Director

## Escalation
Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Marketing Manager, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._