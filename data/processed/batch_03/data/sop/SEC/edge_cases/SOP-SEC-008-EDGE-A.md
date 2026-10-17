# Edge Case: Security Awareness Training Assignment — When the HR Business Partner Is Unavailable

```json
{
  "document_id": "SOP-SEC-008-EDGE-A",
  "title": "Edge Case: Security Awareness Training Assignment \u2014 When the HR Business Partner Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Training",
  "subcategory": "Training Assignment",
  "roles": [
    "Security Analyst",
    "HR Business Partner"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Security Awareness Training Assignment",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "HR Business Partner",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-008"
}
```

**Document ID:** SOP-SEC-008-EDGE-A  
**Related SOP:** SOP-SEC-008 (Security Awareness Training Assignment)  
**Department:** Cybersecurity / Information Security

## Scenario
The designated approver (HR Business Partner) is on leave, travel, or otherwise unreachable within the normal response window, but the training assignment cannot wait for their return.

## Deviation Procedure

1. Security Analyst confirms the HR Business Partner has an active out-of-office status in MK-SecGuard or MK-HRMS before invoking this path.
2. Security Analyst identifies the HR Business Partner's designated delegate — typically the next role up the escalation chain (Security Analyst -> Incident Response Lead -> Security Manager -> CISO) — as recorded in MK-SecGuard.
3. Security Analyst resubmits or flags the existing request in MK-SecGuard, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original HR Business Partner would apply, and either approves, rejects, or requests clarification.
5. Once the HR Business Partner returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-SecGuard logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Security Awareness Training Assignment decisions explicitly reserved for the HR Business Partner by policy (e.g., anything requiring named signing authority); those must wait for the HR Business Partner's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Security Analyst -> Incident Response Lead -> Security Manager -> CISO.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._