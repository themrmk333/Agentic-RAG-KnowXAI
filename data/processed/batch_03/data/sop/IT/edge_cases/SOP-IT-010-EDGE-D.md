# Edge Case: Corporate Email Account Setup — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-IT-010-EDGE-D",
  "title": "Edge Case: Corporate Email Account Setup \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "IT Support / Information Technology",
  "department_code": "IT",
  "category": "Email",
  "subcategory": "Email Account",
  "roles": [
    "IT Support Engineer",
    "IT Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Corporate Email Account Setup",
    "edge case",
    "exception",
    "IT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "IT Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-IT-010"
}
```

**Document ID:** SOP-IT-010-EDGE-D  
**Related SOP:** SOP-IT-010 (Corporate Email Account Setup)  
**Department:** IT Support / Information Technology

## Situation
A email account request is rejected by the IT Manager, or IT Support Engineer accidentally submits the same request twice in MK-ServiceDesk.

## Detection
MK-ServiceDesk shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The IT Manager (for rejections) or MK-ServiceDesk itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the IT Manager records a specific rejection reason in MK-ServiceDesk — a bare 'Rejected' status without a reason is not acceptable practice.
2. IT Support Engineer reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If IT Support Engineer disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (IT Support Engineer -> IT Manager -> IT Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-ServiceDesk flags the second entry automatically; the IT Support Engineer or IT Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the IT Manager initiates the standard reversal process instead of just closing the record.
6. MK-ServiceDesk retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
IT Support Engineer

## Approval
IT Manager

## Escalation
IT Support Engineer -> IT Manager -> IT Director

## Expected Result
Rejections always carry a documented reason and a clear next step for IT Support Engineer, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._