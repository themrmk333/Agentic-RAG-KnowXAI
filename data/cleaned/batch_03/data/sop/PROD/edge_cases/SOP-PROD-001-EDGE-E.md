# Edge Case: Product Requirement Document (PRD) Creation — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-PROD-001-EDGE-E",
  "title": "Edge Case: Product Requirement Document (PRD) Creation \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Product Planning",
  "subcategory": "PRD",
  "roles": [
    "Product Manager",
    "Head of Product"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Product Requirement Document (PRD) Creation",
    "edge case",
    "exception",
    "PROD"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Head of Product",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROD-001"
}
```

**Document ID:** SOP-PROD-001-EDGE-E
**Related SOP:** SOP-PROD-001 (Product Requirement Document (PRD) Creation)
**Department:** Product Management

## Situation
Product Manager submits a prd request in MK-ProductHub that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Head of Product reviewing the request in MK-ProductHub notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Head of Product decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Head of Product does not approve or silently correct the request themselves; they return it to Product Manager in MK-ProductHub with a specific note on what's missing or wrong.
2. Product Manager is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Product Manager corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Head of Product reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Head of Product flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-PROD-001.

## Responsible Role
Product Manager

## Approval
Head of Product

## Escalation
Associate Product Manager -> Product Manager -> Product Lead -> Head of Product

## Expected Result
Incomplete or incorrect prd requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._