# Edge Case: Environment Promotion Procedure (Dev → Staging → Prod) — Urgent / Expedited Path

```json
{
  "document_id": "SOP-DEVOPS-011-EDGE-B",
  "title": "Edge Case: Environment Promotion Procedure (Dev \u2192 Staging \u2192 Prod) \u2014 Urgent / Expedited Path",
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

**Document ID:** SOP-DEVOPS-011-EDGE-B  
**Related SOP:** SOP-DEVOPS-011 (Environment Promotion Procedure (Dev → Staging → Prod))  
**Department:** DevOps & Cloud

## Scenario
A genuine business emergency requires the promotion request to be actioned faster than the standard SOP allows, and waiting for the full standard approval chain would cause material harm (e.g., a production outage, a compliance deadline, or a safety issue).

## Deviation Procedure

1. DevOps Engineer clearly documents why the standard timeline in SOP-DEVOPS-011 cannot be met, including the business impact of waiting.
2. DevOps Engineer contacts the Engineering Manager directly (not only via MK-CloudOps) — by phone or in-person — to request verbal pre-approval.
3. On verbal pre-approval, DevOps Engineer proceeds with the minimum necessary action to resolve the emergency, logging every action taken.
4. DevOps Engineer files the formal request in MK-CloudOps within 24 hours of the verbal approval, marked 'Emergency — Retroactive Approval'.
5. The Engineering Manager formally reviews and signs off on the retroactive request within 2 business days, confirming the emergency justification was reasonable.
6. If the Engineering Manager finds the emergency justification insufficient, the case is escalated to DevOps Director for a policy-compliance review.

## Important Note
The expedited path is an exception, not a routine option — repeated use of this path for the same promotion request type by the same requester is flagged for review by DevOps Director.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: DevOps Engineer -> DevOps Manager -> DevOps Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._