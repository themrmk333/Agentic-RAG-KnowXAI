# Edge Case: Local Development Environment Setup — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-ENG-005-EDGE-E",
  "title": "Edge Case: Local Development Environment Setup \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Onboarding",
  "subcategory": "Dev Environment",
  "roles": [
    "new Software Engineer",
    "Tech Lead"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Local Development Environment Setup",
    "edge case",
    "exception",
    "ENG"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Tech Lead",
  "source": "synthetic-generated",
  "related_sop": "SOP-ENG-005"
}
```

**Document ID:** SOP-ENG-005-EDGE-E
**Related SOP:** SOP-ENG-005 (Local Development Environment Setup)
**Department:** Software Engineering / Development

## Situation
new Software Engineer submits a dev environment request in MK-CodeForge that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Tech Lead reviewing the request in MK-CodeForge notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Tech Lead decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Tech Lead does not approve or silently correct the request themselves; they return it to new Software Engineer in MK-CodeForge with a specific note on what's missing or wrong.
2. new Software Engineer is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. new Software Engineer corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Tech Lead reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Tech Lead flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-ENG-005.

## Responsible Role
new Software Engineer

## Approval
Tech Lead

## Escalation
Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

## Expected Result
Incomplete or incorrect dev environment requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._