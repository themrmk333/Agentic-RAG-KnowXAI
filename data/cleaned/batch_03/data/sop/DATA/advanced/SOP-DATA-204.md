# SOP: Data & Analytics Dependency Failure Recovery Procedure

```json
{
  "document_id": "SOP-DATA-204",
  "title": "Data & Analytics Dependency Failure Recovery Procedure",
  "document_type": "SOP",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Dependency Management",
  "subcategory": "Dependency Failure",
  "roles": [
    "Data Analyst",
    "Data Manager"
  ],
  "access_level": "manager",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data & Analytics Dependency Failure Recovery Procedure",
    "Dependency Management",
    "DATA",
    "advanced procedure"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Data Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DATA-204
**Department:** Data & Analytics
**Access Level:** manager

## Purpose

This advanced procedure defines how Data & Analytics handles **data & analytics dependency failure recovery procedure**, covering a scenario beyond the department's routine day-to-day operations.

## Scope

Applies to Data Analyst and Data Manager within Data & Analytics.

## Procedure

**Step 1:** the Data Analyst confirms the exact symptom, when it started, and whether it affects one system or several.

**Step 2:** the Data Analyst performs the standard first-line check: identifying which upstream system or team Data & Analytics depends on for the affected process.

**Step 3:** If the issue persists, the Data Analyst applies the documented workaround for this issue type.

**Step 4:** the Data Analyst checks whether the issue is isolated to their own account/device or is affecting other users too.

**Step 5:** If still unresolved, the Data Analyst raises a ticket in MK-DataLake categorised under 'Dependency Failure', attaching screenshots or error logs.

**Step 6:** The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.

**Step 7:** the Data Analyst confirms the fix works; the ticket is closed in MK-DataLake with the root cause logged. If the dependency is another department, Data & Analytics notifies that department's escalation contact directly rather than waiting silently.

## Exceptions
If the dependency is another department, Data & Analytics notifies that department's escalation contact directly rather than waiting silently.

## Escalation
Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

## Responsible Role
Data Analyst

## Approval Role
Data Manager

---
_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._