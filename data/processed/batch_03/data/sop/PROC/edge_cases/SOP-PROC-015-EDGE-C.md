# Edge Case: Procurement Policy Exception Request — MK-ProcureX Is Unavailable

```json
{
  "document_id": "SOP-PROC-015-EDGE-C",
  "title": "Edge Case: Procurement Policy Exception Request \u2014 MK-ProcureX Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Procurement / Purchasing",
  "department_code": "PROC",
  "category": "Governance",
  "subcategory": "Procurement Policy Exception",
  "roles": [
    "requester",
    "Procurement Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Procurement Policy Exception Request",
    "edge case",
    "exception",
    "PROC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Procurement Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROC-015"
}
```

**Document ID:** SOP-PROC-015-EDGE-C  
**Related SOP:** SOP-PROC-015 (Procurement Policy Exception Request)  
**Department:** Procurement / Purchasing

## Situation
MK-ProcureX is down, in scheduled maintenance, or otherwise unreachable, but the procurement policy exception genuinely cannot wait until the system is restored.

## Detection
requester attempts to log into MK-ProcureX and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
requester first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-ProcureX to be restored (the default expectation).

## Steps

1. requester confirms MK-ProcureX is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent procurement policy exception requests, requester waits for MK-ProcureX to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, requester documents the request details (who, what, why, when) in an email to the Procurement Director instead of the system.
4. The Procurement Director reviews the emailed request using the same criteria they would apply inside MK-ProcureX, and replies with an approval/rejection decision in writing.
5. Once MK-ProcureX is restored, requester or the Procurement Director re-enters the request and its outcome into MK-ProcureX retroactively, referencing the original email for the audit trail.
6. MK-ProcureX's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
requester

## Approval
Procurement Director

## Escalation
Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director

## Expected Result
The procurement policy exception is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-ProcureX once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._