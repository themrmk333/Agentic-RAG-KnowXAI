# Edge Case: Vendor Payment Procedure — When the Finance Manager Is Unavailable

```json
{
  "document_id": "SOP-FIN-005-EDGE-A",
  "title": "Edge Case: Vendor Payment Procedure \u2014 When the Finance Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Finance & Accounting",
  "department_code": "FIN",
  "category": "Accounts Payable",
  "subcategory": "Vendor Payment",
  "roles": [
    "Accountant",
    "Finance Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Vendor Payment Procedure",
    "edge case",
    "exception",
    "FIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-FIN-005"
}
```

**Document ID:** SOP-FIN-005-EDGE-A  
**Related SOP:** SOP-FIN-005 (Vendor Payment Procedure)  
**Department:** Finance & Accounting

## Scenario
The designated approver (Finance Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the vendor payment cannot wait for their return.

## Deviation Procedure

1. Accountant confirms the Finance Manager has an active out-of-office status in MK-Finance360 or MK-HRMS before invoking this path.
2. Accountant identifies the Finance Manager's designated delegate — typically the next role up the escalation chain (Accountant -> Finance Lead -> Finance Manager -> Finance Director) — as recorded in MK-Finance360.
3. Accountant resubmits or flags the existing request in MK-Finance360, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Finance Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Finance Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-Finance360 logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Vendor Payment Procedure decisions explicitly reserved for the Finance Manager by policy (e.g., anything requiring named signing authority); those must wait for the Finance Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Accountant -> Finance Lead -> Finance Manager -> Finance Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._