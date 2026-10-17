# Edge Case: Change Request Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-PMO-004-EDGE-D",
  "title": "Edge Case: Change Request Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Project Management / PMO",
  "department_code": "PMO",
  "category": "Change Management",
  "subcategory": "Change Request",
  "roles": [
    "Project Manager",
    "PMO Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Change Request Procedure",
    "edge case",
    "exception",
    "PMO"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "PMO Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-PMO-004"
}
```

**Document ID:** SOP-PMO-004-EDGE-D
**Related SOP:** SOP-PMO-004 (Change Request Procedure)
**Department:** Project Management / PMO

## Situation
A change request request is rejected by the PMO Lead, or Project Manager accidentally submits the same request twice in MK-PMTrack.

## Detection
MK-PMTrack shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The PMO Lead (for rejections) or MK-PMTrack itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the PMO Lead records a specific rejection reason in MK-PMTrack — a bare 'Rejected' status without a reason is not acceptable practice.
2. Project Manager reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Project Manager disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Project Coordinator -> Project Manager -> PMO Lead -> PMO Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-PMTrack flags the second entry automatically; the Project Manager or PMO Lead confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the PMO Lead initiates the standard reversal process instead of just closing the record.
6. MK-PMTrack retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Project Manager

## Approval
PMO Lead

## Escalation
Project Coordinator -> Project Manager -> PMO Lead -> PMO Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Project Manager, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._