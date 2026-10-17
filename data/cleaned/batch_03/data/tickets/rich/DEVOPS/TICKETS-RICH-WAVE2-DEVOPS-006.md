# DevOps & Cloud — Rich Historical Ticket Archive (wave2, Page 6)

## TCK3-DEVOPS-00040 — Deployment (P4, In Progress)
**Created:** 2026-02-23 via Portal  |  **Requester:** Kabir Reddy  |  **Assigned to:** Preeti Malhotra

**Description:** Kabir Reddy (QA / Testing) reported an issue via Portal related to 'Rollback Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Rollback Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-012

---

## TCK3-DEVOPS-00126 — Operations (P3, Resolved)
**Created:** 2026-02-24 via Slack  |  **Requester:** Sneha Singh  |  **Assigned to:** Isha Desai

**Description:** Sneha Singh (Customer Support / Helpdesk) reported an issue via Slack related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00120 — Infrastructure (P4, Resolved)
**Created:** 2026-02-26 via Walk-in  |  **Requester:** Alisha Pillai  |  **Assigned to:** Priya Rao

**Description:** Alisha Pillai (Cybersecurity / Information Security) reported an issue via Walk-in related to 'Infrastructure as Code (IaC) Change Procedure'. Category: Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Infrastructure as Code (IaC) Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply. The review team examines the IaC Change against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-005

---

## TCK3-DEVOPS-00090 — Release Management (P4, Resolved)
**Created:** 2026-03-04 via Portal  |  **Requester:** Tanya Iyer  |  **Assigned to:** Preeti Malhotra

**Description:** Tanya Iyer (Data & Analytics) reported an issue via Portal related to 'Environment Promotion Procedure (Dev → Staging → Prod)'. Category: Release Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Environment Promotion Procedure (Dev → Staging → Prod)', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-DEVOPS-011 to resolve. the DevOps Engineer logs into MK-CloudOps and navigates to the 'Promotion Request' section. the DevOps Engineer selects 'New Promotion Request' and enters the required details, including staging sign-off evidence and change ticket reference. the DevOps Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the DevOps Engineer submits the Promotion Request; MK-CloudOps automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-011

---

## TCK3-DEVOPS-00123 — Disaster Recovery (P3, Resolved)
**Created:** 2026-03-11 via Email  |  **Requester:** Vikram Mehta  |  **Assigned to:** Isha Desai

**Description:** Vikram Mehta (DevOps & Cloud) reported an issue via Email related to 'Backup and Disaster Recovery Test'. Category: Disaster Recovery. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Backup and Disaster Recovery Test', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Site Reliability Engineer gathers the required data and documents, including restoring a sample backup to a sandbox environment and validating integrity. The review team examines the DR Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-007

---

## TCK3-DEVOPS-00086 — Onboarding (P3, Resolved)
**Created:** 2026-03-21 via Slack  |  **Requester:** Manoj Mehta  |  **Assigned to:** Priya Rao

**Description:** Manoj Mehta (Product Management) reported an issue via Slack related to 'DevOps New Engineer Onboarding'. Category: Onboarding. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'DevOps New Engineer Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-DEVOPS-014 to resolve. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The DevOps Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DEVOPS-014

---

## TCK3-DEVOPS-00109 — Cloud Infrastructure (P3, Resolved)
**Created:** 2026-03-25 via Portal  |  **Requester:** Yash Malhotra  |  **Assigned to:** Riya Chauhan

**Description:** Yash Malhotra (Management / Leadership) reported an issue via Portal related to 'Auto-scaling Configuration Procedure'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Auto-scaling Configuration Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-006 to resolve. the DevOps Engineer confirms eligibility and prerequisites: target CPU/memory thresholds and min/max instance counts. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Auto-scaling Policy is required. The Cloud Architect reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Auto-scaling Policy in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-006

---

## TCK3-DEVOPS-00151 — Incident Management (P3, Resolved)
**Created:** 2026-03-26 via Slack  |  **Requester:** Divya Malhotra  |  **Assigned to:** Bhavna Kapoor

**Description:** Divya Malhotra (Customer Support / Helpdesk) reported an issue via Slack related to 'Production Incident Response (DevOps)'. Category: Incident Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Production Incident Response (DevOps)', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-DEVOPS-004 to resolve. the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the on-call DevOps Engineer performs the standard first-line check: checking MK-CloudOps monitoring dashboards for alerts and anomalies. If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type. the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Infrastructure Incident', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-004

---

## TCK3-DEVOPS-00073 — Incident Management (P4, Resolved)
**Created:** 2026-04-01 via Slack  |  **Requester:** Aman Verma  |  **Assigned to:** Isha Desai

**Description:** Aman Verma (Research & Development) reported an issue via Slack related to 'Production Incident Response (DevOps)'. Category: Incident Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Production Incident Response (DevOps)', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-DEVOPS-004 to resolve. the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the on-call DevOps Engineer performs the standard first-line check: checking MK-CloudOps monitoring dashboards for alerts and anomalies. If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type. the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Infrastructure Incident', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-004

---

## TCK3-DEVOPS-00030 — Disaster Recovery (P4, Resolved)
**Created:** 2026-04-14 via Email  |  **Requester:** Anjali Verma  |  **Assigned to:** Neel Joshi

**Description:** Anjali Verma (Sales) reported an issue via Email related to 'Backup and Disaster Recovery Test'. Category: Disaster Recovery. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Backup and Disaster Recovery Test', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-DEVOPS-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Site Reliability Engineer gathers the required data and documents, including restoring a sample backup to a sandbox environment and validating integrity. The review team examines the DR Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-007

---

## TCK3-DEVOPS-00116 — Infrastructure (P3, Closed)
**Created:** 2026-04-14 via Phone  |  **Requester:** Dev Sharma  |  **Assigned to:** Aditya Rao

**Description:** Dev Sharma (Product Management) reported an issue via Phone related to 'Infrastructure as Code (IaC) Change Procedure'. Category: Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Infrastructure as Code (IaC) Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-DEVOPS-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply. The review team examines the IaC Change against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-005

---

## TCK3-DEVOPS-00093 — Security (P3, Resolved)
**Created:** 2026-04-19 via Walk-in  |  **Requester:** Kabir Agarwal  |  **Assigned to:** Rahul Menon

**Description:** Kabir Agarwal (IT Support / Information Technology) reported an issue via Walk-in related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00065 — Deployment (P3, Resolved)
**Created:** 2026-04-25 via Portal  |  **Requester:** Vikram Bhatt  |  **Assigned to:** Bhavna Kapoor

**Description:** Vikram Bhatt (Human Resources) reported an issue via Portal related to 'Rollback Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Rollback Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-DEVOPS-012 to resolve. the DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the DevOps Engineer performs the standard first-line check: identifying the last known good deployment version in MK-CloudOps. If the issue persists, the DevOps Engineer applies the documented workaround for this issue type. the DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Deployment Rollback', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-012

---

## TCK3-DEVOPS-00128 — Cloud Infrastructure (P3, Resolved)
**Created:** 2026-04-27 via Email  |  **Requester:** Gaurav Malhotra  |  **Assigned to:** Aditya Rao

**Description:** Gaurav Malhotra (Procurement / Purchasing) reported an issue via Email related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00041 — Onboarding (P3, Resolved)
**Created:** 2026-04-29 via Live Chat  |  **Requester:** Rohan Singh  |  **Assigned to:** Vikram Mehta

**Description:** Rohan Singh (Sales) reported an issue via Live Chat related to 'DevOps New Engineer Onboarding'. Category: Onboarding. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'DevOps New Engineer Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-DEVOPS-014 to resolve. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The DevOps Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DEVOPS-014

---

## TCK3-DEVOPS-00048 — Containers (P3, Closed)
**Created:** 2026-04-30 via Slack  |  **Requester:** Rahul Nair  |  **Assigned to:** Siddharth Mehta

**Description:** Rahul Nair (Administration / Facilities) reported an issue via Slack related to 'Container Image Build and Publish'. Category: Containers. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Container Image Build and Publish', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-010 to resolve. the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Container Image in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-010

---

## TCK3-DEVOPS-00080 — Deployment (P4, In Progress)
**Created:** 2026-05-08 via Walk-in  |  **Requester:** Priya Bhatt  |  **Assigned to:** Meera Joshi

**Description:** Priya Bhatt (Human Resources) reported an issue via Walk-in related to 'Rollback Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Rollback Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-012

---

## TCK3-DEVOPS-00129 — Security (P3, Resolved)
**Created:** 2026-05-09 via Phone  |  **Requester:** Siddharth Singh  |  **Assigned to:** Bhavna Kapoor

**Description:** Siddharth Singh (Procurement / Purchasing) reported an issue via Phone related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00066 — Security (P3, Closed)
**Created:** 2026-05-20 via Portal  |  **Requester:** Neel Joshi  |  **Assigned to:** Gaurav Menon

**Description:** Neel Joshi (DevOps & Cloud) reported an issue via Portal related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00054 — Cloud Infrastructure (P3, Closed)
**Created:** 2026-06-03 via Portal  |  **Requester:** Riya Desai  |  **Assigned to:** Aditya Rao

**Description:** Riya Desai (Procurement / Purchasing) reported an issue via Portal related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---