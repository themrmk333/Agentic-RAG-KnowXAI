# Edge Case: Infrastructure as Code (IaC) Change Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-DEVOPS-005-EDGE-E",
  "title": "Edge Case: Infrastructure as Code (IaC) Change Procedure \u2014 Missing Documentation or Incorrect Submission",
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

**Document ID:** SOP-DEVOPS-005-EDGE-E  
**Related SOP:** SOP-DEVOPS-005 (Infrastructure as Code (IaC) Change Procedure)  
**Department:** DevOps & Cloud

## Situation
DevOps Engineer submits a iac change request in MK-CloudOps that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Cloud Architect reviewing the request in MK-CloudOps notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Cloud Architect decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Cloud Architect does not approve or silently correct the request themselves; they return it to DevOps Engineer in MK-CloudOps with a specific note on what's missing or wrong.
2. DevOps Engineer is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. DevOps Engineer corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Cloud Architect reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Cloud Architect flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-DEVOPS-005.

## Responsible Role
DevOps Engineer

## Approval
Cloud Architect

## Escalation
DevOps Engineer -> DevOps Manager -> DevOps Director

## Expected Result
Incomplete or incorrect iac change requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._