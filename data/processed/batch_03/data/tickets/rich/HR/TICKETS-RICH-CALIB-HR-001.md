# Human Resources — Rich Historical Ticket Archive (calib, Page 1)

## TCK3-HR-00015 — Mobility (P3, In Progress)
**Created:** 2024-07-11 via Walk-in  |  **Requester:** Ritika Desai  |  **Assigned to:** Divya Chowdhury

**Description:** Ritika Desai (Legal & Compliance) reported an issue via Walk-in related to 'Internal Job Transfer Procedure'. Category: Mobility. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Internal Job Transfer Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-006

---

## TCK3-HR-00002 — Compensation (P4, Closed)
**Created:** 2024-08-19 via Slack  |  **Requester:** Siddharth Iyer  |  **Assigned to:** Neel Bose

**Description:** Siddharth Iyer (Management / Leadership) reported an issue via Slack related to 'Compensation Revision Procedure'. Category: Compensation. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Compensation Revision Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-HR-014 to resolve. the Reporting Manager logs into MK-HRMS and navigates to the 'Compensation Revision' section. the Reporting Manager selects 'New Compensation Revision' and enters the required details, including performance rating, market benchmarking data, and budget availability. the Reporting Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Reporting Manager submits the Compensation Revision; MK-HRMS automatically routes it to the HR Director for review. The HR Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-014

---

## TCK3-HR-00010 — Recruitment (P3, Closed)
**Created:** 2024-11-02 via Slack  |  **Requester:** Yash Bose  |  **Assigned to:** Naveen Singh

**Description:** Yash Bose (Software Engineering / Development) reported an issue via Slack related to 'Background Verification Procedure'. Category: Recruitment. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Background Verification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-HR-015 to resolve. the HR Executive confirms eligibility and prerequisites: education, employment history, and criminal record checks via the approved vendor. the HR Executive raises a request in MK-HRMS specifying exactly which Background Check is required. The HR Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Background Check in the relevant system. the HR Executive is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-HR-015

---

## TCK3-HR-00016 — Recruitment (P3, Resolved)
**Created:** 2024-12-13 via Live Chat  |  **Requester:** Nisha Chauhan  |  **Assigned to:** Swati Verma

**Description:** Nisha Chauhan (IT Support / Information Technology) reported an issue via Live Chat related to 'Recruitment Requisition Procedure'. Category: Recruitment. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Recruitment Requisition Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-HR-008 to resolve. the Hiring Manager logs into MK-HRMS and navigates to the 'Requisition' section. the Hiring Manager selects 'New Requisition' and enters the required details, including headcount justification, budget approval, and job description. the Hiring Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Hiring Manager submits the Requisition; MK-HRMS automatically routes it to the HR Director for review. The HR Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-008

---

## TCK3-HR-00017 — Compensation (P3, Resolved)
**Created:** 2024-12-24 via Live Chat  |  **Requester:** Divya Rao  |  **Assigned to:** Isha Agarwal

**Description:** Divya Rao (IT Support / Information Technology) reported an issue via Live Chat related to 'Compensation Revision Procedure'. Category: Compensation. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Compensation Revision Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-HR-014 to resolve. the Reporting Manager logs into MK-HRMS and navigates to the 'Compensation Revision' section. the Reporting Manager selects 'New Compensation Revision' and enters the required details, including performance rating, market benchmarking data, and budget availability. the Reporting Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Reporting Manager submits the Compensation Revision; MK-HRMS automatically routes it to the HR Director for review. The HR Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-014

---

## TCK3-HR-00005 — Employee Relations (P3, Resolved)
**Created:** 2025-01-05 via Live Chat  |  **Requester:** Harsh Malhotra  |  **Assigned to:** Swati Verma

**Description:** Harsh Malhotra (Procurement / Purchasing) reported an issue via Live Chat related to 'Employee Conduct / Disciplinary Procedure'. Category: Employee Relations. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Employee Conduct / Disciplinary Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-HR-013 to resolve. the HR Business Partner confirms the exact symptom, when it started, and whether it affects one system or several. the HR Business Partner performs the standard first-line check: documenting the incident with witness statements where relevant. If the issue persists, the HR Business Partner applies the documented workaround for this issue type. the HR Business Partner checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the HR Business Partner raises a ticket in MK-HRMS categorised under 'Disciplinary Case', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-HR-013

---

## TCK3-HR-00014 — Onboarding (P4, Resolved)
**Created:** 2025-01-10 via Live Chat  |  **Requester:** Nidhi Bhatt  |  **Assigned to:** Nidhi Pillai

**Description:** Nidhi Bhatt (Project Management / PMO) reported an issue via Live Chat related to 'New Employee Onboarding Procedure'. Category: Onboarding. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'New Employee Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-HR-002 to resolve. HR notifies the relevant department and the MK-HRMS owner ahead of the employee's start or end date. the HR Executive prepares the required Onboarding Plan, including offer letter acknowledgment, document collection, and day-1 induction schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The HR Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-HR-002

---

## TCK3-HR-00011 — Career Development (P3, Resolved)
**Created:** 2025-05-24 via Live Chat  |  **Requester:** Vikram Mehta  |  **Assigned to:** Priya Bhatt

**Description:** Vikram Mehta (DevOps & Cloud) reported an issue via Live Chat related to 'Promotion Nomination Procedure'. Category: Career Development. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Promotion Nomination Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-HR-005 to resolve. the Reporting Manager logs into MK-HRMS and navigates to the 'Promotion Nomination' section. the Reporting Manager selects 'New Promotion Nomination' and enters the required details, including performance history, readiness assessment, and business justification. the Reporting Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Reporting Manager submits the Promotion Nomination; MK-HRMS automatically routes it to the HR Director for review. The HR Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-005

---

## TCK3-HR-00008 — Recruitment (P3, Closed)
**Created:** 2025-09-13 via Phone  |  **Requester:** Kabir Reddy  |  **Assigned to:** Siddharth Reddy

**Description:** Kabir Reddy (QA / Testing) reported an issue via Phone related to 'Background Verification Procedure'. Category: Recruitment. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Background Verification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-HR-015 to resolve. the HR Executive confirms eligibility and prerequisites: education, employment history, and criminal record checks via the approved vendor. the HR Executive raises a request in MK-HRMS specifying exactly which Background Check is required. The HR Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Background Check in the relevant system. the HR Executive is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-HR-015

---

## TCK3-HR-00007 — Recruitment (P4, Resolved)
**Created:** 2025-09-29 via Slack  |  **Requester:** Vikram Bhatt  |  **Assigned to:** Neel Bose

**Description:** Vikram Bhatt (Human Resources) reported an issue via Slack related to 'Employee Referral Program Procedure'. Category: Recruitment. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Employee Referral Program Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-HR-016 to resolve. the employee logs into MK-HRMS and navigates to the 'Referral Submission' section. the employee selects 'New Referral Submission' and enters the required details, including the candidate's resume and the open requisition ID being referred against. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Referral Submission; MK-HRMS automatically routes it to the HR Executive for review. The HR Executive reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-016

---

## TCK3-HR-00006 — Internship (P3, Closed)
**Created:** 2025-12-17 via Email  |  **Requester:** Bhavna Rao  |  **Assigned to:** Nidhi Pillai

**Description:** Bhavna Rao (Data & Analytics) reported an issue via Email related to 'Internship Evaluation and Completion Procedure'. Category: Internship. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Internship Evaluation and Completion Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-HR-011 to resolve. The review is scheduled in advance and stakeholders are notified through MK-HRMS. the assigned Mentor gathers the required data and documents, including project outcomes, attendance record, and mentor feedback. The review team examines the Internship Evaluation against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The HR Business Partner discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-HR-011

---

## TCK3-HR-00001 — Onboarding (P2, Closed)
**Created:** 2026-03-09 via Email  |  **Requester:** Kabir Chauhan  |  **Assigned to:** Vikram Bhatt

**Description:** Kabir Chauhan (Sales) reported an issue via Email related to 'New Employee Onboarding Procedure'. Category: Onboarding. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'New Employee Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-HR-002 to resolve. HR notifies the relevant department and the MK-HRMS owner ahead of the employee's start or end date. the HR Executive prepares the required Onboarding Plan, including offer letter acknowledgment, document collection, and day-1 induction schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The HR Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-HR-002

---

## TCK3-HR-00018 — Recruitment (P3, Closed)
**Created:** 2026-03-10 via Email  |  **Requester:** Rohan Sharma  |  **Assigned to:** Siddharth Reddy

**Description:** Rohan Sharma (Administration / Facilities) reported an issue via Email related to 'Offer Letter Generation Procedure'. Category: Recruitment. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Offer Letter Generation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-HR-009 to resolve. the HR Executive confirms eligibility and prerequisites: verifying compensation band approval and background check clearance. the HR Executive raises a request in MK-HRMS specifying exactly which Offer Letter is required. The HR Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Offer Letter in the relevant system. the HR Executive is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-HR-009

---

## TCK3-HR-00012 — Recruitment (P3, Resolved)
**Created:** 2026-04-29 via Walk-in  |  **Requester:** Swati Verma  |  **Assigned to:** Naveen Singh

**Description:** Swati Verma (Human Resources) reported an issue via Walk-in related to 'Background Verification Procedure'. Category: Recruitment. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Background Verification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-HR-015 to resolve. the HR Executive confirms eligibility and prerequisites: education, employment history, and criminal record checks via the approved vendor. the HR Executive raises a request in MK-HRMS specifying exactly which Background Check is required. The HR Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Background Check in the relevant system. the HR Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-HR-015

---

## TCK3-HR-00009 — Leave Management (P2, Resolved)
**Created:** 2026-05-14 via Portal  |  **Requester:** Bhavna Pillai  |  **Assigned to:** Siddharth Reddy

**Description:** Bhavna Pillai (Sales) reported an issue via Portal related to 'Leave Application Procedure'. Category: Leave Management. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Leave Application Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-HR-001 to resolve. the employee logs into MK-HRMS and navigates to the 'Leave Application' section. the employee selects 'New Leave Application' and enters the required details, including leave type, dates, and reason. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Leave Application; MK-HRMS automatically routes it to the Reporting Manager for review. The Reporting Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-001

---

## TCK3-HR-00004 — Performance Management (P4, Resolved)
**Created:** 2026-05-15 via Slack  |  **Requester:** Ananya Menon  |  **Assigned to:** Naveen Singh

**Description:** Ananya Menon (Human Resources) reported an issue via Slack related to 'Performance Review Cycle Procedure'. Category: Performance Management. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Performance Review Cycle Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-HR-004 to resolve. The review is scheduled in advance and stakeholders are notified through MK-HRMS. the Reporting Manager gathers the required data and documents, including self-assessment, manager assessment, and calibration discussion. The review team examines the Performance Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The HR Business Partner discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-HR-004

---

## TCK3-HR-00020 — Attendance (P1, Resolved)
**Created:** 2026-05-30 via Phone  |  **Requester:** Aman Nair  |  **Assigned to:** Siddharth Reddy

**Description:** Aman Nair (Finance & Accounting) reported an issue via Phone related to 'Attendance Regularization Procedure'. Category: Attendance. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Attendance Regularization Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-HR-012 to resolve. the employee logs into MK-HRMS and navigates to the 'Attendance Regularization' section. the employee selects 'New Attendance Regularization' and enters the required details, including the date, reason for missed punch, and supporting evidence if any. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Attendance Regularization; MK-HRMS automatically routes it to the Reporting Manager for review. The Reporting Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-012

---

## TCK3-HR-00013 — Recruitment (P1, Resolved)
**Created:** 2026-06-08 via Slack  |  **Requester:** Harsh Joshi  |  **Assigned to:** Swati Verma

**Description:** Harsh Joshi (Marketing) reported an issue via Slack related to 'Recruitment Requisition Procedure'. Category: Recruitment. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Recruitment Requisition Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-HR-008 to resolve. the Hiring Manager logs into MK-HRMS and navigates to the 'Requisition' section. the Hiring Manager selects 'New Requisition' and enters the required details, including headcount justification, budget approval, and job description. the Hiring Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Hiring Manager submits the Requisition; MK-HRMS automatically routes it to the HR Director for review. The HR Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-008

---

## TCK3-HR-00019 — Onboarding (P3, Resolved)
**Created:** 2026-07-13 via Slack  |  **Requester:** Vikram Mehta  |  **Assigned to:** Isha Agarwal

**Description:** Vikram Mehta (DevOps & Cloud) reported an issue via Slack related to 'New Employee Onboarding Procedure'. Category: Onboarding. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'New Employee Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-HR-002 to resolve. HR notifies the relevant department and the MK-HRMS owner ahead of the employee's start or end date. the HR Executive prepares the required Onboarding Plan, including offer letter acknowledgment, document collection, and day-1 induction schedule. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The HR Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-HR-002

---

## TCK3-HR-00003 — Mobility (P3, Resolved)
**Created:** 2026-08-14 via Phone  |  **Requester:** Sneha Reddy  |  **Assigned to:** Ritika Singh

**Description:** Sneha Reddy (QA / Testing) reported an issue via Phone related to 'Internal Job Transfer Procedure'. Category: Mobility. Logged against MK-HRMS.

**Investigation:** The assigned specialist reviewed the MK-HRMS record, confirmed the reported symptom against 'Internal Job Transfer Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-HR-006 to resolve. the employee logs into MK-HRMS and navigates to the 'Transfer Request' section. the employee selects 'New Transfer Request' and enters the required details, including current manager no-objection and target team acceptance. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Transfer Request; MK-HRMS automatically routes it to the HR Business Partner for review. The HR Business Partner reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-HR-006

---
