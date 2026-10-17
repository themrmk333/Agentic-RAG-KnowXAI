# Edge Case: Production Incident Response (DevOps) — MK-CloudOps Is Unavailable

```json
{
  "document_id": "SOP-DEVOPS-004-EDGE-C",
  "title": "Edge Case: Production Incident Response (DevOps) \u2014 MK-CloudOps Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "DevOps & Cloud",
  "department_code": "DEVOPS",
  "category": "Incident Management",
  "subcategory": "Infrastructure Incident",
  "roles": [
    "on-call DevOps Engineer",
    "DevOps Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Production Incident Response (DevOps)",
    "edge case",
    "exception",
    "DEVOPS"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "DevOps Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-DEVOPS-004"
}
```

**Document ID:** SOP-DEVOPS-004-EDGE-C
**Related SOP:** SOP-DEVOPS-004 (Production Incident Response (DevOps))
**Department:** DevOps & Cloud

## Situation
MK-CloudOps is down, in scheduled maintenance, or otherwise unreachable, but the infrastructure incident genuinely cannot wait until the system is restored.

## Detection
on-call DevOps Engineer attempts to log into MK-CloudOps and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
on-call DevOps Engineer first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-CloudOps to be restored (the default expectation).

## Steps

1. on-call DevOps Engineer confirms MK-CloudOps is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent infrastructure incident requests, on-call DevOps Engineer waits for MK-CloudOps to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, on-call DevOps Engineer documents the request details (who, what, why, when) in an email to the DevOps Manager instead of the system.
4. The DevOps Manager reviews the emailed request using the same criteria they would apply inside MK-CloudOps, and replies with an approval/rejection decision in writing.
5. Once MK-CloudOps is restored, on-call DevOps Engineer or the DevOps Manager re-enters the request and its outcome into MK-CloudOps retroactively, referencing the original email for the audit trail.
6. MK-CloudOps's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
on-call DevOps Engineer

## Approval
DevOps Manager

## Escalation
DevOps Engineer -> DevOps Manager -> DevOps Director

## Expected Result
The infrastructure incident is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-CloudOps once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._