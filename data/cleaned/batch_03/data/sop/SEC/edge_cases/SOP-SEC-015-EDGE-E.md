# Edge Case: Security Policy Exception Request — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-SEC-015-EDGE-E",
  "title": "Edge Case: Security Policy Exception Request \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Governance",
  "subcategory": "Policy Exception Request",
  "roles": [
    "requester",
    "CISO"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Security Policy Exception Request",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "CISO",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-015"
}
```

**Document ID:** SOP-SEC-015-EDGE-E
**Related SOP:** SOP-SEC-015 (Security Policy Exception Request)
**Department:** Cybersecurity / Information Security

## Situation
requester submits a policy exception request request in MK-SecGuard that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The CISO reviewing the request in MK-SecGuard notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The CISO decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The CISO does not approve or silently correct the request themselves; they return it to requester in MK-SecGuard with a specific note on what's missing or wrong.
2. requester is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. requester corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The CISO reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the CISO flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-SEC-015.

## Responsible Role
requester

## Approval
CISO

## Escalation
Security Analyst -> Incident Response Lead -> Security Manager -> CISO

## Expected Result
Incomplete or incorrect policy exception request requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._