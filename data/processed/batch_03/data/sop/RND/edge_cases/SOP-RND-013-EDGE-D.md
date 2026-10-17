# Edge Case: External Research Collaboration Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-RND-013-EDGE-D",
  "title": "Edge Case: External Research Collaboration Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Research & Development",
  "department_code": "RND",
  "category": "Partnerships",
  "subcategory": "Collaboration Agreement",
  "roles": [
    "R&D Manager",
    "General Counsel"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "External Research Collaboration Procedure",
    "edge case",
    "exception",
    "RND"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "General Counsel",
  "source": "synthetic-generated",
  "related_sop": "SOP-RND-013"
}
```

**Document ID:** SOP-RND-013-EDGE-D  
**Related SOP:** SOP-RND-013 (External Research Collaboration Procedure)  
**Department:** Research & Development

## Situation
A collaboration agreement request is rejected by the General Counsel, or R&D Manager accidentally submits the same request twice in MK-Labs.

## Detection
MK-Labs shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The General Counsel (for rejections) or MK-Labs itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the General Counsel records a specific rejection reason in MK-Labs — a bare 'Rejected' status without a reason is not acceptable practice.
2. R&D Manager reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If R&D Manager disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Research Associate -> Research Lead -> R&D Manager -> R&D Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-Labs flags the second entry automatically; the R&D Manager or General Counsel confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the General Counsel initiates the standard reversal process instead of just closing the record.
6. MK-Labs retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
R&D Manager

## Approval
General Counsel

## Escalation
Research Associate -> Research Lead -> R&D Manager -> R&D Director

## Expected Result
Rejections always carry a documented reason and a clear next step for R&D Manager, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._