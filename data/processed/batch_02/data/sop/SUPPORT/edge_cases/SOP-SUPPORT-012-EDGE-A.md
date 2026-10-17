# Edge Case: Support Onboarding for New Hires — When the Support Manager Is Unavailable

```json
{
  "document_id": "SOP-SUPPORT-012-EDGE-A",
  "title": "Edge Case: Support Onboarding for New Hires \u2014 When the Support Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Customer Support / Helpdesk",
  "department_code": "SUPPORT",
  "category": "Onboarding",
  "subcategory": "Support Onboarding",
  "roles": [
    "Support Team Lead",
    "Support Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Support Onboarding for New Hires",
    "edge case",
    "exception",
    "SUPPORT"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Support Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SUPPORT-012"
}
```

**Document ID:** SOP-SUPPORT-012-EDGE-A  
**Related SOP:** SOP-SUPPORT-012 (Support Onboarding for New Hires)  
**Department:** Customer Support / Helpdesk

## Scenario
The designated approver (Support Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the support onboarding cannot wait for their return.

## Deviation Procedure

1. Support Team Lead confirms the Support Manager has an active out-of-office status in MK-SupportDesk or MK-HRMS before invoking this path.
2. Support Team Lead identifies the Support Manager's designated delegate — typically the next role up the escalation chain (Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director) — as recorded in MK-SupportDesk.
3. Support Team Lead resubmits or flags the existing request in MK-SupportDesk, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Support Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Support Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-SupportDesk logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Support Onboarding for New Hires decisions explicitly reserved for the Support Manager by policy (e.g., anything requiring named signing authority); those must wait for the Support Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._