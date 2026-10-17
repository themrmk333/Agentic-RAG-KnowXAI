# Edge Case: Research-to-Production Handover Procedure — MK-Labs Is Unavailable

```json
{
  "document_id": "SOP-RND-004-EDGE-C",
  "title": "Edge Case: Research-to-Production Handover Procedure \u2014 MK-Labs Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Research & Development",
  "department_code": "RND",
  "category": "Technology Transfer",
  "subcategory": "Research Handover",
  "roles": [
    "Research Lead",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Research-to-Production Handover Procedure",
    "edge case",
    "exception",
    "RND"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-RND-004"
}
```

**Document ID:** SOP-RND-004-EDGE-C
**Related SOP:** SOP-RND-004 (Research-to-Production Handover Procedure)
**Department:** Research & Development

## Situation
MK-Labs is down, in scheduled maintenance, or otherwise unreachable, but the research handover genuinely cannot wait until the system is restored.

## Detection
Research Lead attempts to log into MK-Labs and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Research Lead first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-Labs to be restored (the default expectation).

## Steps

1. Research Lead confirms MK-Labs is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent research handover requests, Research Lead waits for MK-Labs to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Research Lead documents the request details (who, what, why, when) in an email to the Engineering Manager instead of the system.
4. The Engineering Manager reviews the emailed request using the same criteria they would apply inside MK-Labs, and replies with an approval/rejection decision in writing.
5. Once MK-Labs is restored, Research Lead or the Engineering Manager re-enters the request and its outcome into MK-Labs retroactively, referencing the original email for the audit trail.
6. MK-Labs's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Research Lead

## Approval
Engineering Manager

## Escalation
Research Associate -> Research Lead -> R&D Manager -> R&D Director

## Expected Result
The research handover is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-Labs once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._