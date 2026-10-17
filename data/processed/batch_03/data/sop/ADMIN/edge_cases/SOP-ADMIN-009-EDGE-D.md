# Edge Case: Courier and Mail Handling Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-ADMIN-009-EDGE-D",
  "title": "Edge Case: Courier and Mail Handling Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Mailroom",
  "subcategory": "Courier Request",
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
    "Courier and Mail Handling Procedure",
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
  "related_sop": "SOP-ADMIN-009"
}
```

**Document ID:** SOP-ADMIN-009-EDGE-D  
**Related SOP:** SOP-ADMIN-009 (Courier and Mail Handling Procedure)  
**Department:** Administration / Facilities

## Situation
A courier request request is rejected by the Admin Team Lead, or Facilities Executive accidentally submits the same request twice in MK-FacilitiesDesk.

## Detection
MK-FacilitiesDesk shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Admin Team Lead (for rejections) or MK-FacilitiesDesk itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Admin Team Lead records a specific rejection reason in MK-FacilitiesDesk — a bare 'Rejected' status without a reason is not acceptable practice.
2. Facilities Executive reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Facilities Executive disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-FacilitiesDesk flags the second entry automatically; the Facilities Executive or Admin Team Lead confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Admin Team Lead initiates the standard reversal process instead of just closing the record.
6. MK-FacilitiesDesk retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Facilities Executive

## Approval
Admin Team Lead

## Escalation
Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration

## Expected Result
Rejections always carry a documented reason and a clear next step for Facilities Executive, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._