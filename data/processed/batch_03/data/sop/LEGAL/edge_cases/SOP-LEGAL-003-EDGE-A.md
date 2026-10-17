# Edge Case: Vendor Contract Negotiation Support — When the Legal Manager Is Unavailable

```json
{
  "document_id": "SOP-LEGAL-003-EDGE-A",
  "title": "Edge Case: Vendor Contract Negotiation Support \u2014 When the Legal Manager Is Unavailable",
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

**Document ID:** SOP-LEGAL-003-EDGE-A  
**Related SOP:** SOP-LEGAL-003 (Vendor Contract Negotiation Support)  
**Department:** Legal & Compliance

## Scenario
The designated approver (Legal Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the vendor contract cannot wait for their return.

## Deviation Procedure

1. Contracts Specialist confirms the Legal Manager has an active out-of-office status in MK-LegalVault or MK-HRMS before invoking this path.
2. Contracts Specialist identifies the Legal Manager's designated delegate — typically the next role up the escalation chain (Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel) — as recorded in MK-LegalVault.
3. Contracts Specialist resubmits or flags the existing request in MK-LegalVault, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Legal Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Legal Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-LegalVault logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Vendor Contract Negotiation Support decisions explicitly reserved for the Legal Manager by policy (e.g., anything requiring named signing authority); those must wait for the Legal Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._