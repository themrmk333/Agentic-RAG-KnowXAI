# Edge Case: New Hardware/Equipment Request Procedure — When the Procurement Lead Is Unavailable

```json
{
  "document_id": "SOP-PROC-001-EDGE-A",
  "title": "Edge Case: New Hardware/Equipment Request Procedure \u2014 When the Procurement Lead Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Procurement / Purchasing",
  "department_code": "PROC",
  "category": "Requisitioning",
  "subcategory": "Purchase Requisition",
  "roles": [
    "employee",
    "Procurement Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "New Hardware/Equipment Request Procedure",
    "edge case",
    "exception",
    "PROC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Procurement Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROC-001"
}
```

**Document ID:** SOP-PROC-001-EDGE-A
**Related SOP:** SOP-PROC-001 (New Hardware/Equipment Request Procedure)
**Department:** Procurement / Purchasing

## Scenario
The designated approver (Procurement Lead) is on leave, travel, or otherwise unreachable within the normal response window, but the purchase requisition cannot wait for their return.

## Deviation Procedure

1. employee confirms the Procurement Lead has an active out-of-office status in MK-ProcureX or MK-HRMS before invoking this path.
2. employee identifies the Procurement Lead's designated delegate — typically the next role up the escalation chain (Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director) — as recorded in MK-ProcureX.
3. employee resubmits or flags the existing request in MK-ProcureX, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Procurement Lead would apply, and either approves, rejects, or requests clarification.
5. Once the Procurement Lead returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-ProcureX logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to New Hardware/Equipment Request Procedure decisions explicitly reserved for the Procurement Lead by policy (e.g., anything requiring named signing authority); those must wait for the Procurement Lead's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._