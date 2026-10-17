# Data & Analytics — Rich Historical Ticket Archive (wave2, Page 3)

## TCK3-DATA-00061 — Data Access (P3, Resolved)
**Created:** 2025-03-07 via Walk-in  |  **Requester:** Neel Joshi  |  **Assigned to:** Vikram Rao

**Description:** Neel Joshi (DevOps & Cloud) reported an issue via Walk-in related to 'Analytics Tool Access Provisioning'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Analytics Tool Access Provisioning', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-015 to resolve. the requester confirms eligibility and prerequisites: the specific tool (MK-DataLake, BI dashboards) and role required. the requester raises a request in MK-DataLake specifying exactly which Analytics Tool Access is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Analytics Tool Access in the relevant system. the requester is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-015

---

## TCK3-DATA-00079 — Data Engineering (P3, Resolved)
**Created:** 2025-03-20 via Email  |  **Requester:** Yash Mehta  |  **Assigned to:** Isha Iyer

**Description:** Yash Mehta (Software Engineering / Development) reported an issue via Email related to 'Data Pipeline Development Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Pipeline Development Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-003 to resolve. the Data Engineer confirms eligibility and prerequisites: source system, transformation logic, and data quality checks. the Data Engineer raises a request in MK-DataLake specifying exactly which Data Pipeline is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Pipeline in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-003

---

## TCK3-DATA-00045 — Machine Learning (P4, Resolved)
**Created:** 2025-03-21 via Walk-in  |  **Requester:** Kabir Reddy  |  **Assigned to:** Isha Iyer

**Description:** Kabir Reddy (QA / Testing) reported an issue via Walk-in related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00070 — Executive Reporting (P3, Resolved)
**Created:** 2025-03-23 via Live Chat  |  **Requester:** Manoj Nair  |  **Assigned to:** Gaurav Pillai

**Description:** Manoj Nair (QA / Testing) reported an issue via Live Chat related to 'Executive Reporting Package Preparation'. Category: Executive Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Executive Reporting Package Preparation', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DATA-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including validating figures against source systems before distribution. The review team examines the Executive Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-012

---

## TCK3-DATA-00042 — Onboarding (P3, Resolved)
**Created:** 2025-04-03 via Phone  |  **Requester:** Isha Iyer  |  **Assigned to:** Preeti Mehta

**Description:** Isha Iyer (Product Management) reported an issue via Phone related to 'Data Onboarding for New Team Members'. Category: Onboarding. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Onboarding for New Team Members', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-DATA-011 to resolve. HR notifies the relevant department and the MK-DataLake owner ahead of the employee's start or end date. the Data Manager prepares the required Data Onboarding, including MK-DataLake access, SQL style guide, and a shadowing assignment. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Director of Data & Analytics verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DATA-011

---

## TCK3-DATA-00054 — Data Engineering (P3, Resolved)
**Created:** 2025-04-04 via Walk-in  |  **Requester:** Manoj Sharma  |  **Assigned to:** Sneha Kapoor

**Description:** Manoj Sharma (Research & Development) reported an issue via Walk-in related to 'Data Pipeline Development Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Pipeline Development Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-003 to resolve. the Data Engineer confirms eligibility and prerequisites: source system, transformation logic, and data quality checks. the Data Engineer raises a request in MK-DataLake specifying exactly which Data Pipeline is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Pipeline in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-003

---

## TCK3-DATA-00098 — Data Privacy (P4, Resolved)
**Created:** 2025-04-06 via Live Chat  |  **Requester:** Rohan Reddy  |  **Assigned to:** Arjun Gupta

**Description:** Rohan Reddy (Procurement / Purchasing) reported an issue via Live Chat related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00075 — Data Access (P2, Resolved)
**Created:** 2025-04-11 via Live Chat  |  **Requester:** Aditya Rao  |  **Assigned to:** Tanya Iyer

**Description:** Aditya Rao (Cybersecurity / Information Security) reported an issue via Live Chat related to 'Analytics Tool Access Provisioning'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Analytics Tool Access Provisioning', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-015 to resolve. the requester confirms eligibility and prerequisites: the specific tool (MK-DataLake, BI dashboards) and role required. the requester raises a request in MK-DataLake specifying exactly which Analytics Tool Access is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Analytics Tool Access in the relevant system. the requester is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-015

---

## TCK3-DATA-00041 — Analytics (P4, Resolved)
**Created:** 2025-04-12 via Slack  |  **Requester:** Vivek Chauhan  |  **Assigned to:** Neel Reddy

**Description:** Vivek Chauhan (Marketing) reported an issue via Slack related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00053 — Machine Learning (P4, Resolved)
**Created:** 2025-04-20 via Portal  |  **Requester:** Vikram Iyer  |  **Assigned to:** Preeti Mehta

**Description:** Vikram Iyer (Management / Leadership) reported an issue via Portal related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00106 — Executive Reporting (P3, Resolved)
**Created:** 2025-04-22 via Slack  |  **Requester:** Manoj Singh  |  **Assigned to:** Varun Kapoor

**Description:** Manoj Singh (Product Management) reported an issue via Slack related to 'Executive Reporting Package Preparation'. Category: Executive Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Executive Reporting Package Preparation', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-DATA-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including validating figures against source systems before distribution. The review team examines the Executive Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-012

---

## TCK3-DATA-00148 — Data Engineering (P4, Closed)
**Created:** 2025-04-22 via Walk-in  |  **Requester:** Isha Agarwal  |  **Assigned to:** Isha Iyer

**Description:** Isha Agarwal (Human Resources) reported an issue via Walk-in related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00130 — Machine Learning (P3, Resolved)
**Created:** 2025-04-30 via Portal  |  **Requester:** Anjali Kapoor  |  **Assigned to:** Isha Iyer

**Description:** Anjali Kapoor (Software Engineering / Development) reported an issue via Portal related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00024 — Analytics (P3, Resolved)
**Created:** 2025-05-01 via Live Chat  |  **Requester:** Bhavna Gupta  |  **Assigned to:** Vikram Rao

**Description:** Bhavna Gupta (Legal & Compliance) reported an issue via Live Chat related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00116 — Data Quality (P3, Resolved)
**Created:** 2025-05-07 via Email  |  **Requester:** Ritika Agarwal  |  **Assigned to:** Varun Kapoor

**Description:** Ritika Agarwal (Project Management / PMO) reported an issue via Email related to 'Data Quality Issue Resolution Procedure'. Category: Data Quality. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Quality Issue Resolution Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-DATA-004 to resolve. the Data Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Data Analyst performs the standard first-line check: identifying the affected table and the scope of impacted reports. If the issue persists, the Data Analyst applies the documented workaround for this issue type. the Data Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Data Analyst raises a ticket in MK-DataLake categorised under 'Data Quality Incident', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DATA-004

---

## TCK3-DATA-00121 — Data Engineering (P3, Resolved)
**Created:** 2025-05-08 via Walk-in  |  **Requester:** Simran Agarwal  |  **Assigned to:** Bhavna Rao

**Description:** Simran Agarwal (Finance & Accounting) reported an issue via Walk-in related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00036 — Data Privacy (P3, Closed)
**Created:** 2025-05-14 via Phone  |  **Requester:** Kabir Rao  |  **Assigned to:** Gaurav Mehta

**Description:** Kabir Rao (Marketing) reported an issue via Phone related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00104 — Data Engineering (P3, In Progress)
**Created:** 2025-05-16 via Email  |  **Requester:** Harsh Chauhan  |  **Assigned to:** Isha Iyer

**Description:** Harsh Chauhan (QA / Testing) reported an issue via Email related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00101 — Executive Reporting (P2, Resolved)
**Created:** 2025-05-23 via Email  |  **Requester:** Aditya Rao  |  **Assigned to:** Alisha Reddy

**Description:** Aditya Rao (DevOps & Cloud) reported an issue via Email related to 'Executive Reporting Package Preparation'. Category: Executive Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Executive Reporting Package Preparation', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DATA-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including validating figures against source systems before distribution. The review team examines the Executive Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-012

---

## TCK3-DATA-00077 — Executive Reporting (P3, Closed)
**Created:** 2025-06-05 via Email  |  **Requester:** Divya Joshi  |  **Assigned to:** Gaurav Pillai

**Description:** Divya Joshi (IT Support / Information Technology) reported an issue via Email related to 'Executive Reporting Package Preparation'. Category: Executive Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Executive Reporting Package Preparation', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DATA-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including validating figures against source systems before distribution. The review team examines the Executive Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-012

---
