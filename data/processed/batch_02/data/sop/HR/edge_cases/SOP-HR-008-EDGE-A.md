# Edge Case: Recruitment Requisition Procedure — When the HR Director Is Unavailable

```json
{
  "document_id": "SOP-HR-008-EDGE-A",
  "title": "Edge Case: Recruitment Requisition Procedure \u2014 When the HR Director Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Human Resources",
  "department_code": "HR",
  "category": "Recruitment",
  "subcategory": "Requisition",
  "roles": [
    "Hiring Manager",
    "HR Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Recruitment Requisition Procedure",
    "edge case",
    "exception",
    "HR"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "HR Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-HR-008"
}
```

**Document ID:** SOP-HR-008-EDGE-A  
**Related SOP:** SOP-HR-008 (Recruitment Requisition Procedure)  
**Department:** Human Resources

## Scenario
The designated approver (HR Director) is on leave, travel, or otherwise unreachable within the normal response window, but the requisition cannot wait for their return.

## Deviation Procedure

1. Hiring Manager confirms the HR Director has an active out-of-office status in MK-HRMS or MK-HRMS before invoking this path.
2. Hiring Manager identifies the HR Director's designated delegate — typically the next role up the escalation chain (HR Executive -> HR Business Partner -> HR Manager -> HR Director) — as recorded in MK-HRMS.
3. Hiring Manager resubmits or flags the existing request in MK-HRMS, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original HR Director would apply, and either approves, rejects, or requests clarification.
5. Once the HR Director returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-HRMS logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Recruitment Requisition Procedure decisions explicitly reserved for the HR Director by policy (e.g., anything requiring named signing authority); those must wait for the HR Director's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: HR Executive -> HR Business Partner -> HR Manager -> HR Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._