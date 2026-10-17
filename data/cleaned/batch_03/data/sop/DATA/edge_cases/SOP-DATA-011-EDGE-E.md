# Edge Case: Data Onboarding for New Team Members — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-DATA-011-EDGE-E",
  "title": "Edge Case: Data Onboarding for New Team Members \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Onboarding",
  "subcategory": "Data Onboarding",
  "roles": [
    "Data Manager",
    "Director of Data & Analytics"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Onboarding for New Team Members",
    "edge case",
    "exception",
    "DATA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Director of Data & Analytics",
  "source": "synthetic-generated",
  "related_sop": "SOP-DATA-011"
}
```

**Document ID:** SOP-DATA-011-EDGE-E
**Related SOP:** SOP-DATA-011 (Data Onboarding for New Team Members)
**Department:** Data & Analytics

## Situation
Data Manager submits a data onboarding request in MK-DataLake that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Director of Data & Analytics reviewing the request in MK-DataLake notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Director of Data & Analytics decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Director of Data & Analytics does not approve or silently correct the request themselves; they return it to Data Manager in MK-DataLake with a specific note on what's missing or wrong.
2. Data Manager is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Data Manager corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Director of Data & Analytics reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Director of Data & Analytics flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-DATA-011.

## Responsible Role
Data Manager

## Approval
Director of Data & Analytics

## Escalation
Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

## Expected Result
Incomplete or incorrect data onboarding requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._