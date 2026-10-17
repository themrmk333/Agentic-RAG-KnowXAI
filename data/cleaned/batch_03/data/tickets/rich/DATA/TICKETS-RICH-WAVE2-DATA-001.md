# Data & Analytics — Rich Historical Ticket Archive (wave2, Page 1)

## TCK3-DATA-00065 — Data Governance (P4, Closed)
**Created:** 2024-06-01 via Portal  |  **Requester:** Sneha Reddy  |  **Assigned to:** Bhavna Rao

**Description:** Sneha Reddy (QA / Testing) reported an issue via Portal related to 'KPI Definition and Governance Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'KPI Definition and Governance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DATA-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including a single agreed formula and data source per KPI to avoid conflicting numbers. The review team examines the KPI Definition against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-010

---

## TCK3-DATA-00060 — Reporting (P3, Resolved)
**Created:** 2024-06-04 via Walk-in  |  **Requester:** Varun Menon  |  **Assigned to:** Gaurav Mehta

**Description:** Varun Menon (QA / Testing) reported an issue via Walk-in related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00088 — Analytics (P4, Closed)
**Created:** 2024-06-10 via Email  |  **Requester:** Preeti Kapoor  |  **Assigned to:** Neel Reddy

**Description:** Preeti Kapoor (Marketing) reported an issue via Email related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00030 — Reporting (P2, Resolved)
**Created:** 2024-06-29 via Slack  |  **Requester:** Bhavna Rao  |  **Assigned to:** Varun Kapoor

**Description:** Bhavna Rao (Data & Analytics) reported an issue via Slack related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00122 — Data Engineering (P4, Closed)
**Created:** 2024-07-03 via Phone  |  **Requester:** Siddharth Singh  |  **Assigned to:** Bhavna Rao

**Description:** Siddharth Singh (Product Management) reported an issue via Phone related to 'Data Pipeline Development Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Pipeline Development Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-003 to resolve. the Data Engineer confirms eligibility and prerequisites: source system, transformation logic, and data quality checks. the Data Engineer raises a request in MK-DataLake specifying exactly which Data Pipeline is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Pipeline in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-003

---

## TCK3-DATA-00040 — Data Governance (P3, Resolved)
**Created:** 2024-07-12 via Email  |  **Requester:** Divya Bose  |  **Assigned to:** Tanya Iyer

**Description:** Divya Bose (QA / Testing) reported an issue via Email related to 'Data Retention and Deletion Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Retention and Deletion Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DATA-008 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal. The review team examines the Data Retention Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-008

---

## TCK3-DATA-00105 — Data Access (P2, Resolved)
**Created:** 2024-07-14 via Slack  |  **Requester:** Karan Kapoor  |  **Assigned to:** Tanya Iyer

**Description:** Karan Kapoor (Software Engineering / Development) reported an issue via Slack related to 'Analytics Tool Access Provisioning'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Analytics Tool Access Provisioning', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-015 to resolve. the requester confirms eligibility and prerequisites: the specific tool (MK-DataLake, BI dashboards) and role required. the requester raises a request in MK-DataLake specifying exactly which Analytics Tool Access is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Analytics Tool Access in the relevant system. the requester is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-015

---

## TCK3-DATA-00124 — Data Engineering (P3, Resolved)
**Created:** 2024-08-01 via Walk-in  |  **Requester:** Vivek Chauhan  |  **Assigned to:** Siddharth Verma

**Description:** Vivek Chauhan (Marketing) reported an issue via Walk-in related to 'Data Pipeline Development Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Pipeline Development Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-003 to resolve. the Data Engineer confirms eligibility and prerequisites: source system, transformation logic, and data quality checks. the Data Engineer raises a request in MK-DataLake specifying exactly which Data Pipeline is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Pipeline in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-003

---

## TCK3-DATA-00028 — Machine Learning (P3, Resolved)
**Created:** 2024-08-03 via Email  |  **Requester:** Kavya Iyer  |  **Assigned to:** Varun Kapoor

**Description:** Kavya Iyer (Finance & Accounting) reported an issue via Email related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00056 — Machine Learning (P3, Resolved)
**Created:** 2024-08-12 via Live Chat  |  **Requester:** Divya Malhotra  |  **Assigned to:** Alisha Reddy

**Description:** Divya Malhotra (Product Management) reported an issue via Live Chat related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00093 — Machine Learning (P4, Resolved)
**Created:** 2024-08-13 via Live Chat  |  **Requester:** Manoj Singh  |  **Assigned to:** Rohan Mehta

**Description:** Manoj Singh (Product Management) reported an issue via Live Chat related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00096 — Reporting (P2, Resolved)
**Created:** 2024-08-16 via Portal  |  **Requester:** Bhavna Pillai  |  **Assigned to:** Sneha Kapoor

**Description:** Bhavna Pillai (Sales) reported an issue via Portal related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00094 — Data Access (P3, Resolved)
**Created:** 2024-08-25 via Walk-in  |  **Requester:** Ananya Bose  |  **Assigned to:** Bhavna Rao

**Description:** Ananya Bose (DevOps & Cloud) reported an issue via Walk-in related to 'Analytics Tool Access Provisioning'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Analytics Tool Access Provisioning', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-015 to resolve. the requester confirms eligibility and prerequisites: the specific tool (MK-DataLake, BI dashboards) and role required. the requester raises a request in MK-DataLake specifying exactly which Analytics Tool Access is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Analytics Tool Access in the relevant system. the requester is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-015

---

## TCK3-DATA-00137 — Data Privacy (P1, Resolved)
**Created:** 2024-09-04 via Portal  |  **Requester:** Aman Menon  |  **Assigned to:** Priya Sharma

**Description:** Aman Menon (DevOps & Cloud) reported an issue via Portal related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00078 — Reporting (P3, Resolved)
**Created:** 2024-09-20 via Live Chat  |  **Requester:** Swati Sharma  |  **Assigned to:** Bhavna Rao

**Description:** Swati Sharma (QA / Testing) reported an issue via Live Chat related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00091 — Data Engineering (P2, Closed)
**Created:** 2024-09-27 via Live Chat  |  **Requester:** Sneha Sharma  |  **Assigned to:** Siddharth Verma

**Description:** Sneha Sharma (Research & Development) reported an issue via Live Chat related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00147 — Data Quality (P4, Resolved)
**Created:** 2024-10-04 via Phone  |  **Requester:** Simran Malhotra  |  **Assigned to:** Varun Kapoor

**Description:** Simran Malhotra (Finance & Accounting) reported an issue via Phone related to 'Data Quality Issue Resolution Procedure'. Category: Data Quality. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Quality Issue Resolution Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-DATA-004 to resolve. the Data Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Data Analyst performs the standard first-line check: identifying the affected table and the scope of impacted reports. If the issue persists, the Data Analyst applies the documented workaround for this issue type. the Data Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Data Analyst raises a ticket in MK-DataLake categorised under 'Data Quality Incident', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DATA-004

---

## TCK3-DATA-00092 — Analytics (P3, Closed)
**Created:** 2024-10-10 via Live Chat  |  **Requester:** Preeti Mehta  |  **Assigned to:** Neel Reddy

**Description:** Preeti Mehta (Data & Analytics) reported an issue via Live Chat related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00055 — Data Engineering (P3, Resolved)
**Created:** 2024-10-13 via Walk-in  |  **Requester:** Arjun Pillai  |  **Assigned to:** Aman Pillai

**Description:** Arjun Pillai (Human Resources) reported an issue via Walk-in related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00043 — Data Sharing (P4, Resolved)
**Created:** 2024-10-16 via Portal  |  **Requester:** Simran Kapoor  |  **Assigned to:** Varun Kapoor

**Description:** Simran Kapoor (Product Management) reported an issue via Portal related to 'Third-Party Data Sharing Request'. Category: Data Sharing. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Third-Party Data Sharing Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-014 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Sharing Request' section. the requester selects 'New Data Sharing Request' and enters the required details, including the recipient organisation, purpose, and data fields to be shared. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Sharing Request; MK-DataLake automatically routes it to the Legal Manager for review. The Legal Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-014

---