# Edge Case: Pricing Change Request Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-PROD-009-EDGE-E",
  "title": "Edge Case: Pricing Change Request Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Pricing",
  "subcategory": "Pricing Change Request",
  "roles": [
    "Product Manager",
    "VP Product"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Pricing Change Request Procedure",
    "edge case",
    "exception",
    "PROD"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "VP Product",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROD-009"
}
```

**Document ID:** SOP-PROD-009-EDGE-E
**Related SOP:** SOP-PROD-009 (Pricing Change Request Procedure)
**Department:** Product Management

## Situation
Product Manager submits a pricing change request request in MK-ProductHub that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The VP Product reviewing the request in MK-ProductHub notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The VP Product decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The VP Product does not approve or silently correct the request themselves; they return it to Product Manager in MK-ProductHub with a specific note on what's missing or wrong.
2. Product Manager is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Product Manager corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The VP Product reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the VP Product flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-PROD-009.

## Responsible Role
Product Manager

## Approval
VP Product

## Escalation
Associate Product Manager -> Product Manager -> Product Lead -> Head of Product

## Expected Result
Incomplete or incorrect pricing change request requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._