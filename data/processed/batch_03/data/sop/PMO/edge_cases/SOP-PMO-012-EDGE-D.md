# Edge Case: Project Portfolio Review Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-PMO-012-EDGE-D",
  "title": "Edge Case: Project Portfolio Review Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Project Management / PMO",
  "department_code": "PMO",
  "category": "Portfolio Management",
  "subcategory": "Portfolio Review",
  "roles": [
    "PMO Lead",
    "PMO Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Project Portfolio Review Procedure",
    "edge case",
    "exception",
    "PMO"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "PMO Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-PMO-012"
}
```

**Document ID:** SOP-PMO-012-EDGE-D  
**Related SOP:** SOP-PMO-012 (Project Portfolio Review Procedure)  
**Department:** Project Management / PMO

## Situation
A portfolio review request is rejected by the PMO Director, or PMO Lead accidentally submits the same request twice in MK-PMTrack.

## Detection
MK-PMTrack shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The PMO Director (for rejections) or MK-PMTrack itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the PMO Director records a specific rejection reason in MK-PMTrack — a bare 'Rejected' status without a reason is not acceptable practice.
2. PMO Lead reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If PMO Lead disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Project Coordinator -> Project Manager -> PMO Lead -> PMO Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-PMTrack flags the second entry automatically; the PMO Lead or PMO Director confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the PMO Director initiates the standard reversal process instead of just closing the record.
6. MK-PMTrack retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
PMO Lead

## Approval
PMO Director

## Escalation
Project Coordinator -> Project Manager -> PMO Lead -> PMO Director

## Expected Result
Rejections always carry a documented reason and a clear next step for PMO Lead, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._