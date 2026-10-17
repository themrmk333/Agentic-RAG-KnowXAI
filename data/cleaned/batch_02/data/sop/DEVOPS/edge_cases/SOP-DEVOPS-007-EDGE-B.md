# Edge Case: Backup and Disaster Recovery Test — Urgent / Expedited Path

```json
{
  "document_id": "SOP-DEVOPS-007-EDGE-B",
  "title": "Edge Case: Backup and Disaster Recovery Test \u2014 Urgent / Expedited Path",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Disaster Recovery",
  "subcategory": "DR Test",
  "roles": [
    "Site Reliability Engineer",
    "DevOps Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Backup and Disaster Recovery Test",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-007"
}
```

**Document ID:** SOP-DEVOPS-007-EDGE-B
**Related SOP:** SOP-DEVOPS-007 (Backup and Disaster Recovery Test)
**Department:** DevOps & Cloud

## Scenario
A genuine business emergency requires the dr test to be actioned faster than the standard SOP allows, and waiting for the full standard approval chain would cause material harm (e.g., a production outage, a compliance deadline, or a safety issue).

## Deviation Procedure

1. Site Reliability Engineer clearly documents why the standard timeline in SOP-DEVOPS-007 cannot be met, including the business impact of waiting.
2. Site Reliability Engineer contacts the DevOps Manager directly (not only via MK-CloudOps) — by phone or in-person — to request verbal pre-approval.
3. On verbal pre-approval, Site Reliability Engineer proceeds with the minimum necessary action to resolve the emergency, logging every action taken.
4. Site Reliability Engineer files the formal request in MK-CloudOps within 24 hours of the verbal approval, marked 'Emergency — Retroactive Approval'.
5. The DevOps Manager formally reviews and signs off on the retroactive request within 2 business days, confirming the emergency justification was reasonable.
6. If the DevOps Manager finds the emergency justification insufficient, the case is escalated to DevOps Director for a policy-compliance review.

## Important Note
The expedited path is an exception, not a routine option — repeated use of this path for the same dr test type by the same requester is flagged for review by DevOps Director.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: DevOps Engineer -> DevOps Manager -> DevOps Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._