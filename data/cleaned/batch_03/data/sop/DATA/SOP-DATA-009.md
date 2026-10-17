# SOP: Data Warehouse Schema Change Procedure

```json
{
  "document_id": "SOP-DATA-009",
  "title": "Data Warehouse Schema Change Procedure",
  "document_type": "SOP",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Engineering",
  "subcategory": "Schema Change",
  "roles": [
    "Data Engineer",
    "Data Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Warehouse Schema Change Procedure",
    "Data Engineering",
    "Schema Change",
    "DATA",
    "MK-DataLake"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Data Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DATA-009
**Department:** Data & Analytics
**Applicable Roles:** Data Engineer, Data Manager
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **data warehouse schema change procedure** within the Data & Analytics department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Data Engineers and any employee across MK-Infinite-AI who needs to initiate a **Schema Change** request. It covers the full workflow from initiation through to closure in MK-DataLake.

## Applicable Roles

- Primary actor: **Data Engineer**
- Approver: **Data Manager**
- System of record: **MK-DataLake**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-DataLake.
- Impact analysis on downstream dashboards and reports must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the schema change being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports.

**Step 2:** the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required.

**Step 3:** The Data Manager reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system.

**Step 5:** the Data Engineer is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-DataLake and corrected before sign-off.

**Step 7:** MK-DataLake marks the request 'Complete' and the configuration is logged for audit and future reference. Breaking schema changes are communicated to all dashboard owners a week in advance.

## Expected Result

The schema change is completed, logged in MK-DataLake, and the requester is notified of the outcome. The record remains available in MK-DataLake for future reference and audit.

## Exceptions

- Breaking schema changes are communicated to all dashboard owners a week in advance.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Data Analyst → Analytics Lead → Data Manager → Director of Data & Analytics. Escalations should reference the SOP-DATA-009 document ID and the relevant ticket/request number.

## Responsible Role

Data Engineer

## Approval Role

Data Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._