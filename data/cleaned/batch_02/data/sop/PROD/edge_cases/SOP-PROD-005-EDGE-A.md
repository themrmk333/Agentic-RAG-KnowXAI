# Edge Case: A/B Experiment Design Procedure — When the Data Analyst Is Unavailable

```json
{
  "document_id": "SOP-PROD-005-EDGE-A",
  "title": "Edge Case: A/B Experiment Design Procedure \u2014 When the Data Analyst Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Experimentation",
  "subcategory": "Experiment Design",
  "roles": [
    "Product Manager",
    "Data Analyst"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "A/B Experiment Design Procedure",
    "edge case",
    "exception",
    "PROD"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Data Analyst",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROD-005"
}
```

**Document ID:** SOP-PROD-005-EDGE-A
**Related SOP:** SOP-PROD-005 (A/B Experiment Design Procedure)
**Department:** Product Management

## Scenario
The designated approver (Data Analyst) is on leave, travel, or otherwise unreachable within the normal response window, but the experiment design cannot wait for their return.

## Deviation Procedure

1. Product Manager confirms the Data Analyst has an active out-of-office status in MK-ProductHub or MK-HRMS before invoking this path.
2. Product Manager identifies the Data Analyst's designated delegate — typically the next role up the escalation chain (Associate Product Manager -> Product Manager -> Product Lead -> Head of Product) — as recorded in MK-ProductHub.
3. Product Manager resubmits or flags the existing request in MK-ProductHub, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Data Analyst would apply, and either approves, rejects, or requests clarification.
5. Once the Data Analyst returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-ProductHub logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to A/B Experiment Design Procedure decisions explicitly reserved for the Data Analyst by policy (e.g., anything requiring named signing authority); those must wait for the Data Analyst's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Associate Product Manager -> Product Manager -> Product Lead -> Head of Product.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._