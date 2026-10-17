# Edge Case: QA Metrics Reporting Procedure — MK-TestHub Is Unavailable

```json
{
  "document_id": "SOP-QA-016-EDGE-C",
  "title": "Edge Case: QA Metrics Reporting Procedure \u2014 MK-TestHub Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Reporting",
  "subcategory": "QA Metrics Report",
  "roles": [
    "QA Lead",
    "QA Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "QA Metrics Reporting Procedure",
    "edge case",
    "exception",
    "QA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "QA Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-QA-016"
}
```

**Document ID:** SOP-QA-016-EDGE-C
**Related SOP:** SOP-QA-016 (QA Metrics Reporting Procedure)
**Department:** QA / Testing

## Situation
MK-TestHub is down, in scheduled maintenance, or otherwise unreachable, but the qa metrics report genuinely cannot wait until the system is restored.

## Detection
QA Lead attempts to log into MK-TestHub and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
QA Lead first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-TestHub to be restored (the default expectation).

## Steps

1. QA Lead confirms MK-TestHub is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent qa metrics report requests, QA Lead waits for MK-TestHub to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, QA Lead documents the request details (who, what, why, when) in an email to the QA Manager instead of the system.
4. The QA Manager reviews the emailed request using the same criteria they would apply inside MK-TestHub, and replies with an approval/rejection decision in writing.
5. Once MK-TestHub is restored, QA Lead or the QA Manager re-enters the request and its outcome into MK-TestHub retroactively, referencing the original email for the audit trail.
6. MK-TestHub's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
QA Lead

## Approval
QA Manager

## Escalation
QA Engineer -> QA Lead -> QA Manager -> QA Director

## Expected Result
The qa metrics report is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-TestHub once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._