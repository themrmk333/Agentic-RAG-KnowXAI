# Edge Case: Patch Management for Infrastructure — When the Security Manager Is Unavailable

```json
{
  "document_id": "SOP-DEVOPS-015-EDGE-A",
  "title": "Edge Case: Patch Management for Infrastructure \u2014 When the Security Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Patch Management",
  "subcategory": "Patch Deployment",
  "roles": [
    "DevOps Engineer",
    "Security Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Patch Management for Infrastructure",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-015"
}
```

**Document ID:** SOP-DEVOPS-015-EDGE-A
**Related SOP:** SOP-DEVOPS-015 (Patch Management for Infrastructure)
**Department:** DevOps & Cloud

## Scenario
The designated approver (Security Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the patch deployment cannot wait for their return.

## Deviation Procedure

1. DevOps Engineer confirms the Security Manager has an active out-of-office status in MK-CloudOps or MK-HRMS before invoking this path.
2. DevOps Engineer identifies the Security Manager's designated delegate — typically the next role up the escalation chain (DevOps Engineer -> DevOps Manager -> DevOps Director) — as recorded in MK-CloudOps.
3. DevOps Engineer resubmits or flags the existing request in MK-CloudOps, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Security Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Security Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-CloudOps logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Patch Management for Infrastructure decisions explicitly reserved for the Security Manager by policy (e.g., anything requiring named signing authority); those must wait for the Security Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: DevOps Engineer -> DevOps Manager -> DevOps Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._