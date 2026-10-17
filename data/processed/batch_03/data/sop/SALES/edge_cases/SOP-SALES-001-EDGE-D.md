# Edge Case: New Lead Qualification Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-SALES-001-EDGE-D",
  "title": "Edge Case: New Lead Qualification Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Sales",
  "department_code": "SALES",
  "category": "Lead Management",
  "subcategory": "Lead Qualification",
  "roles": [
    "Sales Development Representative",
    "Sales Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "New Lead Qualification Procedure",
    "edge case",
    "exception",
    "SALES"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Sales Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SALES-001"
}
```

**Document ID:** SOP-SALES-001-EDGE-D  
**Related SOP:** SOP-SALES-001 (New Lead Qualification Procedure)  
**Department:** Sales

## Situation
A lead qualification request is rejected by the Sales Manager, or Sales Development Representative accidentally submits the same request twice in MK-CRM.

## Detection
MK-CRM shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Sales Manager (for rejections) or MK-CRM itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Sales Manager records a specific rejection reason in MK-CRM — a bare 'Rejected' status without a reason is not acceptable practice.
2. Sales Development Representative reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Sales Development Representative disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-CRM flags the second entry automatically; the Sales Development Representative or Sales Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Sales Manager initiates the standard reversal process instead of just closing the record.
6. MK-CRM retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Sales Development Representative

## Approval
Sales Manager

## Escalation
Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Sales Development Representative, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._