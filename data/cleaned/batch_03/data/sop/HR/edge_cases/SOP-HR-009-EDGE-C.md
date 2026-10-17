# Edge Case: Offer Letter Generation Procedure — MK-HRMS Is Unavailable

```json
{
  "document_id": "SOP-HR-009-EDGE-C",
  "title": "Edge Case: Offer Letter Generation Procedure \u2014 MK-HRMS Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Human Resources",
  "department_code": "HR",
  "category": "Recruitment",
  "subcategory": "Offer Letter",
  "roles": [
    "HR Executive",
    "HR Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Offer Letter Generation Procedure",
    "edge case",
    "exception",
    "HR"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "HR Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-HR-009"
}
```

**Document ID:** SOP-HR-009-EDGE-C
**Related SOP:** SOP-HR-009 (Offer Letter Generation Procedure)
**Department:** Human Resources

## Situation
MK-HRMS is down, in scheduled maintenance, or otherwise unreachable, but the offer letter genuinely cannot wait until the system is restored.

## Detection
HR Executive attempts to log into MK-HRMS and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
HR Executive first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-HRMS to be restored (the default expectation).

## Steps

1. HR Executive confirms MK-HRMS is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent offer letter requests, HR Executive waits for MK-HRMS to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, HR Executive documents the request details (who, what, why, when) in an email to the HR Manager instead of the system.
4. The HR Manager reviews the emailed request using the same criteria they would apply inside MK-HRMS, and replies with an approval/rejection decision in writing.
5. Once MK-HRMS is restored, HR Executive or the HR Manager re-enters the request and its outcome into MK-HRMS retroactively, referencing the original email for the audit trail.
6. MK-HRMS's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
HR Executive

## Approval
HR Manager

## Escalation
HR Executive -> HR Business Partner -> HR Manager -> HR Director

## Expected Result
The offer letter is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-HRMS once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._