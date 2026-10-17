# Software Engineering / Development — Rich Historical Ticket Archive (wave2, Page 5)

## TCK3-ENG-00113 — Onboarding (P4, Closed)
**Created:** 2025-08-19 via Live Chat  |  **Requester:** Rahul Bose  |  **Assigned to:** Yash Bose

**Description:** Rahul Bose (Finance & Accounting) reported an issue via Live Chat related to 'Engineering Onboarding Procedure'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-ENG-012 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the Engineering Manager prepares the required Engineering Onboarding Plan, including repository access, MK-CodeForge SSH keys, and assigning an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Tech Lead verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-012

---

## TCK3-ENG-00070 — Data Management (P2, Resolved)
**Created:** 2025-08-25 via Slack  |  **Requester:** Aditya Rao  |  **Assigned to:** Yash Mehta

**Description:** Aditya Rao (DevOps & Cloud) reported an issue via Slack related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00138 — Security (P4, Resolved)
**Created:** 2025-08-28 via Live Chat  |  **Requester:** Arjun Pillai  |  **Assigned to:** Dev Pillai

**Description:** Arjun Pillai (Human Resources) reported an issue via Live Chat related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-006 to resolve. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00072 — Version Control (P3, In Progress)
**Created:** 2025-09-01 via Phone  |  **Requester:** Kavya Reddy  |  **Assigned to:** Nisha Kapoor

**Description:** Kavya Reddy (Finance & Accounting) reported an issue via Phone related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00121 — Onboarding (P4, Closed)
**Created:** 2025-09-02 via Portal  |  **Requester:** Rahul Pillai  |  **Assigned to:** Preeti Verma

**Description:** Rahul Pillai (Software Engineering / Development) reported an issue via Portal related to 'Engineering Onboarding Procedure'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-ENG-012 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the Engineering Manager prepares the required Engineering Onboarding Plan, including repository access, MK-CodeForge SSH keys, and assigning an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Tech Lead verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-012

---

## TCK3-ENG-00095 — Security (P3, Resolved)
**Created:** 2025-09-11 via Live Chat  |  **Requester:** Shreya Nair  |  **Assigned to:** Rahul Pillai

**Description:** Shreya Nair (Project Management / PMO) reported an issue via Live Chat related to 'API Key and Secret Rotation'. Category: Security. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'API Key and Secret Rotation', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-006 to resolve. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-006

---

## TCK3-ENG-00022 — Agile Process (P4, Resolved)
**Created:** 2025-10-11 via Phone  |  **Requester:** Dev Sharma  |  **Assigned to:** Gaurav Agarwal

**Description:** Dev Sharma (Product Management) reported an issue via Phone related to 'Sprint Planning Procedure'. Category: Agile Process. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Sprint Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item. The review team examines the Sprint Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-009

---

## TCK3-ENG-00129 — Version Control (P3, Resolved)
**Created:** 2025-10-18 via Slack  |  **Requester:** Arjun Verma  |  **Assigned to:** Anjali Kapoor

**Description:** Arjun Verma (Administration / Facilities) reported an issue via Slack related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00124 — Architecture (P2, Resolved)
**Created:** 2025-10-21 via Slack  |  **Requester:** Harsh Chauhan  |  **Assigned to:** Yash Mehta

**Description:** Harsh Chauhan (QA / Testing) reported an issue via Slack related to 'Technical Design Document Review'. Category: Architecture. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Technical Design Document Review', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-ENG-011 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including architecture diagrams, data flow, and rollback/monitoring plan. The review team examines the Design Document against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-011

---

## TCK3-ENG-00150 — Quality (P2, Resolved)
**Created:** 2025-10-28 via Slack  |  **Requester:** Aditya Nair  |  **Assigned to:** Tanya Singh

**Description:** Aditya Nair (Administration / Facilities) reported an issue via Slack related to 'Bug Triage and Assignment'. Category: Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Bug Triage and Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including severity, reproducibility, and affected module for each open bug. The review team examines the Bug Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-007

---

## TCK3-ENG-00045 — Architecture (P3, Closed)
**Created:** 2025-10-30 via Phone  |  **Requester:** Varun Reddy  |  **Assigned to:** Neel Sharma

**Description:** Varun Reddy (Product Management) reported an issue via Phone related to 'Technical Design Document Review'. Category: Architecture. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Technical Design Document Review', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-ENG-011 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including architecture diagrams, data flow, and rollback/monitoring plan. The review team examines the Design Document against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-011

---

## TCK3-ENG-00132 — Architecture (P4, Resolved)
**Created:** 2025-11-04 via Live Chat  |  **Requester:** Shreya Iyer  |  **Assigned to:** Karan Kapoor

**Description:** Shreya Iyer (Administration / Facilities) reported an issue via Live Chat related to 'Technical Design Document Review'. Category: Architecture. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Technical Design Document Review', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-011 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including architecture diagrams, data flow, and rollback/monitoring plan. The review team examines the Design Document against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-011

---

## TCK3-ENG-00108 — Onboarding (P2, Closed)
**Created:** 2025-11-17 via Email  |  **Requester:** Swati Nair  |  **Assigned to:** Yash Mehta

**Description:** Swati Nair (Customer Support / Helpdesk) reported an issue via Email related to 'Engineering Onboarding Procedure'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Engineering Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-ENG-012 to resolve. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date. the Engineering Manager prepares the required Engineering Onboarding Plan, including repository access, MK-CodeForge SSH keys, and assigning an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Tech Lead verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-ENG-012

---

## TCK3-ENG-00144 — Onboarding (P4, Resolved)
**Created:** 2025-11-17 via Live Chat  |  **Requester:** Dev Malhotra  |  **Assigned to:** Yash Bose

**Description:** Dev Malhotra (Cybersecurity / Information Security) reported an issue via Live Chat related to 'Local Development Environment Setup'. Category: Onboarding. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Local Development Environment Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ENG-005 to resolve. the new Software Engineer confirms eligibility and prerequisites: cloning the onboarding repo and running the setup script documented in MK-CodeForge. the new Software Engineer raises a request in MK-CodeForge specifying exactly which Dev Environment is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dev Environment in the relevant system. the new Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-005

---

## TCK3-ENG-00115 — Release Management (P4, Resolved)
**Created:** 2025-11-18 via Live Chat  |  **Requester:** Swati Nair  |  **Assigned to:** Gaurav Agarwal

**Description:** Swati Nair (Customer Support / Helpdesk) reported an issue via Live Chat related to 'Code Freeze Procedure'. Category: Release Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Freeze Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-ENG-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including listing all open PRs targeting the release branch. The review team examines the Release Branch against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-010

---

## TCK3-ENG-00032 — Code Quality (P3, In Progress)
**Created:** 2025-12-10 via Phone  |  **Requester:** Alisha Gupta  |  **Assigned to:** Dev Pillai

**Description:** Alisha Gupta (Customer Support / Helpdesk) reported an issue via Phone related to 'Code Review Process'. Category: Code Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Code Review Process', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-002

---

## TCK3-ENG-00103 — Version Control (P3, Closed)
**Created:** 2025-12-16 via Walk-in  |  **Requester:** Karan Pillai  |  **Assigned to:** Neel Joshi

**Description:** Karan Pillai (Product Management) reported an issue via Walk-in related to 'New Repository Setup'. Category: Version Control. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'New Repository Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ENG-003 to resolve. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Repository in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-003

---

## TCK3-ENG-00122 — Architecture (P4, Closed)
**Created:** 2025-12-16 via Live Chat  |  **Requester:** Nisha Kapoor  |  **Assigned to:** Rahul Pillai

**Description:** Nisha Kapoor (Software Engineering / Development) reported an issue via Live Chat related to 'Technical Design Document Review'. Category: Architecture. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Technical Design Document Review', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-ENG-011 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Software Engineer gathers the required data and documents, including architecture diagrams, data flow, and rollback/monitoring plan. The review team examines the Design Document against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-011

---

## TCK3-ENG-00087 — Data Management (P3, Closed)
**Created:** 2025-12-23 via Email  |  **Requester:** Dev Sharma  |  **Assigned to:** Simran Desai

**Description:** Dev Sharma (Product Management) reported an issue via Email related to 'Database Schema Migration'. Category: Data Management. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Database Schema Migration', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ENG-014 to resolve. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system. the Software Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ENG-014

---

## TCK3-ENG-00025 — Quality (P3, Resolved)
**Created:** 2025-12-25 via Slack  |  **Requester:** Ananya Nair  |  **Assigned to:** Karan Kapoor

**Description:** Ananya Nair (Cybersecurity / Information Security) reported an issue via Slack related to 'Bug Triage and Assignment'. Category: Quality. Logged against MK-CodeForge.

**Investigation:** The assigned specialist reviewed the MK-CodeForge record, confirmed the reported symptom against 'Bug Triage and Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-ENG-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CodeForge. the Tech Lead gathers the required data and documents, including severity, reproducibility, and affected module for each open bug. The review team examines the Bug Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ENG-007

---