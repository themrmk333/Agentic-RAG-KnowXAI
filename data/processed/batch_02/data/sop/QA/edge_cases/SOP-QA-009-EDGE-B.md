# Edge Case: Defect Triage Meeting Procedure — Urgent / Expedited Path

```json
{
  "document_id": "SOP-QA-009-EDGE-B",
  "title": "Edge Case: Defect Triage Meeting Procedure \u2014 Urgent / Expedited Path",
  "document_type": "SOP Edge Case",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Defect Management",
  "subcategory": "Defect Triage",
  "roles": [
    "QA Lead",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Defect Triage Meeting Procedure",
    "edge case",
    "exception",
    "QA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-QA-009"
}
```

**Document ID:** SOP-QA-009-EDGE-B  
**Related SOP:** SOP-QA-009 (Defect Triage Meeting Procedure)  
**Department:** QA / Testing

## Scenario
A genuine business emergency requires the defect triage to be actioned faster than the standard SOP allows, and waiting for the full standard approval chain would cause material harm (e.g., a production outage, a compliance deadline, or a safety issue).

## Deviation Procedure

1. QA Lead clearly documents why the standard timeline in SOP-QA-009 cannot be met, including the business impact of waiting.
2. QA Lead contacts the Engineering Manager directly (not only via MK-TestHub) — by phone or in-person — to request verbal pre-approval.
3. On verbal pre-approval, QA Lead proceeds with the minimum necessary action to resolve the emergency, logging every action taken.
4. QA Lead files the formal request in MK-TestHub within 24 hours of the verbal approval, marked 'Emergency — Retroactive Approval'.
5. The Engineering Manager formally reviews and signs off on the retroactive request within 2 business days, confirming the emergency justification was reasonable.
6. If the Engineering Manager finds the emergency justification insufficient, the case is escalated to QA Director for a policy-compliance review.

## Important Note
The expedited path is an exception, not a routine option — repeated use of this path for the same defect triage type by the same requester is flagged for review by QA Director.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: QA Engineer -> QA Lead -> QA Manager -> QA Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._