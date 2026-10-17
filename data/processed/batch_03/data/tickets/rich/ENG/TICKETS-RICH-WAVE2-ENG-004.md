# Software Engineering / Development — Rich Historical Ticket Archive (wave2, Page 4)

## TCK3-ENG-00059 — Quality (P3, Resolved)
**Created:** 2025-05-04 via Live Chat  |  **Requester:** Gaurav Sharma  |  **Assigned to:** Neel Sharma

**Description:** Gaurav Sharma (IT Support / Information Technology) reported an issue via Live Chat related to 'Bug Triage and Assignment'. Category: Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Bug Triage and Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-ENG-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including severity, reproducibility, and affected module for each open bug. The review team examines the Bug Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-007

---

## TCK3-ENG-00116 — Version Control (P2, Resolved)
**Created:** 2025-05-07 via Email  |  **Requester:** Siddharth Singh  |  **Assigned to:** Neel Joshi

**Description:** Siddharth Singh (Product Management) reported an issue via Email related to 'Feature Branch Creation and Naming'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Branch Creation and Naming', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ENG-001 to resolve. the Software Engineer confirms eligibility and prerequisites: the JIRA-equivalent MK-PMTrack ticket ID and a short kebab-case description. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Branch is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Branch in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-001

---

## TCK3-ENG-00097 — Agile Process (P4, Closed)
**Created:** 2025-05-12 via Phone  |  **Requester:** Bhavna Rao  |  **Assigned to:** Simran Desai

**Description:** Bhavna Rao (Data & Analytics) reported an issue via Phone related to 'Sprint Planning Procedure'. Category: Agile Process. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Sprint Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-ENG-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item. The review team examines the Sprint Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-009

---

## TCK3-ENG-00148 — Release Management (P3, Closed)
**Created:** 2025-05-16 via Phone  |  **Requester:** Rohan Singh  |  **Assigned to:** Rahul Pillai

**Description:** Rohan Singh (Marketing) reported an issue via Phone related to 'Production Hotfix Deployment'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Production Hotfix Deployment', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-ENG-004 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section. the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-004

---

## TCK3-ENG-00127 — Offboarding (P4, Resolved)
**Created:** 2025-05-18 via Email  |  **Requester:** Nidhi Malhotra  |  **Assigned to:** Neel Joshi

**Description:** Nidhi Malhotra (Sales) reported an issue via Email related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-ENG-016 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the departing Software Engineer prepares the required Knowledge Handover, including documenting owned services, open PRs, and pending on-call responsibilities. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Engineering Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00058 — Version Control (P2, Closed)
**Created:** 2025-06-03 via Portal  |  **Requester:** Sneha Sharma  |  **Assigned to:** Dev Pillai

**Description:** Sneha Sharma (Research & Development) reported an issue via Portal related to 'Feature Branch Creation and Naming'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Branch Creation and Naming', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-001 to resolve. the Software Engineer confirms eligibility and prerequisites: the JIRA-equivalent MK-PMTrack ticket ID and a short kebab-case description. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Branch is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Branch in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-001

---

## TCK3-ENG-00133 — Offboarding (P4, Closed)
**Created:** 2025-06-11 via Slack  |  **Requester:** Sneha Kapoor  |  **Assigned to:** Yash Bose

**Description:** Sneha Kapoor (Data & Analytics) reported an issue via Slack related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-ENG-016 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the departing Software Engineer prepares the required Knowledge Handover, including documenting owned services, open PRs, and pending on-call responsibilities. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Engineering Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00096 — Code Quality (P3, Resolved)
**Created:** 2025-06-12 via Phone  |  **Requester:** Harsh Pillai  |  **Assigned to:** Neel Sharma

**Description:** Harsh Pillai (Project Management / PMO) reported an issue via Phone related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00130 — Agile Process (P4, Resolved)
**Created:** 2025-06-12 via Email  |  **Requester:** Neel Reddy  |  **Assigned to:** Tanya Singh

**Description:** Neel Reddy (Data & Analytics) reported an issue via Email related to 'Sprint Planning Procedure'. Category: Agile Process. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Sprint Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-ENG-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item. The review team examines the Sprint Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-009

---

## TCK3-ENG-00028 — Offboarding (P4, Resolved)
**Created:** 2025-06-16 via Walk-in  |  **Requester:** Sahil Sharma  |  **Assigned to:** Tanya Singh

**Description:** Sahil Sharma (Sales) reported an issue via Walk-in related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-ENG-016 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the departing Software Engineer prepares the required Knowledge Handover, including documenting owned services, open PRs, and pending on-call responsibilities. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Engineering Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00137 — Data Management (P4, Resolved)
**Created:** 2025-06-17 via Walk-in  |  **Requester:** Shreya Iyer  |  **Assigned to:** Neel Sharma

**Description:** Shreya Iyer (Administration / Facilities) reported an issue via Walk-in related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00073 — Version Control (P3, Resolved)
**Created:** 2025-07-03 via Email  |  **Requester:** Neel Reddy  |  **Assigned to:** Tanya Singh

**Description:** Neel Reddy (Data & Analytics) reported an issue via Email related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00082 — Offboarding (P3, Closed)
**Created:** 2025-07-14 via Phone  |  **Requester:** Rohan Singh  |  **Assigned to:** Gaurav Agarwal

**Description:** Rohan Singh (Sales) reported an issue via Phone related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-ENG-016 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the departing Software Engineer prepares the required Knowledge Handover, including documenting owned services, open PRs, and pending on-call responsibilities. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Engineering Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00102 — Dependency Management (P3, Resolved)
**Created:** 2025-07-23 via Walk-in  |  **Requester:** Harsh Nair  |  **Assigned to:** Tanya Singh

**Description:** Harsh Nair (Cybersecurity / Information Security) reported an issue via Walk-in related to 'Third-Party Library Approval'. Category: Dependency Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Third-Party Library Approval', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-ENG-008 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-008

---

## TCK3-ENG-00111 — Version Control (P1, Resolved)
**Created:** 2025-07-28 via Live Chat  |  **Requester:** Yash Chauhan  |  **Assigned to:** Simran Desai

**Description:** Yash Chauhan (Procurement / Purchasing) reported an issue via Live Chat related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00027 — Agile Process (P3, Resolved)
**Created:** 2025-07-31 via Live Chat  |  **Requester:** Isha Agarwal  |  **Assigned to:** Dev Pillai

**Description:** Isha Agarwal (Human Resources) reported an issue via Live Chat related to 'Sprint Planning Procedure'. Category: Agile Process. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Sprint Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item. The review team examines the Sprint Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-009

---

## TCK3-ENG-00021 — Offboarding (P3, In Progress)
**Created:** 2025-08-03 via Portal  |  **Requester:** Tanya Mehta  |  **Assigned to:** Neel Joshi

**Description:** Tanya Mehta (Human Resources) reported an issue via Portal related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00078 — Data Management (P3, Resolved)
**Created:** 2025-08-03 via Live Chat  |  **Requester:** Priya Bhatt  |  **Assigned to:** Dev Pillai

**Description:** Priya Bhatt (Human Resources) reported an issue via Live Chat related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00131 — Offboarding (P4, Resolved)
**Created:** 2025-08-11 via Portal  |  **Requester:** Isha Iyer  |  **Assigned to:** Gaurav Agarwal

**Description:** Isha Iyer (Product Management) reported an issue via Portal related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-ENG-016 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the departing Software Engineer prepares the required Knowledge Handover, including documenting owned services, open PRs, and pending on-call responsibilities. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Engineering Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00139 — Code Quality (P1, Resolved)
**Created:** 2025-08-18 via Email  |  **Requester:** Kavya Reddy  |  **Assigned to:** Rohan Mehta

**Description:** Kavya Reddy (Finance & Accounting) reported an issue via Email related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---
