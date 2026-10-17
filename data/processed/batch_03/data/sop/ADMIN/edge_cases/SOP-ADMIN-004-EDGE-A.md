# Edge Case: Facility Maintenance Request Procedure — When the Facilities Coordinator Is Unavailable

```json
{
  "document_id": "SOP-ADMIN-004-EDGE-A",
  "title": "Edge Case: Facility Maintenance Request Procedure \u2014 When the Facilities Coordinator Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Maintenance",
  "subcategory": "Maintenance Request",
  "roles": [
    "employee",
    "Facilities Coordinator"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Facility Maintenance Request Procedure",
    "edge case",
    "exception",
    "ADMIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Facilities Coordinator",
  "source": "synthetic-generated",
  "related_sop": "SOP-ADMIN-004"
}
```

**Document ID:** SOP-ADMIN-004-EDGE-A  
**Related SOP:** SOP-ADMIN-004 (Facility Maintenance Request Procedure)  
**Department:** Administration / Facilities

## Scenario
The designated approver (Facilities Coordinator) is on leave, travel, or otherwise unreachable within the normal response window, but the maintenance request cannot wait for their return.

## Deviation Procedure

1. employee confirms the Facilities Coordinator has an active out-of-office status in MK-FacilitiesDesk or MK-HRMS before invoking this path.
2. employee identifies the Facilities Coordinator's designated delegate — typically the next role up the escalation chain (Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration) — as recorded in MK-FacilitiesDesk.
3. employee resubmits or flags the existing request in MK-FacilitiesDesk, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Facilities Coordinator would apply, and either approves, rejects, or requests clarification.
5. Once the Facilities Coordinator returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-FacilitiesDesk logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Facility Maintenance Request Procedure decisions explicitly reserved for the Facilities Coordinator by policy (e.g., anything requiring named signing authority); those must wait for the Facilities Coordinator's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._