# Edge Case: Local Development Environment Setup — Rejected or Duplicate Request Handling

```json
{
  "document_id": "SOP-ENG-005-EDGE-D",
  "title": "Edge Case: Local Development Environment Setup \u2014 Rejected or Duplicate Request Handling",
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

**Document ID:** SOP-ENG-005-EDGE-D  
**Related SOP:** SOP-ENG-005 (Local Development Environment Setup)  
**Department:** Software Engineering / Development

## Situation
A dev environment request is rejected by the Tech Lead, or new Software Engineer accidentally submits the same request twice in MK-CodeForge.

## Detection
MK-CodeForge shows two open requests with identical or near-identical details from the same requester within a short window, or a request status changes to 'Rejected' with a reason code.

## Decision Criteria
The Tech Lead (for rejections) or MK-CodeForge itself (for duplicates, via a similarity check) determines whether to merge, close, or require resubmission.

## Steps

1. On rejection, the Tech Lead records a specific rejection reason in MK-CodeForge — a bare 'Rejected' status without a reason is not acceptable practice.
2. new Software Engineer reviews the rejection reason and either corrects the issue and resubmits, or accepts the rejection and takes no further action.
3. If new Software Engineer disagrees with the rejection, they may request a one-time review from the next level up the escalation chain (Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director) rather than repeatedly resubmitting the same request.
4. For a detected duplicate, MK-CodeForge flags the second entry automatically; the new Software Engineer or Tech Lead confirms which one is authoritative and closes the other as 'Duplicate — see [original ID]'.
5. If the duplicate had already been independently approved and actioned twice (e.g., a purchase made twice), the Tech Lead initiates the standard reversal process instead of just closing the record.
6. MK-CodeForge retains both records for audit purposes even after closure, with the duplicate clearly cross-referenced to the original.

## Responsible Role
new Software Engineer

## Approval
Tech Lead

## Escalation
Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

## Expected Result
Rejections always carry a documented reason and a clear next step for new Software Engineer, and duplicates are caught and reconciled before they cause double-processing.

---
_This edge-case procedure is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._