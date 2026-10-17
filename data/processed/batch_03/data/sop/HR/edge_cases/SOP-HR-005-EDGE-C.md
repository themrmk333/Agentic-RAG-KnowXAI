# Edge Case: Promotion Nomination Procedure — MK-HRMS Is Unavailable

```json
{
  "document_id": "SOP-HR-005-EDGE-C",
  "title": "Edge Case: Promotion Nomination Procedure \u2014 MK-HRMS Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Human Resources",
  "department_code": "HR",
  "category": "Career Development",
  "subcategory": "Promotion Nomination",
  "roles": [
    "Reporting Manager",
    "HR Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Promotion Nomination Procedure",
    "edge case",
    "exception",
    "HR"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "HR Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-HR-005"
}
```

**Document ID:** SOP-HR-005-EDGE-C  
**Related SOP:** SOP-HR-005 (Promotion Nomination Procedure)  
**Department:** Human Resources

## Situation
MK-HRMS is down, in scheduled maintenance, or otherwise unreachable, but the promotion nomination genuinely cannot wait until the system is restored.

## Detection
Reporting Manager attempts to log into MK-HRMS and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Reporting Manager first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-HRMS to be restored (the default expectation).

## Steps

1. Reporting Manager confirms MK-HRMS is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent promotion nomination requests, Reporting Manager waits for MK-HRMS to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Reporting Manager documents the request details (who, what, why, when) in an email to the HR Director instead of the system.
4. The HR Director reviews the emailed request using the same criteria they would apply inside MK-HRMS, and replies with an approval/rejection decision in writing.
5. Once MK-HRMS is restored, Reporting Manager or the HR Director re-enters the request and its outcome into MK-HRMS retroactively, referencing the original email for the audit trail.
6. MK-HRMS's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Reporting Manager

## Approval
HR Director

## Escalation
HR Executive -> HR Business Partner -> HR Manager -> HR Director

## Expected Result
The promotion nomination is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-HRMS once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._