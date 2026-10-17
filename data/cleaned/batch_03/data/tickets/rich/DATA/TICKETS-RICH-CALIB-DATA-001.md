# Data & Analytics — Rich Historical Ticket Archive (calib, Page 1)

## TCK3-DATA-00008 — Data Privacy (P3, Resolved)
**Created:** 2024-06-30 via Phone  |  **Requester:** Divya Menon  |  **Assigned to:** Varun Kapoor

**Description:** Divya Menon (QA / Testing) reported an issue via Phone related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00015 — Data Governance (P3, Resolved)
**Created:** 2024-09-26 via Email  |  **Requester:** Kabir Reddy  |  **Assigned to:** Tanya Iyer

**Description:** Kabir Reddy (QA / Testing) reported an issue via Email related to 'Data Retention and Deletion Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Retention and Deletion Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DATA-008 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal. The review team examines the Data Retention Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-008

---

## TCK3-DATA-00007 — Data Governance (P3, Resolved)
**Created:** 2024-10-15 via Phone  |  **Requester:** Rohan Singh  |  **Assigned to:** Varun Kapoor

**Description:** Rohan Singh (Sales) reported an issue via Phone related to 'Data Retention and Deletion Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Retention and Deletion Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DATA-008 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal. The review team examines the Data Retention Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-008

---

## TCK3-DATA-00011 — Onboarding (P3, Closed)
**Created:** 2024-11-02 via Phone  |  **Requester:** Rohan Singh  |  **Assigned to:** Gaurav Mehta

**Description:** Rohan Singh (Marketing) reported an issue via Phone related to 'Data Onboarding for New Team Members'. Category: Onboarding. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Onboarding for New Team Members', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-DATA-011 to resolve. HR notifies the relevant department and the MK-DataLake owner ahead of the employee's start or end date. the Data Manager prepares the required Data Onboarding, including MK-DataLake access, SQL style guide, and a shadowing assignment. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Director of Data & Analytics verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DATA-011

---

## TCK3-DATA-00009 — Data Engineering (P2, Resolved)
**Created:** 2024-11-26 via Email  |  **Requester:** Kabir Agarwal  |  **Assigned to:** Aman Pillai

**Description:** Kabir Agarwal (Customer Support / Helpdesk) reported an issue via Email related to 'Data Pipeline Development Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Pipeline Development Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-003 to resolve. the Data Engineer confirms eligibility and prerequisites: source system, transformation logic, and data quality checks. the Data Engineer raises a request in MK-DataLake specifying exactly which Data Pipeline is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Pipeline in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-003

---

## TCK3-DATA-00018 — Data Governance (P4, Resolved)
**Created:** 2024-12-02 via Live Chat  |  **Requester:** Ritika Rao  |  **Assigned to:** Priya Sharma

**Description:** Ritika Rao (Human Resources) reported an issue via Live Chat related to 'KPI Definition and Governance Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'KPI Definition and Governance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DATA-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including a single agreed formula and data source per KPI to avoid conflicting numbers. The review team examines the KPI Definition against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-010

---

## TCK3-DATA-00003 — Data Privacy (P2, Resolved)
**Created:** 2024-12-09 via Live Chat  |  **Requester:** Sneha Pillai  |  **Assigned to:** Alisha Reddy

**Description:** Sneha Pillai (Administration / Facilities) reported an issue via Live Chat related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00014 — Data Quality (P3, Closed)
**Created:** 2024-12-26 via Walk-in  |  **Requester:** Dev Chauhan  |  **Assigned to:** Vikram Rao

**Description:** Dev Chauhan (Marketing) reported an issue via Walk-in related to 'Data Quality Issue Resolution Procedure'. Category: Data Quality. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Quality Issue Resolution Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-DATA-004 to resolve. the Data Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Data Analyst performs the standard first-line check: identifying the affected table and the scope of impacted reports. If the issue persists, the Data Analyst applies the documented workaround for this issue type. the Data Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Data Analyst raises a ticket in MK-DataLake categorised under 'Data Quality Incident', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DATA-004

---

## TCK3-DATA-00001 — Machine Learning (P3, Resolved)
**Created:** 2025-04-21 via Slack  |  **Requester:** Kavya Desai  |  **Assigned to:** Varun Kapoor

**Description:** Kavya Desai (Customer Support / Helpdesk) reported an issue via Slack related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00013 — Onboarding (P3, Resolved)
**Created:** 2025-07-24 via Email  |  **Requester:** Isha Iyer  |  **Assigned to:** Isha Iyer

**Description:** Isha Iyer (Data & Analytics) reported an issue via Email related to 'Data Onboarding for New Team Members'. Category: Onboarding. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Onboarding for New Team Members', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-DATA-011 to resolve. HR notifies the relevant department and the MK-DataLake owner ahead of the employee's start or end date. the Data Manager prepares the required Data Onboarding, including MK-DataLake access, SQL style guide, and a shadowing assignment. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Director of Data & Analytics verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DATA-011

---

## TCK3-DATA-00010 — Analytics (P2, Closed)
**Created:** 2025-09-12 via Email  |  **Requester:** Yash Iyer  |  **Assigned to:** Aman Pillai

**Description:** Yash Iyer (Research & Development) reported an issue via Email related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00002 — Analytics (P3, Resolved)
**Created:** 2026-01-07 via Live Chat  |  **Requester:** Bhavna Kapoor  |  **Assigned to:** Rohan Mehta

**Description:** Bhavna Kapoor (DevOps & Cloud) reported an issue via Live Chat related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00019 — Reporting (P2, Resolved)
**Created:** 2026-01-20 via Phone  |  **Requester:** Vikram Iyer  |  **Assigned to:** Bhavna Rao

**Description:** Vikram Iyer (Management / Leadership) reported an issue via Phone related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00020 — Data Governance (P3, Resolved)
**Created:** 2026-01-27 via Live Chat  |  **Requester:** Vivek Singh  |  **Assigned to:** Rohan Mehta

**Description:** Vivek Singh (Procurement / Purchasing) reported an issue via Live Chat related to 'Data Retention and Deletion Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Retention and Deletion Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DATA-008 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal. The review team examines the Data Retention Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-008

---

## TCK3-DATA-00012 — Data Governance (P3, Closed)
**Created:** 2026-02-16 via Walk-in  |  **Requester:** Ananya Nair  |  **Assigned to:** Rohan Mehta

**Description:** Ananya Nair (IT Support / Information Technology) reported an issue via Walk-in related to 'Data Retention and Deletion Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Retention and Deletion Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-DATA-008 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal. The review team examines the Data Retention Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-008

---

## TCK3-DATA-00005 — Machine Learning (P4, Closed)
**Created:** 2026-02-20 via Walk-in  |  **Requester:** Riya Chauhan  |  **Assigned to:** Bhavna Rao

**Description:** Riya Chauhan (DevOps & Cloud) reported an issue via Walk-in related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00004 — Machine Learning (P3, In Progress)
**Created:** 2026-03-17 via Live Chat  |  **Requester:** Meera Malhotra  |  **Assigned to:** Sneha Kapoor

**Description:** Meera Malhotra (Procurement / Purchasing) reported an issue via Live Chat related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00016 — Data Governance (P4, Resolved)
**Created:** 2026-05-14 via Email  |  **Requester:** Sneha Agarwal  |  **Assigned to:** Sneha Kapoor

**Description:** Sneha Agarwal (Research & Development) reported an issue via Email related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---

## TCK3-DATA-00006 — Data Access (P4, Resolved)
**Created:** 2026-07-01 via Walk-in  |  **Requester:** Gaurav Mehta  |  **Assigned to:** Isha Iyer

**Description:** Gaurav Mehta (Data & Analytics) reported an issue via Walk-in related to 'Analytics Tool Access Provisioning'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Analytics Tool Access Provisioning', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-015 to resolve. the requester confirms eligibility and prerequisites: the specific tool (MK-DataLake, BI dashboards) and role required. the requester raises a request in MK-DataLake specifying exactly which Analytics Tool Access is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Analytics Tool Access in the relevant system. the requester is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-015

---

## TCK3-DATA-00017 — Data Sharing (P4, Closed)
**Created:** 2026-07-03 via Walk-in  |  **Requester:** Manoj Nair  |  **Assigned to:** Bhavna Rao

**Description:** Manoj Nair (Cybersecurity / Information Security) reported an issue via Walk-in related to 'Third-Party Data Sharing Request'. Category: Data Sharing. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Third-Party Data Sharing Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-014 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Sharing Request' section. the requester selects 'New Data Sharing Request' and enters the required details, including the recipient organisation, purpose, and data fields to be shared. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Sharing Request; MK-DataLake automatically routes it to the Legal Manager for review. The Legal Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-014

---