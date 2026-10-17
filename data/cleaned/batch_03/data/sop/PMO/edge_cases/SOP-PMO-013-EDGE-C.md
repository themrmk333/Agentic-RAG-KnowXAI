# Edge Case: Project Quality Gate Review — MK-PMTrack Is Unavailable

```json
{
  "document_id": "SOP-PMO-013-EDGE-C",
  "title": "Edge Case: Project Quality Gate Review \u2014 MK-PMTrack Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Project Management / PMO",
  "department_code": "PMO",
  "category": "Quality Management",
  "subcategory": "Quality Gate",
  "roles": [
    "Project Manager",
    "QA Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Project Quality Gate Review",
    "edge case",
    "exception",
    "PMO"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "QA Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-PMO-013"
}
```

**Document ID:** SOP-PMO-013-EDGE-C
**Related SOP:** SOP-PMO-013 (Project Quality Gate Review)
**Department:** Project Management / PMO

## Situation
MK-PMTrack is down, in scheduled maintenance, or otherwise unreachable, but the quality gate genuinely cannot wait until the system is restored.

## Detection
Project Manager attempts to log into MK-PMTrack and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Project Manager first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-PMTrack to be restored (the default expectation).

## Steps

1. Project Manager confirms MK-PMTrack is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent quality gate requests, Project Manager waits for MK-PMTrack to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Project Manager documents the request details (who, what, why, when) in an email to the QA Lead instead of the system.
4. The QA Lead reviews the emailed request using the same criteria they would apply inside MK-PMTrack, and replies with an approval/rejection decision in writing.
5. Once MK-PMTrack is restored, Project Manager or the QA Lead re-enters the request and its outcome into MK-PMTrack retroactively, referencing the original email for the audit trail.
6. MK-PMTrack's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Project Manager

## Approval
QA Lead

## Escalation
Project Coordinator -> Project Manager -> PMO Lead -> PMO Director

## Expected Result
The quality gate is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-PMTrack once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._