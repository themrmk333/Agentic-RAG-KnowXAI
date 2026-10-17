# Edge Case: Infrastructure as Code (IaC) Change Procedure — MK-CloudOps Is Unavailable

```json
{
  "document_id": "SOP-DEVOPS-005-EDGE-C",
  "title": "Edge Case: Infrastructure as Code (IaC) Change Procedure \u2014 MK-CloudOps Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Infrastructure",
  "subcategory": "IaC Change",
  "roles": [
    "DevOps Engineer",
    "Cloud Architect"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Infrastructure as Code (IaC) Change Procedure",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Cloud Architect",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-005"
}
```

**Document ID:** SOP-DEVOPS-005-EDGE-C  
**Related SOP:** SOP-DEVOPS-005 (Infrastructure as Code (IaC) Change Procedure)  
**Department:** DevOps & Cloud

## Situation
MK-CloudOps is down, in scheduled maintenance, or otherwise unreachable, but the iac change genuinely cannot wait until the system is restored.

## Detection
DevOps Engineer attempts to log into MK-CloudOps and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
DevOps Engineer first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-CloudOps to be restored (the default expectation).

## Steps

1. DevOps Engineer confirms MK-CloudOps is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent iac change requests, DevOps Engineer waits for MK-CloudOps to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, DevOps Engineer documents the request details (who, what, why, when) in an email to the Cloud Architect instead of the system.
4. The Cloud Architect reviews the emailed request using the same criteria they would apply inside MK-CloudOps, and replies with an approval/rejection decision in writing.
5. Once MK-CloudOps is restored, DevOps Engineer or the Cloud Architect re-enters the request and its outcome into MK-CloudOps retroactively, referencing the original email for the audit trail.
6. MK-CloudOps's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
DevOps Engineer

## Approval
Cloud Architect

## Escalation
DevOps Engineer -> DevOps Manager -> DevOps Director

## Expected Result
The iac change is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-CloudOps once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._