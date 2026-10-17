# Edge Case: Remote Desktop / Screen Share Support Session — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-IT-014-EDGE-D",
  "title": "Edge Case: Remote Desktop / Screen Share Support Session \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "IT Support / Information Technology",
  "department_code": "IT",
  "category": "Support Operations",
  "subcategory": "Remote Support Session",
  "roles": [
    "employee",
    "IT Support Engineer"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Remote Desktop / Screen Share Support Session",
    "edge case",
    "exception",
    "IT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "IT Support Engineer",
  "source": "synthetic-generated",
  "related_sop": "SOP-IT-014"
}
```

**Document ID:** SOP-IT-014-EDGE-D  
**Related SOP:** SOP-IT-014 (Remote Desktop / Screen Share Support Session)  
**Department:** IT Support / Information Technology

## Situation
A remote support session request is rejected by the IT Support Engineer, or employee accidentally submits the same request twice in MK-ServiceDesk.

## Detection
MK-ServiceDesk shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The IT Support Engineer (for rejections) or MK-ServiceDesk itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the IT Support Engineer records a specific rejection reason in MK-ServiceDesk — a bare 'Rejected' status without a reason is not acceptable practice.
2. employee reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If employee disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (IT Support Engineer -> IT Manager -> IT Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-ServiceDesk flags the second entry automatically; the employee or IT Support Engineer confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the IT Support Engineer initiates the standard reversal process instead of just closing the record.
6. MK-ServiceDesk retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
employee

## Approval
IT Support Engineer

## Escalation
IT Support Engineer -> IT Manager -> IT Director

## Expected Result
Rejections always carry a documented reason and a clear next step for employee, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._