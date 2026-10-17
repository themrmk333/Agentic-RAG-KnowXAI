# SOP: Cloud Resource Provisioning Request

```json
{
  "document_id": "SOP-DEVOPS-003",
  "title": "Cloud Resource Provisioning Request",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Cloud Infrastructure",
  "subcategory": "Cloud Resource Request",
  "roles": [
    "requester",
    "Cloud Architect"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Cloud Resource Provisioning Request",
    "Cloud Infrastructure",
    "Cloud Resource Request",
    "DEVOPS",
    "MK-CloudOps"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Cloud Architect",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-DEVOPS-003  
**Department:** DevOps & Cloud  
**Applicable Roles:** requester, Cloud Architect  
**Access Level:** general  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **cloud resource provisioning request** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all requesters and any employee across MK-Infinite-AI who needs to initiate a **Cloud Resource Request** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **requester**
- Approver: **Cloud Architect**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- Resource type, sizing, environment, and estimated monthly cost must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the cloud resource request being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section.

**Step 2:** the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost.

**Step 3:** the requester attaches any supporting documentation and reviews the entry for accuracy before submitting.

**Step 4:** the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review.

**Step 5:** The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Step 6:** On approval, MK-CloudOps updates the status to 'Approved' and notifies the requester by email/in-app notification.

**Step 7:** The approved Cloud Resource Request is processed and the record is retained in MK-CloudOps for audit purposes. Resources exceeding budget thresholds require Finance co-approval.

## Expected Result

The cloud resource request is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Resources exceeding budget thresholds require Finance co-approval.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-003 document ID and the relevant ticket/request number.

## Responsible Role

requester

## Approval Role

Cloud Architect

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._