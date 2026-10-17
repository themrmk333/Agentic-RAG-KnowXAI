# Edge Case: DevOps New Engineer Onboarding — When the DevOps Director Is Unavailable

```json
{
  "document_id": "SOP-DEVOPS-014-EDGE-A",
  "title": "Edge Case: DevOps New Engineer Onboarding \u2014 When the DevOps Director Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Onboarding",
  "subcategory": "DevOps Onboarding Plan",
  "roles": [
    "DevOps Manager",
    "DevOps Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "DevOps New Engineer Onboarding",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-014"
}
```

**Document ID:** SOP-DEVOPS-014-EDGE-A
**Related SOP:** SOP-DEVOPS-014 (DevOps New Engineer Onboarding)
**Department:** DevOps & Cloud

## Scenario
The designated approver (DevOps Director) is on leave, travel, or otherwise unreachable within the normal response window, but the devops onboarding plan cannot wait for their return.

## Deviation Procedure

1. DevOps Manager confirms the DevOps Director has an active out-of-office status in MK-CloudOps or MK-HRMS before invoking this path.
2. DevOps Manager identifies the DevOps Director's designated delegate — typically the next role up the escalation chain (DevOps Engineer -> DevOps Manager -> DevOps Director) — as recorded in MK-CloudOps.
3. DevOps Manager resubmits or flags the existing request in MK-CloudOps, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original DevOps Director would apply, and either approves, rejects, or requests clarification.
5. Once the DevOps Director returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-CloudOps logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to DevOps New Engineer Onboarding decisions explicitly reserved for the DevOps Director by policy (e.g., anything requiring named signing authority); those must wait for the DevOps Director's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: DevOps Engineer -> DevOps Manager -> DevOps Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._