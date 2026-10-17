# Cross-Department Scenario (ENG + QA): Release Blocked by a Single Open Sev-1 Defect Near the Deadline

```json
{
  "document_id": "XSCEN-ENG-QA-03",
  "title": "Release Blocked by a Single Open Sev-1 Defect Near the Deadline",
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
    "Release Blocked by a Single Open Sev-1 Defect Near the Deadline",
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

**Document ID:** XSCEN-ENG-QA-03  
**Departments Involved:** ENG, QA

## Situation
A Sev-1 defect is found the day before a committed release date, and Product is under pressure to ship anyway.

## Resolution Steps

- QA holds firm on its Release Sign-off Policy: no release proceeds with an open Sev-1 defect.
- Engineering and QA assess whether a targeted fix is feasible within hours versus requiring a full new test cycle.
- Product is informed of the realistic options: delay the release, or ship a reduced scope that excludes the affected feature.
- The final decision is made jointly by Engineering Manager and QA Manager, not unilaterally by Product.
- The decision and rationale are documented for the post-release retrospective regardless of which option is chosen.

## Lesson
QA's Sev-1 release block is a hard control that requires a joint Engineering/QA decision to work around, not a unilateral business override.

## Escalation Contacts
- ENG: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director
- QA: QA Engineer -> QA Lead -> QA Manager -> QA Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._