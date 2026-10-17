# Edge Case: Internal Job Transfer Procedure — When the HR Business Partner Is Unavailable

```json
{
  "document_id": "SOP-HR-006-EDGE-A",
  "title": "Edge Case: Internal Job Transfer Procedure \u2014 When the HR Business Partner Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Human Resources",
  "department_code": "HR",
  "category": "Mobility",
  "subcategory": "Transfer Request",
  "roles": [
    "employee",
    "HR Business Partner"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Internal Job Transfer Procedure",
    "edge case",
    "exception",
    "HR"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "HR Business Partner",
  "source": "synthetic-generated",
  "related_sop": "SOP-HR-006"
}
```

**Document ID:** SOP-HR-006-EDGE-A
**Related SOP:** SOP-HR-006 (Internal Job Transfer Procedure)
**Department:** Human Resources

## Scenario
The designated approver (HR Business Partner) is on leave, travel, or otherwise unreachable within the normal response window, but the transfer request cannot wait for their return.

## Deviation Procedure

1. employee confirms the HR Business Partner has an active out-of-office status in MK-HRMS or MK-HRMS before invoking this path.
2. employee identifies the HR Business Partner's designated delegate — typically the next role up the escalation chain (HR Executive -> HR Business Partner -> HR Manager -> HR Director) — as recorded in MK-HRMS.
3. employee resubmits or flags the existing request in MK-HRMS, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original HR Business Partner would apply, and either approves, rejects, or requests clarification.
5. Once the HR Business Partner returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-HRMS logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Internal Job Transfer Procedure decisions explicitly reserved for the HR Business Partner by policy (e.g., anything requiring named signing authority); those must wait for the HR Business Partner's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: HR Executive -> HR Business Partner -> HR Manager -> HR Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._