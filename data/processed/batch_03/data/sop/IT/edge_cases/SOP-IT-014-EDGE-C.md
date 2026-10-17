# Edge Case: Remote Desktop / Screen Share Support Session — MK-ServiceDesk Is Unavailable

```json
{
  "document_id": "SOP-IT-014-EDGE-C",
  "title": "Edge Case: Remote Desktop / Screen Share Support Session \u2014 MK-ServiceDesk Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "IT Support / Information Technology",
  "department_code": "IT",
  "category": "Support Operations",
  "subcategory": "Remote Support Session",
  "roles": [
    "employee",
    "IT Support Engineer"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Remote Desktop / Screen Share Support Session",
    "edge case",
    "exception",
    "IT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "IT Support Engineer",
  "source": "synthetic-generated",
  "related_sop": "SOP-IT-014"
}
```

**Document ID:** SOP-IT-014-EDGE-C  
**Related SOP:** SOP-IT-014 (Remote Desktop / Screen Share Support Session)  
**Department:** IT Support / Information Technology

## Situation
MK-ServiceDesk is down, in scheduled maintenance, or otherwise unreachable, but the remote support session genuinely cannot wait until the system is restored.

## Detection
employee attempts to log into MK-ServiceDesk and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
employee first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-ServiceDesk to be restored (the default expectation).

## Steps

1. employee confirms MK-ServiceDesk is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent remote support session requests, employee waits for MK-ServiceDesk to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, employee documents the request details (who, what, why, when) in an email to the IT Support Engineer instead of the system.
4. The IT Support Engineer reviews the emailed request using the same criteria they would apply inside MK-ServiceDesk, and replies with an approval/rejection decision in writing.
5. Once MK-ServiceDesk is restored, employee or the IT Support Engineer re-enters the request and its outcome into MK-ServiceDesk retroactively, referencing the original email for the audit trail.
6. MK-ServiceDesk's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
employee

## Approval
IT Support Engineer

## Escalation
IT Support Engineer -> IT Manager -> IT Director

## Expected Result
The remote support session is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-ServiceDesk once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._