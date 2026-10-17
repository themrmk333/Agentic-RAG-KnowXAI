# Edge Case: Live Chat Support Procedure — MK-SupportDesk Is Unavailable

```json
{
  "document_id": "SOP-SUPPORT-013-EDGE-C",
  "title": "Edge Case: Live Chat Support Procedure \u2014 MK-SupportDesk Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Live Support",
  "subcategory": "Live Chat Session",
  "roles": [
    "Customer Support Associate",
    "Support Team Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Live Chat Support Procedure",
    "edge case",
    "exception",
    "SUPPORT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Support Team Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-SUPPORT-013"
}
```

**Document ID:** SOP-SUPPORT-013-EDGE-C
**Related SOP:** SOP-SUPPORT-013 (Live Chat Support Procedure)
**Department:** Customer Support / Helpdesk

## Situation
MK-SupportDesk is down, in scheduled maintenance, or otherwise unreachable, but the live chat session genuinely cannot wait until the system is restored.

## Detection
Customer Support Associate attempts to log into MK-SupportDesk and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Customer Support Associate first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-SupportDesk to be restored (the default expectation).

## Steps

1. Customer Support Associate confirms MK-SupportDesk is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent live chat session requests, Customer Support Associate waits for MK-SupportDesk to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Customer Support Associate documents the request details (who, what, why, when) in an email to the Support Team Lead instead of the system.
4. The Support Team Lead reviews the emailed request using the same criteria they would apply inside MK-SupportDesk, and replies with an approval/rejection decision in writing.
5. Once MK-SupportDesk is restored, Customer Support Associate or the Support Team Lead re-enters the request and its outcome into MK-SupportDesk retroactively, referencing the original email for the audit trail.
6. MK-SupportDesk's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Customer Support Associate

## Approval
Support Team Lead

## Escalation
Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director

## Expected Result
The live chat session is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-SupportDesk once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._