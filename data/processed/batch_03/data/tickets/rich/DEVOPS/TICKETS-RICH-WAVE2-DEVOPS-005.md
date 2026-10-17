# DevOps & Cloud — Rich Historical Ticket Archive (wave2, Page 5)

## TCK3-DEVOPS-00136 — Containers (P4, Closed)
**Created:** 2025-10-10 via Email  |  **Requester:** Priya Sharma  |  **Assigned to:** Gaurav Menon

**Description:** Priya Sharma (Data & Analytics) reported an issue via Email related to 'Container Image Build and Publish'. Category: Containers. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Container Image Build and Publish', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-010 to resolve. the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Container Image in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-010

---

## TCK3-DEVOPS-00068 — Operations (P1, Resolved)
**Created:** 2025-10-18 via Slack  |  **Requester:** Swati Nair  |  **Assigned to:** Bhavna Kapoor

**Description:** Swati Nair (Finance & Accounting) reported an issue via Slack related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00095 — Release Management (P2, Resolved)
**Created:** 2025-10-28 via Email  |  **Requester:** Harsh Malhotra  |  **Assigned to:** Vivek Sharma

**Description:** Harsh Malhotra (Procurement / Purchasing) reported an issue via Email related to 'Environment Promotion Procedure (Dev → Staging → Prod)'. Category: Release Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Environment Promotion Procedure (Dev → Staging → Prod)', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DEVOPS-011 to resolve. the DevOps Engineer logs into MK-CloudOps and navigates to the 'Promotion Request' section. the DevOps Engineer selects 'New Promotion Request' and enters the required details, including staging sign-off evidence and change ticket reference. the DevOps Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the DevOps Engineer submits the Promotion Request; MK-CloudOps automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-011

---

## TCK3-DEVOPS-00148 — Cloud Infrastructure (P3, In Progress)
**Created:** 2025-10-29 via Walk-in  |  **Requester:** Isha Iyer  |  **Assigned to:** Riya Chauhan

**Description:** Isha Iyer (Product Management) reported an issue via Walk-in related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00118 — Containers (P4, Closed)
**Created:** 2025-11-19 via Phone  |  **Requester:** Nisha Kapoor  |  **Assigned to:** Gaurav Menon

**Description:** Nisha Kapoor (Software Engineering / Development) reported an issue via Phone related to 'Container Image Build and Publish'. Category: Containers. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Container Image Build and Publish', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-010 to resolve. the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Container Image in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-010

---

## TCK3-DEVOPS-00138 — Cost Management (P2, Resolved)
**Created:** 2025-11-22 via Phone  |  **Requester:** Ananya Nair  |  **Assigned to:** Siddharth Mehta

**Description:** Ananya Nair (IT Support / Information Technology) reported an issue via Phone related to 'Cost Optimization Review'. Category: Cost Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cost Optimization Review', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-DEVOPS-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Cloud Architect gathers the required data and documents, including idle resources, oversized instances, and unused storage. The review team examines the Cloud Cost Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-013

---

## TCK3-DEVOPS-00147 — Observability (P4, Resolved)
**Created:** 2025-12-05 via Live Chat  |  **Requester:** Aditya Nair  |  **Assigned to:** Ananya Bose

**Description:** Aditya Nair (Administration / Facilities) reported an issue via Live Chat related to 'Monitoring and Alerting Setup'. Category: Observability. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Monitoring and Alerting Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-009 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining alert thresholds and the on-call notification channel. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Monitoring Alert is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Monitoring Alert in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-009

---

## TCK3-DEVOPS-00089 — Security (P3, Resolved)
**Created:** 2025-12-06 via Portal  |  **Requester:** Ananya Nair  |  **Assigned to:** Riya Chauhan

**Description:** Ananya Nair (IT Support / Information Technology) reported an issue via Portal related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00053 — CI/CD (P4, Resolved)
**Created:** 2025-12-19 via Live Chat  |  **Requester:** Manoj Chauhan  |  **Assigned to:** Siddharth Mehta

**Description:** Manoj Chauhan (Administration / Facilities) reported an issue via Live Chat related to 'CI/CD Pipeline Configuration'. Category: CI/CD. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'CI/CD Pipeline Configuration', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-002 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining build, test, and deploy stages with required approvals. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which CI/CD Pipeline is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the CI/CD Pipeline in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-002

---

## TCK3-DEVOPS-00057 — Deployment (P4, Resolved)
**Created:** 2025-12-20 via Phone  |  **Requester:** Sahil Bhatt  |  **Assigned to:** Bhavna Kapoor

**Description:** Sahil Bhatt (Project Management / PMO) reported an issue via Phone related to 'Rollback Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Rollback Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-DEVOPS-012 to resolve. the DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the DevOps Engineer performs the standard first-line check: identifying the last known good deployment version in MK-CloudOps. If the issue persists, the DevOps Engineer applies the documented workaround for this issue type. the DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Deployment Rollback', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-012

---

## TCK3-DEVOPS-00042 — Security (P3, Resolved)
**Created:** 2025-12-21 via Phone  |  **Requester:** Varun Reddy  |  **Assigned to:** Rahul Menon

**Description:** Varun Reddy (Product Management) reported an issue via Phone related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00088 — Security (P3, Closed)
**Created:** 2025-12-21 via Email  |  **Requester:** Kabir Agarwal  |  **Assigned to:** Siddharth Mehta

**Description:** Kabir Agarwal (IT Support / Information Technology) reported an issue via Email related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00075 — Deployment (P4, Closed)
**Created:** 2025-12-29 via Email  |  **Requester:** Dev Mehta  |  **Assigned to:** Aman Menon

**Description:** Dev Mehta (Sales) reported an issue via Email related to 'Service Deployment Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Service Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-001 to resolve. the DevOps Engineer confirms eligibility and prerequisites: verifying the build passed all MK-CI pipeline gates. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Deployment is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-001

---

## TCK3-DEVOPS-00039 — Disaster Recovery (P4, Closed)
**Created:** 2026-01-07 via Phone  |  **Requester:** Sneha Kapoor  |  **Assigned to:** Rahul Menon

**Description:** Sneha Kapoor (Data & Analytics) reported an issue via Phone related to 'Backup and Disaster Recovery Test'. Category: Disaster Recovery. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Backup and Disaster Recovery Test', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DEVOPS-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Site Reliability Engineer gathers the required data and documents, including restoring a sample backup to a sandbox environment and validating integrity. The review team examines the DR Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-007

---

## TCK3-DEVOPS-00026 — Onboarding (P4, Resolved)
**Created:** 2026-01-18 via Walk-in  |  **Requester:** Divya Pillai  |  **Assigned to:** Gaurav Menon

**Description:** Divya Pillai (Marketing) reported an issue via Walk-in related to 'DevOps New Engineer Onboarding'. Category: Onboarding. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'DevOps New Engineer Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-DEVOPS-014 to resolve. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The DevOps Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DEVOPS-014

---

## TCK3-DEVOPS-00077 — Operations (P4, Closed)
**Created:** 2026-01-22 via Slack  |  **Requester:** Ananya Desai  |  **Assigned to:** Aman Menon

**Description:** Ananya Desai (Legal & Compliance) reported an issue via Slack related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00115 — Patch Management (P3, Resolved)
**Created:** 2026-01-27 via Walk-in  |  **Requester:** Neel Sharma  |  **Assigned to:** Meera Joshi

**Description:** Neel Sharma (Software Engineering / Development) reported an issue via Walk-in related to 'Patch Management for Infrastructure'. Category: Patch Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Patch Management for Infrastructure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DEVOPS-015 to resolve. the DevOps Engineer confirms eligibility and prerequisites: testing the patch in staging before production rollout. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Patch Deployment is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Patch Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-015

---

## TCK3-DEVOPS-00028 — Deployment (P3, Resolved)
**Created:** 2026-02-07 via Email  |  **Requester:** Anjali Nair  |  **Assigned to:** Riya Chauhan

**Description:** Anjali Nair (Cybersecurity / Information Security) reported an issue via Email related to 'Service Deployment Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Service Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-001 to resolve. the DevOps Engineer confirms eligibility and prerequisites: verifying the build passed all MK-CI pipeline gates. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Deployment is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-001

---

## TCK3-DEVOPS-00067 — Cloud Infrastructure (P3, Resolved)
**Created:** 2026-02-22 via Portal  |  **Requester:** Meera Chauhan  |  **Assigned to:** Aditya Rao

**Description:** Meera Chauhan (Procurement / Purchasing) reported an issue via Portal related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00122 — CI/CD (P3, Closed)
**Created:** 2026-02-22 via Portal  |  **Requester:** Isha Iyer  |  **Assigned to:** Karan Bhatt

**Description:** Isha Iyer (Data & Analytics) reported an issue via Portal related to 'CI/CD Pipeline Configuration'. Category: CI/CD. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'CI/CD Pipeline Configuration', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-002 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining build, test, and deploy stages with required approvals. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which CI/CD Pipeline is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the CI/CD Pipeline in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-002

---
