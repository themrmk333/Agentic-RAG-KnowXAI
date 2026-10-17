# Edge Case: Experiment Design and Tracking Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-RND-002-EDGE-D",
  "title": "Edge Case: Experiment Design and Tracking Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Research & Development",
  "department_code": "RND",
  "category": "Experimentation",
  "subcategory": "Research Experiment",
  "roles": [
    "AI Research Engineer",
    "Research Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Experiment Design and Tracking Procedure",
    "edge case",
    "exception",
    "RND"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Research Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-RND-002"
}
```

**Document ID:** SOP-RND-002-EDGE-D  
**Related SOP:** SOP-RND-002 (Experiment Design and Tracking Procedure)  
**Department:** Research & Development

## Situation
A research experiment request is rejected by the Research Lead, or AI Research Engineer accidentally submits the same request twice in MK-Labs.

## Detection
MK-Labs shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Research Lead (for rejections) or MK-Labs itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Research Lead records a specific rejection reason in MK-Labs — a bare 'Rejected' status without a reason is not acceptable practice.
2. AI Research Engineer reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If AI Research Engineer disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Research Associate -> Research Lead -> R&D Manager -> R&D Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-Labs flags the second entry automatically; the AI Research Engineer or Research Lead confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Research Lead initiates the standard reversal process instead of just closing the record.
6. MK-Labs retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
AI Research Engineer

## Approval
Research Lead

## Escalation
Research Associate -> Research Lead -> R&D Manager -> R&D Director

## Expected Result
Rejections always carry a documented reason and a clear next step for AI Research Engineer, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._