# Edge Case: Sales Commission Calculation Procedure — When the Finance Manager Is Unavailable

```json
{
  "document_id": "SOP-SALES-012-EDGE-A",
  "title": "Edge Case: Sales Commission Calculation Procedure \u2014 When the Finance Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Sales",
  "department_code": "SALES",
  "category": "Compensation",
  "subcategory": "Commission Calculation",
  "roles": [
    "Sales Manager",
    "Finance Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Sales Commission Calculation Procedure",
    "edge case",
    "exception",
    "SALES"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SALES-012"
}
```

**Document ID:** SOP-SALES-012-EDGE-A
**Related SOP:** SOP-SALES-012 (Sales Commission Calculation Procedure)
**Department:** Sales

## Scenario
The designated approver (Finance Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the commission calculation cannot wait for their return.

## Deviation Procedure

1. Sales Manager confirms the Finance Manager has an active out-of-office status in MK-CRM or MK-HRMS before invoking this path.
2. Sales Manager identifies the Finance Manager's designated delegate — typically the next role up the escalation chain (Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director) — as recorded in MK-CRM.
3. Sales Manager resubmits or flags the existing request in MK-CRM, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Finance Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Finance Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-CRM logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Sales Commission Calculation Procedure decisions explicitly reserved for the Finance Manager by policy (e.g., anything requiring named signing authority); those must wait for the Finance Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._