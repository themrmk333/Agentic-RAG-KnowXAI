# Software Engineering / Development — Rich Historical Ticket Archive (calib, Page 1)

## TCK3-ENG-00020 — Release Management (P3, Closed)
**Created:** 2024-06-20 via Portal  |  **Requester:** Varun Kapoor  |  **Assigned to:** Riya Pillai

**Description:** Varun Kapoor (Data & Analytics) reported an issue via Portal related to 'Feature Flag Rollout Procedure'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Flag Rollout Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ENG-015 to resolve. the Software Engineer confirms eligibility and prerequisites: the target user percentage and success metrics to monitor. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Flag is required. The Product Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Flag in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-015

---

## TCK3-ENG-00003 — Onboarding (P3, Resolved)
**Created:** 2024-06-30 via Email  |  **Requester:** Anjali Verma  |  **Assigned to:** Nisha Kapoor

**Description:** Anjali Verma (Sales) reported an issue via Email related to 'Engineering Onboarding Procedure'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-ENG-012 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the Engineering Manager prepares the required Engineering Onboarding Plan, including repository access, MK-CodeForge SSH keys, and assigning an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Tech Lead verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-012

---

## TCK3-ENG-00005 — Security (P4, Resolved)
**Created:** 2024-07-01 via Slack  |  **Requester:** Sneha Singh  |  **Assigned to:** Rahul Pillai

**Description:** Sneha Singh (Procurement / Purchasing) reported an issue via Slack related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ENG-006 to resolve. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00015 — Version Control (P4, In Progress)
**Created:** 2024-07-23 via Live Chat  |  **Requester:** Manoj Desai  |  **Assigned to:** Simran Desai

**Description:** Manoj Desai (Finance & Accounting) reported an issue via Live Chat related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00008 — Release Management (P3, Resolved)
**Created:** 2024-10-16 via Phone  |  **Requester:** Varun Nair  |  **Assigned to:** Rohan Mehta

**Description:** Varun Nair (IT Support / Information Technology) reported an issue via Phone related to 'Code Freeze Procedure'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Freeze Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including listing all open PRs targeting the release branch. The review team examines the Release Branch against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-010

---

## TCK3-ENG-00001 — Data Management (P3, Resolved)
**Created:** 2024-11-02 via Portal  |  **Requester:** Manoj Desai  |  **Assigned to:** Yash Bose

**Description:** Manoj Desai (Finance & Accounting) reported an issue via Portal related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00012 — Incident Management (P3, Resolved)
**Created:** 2024-11-17 via Portal  |  **Requester:** Divya Gupta  |  **Assigned to:** Rahul Pillai

**Description:** Divya Gupta (QA / Testing) reported an issue via Portal related to 'Production Incident Response (Engineering)'. Category: Incident Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Production Incident Response (Engineering)', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-ENG-013 to resolve. the on-call Software Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the on-call Software Engineer performs the standard first-line check: checking MK-CloudOps dashboards and recent deployments for correlation. If the issue persists, the on-call Software Engineer applies the documented workaround for this issue type. the on-call Software Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call Software Engineer raises a ticket in MK-CodeForge categorised under 'Production Incident', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-ENG-013

---

## TCK3-ENG-00009 — Onboarding (P3, Closed)
**Created:** 2024-11-22 via Email  |  **Requester:** Naveen Singh  |  **Assigned to:** Riya Pillai

**Description:** Naveen Singh (Human Resources) reported an issue via Email related to 'Local Development Environment Setup'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Local Development Environment Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-005 to resolve. the new Software Engineer confirms eligibility and prerequisites: cloning the onboarding repo and running the setup script documented in MK-CodeForge. the new Software Engineer raises a request in MK-CodeForge specifying exactly which Dev Environment is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dev Environment in the relevant system. the new Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-005

---

## TCK3-ENG-00014 — Data Management (P4, Resolved)
**Created:** 2024-11-23 via Portal  |  **Requester:** Sneha Sharma  |  **Assigned to:** Karan Kapoor

**Description:** Sneha Sharma (Research & Development) reported an issue via Portal related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00018 — Security (P4, Closed)
**Created:** 2024-12-26 via Phone  |  **Requester:** Sahil Chowdhury  |  **Assigned to:** Nisha Kapoor

**Description:** Sahil Chowdhury (Legal & Compliance) reported an issue via Phone related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-006 to resolve. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00010 — Onboarding (P3, Resolved)
**Created:** 2025-01-29 via Portal  |  **Requester:** Dev Mehta  |  **Assigned to:** Yash Mehta

**Description:** Dev Mehta (Sales) reported an issue via Portal related to 'Local Development Environment Setup'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Local Development Environment Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-005 to resolve. the new Software Engineer confirms eligibility and prerequisites: cloning the onboarding repo and running the setup script documented in MK-CodeForge. the new Software Engineer raises a request in MK-CodeForge specifying exactly which Dev Environment is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dev Environment in the relevant system. the new Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-005

---

## TCK3-ENG-00002 — Code Quality (P3, Resolved)
**Created:** 2025-02-06 via Live Chat  |  **Requester:** Naveen Bose  |  **Assigned to:** Yash Bose

**Description:** Naveen Bose (Project Management / PMO) reported an issue via Live Chat related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00016 — Release Management (P4, Resolved)
**Created:** 2025-10-07 via Email  |  **Requester:** Bhavna Kapoor  |  **Assigned to:** Rohan Mehta

**Description:** Bhavna Kapoor (DevOps & Cloud) reported an issue via Email related to 'Production Hotfix Deployment'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Production Hotfix Deployment', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-ENG-004 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section. the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-004

---

## TCK3-ENG-00011 — Dependency Management (P3, Closed)
**Created:** 2025-11-13 via Slack  |  **Requester:** Manoj Singh  |  **Assigned to:** Anjali Kapoor

**Description:** Manoj Singh (Product Management) reported an issue via Slack related to 'Third-Party Library Approval'. Category: Dependency Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Third-Party Library Approval', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-ENG-008 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-008

---

## TCK3-ENG-00007 — Version Control (P3, Resolved)
**Created:** 2025-12-07 via Slack  |  **Requester:** Tanya Sharma  |  **Assigned to:** Karan Kapoor

**Description:** Tanya Sharma (Customer Support / Helpdesk) reported an issue via Slack related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00006 — Security (P3, Resolved)
**Created:** 2025-12-26 via Walk-in  |  **Requester:** Aman Bhatt  |  **Assigned to:** Preeti Verma

**Description:** Aman Bhatt (Marketing) reported an issue via Walk-in related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-006 to resolve. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00004 — Code Quality (P3, Resolved)
**Created:** 2026-04-08 via Portal  |  **Requester:** Aditya Desai  |  **Assigned to:** Neel Sharma

**Description:** Aditya Desai (Management / Leadership) reported an issue via Portal related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00013 — Version Control (P3, Resolved)
**Created:** 2026-05-08 via Email  |  **Requester:** Gaurav Malhotra  |  **Assigned to:** Preeti Verma

**Description:** Gaurav Malhotra (Procurement / Purchasing) reported an issue via Email related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00019 — Offboarding (P2, In Progress)
**Created:** 2026-05-10 via Walk-in  |  **Requester:** Aditya Verma  |  **Assigned to:** Yash Bose

**Description:** Aditya Verma (Administration / Facilities) reported an issue via Walk-in related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00017 — Data Management (P4, Closed)
**Created:** 2026-06-01 via Phone  |  **Requester:** Meera Pillai  |  **Assigned to:** Gaurav Agarwal

**Description:** Meera Pillai (Research & Development) reported an issue via Phone related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---
