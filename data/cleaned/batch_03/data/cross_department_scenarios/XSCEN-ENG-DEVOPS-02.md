# Cross-Department Scenario (ENG + DEVOPS): Auto-scaling Fails to Trigger During a Traffic Spike

```json
{
  "document_id": "XSCEN-ENG-DEVOPS-02",
  "title": "Auto-scaling Fails to Trigger During a Traffic Spike",
  "document_type": "Cross-Department Scenario",
  "department": "ENG + DEVOPS",
  "department_codes": [
    "ENG",
    "DEVOPS"
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
    "Auto-scaling Fails to Trigger During a Traffic Spike",
    "ENG",
    "DEVOPS",
    "cross-department"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Director / DevOps Director",
  "source": "synthetic-generated"
}
```

**Document ID:** XSCEN-ENG-DEVOPS-02
**Departments Involved:** ENG, DEVOPS

## Situation
A marketing campaign drives unexpected traffic, but the auto-scaling policy doesn't add capacity in time, causing slow response times.

## Resolution Steps

- DevOps checks whether the metric source (CPU/memory) is reporting correctly during the spike.
- If the metric source is fine, DevOps manually scales capacity immediately to restore performance.
- Engineering and DevOps jointly review whether the scaling thresholds were set too conservatively for this traffic pattern.
- Marketing is asked to give DevOps advance notice of major campaigns going forward so capacity can be pre-provisioned.
- The auto-scaling policy is updated and load-tested against a simulated version of the spike before the next campaign.

## Lesson
Auto-scaling policies need both a technical fix and a process fix (advance notice from Marketing) to fully prevent recurrence.

## Escalation Contacts
- ENG: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director
- DEVOPS: DevOps Engineer -> DevOps Manager -> DevOps Director

---
_This cross-department scenario is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._