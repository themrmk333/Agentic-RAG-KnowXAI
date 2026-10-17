# Edge Case: Analytics Tool Access Provisioning — When the Data Manager Is Unavailable

```json
{
  "document_id": "SOP-DATA-015-EDGE-A",
  "title": "Edge Case: Analytics Tool Access Provisioning \u2014 When the Data Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Access",
  "subcategory": "Analytics Tool Access",
  "roles": [
    "requester",
    "Data Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Analytics Tool Access Provisioning",
    "edge case",
    "exception",
    "DATA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Data Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-DATA-015"
}
```

**Document ID:** SOP-DATA-015-EDGE-A  
**Related SOP:** SOP-DATA-015 (Analytics Tool Access Provisioning)  
**Department:** Data & Analytics

## Scenario
The designated approver (Data Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the analytics tool access cannot wait for their return.

## Deviation Procedure

1. requester confirms the Data Manager has an active out-of-office status in MK-DataLake or MK-HRMS before invoking this path.
2. requester identifies the Data Manager's designated delegate — typically the next role up the escalation chain (Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics) — as recorded in MK-DataLake.
3. requester resubmits or flags the existing request in MK-DataLake, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Data Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Data Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-DataLake logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Analytics Tool Access Provisioning decisions explicitly reserved for the Data Manager by policy (e.g., anything requiring named signing authority); those must wait for the Data Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._