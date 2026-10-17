# Edge Case: KPI Definition and Governance Procedure — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-DATA-010-EDGE-D",
  "title": "Edge Case: KPI Definition and Governance Procedure \u2014 Rejected or Duplicate Request Handling",
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

**Document ID:** SOP-DATA-010-EDGE-D  
**Related SOP:** SOP-DATA-010 (KPI Definition and Governance Procedure)  
**Department:** Data & Analytics

## Situation
A kpi definition request is rejected by the Director of Data & Analytics, or Analytics Lead accidentally submits the same request twice in MK-DataLake.

## Detection
MK-DataLake shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Director of Data & Analytics (for rejections) or MK-DataLake itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Director of Data & Analytics records a specific rejection reason in MK-DataLake — a bare 'Rejected' status without a reason is not acceptable practice.
2. Analytics Lead reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If Analytics Lead disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-DataLake flags the second entry automatically; the Analytics Lead or Director of Data & Analytics confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Director of Data & Analytics initiates the standard reversal process instead of just closing the record.
6. MK-DataLake retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
Analytics Lead

## Approval
Director of Data & Analytics

## Escalation
Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

## Expected Result
Rejections always carry a documented reason and a clear next step for Analytics Lead, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._