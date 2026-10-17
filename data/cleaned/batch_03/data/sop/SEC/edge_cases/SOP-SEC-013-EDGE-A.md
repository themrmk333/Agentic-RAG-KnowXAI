# Edge Case: Penetration Test Coordination — When the CISO Is Unavailable

```json
{
  "document_id": "SOP-SEC-013-EDGE-A",
  "title": "Edge Case: Penetration Test Coordination \u2014 When the CISO Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Security Testing",
  "subcategory": "Penetration Test",
  "roles": [
    "Security Engineer",
    "CISO"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Penetration Test Coordination",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "CISO",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-013"
}
```

**Document ID:** SOP-SEC-013-EDGE-A
**Related SOP:** SOP-SEC-013 (Penetration Test Coordination)
**Department:** Cybersecurity / Information Security

## Scenario
The designated approver (CISO) is on leave, travel, or otherwise unreachable within the normal response window, but the penetration test cannot wait for their return.

## Deviation Procedure

1. Security Engineer confirms the CISO has an active out-of-office status in MK-SecGuard or MK-HRMS before invoking this path.
2. Security Engineer identifies the CISO's designated delegate — typically the next role up the escalation chain (Security Analyst -> Incident Response Lead -> Security Manager -> CISO) — as recorded in MK-SecGuard.
3. Security Engineer resubmits or flags the existing request in MK-SecGuard, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original CISO would apply, and either approves, rejects, or requests clarification.
5. Once the CISO returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-SecGuard logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Penetration Test Coordination decisions explicitly reserved for the CISO by policy (e.g., anything requiring named signing authority); those must wait for the CISO's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Security Analyst -> Incident Response Lead -> Security Manager -> CISO.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._