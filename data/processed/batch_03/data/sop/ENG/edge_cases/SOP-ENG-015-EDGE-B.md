# Edge Case: Feature Flag Rollout Procedure — Urgent / Expedited Path

```json
{
  "document_id": "SOP-ENG-015-EDGE-B",
  "title": "Edge Case: Feature Flag Rollout Procedure \u2014 Urgent / Expedited Path",
  "document_type": "SOP Edge Case",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Release Management",
  "subcategory": "Feature Flag",
  "roles": [
    "Software Engineer",
    "Product Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Feature Flag Rollout Procedure",
    "edge case",
    "exception",
    "ENG"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Product Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-ENG-015"
}
```

**Document ID:** SOP-ENG-015-EDGE-B  
**Related SOP:** SOP-ENG-015 (Feature Flag Rollout Procedure)  
**Department:** Software Engineering / Development

## Scenario
A genuine business emergency requires the feature flag to be actioned faster than the standard SOP allows, and waiting for the full standard approval chain would cause material harm (e.g., a production outage, a compliance deadline, or a safety issue).

## Deviation Procedure

1. Software Engineer clearly documents why the standard timeline in SOP-ENG-015 cannot be met, including the business impact of waiting.
2. Software Engineer contacts the Product Manager directly (not only via MK-CodeForge) — by phone or in-person — to request verbal pre-approval.
3. On verbal pre-approval, Software Engineer proceeds with the minimum necessary action to resolve the emergency, logging every action taken.
4. Software Engineer files the formal request in MK-CodeForge within 24 hours of the verbal approval, marked 'Emergency — Retroactive Approval'.
5. The Product Manager formally reviews and signs off on the retroactive request within 2 business days, confirming the emergency justification was reasonable.
6. If the Product Manager finds the emergency justification insufficient, the case is escalated to Engineering Director for a policy-compliance review.

## Important Note
The expedited path is an exception, not a routine option — repeated use of this path for the same feature flag type by the same requester is flagged for review by Engineering Director.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._