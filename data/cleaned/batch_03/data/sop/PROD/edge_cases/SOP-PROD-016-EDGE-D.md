# Edge Case: Product Risk & Compliance Review — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-PROD-016-EDGE-D",
  "title": "Edge Case: Product Risk & Compliance Review \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Compliance",
  "subcategory": "Product Compliance Review",
  "roles": [
    "Product Manager",
    "Legal Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Product Risk & Compliance Review",
    "edge case",
    "exception",
    "PROD"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Legal Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROD-016"
}
```

**Document ID:** SOP-PROD-016-EDGE-D
**Related SOP:** SOP-PROD-016 (Product Risk & Compliance Review)
**Department:** Product Management

## Situation
A product compliance review request is rejected by the Legal Manager, or Product Manager accidentally submits the same request twice in MK-ProductHub.

## Detection
MK-ProductHub shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Legal Manager (for rejections) or MK-ProductHub itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Legal Manager records a specific rejection reason in MK-ProductHub — a bare 'Rejected' status without a reason is not acceptable practice.
2. Product Manager reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Product Manager disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Associate Product Manager -> Product Manager -> Product Lead -> Head of Product) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-ProductHub flags the second entry automatically; the Product Manager or Legal Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Legal Manager initiates the standard reversal process instead of just closing the record.
6. MK-ProductHub retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Product Manager

## Approval
Legal Manager

## Escalation
Associate Product Manager -> Product Manager -> Product Lead -> Head of Product

## Expected Result
Rejections always carry a documented reason and a clear next step for Product Manager, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._