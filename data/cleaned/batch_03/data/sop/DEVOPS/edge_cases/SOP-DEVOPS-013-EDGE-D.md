# Edge Case: Cost Optimization Review — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-DEVOPS-013-EDGE-D",
  "title": "Edge Case: Cost Optimization Review \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Cost Management",
  "subcategory": "Cloud Cost Report",
  "roles": [
    "Cloud Architect",
    "DevOps Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Cost Optimization Review",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-013"
}
```

**Document ID:** SOP-DEVOPS-013-EDGE-D
**Related SOP:** SOP-DEVOPS-013 (Cost Optimization Review)
**Department:** DevOps & Cloud

## Situation
A cloud cost report request is rejected by the DevOps Director, or Cloud Architect accidentally submits the same request twice in MK-CloudOps.

## Detection
MK-CloudOps shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The DevOps Director (for rejections) or MK-CloudOps itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the DevOps Director records a specific rejection reason in MK-CloudOps — a bare 'Rejected' status without a reason is not acceptable practice.
2. Cloud Architect reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Cloud Architect disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (DevOps Engineer -> DevOps Manager -> DevOps Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-CloudOps flags the second entry automatically; the Cloud Architect or DevOps Director confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the DevOps Director initiates the standard reversal process instead of just closing the record.
6. MK-CloudOps retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Cloud Architect

## Approval
DevOps Director

## Escalation
DevOps Engineer -> DevOps Manager -> DevOps Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Cloud Architect, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._