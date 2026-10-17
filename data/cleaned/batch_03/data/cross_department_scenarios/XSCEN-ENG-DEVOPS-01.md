# Cross-Department Scenario (ENG + DEVOPS): A Deployment Succeeds in Staging But Fails in Production

```json
{
  "document_id": "XSCEN-ENG-DEVOPS-01",
  "title": "A Deployment Succeeds in Staging But Fails in Production",
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
    "A Deployment Succeeds in Staging But Fails in Production",
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

**Document ID:** XSCEN-ENG-DEVOPS-01
**Departments Involved:** ENG, DEVOPS

## Situation
The same build that passed staging validation fails immediately after production deployment.

## Resolution Steps

- DevOps checks whether a production-only configuration (secrets, environment variables) differs from staging.
- Engineering reviews the deployment logs for the specific failure point.
- If a configuration mismatch is found, DevOps corrects it and redeploys following the standard promotion procedure, not a manual patch.
- If the issue is code-level and staging simply didn't catch it, Engineering rolls back per the Rollback Procedure while a fix is prepared.
- The root cause is documented so the staging environment can be updated to better mirror production for this class of issue.

## Lesson
A staging/production discrepancy is itself the finding — the fix should close that gap, not just the immediate failure.

## Escalation Contacts
- ENG: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director
- DEVOPS: DevOps Engineer -> DevOps Manager -> DevOps Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._