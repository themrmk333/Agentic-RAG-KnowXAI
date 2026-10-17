# Edge Case: Legal Hold Notification Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-LEGAL-011-EDGE-D",
  "title": "Edge Case: Legal Hold Notification Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Legal & Compliance",
  "department_code": "LEGAL",
  "category": "Litigation",
  "subcategory": "Legal Hold Notice",
  "roles": [
    "Senior Legal Counsel",
    "General Counsel"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Legal Hold Notification Procedure",
    "edge case",
    "exception",
    "LEGAL"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "General Counsel",
  "source": "synthetic-generated",
  "related_sop": "SOP-LEGAL-011"
}
```

**Document ID:** SOP-LEGAL-011-EDGE-D
**Related SOP:** SOP-LEGAL-011 (Legal Hold Notification Procedure)
**Department:** Legal & Compliance

## Situation
A legal hold notice request is rejected by the General Counsel, or Senior Legal Counsel accidentally submits the same request twice in MK-LegalVault.

## Detection
MK-LegalVault shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The General Counsel (for rejections) or MK-LegalVault itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the General Counsel records a specific rejection reason in MK-LegalVault — a bare 'Rejected' status without a reason is not acceptable practice.
2. Senior Legal Counsel reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Senior Legal Counsel disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-LegalVault flags the second entry automatically; the Senior Legal Counsel or General Counsel confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the General Counsel initiates the standard reversal process instead of just closing the record.
6. MK-LegalVault retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Senior Legal Counsel

## Approval
General Counsel

## Escalation
Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel

## Expected Result
Rejections always carry a documented reason and a clear next step for Senior Legal Counsel, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._