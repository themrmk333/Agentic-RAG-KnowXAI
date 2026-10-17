# Edge Case: Support Quality Audit Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-SUPPORT-014-EDGE-E",
  "title": "Edge Case: Support Quality Audit Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Quality Assurance",
  "subcategory": "Quality Audit",
  "roles": [
    "Support Manager",
    "Customer Experience Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Support Quality Audit Procedure",
    "edge case",
    "exception",
    "SUPPORT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Customer Experience Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-SUPPORT-014"
}
```

**Document ID:** SOP-SUPPORT-014-EDGE-E  
**Related SOP:** SOP-SUPPORT-014 (Support Quality Audit Procedure)  
**Department:** Customer Support / Helpdesk

## Situation
Support Manager submits a quality audit request in MK-SupportDesk that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Customer Experience Director reviewing the request in MK-SupportDesk notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Customer Experience Director decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Customer Experience Director does not approve or silently correct the request themselves; they return it to Support Manager in MK-SupportDesk with a specific note on what's missing or wrong.
2. Support Manager is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Support Manager corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Customer Experience Director reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Customer Experience Director flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-SUPPORT-014.

## Responsible Role
Support Manager

## Approval
Customer Experience Director

## Escalation
Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director

## Expected Result
Incomplete or incorrect quality audit requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._