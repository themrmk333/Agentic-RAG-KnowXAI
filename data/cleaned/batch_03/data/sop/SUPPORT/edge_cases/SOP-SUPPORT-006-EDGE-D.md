# Edge Case: Knowledge Base Article Creation Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-SUPPORT-006-EDGE-D",
  "title": "Edge Case: Knowledge Base Article Creation Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Knowledge Management",
  "subcategory": "KB Article",
  "roles": [
    "Senior Support Associate",
    "Support Team Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Knowledge Base Article Creation Procedure",
    "edge case",
    "exception",
    "SUPPORT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Support Team Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-SUPPORT-006"
}
```

**Document ID:** SOP-SUPPORT-006-EDGE-D
**Related SOP:** SOP-SUPPORT-006 (Knowledge Base Article Creation Procedure)
**Department:** Customer Support / Helpdesk

## Situation
A kb article request is rejected by the Support Team Lead, or Senior Support Associate accidentally submits the same request twice in MK-SupportDesk.

## Detection
MK-SupportDesk shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Support Team Lead (for rejections) or MK-SupportDesk itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Support Team Lead records a specific rejection reason in MK-SupportDesk — a bare 'Rejected' status without a reason is not acceptable practice.
2. Senior Support Associate reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Senior Support Associate disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-SupportDesk flags the second entry automatically; the Senior Support Associate or Support Team Lead confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Support Team Lead initiates the standard reversal process instead of just closing the record.
6. MK-SupportDesk retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Senior Support Associate

## Approval
Support Team Lead

## Escalation
Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Senior Support Associate, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._