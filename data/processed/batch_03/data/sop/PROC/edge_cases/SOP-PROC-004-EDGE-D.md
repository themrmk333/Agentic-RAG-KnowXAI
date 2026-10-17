# Edge Case: Vendor Contract Renewal Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-PROC-004-EDGE-D",
  "title": "Edge Case: Vendor Contract Renewal Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Procurement / Purchasing",
  "department_code": "PROC",
  "category": "Vendor Management",
  "subcategory": "Vendor Contract Renewal",
  "roles": [
    "Vendor Manager",
    "Procurement Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Vendor Contract Renewal Procedure",
    "edge case",
    "exception",
    "PROC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Procurement Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROC-004"
}
```

**Document ID:** SOP-PROC-004-EDGE-D  
**Related SOP:** SOP-PROC-004 (Vendor Contract Renewal Procedure)  
**Department:** Procurement / Purchasing

## Situation
A vendor contract renewal request is rejected by the Procurement Manager, or Vendor Manager accidentally submits the same request twice in MK-ProcureX.

## Detection
MK-ProcureX shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Procurement Manager (for rejections) or MK-ProcureX itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Procurement Manager records a specific rejection reason in MK-ProcureX — a bare 'Rejected' status without a reason is not acceptable practice.
2. Vendor Manager reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Vendor Manager disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-ProcureX flags the second entry automatically; the Vendor Manager or Procurement Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Procurement Manager initiates the standard reversal process instead of just closing the record.
6. MK-ProcureX retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Vendor Manager

## Approval
Procurement Manager

## Escalation
Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director

## Expected Result
Rejections always carry a documented reason and a clear next step for Vendor Manager, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._