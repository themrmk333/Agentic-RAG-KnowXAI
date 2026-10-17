# DevOps & Cloud — Rich Historical Ticket Archive (wave2, Page 7)

## TCK3-DEVOPS-00127 — Operations (P1, Closed)
**Created:** 2026-06-07 via Live Chat  |  **Requester:** Siddharth Joshi  |  **Assigned to:** Karan Bhatt

**Description:** Siddharth Joshi (Cybersecurity / Information Security) reported an issue via Live Chat related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00079 — Patch Management (P3, In Progress)
**Created:** 2026-07-03 via Email  |  **Requester:** Anjali Gupta  |  **Assigned to:** Gaurav Menon

**Description:** Anjali Gupta (Legal & Compliance) reported an issue via Email related to 'Patch Management for Infrastructure'. Category: Patch Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Patch Management for Infrastructure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-015

---

## TCK3-DEVOPS-00084 — Onboarding (P3, Resolved)
**Created:** 2026-07-10 via Live Chat  |  **Requester:** Kavya Nair  |  **Assigned to:** Siddharth Mehta

**Description:** Kavya Nair (Finance & Accounting) reported an issue via Live Chat related to 'DevOps New Engineer Onboarding'. Category: Onboarding. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'DevOps New Engineer Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-DEVOPS-014 to resolve. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The DevOps Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DEVOPS-014

---

## TCK3-DEVOPS-00022 — Deployment (P3, Resolved)
**Created:** 2026-07-11 via Portal  |  **Requester:** Swati Nair  |  **Assigned to:** Isha Desai

**Description:** Swati Nair (Customer Support / Helpdesk) reported an issue via Portal related to 'Service Deployment Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Service Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DEVOPS-001 to resolve. the DevOps Engineer confirms eligibility and prerequisites: verifying the build passed all MK-CI pipeline gates. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Deployment is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-001

---

## TCK3-DEVOPS-00071 — Security (P3, Closed)
**Created:** 2026-07-14 via Phone  |  **Requester:** Nisha Bose  |  **Assigned to:** Siddharth Mehta

**Description:** Nisha Bose (Customer Support / Helpdesk) reported an issue via Phone related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00140 — Infrastructure (P2, Resolved)
**Created:** 2026-07-26 via Live Chat  |  **Requester:** Nisha Desai  |  **Assigned to:** Ananya Bose

**Description:** Nisha Desai (Project Management / PMO) reported an issue via Live Chat related to 'Infrastructure as Code (IaC) Change Procedure'. Category: Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Infrastructure as Code (IaC) Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply. The review team examines the IaC Change against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-005

---

## TCK3-DEVOPS-00043 — Cost Management (P3, Resolved)
**Created:** 2026-07-27 via Slack  |  **Requester:** Swati Sharma  |  **Assigned to:** Siddharth Mehta

**Description:** Swati Sharma (QA / Testing) reported an issue via Slack related to 'Cost Optimization Review'. Category: Cost Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cost Optimization Review', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-DEVOPS-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Cloud Architect gathers the required data and documents, including idle resources, oversized instances, and unused storage. The review team examines the Cloud Cost Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-013

---

## TCK3-DEVOPS-00143 — Cost Management (P4, Resolved)
**Created:** 2026-08-01 via Portal  |  **Requester:** Simran Iyer  |  **Assigned to:** Ananya Bose

**Description:** Simran Iyer (Project Management / PMO) reported an issue via Portal related to 'Cost Optimization Review'. Category: Cost Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cost Optimization Review', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DEVOPS-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Cloud Architect gathers the required data and documents, including idle resources, oversized instances, and unused storage. The review team examines the Cloud Cost Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-013

---

## TCK3-DEVOPS-00092 — Cost Management (P4, Resolved)
**Created:** 2026-08-06 via Phone  |  **Requester:** Sneha Singh  |  **Assigned to:** Meera Joshi

**Description:** Sneha Singh (Procurement / Purchasing) reported an issue via Phone related to 'Cost Optimization Review'. Category: Cost Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cost Optimization Review', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Cloud Architect gathers the required data and documents, including idle resources, oversized instances, and unused storage. The review team examines the Cloud Cost Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-013

---

## TCK3-DEVOPS-00121 — Containers (P3, Closed)
**Created:** 2026-08-14 via Phone  |  **Requester:** Aditya Menon  |  **Assigned to:** Aman Menon

**Description:** Aditya Menon (IT Support / Information Technology) reported an issue via Phone related to 'Container Image Build and Publish'. Category: Containers. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Container Image Build and Publish', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-010 to resolve. the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Container Image in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-010

---

## TCK3-DEVOPS-00139 — CI/CD (P2, Resolved)
**Created:** 2026-08-14 via Email  |  **Requester:** Ananya Pillai  |  **Assigned to:** Aman Menon

**Description:** Ananya Pillai (Research & Development) reported an issue via Email related to 'CI/CD Pipeline Configuration'. Category: CI/CD. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'CI/CD Pipeline Configuration', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-002 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining build, test, and deploy stages with required approvals. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which CI/CD Pipeline is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the CI/CD Pipeline in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-002

---
