# Edge Case: New Repository Setup — When the Engineering Manager Is Unavailable

```json
{
  "document_id": "SOP-ENG-003-EDGE-A",
  "title": "Edge Case: New Repository Setup \u2014 When the Engineering Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Version Control",
  "subcategory": "Repository",
  "roles": [
    "Software Engineer",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "New Repository Setup",
    "edge case",
    "exception",
    "ENG"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-ENG-003"
}
```

**Document ID:** SOP-ENG-003-EDGE-A  
**Related SOP:** SOP-ENG-003 (New Repository Setup)  
**Department:** Software Engineering / Development

## Scenario
The designated approver (Engineering Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the repository cannot wait for their return.

## Deviation Procedure

1. Software Engineer confirms the Engineering Manager has an active out-of-office status in MK-CodeForge or MK-HRMS before invoking this path.
2. Software Engineer identifies the Engineering Manager's designated delegate — typically the next role up the escalation chain (Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director) — as recorded in MK-CodeForge.
3. Software Engineer resubmits or flags the existing request in MK-CodeForge, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Engineering Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Engineering Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-CodeForge logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to New Repository Setup decisions explicitly reserved for the Engineering Manager by policy (e.g., anything requiring named signing authority); those must wait for the Engineering Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._