# Edge Case: Company-wide Policy Approval Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-MGMT-009-EDGE-E",
  "title": "Edge Case: Company-wide Policy Approval Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Management / Leadership",
  "department_code": "MGMT",
  "category": "Policy Governance",
  "subcategory": "Company Policy Approval",
  "roles": [
    "Department Manager",
    "CEO Office"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Company-wide Policy Approval Procedure",
    "edge case",
    "exception",
    "MGMT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "CEO Office",
  "source": "synthetic-generated",
  "related_sop": "SOP-MGMT-009"
}
```

**Document ID:** SOP-MGMT-009-EDGE-E  
**Related SOP:** SOP-MGMT-009 (Company-wide Policy Approval Procedure)  
**Department:** Management / Leadership

## Situation
Department Manager submits a company policy approval request in MK-ExecDash that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The CEO Office reviewing the request in MK-ExecDash notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The CEO Office decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The CEO Office does not approve or silently correct the request themselves; they return it to Department Manager in MK-ExecDash with a specific note on what's missing or wrong.
2. Department Manager is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Department Manager corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The CEO Office reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the CEO Office flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-MGMT-009.

## Responsible Role
Department Manager

## Approval
CEO Office

## Escalation
Manager -> Director -> Vice President -> CEO Office

## Expected Result
Incomplete or incorrect company policy approval requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._