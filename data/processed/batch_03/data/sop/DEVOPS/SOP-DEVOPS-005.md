# SOP: Infrastructure as Code (IaC) Change Procedure

```json
{
  "document_id": "SOP-DEVOPS-005",
  "title": "Infrastructure as Code (IaC) Change Procedure",
  "document_type": "SOP",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Infrastructure",
  "subcategory": "IaC Change",
  "roles": [
    "DevOps Engineer",
    "Cloud Architect"
  ],
  "access_level": "manager",
  "allowed_departments": [
    "DEVOPS"
  ],
  "confidentiality": "Confidential",
  "keywords": [
    "Infrastructure as Code (IaC) Change Procedure",
    "Infrastructure",
    "IaC Change",
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

**Document ID:** SOP-DEVOPS-005  
**Department:** DevOps & Cloud  
**Applicable Roles:** DevOps Engineer, Cloud Architect  
**Access Level:** manager  
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **infrastructure as code (iac) change procedure** within the DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all DevOps Engineers and any employee across MK-Infinite-AI who needs to initiate a **IaC Change** request. It covers the full workflow from initiation through to closure in MK-CloudOps.

## Applicable Roles

- Primary actor: **DevOps Engineer**
- Approver: **Cloud Architect**
- System of record: **MK-CloudOps**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-CloudOps.
- A plan/diff output reviewed before apply must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the iac change being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** The review is scheduled in advance and stakeholders are notified through MK-CloudOps.

**Step 2:** the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply.

**Step 3:** The review team examines the IaC Change against the applicable policy or checklist.

**Step 4:** Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.

**Step 5:** The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Step 6:** Remediation actions are tracked in MK-CloudOps with due dates and status.

**Step 7:** The review is closed once all actions are completed, and the outcome is recorded for future audits. Changes to production Terraform state require a second engineer to review the plan.

## Expected Result

The iac change is completed, logged in MK-CloudOps, and the requester is notified of the outcome. The record remains available in MK-CloudOps for future reference and audit.

## Exceptions

- Changes to production Terraform state require a second engineer to review the plan.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: DevOps Engineer → DevOps Manager → DevOps Director. Escalations should reference the SOP-DEVOPS-005 document ID and the relevant ticket/request number.

## Responsible Role

DevOps Engineer

## Approval Role

Cloud Architect

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._