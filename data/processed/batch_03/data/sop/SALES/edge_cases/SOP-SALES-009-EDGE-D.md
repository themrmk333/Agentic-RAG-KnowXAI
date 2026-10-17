# Edge Case: Competitive Deal Support Request — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-SALES-009-EDGE-D",
  "title": "Edge Case: Competitive Deal Support Request \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Sales",
  "department_code": "SALES",
  "category": "Competitive Intelligence",
  "subcategory": "Competitive Intel Request",
  "roles": [
    "Account Executive",
    "Product Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Competitive Deal Support Request",
    "edge case",
    "exception",
    "SALES"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Product Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SALES-009"
}
```

**Document ID:** SOP-SALES-009-EDGE-D  
**Related SOP:** SOP-SALES-009 (Competitive Deal Support Request)  
**Department:** Sales

## Situation
A competitive intel request request is rejected by the Product Manager, or Account Executive accidentally submits the same request twice in MK-CRM.

## Detection
MK-CRM shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Product Manager (for rejections) or MK-CRM itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Product Manager records a specific rejection reason in MK-CRM — a bare 'Rejected' status without a reason is not acceptable practice.
2. Account Executive reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Account Executive disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-CRM flags the second entry automatically; the Account Executive or Product Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Product Manager initiates the standard reversal process instead of just closing the record.
6. MK-CRM retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Account Executive

## Approval
Product Manager

## Escalation
Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Account Executive, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._