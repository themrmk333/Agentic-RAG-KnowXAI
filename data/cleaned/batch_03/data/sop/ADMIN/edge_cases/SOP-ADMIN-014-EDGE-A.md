# Edge Case: Office Budget and Vendor Invoice Approval (Admin) — When the Finance Manager Is Unavailable

```json
{
  "document_id": "SOP-ADMIN-014-EDGE-A",
  "title": "Edge Case: Office Budget and Vendor Invoice Approval (Admin) \u2014 When the Finance Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Budget Management",
  "subcategory": "Admin Invoice Approval",
  "roles": [
    "Facilities Manager",
    "Finance Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Office Budget and Vendor Invoice Approval (Admin)",
    "edge case",
    "exception",
    "ADMIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-ADMIN-014"
}
```

**Document ID:** SOP-ADMIN-014-EDGE-A
**Related SOP:** SOP-ADMIN-014 (Office Budget and Vendor Invoice Approval (Admin))
**Department:** Administration / Facilities

## Scenario
The designated approver (Finance Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the admin invoice approval cannot wait for their return.

## Deviation Procedure

1. Facilities Manager confirms the Finance Manager has an active out-of-office status in MK-FacilitiesDesk or MK-HRMS before invoking this path.
2. Facilities Manager identifies the Finance Manager's designated delegate — typically the next role up the escalation chain (Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration) — as recorded in MK-FacilitiesDesk.
3. Facilities Manager resubmits or flags the existing request in MK-FacilitiesDesk, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Finance Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Finance Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-FacilitiesDesk logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Office Budget and Vendor Invoice Approval (Admin) decisions explicitly reserved for the Finance Manager by policy (e.g., anything requiring named signing authority); those must wait for the Finance Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._