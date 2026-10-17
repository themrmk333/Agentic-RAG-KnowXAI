# Edge Case: Marketing Qualified Lead (MQL) Handover to Sales — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-MKT-005-EDGE-D",
  "title": "Edge Case: Marketing Qualified Lead (MQL) Handover to Sales \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Marketing",
  "department_code": "MKT",
  "category": "Lead Generation",
  "subcategory": "MQL Handover",
  "roles": [
    "Marketing Specialist",
    "Sales Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Marketing Qualified Lead (MQL) Handover to Sales",
    "edge case",
    "exception",
    "MKT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Sales Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-MKT-005"
}
```

**Document ID:** SOP-MKT-005-EDGE-D  
**Related SOP:** SOP-MKT-005 (Marketing Qualified Lead (MQL) Handover to Sales)  
**Department:** Marketing

## Situation
A mql handover request is rejected by the Sales Manager, or Marketing Specialist accidentally submits the same request twice in MK-MarketHub.

## Detection
MK-MarketHub shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Sales Manager (for rejections) or MK-MarketHub itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Sales Manager records a specific rejection reason in MK-MarketHub — a bare 'Rejected' status without a reason is not acceptable practice.
2. Marketing Specialist reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Marketing Specialist disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-MarketHub flags the second entry automatically; the Marketing Specialist or Sales Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Sales Manager initiates the standard reversal process instead of just closing the record.
6. MK-MarketHub retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Marketing Specialist

## Approval
Sales Manager

## Escalation
Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Marketing Specialist, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._