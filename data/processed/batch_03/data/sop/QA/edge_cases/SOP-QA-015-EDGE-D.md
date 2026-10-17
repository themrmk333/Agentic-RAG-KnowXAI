# Edge Case: Exploratory Testing Session Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-QA-015-EDGE-D",
  "title": "Edge Case: Exploratory Testing Session Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Test Execution",
  "subcategory": "Exploratory Test Charter",
  "roles": [
    "QA Engineer",
    "QA Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Exploratory Testing Session Procedure",
    "edge case",
    "exception",
    "QA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "QA Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-QA-015"
}
```

**Document ID:** SOP-QA-015-EDGE-D  
**Related SOP:** SOP-QA-015 (Exploratory Testing Session Procedure)  
**Department:** QA / Testing

## Situation
A exploratory test charter request is rejected by the QA Lead, or QA Engineer accidentally submits the same request twice in MK-TestHub.

## Detection
MK-TestHub shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The QA Lead (for rejections) or MK-TestHub itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the QA Lead records a specific rejection reason in MK-TestHub — a bare 'Rejected' status without a reason is not acceptable practice.
2. QA Engineer reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If QA Engineer disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (QA Engineer -> QA Lead -> QA Manager -> QA Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-TestHub flags the second entry automatically; the QA Engineer or QA Lead confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the QA Lead initiates the standard reversal process instead of just closing the record.
6. MK-TestHub retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
QA Engineer

## Approval
QA Lead

## Escalation
QA Engineer -> QA Lead -> QA Manager -> QA Director

## Expected Result
Rejections always carry a documented reason and a clear next step for QA Engineer, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._