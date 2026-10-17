# Edge Case: Cloud Resource Provisioning Request — When the Cloud Architect Is Unavailable

```json
{
  "document_id": "SOP-DEVOPS-003-EDGE-A",
  "title": "Edge Case: Cloud Resource Provisioning Request \u2014 When the Cloud Architect Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Cloud Infrastructure",
  "subcategory": "Cloud Resource Request",
  "roles": [
    "requester",
    "Cloud Architect"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Cloud Resource Provisioning Request",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Cloud Architect",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-003"
}
```

**Document ID:** SOP-DEVOPS-003-EDGE-A
**Related SOP:** SOP-DEVOPS-003 (Cloud Resource Provisioning Request)
**Department:** DevOps & Cloud

## Scenario
The designated approver (Cloud Architect) is on leave, travel, or otherwise unreachable within the normal response window, but the cloud resource request cannot wait for their return.

## Deviation Procedure

1. requester confirms the Cloud Architect has an active out-of-office status in MK-CloudOps or MK-HRMS before invoking this path.
2. requester identifies the Cloud Architect's designated delegate — typically the next role up the escalation chain (DevOps Engineer -> DevOps Manager -> DevOps Director) — as recorded in MK-CloudOps.
3. requester resubmits or flags the existing request in MK-CloudOps, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Cloud Architect would apply, and either approves, rejects, or requests clarification.
5. Once the Cloud Architect returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-CloudOps logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Cloud Resource Provisioning Request decisions explicitly reserved for the Cloud Architect by policy (e.g., anything requiring named signing authority); those must wait for the Cloud Architect's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: DevOps Engineer -> DevOps Manager -> DevOps Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._