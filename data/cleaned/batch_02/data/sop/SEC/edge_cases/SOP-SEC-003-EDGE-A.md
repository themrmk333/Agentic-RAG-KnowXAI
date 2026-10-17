# Edge Case: Security Incident Response Procedure — When the Incident Response Lead Is Unavailable

```json
{
  "document_id": "SOP-SEC-003-EDGE-A",
  "title": "Edge Case: Security Incident Response Procedure \u2014 When the Incident Response Lead Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Incident Response",
  "subcategory": "Security Incident",
  "roles": [
    "Security Analyst",
    "Incident Response Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Security Incident Response Procedure",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Incident Response Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-003"
}
```

**Document ID:** SOP-SEC-003-EDGE-A
**Related SOP:** SOP-SEC-003 (Security Incident Response Procedure)
**Department:** Cybersecurity / Information Security

## Scenario
The designated approver (Incident Response Lead) is on leave, travel, or otherwise unreachable within the normal response window, but the security incident cannot wait for their return.

## Deviation Procedure

1. Security Analyst confirms the Incident Response Lead has an active out-of-office status in MK-SecGuard or MK-HRMS before invoking this path.
2. Security Analyst identifies the Incident Response Lead's designated delegate — typically the next role up the escalation chain (Security Analyst -> Incident Response Lead -> Security Manager -> CISO) — as recorded in MK-SecGuard.
3. Security Analyst resubmits or flags the existing request in MK-SecGuard, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Incident Response Lead would apply, and either approves, rejects, or requests clarification.
5. Once the Incident Response Lead returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-SecGuard logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Security Incident Response Procedure decisions explicitly reserved for the Incident Response Lead by policy (e.g., anything requiring named signing authority); those must wait for the Incident Response Lead's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Security Analyst -> Incident Response Lead -> Security Manager -> CISO.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._