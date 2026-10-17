# Edge Case: Customer Complaint Handling Procedure — When the Customer Experience Director Is Unavailable

```json
{
  "document_id": "SOP-SUPPORT-015-EDGE-A",
  "title": "Edge Case: Customer Complaint Handling Procedure \u2014 When the Customer Experience Director Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Customer Relations",
  "subcategory": "Formal Complaint",
  "roles": [
    "Support Manager",
    "Customer Experience Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Customer Complaint Handling Procedure",
    "edge case",
    "exception",
    "SUPPORT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Customer Experience Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-SUPPORT-015"
}
```

**Document ID:** SOP-SUPPORT-015-EDGE-A
**Related SOP:** SOP-SUPPORT-015 (Customer Complaint Handling Procedure)
**Department:** Customer Support / Helpdesk

## Scenario
The designated approver (Customer Experience Director) is on leave, travel, or otherwise unreachable within the normal response window, but the formal complaint cannot wait for their return.

## Deviation Procedure

1. Support Manager confirms the Customer Experience Director has an active out-of-office status in MK-SupportDesk or MK-HRMS before invoking this path.
2. Support Manager identifies the Customer Experience Director's designated delegate — typically the next role up the escalation chain (Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director) — as recorded in MK-SupportDesk.
3. Support Manager resubmits or flags the existing request in MK-SupportDesk, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Customer Experience Director would apply, and either approves, rejects, or requests clarification.
5. Once the Customer Experience Director returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-SupportDesk logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Customer Complaint Handling Procedure decisions explicitly reserved for the Customer Experience Director by policy (e.g., anything requiring named signing authority); those must wait for the Customer Experience Director's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._