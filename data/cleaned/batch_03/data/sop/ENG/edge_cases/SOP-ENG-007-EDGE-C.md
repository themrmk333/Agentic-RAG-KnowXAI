# Edge Case: Bug Triage and Assignment — MK-CodeForge Is Unavailable

```json
{
  "document_id": "SOP-ENG-007-EDGE-C",
  "title": "Edge Case: Bug Triage and Assignment \u2014 MK-CodeForge Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Quality",
  "subcategory": "Bug Backlog",
  "roles": [
    "Tech Lead",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Bug Triage and Assignment",
    "edge case",
    "exception",
    "ENG"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-ENG-007"
}
```

**Document ID:** SOP-ENG-007-EDGE-C
**Related SOP:** SOP-ENG-007 (Bug Triage and Assignment)
**Department:** Software Engineering / Development

## Situation
MK-CodeForge is down, in scheduled maintenance, or otherwise unreachable, but the bug backlog genuinely cannot wait until the system is restored.

## Detection
Tech Lead attempts to log into MK-CodeForge and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Tech Lead first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-CodeForge to be restored (the default expectation).

## Steps

1. Tech Lead confirms MK-CodeForge is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent bug backlog requests, Tech Lead waits for MK-CodeForge to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Tech Lead documents the request details (who, what, why, when) in an email to the Engineering Manager instead of the system.
4. The Engineering Manager reviews the emailed request using the same criteria they would apply inside MK-CodeForge, and replies with an approval/rejection decision in writing.
5. Once MK-CodeForge is restored, Tech Lead or the Engineering Manager re-enters the request and its outcome into MK-CodeForge retroactively, referencing the original email for the audit trail.
6. MK-CodeForge's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Tech Lead

## Approval
Engineering Manager

## Escalation
Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

## Expected Result
The bug backlog is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-CodeForge once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._