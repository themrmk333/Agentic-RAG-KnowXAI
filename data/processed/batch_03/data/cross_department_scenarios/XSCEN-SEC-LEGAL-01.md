# Cross-Department Scenario (SEC + LEGAL): A Security Incident May Involve Customer Data

```json
{
  "document_id": "XSCEN-SEC-LEGAL-01",
  "title": "A Security Incident May Involve Customer Data",
  "document_type": "Cross-Department Scenario",
  "department": "SEC + LEGAL",
  "department_codes": [
    "SEC",
    "LEGAL"
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
    "A Security Incident May Involve Customer Data",
    "SEC",
    "LEGAL",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "CISO / General Counsel",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-SEC-LEGAL-01  
**Departments Involved:** SEC, LEGAL

## Situation
A confirmed security incident potentially exposed a subset of customer records.

## Resolution Steps

- Security contains the incident first, per the Incident Response Policy, before full scope is known.
- Security notifies Legal within 4 hours of confirming the incident involves customer data, per policy.
- Legal assesses regulatory notification obligations based on the data types and affected jurisdictions.
- Security and Legal jointly determine what can be communicated externally and when.
- A joint post-incident review captures both the technical response and the regulatory response for the record.

## Lesson
Security owns containment and technical response; Legal owns regulatory and disclosure obligations — both are required, not either/or.

## Escalation Contacts
- SEC: Security Analyst -> Incident Response Lead -> Security Manager -> CISO
- LEGAL: Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._