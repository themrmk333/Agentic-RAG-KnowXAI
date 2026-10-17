# Edge Case: Responsible AI / Ethics Review Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-RND-008-EDGE-D",
  "title": "Edge Case: Responsible AI / Ethics Review Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Research & Development",
  "department_code": "RND",
  "category": "Responsible AI",
  "subcategory": "Ethics Review",
  "roles": [
    "Research Lead",
    "R&D Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Responsible AI / Ethics Review Procedure",
    "edge case",
    "exception",
    "RND"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "R&D Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-RND-008"
}
```

**Document ID:** SOP-RND-008-EDGE-D
**Related SOP:** SOP-RND-008 (Responsible AI / Ethics Review Procedure)
**Department:** Research & Development

## Situation
A ethics review request is rejected by the R&D Director, or Research Lead accidentally submits the same request twice in MK-Labs.

## Detection
MK-Labs shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The R&D Director (for rejections) or MK-Labs itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the R&D Director records a specific rejection reason in MK-Labs — a bare 'Rejected' status without a reason is not acceptable practice.
2. Research Lead reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Research Lead disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Research Associate -> Research Lead -> R&D Manager -> R&D Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-Labs flags the second entry automatically; the Research Lead or R&D Director confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the R&D Director initiates the standard reversal process instead of just closing the record.
6. MK-Labs retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Research Lead

## Approval
R&D Director

## Escalation
Research Associate -> Research Lead -> R&D Manager -> R&D Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Research Lead, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._