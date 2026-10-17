# Edge Case: Marketing Automation Workflow Setup — When the Marketing Manager Is Unavailable

```json
{
  "document_id": "SOP-MKT-016-EDGE-A",
  "title": "Edge Case: Marketing Automation Workflow Setup \u2014 When the Marketing Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Marketing",
  "department_code": "MKT",
  "category": "Marketing Automation",
  "subcategory": "Automation Workflow",
  "roles": [
    "Marketing Specialist",
    "Marketing Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Marketing Automation Workflow Setup",
    "edge case",
    "exception",
    "MKT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Marketing Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-MKT-016"
}
```

**Document ID:** SOP-MKT-016-EDGE-A
**Related SOP:** SOP-MKT-016 (Marketing Automation Workflow Setup)
**Department:** Marketing

## Scenario
The designated approver (Marketing Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the automation workflow cannot wait for their return.

## Deviation Procedure

1. Marketing Specialist confirms the Marketing Manager has an active out-of-office status in MK-MarketHub or MK-HRMS before invoking this path.
2. Marketing Specialist identifies the Marketing Manager's designated delegate — typically the next role up the escalation chain (Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director) — as recorded in MK-MarketHub.
3. Marketing Specialist resubmits or flags the existing request in MK-MarketHub, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Marketing Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Marketing Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-MarketHub logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Marketing Automation Workflow Setup decisions explicitly reserved for the Marketing Manager by policy (e.g., anything requiring named signing authority); those must wait for the Marketing Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._