# Edge Case: Product Risk & Compliance Review — When the Legal Manager Is Unavailable

```json
{
  "document_id": "SOP-PROD-016-EDGE-A",
  "title": "Edge Case: Product Risk & Compliance Review \u2014 When the Legal Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Compliance",
  "subcategory": "Product Compliance Review",
  "roles": [
    "Product Manager",
    "Legal Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Product Risk & Compliance Review",
    "edge case",
    "exception",
    "PROD"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Legal Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROD-016"
}
```

**Document ID:** SOP-PROD-016-EDGE-A
**Related SOP:** SOP-PROD-016 (Product Risk & Compliance Review)
**Department:** Product Management

## Scenario
The designated approver (Legal Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the product compliance review cannot wait for their return.

## Deviation Procedure

1. Product Manager confirms the Legal Manager has an active out-of-office status in MK-ProductHub or MK-HRMS before invoking this path.
2. Product Manager identifies the Legal Manager's designated delegate — typically the next role up the escalation chain (Associate Product Manager -> Product Manager -> Product Lead -> Head of Product) — as recorded in MK-ProductHub.
3. Product Manager resubmits or flags the existing request in MK-ProductHub, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Legal Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Legal Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-ProductHub logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Product Risk & Compliance Review decisions explicitly reserved for the Legal Manager by policy (e.g., anything requiring named signing authority); those must wait for the Legal Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Associate Product Manager -> Product Manager -> Product Lead -> Head of Product.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._