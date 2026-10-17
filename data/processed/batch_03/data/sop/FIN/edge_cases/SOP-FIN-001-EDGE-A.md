# Edge Case: Expense Reimbursement Procedure — When the Finance Lead Is Unavailable

```json
{
  "document_id": "SOP-FIN-001-EDGE-A",
  "title": "Edge Case: Expense Reimbursement Procedure \u2014 When the Finance Lead Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Finance & Accounting",
  "department_code": "FIN",
  "category": "Expense Reimbursement",
  "subcategory": "Expense Claim",
  "roles": [
    "employee",
    "Finance Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Expense Reimbursement Procedure",
    "edge case",
    "exception",
    "FIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-FIN-001"
}
```

**Document ID:** SOP-FIN-001-EDGE-A  
**Related SOP:** SOP-FIN-001 (Expense Reimbursement Procedure)  
**Department:** Finance & Accounting

## Scenario
The designated approver (Finance Lead) is on leave, travel, or otherwise unreachable within the normal response window, but the expense claim cannot wait for their return.

## Deviation Procedure

1. employee confirms the Finance Lead has an active out-of-office status in MK-Finance360 or MK-HRMS before invoking this path.
2. employee identifies the Finance Lead's designated delegate — typically the next role up the escalation chain (Accountant -> Finance Lead -> Finance Manager -> Finance Director) — as recorded in MK-Finance360.
3. employee resubmits or flags the existing request in MK-Finance360, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Finance Lead would apply, and either approves, rejects, or requests clarification.
5. Once the Finance Lead returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-Finance360 logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Expense Reimbursement Procedure decisions explicitly reserved for the Finance Lead by policy (e.g., anything requiring named signing authority); those must wait for the Finance Lead's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Accountant -> Finance Lead -> Finance Manager -> Finance Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._