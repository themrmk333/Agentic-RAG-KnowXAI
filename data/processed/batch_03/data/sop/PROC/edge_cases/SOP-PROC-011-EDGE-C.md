# Edge Case: Procurement Onboarding Procedure — MK-ProcureX Is Unavailable

```json
{
  "document_id": "SOP-PROC-011-EDGE-C",
  "title": "Edge Case: Procurement Onboarding Procedure \u2014 MK-ProcureX Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Procurement / Purchasing",
  "department_code": "PROC",
  "category": "Onboarding",
  "subcategory": "Procurement Onboarding",
  "roles": [
    "Procurement Lead",
    "Procurement Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Procurement Onboarding Procedure",
    "edge case",
    "exception",
    "PROC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Procurement Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROC-011"
}
```

**Document ID:** SOP-PROC-011-EDGE-C  
**Related SOP:** SOP-PROC-011 (Procurement Onboarding Procedure)  
**Department:** Procurement / Purchasing

## Situation
MK-ProcureX is down, in scheduled maintenance, or otherwise unreachable, but the procurement onboarding genuinely cannot wait until the system is restored.

## Detection
Procurement Lead attempts to log into MK-ProcureX and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Procurement Lead first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-ProcureX to be restored (the default expectation).

## Steps

1. Procurement Lead confirms MK-ProcureX is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent procurement onboarding requests, Procurement Lead waits for MK-ProcureX to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Procurement Lead documents the request details (who, what, why, when) in an email to the Procurement Manager instead of the system.
4. The Procurement Manager reviews the emailed request using the same criteria they would apply inside MK-ProcureX, and replies with an approval/rejection decision in writing.
5. Once MK-ProcureX is restored, Procurement Lead or the Procurement Manager re-enters the request and its outcome into MK-ProcureX retroactively, referencing the original email for the audit trail.
6. MK-ProcureX's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Procurement Lead

## Approval
Procurement Manager

## Escalation
Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director

## Expected Result
The procurement onboarding is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-ProcureX once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._