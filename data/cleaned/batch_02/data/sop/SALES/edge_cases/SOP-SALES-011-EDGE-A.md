# Edge Case: Customer Reference Request Procedure — When the Marketing Manager Is Unavailable

```json
{
  "document_id": "SOP-SALES-011-EDGE-A",
  "title": "Edge Case: Customer Reference Request Procedure \u2014 When the Marketing Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Sales",
  "department_code": "SALES",
  "category": "Customer References",
  "subcategory": "Reference Request",
  "roles": [
    "Account Executive",
    "Marketing Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Customer Reference Request Procedure",
    "edge case",
    "exception",
    "SALES"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Marketing Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SALES-011"
}
```

**Document ID:** SOP-SALES-011-EDGE-A
**Related SOP:** SOP-SALES-011 (Customer Reference Request Procedure)
**Department:** Sales

## Scenario
The designated approver (Marketing Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the reference request cannot wait for their return.

## Deviation Procedure

1. Account Executive confirms the Marketing Manager has an active out-of-office status in MK-CRM or MK-HRMS before invoking this path.
2. Account Executive identifies the Marketing Manager's designated delegate — typically the next role up the escalation chain (Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director) — as recorded in MK-CRM.
3. Account Executive resubmits or flags the existing request in MK-CRM, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Marketing Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Marketing Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-CRM logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Customer Reference Request Procedure decisions explicitly reserved for the Marketing Manager by policy (e.g., anything requiring named signing authority); those must wait for the Marketing Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._