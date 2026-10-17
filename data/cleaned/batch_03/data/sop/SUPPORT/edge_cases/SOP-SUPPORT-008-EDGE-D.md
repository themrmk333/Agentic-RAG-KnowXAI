# Edge Case: Priority/Severity Reclassification Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-SUPPORT-008-EDGE-D",
  "title": "Edge Case: Priority/Severity Reclassification Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Ticket Management",
  "subcategory": "Severity Reclassification",
  "roles": [
    "Customer Support Associate",
    "Support Team Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Priority/Severity Reclassification Procedure",
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
  "related_sop": "SOP-SUPPORT-008"
}
```

**Document ID:** SOP-SUPPORT-008-EDGE-D
**Related SOP:** SOP-SUPPORT-008 (Priority/Severity Reclassification Procedure)
**Department:** Customer Support / Helpdesk

## Situation
A severity reclassification request is rejected by the Support Team Lead, or Customer Support Associate accidentally submits the same request twice in MK-SupportDesk.

## Detection
MK-SupportDesk shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Support Team Lead (for rejections) or MK-SupportDesk itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Support Team Lead records a specific rejection reason in MK-SupportDesk — a bare 'Rejected' status without a reason is not acceptable practice.
2. Customer Support Associate reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Customer Support Associate disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-SupportDesk flags the second entry automatically; the Customer Support Associate or Support Team Lead confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Support Team Lead initiates the standard reversal process instead of just closing the record.
6. MK-SupportDesk retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Customer Support Associate

## Approval
Support Team Lead

## Escalation
Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Customer Support Associate, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._