# Edge Case: Cost Optimization Review — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-DEVOPS-013-EDGE-E",
  "title": "Edge Case: Cost Optimization Review \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Cost Management",
  "subcategory": "Cloud Cost Report",
  "roles": [
    "Cloud Architect",
    "DevOps Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Cost Optimization Review",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-013"
}
```

**Document ID:** SOP-DEVOPS-013-EDGE-E
**Related SOP:** SOP-DEVOPS-013 (Cost Optimization Review)
**Department:** DevOps & Cloud

## Situation
Cloud Architect submits a cloud cost report request in MK-CloudOps that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The DevOps Director reviewing the request in MK-CloudOps notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The DevOps Director decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The DevOps Director does not approve or silently correct the request themselves; they return it to Cloud Architect in MK-CloudOps with a specific note on what's missing or wrong.
2. Cloud Architect is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Cloud Architect corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The DevOps Director reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the DevOps Director flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-DEVOPS-013.

## Responsible Role
Cloud Architect

## Approval
DevOps Director

## Escalation
DevOps Engineer -> DevOps Manager -> DevOps Director

## Expected Result
Incomplete or incorrect cloud cost report requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._