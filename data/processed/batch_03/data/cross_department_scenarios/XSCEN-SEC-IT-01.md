# Cross-Department Scenario (SEC + IT): A Phishing Email Leads to a Compromised Account

```json
{
  "document_id": "XSCEN-SEC-IT-01",
  "title": "A Phishing Email Leads to a Compromised Account",
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
    "A Phishing Email Leads to a Compromised Account",
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

**Document ID:** XSCEN-SEC-IT-01  
**Departments Involved:** SEC, IT

## Situation
An employee clicks a phishing link and enters their credentials on a fake login page.

## Resolution Steps

- The employee reports it immediately via the Report Phishing button, and Security is alerted.
- Security force-resets the employee's password and revokes all active sessions immediately via IT.
- IT re-issues MFA enrollment for the employee to ensure no attacker-controlled device remains enrolled.
- Security reviews account activity logs for any unauthorized access between compromise and reset.
- If any unauthorized access occurred, it's escalated per the Security Incident Response Procedure; otherwise the case is closed with lessons logged.

## Lesson
IT's account tools (password reset, MFA re-enrollment) are the execution arm of Security's incident response decisions.

## Escalation Contacts
- SEC: Security Analyst -> Incident Response Lead -> Security Manager -> CISO
- IT: IT Support Engineer -> IT Manager -> IT Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._