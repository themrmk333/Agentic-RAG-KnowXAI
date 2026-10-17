# Edge Case: Remote Desktop / Screen Share Support Session — When the IT Support Engineer Is Unavailable

```json
{
  "document_id": "SOP-IT-014-EDGE-A",
  "title": "Edge Case: Remote Desktop / Screen Share Support Session \u2014 When the IT Support Engineer Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "IT Support / Information Technology",
  "department_code": "IT",
  "category": "Support Operations",
  "subcategory": "Remote Support Session",
  "roles": [
    "employee",
    "IT Support Engineer"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Remote Desktop / Screen Share Support Session",
    "edge case",
    "exception",
    "IT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "IT Support Engineer",
  "source": "synthetic-generated",
  "related_sop": "SOP-IT-014"
}
```

**Document ID:** SOP-IT-014-EDGE-A
**Related SOP:** SOP-IT-014 (Remote Desktop / Screen Share Support Session)
**Department:** IT Support / Information Technology

## Scenario
The designated approver (IT Support Engineer) is on leave, travel, or otherwise unreachable within the normal response window, but the remote support session cannot wait for their return.

## Deviation Procedure

1. employee confirms the IT Support Engineer has an active out-of-office status in MK-ServiceDesk or MK-HRMS before invoking this path.
2. employee identifies the IT Support Engineer's designated delegate — typically the next role up the escalation chain (IT Support Engineer -> IT Manager -> IT Director) — as recorded in MK-ServiceDesk.
3. employee resubmits or flags the existing request in MK-ServiceDesk, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original IT Support Engineer would apply, and either approves, rejects, or requests clarification.
5. Once the IT Support Engineer returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-ServiceDesk logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Remote Desktop / Screen Share Support Session decisions explicitly reserved for the IT Support Engineer by policy (e.g., anything requiring named signing authority); those must wait for the IT Support Engineer's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: IT Support Engineer -> IT Manager -> IT Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._