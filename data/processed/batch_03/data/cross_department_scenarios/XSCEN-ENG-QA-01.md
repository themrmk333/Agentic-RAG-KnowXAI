# Cross-Department Scenario (ENG + QA): A Feature Ships With a Known Bug QA Flagged as Non-Blocking

```json
{
  "document_id": "XSCEN-ENG-QA-01",
  "title": "A Feature Ships With a Known Bug QA Flagged as Non-Blocking",
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
    "A Feature Ships With a Known Bug QA Flagged as Non-Blocking",
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

**Document ID:** XSCEN-ENG-QA-01  
**Departments Involved:** ENG, QA

## Situation
QA flagged a minor UI bug as non-blocking before release, but customers report it as confusing post-launch.

## Resolution Steps

- Support logs the customer reports and routes them to QA and Engineering for reassessment.
- QA re-triages the bug's severity based on actual customer impact rather than the pre-launch assessment.
- If reclassified as higher severity, Engineering schedules a fix in the next available sprint or hotfix if urgent.
- QA updates its Defect Triage Meeting notes to reflect that user-facing confusion outweighs the original 'cosmetic' classification.
- The release retrospective notes that customer-facing UI issues should default to a higher severity floor going forward.

## Lesson
A pre-launch severity call isn't final — real customer impact after release can and should override it.

## Escalation Contacts
- ENG: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director
- QA: QA Engineer -> QA Lead -> QA Manager -> QA Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._