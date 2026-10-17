# Data & Analytics — Rich Historical Ticket Archive (wave2, Page 4)

## TCK3-DATA-00143 — Data Governance (P3, Resolved)
**Created:** 2025-06-05 via Email  |  **Requester:** Arjun Pillai  |  **Assigned to:** Neel Reddy

**Description:** Arjun Pillai (IT Support / Information Technology) reported an issue via Email related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---

## TCK3-DATA-00095 — Data Privacy (P2, Resolved)
**Created:** 2025-06-06 via Live Chat  |  **Requester:** Vikram Mehta  |  **Assigned to:** Tanya Iyer

**Description:** Vikram Mehta (DevOps & Cloud) reported an issue via Live Chat related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00127 — Analytics (P2, Resolved)
**Created:** 2025-06-06 via Email  |  **Requester:** Tanya Mehta  |  **Assigned to:** Isha Iyer

**Description:** Tanya Mehta (Human Resources) reported an issue via Email related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00051 — Data Access (P3, In Progress)
**Created:** 2025-06-10 via Portal  |  **Requester:** Nisha Bose  |  **Assigned to:** Aman Pillai

**Description:** Nisha Bose (Customer Support / Helpdesk) reported an issue via Portal related to 'Analytics Tool Access Provisioning'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Analytics Tool Access Provisioning', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-015

---

## TCK3-DATA-00135 — Data Privacy (P3, Closed)
**Created:** 2025-06-12 via Email  |  **Requester:** Kavya Iyer  |  **Assigned to:** Priya Sharma

**Description:** Kavya Iyer (Finance & Accounting) reported an issue via Email related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00133 — Data Access (P4, Resolved)
**Created:** 2025-06-19 via Slack  |  **Requester:** Tanya Iyer  |  **Assigned to:** Rohan Mehta

**Description:** Tanya Iyer (Data & Analytics) reported an issue via Slack related to 'Data Access Request Procedure'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Access Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-DATA-001 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Access Request' section. the requester selects 'New Data Access Request' and enters the required details, including the specific dataset, business purpose, and required access level. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Access Request; MK-DataLake automatically routes it to the Data Manager for review. The Data Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-001

---

## TCK3-DATA-00145 — Data Governance (P3, Resolved)
**Created:** 2025-06-20 via Phone  |  **Requester:** Ananya Bose  |  **Assigned to:** Sneha Kapoor

**Description:** Ananya Bose (Sales) reported an issue via Phone related to 'KPI Definition and Governance Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'KPI Definition and Governance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DATA-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including a single agreed formula and data source per KPI to avoid conflicting numbers. The review team examines the KPI Definition against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-010

---

## TCK3-DATA-00059 — Analytics (P3, Resolved)
**Created:** 2025-06-23 via Slack  |  **Requester:** Karan Bhatt  |  **Assigned to:** Aman Pillai

**Description:** Karan Bhatt (DevOps & Cloud) reported an issue via Slack related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00139 — Data Governance (P4, Resolved)
**Created:** 2025-07-08 via Portal  |  **Requester:** Naveen Verma  |  **Assigned to:** Alisha Reddy

**Description:** Naveen Verma (Finance & Accounting) reported an issue via Portal related to 'KPI Definition and Governance Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'KPI Definition and Governance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-DATA-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including a single agreed formula and data source per KPI to avoid conflicting numbers. The review team examines the KPI Definition against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-010

---

## TCK3-DATA-00025 — Data Governance (P4, In Progress)
**Created:** 2025-07-09 via Phone  |  **Requester:** Aditya Menon  |  **Assigned to:** Varun Kapoor

**Description:** Aditya Menon (IT Support / Information Technology) reported an issue via Phone related to 'KPI Definition and Governance Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'KPI Definition and Governance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-010

---

## TCK3-DATA-00086 — Data Engineering (P3, In Progress)
**Created:** 2025-07-27 via Phone  |  **Requester:** Shreya Reddy  |  **Assigned to:** Vikram Rao

**Description:** Shreya Reddy (Cybersecurity / Information Security) reported an issue via Phone related to 'Data Pipeline Development Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Pipeline Development Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-003

---

## TCK3-DATA-00066 — Data Governance (P2, Resolved)
**Created:** 2025-07-30 via Walk-in  |  **Requester:** Siddharth Iyer  |  **Assigned to:** Gaurav Mehta

**Description:** Siddharth Iyer (Management / Leadership) reported an issue via Walk-in related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---

## TCK3-DATA-00112 — Data Governance (P2, Closed)
**Created:** 2025-07-30 via Slack  |  **Requester:** Arjun Pillai  |  **Assigned to:** Varun Kapoor

**Description:** Arjun Pillai (Human Resources) reported an issue via Slack related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---

## TCK3-DATA-00063 — Data Privacy (P3, Resolved)
**Created:** 2025-08-11 via Walk-in  |  **Requester:** Divya Menon  |  **Assigned to:** Gaurav Mehta

**Description:** Divya Menon (QA / Testing) reported an issue via Walk-in related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00082 — Data Engineering (P4, Resolved)
**Created:** 2025-08-13 via Slack  |  **Requester:** Gaurav Chowdhury  |  **Assigned to:** Varun Kapoor

**Description:** Gaurav Chowdhury (Marketing) reported an issue via Slack related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00144 — Machine Learning (P3, Closed)
**Created:** 2025-08-24 via Live Chat  |  **Requester:** Aditya Verma  |  **Assigned to:** Vikram Rao

**Description:** Aditya Verma (Administration / Facilities) reported an issue via Live Chat related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---

## TCK3-DATA-00109 — Data Engineering (P3, Resolved)
**Created:** 2025-08-28 via Portal  |  **Requester:** Swati Nair  |  **Assigned to:** Alisha Reddy

**Description:** Swati Nair (Finance & Accounting) reported an issue via Portal related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00111 — Data Governance (P2, Resolved)
**Created:** 2025-08-30 via Phone  |  **Requester:** Preeti Desai  |  **Assigned to:** Sneha Kapoor

**Description:** Preeti Desai (Legal & Compliance) reported an issue via Phone related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---

## TCK3-DATA-00021 — Data Sharing (P1, Resolved)
**Created:** 2025-09-16 via Slack  |  **Requester:** Kabir Iyer  |  **Assigned to:** Gaurav Mehta

**Description:** Kabir Iyer (Legal & Compliance) reported an issue via Slack related to 'Third-Party Data Sharing Request'. Category: Data Sharing. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Third-Party Data Sharing Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-014 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Sharing Request' section. the requester selects 'New Data Sharing Request' and enters the required details, including the recipient organisation, purpose, and data fields to be shared. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Sharing Request; MK-DataLake automatically routes it to the Legal Manager for review. The Legal Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-014

---

## TCK3-DATA-00089 — Machine Learning (P4, Closed)
**Created:** 2025-10-01 via Portal  |  **Requester:** Rahul Sharma  |  **Assigned to:** Neel Reddy

**Description:** Rahul Sharma (Finance & Accounting) reported an issue via Portal related to 'Machine Learning Model Deployment Procedure'. Category: Machine Learning. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Machine Learning Model Deployment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-007 to resolve. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-007

---
