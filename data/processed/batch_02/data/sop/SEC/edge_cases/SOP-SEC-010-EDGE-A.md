# Edge Case: Firewall / Network Access Change Request — When the Security Manager Is Unavailable

```json
{
  "document_id": "SOP-SEC-010-EDGE-A",
  "title": "Edge Case: Firewall / Network Access Change Request \u2014 When the Security Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Network Security",
  "subcategory": "Firewall Change Request",
  "roles": [
    "requester",
    "Security Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Firewall / Network Access Change Request",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-010"
}
```

**Document ID:** SOP-SEC-010-EDGE-A  
**Related SOP:** SOP-SEC-010 (Firewall / Network Access Change Request)  
**Department:** Cybersecurity / Information Security

## Scenario
The designated approver (Security Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the firewall change request cannot wait for their return.

## Deviation Procedure

1. requester confirms the Security Manager has an active out-of-office status in MK-SecGuard or MK-HRMS before invoking this path.
2. requester identifies the Security Manager's designated delegate — typically the next role up the escalation chain (Security Analyst -> Incident Response Lead -> Security Manager -> CISO) — as recorded in MK-SecGuard.
3. requester resubmits or flags the existing request in MK-SecGuard, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Security Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Security Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-SecGuard logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Firewall / Network Access Change Request decisions explicitly reserved for the Security Manager by policy (e.g., anything requiring named signing authority); those must wait for the Security Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Security Analyst -> Incident Response Lead -> Security Manager -> CISO.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._