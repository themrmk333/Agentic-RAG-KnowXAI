# Data & Analytics — Rich Historical Ticket Archive (wave2, Page 7)

## TCK3-DATA-00129 — Data Governance (P3, Resolved)
**Created:** 2026-05-22 via Phone  |  **Requester:** Tanya Singh  |  **Assigned to:** Gaurav Pillai

**Description:** Tanya Singh (Software Engineering / Development) reported an issue via Phone related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---

## TCK3-DATA-00125 — Data Sharing (P3, Resolved)
**Created:** 2026-05-26 via Walk-in  |  **Requester:** Kavya Reddy  |  **Assigned to:** Varun Kapoor

**Description:** Kavya Reddy (Finance & Accounting) reported an issue via Walk-in related to 'Third-Party Data Sharing Request'. Category: Data Sharing. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Third-Party Data Sharing Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-014 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Sharing Request' section. the requester selects 'New Data Sharing Request' and enters the required details, including the recipient organisation, purpose, and data fields to be shared. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Sharing Request; MK-DataLake automatically routes it to the Legal Manager for review. The Legal Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-014

---

## TCK3-DATA-00110 — Data Access (P3, Resolved)
**Created:** 2026-06-03 via Portal  |  **Requester:** Meera Chauhan  |  **Assigned to:** Isha Iyer

**Description:** Meera Chauhan (Procurement / Purchasing) reported an issue via Portal related to 'Data Access Request Procedure'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Access Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-DATA-001 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Access Request' section. the requester selects 'New Data Access Request' and enters the required details, including the specific dataset, business purpose, and required access level. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Access Request; MK-DataLake automatically routes it to the Data Manager for review. The Data Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-001

---

## TCK3-DATA-00142 — Data Sharing (P3, Resolved)
**Created:** 2026-06-05 via Slack  |  **Requester:** Neel Reddy  |  **Assigned to:** Varun Kapoor

**Description:** Neel Reddy (Data & Analytics) reported an issue via Slack related to 'Third-Party Data Sharing Request'. Category: Data Sharing. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Third-Party Data Sharing Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-014 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Sharing Request' section. the requester selects 'New Data Sharing Request' and enters the required details, including the recipient organisation, purpose, and data fields to be shared. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Sharing Request; MK-DataLake automatically routes it to the Legal Manager for review. The Legal Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-014

---

## TCK3-DATA-00072 — Data Access (P4, Closed)
**Created:** 2026-06-09 via Phone  |  **Requester:** Alisha Reddy  |  **Assigned to:** Varun Kapoor

**Description:** Alisha Reddy (Data & Analytics) reported an issue via Phone related to 'Analytics Tool Access Provisioning'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Analytics Tool Access Provisioning', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-015 to resolve. the requester confirms eligibility and prerequisites: the specific tool (MK-DataLake, BI dashboards) and role required. the requester raises a request in MK-DataLake specifying exactly which Analytics Tool Access is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Analytics Tool Access in the relevant system. the requester is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-015

---

## TCK3-DATA-00108 — Data Access (P2, Closed)
**Created:** 2026-06-26 via Portal  |  **Requester:** Aditya Chauhan  |  **Assigned to:** Isha Iyer

**Description:** Aditya Chauhan (Administration / Facilities) reported an issue via Portal related to 'Data Access Request Procedure'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Access Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-001 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Access Request' section. the requester selects 'New Data Access Request' and enters the required details, including the specific dataset, business purpose, and required access level. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Access Request; MK-DataLake automatically routes it to the Data Manager for review. The Data Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-001

---

## TCK3-DATA-00120 — Data Engineering (P3, Resolved)
**Created:** 2026-06-28 via Walk-in  |  **Requester:** Yash Chauhan  |  **Assigned to:** Sneha Kapoor

**Description:** Yash Chauhan (Procurement / Purchasing) reported an issue via Walk-in related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00074 — Data Governance (P2, Resolved)
**Created:** 2026-07-31 via Slack  |  **Requester:** Pooja Mehta  |  **Assigned to:** Siddharth Verma

**Description:** Pooja Mehta (Product Management) reported an issue via Slack related to 'KPI Definition and Governance Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'KPI Definition and Governance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DATA-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including a single agreed formula and data source per KPI to avoid conflicting numbers. The review team examines the KPI Definition against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-010

---

## TCK3-DATA-00132 — Data Access (P3, Resolved)
**Created:** 2026-07-31 via Walk-in  |  **Requester:** Neel Reddy  |  **Assigned to:** Arjun Gupta

**Description:** Neel Reddy (Data & Analytics) reported an issue via Walk-in related to 'Data Access Request Procedure'. Category: Data Access. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Access Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-DATA-001 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Access Request' section. the requester selects 'New Data Access Request' and enters the required details, including the specific dataset, business purpose, and required access level. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Access Request; MK-DataLake automatically routes it to the Data Manager for review. The Data Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-001

---

## TCK3-DATA-00083 — Data Governance (P3, Closed)
**Created:** 2026-08-01 via Live Chat  |  **Requester:** Preeti Malhotra  |  **Assigned to:** Isha Iyer

**Description:** Preeti Malhotra (DevOps & Cloud) reported an issue via Live Chat related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---

## TCK3-DATA-00090 — Data Governance (P3, Resolved)
**Created:** 2026-08-19 via Live Chat  |  **Requester:** Siddharth Mehta  |  **Assigned to:** Neel Reddy

**Description:** Siddharth Mehta (DevOps & Cloud) reported an issue via Live Chat related to 'Data Classification for Analytics Datasets'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Classification for Analytics Datasets', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-005 to resolve. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system. the Data Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-005

---