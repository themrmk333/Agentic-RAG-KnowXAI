# Edge Case: Opportunity Creation and Pipeline Entry — MK-CRM Is Unavailable

```json
{
  "document_id": "SOP-SALES-002-EDGE-C",
  "title": "Edge Case: Opportunity Creation and Pipeline Entry \u2014 MK-CRM Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Sales",
  "department_code": "SALES",
  "category": "Pipeline Management",
  "subcategory": "Sales Opportunity",
  "roles": [
    "Account Executive",
    "Sales Team Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Opportunity Creation and Pipeline Entry",
    "edge case",
    "exception",
    "SALES"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Sales Team Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-SALES-002"
}
```

**Document ID:** SOP-SALES-002-EDGE-C
**Related SOP:** SOP-SALES-002 (Opportunity Creation and Pipeline Entry)
**Department:** Sales

## Situation
MK-CRM is down, in scheduled maintenance, or otherwise unreachable, but the sales opportunity genuinely cannot wait until the system is restored.

## Detection
Account Executive attempts to log into MK-CRM and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Account Executive first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-CRM to be restored (the default expectation).

## Steps

1. Account Executive confirms MK-CRM is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent sales opportunity requests, Account Executive waits for MK-CRM to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Account Executive documents the request details (who, what, why, when) in an email to the Sales Team Lead instead of the system.
4. The Sales Team Lead reviews the emailed request using the same criteria they would apply inside MK-CRM, and replies with an approval/rejection decision in writing.
5. Once MK-CRM is restored, Account Executive or the Sales Team Lead re-enters the request and its outcome into MK-CRM retroactively, referencing the original email for the audit trail.
6. MK-CRM's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Account Executive

## Approval
Sales Team Lead

## Escalation
Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director

## Expected Result
The sales opportunity is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-CRM once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._