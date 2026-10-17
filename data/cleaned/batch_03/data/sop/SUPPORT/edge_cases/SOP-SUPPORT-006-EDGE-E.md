# Edge Case: Knowledge Base Article Creation Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-SUPPORT-006-EDGE-E",
  "title": "Edge Case: Knowledge Base Article Creation Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Knowledge Management",
  "subcategory": "KB Article",
  "roles": [
    "Senior Support Associate",
    "Support Team Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Knowledge Base Article Creation Procedure",
    "edge case",
    "exception",
    "SUPPORT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Support Team Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-SUPPORT-006"
}
```

**Document ID:** SOP-SUPPORT-006-EDGE-E
**Related SOP:** SOP-SUPPORT-006 (Knowledge Base Article Creation Procedure)
**Department:** Customer Support / Helpdesk

## Situation
Senior Support Associate submits a kb article request in MK-SupportDesk that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Support Team Lead reviewing the request in MK-SupportDesk notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Support Team Lead decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Support Team Lead does not approve or silently correct the request themselves; they return it to Senior Support Associate in MK-SupportDesk with a specific note on what's missing or wrong.
2. Senior Support Associate is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Senior Support Associate corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Support Team Lead reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Support Team Lead flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-SUPPORT-006.

## Responsible Role
Senior Support Associate

## Approval
Support Team Lead

## Escalation
Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director

## Expected Result
Incomplete or incorrect kb article requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._