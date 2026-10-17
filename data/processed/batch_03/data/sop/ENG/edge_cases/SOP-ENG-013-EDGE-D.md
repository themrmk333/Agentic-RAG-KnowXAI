# Edge Case: Production Incident Response (Engineering) — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-ENG-013-EDGE-D",
  "title": "Edge Case: Production Incident Response (Engineering) \u2014 Rejected or Duplicate Request Handling",
  "document_type": "SOP Edge Case",
  "department": "Software Engineering / Development",
  "department_code": "ENG",
  "category": "Incident Management",
  "subcategory": "Production Incident",
  "roles": [
    "on-call Software Engineer",
    "Engineering Manager"
  ],
  "access_level": "employee",
  "allowed_departments": [
    "ALL"
  ],
  "confidentiality": "Internal",
  "keywords": [
    "Production Incident Response (Engineering)",
    "edge case",
    "exception",
    "ENG"
  ],
  "created_date": "2026-08-26",
  "updated_date": "2026-08-26",
  "version": "1.0",
  "status": "Active",
  "owner": "Engineering Manager",
  "source": "synthetic-generated",
  "related_sop": "SOP-ENG-013"
}
```

**Document ID:** SOP-ENG-013-EDGE-D  
**Related SOP:** SOP-ENG-013 (Production Incident Response (Engineering))  
**Department:** Software Engineering / Development

## Situation
A production incident request is rejected by the Engineering Manager, or on-call Software Engineer accidentally submits the same request twice in MK-CodeForge.

## Detection
MK-CodeForge shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Engineering Manager (for rejections) or MK-CodeForge itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Engineering Manager records a specific rejection reason in MK-CodeForge — a bare 'Rejected' status without a reason is not acceptable practice.
2. on-call Software Engineer reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If on-call Software Engineer disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-CodeForge flags the second entry automatically; the on-call Software Engineer or Engineering Manager confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Engineering Manager initiates the standard reversal process instead of just closing the record.
6. MK-CodeForge retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
on-call Software Engineer

## Approval
Engineering Manager

## Escalation
Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

## Expected Result
Rejections always carry a documented reason and a clear next step for on-call Software Engineer, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._