# Edge Case: Employee Referral Program Procedure — When the HR Executive Is Unavailable

```json
{
  "document_id": "SOP-HR-016-EDGE-A",
  "title": "Edge Case: Employee Referral Program Procedure \u2014 When the HR Executive Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Human Resources",
  "department_code": "HR",
  "category": "Recruitment",
  "subcategory": "Referral Submission",
  "roles": [
    "employee",
    "HR Executive"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Employee Referral Program Procedure",
    "edge case",
    "exception",
    "HR"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "HR Executive",
  "source": "synthetic-generated",
  "related_sop": "SOP-HR-016"
}
```

**Document ID:** SOP-HR-016-EDGE-A  
**Related SOP:** SOP-HR-016 (Employee Referral Program Procedure)  
**Department:** Human Resources

## Scenario
The designated approver (HR Executive) is on leave, travel, or otherwise unreachable within the normal response window, but the referral submission cannot wait for their return.

## Deviation Procedure

1. employee confirms the HR Executive has an active out-of-office status in MK-HRMS or MK-HRMS before invoking this path.
2. employee identifies the HR Executive's designated delegate — typically the next role up the escalation chain (HR Executive -> HR Business Partner -> HR Manager -> HR Director) — as recorded in MK-HRMS.
3. employee resubmits or flags the existing request in MK-HRMS, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original HR Executive would apply, and either approves, rejects, or requests clarification.
5. Once the HR Executive returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-HRMS logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Employee Referral Program Procedure decisions explicitly reserved for the HR Executive by policy (e.g., anything requiring named signing authority); those must wait for the HR Executive's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: HR Executive -> HR Business Partner -> HR Manager -> HR Director.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._