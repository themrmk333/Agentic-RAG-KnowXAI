# Edge Case: Environment Promotion Procedure (Dev → Staging → Prod) — When the Engineering Manager Is Unavailable

```json
{
  "document_id": "SOP-DEVOPS-011-EDGE-A",
  "title": "Edge Case: Environment Promotion Procedure (Dev \u2192 Staging \u2192 Prod) \u2014 When the Engineering Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Release Management",
  "subcategory": "Promotion Request",
  "roles": [
    "DevOps Engineer",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Environment Promotion Procedure (Dev \u2192 Staging \u2192 Prod)",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-011"
}
```

**Document ID:** SOP-DEVOPS-011-EDGE-A
**Related SOP:** SOP-DEVOPS-011 (Environment Promotion Procedure (Dev → Staging → Prod))
**Department:** DevOps & Cloud

## Scenario
The designated approver (Engineering Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the promotion request cannot wait for their return.

## Deviation Procedure

1. DevOps Engineer confirms the Engineering Manager has an active out-of-office status in MK-CloudOps or MK-HRMS before invoking this path.
2. DevOps Engineer identifies the Engineering Manager's designated delegate — typically the next role up the escalation chain (DevOps Engineer -> DevOps Manager -> DevOps Director) — as recorded in MK-CloudOps.
3. DevOps Engineer resubmits or flags the existing request in MK-CloudOps, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Engineering Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Engineering Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-CloudOps logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Environment Promotion Procedure (Dev → Staging → Prod) decisions explicitly reserved for the Engineering Manager by policy (e.g., anything requiring named signing authority); those must wait for the Engineering Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: DevOps Engineer -> DevOps Manager -> DevOps Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._