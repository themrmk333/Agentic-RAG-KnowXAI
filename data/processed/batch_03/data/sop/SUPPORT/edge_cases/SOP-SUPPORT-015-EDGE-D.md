# Edge Case: Customer Complaint Handling Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-SUPPORT-015-EDGE-D",
  "title": "Edge Case: Customer Complaint Handling Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Customer Relations",
  "subcategory": "Formal Complaint",
  "roles": [
    "Support Manager",
    "Customer Experience Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Customer Complaint Handling Procedure",
    "edge case",
    "exception",
    "SUPPORT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Customer Experience Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-SUPPORT-015"
}
```

**Document ID:** SOP-SUPPORT-015-EDGE-D  
**Related SOP:** SOP-SUPPORT-015 (Customer Complaint Handling Procedure)  
**Department:** Customer Support / Helpdesk

## Situation
A formal complaint request is rejected by the Customer Experience Director, or Support Manager accidentally submits the same request twice in MK-SupportDesk.

## Detection
MK-SupportDesk shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Customer Experience Director (for rejections) or MK-SupportDesk itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Customer Experience Director records a specific rejection reason in MK-SupportDesk — a bare 'Rejected' status without a reason is not acceptable practice.
2. Support Manager reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Support Manager disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-SupportDesk flags the second entry automatically; the Support Manager or Customer Experience Director confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Customer Experience Director initiates the standard reversal process instead of just closing the record.
6. MK-SupportDesk retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Support Manager

## Approval
Customer Experience Director

## Escalation
Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Support Manager, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._