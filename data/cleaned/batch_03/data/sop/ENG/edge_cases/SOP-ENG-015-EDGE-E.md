# Edge Case: Feature Flag Rollout Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-ENG-015-EDGE-E",
  "title": "Edge Case: Feature Flag Rollout Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Release Management",
  "subcategory": "Feature Flag",
  "roles": [
    "Software Engineer",
    "Product Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Feature Flag Rollout Procedure",
    "edge case",
    "exception",
    "ENG"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Product Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-ENG-015"
}
```

**Document ID:** SOP-ENG-015-EDGE-E
**Related SOP:** SOP-ENG-015 (Feature Flag Rollout Procedure)
**Department:** Software Engineering / Development

## Situation
Software Engineer submits a feature flag request in MK-CodeForge that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Product Manager reviewing the request in MK-CodeForge notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Product Manager decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Product Manager does not approve or silently correct the request themselves; they return it to Software Engineer in MK-CodeForge with a specific note on what's missing or wrong.
2. Software Engineer is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Software Engineer corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Product Manager reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Product Manager flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-ENG-015.

## Responsible Role
Software Engineer

## Approval
Product Manager

## Escalation
Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

## Expected Result
Incomplete or incorrect feature flag requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._