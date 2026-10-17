# Cross-Department Scenario (IT + HR): Manager Requests IT Access for an Employee Who Hasn't Completed HR Onboarding

```json
{
  "document_id": "XSCEN-IT-HR-03",
  "title": "Manager Requests IT Access for an Employee Who Hasn't Completed HR Onboarding",
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
    "Manager Requests IT Access for an Employee Who Hasn't Completed HR Onboarding",
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

**Document ID:** XSCEN-IT-HR-03
**Departments Involved:** IT, HR

## Situation
A manager asks IT directly to grant system access for a new employee before HR has completed background verification.

## Resolution Steps

- IT checks MK-HRMS for onboarding completion status before granting any access, regardless of manager urgency.
- If onboarding is incomplete, IT declines and redirects the manager to HR to confirm status.
- HR expedites the background verification if genuinely urgent, following the Background Verification Procedure.
- Once HR confirms completion in MK-HRMS, IT proceeds with standard onboarding access provisioning.
- The manager is reminded that IT access provisioning is gated on HR onboarding completion, not manager request alone.

## Lesson
IT access provisioning is intentionally gated by HR's own onboarding completion status as a control, not a bureaucratic delay.

## Escalation Contacts
- IT: IT Support Engineer -> IT Manager -> IT Director
- HR: HR Executive -> HR Business Partner -> HR Manager -> HR Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._