# Cross-Department Scenario (ENG + DEVOPS): A Hotfix Bypasses Code Review Due to Time Pressure

```json
{
  "document_id": "XSCEN-ENG-DEVOPS-03",
  "title": "A Hotfix Bypasses Code Review Due to Time Pressure",
  "document_type": "Cross-Department Scenario",
  "department": "ENG + DEVOPS",
  "department_codes": [
    "ENG",
    "DEVOPS"
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
    "A Hotfix Bypasses Code Review Due to Time Pressure",
    "ENG",
    "DEVOPS",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Director / DevOps Director",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-ENG-DEVOPS-03
**Departments Involved:** ENG, DEVOPS

## Situation
An engineer pushes a production hotfix without the normal peer review because the incident felt too urgent to wait.

## Resolution Steps

- DevOps confirms the hotfix was deployed under a declared incident, which is the only condition allowing this exception.
- The engineer documents the change and rationale immediately after deployment, not the next day.
- A peer review is still conducted retroactively within the same business day.
- If the retroactive review finds an issue, a follow-up fix is scheduled immediately.
- The incident postmortem explicitly notes that review was retroactive, for transparency in the audit trail.

## Lesson
Emergency bypasses of normal controls (like code review) still require the same rigor after the fact — just not before.

## Escalation Contacts
- ENG: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director
- DEVOPS: DevOps Engineer -> DevOps Manager -> DevOps Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._