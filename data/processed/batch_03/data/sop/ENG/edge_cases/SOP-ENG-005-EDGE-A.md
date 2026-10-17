# Edge Case: Local Development Environment Setup — When the Tech Lead Is Unavailable

```json
{
  "document_id": "SOP-ENG-005-EDGE-A",
  "title": "Edge Case: Local Development Environment Setup \u2014 When the Tech Lead Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Onboarding",
  "subcategory": "Dev Environment",
  "roles": [
    "new Software Engineer",
    "Tech Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Local Development Environment Setup",
    "edge case",
    "exception",
    "ENG"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Tech Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-ENG-005"
}
```

**Document ID:** SOP-ENG-005-EDGE-A  
**Related SOP:** SOP-ENG-005 (Local Development Environment Setup)  
**Department:** Software Engineering / Development

## Scenario
The designated approver (Tech Lead) is on leave, travel, or otherwise unreachable within the normal response window, but the dev environment cannot wait for their return.

## Deviation Procedure

1. new Software Engineer confirms the Tech Lead has an active out-of-office status in MK-CodeForge or MK-HRMS before invoking this path.
2. new Software Engineer identifies the Tech Lead's designated delegate — typically the next role up the escalation chain (Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director) — as recorded in MK-CodeForge.
3. new Software Engineer resubmits or flags the existing request in MK-CodeForge, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Tech Lead would apply, and either approves, rejects, or requests clarification.
5. Once the Tech Lead returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-CodeForge logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Local Development Environment Setup decisions explicitly reserved for the Tech Lead by policy (e.g., anything requiring named signing authority); those must wait for the Tech Lead's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._