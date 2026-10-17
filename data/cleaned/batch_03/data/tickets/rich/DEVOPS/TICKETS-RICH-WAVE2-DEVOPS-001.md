# DevOps & Cloud — Rich Historical Ticket Archive (wave2, Page 1)

## TCK3-DEVOPS-00135 — Containers (P3, Resolved)
**Created:** 2024-06-04 via Live Chat  |  **Requester:** Shreya Kapoor  |  **Assigned to:** Siddharth Mehta

**Description:** Shreya Kapoor (Cybersecurity / Information Security) reported an issue via Live Chat related to 'Container Image Build and Publish'. Category: Containers. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Container Image Build and Publish', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-010 to resolve. the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Container Image in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-010

---

## TCK3-DEVOPS-00056 — Cloud Infrastructure (P2, Resolved)
**Created:** 2024-06-06 via Phone  |  **Requester:** Ritika Kapoor  |  **Assigned to:** Bhavna Kapoor

**Description:** Ritika Kapoor (Product Management) reported an issue via Phone related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00106 — Containers (P3, Resolved)
**Created:** 2024-06-10 via Portal  |  **Requester:** Preeti Reddy  |  **Assigned to:** Aditya Rao

**Description:** Preeti Reddy (Management / Leadership) reported an issue via Portal related to 'Container Image Build and Publish'. Category: Containers. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Container Image Build and Publish', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-010 to resolve. the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Container Image in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-010

---

## TCK3-DEVOPS-00070 — Security (P4, Resolved)
**Created:** 2024-06-17 via Portal  |  **Requester:** Bhavna Pillai  |  **Assigned to:** Vikram Mehta

**Description:** Bhavna Pillai (Sales) reported an issue via Portal related to 'Secrets and Credentials Management'. Category: Security. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Secrets and Credentials Management', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-008 to resolve. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-008

---

## TCK3-DEVOPS-00103 — Onboarding (P2, Resolved)
**Created:** 2024-06-23 via Phone  |  **Requester:** Priya Rao  |  **Assigned to:** Vikram Mehta

**Description:** Priya Rao (DevOps & Cloud) reported an issue via Phone related to 'DevOps New Engineer Onboarding'. Category: Onboarding. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'DevOps New Engineer Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-DEVOPS-014 to resolve. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The DevOps Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DEVOPS-014

---

## TCK3-DEVOPS-00031 — Deployment (P3, Resolved)
**Created:** 2024-07-02 via Phone  |  **Requester:** Rahul Reddy  |  **Assigned to:** Bhavna Kapoor

**Description:** Rahul Reddy (Cybersecurity / Information Security) reported an issue via Phone related to 'Service Deployment Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Service Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-001 to resolve. the DevOps Engineer confirms eligibility and prerequisites: verifying the build passed all MK-CI pipeline gates. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Deployment is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Deployment in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-001

---

## TCK3-DEVOPS-00051 — Deployment (P3, In Progress)
**Created:** 2024-07-05 via Slack  |  **Requester:** Divya Gupta  |  **Assigned to:** Gaurav Menon

**Description:** Divya Gupta (QA / Testing) reported an issue via Slack related to 'Rollback Procedure'. Category: Deployment. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Rollback Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-012

---

## TCK3-DEVOPS-00087 — Cloud Infrastructure (P4, Closed)
**Created:** 2024-07-07 via Email  |  **Requester:** Sneha Reddy  |  **Assigned to:** Vivek Sharma

**Description:** Sneha Reddy (QA / Testing) reported an issue via Email related to 'Auto-scaling Configuration Procedure'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Auto-scaling Configuration Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-006 to resolve. the DevOps Engineer confirms eligibility and prerequisites: target CPU/memory thresholds and min/max instance counts. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Auto-scaling Policy is required. The Cloud Architect reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Auto-scaling Policy in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-006

---

## TCK3-DEVOPS-00085 — Cloud Infrastructure (P4, Resolved)
**Created:** 2024-07-14 via Portal  |  **Requester:** Shreya Nair  |  **Assigned to:** Bhavna Kapoor

**Description:** Shreya Nair (Project Management / PMO) reported an issue via Portal related to 'Auto-scaling Configuration Procedure'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Auto-scaling Configuration Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DEVOPS-006 to resolve. the DevOps Engineer confirms eligibility and prerequisites: target CPU/memory thresholds and min/max instance counts. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Auto-scaling Policy is required. The Cloud Architect reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Auto-scaling Policy in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-006

---

## TCK3-DEVOPS-00145 — Operations (P3, Resolved)
**Created:** 2024-07-15 via Portal  |  **Requester:** Harsh Nair  |  **Assigned to:** Priya Rao

**Description:** Harsh Nair (Cybersecurity / Information Security) reported an issue via Portal related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00034 — Observability (P4, Resolved)
**Created:** 2024-07-17 via Live Chat  |  **Requester:** Gaurav Pillai  |  **Assigned to:** Gaurav Menon

**Description:** Gaurav Pillai (Data & Analytics) reported an issue via Live Chat related to 'Monitoring and Alerting Setup'. Category: Observability. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Monitoring and Alerting Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DEVOPS-009 to resolve. the DevOps Engineer confirms eligibility and prerequisites: defining alert thresholds and the on-call notification channel. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Monitoring Alert is required. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Monitoring Alert in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-009

---

## TCK3-DEVOPS-00091 — Incident Management (P4, In Progress)
**Created:** 2024-07-20 via Phone  |  **Requester:** Siddharth Iyer  |  **Assigned to:** Vivek Sharma

**Description:** Siddharth Iyer (Management / Leadership) reported an issue via Phone related to 'Production Incident Response (DevOps)'. Category: Incident Management. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Production Incident Response (DevOps)', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DEVOPS-004

---

## TCK3-DEVOPS-00027 — Operations (P3, Resolved)
**Created:** 2024-07-28 via Portal  |  **Requester:** Nisha Bose  |  **Assigned to:** Preeti Malhotra

**Description:** Nisha Bose (Customer Support / Helpdesk) reported an issue via Portal related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00060 — Operations (P3, Resolved)
**Created:** 2024-08-05 via Email  |  **Requester:** Bhavna Gupta  |  **Assigned to:** Meera Joshi

**Description:** Bhavna Gupta (Legal & Compliance) reported an issue via Email related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00063 — Cloud Infrastructure (P3, Closed)
**Created:** 2024-08-05 via Email  |  **Requester:** Rohan Kapoor  |  **Assigned to:** Meera Joshi

**Description:** Rohan Kapoor (Marketing) reported an issue via Email related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00112 — Operations (P4, Resolved)
**Created:** 2024-08-08 via Slack  |  **Requester:** Aman Nair  |  **Assigned to:** Aditya Rao

**Description:** Aman Nair (Finance & Accounting) reported an issue via Slack related to 'On-call Rotation and Handover'. Category: Operations. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'On-call Rotation and Handover', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DEVOPS-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts. The review team examines the On-call Handover against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-016

---

## TCK3-DEVOPS-00072 — Cloud Infrastructure (P4, Resolved)
**Created:** 2024-08-10 via Phone  |  **Requester:** Bhavna Kapoor  |  **Assigned to:** Meera Joshi

**Description:** Bhavna Kapoor (Project Management / PMO) reported an issue via Phone related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---

## TCK3-DEVOPS-00113 — Cloud Infrastructure (P3, Resolved)
**Created:** 2024-08-11 via Live Chat  |  **Requester:** Siddharth Singh  |  **Assigned to:** Vivek Sharma

**Description:** Siddharth Singh (Procurement / Purchasing) reported an issue via Live Chat related to 'Auto-scaling Configuration Procedure'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Auto-scaling Configuration Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DEVOPS-006 to resolve. the DevOps Engineer confirms eligibility and prerequisites: target CPU/memory thresholds and min/max instance counts. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Auto-scaling Policy is required. The Cloud Architect reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Auto-scaling Policy in the relevant system. the DevOps Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DEVOPS-006

---

## TCK3-DEVOPS-00025 — Infrastructure (P4, Resolved)
**Created:** 2024-08-16 via Portal  |  **Requester:** Siddharth Kapoor  |  **Assigned to:** Ananya Bose

**Description:** Siddharth Kapoor (Marketing) reported an issue via Portal related to 'Infrastructure as Code (IaC) Change Procedure'. Category: Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Infrastructure as Code (IaC) Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-DEVOPS-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CloudOps. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply. The review team examines the IaC Change against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DEVOPS-005

---

## TCK3-DEVOPS-00059 — Cloud Infrastructure (P4, Resolved)
**Created:** 2024-09-14 via Live Chat  |  **Requester:** Isha Iyer  |  **Assigned to:** Vivek Sharma

**Description:** Isha Iyer (Product Management) reported an issue via Live Chat related to 'Cloud Resource Provisioning Request'. Category: Cloud Infrastructure. Logged against MK-CloudOps.

**Investigation:** The assigned specialist reviewed the MK-CloudOps record, confirmed the reported symptom against 'Cloud Resource Provisioning Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DEVOPS-003 to resolve. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DEVOPS-003

---