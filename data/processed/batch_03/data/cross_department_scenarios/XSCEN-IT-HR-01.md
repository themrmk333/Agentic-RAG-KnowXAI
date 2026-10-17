# Cross-Department Scenario (IT + HR): New Hire Laptop Not Ready On Day One

```json
{
  "document_id": "XSCEN-IT-HR-01",
  "title": "New Hire Laptop Not Ready On Day One",
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
    "New Hire Laptop Not Ready On Day One",
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

**Document ID:** XSCEN-IT-HR-01  
**Departments Involved:** IT, HR

## Situation
A new employee's start date was moved up by HR by three days, but IT's onboarding queue still shows the original date.

## Resolution Steps

- HR notifies IT immediately via MK-ServiceDesk (not just MK-HRMS) whenever a start date changes.
- IT treats a date-change notification as a rush request and reprioritizes the laptop build.
- If the laptop cannot be ready in time, IT issues a loaner device for day one and completes the standard build within 48 hours.
- HR informs the new hire's manager so expectations are set correctly for day one.
- IT and HR agree the root cause: start-date changes in MK-HRMS don't auto-notify MK-ServiceDesk, logged as a system-integration gap.

## Lesson
Cross-department onboarding depends on HR proactively notifying IT of any date change, not just updating its own system.

## Escalation Contacts
- IT: IT Support Engineer -> IT Manager -> IT Director
- HR: HR Executive -> HR Business Partner -> HR Manager -> HR Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._