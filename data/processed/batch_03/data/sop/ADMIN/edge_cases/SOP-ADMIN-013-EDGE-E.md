# Edge Case: Emergency Evacuation Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-ADMIN-013-EDGE-E",
  "title": "Edge Case: Emergency Evacuation Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Health & Safety",
  "subcategory": "Emergency Evacuation",
  "roles": [
    "Facilities Coordinator",
    "Head of Administration"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Emergency Evacuation Procedure",
    "edge case",
    "exception",
    "ADMIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Head of Administration",
  "source": "synthetic-generated",
  "related_sop": "SOP-ADMIN-013"
}
```

**Document ID:** SOP-ADMIN-013-EDGE-E  
**Related SOP:** SOP-ADMIN-013 (Emergency Evacuation Procedure)  
**Department:** Administration / Facilities

## Situation
Facilities Coordinator submits a emergency evacuation request in MK-FacilitiesDesk that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Head of Administration reviewing the request in MK-FacilitiesDesk notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Head of Administration decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Head of Administration does not approve or silently correct the request themselves; they return it to Facilities Coordinator in MK-FacilitiesDesk with a specific note on what's missing or wrong.
2. Facilities Coordinator is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Facilities Coordinator corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Head of Administration reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Head of Administration flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-ADMIN-013.

## Responsible Role
Facilities Coordinator

## Approval
Head of Administration

## Escalation
Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration

## Expected Result
Incomplete or incorrect emergency evacuation requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._