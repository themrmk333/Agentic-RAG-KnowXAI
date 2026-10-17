# Edge Case: Pricing Change Request Procedure — When the VP Product Is Unavailable

```json
{
  "document_id": "SOP-PROD-009-EDGE-A",
  "title": "Edge Case: Pricing Change Request Procedure \u2014 When the VP Product Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Pricing",
  "subcategory": "Pricing Change Request",
  "roles": [
    "Product Manager",
    "VP Product"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Pricing Change Request Procedure",
    "edge case",
    "exception",
    "PROD"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "VP Product",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROD-009"
}
```

**Document ID:** SOP-PROD-009-EDGE-A
**Related SOP:** SOP-PROD-009 (Pricing Change Request Procedure)
**Department:** Product Management

## Scenario
The designated approver (VP Product) is on leave, travel, or otherwise unreachable within the normal response window, but the pricing change request cannot wait for their return.

## Deviation Procedure

1. Product Manager confirms the VP Product has an active out-of-office status in MK-ProductHub or MK-HRMS before invoking this path.
2. Product Manager identifies the VP Product's designated delegate — typically the next role up the escalation chain (Associate Product Manager -> Product Manager -> Product Lead -> Head of Product) — as recorded in MK-ProductHub.
3. Product Manager resubmits or flags the existing request in MK-ProductHub, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original VP Product would apply, and either approves, rejects, or requests clarification.
5. Once the VP Product returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-ProductHub logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Pricing Change Request Procedure decisions explicitly reserved for the VP Product by policy (e.g., anything requiring named signing authority); those must wait for the VP Product's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Associate Product Manager -> Product Manager -> Product Lead -> Head of Product.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._