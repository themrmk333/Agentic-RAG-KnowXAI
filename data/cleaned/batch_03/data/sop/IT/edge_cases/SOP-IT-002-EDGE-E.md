# Edge Case: New Hardware Request Fulfillment — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-IT-002-EDGE-E",
  "title": "Edge Case: New Hardware Request Fulfillment \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "IT Support / Information Technology",
  "department_code": "IT",
  "category": "Hardware",
  "subcategory": "Hardware Request",
  "roles": [
    "employee",
    "IT Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "New Hardware Request Fulfillment",
    "edge case",
    "exception",
    "IT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "IT Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-IT-002"
}
```

**Document ID:** SOP-IT-002-EDGE-E
**Related SOP:** SOP-IT-002 (New Hardware Request Fulfillment)
**Department:** IT Support / Information Technology

## Situation
employee submits a hardware request request in MK-ServiceDesk that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The IT Manager reviewing the request in MK-ServiceDesk notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The IT Manager decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The IT Manager does not approve or silently correct the request themselves; they return it to employee in MK-ServiceDesk with a specific note on what's missing or wrong.
2. employee is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. employee corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The IT Manager reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the IT Manager flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-IT-002.

## Responsible Role
employee

## Approval
IT Manager

## Escalation
IT Support Engineer -> IT Manager -> IT Director

## Expected Result
Incomplete or incorrect hardware request requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._