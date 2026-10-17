# Edge Case: Production Incident Response (DevOps) — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-DEVOPS-004-EDGE-D",
  "title": "Edge Case: Production Incident Response (DevOps) \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Incident Management",
  "subcategory": "Infrastructure Incident",
  "roles": [
    "on-call DevOps Engineer",
    "DevOps Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Production Incident Response (DevOps)",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-004"
}
```

**Document ID:** SOP-DEVOPS-004-EDGE-D
**Related SOP:** SOP-DEVOPS-004 (Production Incident Response (DevOps))
**Department:** DevOps & Cloud

## Situation
A infrastructure incident request is rejected by the DevOps Manager, or on-call DevOps Engineer accidentally submits the same request twice in MK-CloudOps.

## Detection
MK-CloudOps shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The DevOps Manager (for rejections) or MK-CloudOps itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the DevOps Manager records a specific rejection reason in MK-CloudOps — a bare 'Rejected' status without a reason is not acceptable practice.
2. on-call DevOps Engineer reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If on-call DevOps Engineer disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (DevOps Engineer -> DevOps Manager -> DevOps Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-CloudOps flags the second entry automatically; the on-call DevOps Engineer or DevOps Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the DevOps Manager initiates the standard reversal process instead of just closing the record.
6. MK-CloudOps retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
on-call DevOps Engineer

## Approval
DevOps Manager

## Escalation
DevOps Engineer -> DevOps Manager -> DevOps Director

## Expected Result
Rejections always carry a documented reason and a clear next step for on-call DevOps Engineer, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._