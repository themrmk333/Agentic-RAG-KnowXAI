# Edge Case: Patent Disclosure Procedure — When the General Counsel Is Unavailable

```json
{
  "document_id": "SOP-RND-009-EDGE-A",
  "title": "Edge Case: Patent Disclosure Procedure \u2014 When the General Counsel Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Research & Development",
  "department_code": "RND",
  "category": "Intellectual Property",
  "subcategory": "Invention Disclosure",
  "roles": [
    "Research Engineer",
    "General Counsel"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Patent Disclosure Procedure",
    "edge case",
    "exception",
    "RND"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "General Counsel",
  "source": "synthetic-generated",
  "related_sop": "SOP-RND-009"
}
```

**Document ID:** SOP-RND-009-EDGE-A
**Related SOP:** SOP-RND-009 (Patent Disclosure Procedure)
**Department:** Research & Development

## Scenario
The designated approver (General Counsel) is on leave, travel, or otherwise unreachable within the normal response window, but the invention disclosure cannot wait for their return.

## Deviation Procedure

1. Research Engineer confirms the General Counsel has an active out-of-office status in MK-Labs or MK-HRMS before invoking this path.
2. Research Engineer identifies the General Counsel's designated delegate — typically the next role up the escalation chain (Research Associate -> Research Lead -> R&D Manager -> R&D Director) — as recorded in MK-Labs.
3. Research Engineer resubmits or flags the existing request in MK-Labs, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original General Counsel would apply, and either approves, rejects, or requests clarification.
5. Once the General Counsel returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-Labs logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Patent Disclosure Procedure decisions explicitly reserved for the General Counsel by policy (e.g., anything requiring named signing authority); those must wait for the General Counsel's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Research Associate -> Research Lead -> R&D Manager -> R&D Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._