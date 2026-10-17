# Edge Case: Phishing Email Reporting Procedure — When the Security Analyst Is Unavailable

```json
{
  "document_id": "SOP-SEC-001-EDGE-A",
  "title": "Edge Case: Phishing Email Reporting Procedure \u2014 When the Security Analyst Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Phishing",
  "subcategory": "Phishing Report",
  "roles": [
    "employee",
    "Security Analyst"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Phishing Email Reporting Procedure",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Analyst",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-001"
}
```

**Document ID:** SOP-SEC-001-EDGE-A
**Related SOP:** SOP-SEC-001 (Phishing Email Reporting Procedure)
**Department:** Cybersecurity / Information Security

## Scenario
The designated approver (Security Analyst) is on leave, travel, or otherwise unreachable within the normal response window, but the phishing report cannot wait for their return.

## Deviation Procedure

1. employee confirms the Security Analyst has an active out-of-office status in MK-SecGuard or MK-HRMS before invoking this path.
2. employee identifies the Security Analyst's designated delegate — typically the next role up the escalation chain (Security Analyst -> Incident Response Lead -> Security Manager -> CISO) — as recorded in MK-SecGuard.
3. employee resubmits or flags the existing request in MK-SecGuard, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Security Analyst would apply, and either approves, rejects, or requests clarification.
5. Once the Security Analyst returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-SecGuard logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Phishing Email Reporting Procedure decisions explicitly reserved for the Security Analyst by policy (e.g., anything requiring named signing authority); those must wait for the Security Analyst's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Security Analyst -> Incident Response Lead -> Security Manager -> CISO.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._