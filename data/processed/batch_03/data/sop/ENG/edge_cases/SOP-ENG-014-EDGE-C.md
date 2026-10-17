# Edge Case: Database Schema Migration — MK-CodeForge Is Unavailable

```json
{
  "document_id": "SOP-ENG-014-EDGE-C",
  "title": "Edge Case: Database Schema Migration \u2014 MK-CodeForge Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Data Management",
  "subcategory": "Schema Migration",
  "roles": [
    "Software Engineer",
    "Tech Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Database Schema Migration",
    "edge case",
    "exception",
    "ENG"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Tech Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-ENG-014"
}
```

**Document ID:** SOP-ENG-014-EDGE-C  
**Related SOP:** SOP-ENG-014 (Database Schema Migration)  
**Department:** Software Engineering / Development

## Situation
MK-CodeForge is down, in scheduled maintenance, or otherwise unreachable, but the schema migration genuinely cannot wait until the system is restored.

## Detection
Software Engineer attempts to log into MK-CodeForge and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Software Engineer first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-CodeForge to be restored (the default expectation).

## Steps

1. Software Engineer confirms MK-CodeForge is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent schema migration requests, Software Engineer waits for MK-CodeForge to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Software Engineer documents the request details (who, what, why, when) in an email to the Tech Lead instead of the system.
4. The Tech Lead reviews the emailed request using the same criteria they would apply inside MK-CodeForge, and replies with an approval/rejection decision in writing.
5. Once MK-CodeForge is restored, Software Engineer or the Tech Lead re-enters the request and its outcome into MK-CodeForge retroactively, referencing the original email for the audit trail.
6. MK-CodeForge's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Software Engineer

## Approval
Tech Lead

## Escalation
Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

## Expected Result
The schema migration is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-CodeForge once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._