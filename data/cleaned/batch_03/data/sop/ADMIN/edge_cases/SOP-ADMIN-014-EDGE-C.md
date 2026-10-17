# Edge Case: Office Budget and Vendor Invoice Approval (Admin) — MK-FacilitiesDesk Is Unavailable

```json
{
  "document_id": "SOP-ADMIN-014-EDGE-C",
  "title": "Edge Case: Office Budget and Vendor Invoice Approval (Admin) \u2014 MK-FacilitiesDesk Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Administration / Facilities",
  "department_code": "ADMIN",
  "category": "Budget Management",
  "subcategory": "Admin Invoice Approval",
  "roles": [
    "Facilities Manager",
    "Finance Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Office Budget and Vendor Invoice Approval (Admin)",
    "edge case",
    "exception",
    "ADMIN"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-ADMIN-014"
}
```

**Document ID:** SOP-ADMIN-014-EDGE-C
**Related SOP:** SOP-ADMIN-014 (Office Budget and Vendor Invoice Approval (Admin))
**Department:** Administration / Facilities

## Situation
MK-FacilitiesDesk is down, in scheduled maintenance, or otherwise unreachable, but the admin invoice approval genuinely cannot wait until the system is restored.

## Detection
Facilities Manager attempts to log into MK-FacilitiesDesk and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Facilities Manager first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-FacilitiesDesk to be restored (the default expectation).

## Steps

1. Facilities Manager confirms MK-FacilitiesDesk is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent admin invoice approval requests, Facilities Manager waits for MK-FacilitiesDesk to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Facilities Manager documents the request details (who, what, why, when) in an email to the Finance Manager instead of the system.
4. The Finance Manager reviews the emailed request using the same criteria they would apply inside MK-FacilitiesDesk, and replies with an approval/rejection decision in writing.
5. Once MK-FacilitiesDesk is restored, Facilities Manager or the Finance Manager re-enters the request and its outcome into MK-FacilitiesDesk retroactively, referencing the original email for the audit trail.
6. MK-FacilitiesDesk's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Facilities Manager

## Approval
Finance Manager

## Escalation
Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration

## Expected Result
The admin invoice approval is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-FacilitiesDesk once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._