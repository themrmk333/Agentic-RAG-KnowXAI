# SOP: Data Quality Issue Resolution Procedure

```json
{
  "document_id": "SOP-DATA-004",
  "title": "Data Quality Issue Resolution Procedure",
  "document_type": "SOP",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Quality",
  "subcategory": "Data Quality Incident",
  "roles": [
    "Data Analyst",
    "Analytics Lead"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Quality Issue Resolution Procedure",
    "Data Quality",
    "Data Quality Incident",
    "DATA",
    "MK-DataLake"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Analytics Lead",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DATA-004
**Department:** Data & Analytics
**Applicable Roles:** Data Analyst, Analytics Lead
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **data quality issue resolution procedure** within the Data & Analytics department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Data Analysts and any employee across MK-Infinite-AI who needs to initiate a **Data Quality Incident** request. It covers the full workflow from initiation through to closure in MK-DataLake.

## Applicable Roles

- Primary actor: **Data Analyst**
- Approver: **Analytics Lead**
- System of record: **MK-DataLake**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-DataLake.
- Identifying the affected table and the scope of impacted reports must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the data quality incident being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the Data Analyst confirms the exact symptom, when it started, and whether it affects one system or several.

**Step 2:** the Data Analyst performs the standard first-line check: identifying the affected table and the scope of impacted reports.

**Step 3:** If the issue persists, the Data Analyst applies the documented workaround for this issue type.

**Step 4:** the Data Analyst checks whether the issue is isolated to their own account/device or is affecting other users too.

**Step 5:** If still unresolved, the Data Analyst raises a ticket in MK-DataLake categorised under 'Data Quality Incident', attaching screenshots or error logs.

**Step 6:** The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.

**Step 7:** the Data Analyst confirms the fix works; the ticket is closed in MK-DataLake with the root cause logged. Data quality incidents affecting Finance reporting are flagged to Finance immediately.

## Expected Result

The data quality incident is completed, logged in MK-DataLake, and the requester is notified of the outcome. The record remains available in MK-DataLake for future reference and audit.

## Exceptions

- Data quality incidents affecting Finance reporting are flagged to Finance immediately.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Data Analyst → Analytics Lead → Data Manager → Director of Data & Analytics. Escalations should reference the SOP-DATA-004 document ID and the relevant ticket/request number.

## Responsible Role

Data Analyst

## Approval Role

Analytics Lead

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._