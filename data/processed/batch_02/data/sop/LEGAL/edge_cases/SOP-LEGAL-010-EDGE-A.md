# Edge Case: Customer Contract Renewal Legal Review — When the Legal Manager Is Unavailable

```json
{
  "document_id": "SOP-LEGAL-010-EDGE-A",
  "title": "Edge Case: Customer Contract Renewal Legal Review \u2014 When the Legal Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Legal & Compliance",
  "department_code": "LEGAL",
  "category": "Contract Management",
  "subcategory": "Renewal Contract Review",
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
    "Customer Contract Renewal Legal Review",
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
  "related_sop": "SOP-LEGAL-010"
}
```

**Document ID:** SOP-LEGAL-010-EDGE-A  
**Related SOP:** SOP-LEGAL-010 (Customer Contract Renewal Legal Review)  
**Department:** Legal & Compliance

## Scenario
The designated approver (Legal Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the renewal contract review cannot wait for their return.

## Deviation Procedure

1. Contracts Specialist confirms the Legal Manager has an active out-of-office status in MK-LegalVault or MK-HRMS before invoking this path.
2. Contracts Specialist identifies the Legal Manager's designated delegate — typically the next role up the escalation chain (Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel) — as recorded in MK-LegalVault.
3. Contracts Specialist resubmits or flags the existing request in MK-LegalVault, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Legal Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Legal Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-LegalVault logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Customer Contract Renewal Legal Review decisions explicitly reserved for the Legal Manager by policy (e.g., anything requiring named signing authority); those must wait for the Legal Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._