# Edge Case: Cross-functional Product Sync Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-PROD-011-EDGE-D",
  "title": "Edge Case: Cross-functional Product Sync Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Collaboration",
  "subcategory": "Product Sync Meeting",
  "roles": [
    "Product Manager",
    "Product Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Cross-functional Product Sync Procedure",
    "edge case",
    "exception",
    "PROD"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Product Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROD-011"
}
```

**Document ID:** SOP-PROD-011-EDGE-D  
**Related SOP:** SOP-PROD-011 (Cross-functional Product Sync Procedure)  
**Department:** Product Management

## Situation
A product sync meeting request is rejected by the Product Lead, or Product Manager accidentally submits the same request twice in MK-ProductHub.

## Detection
MK-ProductHub shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Product Lead (for rejections) or MK-ProductHub itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Product Lead records a specific rejection reason in MK-ProductHub — a bare 'Rejected' status without a reason is not acceptable practice.
2. Product Manager reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Product Manager disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Associate Product Manager -> Product Manager -> Product Lead -> Head of Product) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-ProductHub flags the second entry automatically; the Product Manager or Product Lead confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Product Lead initiates the standard reversal process instead of just closing the record.
6. MK-ProductHub retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Product Manager

## Approval
Product Lead

## Escalation
Associate Product Manager -> Product Manager -> Product Lead -> Head of Product

## Expected Result
Rejections always carry a documented reason and a clear next step for Product Manager, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._