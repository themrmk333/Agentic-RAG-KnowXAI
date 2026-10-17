# DevOps & Cloud — Rich Historical Ticket Archive (wave2, Page 4)

## TCK3-DEVOPS-00044 — Incident Management (P2, Resolved)
**Created:** 2025-05-20 via Phone  |  **Requester:** Bhavna Pillai  |  **Assigned to:** Aman Menon

**Description:** Bhavna Pillai (Sales) reported an issue via Phone related to 'Production Incident Response (DevOps)'. Category: Incident Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Production Incident Response (DevOps)', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-DEVOPS-004 to resolve. the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the on-call DevOps Engineer performs the standard first-line check: checking MK-CloudOps monitoring dashboards for alerts and anomalies. If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type. the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Infrastructure Incident', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-004

---

## TCK3-DEVOPS-00023 — Security (P3, Resolved)
**Created:** 2025-05-22 via Portal  |  **Requester:** Nidhi Malhotra  |  **Assigned to:** Meera Joshi

**Description:** Nidhi Malhotra (Sales) reported an issue via Portal related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00096 — Onboarding (P1, Resolved)
**Created:** 2025-05-22 via Walk-in  |  **Requester:** Rahul Pillai  |  **Assigned to:** Bhavna Kapoor

**Description:** Rahul Pillai (Software Engineering / Development) reported an issue via Walk-in related to 'DevOps New Engineer Onboarding'. Category: Onboarding. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'DevOps New Engineer Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-DEVOPS-014 to resolve. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The DevOps Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DEVOPS-014

---

## TCK3-DEVOPS-00117 — Security (P4, Resolved)
**Created:** 2025-06-01 via Portal  |  **Requester:** Neel Menon  |  **Assigned to:** Ananya Bose

**Description:** Neel Menon (IT Support / Information Technology) reported an issue via Portal related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00141 — Patch Management (P4, Resolved)
**Created:** 2025-06-09 via Walk-in  |  **Requester:** Divya Joshi  |  **Assigned to:** Priya Rao

**Description:** Divya Joshi (Finance & Accounting) reported an issue via Walk-in related to 'Patch Management for Infrastructure'. Category: Patch Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Patch Management for Infrastructure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-015 to resolve. the DevOps Engineer confirms eligibility and prerequisites: testing the patch in staging before production rollout. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Patch Deployment is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Patch Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-015

---

## TCK3-DEVOPS-00142 — Infrastructure (P4, Resolved)
**Created:** 2025-06-12 via Phone  |  **Requester:** Neel Menon  |  **Assigned to:** Isha Desai

**Description:** Neel Menon (IT Support / Information Technology) reported an issue via Phone related to 'Infrastructure as Code (IaC) Change Procedure'. Category: Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Infrastructure as Code (IaC) Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-DEVOPS-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply. The review team examines the IaC Change against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-005

---

## TCK3-DEVOPS-00082 — Incident Management (P3, Resolved)
**Created:** 2025-06-29 via Walk-in  |  **Requester:** Rahul Nair  |  **Assigned to:** Rahul Menon

**Description:** Rahul Nair (Administration / Facilities) reported an issue via Walk-in related to 'Production Incident Response (DevOps)'. Category: Incident Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Production Incident Response (DevOps)', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-DEVOPS-004 to resolve. the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the on-call DevOps Engineer performs the standard first-line check: checking MK-CloudOps monitoring dashboards for alerts and anomalies. If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type. the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Infrastructure Incident', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-004

---

## TCK3-DEVOPS-00083 — CI/CD (P4, Resolved)
**Created:** 2025-06-30 via Email  |  **Requester:** Rahul Pillai  |  **Assigned to:** Riya Chauhan

**Description:** Rahul Pillai (Software Engineering / Development) reported an issue via Email related to 'CI/CD Pipeline Configuration'. Category: CI/CD. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'CI/CD Pipeline Configuration', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DEVOPS-002 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining build, test, and deploy stages with required approvals. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which CI/CD Pipeline is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the CI/CD Pipeline in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-002

---

## TCK3-DEVOPS-00032 — Security (P3, Resolved)
**Created:** 2025-07-02 via Slack  |  **Requester:** Rahul Nair  |  **Assigned to:** Aman Menon

**Description:** Rahul Nair (Administration / Facilities) reported an issue via Slack related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00101 — Cost Management (P4, Resolved)
**Created:** 2025-07-03 via Phone  |  **Requester:** Yash Iyer  |  **Assigned to:** Aditya Rao

**Description:** Yash Iyer (Research & Development) reported an issue via Phone related to 'Cost Optimization Review'. Category: Cost Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cost Optimization Review', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Cloud Architect gathers the required data and documents, including idle resources, oversized instances, and unused storage. The review team examines the Cloud Cost Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-013

---

## TCK3-DEVOPS-00094 — Security (P3, Closed)
**Created:** 2025-07-07 via Slack  |  **Requester:** Dev Chauhan  |  **Assigned to:** Siddharth Mehta

**Description:** Dev Chauhan (Marketing) reported an issue via Slack related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00098 — Deployment (P3, In Progress)
**Created:** 2025-08-08 via Portal  |  **Requester:** Ananya Nair  |  **Assigned to:** Vivek Sharma

**Description:** Ananya Nair (IT Support / Information Technology) reported an issue via Portal related to 'Rollback Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Rollback Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-012

---

## TCK3-DEVOPS-00107 — Infrastructure (P3, Closed)
**Created:** 2025-08-10 via Walk-in  |  **Requester:** Rohan Sharma  |  **Assigned to:** Riya Chauhan

**Description:** Rohan Sharma (Project Management / PMO) reported an issue via Walk-in related to 'Infrastructure as Code (IaC) Change Procedure'. Category: Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Infrastructure as Code (IaC) Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply. The review team examines the IaC Change against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-005

---

## TCK3-DEVOPS-00037 — Patch Management (P3, Closed)
**Created:** 2025-08-15 via Slack  |  **Requester:** Ananya Bose  |  **Assigned to:** Bhavna Kapoor

**Description:** Ananya Bose (DevOps & Cloud) reported an issue via Slack related to 'Patch Management for Infrastructure'. Category: Patch Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Patch Management for Infrastructure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-015 to resolve. the DevOps Engineer confirms eligibility and prerequisites: testing the patch in staging before production rollout. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Patch Deployment is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Patch Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-015

---

## TCK3-DEVOPS-00052 — Disaster Recovery (P3, Resolved)
**Created:** 2025-08-19 via Email  |  **Requester:** Simran Malhotra  |  **Assigned to:** Ananya Bose

**Description:** Simran Malhotra (Finance & Accounting) reported an issue via Email related to 'Backup and Disaster Recovery Test'. Category: Disaster Recovery. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Backup and Disaster Recovery Test', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DEVOPS-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Site Reliability Engineer gathers the required data and documents, including restoring a sample backup to a sandbox environment and validating integrity. The review team examines the DR Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-007

---

## TCK3-DEVOPS-00150 — Deployment (P2, Resolved)
**Created:** 2025-08-27 via Live Chat  |  **Requester:** Swati Sharma  |  **Assigned to:** Neel Joshi

**Description:** Swati Sharma (QA / Testing) reported an issue via Live Chat related to 'Service Deployment Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Service Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-001 to resolve. the DevOps Engineer confirms eligibility and prerequisites: verifying the build passed all MK-CI pipeline gates. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Deployment is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-001

---

## TCK3-DEVOPS-00144 — Onboarding (P4, Resolved)
**Created:** 2025-09-01 via Phone  |  **Requester:** Ananya Menon  |  **Assigned to:** Gaurav Menon

**Description:** Ananya Menon (Human Resources) reported an issue via Phone related to 'DevOps New Engineer Onboarding'. Category: Onboarding. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'DevOps New Engineer Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-DEVOPS-014 to resolve. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The DevOps Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DEVOPS-014

---

## TCK3-DEVOPS-00100 — Operations (P4, Resolved)
**Created:** 2025-09-20 via Walk-in  |  **Requester:** Dev Pillai  |  **Assigned to:** Karan Bhatt

**Description:** Dev Pillai (Software Engineering / Development) reported an issue via Walk-in related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00110 — Containers (P4, Resolved)
**Created:** 2025-09-22 via Phone  |  **Requester:** Manoj Nair  |  **Assigned to:** Karan Bhatt

**Description:** Manoj Nair (QA / Testing) reported an issue via Phone related to 'Container Image Build and Publish'. Category: Containers. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Container Image Build and Publish', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-010 to resolve. the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Container Image in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-010

---

## TCK3-DEVOPS-00064 — Infrastructure (P3, Resolved)
**Created:** 2025-09-25 via Walk-in  |  **Requester:** Arjun Chowdhury  |  **Assigned to:** Vivek Sharma

**Description:** Arjun Chowdhury (Finance & Accounting) reported an issue via Walk-in related to 'Infrastructure as Code (IaC) Change Procedure'. Category: Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Infrastructure as Code (IaC) Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DEVOPS-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply. The review team examines the IaC Change against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-005

---
