# Edge Case: Data Quality Issue Resolution Procedure — MK-DataLake Is Unavailable

```json
{
  "document_id": "SOP-DATA-004-EDGE-C",
  "title": "Edge Case: Data Quality Issue Resolution Procedure \u2014 MK-DataLake Is Unavailable",
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

**Document ID:** SOP-DATA-004-EDGE-C
**Related SOP:** SOP-DATA-004 (Data Quality Issue Resolution Procedure)
**Department:** Data & Analytics

## Situation
MK-DataLake is down, in scheduled maintenance, or otherwise unreachable, but the data quality incident genuinely cannot wait until the system is restored.

## Detection
Data Analyst attempts to log into MK-DataLake and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Data Analyst first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-DataLake to be restored (the default expectation).

## Steps

1. Data Analyst confirms MK-DataLake is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent data quality incident requests, Data Analyst waits for MK-DataLake to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Data Analyst documents the request details (who, what, why, when) in an email to the Analytics Lead instead of the system.
4. The Analytics Lead reviews the emailed request using the same criteria they would apply inside MK-DataLake, and replies with an approval/rejection decision in writing.
5. Once MK-DataLake is restored, Data Analyst or the Analytics Lead re-enters the request and its outcome into MK-DataLake retroactively, referencing the original email for the audit trail.
6. MK-DataLake's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Data Analyst

## Approval
Analytics Lead

## Escalation
Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

## Expected Result
The data quality incident is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-DataLake once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._