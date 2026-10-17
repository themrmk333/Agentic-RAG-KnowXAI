# Edge Case: Marketing Qualified Lead (MQL) Handover to Sales — MK-MarketHub Is Unavailable

```json
{
  "document_id": "SOP-MKT-005-EDGE-C",
  "title": "Edge Case: Marketing Qualified Lead (MQL) Handover to Sales \u2014 MK-MarketHub Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Marketing",
  "department_code": "MKT",
  "category": "Lead Generation",
  "subcategory": "MQL Handover",
  "roles": [
    "Marketing Specialist",
    "Sales Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Marketing Qualified Lead (MQL) Handover to Sales",
    "edge case",
    "exception",
    "MKT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Sales Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-MKT-005"
}
```

**Document ID:** SOP-MKT-005-EDGE-C
**Related SOP:** SOP-MKT-005 (Marketing Qualified Lead (MQL) Handover to Sales)
**Department:** Marketing

## Situation
MK-MarketHub is down, in scheduled maintenance, or otherwise unreachable, but the mql handover genuinely cannot wait until the system is restored.

## Detection
Marketing Specialist attempts to log into MK-MarketHub and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Marketing Specialist first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-MarketHub to be restored (the default expectation).

## Steps

1. Marketing Specialist confirms MK-MarketHub is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent mql handover requests, Marketing Specialist waits for MK-MarketHub to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Marketing Specialist documents the request details (who, what, why, when) in an email to the Sales Manager instead of the system.
4. The Sales Manager reviews the emailed request using the same criteria they would apply inside MK-MarketHub, and replies with an approval/rejection decision in writing.
5. Once MK-MarketHub is restored, Marketing Specialist or the Sales Manager re-enters the request and its outcome into MK-MarketHub retroactively, referencing the original email for the audit trail.
6. MK-MarketHub's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Marketing Specialist

## Approval
Sales Manager

## Escalation
Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director

## Expected Result
The mql handover is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-MarketHub once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._