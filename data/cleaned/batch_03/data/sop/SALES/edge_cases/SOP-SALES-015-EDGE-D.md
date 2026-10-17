# Edge Case: Key Account Planning Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-SALES-015-EDGE-D",
  "title": "Edge Case: Key Account Planning Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Sales",
  "department_code": "SALES",
  "category": "Account Management",
  "subcategory": "Account Plan",
  "roles": [
    "Senior Account Executive",
    "Sales Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Key Account Planning Procedure",
    "edge case",
    "exception",
    "SALES"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Sales Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-SALES-015"
}
```

**Document ID:** SOP-SALES-015-EDGE-D
**Related SOP:** SOP-SALES-015 (Key Account Planning Procedure)
**Department:** Sales

## Situation
A account plan request is rejected by the Sales Director, or Senior Account Executive accidentally submits the same request twice in MK-CRM.

## Detection
MK-CRM shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Sales Director (for rejections) or MK-CRM itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Sales Director records a specific rejection reason in MK-CRM — a bare 'Rejected' status without a reason is not acceptable practice.
2. Senior Account Executive reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Senior Account Executive disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-CRM flags the second entry automatically; the Senior Account Executive or Sales Director confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Sales Director initiates the standard reversal process instead of just closing the record.
6. MK-CRM retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Senior Account Executive

## Approval
Sales Director

## Escalation
Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Senior Account Executive, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._