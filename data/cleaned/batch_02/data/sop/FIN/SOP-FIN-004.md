# SOP: Invoice Processing Procedure

```json
{
  "document_id": "SOP-FIN-004",
  "title": "Invoice Processing Procedure",
  "document_type": "SOP",
  "department": "Finance & Accounting",
  "department_code": "FIN",
  "category": "Accounts Payable",
  "subcategory": "Vendor Invoice",
  "roles": [
    "Accountant",
    "Finance Lead"
  ],
  "access_level": "general",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Invoice Processing Procedure",
    "Accounts Payable",
    "Vendor Invoice",
    "FIN",
    "MK-Finance360"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Finance Lead",
  "source": "synthetic-generated"
}
```

**Document ID:** SOP-FIN-004
**Department:** Finance & Accounting
**Applicable Roles:** Accountant, Finance Lead
**Access Level:** general
**Effective Date:** 2026-08-26  |  **Review Date:** 2027-08-26  |  **Revision:** 1.0

## Purpose

This SOP defines the standard procedure for **invoice processing procedure** within the Finance & Accounting department at MK-INFINITE-AI PRIVATE LIMITED, ensuring the process is followed consistently, is auditable, and meets the department's service expectations.

## Scope

This procedure applies to all Accountants and any employee across MK-Infinite-AI who needs to initiate a **Vendor Invoice** request. It covers the full workflow from initiation through to closure in MK-Finance360.

## Applicable Roles

- Primary actor: **Accountant**
- Approver: **Finance Lead**
- System of record: **MK-Finance360**

## Preconditions

- The requester has an active MK-Infinite-AI account and access to MK-Finance360.
- A three-way match against the purchase order and goods receipt must be available before starting this procedure.

## Required Information

- Employee ID and department
- Details of the vendor invoice being requested
- Any supporting documentation required for approval

## Procedure

**Step 1:** the Accountant confirms eligibility and prerequisites: a three-way match against the purchase order and goods receipt.

**Step 2:** the Accountant raises a request in MK-Finance360 specifying exactly which Vendor Invoice is required.

**Step 3:** The Finance Lead reviews and approves the request, applying least-privilege / need-basis principles.

**Step 4:** Once approved, the assigned engineer provisions or configures the Vendor Invoice in the relevant system.

**Step 5:** the Accountant is notified and asked to test and verify the access or functionality.

**Step 6:** Any issues found during verification are logged in MK-Finance360 and corrected before sign-off.

**Step 7:** MK-Finance360 marks the request 'Complete' and the configuration is logged for audit and future reference. Invoices without a matching PO are routed to Procurement for clarification.

## Expected Result

The vendor invoice is completed, logged in MK-Finance360, and the requester is notified of the outcome. The record remains available in MK-Finance360 for future reference and audit.

## Exceptions

- Invoices without a matching PO are routed to Procurement for clarification.
- Requests that do not meet the preconditions above are returned to the requester with an explanation rather than being rejected outright.

## Escalation Procedure

If the request is not actioned within the expected timeframe, escalate in this order: Accountant → Finance Lead → Finance Manager → Finance Director. Escalations should reference the SOP-FIN-004 document ID and the relevant ticket/request number.

## Responsible Role

Accountant

## Approval Role

Finance Lead

---

_This SOP is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset. It does not represent any real company's actual procedures._