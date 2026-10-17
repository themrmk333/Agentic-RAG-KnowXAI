# Edge Case: Customer Reference Request Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-SALES-011-EDGE-E",
  "title": "Edge Case: Customer Reference Request Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Sales",
  "department_code": "SALES",
  "category": "Customer References",
  "subcategory": "Reference Request",
  "roles": [
    "Account Executive",
    "Marketing Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Customer Reference Request Procedure",
    "edge case",
    "exception",
    "SALES"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Marketing Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SALES-011"
}
```

**Document ID:** SOP-SALES-011-EDGE-E  
**Related SOP:** SOP-SALES-011 (Customer Reference Request Procedure)  
**Department:** Sales

## Situation
Account Executive submits a reference request request in MK-CRM that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Marketing Manager reviewing the request in MK-CRM notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Marketing Manager decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Marketing Manager does not approve or silently correct the request themselves; they return it to Account Executive in MK-CRM with a specific note on what's missing or wrong.
2. Account Executive is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Account Executive corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Marketing Manager reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Marketing Manager flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-SALES-011.

## Responsible Role
Account Executive

## Approval
Marketing Manager

## Escalation
Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director

## Expected Result
Incomplete or incorrect reference request requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._