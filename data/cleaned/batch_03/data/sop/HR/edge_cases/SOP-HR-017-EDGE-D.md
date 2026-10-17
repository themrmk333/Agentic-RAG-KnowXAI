# Edge Case: HR Onboarding for New HR Team Members — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-HR-017-EDGE-D",
  "title": "Edge Case: HR Onboarding for New HR Team Members \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Human Resources",
  "department_code": "HR",
  "category": "Onboarding",
  "subcategory": "HR Team Onboarding",
  "roles": [
    "HR Manager",
    "HR Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "HR Onboarding for New HR Team Members",
    "edge case",
    "exception",
    "HR"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "HR Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-HR-017"
}
```

**Document ID:** SOP-HR-017-EDGE-D
**Related SOP:** SOP-HR-017 (HR Onboarding for New HR Team Members)
**Department:** Human Resources

## Situation
A hr team onboarding request is rejected by the HR Director, or HR Manager accidentally submits the same request twice in MK-HRMS.

## Detection
MK-HRMS shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The HR Director (for rejections) or MK-HRMS itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the HR Director records a specific rejection reason in MK-HRMS — a bare 'Rejected' status without a reason is not acceptable practice.
2. HR Manager reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If HR Manager disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (HR Executive -> HR Business Partner -> HR Manager -> HR Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-HRMS flags the second entry automatically; the HR Manager or HR Director confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the HR Director initiates the standard reversal process instead of just closing the record.
6. MK-HRMS retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
HR Manager

## Approval
HR Director

## Escalation
HR Executive -> HR Business Partner -> HR Manager -> HR Director

## Expected Result
Rejections always carry a documented reason and a clear next step for HR Manager, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._