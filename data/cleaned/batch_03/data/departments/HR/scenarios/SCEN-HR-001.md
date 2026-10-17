# Scenario: Approval Delay Escalation in Human Resources

```json
{
  "document_id": "SCEN-HR-001",
  "title": "Scenario: Approval Delay Escalation in Human Resources",
  "document_type": "Approval/Escalation Scenario",
  "department": "Human Resources",
  "department_code": "HR",
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
    "Scenario: Approval Delay Escalation in Human Resources",
    "escalation",
    "scenario",
    "HR"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "HR Director",
  "source": "synthetic-generated"
}
```

**Document ID:** SCEN-HR-001
**Department:** Human Resources

## Situation
An employee submitted a routine request in MK-HRMS five business days ago. The assigned approver (HR Business Partner) has not actioned it, and the delay is now affecting the employee's ability to complete their own work.

## Timeline / Walkthrough

- Day 1: The employee submits the request in MK-HRMS following the standard SOP for that request type.
- Day 3: No action has been taken. The employee sends a polite follow-up directly to the approver, referencing the MK-HRMS ticket/request ID.
- Day 5: Still no response. The employee escalates one level up the chain — to HR Manager — per the department's documented escalation path: HR Executive -> HR Business Partner -> HR Manager -> HR Director.
- Day 5 (same day): HR Manager reviews the request, either actions it directly or identifies the original approver's delegate.
- Day 6: The request is approved (or rejected with a clear reason) and the employee is notified.
- Follow-up: The department lead (Human Resources contact Ananya Sharma, ananya.sharma@mkinfinite-ai.com) reviews why the SLA was missed and whether a process gap needs fixing (e.g., missing delegate coverage during leave).

**Lesson:** Escalation paths exist precisely for this situation — waiting indefinitely without escalating is itself considered a process mistake at MK-Infinite-AI. The documented path (HR Executive -> HR Business Partner -> HR Manager -> HR Director) should always be used rather than repeatedly re-sending the same request to the same unresponsive approver.

---
_This scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._