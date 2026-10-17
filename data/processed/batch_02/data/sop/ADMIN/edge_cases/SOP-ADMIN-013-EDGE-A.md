# Edge Case: Emergency Evacuation Procedure — When the Head of Administration Is Unavailable

```json
{
  "document_id": "SOP-ADMIN-013-EDGE-A",
  "title": "Edge Case: Emergency Evacuation Procedure \u2014 When the Head of Administration Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Health & Safety",
  "subcategory": "Emergency Evacuation",
  "roles": [
    "Facilities Coordinator",
    "Head of Administration"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Emergency Evacuation Procedure",
    "edge case",
    "exception",
    "ADMIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Head of Administration",
  "source": "synthetic-generated",
  "related_sop": "SOP-ADMIN-013"
}
```

**Document ID:** SOP-ADMIN-013-EDGE-A  
**Related SOP:** SOP-ADMIN-013 (Emergency Evacuation Procedure)  
**Department:** Administration / Facilities

## Scenario
The designated approver (Head of Administration) is on leave, travel, or otherwise unreachable within the normal response window, but the emergency evacuation cannot wait for their return.

## Deviation Procedure

1. Facilities Coordinator confirms the Head of Administration has an active out-of-office status in MK-FacilitiesDesk or MK-HRMS before invoking this path.
2. Facilities Coordinator identifies the Head of Administration's designated delegate — typically the next role up the escalation chain (Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration) — as recorded in MK-FacilitiesDesk.
3. Facilities Coordinator resubmits or flags the existing request in MK-FacilitiesDesk, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Head of Administration would apply, and either approves, rejects, or requests clarification.
5. Once the Head of Administration returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-FacilitiesDesk logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Emergency Evacuation Procedure decisions explicitly reserved for the Head of Administration by policy (e.g., anything requiring named signing authority); those must wait for the Head of Administration's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._