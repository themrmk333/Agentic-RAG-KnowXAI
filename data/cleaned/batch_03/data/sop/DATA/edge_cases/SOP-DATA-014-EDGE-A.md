# Edge Case: Third-Party Data Sharing Request — When the Legal Manager Is Unavailable

```json
{
  "document_id": "SOP-DATA-014-EDGE-A",
  "title": "Edge Case: Third-Party Data Sharing Request \u2014 When the Legal Manager Is Unavailable",
  "document_type": "SOP Edge Case",
  "department": "Data & Analytics",
  "department_code": "DATA",
  "category": "Data Sharing",
  "subcategory": "Data Sharing Request",
  "roles": [
    "requester",
    "Legal Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Third-Party Data Sharing Request",
    "edge case",
    "exception",
    "DATA"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Legal Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-DATA-014"
}
```

**Document ID:** SOP-DATA-014-EDGE-A
**Related SOP:** SOP-DATA-014 (Third-Party Data Sharing Request)
**Department:** Data & Analytics

## Scenario
The designated approver (Legal Manager) is on leave, travel, or otherwise unreachable within the normal response window, but the data sharing request cannot wait for their return.

## Deviation Procedure

1. requester confirms the Legal Manager has an active out-of-office status in MK-DataLake or MK-HRMS before invoking this path.
2. requester identifies the Legal Manager's designated delegate — typically the next role up the escalation chain (Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics) — as recorded in MK-DataLake.
3. requester resubmits or flags the existing request in MK-DataLake, tagging it 'Delegate Approval Required' with the reason.
4. The delegate reviews the request using the same criteria the original Legal Manager would apply, and either approves, rejects, or requests clarification.
5. Once the Legal Manager returns, they are notified of the delegate decision for their records; they may flag it for a follow-up review within 5 business days if something looks inconsistent with policy.
6. MK-DataLake logs both the delegate's identity and the reason for delegation on the request record for audit purposes.

## Important Note
Delegation does not apply to Third-Party Data Sharing Request decisions explicitly reserved for the Legal Manager by policy (e.g., anything requiring named signing authority); those must wait for the Legal Manager's return or be routed to the next level up, not a lateral delegate.

## Escalation
If this edge case procedure itself cannot be completed, escalate through: Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._