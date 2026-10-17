# Edge Case: Visitor Management Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-ADMIN-006-EDGE-D",
  "title": "Edge Case: Visitor Management Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Visitor Management",
  "subcategory": "Visitor Pass",
  "roles": [
    "receptionist",
    "Facilities Coordinator"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Visitor Management Procedure",
    "edge case",
    "exception",
    "ADMIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Facilities Coordinator",
  "source": "synthetic-generated",
  "related_sop": "SOP-ADMIN-006"
}
```

**Document ID:** SOP-ADMIN-006-EDGE-D  
**Related SOP:** SOP-ADMIN-006 (Visitor Management Procedure)  
**Department:** Administration / Facilities

## Situation
A visitor pass request is rejected by the Facilities Coordinator, or receptionist accidentally submits the same request twice in MK-FacilitiesDesk.

## Detection
MK-FacilitiesDesk shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Facilities Coordinator (for rejections) or MK-FacilitiesDesk itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Facilities Coordinator records a specific rejection reason in MK-FacilitiesDesk — a bare 'Rejected' status without a reason is not acceptable practice.
2. receptionist reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If receptionist disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-FacilitiesDesk flags the second entry automatically; the receptionist or Facilities Coordinator confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Facilities Coordinator initiates the standard reversal process instead of just closing the record.
6. MK-FacilitiesDesk retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
receptionist

## Approval
Facilities Coordinator

## Escalation
Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration

## Expected Result
Rejections always carry a documented reason and a clear next step for receptionist, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._