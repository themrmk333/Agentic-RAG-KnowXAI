# Edge Case: Attendance Regularization Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-HR-012-EDGE-D",
  "title": "Edge Case: Attendance Regularization Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Human Resources",
  "department_code": "HR",
  "category": "Attendance",
  "subcategory": "Attendance Regularization",
  "roles": [
    "employee",
    "Reporting Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Attendance Regularization Procedure",
    "edge case",
    "exception",
    "HR"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Reporting Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-HR-012"
}
```

**Document ID:** SOP-HR-012-EDGE-D
**Related SOP:** SOP-HR-012 (Attendance Regularization Procedure)
**Department:** Human Resources

## Situation
A attendance regularization request is rejected by the Reporting Manager, or employee accidentally submits the same request twice in MK-HRMS.

## Detection
MK-HRMS shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Reporting Manager (for rejections) or MK-HRMS itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Reporting Manager records a specific rejection reason in MK-HRMS — a bare 'Rejected' status without a reason is not acceptable practice.
2. employee reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If employee disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (HR Executive -> HR Business Partner -> HR Manager -> HR Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-HRMS flags the second entry automatically; the employee or Reporting Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Reporting Manager initiates the standard reversal process instead of just closing the record.
6. MK-HRMS retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
employee

## Approval
Reporting Manager

## Escalation
HR Executive -> HR Business Partner -> HR Manager -> HR Director

## Expected Result
Rejections always carry a documented reason and a clear next step for employee, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._