# Data & Analytics — Rich Historical Ticket Archive (wave2, Page 2)

## TCK3-DATA-00151 — Onboarding (P3, Resolved)
**Created:** 2024-10-29 via Email  |  **Requester:** Neel Reddy  |  **Assigned to:** Vikram Rao

**Description:** Neel Reddy (Data & Analytics) reported an issue via Email related to 'Data Onboarding for New Team Members'. Category: Onboarding. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Onboarding for New Team Members', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-DATA-011 to resolve. HR notifies the relevant department and the MK-DataLake owner ahead of the employee's start or end date. the Data Manager prepares the required Data Onboarding, including MK-DataLake access, SQL style guide, and a shadowing assignment. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Director of Data & Analytics verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DATA-011

---

## TCK3-DATA-00126 — Data Governance (P3, Closed)
**Created:** 2024-11-05 via Slack  |  **Requester:** Gaurav Menon  |  **Assigned to:** Tanya Iyer

**Description:** Gaurav Menon (DevOps & Cloud) reported an issue via Slack related to 'KPI Definition and Governance Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'KPI Definition and Governance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-DATA-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including a single agreed formula and data source per KPI to avoid conflicting numbers. The review team examines the KPI Definition against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-010

---

## TCK3-DATA-00140 — Data Engineering (P4, Resolved)
**Created:** 2024-11-07 via Walk-in  |  **Requester:** Aditya Verma  |  **Assigned to:** Arjun Gupta

**Description:** Aditya Verma (Administration / Facilities) reported an issue via Walk-in related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00123 — Data Engineering (P3, Resolved)
**Created:** 2024-11-15 via Walk-in  |  **Requester:** Alisha Menon  |  **Assigned to:** Preeti Mehta

**Description:** Alisha Menon (QA / Testing) reported an issue via Walk-in related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-DATA-009 to resolve. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00039 — Reporting (P3, Closed)
**Created:** 2024-12-15 via Phone  |  **Requester:** Tanya Singh  |  **Assigned to:** Gaurav Mehta

**Description:** Tanya Singh (Software Engineering / Development) reported an issue via Phone related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00026 — Data Quality (P3, Resolved)
**Created:** 2024-12-19 via Slack  |  **Requester:** Yash Sharma  |  **Assigned to:** Arjun Gupta

**Description:** Yash Sharma (Administration / Facilities) reported an issue via Slack related to 'Data Quality Issue Resolution Procedure'. Category: Data Quality. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Quality Issue Resolution Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-DATA-004 to resolve. the Data Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Data Analyst performs the standard first-line check: identifying the affected table and the scope of impacted reports. If the issue persists, the Data Analyst applies the documented workaround for this issue type. the Data Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Data Analyst raises a ticket in MK-DataLake categorised under 'Data Quality Incident', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DATA-004

---

## TCK3-DATA-00069 — Data Privacy (P3, Resolved)
**Created:** 2024-12-29 via Email  |  **Requester:** Bhavna Desai  |  **Assigned to:** Rohan Mehta

**Description:** Bhavna Desai (Project Management / PMO) reported an issue via Email related to 'Data Anonymization for Testing Procedure'. Category: Data Privacy. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Anonymization for Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-DATA-013 to resolve. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system. the Data Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-013

---

## TCK3-DATA-00033 — Data Quality (P1, Closed)
**Created:** 2025-01-04 via Phone  |  **Requester:** Gaurav Mehta  |  **Assigned to:** Arjun Gupta

**Description:** Gaurav Mehta (Data & Analytics) reported an issue via Phone related to 'Data Quality Issue Resolution Procedure'. Category: Data Quality. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Quality Issue Resolution Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-DATA-004 to resolve. the Data Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Data Analyst performs the standard first-line check: identifying the affected table and the scope of impacted reports. If the issue persists, the Data Analyst applies the documented workaround for this issue type. the Data Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Data Analyst raises a ticket in MK-DataLake categorised under 'Data Quality Incident', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-DATA-004

---

## TCK3-DATA-00071 — Data Sharing (P4, Closed)
**Created:** 2025-01-07 via Slack  |  **Requester:** Simran Malhotra  |  **Assigned to:** Neel Reddy

**Description:** Simran Malhotra (Finance & Accounting) reported an issue via Slack related to 'Third-Party Data Sharing Request'. Category: Data Sharing. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Third-Party Data Sharing Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-DATA-014 to resolve. the requester logs into MK-DataLake and navigates to the 'Data Sharing Request' section. the requester selects 'New Data Sharing Request' and enters the required details, including the recipient organisation, purpose, and data fields to be shared. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Data Sharing Request; MK-DataLake automatically routes it to the Legal Manager for review. The Legal Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-014

---

## TCK3-DATA-00113 — Reporting (P1, Resolved)
**Created:** 2025-01-09 via Slack  |  **Requester:** Swati Nair  |  **Assigned to:** Arjun Gupta

**Description:** Swati Nair (Finance & Accounting) reported an issue via Slack related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00102 — Data Governance (P3, Resolved)
**Created:** 2025-01-13 via Phone  |  **Requester:** Bhavna Rao  |  **Assigned to:** Preeti Mehta

**Description:** Bhavna Rao (Data & Analytics) reported an issue via Phone related to 'KPI Definition and Governance Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'KPI Definition and Governance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-DATA-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Analytics Lead gathers the required data and documents, including a single agreed formula and data source per KPI to avoid conflicting numbers. The review team examines the KPI Definition against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-010

---

## TCK3-DATA-00134 — Data Governance (P3, Resolved)
**Created:** 2025-01-14 via Portal  |  **Requester:** Isha Iyer  |  **Assigned to:** Bhavna Rao

**Description:** Isha Iyer (Data & Analytics) reported an issue via Portal related to 'Data Retention and Deletion Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Retention and Deletion Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-DATA-008 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal. The review team examines the Data Retention Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-008

---

## TCK3-DATA-00038 — Analytics (P3, Resolved)
**Created:** 2025-01-18 via Portal  |  **Requester:** Naveen Singh  |  **Assigned to:** Neel Reddy

**Description:** Naveen Singh (Human Resources) reported an issue via Portal related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00087 — Onboarding (P3, Resolved)
**Created:** 2025-01-26 via Slack  |  **Requester:** Vivek Sharma  |  **Assigned to:** Neel Reddy

**Description:** Vivek Sharma (DevOps & Cloud) reported an issue via Slack related to 'Data Onboarding for New Team Members'. Category: Onboarding. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Onboarding for New Team Members', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-DATA-011 to resolve. HR notifies the relevant department and the MK-DataLake owner ahead of the employee's start or end date. the Data Manager prepares the required Data Onboarding, including MK-DataLake access, SQL style guide, and a shadowing assignment. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Director of Data & Analytics verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DATA-011

---

## TCK3-DATA-00044 — Reporting (P3, Resolved)
**Created:** 2025-02-06 via Walk-in  |  **Requester:** Ritika Rao  |  **Assigned to:** Tanya Iyer

**Description:** Ritika Rao (Human Resources) reported an issue via Walk-in related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---

## TCK3-DATA-00029 — Analytics (P3, Closed)
**Created:** 2025-02-07 via Slack  |  **Requester:** Ananya Gupta  |  **Assigned to:** Vikram Rao

**Description:** Ananya Gupta (Product Management) reported an issue via Slack related to 'Ad-hoc Data Analysis Request Procedure'. Category: Analytics. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Ad-hoc Data Analysis Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-DATA-006 to resolve. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-006

---

## TCK3-DATA-00150 — Data Engineering (P3, In Progress)
**Created:** 2025-02-07 via Phone  |  **Requester:** Nidhi Pillai  |  **Assigned to:** Tanya Iyer

**Description:** Nidhi Pillai (Human Resources) reported an issue via Phone related to 'Data Warehouse Schema Change Procedure'. Category: Data Engineering. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Warehouse Schema Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-DATA-009

---

## TCK3-DATA-00103 — Onboarding (P4, Closed)
**Created:** 2025-02-11 via Phone  |  **Requester:** Divya Gupta  |  **Assigned to:** Gaurav Mehta

**Description:** Divya Gupta (QA / Testing) reported an issue via Phone related to 'Data Onboarding for New Team Members'. Category: Onboarding. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Onboarding for New Team Members', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-DATA-011 to resolve. HR notifies the relevant department and the MK-DataLake owner ahead of the employee's start or end date. the Data Manager prepares the required Data Onboarding, including MK-DataLake access, SQL style guide, and a shadowing assignment. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Director of Data & Analytics verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-DATA-011

---

## TCK3-DATA-00084 — Data Governance (P3, Resolved)
**Created:** 2025-02-25 via Slack  |  **Requester:** Kabir Reddy  |  **Assigned to:** Preeti Mehta

**Description:** Kabir Reddy (QA / Testing) reported an issue via Slack related to 'Data Retention and Deletion Procedure'. Category: Data Governance. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Data Retention and Deletion Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-DATA-008 to resolve. The review is scheduled in advance and stakeholders are notified through MK-DataLake. the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal. The review team examines the Data Retention Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-DATA-008

---

## TCK3-DATA-00097 — Reporting (P3, Closed)
**Created:** 2025-02-27 via Live Chat  |  **Requester:** Vikram Bose  |  **Assigned to:** Isha Iyer

**Description:** Vikram Bose (IT Support / Information Technology) reported an issue via Live Chat related to 'Dashboard/Report Request Procedure'. Category: Reporting. Logged against MK-DataLake.

**Investigation:** The assigned specialist reviewed the MK-DataLake record, confirmed the reported symptom against 'Dashboard/Report Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-DATA-002 to resolve. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-DATA-002

---
