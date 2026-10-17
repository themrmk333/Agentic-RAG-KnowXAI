# Edge Case: Vendor Contract Negotiation Support — MK-LegalVault Is Unavailable

```json
{
  "document_id": "SOP-LEGAL-003-EDGE-C",
  "title": "Edge Case: Vendor Contract Negotiation Support \u2014 MK-LegalVault Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Legal & Compliance",
  "department_code": "LEGAL",
  "category": "Vendor Contracts",
  "subcategory": "Vendor Contract",
  "roles": [
    "Contracts Specialist",
    "Legal Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Vendor Contract Negotiation Support",
    "edge case",
    "exception",
    "LEGAL"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Legal Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-LEGAL-003"
}
```

**Document ID:** SOP-LEGAL-003-EDGE-C  
**Related SOP:** SOP-LEGAL-003 (Vendor Contract Negotiation Support)  
**Department:** Legal & Compliance

## Situation
MK-LegalVault is down, in scheduled maintenance, or otherwise unreachable, but the vendor contract genuinely cannot wait until the system is restored.

## Detection
Contracts Specialist attempts to log into MK-LegalVault and receives a system-unavailable error, or has received a maintenance notification covering the relevant window (see the Communications archive).

## Decision Criteria
Contracts Specialist first checks whether the request is time-sensitive enough to justify an off-system workaround, or whether it can simply wait for MK-LegalVault to be restored (the default expectation).

## Steps

1. Contracts Specialist confirms MK-LegalVault is genuinely unavailable (not just a personal connectivity issue) by checking with a colleague or the IT status page.
2. For non-urgent vendor contract requests, Contracts Specialist waits for MK-LegalVault to be restored and submits normally — this is the default and preferred path.
3. For genuinely urgent requests, Contracts Specialist documents the request details (who, what, why, when) in an email to the Legal Manager instead of the system.
4. The Legal Manager reviews the emailed request using the same criteria they would apply inside MK-LegalVault, and replies with an approval/rejection decision in writing.
5. Once MK-LegalVault is restored, Contracts Specialist or the Legal Manager re-enters the request and its outcome into MK-LegalVault retroactively, referencing the original email for the audit trail.
6. MK-LegalVault's record is tagged 'Entered Retroactively — System Outage' so reporting doesn't mistake the entry date for the actual request date.

## Responsible Role
Contracts Specialist

## Approval
Legal Manager

## Escalation
Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel

## Expected Result
The vendor contract is actioned without waiting for system restoration when genuinely urgent, while still ending up fully and correctly recorded in MK-LegalVault once it's back online.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._