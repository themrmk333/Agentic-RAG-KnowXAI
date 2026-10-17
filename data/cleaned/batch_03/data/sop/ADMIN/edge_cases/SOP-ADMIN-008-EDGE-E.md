# Edge Case: Business Travel Booking Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-ADMIN-008-EDGE-E",
  "title": "Edge Case: Business Travel Booking Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Travel Administration",
  "subcategory": "Travel Booking Request",
  "roles": [
    "employee",
    "Reporting Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Business Travel Booking Procedure",
    "edge case",
    "exception",
    "ADMIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Reporting Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-ADMIN-008"
}
```

**Document ID:** SOP-ADMIN-008-EDGE-E
**Related SOP:** SOP-ADMIN-008 (Business Travel Booking Procedure)
**Department:** Administration / Facilities

## Situation
employee submits a travel booking request request in MK-FacilitiesDesk that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Reporting Manager reviewing the request in MK-FacilitiesDesk notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Reporting Manager decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Reporting Manager does not approve or silently correct the request themselves; they return it to employee in MK-FacilitiesDesk with a specific note on what's missing or wrong.
2. employee is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. employee corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Reporting Manager reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Reporting Manager flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-ADMIN-008.

## Responsible Role
employee

## Approval
Reporting Manager

## Escalation
Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration

## Expected Result
Incomplete or incorrect travel booking request requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._