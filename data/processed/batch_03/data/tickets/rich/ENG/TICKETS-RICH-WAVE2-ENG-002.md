# Software Engineering / Development — Rich Historical Ticket Archive (wave2, Page 2)

## TCK3-ENG-00033 — Version Control (P3, Resolved)
**Created:** 2024-10-20 via Walk-in  |  **Requester:** Shreya Kapoor  |  **Assigned to:** Rahul Pillai

**Description:** Shreya Kapoor (Cybersecurity / Information Security) reported an issue via Walk-in related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00067 — Release Management (P3, Resolved)
**Created:** 2024-10-30 via Walk-in  |  **Requester:** Tanya Singh  |  **Assigned to:** Tanya Singh

**Description:** Tanya Singh (Software Engineering / Development) reported an issue via Walk-in related to 'Production Hotfix Deployment'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Production Hotfix Deployment', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-ENG-004 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section. the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-004

---

## TCK3-ENG-00024 — Data Management (P1, Resolved)
**Created:** 2024-11-01 via Slack  |  **Requester:** Simran Desai  |  **Assigned to:** Tanya Singh

**Description:** Simran Desai (Software Engineering / Development) reported an issue via Slack related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00118 — Offboarding (P3, Resolved)
**Created:** 2024-11-13 via Slack  |  **Requester:** Ananya Menon  |  **Assigned to:** Rahul Pillai

**Description:** Ananya Menon (Human Resources) reported an issue via Slack related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-ENG-016 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the departing Software Engineer prepares the required Knowledge Handover, including documenting owned services, open PRs, and pending on-call responsibilities. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Engineering Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00091 — Dependency Management (P3, Resolved)
**Created:** 2024-11-20 via Email  |  **Requester:** Sneha Reddy  |  **Assigned to:** Gaurav Agarwal

**Description:** Sneha Reddy (QA / Testing) reported an issue via Email related to 'Third-Party Library Approval'. Category: Dependency Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Third-Party Library Approval', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-ENG-008 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-008

---

## TCK3-ENG-00064 — Version Control (P4, Resolved)
**Created:** 2024-11-30 via Slack  |  **Requester:** Kabir Reddy  |  **Assigned to:** Neel Sharma

**Description:** Kabir Reddy (QA / Testing) reported an issue via Slack related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00066 — Onboarding (P3, Resolved)
**Created:** 2024-11-30 via Slack  |  **Requester:** Sneha Singh  |  **Assigned to:** Gaurav Agarwal

**Description:** Sneha Singh (Customer Support / Helpdesk) reported an issue via Slack related to 'Local Development Environment Setup'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Local Development Environment Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ENG-005 to resolve. the new Software Engineer confirms eligibility and prerequisites: cloning the onboarding repo and running the setup script documented in MK-CodeForge. the new Software Engineer raises a request in MK-CodeForge specifying exactly which Dev Environment is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dev Environment in the relevant system. the new Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-005

---

## TCK3-ENG-00075 — Version Control (P3, Resolved)
**Created:** 2024-12-03 via Email  |  **Requester:** Meera Joshi  |  **Assigned to:** Yash Bose

**Description:** Meera Joshi (DevOps & Cloud) reported an issue via Email related to 'Feature Branch Creation and Naming'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Branch Creation and Naming', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ENG-001 to resolve. the Software Engineer confirms eligibility and prerequisites: the JIRA-equivalent MK-PMTrack ticket ID and a short kebab-case description. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Branch is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Branch in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-001

---

## TCK3-ENG-00023 — Code Quality (P4, Closed)
**Created:** 2024-12-05 via Portal  |  **Requester:** Shreya Bhatt  |  **Assigned to:** Yash Bose

**Description:** Shreya Bhatt (Administration / Facilities) reported an issue via Portal related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00099 — Onboarding (P3, Resolved)
**Created:** 2024-12-07 via Live Chat  |  **Requester:** Neel Malhotra  |  **Assigned to:** Neel Joshi

**Description:** Neel Malhotra (Cybersecurity / Information Security) reported an issue via Live Chat related to 'Local Development Environment Setup'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Local Development Environment Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-005 to resolve. the new Software Engineer confirms eligibility and prerequisites: cloning the onboarding repo and running the setup script documented in MK-CodeForge. the new Software Engineer raises a request in MK-CodeForge specifying exactly which Dev Environment is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dev Environment in the relevant system. the new Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-005

---

## TCK3-ENG-00146 — Data Management (P3, In Progress)
**Created:** 2024-12-10 via Slack  |  **Requester:** Naveen Verma  |  **Assigned to:** Karan Kapoor

**Description:** Naveen Verma (Finance & Accounting) reported an issue via Slack related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00030 — Code Quality (P3, Resolved)
**Created:** 2024-12-11 via Live Chat  |  **Requester:** Simran Kapoor  |  **Assigned to:** Yash Mehta

**Description:** Simran Kapoor (Product Management) reported an issue via Live Chat related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00107 — Version Control (P1, Resolved)
**Created:** 2024-12-12 via Portal  |  **Requester:** Neel Agarwal  |  **Assigned to:** Gaurav Agarwal

**Description:** Neel Agarwal (Research & Development) reported an issue via Portal related to 'Feature Branch Creation and Naming'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Branch Creation and Naming', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-001 to resolve. the Software Engineer confirms eligibility and prerequisites: the JIRA-equivalent MK-PMTrack ticket ID and a short kebab-case description. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Branch is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Branch in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-001

---

## TCK3-ENG-00088 — Data Management (P3, Resolved)
**Created:** 2024-12-17 via Email  |  **Requester:** Divya Joshi  |  **Assigned to:** Rohan Mehta

**Description:** Divya Joshi (Finance & Accounting) reported an issue via Email related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00094 — Agile Process (P2, Closed)
**Created:** 2024-12-18 via Walk-in  |  **Requester:** Gaurav Sharma  |  **Assigned to:** Anjali Kapoor

**Description:** Gaurav Sharma (IT Support / Information Technology) reported an issue via Walk-in related to 'Sprint Planning Procedure'. Category: Agile Process. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Sprint Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-ENG-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item. The review team examines the Sprint Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-009

---

## TCK3-ENG-00051 — Release Management (P3, Closed)
**Created:** 2024-12-19 via Email  |  **Requester:** Naveen Kapoor  |  **Assigned to:** Yash Mehta

**Description:** Naveen Kapoor (Project Management / PMO) reported an issue via Email related to 'Feature Flag Rollout Procedure'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Flag Rollout Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-015 to resolve. the Software Engineer confirms eligibility and prerequisites: the target user percentage and success metrics to monitor. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Flag is required. The Product Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Flag in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-015

---

## TCK3-ENG-00083 — Security (P2, Resolved)
**Created:** 2025-01-01 via Slack  |  **Requester:** Yash Bose  |  **Assigned to:** Riya Pillai

**Description:** Yash Bose (Software Engineering / Development) reported an issue via Slack related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-006 to resolve. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00034 — Offboarding (P3, Resolved)
**Created:** 2025-01-04 via Live Chat  |  **Requester:** Aditya Joshi  |  **Assigned to:** Gaurav Agarwal

**Description:** Aditya Joshi (Research & Development) reported an issue via Live Chat related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-ENG-016 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the departing Software Engineer prepares the required Knowledge Handover, including documenting owned services, open PRs, and pending on-call responsibilities. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Engineering Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00046 — Offboarding (P2, Resolved)
**Created:** 2025-01-08 via Email  |  **Requester:** Divya Menon  |  **Assigned to:** Yash Bose

**Description:** Divya Menon (QA / Testing) reported an issue via Email related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-ENG-016 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the departing Software Engineer prepares the required Knowledge Handover, including documenting owned services, open PRs, and pending on-call responsibilities. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Engineering Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00125 — Offboarding (P4, In Progress)
**Created:** 2025-01-14 via Portal  |  **Requester:** Vikram Malhotra  |  **Assigned to:** Tanya Singh

**Description:** Vikram Malhotra (QA / Testing) reported an issue via Portal related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---
