# Edge Case: Production Incident Response (Engineering) — Urgent / Expedited Path

```json
{
  "document_id": "SOP-ENG-013-EDGE-B",
  "title": "Edge Case: Production Incident Response (Engineering) \u2014 Urgent / Expedited Path",
  "document_type": "SOP Edge Case",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Incident Management",
  "subcategory": "Production Incident",
  "roles": [
    "on-call Software Engineer",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Production Incident Response (Engineering)",
    "edge case",
    "exception",
    "ENG"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-ENG-013"
}
```

**Document ID:** SOP-ENG-013-EDGE-B  
**Related SOP:** SOP-ENG-013 (Production Incident Response (Engineering))  
**Department:** Software Engineering / Development

## Scenario
A genuine business emergency requires the production incident to be actioned faster than the standard SOP allows, and waiting for the full standard approval chain would cause material harm (e.g., a production outage, a compliance deadline, or a safety issue).

## Deviation Procedure

1. on-call Software Engineer clearly documents why the standard timeline in SOP-ENG-013 cannot be met, including the business impact of waiting.
2. on-call Software Engineer contacts the Engineering Manager directly (not only via MK-CodeForge) — by phone or in-person — to request verbal pre-approval.
3. On verbal pre-approval, on-call Software Engineer proceeds with the minimum necessary action to resolve the emergency, logging every action taken.
4. on-call Software Engineer files the formal request in MK-CodeForge within 24 hours of the verbal approval, marked 'Emergency — Retroactive Approval'.
5. The Engineering Manager formally reviews and signs off on the retroactive request within 2 business days, confirming the emergency justification was reasonable.
6. If the Engineering Manager finds the emergency justification insufficient, the case is escalated to Engineering Director for a policy-compliance review.

## Important Note
The expedited path is an exception, not a routine option — repeated use of this path for the same production incident type by the same requester is flagged for review by Engineering Director.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._