# Edge Case: Project Portfolio Review Procedure (Management) — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-MGMT-002-EDGE-D",
  "title": "Edge Case: Project Portfolio Review Procedure (Management) \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Management / Leadership",
  "department_code": "MGMT",
  "category": "Portfolio Governance",
  "subcategory": "Executive Portfolio Review",
  "roles": [
    "PMO Director",
    "Vice President"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Project Portfolio Review Procedure (Management)",
    "edge case",
    "exception",
    "MGMT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Vice President",
  "source": "synthetic-generated",
  "related_sop": "SOP-MGMT-002"
}
```

**Document ID:** SOP-MGMT-002-EDGE-D
**Related SOP:** SOP-MGMT-002 (Project Portfolio Review Procedure (Management))
**Department:** Management / Leadership

## Situation
A executive portfolio review request is rejected by the Vice President, or PMO Director accidentally submits the same request twice in MK-ExecDash.

## Detection
MK-ExecDash shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Vice President (for rejections) or MK-ExecDash itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Vice President records a specific rejection reason in MK-ExecDash — a bare 'Rejected' status without a reason is not acceptable practice.
2. PMO Director reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If PMO Director disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Manager -> Director -> Vice President -> CEO Office) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-ExecDash flags the second entry automatically; the PMO Director or Vice President confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Vice President initiates the standard reversal process instead of just closing the record.
6. MK-ExecDash retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
PMO Director

## Approval
Vice President

## Escalation
Manager -> Director -> Vice President -> CEO Office

## Expected Result
Rejections always carry a documented reason and a clear next step for PMO Director, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._