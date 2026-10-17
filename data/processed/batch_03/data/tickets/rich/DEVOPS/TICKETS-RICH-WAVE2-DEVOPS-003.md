# DevOps & Cloud — Rich Historical Ticket Archive (wave2, Page 3)

## TCK3-DEVOPS-00114 — Containers (P3, In Progress)
**Created:** 2025-01-11 via Phone  |  **Requester:** Dev Chauhan  |  **Assigned to:** Preeti Malhotra

**Description:** Dev Chauhan (Marketing) reported an issue via Phone related to 'Container Image Build and Publish'. Category: Containers. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Container Image Build and Publish', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-010

---

## TCK3-DEVOPS-00130 — CI/CD (P3, Resolved)
**Created:** 2025-01-20 via Portal  |  **Requester:** Yash Chauhan  |  **Assigned to:** Isha Desai

**Description:** Yash Chauhan (Procurement / Purchasing) reported an issue via Portal related to 'CI/CD Pipeline Configuration'. Category: CI/CD. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'CI/CD Pipeline Configuration', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-002 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining build, test, and deploy stages with required approvals. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which CI/CD Pipeline is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the CI/CD Pipeline in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-002

---

## TCK3-DEVOPS-00021 — Cloud Infrastructure (P4, Resolved)
**Created:** 2025-02-02 via Live Chat  |  **Requester:** Yash Malhotra  |  **Assigned to:** Karan Bhatt

**Description:** Yash Malhotra (Management / Leadership) reported an issue via Live Chat related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00104 — Deployment (P3, Closed)
**Created:** 2025-02-05 via Walk-in  |  **Requester:** Manoj Chauhan  |  **Assigned to:** Priya Rao

**Description:** Manoj Chauhan (Administration / Facilities) reported an issue via Walk-in related to 'Rollback Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Rollback Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-DEVOPS-012 to resolve. the DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the DevOps Engineer performs the standard first-line check: identifying the last known good deployment version in MK-CloudOps. If the issue persists, the DevOps Engineer applies the documented workaround for this issue type. the DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Deployment Rollback', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-012

---

## TCK3-DEVOPS-00119 — Infrastructure (P3, Closed)
**Created:** 2025-02-10 via Email  |  **Requester:** Ananya Bose  |  **Assigned to:** Meera Joshi

**Description:** Ananya Bose (Sales) reported an issue via Email related to 'Infrastructure as Code (IaC) Change Procedure'. Category: Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Infrastructure as Code (IaC) Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply. The review team examines the IaC Change against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-005

---

## TCK3-DEVOPS-00036 — Release Management (P2, Resolved)
**Created:** 2025-03-09 via Slack  |  **Requester:** Alisha Rao  |  **Assigned to:** Bhavna Kapoor

**Description:** Alisha Rao (Finance & Accounting) reported an issue via Slack related to 'Environment Promotion Procedure (Dev → Staging → Prod)'. Category: Release Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Environment Promotion Procedure (Dev → Staging → Prod)', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-DEVOPS-011 to resolve. the DevOps Engineer logs into MK-CloudOps and navigates to the 'Promotion Request' section. the DevOps Engineer selects 'New Promotion Request' and enters the required details, including staging sign-off evidence and change ticket reference. the DevOps Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the DevOps Engineer submits the Promotion Request; MK-CloudOps automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-011

---

## TCK3-DEVOPS-00049 — Incident Management (P4, Resolved)
**Created:** 2025-03-17 via Email  |  **Requester:** Rohan Singh  |  **Assigned to:** Priya Rao

**Description:** Rohan Singh (Marketing) reported an issue via Email related to 'Production Incident Response (DevOps)'. Category: Incident Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Production Incident Response (DevOps)', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-DEVOPS-004 to resolve. the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the on-call DevOps Engineer performs the standard first-line check: checking MK-CloudOps monitoring dashboards for alerts and anomalies. If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type. the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Infrastructure Incident', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-004

---

## TCK3-DEVOPS-00108 — Onboarding (P2, Resolved)
**Created:** 2025-03-25 via Portal  |  **Requester:** Alisha Verma  |  **Assigned to:** Ananya Bose

**Description:** Alisha Verma (QA / Testing) reported an issue via Portal related to 'DevOps New Engineer Onboarding'. Category: Onboarding. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'DevOps New Engineer Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-DEVOPS-014 to resolve. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The DevOps Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DEVOPS-014

---

## TCK3-DEVOPS-00047 — Containers (P3, Resolved)
**Created:** 2025-03-28 via Portal  |  **Requester:** Riya Desai  |  **Assigned to:** Riya Chauhan

**Description:** Riya Desai (Procurement / Purchasing) reported an issue via Portal related to 'Container Image Build and Publish'. Category: Containers. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Container Image Build and Publish', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-010 to resolve. the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Container Image in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-010

---

## TCK3-DEVOPS-00146 — Security (P4, In Progress)
**Created:** 2025-04-07 via Email  |  **Requester:** Siddharth Singh  |  **Assigned to:** Rahul Menon

**Description:** Siddharth Singh (Product Management) reported an issue via Email related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00046 — Deployment (P4, Resolved)
**Created:** 2025-04-16 via Slack  |  **Requester:** Siddharth Verma  |  **Assigned to:** Vikram Mehta

**Description:** Siddharth Verma (Data & Analytics) reported an issue via Slack related to 'Service Deployment Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Service Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DEVOPS-001 to resolve. the DevOps Engineer confirms eligibility and prerequisites: verifying the build passed all MK-CI pipeline gates. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Deployment is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-001

---

## TCK3-DEVOPS-00078 — Cost Management (P3, Resolved)
**Created:** 2025-05-03 via Portal  |  **Requester:** Divya Chowdhury  |  **Assigned to:** Vivek Sharma

**Description:** Divya Chowdhury (Human Resources) reported an issue via Portal related to 'Cost Optimization Review'. Category: Cost Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cost Optimization Review', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Cloud Architect gathers the required data and documents, including idle resources, oversized instances, and unused storage. The review team examines the Cloud Cost Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-013

---

## TCK3-DEVOPS-00132 — Observability (P2, Closed)
**Created:** 2025-05-03 via Live Chat  |  **Requester:** Shreya Reddy  |  **Assigned to:** Rahul Menon

**Description:** Shreya Reddy (Product Management) reported an issue via Live Chat related to 'Monitoring and Alerting Setup'. Category: Observability. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Monitoring and Alerting Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DEVOPS-009 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining alert thresholds and the on-call notification channel. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Monitoring Alert is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Monitoring Alert in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-009

---

## TCK3-DEVOPS-00125 — Cost Management (P3, Resolved)
**Created:** 2025-05-04 via Live Chat  |  **Requester:** Ananya Nair  |  **Assigned to:** Vivek Sharma

**Description:** Ananya Nair (IT Support / Information Technology) reported an issue via Live Chat related to 'Cost Optimization Review'. Category: Cost Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cost Optimization Review', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-DEVOPS-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the Cloud Architect gathers the required data and documents, including idle resources, oversized instances, and unused storage. The review team examines the Cloud Cost Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-013

---

## TCK3-DEVOPS-00035 — Infrastructure (P3, Resolved)
**Created:** 2025-05-06 via Email  |  **Requester:** Kavya Nair  |  **Assigned to:** Rahul Menon

**Description:** Kavya Nair (Finance & Accounting) reported an issue via Email related to 'Infrastructure as Code (IaC) Change Procedure'. Category: Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Infrastructure as Code (IaC) Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DEVOPS-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply. The review team examines the IaC Change against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-005

---

## TCK3-DEVOPS-00062 — Cloud Infrastructure (P1, Resolved)
**Created:** 2025-05-07 via Live Chat  |  **Requester:** Kavya Kapoor  |  **Assigned to:** Siddharth Mehta

**Description:** Kavya Kapoor (Customer Support / Helpdesk) reported an issue via Live Chat related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00137 — Cloud Infrastructure (P3, Resolved)
**Created:** 2025-05-10 via Walk-in  |  **Requester:** Varun Chowdhury  |  **Assigned to:** Rahul Menon

**Description:** Varun Chowdhury (Sales) reported an issue via Walk-in related to 'Auto-scaling Configuration Procedure'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Auto-scaling Configuration Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DEVOPS-006 to resolve. the DevOps Engineer confirms eligibility and prerequisites: target CPU/memory thresholds and min/max instance counts. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Auto-scaling Policy is required. The Cloud Architect reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Auto-scaling Policy in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-006

---

## TCK3-DEVOPS-00050 — Operations (P3, Resolved)
**Created:** 2025-05-16 via Phone  |  **Requester:** Preeti Verma  |  **Assigned to:** Meera Joshi

**Description:** Preeti Verma (Software Engineering / Development) reported an issue via Phone related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00076 — CI/CD (P4, Closed)
**Created:** 2025-05-16 via Walk-in  |  **Requester:** Manoj Singh  |  **Assigned to:** Riya Chauhan

**Description:** Manoj Singh (Product Management) reported an issue via Walk-in related to 'CI/CD Pipeline Configuration'. Category: CI/CD. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'CI/CD Pipeline Configuration', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-002 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining build, test, and deploy stages with required approvals. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which CI/CD Pipeline is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the CI/CD Pipeline in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-002

---

## TCK3-DEVOPS-00133 — Operations (P3, Resolved)
**Created:** 2025-05-17 via Email  |  **Requester:** Sahil Menon  |  **Assigned to:** Neel Joshi

**Description:** Sahil Menon (QA / Testing) reported an issue via Email related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---
