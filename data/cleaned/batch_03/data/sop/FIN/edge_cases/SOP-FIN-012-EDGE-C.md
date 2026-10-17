# Edge Case: Corporate Credit Card Reconciliation — MK-Finance360 Is Unavailable

```json
{
  "document_id": "SOP-FIN-012-EDGE-C",
  "title": "Edge Case: Corporate Credit Card Reconciliation \u2014 MK-Finance360 Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Finance & Accounting",
  "department_code": "FIN",
  "category": "Expense Reimbursement",
  "subcategory": "Card Statement Reconciliation",
  "roles": [
    "Finance Executive",
    "Finance Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Corporate Credit Card Reconciliation",
    "edge case",
    "exception",
    "FIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-FIN-012"
}
```

**Document ID:** SOP-FIN-012-EDGE-C
**Related SOP:** SOP-FIN-012 (Corporate Credit Card Reconciliation)
**Department:** Finance & Accounting

## Situation
MK-Finance360 is down, in scheduled maintenance, or otherwise unreachable, but the card statement reconciliation genuinely cannot wait until the system is restored.

## Detection
Finance Executive attempts to log into MK-Finance360 and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Finance Executive first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-Finance360 to be restored (the default expectation).

## Steps

1. Finance Executive confirms MK-Finance360 is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent card statement reconciliation requests, Finance Executive waits for MK-Finance360 to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Finance Executive documents the request details (who, what, why, when) in an email to the Finance Lead instead of the system.
4. The Finance Lead reviews the emailed request using the same criteria they would apply inside MK-Finance360, and replies with an approval/rejection decision in writing.
5. Once MK-Finance360 is restored, Finance Executive or the Finance Lead re-enters the request and its outcome into MK-Finance360 retroactively, referencing the original email for the audit trail.
6. MK-Finance360's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Finance Executive

## Approval
Finance Lead

## Escalation
Accountant -> Finance Lead -> Finance Manager -> Finance Director

## Expected Result
The card statement reconciliation is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-Finance360 once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._