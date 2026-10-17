# Edge Case: Contract Review Request Procedure — When the Senior Legal Counsel Is Unavailable

```json
{
  "document_id": "SOP-LEGAL-001-EDGE-A",
  "title": "Edge Case: Contract Review Request Procedure \u2014 When the Senior Legal Counsel Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Legal & Compliance",
  "department_code": "LEGAL",
  "category": "Contract Management",
  "subcategory": "Contract Review Request",
  "roles": [
    "requester",
    "Senior Legal Counsel"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Contract Review Request Procedure",
    "edge case",
    "exception",
    "LEGAL"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Senior Legal Counsel",
  "source": "synthetic-generated",
  "related_sop": "SOP-LEGAL-001"
}
```

**Document ID:** SOP-LEGAL-001-EDGE-A
**Related SOP:** SOP-LEGAL-001 (Contract Review Request Procedure)
**Department:** Legal & Compliance

## Scenario
The designated approver (Senior Legal Counsel) is on leave, travel, or otherwise unreachable within the normal response window, but the contract review request cannot wait for their return.

## Deviation Procedure

1. requester confirms the Senior Legal Counsel has an active out-of-office status in MK-LegalVault or MK-HRMS before invoking this path.
2. requester identifies the Senior Legal Counsel's designated delegate — typically the next role up the escalation chain (Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel) — as recorded in MK-LegalVault.
3. requester resubmits or flags the existing request in MK-LegalVault, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Senior Legal Counsel would apply, and either approves, rejects, or requests clarification.
5. Once the Senior Legal Counsel returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-LegalVault logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Contract Review Request Procedure decisions explicitly reserved for the Senior Legal Counsel by policy (e.g., anything requiring named signing authority); those must wait for the Senior Legal Counsel's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._