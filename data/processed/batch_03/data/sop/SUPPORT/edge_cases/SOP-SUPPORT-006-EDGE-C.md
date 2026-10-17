# Edge Case: Knowledge Base Article Creation Procedure — MK-SupportDesk Is Unavailable

```json
{
  "document_id": "SOP-SUPPORT-006-EDGE-C",
  "title": "Edge Case: Knowledge Base Article Creation Procedure \u2014 MK-SupportDesk Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Knowledge Management",
  "subcategory": "KB Article",
  "roles": [
    "Senior Support Associate",
    "Support Team Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Knowledge Base Article Creation Procedure",
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
  "related_sop": "SOP-SUPPORT-006"
}
```

**Document ID:** SOP-SUPPORT-006-EDGE-C  
**Related SOP:** SOP-SUPPORT-006 (Knowledge Base Article Creation Procedure)  
**Department:** Customer Support / Helpdesk

## Situation
MK-SupportDesk is down, in scheduled maintenance, or otherwise unreachable, but the kb article genuinely cannot wait until the system is restored.

## Detection
Senior Support Associate attempts to log into MK-SupportDesk and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Senior Support Associate first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-SupportDesk to be restored (the default expectation).

## Steps

1. Senior Support Associate confirms MK-SupportDesk is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent kb article requests, Senior Support Associate waits for MK-SupportDesk to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Senior Support Associate documents the request details (who, what, why, when) in an email to the Support Team Lead instead of the system.
4. The Support Team Lead reviews the emailed request using the same criteria they would apply inside MK-SupportDesk, and replies with an approval/rejection decision in writing.
5. Once MK-SupportDesk is restored, Senior Support Associate or the Support Team Lead re-enters the request and its outcome into MK-SupportDesk retroactively, referencing the original email for the audit trail.
6. MK-SupportDesk's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Senior Support Associate

## Approval
Support Team Lead

## Escalation
Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director

## Expected Result
The kb article is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-SupportDesk once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._