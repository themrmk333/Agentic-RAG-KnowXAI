# Edge Case: Project Quality Gate Review — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-PMO-013-EDGE-E",
  "title": "Edge Case: Project Quality Gate Review \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Project Management / PMO",
  "department_code": "PMO",
  "category": "Quality Management",
  "subcategory": "Quality Gate",
  "roles": [
    "Project Manager",
    "QA Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Project Quality Gate Review",
    "edge case",
    "exception",
    "PMO"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "QA Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-PMO-013"
}
```

**Document ID:** SOP-PMO-013-EDGE-E
**Related SOP:** SOP-PMO-013 (Project Quality Gate Review)
**Department:** Project Management / PMO

## Situation
Project Manager submits a quality gate request in MK-PMTrack that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The QA Lead reviewing the request in MK-PMTrack notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The QA Lead decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The QA Lead does not approve or silently correct the request themselves; they return it to Project Manager in MK-PMTrack with a specific note on what's missing or wrong.
2. Project Manager is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Project Manager corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The QA Lead reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the QA Lead flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-PMO-013.

## Responsible Role
Project Manager

## Approval
QA Lead

## Escalation
Project Coordinator -> Project Manager -> PMO Lead -> PMO Director

## Expected Result
Incomplete or incorrect quality gate requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._