# Edge Case: Test Environment Setup Request — When the DevOps Engineer Is Unavailable

```json
{
  "document_id": "SOP-QA-008-EDGE-A",
  "title": "Edge Case: Test Environment Setup Request \u2014 When the DevOps Engineer Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Environment Management",
  "subcategory": "Test Environment",
  "roles": [
    "QA Engineer",
    "DevOps Engineer"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Test Environment Setup Request",
    "edge case",
    "exception",
    "QA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Engineer",
  "source": "synthetic-generated",
  "related_sop": "SOP-QA-008"
}
```

**Document ID:** SOP-QA-008-EDGE-A
**Related SOP:** SOP-QA-008 (Test Environment Setup Request)
**Department:** QA / Testing

## Scenario
The designated approver (DevOps Engineer) is on leave, travel, or otherwise unreachable within the normal response window, but the test environment cannot wait for their return.

## Deviation Procedure

1. QA Engineer confirms the DevOps Engineer has an active out-of-office status in MK-TestHub or MK-HRMS before invoking this path.
2. QA Engineer identifies the DevOps Engineer's designated delegate — typically the next role up the escalation chain (QA Engineer -> QA Lead -> QA Manager -> QA Director) — as recorded in MK-TestHub.
3. QA Engineer resubmits or flags the existing request in MK-TestHub, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original DevOps Engineer would apply, and either approves, rejects, or requests clarification.
5. Once the DevOps Engineer returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-TestHub logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Test Environment Setup Request decisions explicitly reserved for the DevOps Engineer by policy (e.g., anything requiring named signing authority); those must wait for the DevOps Engineer's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: QA Engineer -> QA Lead -> QA Manager -> QA Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._