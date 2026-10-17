# Edge Case: Customer Feedback Intake and Triage — When the Product Lead Is Unavailable

```json
{
  "document_id": "SOP-PROD-003-EDGE-A",
  "title": "Edge Case: Customer Feedback Intake and Triage \u2014 When the Product Lead Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Customer Insight",
  "subcategory": "Feedback Log",
  "roles": [
    "Product Manager",
    "Product Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Customer Feedback Intake and Triage",
    "edge case",
    "exception",
    "PROD"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Product Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROD-003"
}
```

**Document ID:** SOP-PROD-003-EDGE-A
**Related SOP:** SOP-PROD-003 (Customer Feedback Intake and Triage)
**Department:** Product Management

## Scenario
The designated approver (Product Lead) is on leave, travel, or otherwise unreachable within the normal response window, but the feedback log cannot wait for their return.

## Deviation Procedure

1. Product Manager confirms the Product Lead has an active out-of-office status in MK-ProductHub or MK-HRMS before invoking this path.
2. Product Manager identifies the Product Lead's designated delegate — typically the next role up the escalation chain (Associate Product Manager -> Product Manager -> Product Lead -> Head of Product) — as recorded in MK-ProductHub.
3. Product Manager resubmits or flags the existing request in MK-ProductHub, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Product Lead would apply, and either approves, rejects, or requests clarification.
5. Once the Product Lead returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-ProductHub logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Customer Feedback Intake and Triage decisions explicitly reserved for the Product Lead by policy (e.g., anything requiring named signing authority); those must wait for the Product Lead's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Associate Product Manager -> Product Manager -> Product Lead -> Head of Product.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._