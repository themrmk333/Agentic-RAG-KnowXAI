# Edge Case: Facility Maintenance Request Procedure — MK-FacilitiesDesk Is Unavailable

```json
{
  "document_id": "SOP-ADMIN-004-EDGE-C",
  "title": "Edge Case: Facility Maintenance Request Procedure \u2014 MK-FacilitiesDesk Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Maintenance",
  "subcategory": "Maintenance Request",
  "roles": [
    "employee",
    "Facilities Coordinator"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Facility Maintenance Request Procedure",
    "edge case",
    "exception",
    "ADMIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Facilities Coordinator",
  "source": "synthetic-generated",
  "related_sop": "SOP-ADMIN-004"
}
```

**Document ID:** SOP-ADMIN-004-EDGE-C  
**Related SOP:** SOP-ADMIN-004 (Facility Maintenance Request Procedure)  
**Department:** Administration / Facilities

## Situation
MK-FacilitiesDesk is down, in scheduled maintenance, or otherwise unreachable, but the maintenance request genuinely cannot wait until the system is restored.

## Detection
employee attempts to log into MK-FacilitiesDesk and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
employee first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-FacilitiesDesk to be restored (the default expectation).

## Steps

1. employee confirms MK-FacilitiesDesk is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent maintenance request requests, employee waits for MK-FacilitiesDesk to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, employee documents the request details (who, what, why, when) in an email to the Facilities Coordinator instead of the system.
4. The Facilities Coordinator reviews the emailed request using the same criteria they would apply inside MK-FacilitiesDesk, and replies with an approval/rejection decision in writing.
5. Once MK-FacilitiesDesk is restored, employee or the Facilities Coordinator re-enters the request and its outcome into MK-FacilitiesDesk retroactively, referencing the original email for the audit trail.
6. MK-FacilitiesDesk's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
employee

## Approval
Facilities Coordinator

## Escalation
Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration

## Expected Result
The maintenance request is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-FacilitiesDesk once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._