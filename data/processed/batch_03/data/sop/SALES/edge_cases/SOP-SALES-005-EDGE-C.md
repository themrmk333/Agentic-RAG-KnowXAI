# Edge Case: Deal Closure and Handover to Customer Support — MK-CRM Is Unavailable

```json
{
  "document_id": "SOP-SALES-005-EDGE-C",
  "title": "Edge Case: Deal Closure and Handover to Customer Support \u2014 MK-CRM Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Sales",
  "department_code": "SALES",
  "category": "Customer Handover",
  "subcategory": "Customer Handover",
  "roles": [
    "Account Executive",
    "Sales Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Deal Closure and Handover to Customer Support",
    "edge case",
    "exception",
    "SALES"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Sales Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SALES-005"
}
```

**Document ID:** SOP-SALES-005-EDGE-C  
**Related SOP:** SOP-SALES-005 (Deal Closure and Handover to Customer Support)  
**Department:** Sales

## Situation
MK-CRM is down, in scheduled maintenance, or otherwise unreachable, but the customer handover genuinely cannot wait until the system is restored.

## Detection
Account Executive attempts to log into MK-CRM and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Account Executive first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-CRM to be restored (the default expectation).

## Steps

1. Account Executive confirms MK-CRM is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent customer handover requests, Account Executive waits for MK-CRM to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Account Executive documents the request details (who, what, why, when) in an email to the Sales Manager instead of the system.
4. The Sales Manager reviews the emailed request using the same criteria they would apply inside MK-CRM, and replies with an approval/rejection decision in writing.
5. Once MK-CRM is restored, Account Executive or the Sales Manager re-enters the request and its outcome into MK-CRM retroactively, referencing the original email for the audit trail.
6. MK-CRM's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Account Executive

## Approval
Sales Manager

## Escalation
Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director

## Expected Result
The customer handover is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-CRM once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._