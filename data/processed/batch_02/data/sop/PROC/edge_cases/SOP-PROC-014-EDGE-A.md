# Edge Case: Recurring Vendor Payment Setup — When the Finance Manager Is Unavailable

```json
{
  "document_id": "SOP-PROC-014-EDGE-A",
  "title": "Edge Case: Recurring Vendor Payment Setup \u2014 When the Finance Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Procurement / Purchasing",
  "department_code": "PROC",
  "category": "Vendor Payments",
  "subcategory": "Recurring Payment Setup",
  "roles": [
    "Procurement Executive",
    "Finance Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Recurring Vendor Payment Setup",
    "edge case",
    "exception",
    "PROC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROC-014"
}
```

**Document ID:** SOP-PROC-014-EDGE-A  
**Related SOP:** SOP-PROC-014 (Recurring Vendor Payment Setup)  
**Department:** Procurement / Purchasing

## Scenario
The designated approver (Finance Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the recurring payment setup cannot wait for their return.

## Deviation Procedure

1. Procurement Executive confirms the Finance Manager has an active out-of-office status in MK-ProcureX or MK-HRMS before invoking this path.
2. Procurement Executive identifies the Finance Manager's designated delegate — typically the next role up the escalation chain (Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director) — as recorded in MK-ProcureX.
3. Procurement Executive resubmits or flags the existing request in MK-ProcureX, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Finance Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Finance Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-ProcureX logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Recurring Vendor Payment Setup decisions explicitly reserved for the Finance Manager by policy (e.g., anything requiring named signing authority); those must wait for the Finance Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._