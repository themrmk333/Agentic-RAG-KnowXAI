# SOP: Data Retention and Deletion Procedure

```json
{
  "document_id": "SOP-DATA-008",
  "title": "Data Retention and Deletion Procedure",
  "document_type": "SOP",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Governance",
  "subcategory": "Data Retention Review",
  "roles": [
    "Data Manager",
    "Director of Data & Analytics"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "DATA"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Retention and Deletion Procedure",
    "Data Governance",
    "Data Retention Review",
    "DATA",
    "MK-DataLake"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Director of Data & Analytics",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DATA-008  
**Department:** Data & Analytics  
**Applicable Roles:** Data Manager, Director of Data & Analytics  
**Access Level:** employee  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **data retention and deletion procedure** within the Data & Analytics department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Data Managers and any employee across MK-Infinite-AI who needs to initiate a **Data Retention Review** request. It covers the full workflow from initiation through to closure in MK-DataLake.

## Applicable Roles

- Primary actor: **Data Manager**
- Approver: **Director of Data & Analytics**
- System of record: **MK-DataLake**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-DataLake.
- Checking each dataset against the retention schedule defined by Legal must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the data retention review being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** The review is scheduled in advance and stakeholders are notified through MK-DataLake.

**Step 2:** the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal.

**Step 3:** The review team examines the Data Retention Review against the applicable policy or checklist.

**Step 4:** Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.

**Step 5:** The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Step 6:** Remediation actions are tracked in MK-DataLake with due dates and status.

**Step 7:** The review is closed once all actions are completed, and the outcome is recorded for future audits. Deletion of data under legal hold is blocked until the hold is lifted.

## Expected Result

The data retention review is completed, logged in MK-DataLake, and the requester is notified of the outcome. The record remains available in MK-DataLake for future reference and audit.

## Exceptions

- Deletion of data under legal hold is blocked until the hold is lifted.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Data Analyst → Analytics Lead → Data Manager → Director of Data & Analytics. Escalations should reference the SOP-DATA-008 document ID and the relevant ticket/request number.

## Responsible Role

Data Manager

## Approval Role

Director of Data & Analytics

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._