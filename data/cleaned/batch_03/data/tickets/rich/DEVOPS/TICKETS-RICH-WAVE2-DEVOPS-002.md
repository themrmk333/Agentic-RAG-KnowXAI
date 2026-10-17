# DevOps & Cloud — Rich Historical Ticket Archive (wave2, Page 2)

## TCK3-DEVOPS-00149 — Observability (P4, Resolved)
**Created:** 2024-10-06 via Phone  |  **Requester:** Meera Chowdhury  |  **Assigned to:** Riya Chauhan

**Description:** Meera Chowdhury (Project Management / PMO) reported an issue via Phone related to 'Monitoring and Alerting Setup'. Category: Observability. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Monitoring and Alerting Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-009 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining alert thresholds and the on-call notification channel. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Monitoring Alert is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Monitoring Alert in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-009

---

## TCK3-DEVOPS-00099 — Patch Management (P3, Resolved)
**Created:** 2024-10-23 via Email  |  **Requester:** Aditya Menon  |  **Assigned to:** Riya Chauhan

**Description:** Aditya Menon (IT Support / Information Technology) reported an issue via Email related to 'Patch Management for Infrastructure'. Category: Patch Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Patch Management for Infrastructure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DEVOPS-015 to resolve. the DevOps Engineer confirms eligibility and prerequisites: testing the patch in staging before production rollout. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Patch Deployment is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Patch Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-015

---

## TCK3-DEVOPS-00033 — Cloud Infrastructure (P2, Resolved)
**Created:** 2024-11-02 via Portal  |  **Requester:** Divya Chowdhury  |  **Assigned to:** Aditya Rao

**Description:** Divya Chowdhury (Human Resources) reported an issue via Portal related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00105 — Disaster Recovery (P2, Resolved)
**Created:** 2024-11-07 via Email  |  **Requester:** Aditya Chauhan  |  **Assigned to:** Bhavna Kapoor

**Description:** Aditya Chauhan (Administration / Facilities) reported an issue via Email related to 'Backup and Disaster Recovery Test'. Category: Disaster Recovery. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Backup and Disaster Recovery Test', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-DEVOPS-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Site Reliability Engineer gathers the required data and documents, including restoring a sample backup to a sandbox environment and validating integrity. The review team examines the DR Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-007

---

## TCK3-DEVOPS-00102 — Security (P3, Resolved)
**Created:** 2024-11-08 via Portal  |  **Requester:** Kabir Chauhan  |  **Assigned to:** Preeti Malhotra

**Description:** Kabir Chauhan (Sales) reported an issue via Portal related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00055 — Operations (P2, Resolved)
**Created:** 2024-11-19 via Email  |  **Requester:** Yash Bose  |  **Assigned to:** Siddharth Mehta

**Description:** Yash Bose (Software Engineering / Development) reported an issue via Email related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00134 — Operations (P2, Resolved)
**Created:** 2024-11-28 via Walk-in  |  **Requester:** Neel Joshi  |  **Assigned to:** Aman Menon

**Description:** Neel Joshi (DevOps & Cloud) reported an issue via Walk-in related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00124 — Disaster Recovery (P4, Closed)
**Created:** 2024-12-06 via Portal  |  **Requester:** Yash Sharma  |  **Assigned to:** Bhavna Kapoor

**Description:** Yash Sharma (Administration / Facilities) reported an issue via Portal related to 'Backup and Disaster Recovery Test'. Category: Disaster Recovery. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Backup and Disaster Recovery Test', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DEVOPS-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Site Reliability Engineer gathers the required data and documents, including restoring a sample backup to a sandbox environment and validating integrity. The review team examines the DR Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-007

---

## TCK3-DEVOPS-00097 — Deployment (P3, Closed)
**Created:** 2024-12-16 via Walk-in  |  **Requester:** Sneha Verma  |  **Assigned to:** Aditya Rao

**Description:** Sneha Verma (Product Management) reported an issue via Walk-in related to 'Service Deployment Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Service Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-001 to resolve. the DevOps Engineer confirms eligibility and prerequisites: verifying the build passed all MK-CI pipeline gates. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Deployment is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-001

---

## TCK3-DEVOPS-00081 — Cloud Infrastructure (P3, Resolved)
**Created:** 2024-12-19 via Slack  |  **Requester:** Siddharth Mehta  |  **Assigned to:** Aman Menon

**Description:** Siddharth Mehta (DevOps & Cloud) reported an issue via Slack related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00029 — Onboarding (P3, Resolved)
**Created:** 2024-12-20 via Slack  |  **Requester:** Preeti Reddy  |  **Assigned to:** Vikram Mehta

**Description:** Preeti Reddy (Management / Leadership) reported an issue via Slack related to 'DevOps New Engineer Onboarding'. Category: Onboarding. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'DevOps New Engineer Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-DEVOPS-014 to resolve. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The DevOps Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DEVOPS-014

---

## TCK3-DEVOPS-00024 — Cloud Infrastructure (P2, Resolved)
**Created:** 2024-12-22 via Email  |  **Requester:** Rohan Singh  |  **Assigned to:** Riya Chauhan

**Description:** Rohan Singh (Marketing) reported an issue via Email related to 'Auto-scaling Configuration Procedure'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Auto-scaling Configuration Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-006 to resolve. the DevOps Engineer confirms eligibility and prerequisites: target CPU/memory thresholds and min/max instance counts. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Auto-scaling Policy is required. The Cloud Architect reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Auto-scaling Policy in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-006

---

## TCK3-DEVOPS-00131 — Deployment (P4, Resolved)
**Created:** 2024-12-22 via Walk-in  |  **Requester:** Nisha Kapoor  |  **Assigned to:** Preeti Malhotra

**Description:** Nisha Kapoor (Software Engineering / Development) reported an issue via Walk-in related to 'Rollback Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Rollback Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-DEVOPS-012 to resolve. the DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the DevOps Engineer performs the standard first-line check: identifying the last known good deployment version in MK-CloudOps. If the issue persists, the DevOps Engineer applies the documented workaround for this issue type. the DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Deployment Rollback', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-012

---

## TCK3-DEVOPS-00038 — CI/CD (P4, In Progress)
**Created:** 2025-01-02 via Email  |  **Requester:** Divya Rao  |  **Assigned to:** Isha Desai

**Description:** Divya Rao (Management / Leadership) reported an issue via Email related to 'CI/CD Pipeline Configuration'. Category: CI/CD. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'CI/CD Pipeline Configuration', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-002

---

## TCK3-DEVOPS-00045 — Patch Management (P2, Resolved)
**Created:** 2025-01-03 via Slack  |  **Requester:** Kavya Desai  |  **Assigned to:** Isha Desai

**Description:** Kavya Desai (Customer Support / Helpdesk) reported an issue via Slack related to 'Patch Management for Infrastructure'. Category: Patch Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Patch Management for Infrastructure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-015 to resolve. the DevOps Engineer confirms eligibility and prerequisites: testing the patch in staging before production rollout. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Patch Deployment is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Patch Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-015

---

## TCK3-DEVOPS-00058 — Observability (P3, Resolved)
**Created:** 2025-01-08 via Portal  |  **Requester:** Kabir Nair  |  **Assigned to:** Karan Bhatt

**Description:** Kabir Nair (Administration / Facilities) reported an issue via Portal related to 'Monitoring and Alerting Setup'. Category: Observability. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Monitoring and Alerting Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DEVOPS-009 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining alert thresholds and the on-call notification channel. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Monitoring Alert is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Monitoring Alert in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-009

---

## TCK3-DEVOPS-00061 — Security (P4, Resolved)
**Created:** 2025-01-09 via Live Chat  |  **Requester:** Yash Iyer  |  **Assigned to:** Gaurav Menon

**Description:** Yash Iyer (Research & Development) reported an issue via Live Chat related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00069 — Incident Management (P3, Resolved)
**Created:** 2025-01-10 via Walk-in  |  **Requester:** Divya Chowdhury  |  **Assigned to:** Meera Joshi

**Description:** Divya Chowdhury (Human Resources) reported an issue via Walk-in related to 'Production Incident Response (DevOps)'. Category: Incident Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Production Incident Response (DevOps)', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-DEVOPS-004 to resolve. the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the on-call DevOps Engineer performs the standard first-line check: checking MK-CloudOps monitoring dashboards for alerts and anomalies. If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type. the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Infrastructure Incident', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-004

---

## TCK3-DEVOPS-00074 — Observability (P3, Resolved)
**Created:** 2025-01-10 via Live Chat  |  **Requester:** Nidhi Malhotra  |  **Assigned to:** Ananya Bose

**Description:** Nidhi Malhotra (Sales) reported an issue via Live Chat related to 'Monitoring and Alerting Setup'. Category: Observability. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Monitoring and Alerting Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-009 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining alert thresholds and the on-call notification channel. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Monitoring Alert is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Monitoring Alert in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-009

---

## TCK3-DEVOPS-00111 — Cost Management (P3, Closed)
**Created:** 2025-01-10 via Walk-in  |  **Requester:** Aditya Verma  |  **Assigned to:** Aditya Rao

**Description:** Aditya Verma (Administration / Facilities) reported an issue via Walk-in related to 'Cost Optimization Review'. Category: Cost Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cost Optimization Review', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DEVOPS-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Cloud Architect gathers the required data and documents, including idle resources, oversized instances, and unused storage. The review team examines the Cloud Cost Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-013

---