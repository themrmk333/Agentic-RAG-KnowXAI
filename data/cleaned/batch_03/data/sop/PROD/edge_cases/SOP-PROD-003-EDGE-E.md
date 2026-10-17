# Edge Case: Customer Feedback Intake and Triage — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-PROD-003-EDGE-E",
  "title": "Edge Case: Customer Feedback Intake and Triage \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Customer Insight",
  "subcategory": "Feedback Log",
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
    "Customer Feedback Intake and Triage",
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
  "related_sop": "SOP-PROD-003"
}
```

**Document ID:** SOP-PROD-003-EDGE-E
**Related SOP:** SOP-PROD-003 (Customer Feedback Intake and Triage)
**Department:** Product Management

## Situation
Product Manager submits a feedback log request in MK-ProductHub that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Product Lead reviewing the request in MK-ProductHub notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Product Lead decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Product Lead does not approve or silently correct the request themselves; they return it to Product Manager in MK-ProductHub with a specific note on what's missing or wrong.
2. Product Manager is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Product Manager corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Product Lead reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Product Lead flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-PROD-003.

## Responsible Role
Product Manager

## Approval
Product Lead

## Escalation
Associate Product Manager -> Product Manager -> Product Lead -> Head of Product

## Expected Result
Incomplete or incorrect feedback log requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._