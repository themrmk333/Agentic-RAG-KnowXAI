# Software Engineering / Development — Rich Historical Ticket Archive (wave2, Page 7)

## TCK3-ENG-00105 — Release Management (P3, Resolved)
**Created:** 2026-06-17 via Slack  |  **Requester:** Simran Desai  |  **Assigned to:** Simran Desai

**Description:** Simran Desai (Software Engineering / Development) reported an issue via Slack related to 'Production Hotfix Deployment'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Production Hotfix Deployment', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-ENG-004 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section. the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-004

---

## TCK3-ENG-00056 — Version Control (P3, Resolved)
**Created:** 2026-06-25 via Slack  |  **Requester:** Divya Gupta  |  **Assigned to:** Rahul Pillai

**Description:** Divya Gupta (QA / Testing) reported an issue via Slack related to 'Feature Branch Creation and Naming'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Branch Creation and Naming', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ENG-001 to resolve. the Software Engineer confirms eligibility and prerequisites: the JIRA-equivalent MK-PMTrack ticket ID and a short kebab-case description. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Branch is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Branch in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-001

---

## TCK3-ENG-00038 — Dependency Management (P3, Resolved)
**Created:** 2026-07-03 via Portal  |  **Requester:** Rohan Singh  |  **Assigned to:** Nisha Kapoor

**Description:** Rohan Singh (Marketing) reported an issue via Portal related to 'Third-Party Library Approval'. Category: Dependency Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Third-Party Library Approval', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-ENG-008 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-008

---

## TCK3-ENG-00101 — Dependency Management (P4, Resolved)
**Created:** 2026-07-04 via Phone  |  **Requester:** Kavya Bhatt  |  **Assigned to:** Rahul Pillai

**Description:** Kavya Bhatt (Procurement / Purchasing) reported an issue via Phone related to 'Third-Party Library Approval'. Category: Dependency Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Third-Party Library Approval', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-ENG-008 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-008

---

## TCK3-ENG-00104 — Release Management (P2, Resolved)
**Created:** 2026-07-05 via Walk-in  |  **Requester:** Shreya Iyer  |  **Assigned to:** Riya Pillai

**Description:** Shreya Iyer (Administration / Facilities) reported an issue via Walk-in related to 'Code Freeze Procedure'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Freeze Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including listing all open PRs targeting the release branch. The review team examines the Release Branch against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-010

---

## TCK3-ENG-00076 — Release Management (P3, Resolved)
**Created:** 2026-07-22 via Portal  |  **Requester:** Isha Desai  |  **Assigned to:** Riya Pillai

**Description:** Isha Desai (DevOps & Cloud) reported an issue via Portal related to 'Production Hotfix Deployment'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Production Hotfix Deployment', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-ENG-004 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section. the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-004

---

## TCK3-ENG-00052 — Agile Process (P4, Resolved)
**Created:** 2026-07-26 via Live Chat  |  **Requester:** Shreya Chauhan  |  **Assigned to:** Riya Pillai

**Description:** Shreya Chauhan (Management / Leadership) reported an issue via Live Chat related to 'Sprint Planning Procedure'. Category: Agile Process. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Sprint Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item. The review team examines the Sprint Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-009

---

## TCK3-ENG-00065 — Release Management (P3, Resolved)
**Created:** 2026-07-29 via Email  |  **Requester:** Divya Chowdhury  |  **Assigned to:** Simran Desai

**Description:** Divya Chowdhury (Human Resources) reported an issue via Email related to 'Feature Flag Rollout Procedure'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Flag Rollout Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-015 to resolve. the Software Engineer confirms eligibility and prerequisites: the target user percentage and success metrics to monitor. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Flag is required. The Product Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Flag in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-015

---

## TCK3-ENG-00037 — Data Management (P4, Resolved)
**Created:** 2026-08-01 via Walk-in  |  **Requester:** Naveen Bose  |  **Assigned to:** Yash Bose

**Description:** Naveen Bose (Project Management / PMO) reported an issue via Walk-in related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00145 — Code Quality (P2, Resolved)
**Created:** 2026-08-11 via Live Chat  |  **Requester:** Arjun Verma  |  **Assigned to:** Simran Desai

**Description:** Arjun Verma (Administration / Facilities) reported an issue via Live Chat related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00043 — Code Quality (P2, Resolved)
**Created:** 2026-08-17 via Walk-in  |  **Requester:** Aman Pillai  |  **Assigned to:** Dev Pillai

**Description:** Aman Pillai (Data & Analytics) reported an issue via Walk-in related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---
