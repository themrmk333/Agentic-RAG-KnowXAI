# Edge Case: Office Supplies Replenishment Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-ADMIN-005-EDGE-E",
  "title": "Edge Case: Office Supplies Replenishment Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Supplies",
  "subcategory": "Supplies Request",
  "roles": [
    "Facilities Executive",
    "Admin Team Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Office Supplies Replenishment Procedure",
    "edge case",
    "exception",
    "ADMIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Admin Team Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-ADMIN-005"
}
```

**Document ID:** SOP-ADMIN-005-EDGE-E
**Related SOP:** SOP-ADMIN-005 (Office Supplies Replenishment Procedure)
**Department:** Administration / Facilities

## Situation
Facilities Executive submits a supplies request request in MK-FacilitiesDesk that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Admin Team Lead reviewing the request in MK-FacilitiesDesk notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Admin Team Lead decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Admin Team Lead does not approve or silently correct the request themselves; they return it to Facilities Executive in MK-FacilitiesDesk with a specific note on what's missing or wrong.
2. Facilities Executive is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Facilities Executive corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Admin Team Lead reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Admin Team Lead flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-ADMIN-005.

## Responsible Role
Facilities Executive

## Approval
Admin Team Lead

## Escalation
Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration

## Expected Result
Incomplete or incorrect supplies request requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._