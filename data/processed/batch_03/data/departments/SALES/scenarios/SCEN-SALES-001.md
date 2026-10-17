# Scenario: Approval Delay Escalation in Sales

```json
{
  "document_id": "SCEN-SALES-001",
  "title": "Scenario: Approval Delay Escalation in Sales",
  "document_type": "Approval/Escalation Scenario",
  "department": "Sales",
  "department_code": "SALES",
  "category": "Escalation Scenario",
  "roles": [
    "All Employees"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Scenario: Approval Delay Escalation in Sales",
    "escalation",
    "scenario",
    "SALES"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Sales Director",
  "source": "synthetic-generated"
}
```

**Document ID:** SCEN-SALES-001  
**Department:** Sales

## Situation
An employee submitted a routine request in MK-CRM five business days ago. The assigned approver (Sales Team Lead) has not actioned it, and the delay is now affecting the employee's ability to complete their own work.

## Timeline / Walkthrough

- Day 1: The employee submits the request in MK-CRM following the standard SOP for that request type.
- Day 3: No action has been taken. The employee sends a polite follow-up directly to the approver, referencing the MK-CRM ticket/request ID.
- Day 5: Still no response. The employee escalates one level up the chain — to Sales Manager — per the department's documented escalation path: Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director.
- Day 5 (same day): Sales Manager reviews the request, either actions it directly or identifies the original approver's delegate.
- Day 6: The request is approved (or rejected with a clear reason) and the employee is notified.
- Follow-up: The department lead (Sales contact Harsh Bose, harsh.bose@mkinfinite-ai.com) reviews why the SLA was missed and whether a process gap needs fixing (e.g., missing delegate coverage during leave).

**Lesson:** Escalation paths exist precisely for this situation — waiting indefinitely without escalating is itself considered a process mistake at MK-Infinite-AI. The documented path (Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director) should always be used rather than repeatedly re-sending the same request to the same unresponsive approver.

---
_This scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._