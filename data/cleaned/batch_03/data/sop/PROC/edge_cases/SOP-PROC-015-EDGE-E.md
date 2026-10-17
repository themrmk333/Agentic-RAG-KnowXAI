# Edge Case: Procurement Policy Exception Request — Missing Documentation or Incorrect Submission

```json
{
  "document_id": "SOP-PROC-015-EDGE-E",
  "title": "Edge Case: Procurement Policy Exception Request \u2014 Missing Documentation or Incorrect Submission",
  "document_type": "SOP Edge Case",
  "department": "Procurement / Purchasing",
  "department_code": "PROC",
  "category": "Governance",
  "subcategory": "Procurement Policy Exception",
  "roles": [
    "requester",
    "Procurement Director"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Procurement Policy Exception Request",
    "edge case",
    "exception",
    "PROC"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Procurement Director",
  "source": "synthetic-generated",
  "related_sop": "SOP-PROC-015"
}
```

**Document ID:** SOP-PROC-015-EDGE-E
**Related SOP:** SOP-PROC-015 (Procurement Policy Exception Request)
**Department:** Procurement / Purchasing

## Situation
requester submits a procurement policy exception request in MK-ProcureX that is missing required supporting information, or contains incorrect details (wrong amount, wrong employee, wrong date).

## Detection
The Procurement Director reviewing the request in MK-ProcureX notices a required field is blank, a required attachment is missing, or the details don't reconcile with other records (e.g., an amount that doesn't match the attached receipt).

## Decision Criteria
The Procurement Director decides whether the gap is minor enough to request a quick correction, or serious enough that the request should be rejected outright and resubmitted from scratch.

## Steps

1. The Procurement Director does not approve or silently correct the request themselves; they return it to requester in MK-ProcureX with a specific note on what's missing or wrong.
2. requester is notified automatically and has a defined window (typically 5 business days) to correct and resubmit before the request is auto-closed as abandoned.
3. requester corrects the specific issue identified — not a wholesale re-submission — and resubmits, keeping the same request thread rather than opening a new one.
4. The Procurement Director reviews only the corrected fields on resubmission rather than re-reviewing the entire request from zero, to keep turnaround fast.
5. If the same requester repeatedly submits incomplete requests (3+ times in a quarter), the Procurement Director flags this to the requester's manager for a coaching conversation.
6. Once complete and accurate, the request proceeds through the standard approval procedure in SOP-PROC-015.

## Responsible Role
requester

## Approval
Procurement Director

## Escalation
Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director

## Expected Result
Incomplete or incorrect procurement policy exception requests are corrected quickly through the same request thread, without being silently fixed by the approver or endlessly bounced back and forth.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._