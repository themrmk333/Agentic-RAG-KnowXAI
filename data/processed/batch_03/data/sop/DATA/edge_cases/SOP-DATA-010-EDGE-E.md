# Edge Case: KPI Definition and Governance Procedure — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-DATA-010-EDGE-E",
  "title": "Edge Case: KPI Definition and Governance Procedure \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Governance",
  "subcategory": "KPI Definition",
  "roles": [
    "Analytics Lead",
    "Director of Data & Analytics"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "KPI Definition and Governance Procedure",
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
  "related_sop": "SOP-DATA-010"
}
```

**Document ID:** SOP-DATA-010-EDGE-E  
**Related SOP:** SOP-DATA-010 (KPI Definition and Governance Procedure)  
**Department:** Data & Analytics

## Situation
Analytics Lead submits a kpi definition request in MK-DataLake that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Director of Data & Analytics reviewing the request in MK-DataLake notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Director of Data & Analytics decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Director of Data & Analytics does not approve or silently correct the request themselves; they return it to Analytics Lead in MK-DataLake with a specific note on what's missing or wrong.
2. Analytics Lead is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Analytics Lead corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Director of Data & Analytics reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Director of Data & Analytics flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-DATA-010.

## Responsible Role
Analytics Lead

## Approval
Director of Data & Analytics

## Escalation
Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

## Expected Result
Incomplete or incorrect kpi definition requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._