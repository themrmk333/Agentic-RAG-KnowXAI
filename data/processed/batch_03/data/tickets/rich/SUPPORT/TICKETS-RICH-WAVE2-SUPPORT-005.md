# Customer Support / Helpdesk — Rich Historical Ticket Archive (wave2, Page 5)

## TCK3-SUPPORT-00057 — Ticket Management (P3, Resolved)
**Created:** 2025-08-21 via Slack  |  **Requester:** Nisha Chauhan  |  **Assigned to:** Alisha Gupta

**Description:** Nisha Chauhan (IT Support / Information Technology) reported an issue via Slack related to 'Customer Ticket Intake and Categorization'. Category: Ticket Management. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Ticket Intake and Categorization', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-SUPPORT-001 to resolve. the Customer Support Associate confirms eligibility and prerequisites: issue category, product area, and customer-reported severity. the Customer Support Associate raises a request in MK-SupportDesk specifying exactly which Support Ticket is required. The Support Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Support Ticket in the relevant system. the Customer Support Associate is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SUPPORT-001

---

## TCK3-SUPPORT-00107 — Billing Support (P4, Resolved)
**Created:** 2025-08-29 via Email  |  **Requester:** Vikram Bose  |  **Assigned to:** Aditya Nair

**Description:** Vikram Bose (IT Support / Information Technology) reported an issue via Email related to 'Customer Refund/Credit Request Procedure'. Category: Billing Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Refund/Credit Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SUPPORT-005 to resolve. the Customer Support Associate logs into MK-SupportDesk and navigates to the 'Refund Request' section. the Customer Support Associate selects 'New Refund Request' and enters the required details, including reason for refund, amount, and account history. the Customer Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Customer Support Associate submits the Refund Request; MK-SupportDesk automatically routes it to the Support Manager for review. The Support Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-005

---

## TCK3-SUPPORT-00087 — Onboarding (P2, Closed)
**Created:** 2025-09-20 via Live Chat  |  **Requester:** Tanya Mehta  |  **Assigned to:** Riya Joshi

**Description:** Tanya Mehta (Project Management / PMO) reported an issue via Live Chat related to 'Support Onboarding for New Hires'. Category: Onboarding. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Support Onboarding for New Hires', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-SUPPORT-012 to resolve. HR notifies the relevant department and the MK-SupportDesk owner ahead of the employee's start or end date. the Support Team Lead prepares the required Support Onboarding, including MK-SupportDesk access, product training, and shadowing live tickets. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Support Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SUPPORT-012

---

## TCK3-SUPPORT-00030 — SLA Management (P4, Resolved)
**Created:** 2025-10-01 via Live Chat  |  **Requester:** Swati Nair  |  **Assigned to:** Alisha Gupta

**Description:** Swati Nair (Finance & Accounting) reported an issue via Live Chat related to 'SLA Breach Handling Procedure'. Category: SLA Management. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'SLA Breach Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-SUPPORT-003 to resolve. the Support Team Lead confirms the exact symptom, when it started, and whether it affects one system or several. the Support Team Lead performs the standard first-line check: identifying the cause of delay and reassigning the ticket if needed. If the issue persists, the Support Team Lead applies the documented workaround for this issue type. the Support Team Lead checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Support Team Lead raises a ticket in MK-SupportDesk categorised under 'SLA Breach', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-003

---

## TCK3-SUPPORT-00075 — Customer Relations (P4, Resolved)
**Created:** 2025-10-09 via Email  |  **Requester:** Rohan Kapoor  |  **Assigned to:** Alisha Gupta

**Description:** Rohan Kapoor (Marketing) reported an issue via Email related to 'Customer Complaint Handling Procedure'. Category: Customer Relations. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Complaint Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-SUPPORT-015 to resolve. the Support Manager confirms the exact symptom, when it started, and whether it affects one system or several. the Support Manager performs the standard first-line check: acknowledging the complaint within 2 hours and assigning an owner. If the issue persists, the Support Manager applies the documented workaround for this issue type. the Support Manager checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Support Manager raises a ticket in MK-SupportDesk categorised under 'Formal Complaint', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-015

---

## TCK3-SUPPORT-00043 — Cross-team Handover (P3, Closed)
**Created:** 2025-10-12 via Portal  |  **Requester:** Dev Menon  |  **Assigned to:** Kabir Agarwal

**Description:** Dev Menon (Research & Development) reported an issue via Portal related to 'Bug Report Handover to Engineering'. Category: Cross-team Handover. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Bug Report Handover to Engineering', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SUPPORT-004 to resolve. the Senior Support Associate logs into MK-SupportDesk and navigates to the 'Bug Handover' section. the Senior Support Associate selects 'New Bug Handover' and enters the required details, including reproduction steps, logs, and customer impact assessment. the Senior Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Senior Support Associate submits the Bug Handover; MK-SupportDesk automatically routes it to the Support Manager for review. The Support Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-004

---

## TCK3-SUPPORT-00028 — Ticket Management (P4, Resolved)
**Created:** 2025-10-16 via Slack  |  **Requester:** Divya Malhotra  |  **Assigned to:** Swati Nair

**Description:** Divya Malhotra (Customer Support / Helpdesk) reported an issue via Slack related to 'Priority/Severity Reclassification Procedure'. Category: Ticket Management. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Priority/Severity Reclassification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SUPPORT-008 to resolve. the Customer Support Associate logs into MK-SupportDesk and navigates to the 'Severity Reclassification' section. the Customer Support Associate selects 'New Severity Reclassification' and enters the required details, including business impact justification for the requested change. the Customer Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Customer Support Associate submits the Severity Reclassification; MK-SupportDesk automatically routes it to the Support Team Lead for review. The Support Team Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-008

---

## TCK3-SUPPORT-00022 — Customer Retention (P3, Resolved)
**Created:** 2025-10-28 via Portal  |  **Requester:** Anjali Gupta  |  **Assigned to:** Alisha Gupta

**Description:** Anjali Gupta (Legal & Compliance) reported an issue via Portal related to 'Customer Churn Risk Flagging Procedure'. Category: Customer Retention. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Churn Risk Flagging Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-SUPPORT-011 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SupportDesk. the Support Team Lead gathers the required data and documents, including repeated escalations, negative sentiment, or usage decline. The review team examines the Churn Risk Flag against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Customer Experience Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SUPPORT-011

---

## TCK3-SUPPORT-00044 — Escalation (P3, Resolved)
**Created:** 2025-10-28 via Live Chat  |  **Requester:** Rohan Agarwal  |  **Assigned to:** Sneha Singh

**Description:** Rohan Agarwal (Cybersecurity / Information Security) reported an issue via Live Chat related to 'Customer Ticket Escalation Procedure'. Category: Escalation. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Ticket Escalation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-SUPPORT-002 to resolve. the Customer Support Associate confirms the exact symptom, when it started, and whether it affects one system or several. the Customer Support Associate performs the standard first-line check: reviewing the SLA timer and customer tier in MK-SupportDesk. If the issue persists, the Customer Support Associate applies the documented workaround for this issue type. the Customer Support Associate checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Customer Support Associate raises a ticket in MK-SupportDesk categorised under 'Ticket Escalation', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-002

---

## TCK3-SUPPORT-00119 — Billing Support (P4, Resolved)
**Created:** 2025-10-29 via Portal  |  **Requester:** Sneha Singh  |  **Assigned to:** Divya Malhotra

**Description:** Sneha Singh (Customer Support / Helpdesk) reported an issue via Portal related to 'Customer Refund/Credit Request Procedure'. Category: Billing Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Refund/Credit Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SUPPORT-005 to resolve. the Customer Support Associate logs into MK-SupportDesk and navigates to the 'Refund Request' section. the Customer Support Associate selects 'New Refund Request' and enters the required details, including reason for refund, amount, and account history. the Customer Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Customer Support Associate submits the Refund Request; MK-SupportDesk automatically routes it to the Support Manager for review. The Support Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-005

---

## TCK3-SUPPORT-00136 — Customer Relations (P4, Resolved)
**Created:** 2025-11-04 via Walk-in  |  **Requester:** Bhavna Rao  |  **Assigned to:** Divya Malhotra

**Description:** Bhavna Rao (Data & Analytics) reported an issue via Walk-in related to 'Customer Complaint Handling Procedure'. Category: Customer Relations. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Complaint Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-SUPPORT-015 to resolve. the Support Manager confirms the exact symptom, when it started, and whether it affects one system or several. the Support Manager performs the standard first-line check: acknowledging the complaint within 2 hours and assigning an owner. If the issue persists, the Support Manager applies the documented workaround for this issue type. the Support Manager checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Support Manager raises a ticket in MK-SupportDesk categorised under 'Formal Complaint', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-015

---

## TCK3-SUPPORT-00035 — Ticket Management (P3, Resolved)
**Created:** 2025-11-05 via Live Chat  |  **Requester:** Divya Nair  |  **Assigned to:** Alisha Gupta

**Description:** Divya Nair (Management / Leadership) reported an issue via Live Chat related to 'Customer Ticket Intake and Categorization'. Category: Ticket Management. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Ticket Intake and Categorization', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-SUPPORT-001 to resolve. the Customer Support Associate confirms eligibility and prerequisites: issue category, product area, and customer-reported severity. the Customer Support Associate raises a request in MK-SupportDesk specifying exactly which Support Ticket is required. The Support Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Support Ticket in the relevant system. the Customer Support Associate is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SUPPORT-001

---

## TCK3-SUPPORT-00061 — Onboarding (P4, In Progress)
**Created:** 2025-11-17 via Walk-in  |  **Requester:** Divya Rao  |  **Assigned to:** Divya Malhotra

**Description:** Divya Rao (Management / Leadership) reported an issue via Walk-in related to 'Support Onboarding for New Hires'. Category: Onboarding. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Support Onboarding for New Hires', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SUPPORT-012

---

## TCK3-SUPPORT-00025 — Customer Satisfaction (P3, Resolved)
**Created:** 2025-11-19 via Phone  |  **Requester:** Varun Iyer  |  **Assigned to:** Tanya Sharma

**Description:** Varun Iyer (Legal & Compliance) reported an issue via Phone related to 'Customer Satisfaction (CSAT) Follow-up Procedure'. Category: Customer Satisfaction. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Satisfaction (CSAT) Follow-up Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-SUPPORT-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SupportDesk. the Support Team Lead gathers the required data and documents, including reviewing low CSAT scores and the associated ticket transcript. The review team examines the CSAT Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Support Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SUPPORT-007

---

## TCK3-SUPPORT-00049 — Customer Onboarding (P3, Resolved)
**Created:** 2025-11-19 via Slack  |  **Requester:** Riya Joshi  |  **Assigned to:** Aditya Nair

**Description:** Riya Joshi (Customer Support / Helpdesk) reported an issue via Slack related to 'Customer Onboarding Support Procedure'. Category: Customer Onboarding. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Onboarding Support Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-SUPPORT-009 to resolve. the Customer Support Associate confirms eligibility and prerequisites: walking the new customer through setup and key features. the Customer Support Associate raises a request in MK-SupportDesk specifying exactly which Customer Onboarding Session is required. The Support Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Customer Onboarding Session in the relevant system. the Customer Support Associate is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SUPPORT-009

---

## TCK3-SUPPORT-00140 — Ticket Management (P3, Resolved)
**Created:** 2025-11-20 via Slack  |  **Requester:** Sahil Chowdhury  |  **Assigned to:** Alisha Gupta

**Description:** Sahil Chowdhury (Legal & Compliance) reported an issue via Slack related to 'Priority/Severity Reclassification Procedure'. Category: Ticket Management. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Priority/Severity Reclassification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SUPPORT-008 to resolve. the Customer Support Associate logs into MK-SupportDesk and navigates to the 'Severity Reclassification' section. the Customer Support Associate selects 'New Severity Reclassification' and enters the required details, including business impact justification for the requested change. the Customer Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Customer Support Associate submits the Severity Reclassification; MK-SupportDesk automatically routes it to the Support Team Lead for review. The Support Team Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-008

---

## TCK3-SUPPORT-00135 — Live Support (P2, Resolved)
**Created:** 2025-11-26 via Phone  |  **Requester:** Yash Sharma  |  **Assigned to:** Kavya Kapoor

**Description:** Yash Sharma (Administration / Facilities) reported an issue via Phone related to 'Live Chat Support Procedure'. Category: Live Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Live Chat Support Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-SUPPORT-013 to resolve. the Customer Support Associate confirms eligibility and prerequisites: using approved canned responses while personalising the greeting. the Customer Support Associate raises a request in MK-SupportDesk specifying exactly which Live Chat Session is required. The Support Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Live Chat Session in the relevant system. the Customer Support Associate is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SUPPORT-013

---

## TCK3-SUPPORT-00034 — Cross-team Handover (P1, Resolved)
**Created:** 2025-11-27 via Slack  |  **Requester:** Rahul Menon  |  **Assigned to:** Alisha Gupta

**Description:** Rahul Menon (DevOps & Cloud) reported an issue via Slack related to 'Bug Report Handover to Engineering'. Category: Cross-team Handover. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Bug Report Handover to Engineering', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SUPPORT-004 to resolve. the Senior Support Associate logs into MK-SupportDesk and navigates to the 'Bug Handover' section. the Senior Support Associate selects 'New Bug Handover' and enters the required details, including reproduction steps, logs, and customer impact assessment. the Senior Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Senior Support Associate submits the Bug Handover; MK-SupportDesk automatically routes it to the Support Manager for review. The Support Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-004

---

## TCK3-SUPPORT-00023 — Onboarding (P4, Resolved)
**Created:** 2025-11-28 via Live Chat  |  **Requester:** Anjali Iyer  |  **Assigned to:** Kavya Kapoor

**Description:** Anjali Iyer (Procurement / Purchasing) reported an issue via Live Chat related to 'Support Onboarding for New Hires'. Category: Onboarding. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Support Onboarding for New Hires', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-SUPPORT-012 to resolve. HR notifies the relevant department and the MK-SupportDesk owner ahead of the employee's start or end date. the Support Team Lead prepares the required Support Onboarding, including MK-SupportDesk access, product training, and shadowing live tickets. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Support Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SUPPORT-012

---

## TCK3-SUPPORT-00033 — Billing Support (P4, Resolved)
**Created:** 2025-12-03 via Slack  |  **Requester:** Ritika Agarwal  |  **Assigned to:** Nisha Bose

**Description:** Ritika Agarwal (Project Management / PMO) reported an issue via Slack related to 'Customer Refund/Credit Request Procedure'. Category: Billing Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Refund/Credit Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-SUPPORT-005 to resolve. the Customer Support Associate logs into MK-SupportDesk and navigates to the 'Refund Request' section. the Customer Support Associate selects 'New Refund Request' and enters the required details, including reason for refund, amount, and account history. the Customer Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Customer Support Associate submits the Refund Request; MK-SupportDesk automatically routes it to the Support Manager for review. The Support Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-005

---
