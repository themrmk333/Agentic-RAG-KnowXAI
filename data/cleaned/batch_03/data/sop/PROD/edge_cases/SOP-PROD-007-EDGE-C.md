# Edge Case: Product Backlog Grooming Procedure — MK-ProductHub Is Unavailable

```json
{
  "document_id": "SOP-PROD-007-EDGE-C",
  "title": "Edge Case: Product Backlog Grooming Procedure \u2014 MK-ProductHub Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Product Management",
  "department_code": "PROD",
  "category": "Backlog Management",
  "subcategory": "Product Backlog",
  "roles": [
    "Product Manager",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Product Backlog Grooming Procedure",
    "edge case",
    "exception",
    "PROD"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROD-007"
}
```

**Document ID:** SOP-PROD-007-EDGE-C
**Related SOP:** SOP-PROD-007 (Product Backlog Grooming Procedure)
**Department:** Product Management

## Situation
MK-ProductHub is down, in scheduled maintenance, or otherwise unreachable, but the product backlog genuinely cannot wait until the system is restored.

## Detection
Product Manager attempts to log into MK-ProductHub and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Product Manager first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-ProductHub to be restored (the default expectation).

## Steps

1. Product Manager confirms MK-ProductHub is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent product backlog requests, Product Manager waits for MK-ProductHub to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Product Manager documents the request details (who, what, why, when) in an email to the Engineering Manager instead of the system.
4. The Engineering Manager reviews the emailed request using the same criteria they would apply inside MK-ProductHub, and replies with an approval/rejection decision in writing.
5. Once MK-ProductHub is restored, Product Manager or the Engineering Manager re-enters the request and its outcome into MK-ProductHub retroactively, referencing the original email for the audit trail.
6. MK-ProductHub's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Product Manager

## Approval
Engineering Manager

## Escalation
Associate Product Manager -> Product Manager -> Product Lead -> Head of Product

## Expected Result
The product backlog is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-ProductHub once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._