# Edge Case: Phishing Email Reporting Procedure — MK-SecGuard Is Unavailable

```json
{
  "document_id": "SOP-SEC-001-EDGE-C",
  "title": "Edge Case: Phishing Email Reporting Procedure \u2014 MK-SecGuard Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Phishing",
  "subcategory": "Phishing Report",
  "roles": [
    "employee",
    "Security Analyst"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Phishing Email Reporting Procedure",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Analyst",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-001"
}
```

**Document ID:** SOP-SEC-001-EDGE-C
**Related SOP:** SOP-SEC-001 (Phishing Email Reporting Procedure)
**Department:** Cybersecurity / Information Security

## Situation
MK-SecGuard is down, in scheduled maintenance, or otherwise unreachable, but the phishing report genuinely cannot wait until the system is restored.

## Detection
employee attempts to log into MK-SecGuard and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
employee first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-SecGuard to be restored (the default expectation).

## Steps

1. employee confirms MK-SecGuard is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent phishing report requests, employee waits for MK-SecGuard to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, employee documents the request details (who, what, why, when) in an email to the Security Analyst instead of the system.
4. The Security Analyst reviews the emailed request using the same criteria they would apply inside MK-SecGuard, and replies with an approval/rejection decision in writing.
5. Once MK-SecGuard is restored, employee or the Security Analyst re-enters the request and its outcome into MK-SecGuard retroactively, referencing the original email for the audit trail.
6. MK-SecGuard's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
employee

## Approval
Security Analyst

## Escalation
Security Analyst -> Incident Response Lead -> Security Manager -> CISO

## Expected Result
The phishing report is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-SecGuard once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._