# Edge Case: Compute Resource Request for Research — When the R&D Manager Is Unavailable

```json
{
  "document_id": "SOP-RND-007-EDGE-A",
  "title": "Edge Case: Compute Resource Request for Research \u2014 When the R&D Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Research & Development",
  "department_code": "RND",
  "category": "Infrastructure",
  "subcategory": "Compute Request",
  "roles": [
    "AI Research Engineer",
    "R&D Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Compute Resource Request for Research",
    "edge case",
    "exception",
    "RND"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "R&D Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-RND-007"
}
```

**Document ID:** SOP-RND-007-EDGE-A  
**Related SOP:** SOP-RND-007 (Compute Resource Request for Research)  
**Department:** Research & Development

## Scenario
The designated approver (R&D Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the compute request cannot wait for their return.

## Deviation Procedure

1. AI Research Engineer confirms the R&D Manager has an active out-of-office status in MK-Labs or MK-HRMS before invoking this path.
2. AI Research Engineer identifies the R&D Manager's designated delegate — typically the next role up the escalation chain (Research Associate -> Research Lead -> R&D Manager -> R&D Director) — as recorded in MK-Labs.
3. AI Research Engineer resubmits or flags the existing request in MK-Labs, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original R&D Manager would apply, and either approves, rejects, or requests clarification.
5. Once the R&D Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-Labs logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Compute Resource Request for Research decisions explicitly reserved for the R&D Manager by policy (e.g., anything requiring named signing authority); those must wait for the R&D Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Research Associate -> Research Lead -> R&D Manager -> R&D Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._