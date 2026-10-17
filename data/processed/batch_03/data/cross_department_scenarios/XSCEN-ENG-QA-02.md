# Cross-Department Scenario (ENG + QA): QA Can't Reproduce a Bug Engineering Marked as Fixed

```json
{
  "document_id": "XSCEN-ENG-QA-02",
  "title": "QA Can't Reproduce a Bug Engineering Marked as Fixed",
  "document_type": "Cross-Department Scenario",
  "department": "ENG + QA",
  "department_codes": [
    "ENG",
    "QA"
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
    "QA Can't Reproduce a Bug Engineering Marked as Fixed",
    "ENG",
    "QA",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Director / QA Director",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-ENG-QA-02  
**Departments Involved:** ENG, QA

## Situation
Engineering closes a bug as fixed, but QA's regression test still reproduces the original issue.

## Resolution Steps

- QA reopens the defect in the shared tracker rather than filing a new one, to preserve history.
- QA attaches the exact reproduction steps and environment details used in the failed verification.
- Engineering re-investigates, checking whether the fix was deployed to the environment QA tested against.
- If it's an environment mismatch, DevOps is looped in to confirm the correct build is deployed to the test environment.
- Once genuinely fixed, QA re-verifies and closes the defect with the verification evidence attached.

## Lesson
A 'reopened, not duplicated' defect keeps the full history intact and avoids losing context across two separate tickets.

## Escalation Contacts
- ENG: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director
- QA: QA Engineer -> QA Lead -> QA Manager -> QA Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._