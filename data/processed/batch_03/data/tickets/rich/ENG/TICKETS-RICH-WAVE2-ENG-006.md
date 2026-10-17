# Software Engineering / Development — Rich Historical Ticket Archive (wave2, Page 6)

## TCK3-ENG-00029 — Security (P4, In Progress)
**Created:** 2025-12-26 via Email  |  **Requester:** Naveen Verma  |  **Assigned to:** Yash Bose

**Description:** Naveen Verma (Finance & Accounting) reported an issue via Email related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00061 — Agile Process (P4, Resolved)
**Created:** 2025-12-28 via Slack  |  **Requester:** Divya Rao  |  **Assigned to:** Neel Sharma

**Description:** Divya Rao (Management / Leadership) reported an issue via Slack related to 'Sprint Planning Procedure'. Category: Agile Process. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Sprint Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-ENG-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item. The review team examines the Sprint Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-009

---

## TCK3-ENG-00112 — Quality (P3, Resolved)
**Created:** 2026-01-07 via Slack  |  **Requester:** Vivek Gupta  |  **Assigned to:** Riya Pillai

**Description:** Vivek Gupta (Sales) reported an issue via Slack related to 'Bug Triage and Assignment'. Category: Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Bug Triage and Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-ENG-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including severity, reproducibility, and affected module for each open bug. The review team examines the Bug Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-007

---

## TCK3-ENG-00090 — Onboarding (P3, Resolved)
**Created:** 2026-02-16 via Phone  |  **Requester:** Vikram Mehta  |  **Assigned to:** Yash Mehta

**Description:** Vikram Mehta (DevOps & Cloud) reported an issue via Phone related to 'Engineering Onboarding Procedure'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-ENG-012 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the Engineering Manager prepares the required Engineering Onboarding Plan, including repository access, MK-CodeForge SSH keys, and assigning an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Tech Lead verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-012

---

## TCK3-ENG-00074 — Dependency Management (P3, Closed)
**Created:** 2026-03-11 via Walk-in  |  **Requester:** Karan Bhatt  |  **Assigned to:** Dev Pillai

**Description:** Karan Bhatt (DevOps & Cloud) reported an issue via Walk-in related to 'Third-Party Library Approval'. Category: Dependency Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Third-Party Library Approval', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-ENG-008 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-008

---

## TCK3-ENG-00143 — Code Quality (P4, Resolved)
**Created:** 2026-03-15 via Portal  |  **Requester:** Kavya Iyer  |  **Assigned to:** Yash Bose

**Description:** Kavya Iyer (Finance & Accounting) reported an issue via Portal related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00081 — Security (P3, In Progress)
**Created:** 2026-03-23 via Slack  |  **Requester:** Kabir Iyer  |  **Assigned to:** Neel Joshi

**Description:** Kabir Iyer (Legal & Compliance) reported an issue via Slack related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00050 — Security (P3, Resolved)
**Created:** 2026-03-29 via Walk-in  |  **Requester:** Rohan Desai  |  **Assigned to:** Nisha Kapoor

**Description:** Rohan Desai (Sales) reported an issue via Walk-in related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-006 to resolve. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00092 — Quality (P3, Resolved)
**Created:** 2026-03-31 via Email  |  **Requester:** Shreya Kapoor  |  **Assigned to:** Neel Sharma

**Description:** Shreya Kapoor (Cybersecurity / Information Security) reported an issue via Email related to 'Bug Triage and Assignment'. Category: Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Bug Triage and Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including severity, reproducibility, and affected module for each open bug. The review team examines the Bug Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-007

---

## TCK3-ENG-00060 — Quality (P4, Resolved)
**Created:** 2026-04-08 via Phone  |  **Requester:** Gaurav Agarwal  |  **Assigned to:** Nisha Kapoor

**Description:** Gaurav Agarwal (Software Engineering / Development) reported an issue via Phone related to 'Bug Triage and Assignment'. Category: Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Bug Triage and Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-ENG-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including severity, reproducibility, and affected module for each open bug. The review team examines the Bug Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-007

---

## TCK3-ENG-00080 — Architecture (P3, Resolved)
**Created:** 2026-04-10 via Slack  |  **Requester:** Varun Nair  |  **Assigned to:** Anjali Kapoor

**Description:** Varun Nair (IT Support / Information Technology) reported an issue via Slack related to 'Technical Design Document Review'. Category: Architecture. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Technical Design Document Review', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-ENG-011 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including architecture diagrams, data flow, and rollback/monitoring plan. The review team examines the Design Document against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-011

---

## TCK3-ENG-00057 — Release Management (P3, Closed)
**Created:** 2026-04-21 via Walk-in  |  **Requester:** Rahul Menon  |  **Assigned to:** Nisha Kapoor

**Description:** Rahul Menon (DevOps & Cloud) reported an issue via Walk-in related to 'Production Hotfix Deployment'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Production Hotfix Deployment', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-ENG-004 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section. the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-004

---

## TCK3-ENG-00048 — Dependency Management (P3, Resolved)
**Created:** 2026-04-22 via Slack  |  **Requester:** Siddharth Rao  |  **Assigned to:** Gaurav Agarwal

**Description:** Siddharth Rao (Finance & Accounting) reported an issue via Slack related to 'Third-Party Library Approval'. Category: Dependency Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Third-Party Library Approval', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-ENG-008 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-008

---

## TCK3-ENG-00134 — Code Quality (P3, Resolved)
**Created:** 2026-05-04 via Phone  |  **Requester:** Rahul Singh  |  **Assigned to:** Yash Mehta

**Description:** Rahul Singh (Legal & Compliance) reported an issue via Phone related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-ENG-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description. The review team examines the Pull Request against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00031 — Onboarding (P3, Resolved)
**Created:** 2026-05-12 via Slack  |  **Requester:** Riya Chauhan  |  **Assigned to:** Riya Pillai

**Description:** Riya Chauhan (DevOps & Cloud) reported an issue via Slack related to 'Local Development Environment Setup'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Local Development Environment Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-005 to resolve. the new Software Engineer confirms eligibility and prerequisites: cloning the onboarding repo and running the setup script documented in MK-CodeForge. the new Software Engineer raises a request in MK-CodeForge specifying exactly which Dev Environment is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dev Environment in the relevant system. the new Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-005

---

## TCK3-ENG-00110 — Release Management (P3, Resolved)
**Created:** 2026-05-18 via Email  |  **Requester:** Ananya Gupta  |  **Assigned to:** Yash Bose

**Description:** Ananya Gupta (Product Management) reported an issue via Email related to 'Code Freeze Procedure'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Freeze Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-ENG-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including listing all open PRs targeting the release branch. The review team examines the Release Branch against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-010

---

## TCK3-ENG-00040 — Release Management (P4, Resolved)
**Created:** 2026-05-22 via Slack  |  **Requester:** Vikram Iyer  |  **Assigned to:** Preeti Verma

**Description:** Vikram Iyer (Management / Leadership) reported an issue via Slack related to 'Production Hotfix Deployment'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Production Hotfix Deployment', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-ENG-004 to resolve. the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section. the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ENG-004

---

## TCK3-ENG-00079 — Onboarding (P3, Resolved)
**Created:** 2026-05-27 via Portal  |  **Requester:** Neel Joshi  |  **Assigned to:** Gaurav Agarwal

**Description:** Neel Joshi (Software Engineering / Development) reported an issue via Portal related to 'Local Development Environment Setup'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Local Development Environment Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-005 to resolve. the new Software Engineer confirms eligibility and prerequisites: cloning the onboarding repo and running the setup script documented in MK-CodeForge. the new Software Engineer raises a request in MK-CodeForge specifying exactly which Dev Environment is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dev Environment in the relevant system. the new Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-005

---

## TCK3-ENG-00119 — Offboarding (P3, In Progress)
**Created:** 2026-05-31 via Walk-in  |  **Requester:** Ananya Pillai  |  **Assigned to:** Neel Sharma

**Description:** Ananya Pillai (Research & Development) reported an issue via Walk-in related to 'Engineering Exit Handover'. Category: Offboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Exit Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-016

---

## TCK3-ENG-00054 — Release Management (P3, Closed)
**Created:** 2026-06-01 via Email  |  **Requester:** Gaurav Agarwal  |  **Assigned to:** Dev Pillai

**Description:** Gaurav Agarwal (Software Engineering / Development) reported an issue via Email related to 'Feature Flag Rollout Procedure'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Feature Flag Rollout Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-015 to resolve. the Software Engineer confirms eligibility and prerequisites: the target user percentage and success metrics to monitor. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Flag is required. The Product Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Feature Flag in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-015

---
