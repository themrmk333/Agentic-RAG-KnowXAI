# Edge Case: New Employee Security Onboarding — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-SEC-007-EDGE-E",
  "title": "Edge Case: New Employee Security Onboarding \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Cybersecurity / Information Security",
  "department_code": "SEC",
  "category": "Onboarding",
  "subcategory": "Security Onboarding",
  "roles": [
    "Security Analyst",
    "Security Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "New Employee Security Onboarding",
    "edge case",
    "exception",
    "SEC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Security Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-SEC-007"
}
```

**Document ID:** SOP-SEC-007-EDGE-E
**Related SOP:** SOP-SEC-007 (New Employee Security Onboarding)
**Department:** Cybersecurity / Information Security

## Situation
Security Analyst submits a security onboarding request in MK-SecGuard that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Security Manager reviewing the request in MK-SecGuard notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Security Manager decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Security Manager does not approve or silently correct the request themselves; they return it to Security Analyst in MK-SecGuard with a specific note on what's missing or wrong.
2. Security Analyst is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. Security Analyst corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Security Manager reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Security Manager flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-SEC-007.

## Responsible Role
Security Analyst

## Approval
Security Manager

## Escalation
Security Analyst -> Incident Response Lead -> Security Manager -> CISO

## Expected Result
Incomplete or incorrect security onboarding requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._