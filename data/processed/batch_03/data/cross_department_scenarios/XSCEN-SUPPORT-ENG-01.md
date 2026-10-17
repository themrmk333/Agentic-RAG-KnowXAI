# Cross-Department Scenario (SUPPORT + ENG): A Customer-Reported Bug Can't Be Reproduced by Engineering

```json
{
  "document_id": "XSCEN-SUPPORT-ENG-01",
  "title": "A Customer-Reported Bug Can't Be Reproduced by Engineering",
  "document_type": "Cross-Department Scenario",
  "department": "SUPPORT + ENG",
  "department_codes": [
    "SUPPORT",
    "ENG"
  ],
  "category": "Cross-Department Scenario",
  "roles": [
    "All Employees"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "A Customer-Reported Bug Can't Be Reproduced by Engineering",
    "SUPPORT",
    "ENG",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Customer Experience Director / Engineering Director",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-SUPPORT-ENG-01  
**Departments Involved:** SUPPORT, ENG

## Situation
Support escalates a bug report to Engineering, but Engineering cannot reproduce it with the information given.

## Resolution Steps

- Engineering sends the bug back to Support with specific additional information needed, rather than closing it as 'cannot reproduce'.
- Support follows up with the customer for exact steps, browser/device details, and timing.
- If the customer can't provide more detail, Support checks account-level logs for clues Engineering can use.
- Once sufficient detail is gathered, Engineering re-attempts reproduction with the specific customer's exact conditions.
- If still unreproducible after genuine effort, it's logged as a monitored issue rather than dismissed outright.

## Lesson
'Cannot reproduce' should trigger a request for more specific information, not an immediate close, especially for a paying customer's report.

## Escalation Contacts
- SUPPORT: Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director
- ENG: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._