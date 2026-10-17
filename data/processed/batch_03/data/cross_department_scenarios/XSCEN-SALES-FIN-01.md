# Cross-Department Scenario (SALES + FIN): A Closed-Won Deal's Contract Value Doesn't Match What's Entered in MK-CRM

```json
{
  "document_id": "XSCEN-SALES-FIN-01",
  "title": "A Closed-Won Deal's Contract Value Doesn't Match What's Entered in MK-CRM",
  "document_type": "Cross-Department Scenario",
  "department": "SALES + FIN",
  "department_codes": [
    "SALES",
    "FIN"
  ],
  "category": "Cross-Department Scenario",
  "roles": [
    "All Employees"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "A Closed-Won Deal's Contract Value Doesn't Match What's Entered in MK-CRM",
    "SALES",
    "FIN",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Sales Director / Finance Director",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-SALES-FIN-01  
**Departments Involved:** SALES, FIN

## Situation
Finance notices the signed contract amount differs from the opportunity value recorded in MK-CRM before invoicing the customer.

## Resolution Steps

- Finance holds invoicing until the discrepancy is resolved rather than invoicing either figure.
- The Account Executive checks whether a last-minute negotiation changed the price after the opportunity was last updated.
- MK-CRM is corrected to match the actual signed contract, which is the source of truth.
- Finance proceeds with invoicing against the corrected, verified amount.
- Sales Order Booking procedure is reinforced: MK-CRM must be updated before, not after, invoicing is requested.

## Lesson
The signed contract is always the source of truth for invoicing — CRM data is corrected to match it, never the other way around.

## Escalation Contacts
- SALES: Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director
- FIN: Accountant -> Finance Lead -> Finance Manager -> Finance Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._