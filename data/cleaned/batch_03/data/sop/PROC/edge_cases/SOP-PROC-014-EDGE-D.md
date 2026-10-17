# Edge Case: Recurring Vendor Payment Setup — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-PROC-014-EDGE-D",
  "title": "Edge Case: Recurring Vendor Payment Setup \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Procurement / Purchasing",
  "department_code": "PROC",
  "category": "Vendor Payments",
  "subcategory": "Recurring Payment Setup",
  "roles": [
    "Procurement Executive",
    "Finance Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Recurring Vendor Payment Setup",
    "edge case",
    "exception",
    "PROC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROC-014"
}
```

**Document ID:** SOP-PROC-014-EDGE-D
**Related SOP:** SOP-PROC-014 (Recurring Vendor Payment Setup)
**Department:** Procurement / Purchasing

## Situation
A recurring payment setup request is rejected by the Finance Manager, or Procurement Executive accidentally submits the same request twice in MK-ProcureX.

## Detection
MK-ProcureX shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Finance Manager (for rejections) or MK-ProcureX itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Finance Manager records a specific rejection reason in MK-ProcureX — a bare 'Rejected' status without a reason is not acceptable practice.
2. Procurement Executive reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Procurement Executive disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-ProcureX flags the second entry automatically; the Procurement Executive or Finance Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Finance Manager initiates the standard reversal process instead of just closing the record.
6. MK-ProcureX retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Procurement Executive

## Approval
Finance Manager

## Escalation
Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Procurement Executive, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._