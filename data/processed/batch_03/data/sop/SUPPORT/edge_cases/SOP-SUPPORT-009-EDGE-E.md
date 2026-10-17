# Edge Case: Customer Onboarding Support Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-SUPPORT-009-EDGE-E",
  "title": "Edge Case: Customer Onboarding Support Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Customer Onboarding",
  "subcategory": "Customer Onboarding Session",
  "roles": [
    "Customer Support Associate",
    "Support Team Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Customer Onboarding Support Procedure",
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
  "related_sop": "SOP-SUPPORT-009"
}
```

**Document ID:** SOP-SUPPORT-009-EDGE-E  
**Related SOP:** SOP-SUPPORT-009 (Customer Onboarding Support Procedure)  
**Department:** Customer Support / Helpdesk

## Situation
Customer Support Associate submits a customer onboarding session request in MK-SupportDesk that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Support Team Lead reviewing the request in MK-SupportDesk notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Support Team Lead decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Support Team Lead does not approve or silently correct the request themselves; they return it to Customer Support Associate in MK-SupportDesk with a specific note on what's missing or wrong.
2. Customer Support Associate is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Customer Support Associate corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Support Team Lead reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Support Team Lead flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-SUPPORT-009.

## Responsible Role
Customer Support Associate

## Approval
Support Team Lead

## Escalation
Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director

## Expected Result
Incomplete or incorrect customer onboarding session requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._