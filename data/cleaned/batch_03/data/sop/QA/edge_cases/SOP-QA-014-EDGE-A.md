# Edge Case: Test Data Management Procedure — When the QA Lead Is Unavailable

```json
{
  "document_id": "SOP-QA-014-EDGE-A",
  "title": "Edge Case: Test Data Management Procedure \u2014 When the QA Lead Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Test Data",
  "subcategory": "Test Data Set",
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
    "Test Data Management Procedure",
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
  "related_sop": "SOP-QA-014"
}
```

**Document ID:** SOP-QA-014-EDGE-A
**Related SOP:** SOP-QA-014 (Test Data Management Procedure)
**Department:** QA / Testing

## Scenario
The designated approver (QA Lead) is on leave, travel, or otherwise unreachable within the normal response window, but the test data set cannot wait for their return.

## Deviation Procedure

1. QA Engineer confirms the QA Lead has an active out-of-office status in MK-TestHub or MK-HRMS before invoking this path.
2. QA Engineer identifies the QA Lead's designated delegate — typically the next role up the escalation chain (QA Engineer -> QA Lead -> QA Manager -> QA Director) — as recorded in MK-TestHub.
3. QA Engineer resubmits or flags the existing request in MK-TestHub, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original QA Lead would apply, and either approves, rejects, or requests clarification.
5. Once the QA Lead returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-TestHub logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Test Data Management Procedure decisions explicitly reserved for the QA Lead by policy (e.g., anything requiring named signing authority); those must wait for the QA Lead's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: QA Engineer -> QA Lead -> QA Manager -> QA Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._