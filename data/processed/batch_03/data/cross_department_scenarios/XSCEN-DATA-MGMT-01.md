# Cross-Department Scenario (DATA + MGMT): An Executive Dashboard Number Doesn't Match What a Department Reports Independently

```json
{
  "document_id": "XSCEN-DATA-MGMT-01",
  "title": "An Executive Dashboard Number Doesn't Match What a Department Reports Independently",
  "document_type": "Cross-Department Scenario",
  "department": "DATA + MGMT",
  "department_codes": [
    "DATA",
    "MGMT"
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
    "An Executive Dashboard Number Doesn't Match What a Department Reports Independently",
    "DATA",
    "MGMT",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Director of Data & Analytics / CEO Office",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-DATA-MGMT-01  
**Departments Involved:** DATA, MGMT

## Situation
The CEO Office notices the company-wide revenue figure on the executive dashboard doesn't match Sales' own reported number.

## Resolution Steps

- Data & Analytics checks whether both figures use the same KPI Governance definition and time period.
- If a definition mismatch is found, Data & Analytics corrects the dashboard or clarifies the discrepancy explicitly.
- If it's a data pipeline issue, it's treated as a Data Quality Incident and fixed with priority given executive visibility.
- Management is given a corrected figure with a brief explanation of what caused the mismatch.
- The KPI Governance catalog is updated to make the definition unambiguous for that specific metric going forward.

## Lesson
Executive-facing numbers get priority root-causing when they disagree with a department's own count — trust in the dashboard depends on it.

## Escalation Contacts
- DATA: Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics
- MGMT: Manager -> Director -> Vice President -> CEO Office

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._