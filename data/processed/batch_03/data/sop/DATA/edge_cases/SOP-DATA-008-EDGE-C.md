# Edge Case: Data Retention and Deletion Procedure — MK-DataLake Is Unavailable

```json
{
  "document_id": "SOP-DATA-008-EDGE-C",
  "title": "Edge Case: Data Retention and Deletion Procedure \u2014 MK-DataLake Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Governance",
  "subcategory": "Data Retention Review",
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
    "Data Retention and Deletion Procedure",
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
  "related_sop": "SOP-DATA-008"
}
```

**Document ID:** SOP-DATA-008-EDGE-C  
**Related SOP:** SOP-DATA-008 (Data Retention and Deletion Procedure)  
**Department:** Data & Analytics

## Situation
MK-DataLake is down, in scheduled maintenance, or otherwise unreachable, but the data retention review genuinely cannot wait until the system is restored.

## Detection
Data Manager attempts to log into MK-DataLake and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Data Manager first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-DataLake to be restored (the default expectation).

## Steps

1. Data Manager confirms MK-DataLake is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent data retention review requests, Data Manager waits for MK-DataLake to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Data Manager documents the request details (who, what, why, when) in an email to the Director of Data & Analytics instead of the system.
4. The Director of Data & Analytics reviews the emailed request using the same criteria they would apply inside MK-DataLake, and replies with an approval/rejection decision in writing.
5. Once MK-DataLake is restored, Data Manager or the Director of Data & Analytics re-enters the request and its outcome into MK-DataLake retroactively, referencing the original email for the audit trail.
6. MK-DataLake's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Data Manager

## Approval
Director of Data & Analytics

## Escalation
Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

## Expected Result
The data retention review is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-DataLake once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._