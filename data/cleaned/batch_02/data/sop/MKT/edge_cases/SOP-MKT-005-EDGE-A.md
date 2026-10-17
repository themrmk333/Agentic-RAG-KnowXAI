# Edge Case: Marketing Qualified Lead (MQL) Handover to Sales — When the Sales Manager Is Unavailable

```json
{
  "document_id": "SOP-MKT-005-EDGE-A",
  "title": "Edge Case: Marketing Qualified Lead (MQL) Handover to Sales \u2014 When the Sales Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Marketing",
  "department_code": "MKT",
  "category": "Lead Generation",
  "subcategory": "MQL Handover",
  "roles": [
    "Marketing Specialist",
    "Sales Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Marketing Qualified Lead (MQL) Handover to Sales",
    "edge case",
    "exception",
    "MKT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Sales Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-MKT-005"
}
```

**Document ID:** SOP-MKT-005-EDGE-A
**Related SOP:** SOP-MKT-005 (Marketing Qualified Lead (MQL) Handover to Sales)
**Department:** Marketing

## Scenario
The designated approver (Sales Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the mql handover cannot wait for their return.

## Deviation Procedure

1. Marketing Specialist confirms the Sales Manager has an active out-of-office status in MK-MarketHub or MK-HRMS before invoking this path.
2. Marketing Specialist identifies the Sales Manager's designated delegate — typically the next role up the escalation chain (Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director) — as recorded in MK-MarketHub.
3. Marketing Specialist resubmits or flags the existing request in MK-MarketHub, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Sales Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Sales Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-MarketHub logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Marketing Qualified Lead (MQL) Handover to Sales decisions explicitly reserved for the Sales Manager by policy (e.g., anything requiring named signing authority); those must wait for the Sales Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._