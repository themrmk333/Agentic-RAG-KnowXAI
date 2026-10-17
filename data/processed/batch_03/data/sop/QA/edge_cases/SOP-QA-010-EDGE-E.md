# Edge Case: Mobile App Testing Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-QA-010-EDGE-E",
  "title": "Edge Case: Mobile App Testing Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Test Execution",
  "subcategory": "Mobile Test Pass",
  "roles": [
    "QA Engineer",
    "QA Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Mobile App Testing Procedure",
    "edge case",
    "exception",
    "QA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "QA Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-QA-010"
}
```

**Document ID:** SOP-QA-010-EDGE-E  
**Related SOP:** SOP-QA-010 (Mobile App Testing Procedure)  
**Department:** QA / Testing

## Situation
QA Engineer submits a mobile test pass request in MK-TestHub that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The QA Lead reviewing the request in MK-TestHub notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The QA Lead decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The QA Lead does not approve or silently correct the request themselves; they return it to QA Engineer in MK-TestHub with a specific note on what's missing or wrong.
2. QA Engineer is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. QA Engineer corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The QA Lead reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the QA Lead flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-QA-010.

## Responsible Role
QA Engineer

## Approval
QA Lead

## Escalation
QA Engineer -> QA Lead -> QA Manager -> QA Director

## Expected Result
Incomplete or incorrect mobile test pass requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._