# Edge Case: Test Case Design and Review — MK-TestHub Is Unavailable

```json
{
  "document_id": "SOP-QA-002-EDGE-C",
  "title": "Edge Case: Test Case Design and Review \u2014 MK-TestHub Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "QA / Testing",
  "department_code": "QA",
  "category": "Test Planning",
  "subcategory": "Test Case Suite",
  "roles": [
    "QA Engineer",
    "QA Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Test Case Design and Review",
    "edge case",
    "exception",
    "QA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "QA Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-QA-002"
}
```

**Document ID:** SOP-QA-002-EDGE-C
**Related SOP:** SOP-QA-002 (Test Case Design and Review)
**Department:** QA / Testing

## Situation
MK-TestHub is down, in scheduled maintenance, or otherwise unreachable, but the test case suite genuinely cannot wait until the system is restored.

## Detection
QA Engineer attempts to log into MK-TestHub and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
QA Engineer first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-TestHub to be restored (the default expectation).

## Steps

1. QA Engineer confirms MK-TestHub is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent test case suite requests, QA Engineer waits for MK-TestHub to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, QA Engineer documents the request details (who, what, why, when) in an email to the QA Lead instead of the system.
4. The QA Lead reviews the emailed request using the same criteria they would apply inside MK-TestHub, and replies with an approval/rejection decision in writing.
5. Once MK-TestHub is restored, QA Engineer or the QA Lead re-enters the request and its outcome into MK-TestHub retroactively, referencing the original email for the audit trail.
6. MK-TestHub's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
QA Engineer

## Approval
QA Lead

## Escalation
QA Engineer -> QA Lead -> QA Manager -> QA Director

## Expected Result
The test case suite is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-TestHub once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._