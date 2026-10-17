# Cross-Department Scenario (FIN + PROC): Vendor Payment Blocked Because PO and Invoice Don't Match

```json
{
  "document_id": "XSCEN-FIN-PROC-01",
  "title": "Vendor Payment Blocked Because PO and Invoice Don't Match",
  "document_type": "Cross-Department Scenario",
  "department": "FIN + PROC",
  "department_codes": [
    "FIN",
    "PROC"
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
    "Vendor Payment Blocked Because PO and Invoice Don't Match",
    "FIN",
    "PROC",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Director / Procurement Director",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-FIN-PROC-01
**Departments Involved:** FIN, PROC

## Situation
Finance's three-way match fails because Procurement's purchase order quantity doesn't match what was actually delivered.

## Resolution Steps

- Finance places the invoice on hold rather than paying against a mismatched PO.
- Procurement checks the Goods Receipt record to see whether a partial shipment was received.
- If it was a partial shipment, Procurement updates the PO to reflect the partial receipt and requests a partial-invoice split from the vendor.
- Finance re-runs the three-way match against the corrected PO and processes payment for the matched portion.
- Both departments agree the vendor should be asked to invoice per shipment going forward to avoid recurrence.

## Lesson
A three-way match failure is a signal to investigate the underlying shipment, not just to reject the invoice outright.

## Escalation Contacts
- FIN: Accountant -> Finance Lead -> Finance Manager -> Finance Director
- PROC: Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._