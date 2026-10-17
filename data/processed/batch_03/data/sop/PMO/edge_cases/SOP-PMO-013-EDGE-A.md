# Edge Case: Project Quality Gate Review — When the QA Lead Is Unavailable

```json
{
  "document_id": "SOP-PMO-013-EDGE-A",
  "title": "Edge Case: Project Quality Gate Review \u2014 When the QA Lead Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Project Management / PMO",
  "department_code": "PMO",
  "category": "Quality Management",
  "subcategory": "Quality Gate",
  "roles": [
    "Project Manager",
    "QA Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Project Quality Gate Review",
    "edge case",
    "exception",
    "PMO"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "QA Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-PMO-013"
}
```

**Document ID:** SOP-PMO-013-EDGE-A  
**Related SOP:** SOP-PMO-013 (Project Quality Gate Review)  
**Department:** Project Management / PMO

## Scenario
The designated approver (QA Lead) is on leave, travel, or otherwise unreachable within the normal response window, but the quality gate cannot wait for their return.

## Deviation Procedure

1. Project Manager confirms the QA Lead has an active out-of-office status in MK-PMTrack or MK-HRMS before invoking this path.
2. Project Manager identifies the QA Lead's designated delegate — typically the next role up the escalation chain (Project Coordinator -> Project Manager -> PMO Lead -> PMO Director) — as recorded in MK-PMTrack.
3. Project Manager resubmits or flags the existing request in MK-PMTrack, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original QA Lead would apply, and either approves, rejects, or requests clarification.
5. Once the QA Lead returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-PMTrack logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Project Quality Gate Review decisions explicitly reserved for the QA Lead by policy (e.g., anything requiring named signing authority); those must wait for the QA Lead's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Project Coordinator -> Project Manager -> PMO Lead -> PMO Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._