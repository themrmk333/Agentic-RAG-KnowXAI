# Edge Case: Data Pipeline Development Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-DATA-003-EDGE-E",
  "title": "Edge Case: Data Pipeline Development Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Engineering",
  "subcategory": "Data Pipeline",
  "roles": [
    "Data Engineer",
    "Data Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Pipeline Development Procedure",
    "edge case",
    "exception",
    "DATA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Data Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-DATA-003"
}
```

**Document ID:** SOP-DATA-003-EDGE-E  
**Related SOP:** SOP-DATA-003 (Data Pipeline Development Procedure)  
**Department:** Data & Analytics

## Situation
Data Engineer submits a data pipeline request in MK-DataLake that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Data Manager reviewing the request in MK-DataLake notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Data Manager decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Data Manager does not approve or silently correct the request themselves; they return it to Data Engineer in MK-DataLake with a specific note on what's missing or wrong.
2. Data Engineer is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Data Engineer corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Data Manager reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Data Manager flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-DATA-003.

## Responsible Role
Data Engineer

## Approval
Data Manager

## Escalation
Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

## Expected Result
Incomplete or incorrect data pipeline requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._