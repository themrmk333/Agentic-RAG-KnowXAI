# Edge Case: Data Quality Issue Resolution Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-DATA-004-EDGE-D",
  "title": "Edge Case: Data Quality Issue Resolution Procedure \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Quality",
  "subcategory": "Data Quality Incident",
  "roles": [
    "Data Analyst",
    "Analytics Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Data Quality Issue Resolution Procedure",
    "edge case",
    "exception",
    "DATA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Analytics Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-DATA-004"
}
```

**Document ID:** SOP-DATA-004-EDGE-D
**Related SOP:** SOP-DATA-004 (Data Quality Issue Resolution Procedure)
**Department:** Data & Analytics

## Situation
A data quality incident request is rejected by the Analytics Lead, or Data Analyst accidentally submits the same request twice in MK-DataLake.

## Detection
MK-DataLake shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Analytics Lead (for rejections) or MK-DataLake itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Analytics Lead records a specific rejection reason in MK-DataLake — a bare 'Rejected' status without a reason is not acceptable practice.
2. Data Analyst reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Data Analyst disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-DataLake flags the second entry automatically; the Data Analyst or Analytics Lead confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Analytics Lead initiates the standard reversal process instead of just closing the record.
6. MK-DataLake retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Data Analyst

## Approval
Analytics Lead

## Escalation
Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

## Expected Result
Rejections always carry a documented reason and a clear next step for Data Analyst, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._