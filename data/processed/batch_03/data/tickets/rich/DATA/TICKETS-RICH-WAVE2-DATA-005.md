# Data & Analytics — Rich Historical Ticket Archive (wave2, Page 5)

## TCK3-DATA-00052 — Data Sharing (P1, Resolved)
**Created:** 2025-10-11 via Slack  |  **Requester:** Shreya Reddy  |  **Assigned to:** Priya Sharma

**Description:** Shreya Reddy (Cybersecurity / Information Security) reported an issue via Slack related to 'Third-Party Data Sharing Request'. Category: Data Sharing. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Third-Party Data Sharing Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-014 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Sharing Request' section. the requester selects 'New Data Sharing Request' and enters the required details, including the recipient organisation, purpose, and data fields to be shared. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Sharing Request; MK-DataLake automatically routes it to the Legal Manager for review. The Legal Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-014

---

## TCK3-DATA-00117 — Analytics (P3, Resolved)
**Created:** 2025-10-16 via Slack  |  **Requester:** Simran Gupta  |  **Assigned to:** Arjun Gupta

**Description:** Simran Gupta (Sales) reported an issue via Slack related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00048 — Reporting (P4, Closed)
**Created:** 2025-10-19 via Portal  |  **Requester:** Gaurav Chowdhury  |  **Assigned to:** Priya Sharma

**Description:** Gaurav Chowdhury (Marketing) reported an issue via Portal related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00050 — Data Governance (P4, Closed)
**Created:** 2025-10-26 via Email  |  **Requester:** Nisha Bose  |  **Assigned to:** Vikram Rao

**Description:** Nisha Bose (Customer Support / Helpdesk) reported an issue via Email related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---

## TCK3-DATA-00114 — Machine Learning (P4, Resolved)
**Created:** 2025-10-27 via Slack  |  **Requester:** Aman Chauhan  |  **Assigned to:** Sneha Kapoor

**Description:** Aman Chauhan (Sales) reported an issue via Slack related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00027 — Data Access (P2, Closed)
**Created:** 2025-11-03 via Phone  |  **Requester:** Gaurav Pillai  |  **Assigned to:** Alisha Reddy

**Description:** Gaurav Pillai (Data & Analytics) reported an issue via Phone related to 'Data Access Request Procedure'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Access Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-DATA-001 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Access Request' section. the requester selects 'New Data Access Request' and enters the required details, including the specific dataset, business purpose, and required access level. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Access Request; MK-DataLake automatically routes it to the Data Manager for review. The Data Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-001

---

## TCK3-DATA-00138 — Data Privacy (P2, Resolved)
**Created:** 2025-11-06 via Live Chat  |  **Requester:** Manoj Chauhan  |  **Assigned to:** Gaurav Pillai

**Description:** Manoj Chauhan (Administration / Facilities) reported an issue via Live Chat related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00058 — Data Privacy (P2, Resolved)
**Created:** 2025-11-12 via Slack  |  **Requester:** Harsh Chauhan  |  **Assigned to:** Neel Reddy

**Description:** Harsh Chauhan (QA / Testing) reported an issue via Slack related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00141 — Data Access (P3, Resolved)
**Created:** 2025-11-16 via Walk-in  |  **Requester:** Varun Kapoor  |  **Assigned to:** Preeti Mehta

**Description:** Varun Kapoor (Data & Analytics) reported an issue via Walk-in related to 'Analytics Tool Access Provisioning'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Analytics Tool Access Provisioning', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-015 to resolve. the requester confirms eligibility and prerequisites: the specific tool (MK-DataLake, BI dashboards) and role required. the requester raises a request in MK-DataLake specifying exactly which Analytics Tool Access is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Analytics Tool Access in the relevant system. the requester is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-015

---

## TCK3-DATA-00073 — Data Governance (P3, Resolved)
**Created:** 2025-11-23 via Slack  |  **Requester:** Rohan Agarwal  |  **Assigned to:** Sneha Kapoor

**Description:** Rohan Agarwal (Cybersecurity / Information Security) reported an issue via Slack related to 'Data Retention and Deletion Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Retention and Deletion Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-DATA-008 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal. The review team examines the Data Retention Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-008

---

## TCK3-DATA-00118 — Reporting (P3, In Progress)
**Created:** 2025-11-28 via Email  |  **Requester:** Aditya Sharma  |  **Assigned to:** Isha Iyer

**Description:** Aditya Sharma (Finance & Accounting) reported an issue via Email related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00068 — Data Privacy (P4, Resolved)
**Created:** 2025-12-14 via Portal  |  **Requester:** Kabir Agarwal  |  **Assigned to:** Gaurav Pillai

**Description:** Kabir Agarwal (Customer Support / Helpdesk) reported an issue via Portal related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00031 — Data Privacy (P4, Resolved)
**Created:** 2025-12-26 via Portal  |  **Requester:** Siddharth Reddy  |  **Assigned to:** Varun Kapoor

**Description:** Siddharth Reddy (Human Resources) reported an issue via Portal related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00023 — Reporting (P4, Resolved)
**Created:** 2025-12-30 via Walk-in  |  **Requester:** Neel Sharma  |  **Assigned to:** Alisha Reddy

**Description:** Neel Sharma (Software Engineering / Development) reported an issue via Walk-in related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00146 — Data Engineering (P3, Resolved)
**Created:** 2025-12-31 via Phone  |  **Requester:** Swati Sharma  |  **Assigned to:** Arjun Gupta

**Description:** Swati Sharma (QA / Testing) reported an issue via Phone related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00037 — Analytics (P1, Resolved)
**Created:** 2026-01-25 via Portal  |  **Requester:** Harsh Gupta  |  **Assigned to:** Rohan Mehta

**Description:** Harsh Gupta (Research & Development) reported an issue via Portal related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00115 — Onboarding (P4, Resolved)
**Created:** 2026-01-31 via Portal  |  **Requester:** Isha Agarwal  |  **Assigned to:** Siddharth Verma

**Description:** Isha Agarwal (Human Resources) reported an issue via Portal related to 'Data Onboarding for New Team Members'. Category: Onboarding. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Onboarding for New Team Members', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-DATA-011 to resolve. HR notifies the relevant department and the MK-DataLake owner ahead of the employee's start or end date. the Data Manager prepares the required Data Onboarding, including MK-DataLake access, SQL style guide, and a shadowing assignment. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Director of Data & Analytics verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DATA-011

---

## TCK3-DATA-00081 — Data Governance (P2, Closed)
**Created:** 2026-02-02 via Live Chat  |  **Requester:** Meera Chowdhury  |  **Assigned to:** Rohan Mehta

**Description:** Meera Chowdhury (Project Management / PMO) reported an issue via Live Chat related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---

## TCK3-DATA-00107 — Data Engineering (P3, Resolved)
**Created:** 2026-02-03 via Portal  |  **Requester:** Tanya Mehta  |  **Assigned to:** Varun Kapoor

**Description:** Tanya Mehta (Human Resources) reported an issue via Portal related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00034 — Data Sharing (P2, In Progress)
**Created:** 2026-02-07 via Live Chat  |  **Requester:** Vikram Mehta  |  **Assigned to:** Bhavna Rao

**Description:** Vikram Mehta (DevOps & Cloud) reported an issue via Live Chat related to 'Third-Party Data Sharing Request'. Category: Data Sharing. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Third-Party Data Sharing Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-014

---
