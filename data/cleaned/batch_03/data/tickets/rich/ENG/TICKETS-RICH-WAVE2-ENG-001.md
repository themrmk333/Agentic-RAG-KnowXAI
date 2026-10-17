# Software Engineering / Development — Rich Historical Ticket Archive (wave2, Page 1)

## TCK3-ENG-00141 — Version Control (P3, Closed)
**Created:** 2024-06-01 via Phone  |  **Requester:** Nisha Desai  |  **Assigned to:** Gaurav Agarwal

**Description:** Nisha Desai (Project Management / PMO) reported an issue via Phone related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00142 — Dependency Management (P3, Resolved)
**Created:** 2024-06-04 via Live Chat  |  **Requester:** Vivek Singh  |  **Assigned to:** Dev Pillai

**Description:** Vivek Singh (Procurement / Purchasing) reported an issue via Live Chat related to 'Third-Party Library Approval'. Category: Dependency Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Third-Party Library Approval', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-ENG-008 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-008

---

## TCK3-ENG-00120 — Onboarding (P3, Resolved)
**Created:** 2024-06-09 via Phone  |  **Requester:** Dev Menon  |  **Assigned to:** Neel Sharma

**Description:** Dev Menon (Research & Development) reported an issue via Phone related to 'Local Development Environment Setup'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Local Development Environment Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-005 to resolve. the new Software Engineer confirms eligibility and prerequisites: cloning the onboarding repo and running the setup script documented in MK-CodeForge. the new Software Engineer raises a request in MK-CodeForge specifying exactly which Dev Environment is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dev Environment in the relevant system. the new Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-005

---

## TCK3-ENG-00149 — Code Quality (P3, Resolved)
**Created:** 2024-06-11 via Walk-in  |  **Requester:** Siddharth Iyer  |  **Assigned to:** Anjali Kapoor

**Description:** Siddharth Iyer (Management / Leadership) reported an issue via Walk-in related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00151 — Onboarding (P4, Resolved)
**Created:** 2024-06-24 via Email  |  **Requester:** Naveen Verma  |  **Assigned to:** Rohan Mehta

**Description:** Naveen Verma (Finance & Accounting) reported an issue via Email related to 'Engineering Onboarding Procedure'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-ENG-012 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the Engineering Manager prepares the required Engineering Onboarding Plan, including repository access, MK-CodeForge SSH keys, and assigning an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Tech Lead verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-012

---

## TCK3-ENG-00085 — Version Control (P4, Resolved)
**Created:** 2024-07-08 via Portal  |  **Requester:** Rohan Singh  |  **Assigned to:** Yash Bose

**Description:** Rohan Singh (Marketing) reported an issue via Portal related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00063 — Onboarding (P1, Resolved)
**Created:** 2024-07-24 via Live Chat  |  **Requester:** Varun Chowdhury  |  **Assigned to:** Tanya Singh

**Description:** Varun Chowdhury (Sales) reported an issue via Live Chat related to 'Engineering Onboarding Procedure'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-ENG-012 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the Engineering Manager prepares the required Engineering Onboarding Plan, including repository access, MK-CodeForge SSH keys, and assigning an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Tech Lead verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-012

---

## TCK3-ENG-00055 — Release Management (P2, Resolved)
**Created:** 2024-07-26 via Live Chat  |  **Requester:** Divya Menon  |  **Assigned to:** Dev Pillai

**Description:** Divya Menon (QA / Testing) reported an issue via Live Chat related to 'Production Hotfix Deployment'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Production Hotfix Deployment', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-ENG-004 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section. the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-004

---

## TCK3-ENG-00042 — Dependency Management (P4, Resolved)
**Created:** 2024-07-28 via Slack  |  **Requester:** Vivek Joshi  |  **Assigned to:** Preeti Verma

**Description:** Vivek Joshi (Project Management / PMO) reported an issue via Slack related to 'Third-Party Library Approval'. Category: Dependency Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Third-Party Library Approval', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-ENG-008 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-008

---

## TCK3-ENG-00039 — Security (P3, Resolved)
**Created:** 2024-08-02 via Slack  |  **Requester:** Divya Rao  |  **Assigned to:** Riya Pillai

**Description:** Divya Rao (Management / Leadership) reported an issue via Slack related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-006 to resolve. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00036 — Data Management (P3, Resolved)
**Created:** 2024-08-04 via Live Chat  |  **Requester:** Swati Sharma  |  **Assigned to:** Riya Pillai

**Description:** Swati Sharma (QA / Testing) reported an issue via Live Chat related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00047 — Data Management (P4, Resolved)
**Created:** 2024-08-09 via Email  |  **Requester:** Preeti Kapoor  |  **Assigned to:** Dev Pillai

**Description:** Preeti Kapoor (Marketing) reported an issue via Email related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00117 — Release Management (P3, In Progress)
**Created:** 2024-08-11 via Walk-in  |  **Requester:** Ananya Nair  |  **Assigned to:** Tanya Singh

**Description:** Ananya Nair (Cybersecurity / Information Security) reported an issue via Walk-in related to 'Feature Flag Rollout Procedure'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Flag Rollout Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-015

---

## TCK3-ENG-00069 — Onboarding (P4, Closed)
**Created:** 2024-08-22 via Live Chat  |  **Requester:** Aman Chauhan  |  **Assigned to:** Yash Mehta

**Description:** Aman Chauhan (Sales) reported an issue via Live Chat related to 'Engineering Onboarding Procedure'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-ENG-012 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the Engineering Manager prepares the required Engineering Onboarding Plan, including repository access, MK-CodeForge SSH keys, and assigning an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Tech Lead verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-012

---

## TCK3-ENG-00086 — Agile Process (P3, Resolved)
**Created:** 2024-08-27 via Slack  |  **Requester:** Neel Menon  |  **Assigned to:** Tanya Singh

**Description:** Neel Menon (IT Support / Information Technology) reported an issue via Slack related to 'Sprint Planning Procedure'. Category: Agile Process. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Sprint Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-ENG-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item. The review team examines the Sprint Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-009

---

## TCK3-ENG-00147 — Version Control (P3, Resolved)
**Created:** 2024-09-05 via Walk-in  |  **Requester:** Kabir Iyer  |  **Assigned to:** Neel Sharma

**Description:** Kabir Iyer (Legal & Compliance) reported an issue via Walk-in related to 'Feature Branch Creation and Naming'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Branch Creation and Naming', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ENG-001 to resolve. the Software Engineer confirms eligibility and prerequisites: the JIRA-equivalent MK-PMTrack ticket ID and a short kebab-case description. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Branch is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Branch in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-001

---

## TCK3-ENG-00084 — Security (P4, Resolved)
**Created:** 2024-09-14 via Email  |  **Requester:** Pooja Menon  |  **Assigned to:** Yash Bose

**Description:** Pooja Menon (Marketing) reported an issue via Email related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-006 to resolve. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00049 — Quality (P2, Resolved)
**Created:** 2024-09-20 via Email  |  **Requester:** Yash Sharma  |  **Assigned to:** Dev Pillai

**Description:** Yash Sharma (Administration / Facilities) reported an issue via Email related to 'Bug Triage and Assignment'. Category: Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Bug Triage and Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-ENG-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including severity, reproducibility, and affected module for each open bug. The review team examines the Bug Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-007

---

## TCK3-ENG-00114 — Quality (P3, Closed)
**Created:** 2024-10-17 via Email  |  **Requester:** Tanya Mehta  |  **Assigned to:** Karan Kapoor

**Description:** Tanya Mehta (Project Management / PMO) reported an issue via Email related to 'Bug Triage and Assignment'. Category: Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Bug Triage and Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-ENG-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including severity, reproducibility, and affected module for each open bug. The review team examines the Bug Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-007

---

## TCK3-ENG-00053 — Agile Process (P3, Resolved)
**Created:** 2024-10-19 via Walk-in  |  **Requester:** Neel Malhotra  |  **Assigned to:** Rahul Pillai

**Description:** Neel Malhotra (Cybersecurity / Information Security) reported an issue via Walk-in related to 'Sprint Planning Procedure'. Category: Agile Process. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Sprint Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-ENG-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item. The review team examines the Sprint Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-009

---