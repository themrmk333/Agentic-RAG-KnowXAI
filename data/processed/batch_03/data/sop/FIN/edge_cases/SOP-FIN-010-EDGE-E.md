# Edge Case: Tax Compliance and Filing Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-FIN-010-EDGE-E",
  "title": "Edge Case: Tax Compliance and Filing Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Finance & Accounting",
  "department_code": "FIN",
  "category": "Tax & Compliance",
  "subcategory": "Tax Filing",
  "roles": [
    "Senior Accountant",
    "Finance Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Tax Compliance and Filing Procedure",
    "edge case",
    "exception",
    "FIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-FIN-010"
}
```

**Document ID:** SOP-FIN-010-EDGE-E  
**Related SOP:** SOP-FIN-010 (Tax Compliance and Filing Procedure)  
**Department:** Finance & Accounting

## Situation
Senior Accountant submits a tax filing request in MK-Finance360 that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Finance Director reviewing the request in MK-Finance360 notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Finance Director decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Finance Director does not approve or silently correct the request themselves; they return it to Senior Accountant in MK-Finance360 with a specific note on what's missing or wrong.
2. Senior Accountant is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Senior Accountant corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Finance Director reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Finance Director flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-FIN-010.

## Responsible Role
Senior Accountant

## Approval
Finance Director

## Escalation
Accountant -> Finance Lead -> Finance Manager -> Finance Director

## Expected Result
Incomplete or incorrect tax filing requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._