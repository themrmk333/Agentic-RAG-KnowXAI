# SOP: Analytics Tool Access Provisioning

```json
{
  "document_id": "SOP-DATA-015",
  "title": "Analytics Tool Access Provisioning",
  "document_type": "SOP",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Access",
  "subcategory": "Analytics Tool Access",
  "roles": [
    "requester",
    "Data Manager"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Analytics Tool Access Provisioning",
    "Data Access",
    "Analytics Tool Access",
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

**Document ID:** SOP-DATA-015  
**Department:** Data & Analytics  
**Applicable Roles:** requester, Data Manager  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **analytics tool access provisioning** within the Data & Analytics department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all requesters and any employee across MK-Infinite-AI who needs to initiate a **Analytics Tool Access** request. It covers the full workflow from initiation through to closure in MK-DataLake.

## Applicable Roles

- Primary actor: **requester**
- Approver: **Data Manager**
- System of record: **MK-DataLake**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-DataLake.
- The specific tool (MK-DataLake, BI dashboards) and role required must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the analytics tool access being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the requester confirms eligibility and prerequisites: the specific tool (MK-DataLake, BI dashboards) and role required.

**Step 2:** the requester raises a request in MK-DataLake specifying exactly which Analytics Tool Access is required.

**Step 3:** The Data Manager reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Analytics Tool Access in the relevant system.

**Step 5:** the requester is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-DataLake and corrected before sign-off.

**Step 7:** MK-DataLake marks the request 'Complete' and the configuration is logged for audit and future reference. Write access to production data models is limited to Data Engineers.

## Expected Result

The analytics tool access is completed, logged in MK-DataLake, and the requester is notified of the outcome. The record remains available in MK-DataLake for future reference and audit.

## Exceptions

- Write access to production data models is limited to Data Engineers.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Data Analyst → Analytics Lead → Data Manager → Director of Data & Analytics. Escalations should reference the SOP-DATA-015 document ID and the relevant ticket/request number.

## Responsible Role

requester

## Approval Role

Data Manager

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._