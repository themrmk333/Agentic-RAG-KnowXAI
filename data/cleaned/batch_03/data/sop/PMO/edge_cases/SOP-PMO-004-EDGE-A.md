# Edge Case: Change Request Procedure — When the PMO Lead Is Unavailable

```json
{
  "document_id": "SOP-PMO-004-EDGE-A",
  "title": "Edge Case: Change Request Procedure \u2014 When the PMO Lead Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Project Management / PMO",
  "department_code": "PMO",
  "category": "Change Management",
  "subcategory": "Change Request",
  "roles": [
    "Project Manager",
    "PMO Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Change Request Procedure",
    "edge case",
    "exception",
    "PMO"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "PMO Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-PMO-004"
}
```

**Document ID:** SOP-PMO-004-EDGE-A
**Related SOP:** SOP-PMO-004 (Change Request Procedure)
**Department:** Project Management / PMO

## Scenario
The designated approver (PMO Lead) is on leave, travel, or otherwise unreachable within the normal response window, but the change request cannot wait for their return.

## Deviation Procedure

1. Project Manager confirms the PMO Lead has an active out-of-office status in MK-PMTrack or MK-HRMS before invoking this path.
2. Project Manager identifies the PMO Lead's designated delegate — typically the next role up the escalation chain (Project Coordinator -> Project Manager -> PMO Lead -> PMO Director) — as recorded in MK-PMTrack.
3. Project Manager resubmits or flags the existing request in MK-PMTrack, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original PMO Lead would apply, and either approves, rejects, or requests clarification.
5. Once the PMO Lead returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-PMTrack logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Change Request Procedure decisions explicitly reserved for the PMO Lead by policy (e.g., anything requiring named signing authority); those must wait for the PMO Lead's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Project Coordinator -> Project Manager -> PMO Lead -> PMO Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._