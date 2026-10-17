# Cross-Department Scenario (SEC + IT): Employee Loses a Company Device While Traveling

```json
{
  "document_id": "XSCEN-SEC-IT-03",
  "title": "Employee Loses a Company Device While Traveling",
  "document_type": "Cross-Department Scenario",
  "department": "SEC + IT",
  "department_codes": [
    "SEC",
    "IT"
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
    "Employee Loses a Company Device While Traveling",
    "SEC",
    "IT",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "CISO / IT Director",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-SEC-IT-03
**Departments Involved:** SEC, IT

## Situation
An employee reports their company laptop was lost during travel.

## Resolution Steps

- The employee reports it immediately to both IT and Security — not just IT, given the security implications.
- IT triggers a remote wipe of the device if it has connectivity, or flags it for wipe on next connection.
- Security reviews whether the device had access to any Restricted-classified data and assesses exposure.
- IT issues a replacement device and re-provisions the employee's access following the Laptop Replacement Process.
- If Restricted data exposure is confirmed, it's escalated per the Data Breach Notification Procedure with Legal involved.

## Lesson
A lost device is simultaneously an IT hardware issue and a potential Security incident — both tracks run in parallel, not sequentially.

## Escalation Contacts
- SEC: Security Analyst -> Incident Response Lead -> Security Manager -> CISO
- IT: IT Support Engineer -> IT Manager -> IT Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._