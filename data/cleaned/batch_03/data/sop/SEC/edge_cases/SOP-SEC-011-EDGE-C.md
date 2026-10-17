# Edge Case: Endpoint Security Alert Triage — MK-SecGuard Is Unavailable

```json
{
  "document_id": "SOP-SEC-011-EDGE-C",
  "title": "Edge Case: Endpoint Security Alert Triage \u2014 MK-SecGuard Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Endpoint Security",
  "subcategory": "Endpoint Alert",
  "roles": [
    "Security Analyst",
    "Incident Response Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Endpoint Security Alert Triage",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Incident Response Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-011"
}
```

**Document ID:** SOP-SEC-011-EDGE-C
**Related SOP:** SOP-SEC-011 (Endpoint Security Alert Triage)
**Department:** Cybersecurity / Information Security

## Situation
MK-SecGuard is down, in scheduled maintenance, or otherwise unreachable, but the endpoint alert genuinely cannot wait until the system is restored.

## Detection
Security Analyst attempts to log into MK-SecGuard and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Security Analyst first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-SecGuard to be restored (the default expectation).

## Steps

1. Security Analyst confirms MK-SecGuard is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent endpoint alert requests, Security Analyst waits for MK-SecGuard to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Security Analyst documents the request details (who, what, why, when) in an email to the Incident Response Lead instead of the system.
4. The Incident Response Lead reviews the emailed request using the same criteria they would apply inside MK-SecGuard, and replies with an approval/rejection decision in writing.
5. Once MK-SecGuard is restored, Security Analyst or the Incident Response Lead re-enters the request and its outcome into MK-SecGuard retroactively, referencing the original email for the audit trail.
6. MK-SecGuard's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Security Analyst

## Approval
Incident Response Lead

## Escalation
Security Analyst -> Incident Response Lead -> Security Manager -> CISO

## Expected Result
The endpoint alert is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-SecGuard once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._