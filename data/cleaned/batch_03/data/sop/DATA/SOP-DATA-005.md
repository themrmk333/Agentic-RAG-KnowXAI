# SOP: Data Classification for Analytics Datasets

```json
{
  "document_id": "SOP-DATA-005",
  "title": "Data Classification for Analytics Datasets",
  "document_type": "SOP",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Governance",
  "subcategory": "Dataset Classification",
  "roles": [
    "Data Analyst",
    "Security Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "DATA"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Classification for Analytics Datasets",
    "Data Governance",
    "Dataset Classification",
    "DATA",
    "MK-DataLake"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Manager",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DATA-005
**Department:** Data & Analytics
**Applicable Roles:** Data Analyst, Security Manager
**Access Level:** employee
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **data classification for analytics datasets** within the Data & Analytics department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Data Analysts and any employee across MK-Infinite-AI who needs to initiate a **Dataset Classification** request. It covers the full workflow from initiation through to closure in MK-DataLake.

## Applicable Roles

- Primary actor: **Data Analyst**
- Approver: **Security Manager**
- System of record: **MK-DataLake**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-DataLake.
- Applying the correct sensitivity label before granting broader access must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the dataset classification being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access.

**Step 2:** the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required.

**Step 3:** The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system.

**Step 5:** the Data Analyst is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-DataLake and corrected before sign-off.

**Step 7:** MK-DataLake marks the request 'Complete' and the configuration is logged for audit and future reference. Personally identifiable fields are masked in any broadly shared dataset.

## Expected Result

The dataset classification is completed, logged in MK-DataLake, and the requester is notified of the outcome. The record remains available in MK-DataLake for future reference and audit.

## Exceptions

- Personally identifiable fields are masked in any broadly shared dataset.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Data Analyst → Analytics Lead → Data Manager → Director of Data & Analytics. Escalations should reference the SOP-DATA-005 document ID and the relevant ticket/request number.

## Responsible Role

Data Analyst

## Approval Role

Security Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._