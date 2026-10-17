# Cross-Department Scenario (IT + HR): Departing Employee's HR Exit Interview Delayed by Account Lockout

```json
{
  "document_id": "XSCEN-IT-HR-02",
  "title": "Departing Employee's HR Exit Interview Delayed by Account Lockout",
  "document_type": "Cross-Department Scenario",
  "department": "IT + HR",
  "department_codes": [
    "IT",
    "HR"
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
    "Departing Employee's HR Exit Interview Delayed by Account Lockout",
    "IT",
    "HR",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "IT Director / HR Director",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-IT-HR-02
**Departments Involved:** IT, HR

## Situation
An employee's IT access was revoked before their scheduled HR exit interview because the offboarding date in MK-HRMS was entered incorrectly.

## Resolution Steps

- HR immediately flags the date error and requests temporary read-only access restoration from IT for the interview window only.
- IT verifies the request against the original signed resignation letter before restoring any access.
- Access is restored for a strictly time-boxed window (e.g., 2 hours) and automatically re-revoked afterward.
- HR corrects the offboarding date in MK-HRMS to prevent recurrence.
- Both departments log the incident as a data-entry error, not a security incident, since it was caught and contained quickly.

## Lesson
Even a well-intentioned early revocation needs a fast, controlled path back for legitimate remaining business, not a full policy exception.

## Escalation Contacts
- IT: IT Support Engineer -> IT Manager -> IT Director
- HR: HR Executive -> HR Business Partner -> HR Manager -> HR Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._