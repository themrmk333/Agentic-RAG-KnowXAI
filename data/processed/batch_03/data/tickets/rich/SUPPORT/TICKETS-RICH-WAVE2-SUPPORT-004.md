# Customer Support / Helpdesk — Rich Historical Ticket Archive (wave2, Page 4)

## TCK3-SUPPORT-00068 — Customer Relations (P4, Resolved)
**Created:** 2025-03-26 via Phone  |  **Requester:** Varun Rao  |  **Assigned to:** Kavya Desai

**Description:** Varun Rao (Management / Leadership) reported an issue via Phone related to 'Customer Complaint Handling Procedure'. Category: Customer Relations. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Complaint Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-SUPPORT-015 to resolve. the Support Manager confirms the exact symptom, when it started, and whether it affects one system or several. the Support Manager performs the standard first-line check: acknowledging the complaint within 2 hours and assigning an owner. If the issue persists, the Support Manager applies the documented workaround for this issue type. the Support Manager checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Support Manager raises a ticket in MK-SupportDesk categorised under 'Formal Complaint', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-015

---

## TCK3-SUPPORT-00106 — On-call Support (P3, Resolved)
**Created:** 2025-04-18 via Live Chat  |  **Requester:** Swati Verma  |  **Assigned to:** Kabir Agarwal

**Description:** Swati Verma (Human Resources) reported an issue via Live Chat related to 'After-hours / On-call Support Procedure'. Category: On-call Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'After-hours / On-call Support Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-SUPPORT-010 to resolve. the on-call Support Associate confirms the exact symptom, when it started, and whether it affects one system or several. the on-call Support Associate performs the standard first-line check: checking whether the issue meets the after-hours P1 criteria. If the issue persists, the on-call Support Associate applies the documented workaround for this issue type. the on-call Support Associate checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call Support Associate raises a ticket in MK-SupportDesk categorised under 'After-hours Ticket', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-010

---

## TCK3-SUPPORT-00094 — Live Support (P4, Resolved)
**Created:** 2025-04-27 via Slack  |  **Requester:** Simran Verma  |  **Assigned to:** Swati Nair

**Description:** Simran Verma (IT Support / Information Technology) reported an issue via Slack related to 'Live Chat Support Procedure'. Category: Live Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Live Chat Support Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-SUPPORT-013 to resolve. the Customer Support Associate confirms eligibility and prerequisites: using approved canned responses while personalising the greeting. the Customer Support Associate raises a request in MK-SupportDesk specifying exactly which Live Chat Session is required. The Support Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Live Chat Session in the relevant system. the Customer Support Associate is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SUPPORT-013

---

## TCK3-SUPPORT-00024 — Cross-team Handover (P3, Closed)
**Created:** 2025-04-28 via Phone  |  **Requester:** Kavya Bhatt  |  **Assigned to:** Aditya Nair

**Description:** Kavya Bhatt (Procurement / Purchasing) reported an issue via Phone related to 'Bug Report Handover to Engineering'. Category: Cross-team Handover. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Bug Report Handover to Engineering', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SUPPORT-004 to resolve. the Senior Support Associate logs into MK-SupportDesk and navigates to the 'Bug Handover' section. the Senior Support Associate selects 'New Bug Handover' and enters the required details, including reproduction steps, logs, and customer impact assessment. the Senior Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Senior Support Associate submits the Bug Handover; MK-SupportDesk automatically routes it to the Support Manager for review. The Support Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-004

---

## TCK3-SUPPORT-00056 — Onboarding (P2, Resolved)
**Created:** 2025-04-28 via Email  |  **Requester:** Gaurav Menon  |  **Assigned to:** Kabir Agarwal

**Description:** Gaurav Menon (DevOps & Cloud) reported an issue via Email related to 'Support Onboarding for New Hires'. Category: Onboarding. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Support Onboarding for New Hires', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-SUPPORT-012 to resolve. HR notifies the relevant department and the MK-SupportDesk owner ahead of the employee's start or end date. the Support Team Lead prepares the required Support Onboarding, including MK-SupportDesk access, product training, and shadowing live tickets. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Support Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SUPPORT-012

---

## TCK3-SUPPORT-00090 — Cross-team Handover (P3, Resolved)
**Created:** 2025-04-29 via Slack  |  **Requester:** Neel Sharma  |  **Assigned to:** Ritika Agarwal

**Description:** Neel Sharma (Software Engineering / Development) reported an issue via Slack related to 'Bug Report Handover to Engineering'. Category: Cross-team Handover. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Bug Report Handover to Engineering', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SUPPORT-004 to resolve. the Senior Support Associate logs into MK-SupportDesk and navigates to the 'Bug Handover' section. the Senior Support Associate selects 'New Bug Handover' and enters the required details, including reproduction steps, logs, and customer impact assessment. the Senior Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Senior Support Associate submits the Bug Handover; MK-SupportDesk automatically routes it to the Support Manager for review. The Support Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-004

---

## TCK3-SUPPORT-00151 — Escalation (P4, Resolved)
**Created:** 2025-05-07 via Walk-in  |  **Requester:** Aman Menon  |  **Assigned to:** Nisha Bose

**Description:** Aman Menon (DevOps & Cloud) reported an issue via Walk-in related to 'Customer Ticket Escalation Procedure'. Category: Escalation. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Ticket Escalation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-SUPPORT-002 to resolve. the Customer Support Associate confirms the exact symptom, when it started, and whether it affects one system or several. the Customer Support Associate performs the standard first-line check: reviewing the SLA timer and customer tier in MK-SupportDesk. If the issue persists, the Customer Support Associate applies the documented workaround for this issue type. the Customer Support Associate checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Customer Support Associate raises a ticket in MK-SupportDesk categorised under 'Ticket Escalation', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-002

---

## TCK3-SUPPORT-00091 — Live Support (P2, In Progress)
**Created:** 2025-05-10 via Live Chat  |  **Requester:** Sahil Kapoor  |  **Assigned to:** Kavya Desai

**Description:** Sahil Kapoor (Sales) reported an issue via Live Chat related to 'Live Chat Support Procedure'. Category: Live Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Live Chat Support Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SUPPORT-013

---

## TCK3-SUPPORT-00130 — Quality Assurance (P3, Resolved)
**Created:** 2025-05-10 via Email  |  **Requester:** Divya Chowdhury  |  **Assigned to:** Swati Nair

**Description:** Divya Chowdhury (Human Resources) reported an issue via Email related to 'Support Quality Audit Procedure'. Category: Quality Assurance. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Support Quality Audit Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-SUPPORT-014 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SupportDesk. the Support Manager gathers the required data and documents, including sampling closed tickets against the quality rubric. The review team examines the Quality Audit against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Customer Experience Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SUPPORT-014

---

## TCK3-SUPPORT-00040 — On-call Support (P3, Resolved)
**Created:** 2025-05-11 via Phone  |  **Requester:** Harsh Nair  |  **Assigned to:** Nisha Bose

**Description:** Harsh Nair (Cybersecurity / Information Security) reported an issue via Phone related to 'After-hours / On-call Support Procedure'. Category: On-call Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'After-hours / On-call Support Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-SUPPORT-010 to resolve. the on-call Support Associate confirms the exact symptom, when it started, and whether it affects one system or several. the on-call Support Associate performs the standard first-line check: checking whether the issue meets the after-hours P1 criteria. If the issue persists, the on-call Support Associate applies the documented workaround for this issue type. the on-call Support Associate checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call Support Associate raises a ticket in MK-SupportDesk categorised under 'After-hours Ticket', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-010

---

## TCK3-SUPPORT-00048 — Knowledge Management (P4, Resolved)
**Created:** 2025-05-17 via Live Chat  |  **Requester:** Gaurav Sharma  |  **Assigned to:** Kavya Kapoor

**Description:** Gaurav Sharma (IT Support / Information Technology) reported an issue via Live Chat related to 'Knowledge Base Article Creation Procedure'. Category: Knowledge Management. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Knowledge Base Article Creation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-SUPPORT-006 to resolve. the Senior Support Associate confirms eligibility and prerequisites: a clear step-by-step resolution based on a recurring ticket theme. the Senior Support Associate raises a request in MK-SupportDesk specifying exactly which KB Article is required. The Support Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the KB Article in the relevant system. the Senior Support Associate is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SUPPORT-006

---

## TCK3-SUPPORT-00102 — Customer Relations (P4, Resolved)
**Created:** 2025-05-24 via Email  |  **Requester:** Karan Bhatt  |  **Assigned to:** Meera Chauhan

**Description:** Karan Bhatt (DevOps & Cloud) reported an issue via Email related to 'Customer Complaint Handling Procedure'. Category: Customer Relations. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Complaint Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-SUPPORT-015 to resolve. the Support Manager confirms the exact symptom, when it started, and whether it affects one system or several. the Support Manager performs the standard first-line check: acknowledging the complaint within 2 hours and assigning an owner. If the issue persists, the Support Manager applies the documented workaround for this issue type. the Support Manager checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Support Manager raises a ticket in MK-SupportDesk categorised under 'Formal Complaint', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-015

---

## TCK3-SUPPORT-00139 — Escalation (P3, Resolved)
**Created:** 2025-05-29 via Phone  |  **Requester:** Simran Verma  |  **Assigned to:** Aditya Nair

**Description:** Simran Verma (IT Support / Information Technology) reported an issue via Phone related to 'Customer Ticket Escalation Procedure'. Category: Escalation. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Ticket Escalation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-SUPPORT-002 to resolve. the Customer Support Associate confirms the exact symptom, when it started, and whether it affects one system or several. the Customer Support Associate performs the standard first-line check: reviewing the SLA timer and customer tier in MK-SupportDesk. If the issue persists, the Customer Support Associate applies the documented workaround for this issue type. the Customer Support Associate checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Customer Support Associate raises a ticket in MK-SupportDesk categorised under 'Ticket Escalation', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-002

---

## TCK3-SUPPORT-00066 — On-call Support (P3, Resolved)
**Created:** 2025-06-25 via Portal  |  **Requester:** Divya Bose  |  **Assigned to:** Tanya Sharma

**Description:** Divya Bose (QA / Testing) reported an issue via Portal related to 'After-hours / On-call Support Procedure'. Category: On-call Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'After-hours / On-call Support Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-SUPPORT-010 to resolve. the on-call Support Associate confirms the exact symptom, when it started, and whether it affects one system or several. the on-call Support Associate performs the standard first-line check: checking whether the issue meets the after-hours P1 criteria. If the issue persists, the on-call Support Associate applies the documented workaround for this issue type. the on-call Support Associate checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the on-call Support Associate raises a ticket in MK-SupportDesk categorised under 'After-hours Ticket', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SUPPORT-010

---

## TCK3-SUPPORT-00071 — Cross-team Handover (P4, Resolved)
**Created:** 2025-06-25 via Live Chat  |  **Requester:** Manoj Chauhan  |  **Assigned to:** Kavya Kapoor

**Description:** Manoj Chauhan (Administration / Facilities) reported an issue via Live Chat related to 'Bug Report Handover to Engineering'. Category: Cross-team Handover. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Bug Report Handover to Engineering', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SUPPORT-004 to resolve. the Senior Support Associate logs into MK-SupportDesk and navigates to the 'Bug Handover' section. the Senior Support Associate selects 'New Bug Handover' and enters the required details, including reproduction steps, logs, and customer impact assessment. the Senior Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Senior Support Associate submits the Bug Handover; MK-SupportDesk automatically routes it to the Support Manager for review. The Support Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-004

---

## TCK3-SUPPORT-00115 — Billing Support (P3, Closed)
**Created:** 2025-07-11 via Portal  |  **Requester:** Sahil Chowdhury  |  **Assigned to:** Tanya Sharma

**Description:** Sahil Chowdhury (Legal & Compliance) reported an issue via Portal related to 'Customer Refund/Credit Request Procedure'. Category: Billing Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Refund/Credit Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SUPPORT-005 to resolve. the Customer Support Associate logs into MK-SupportDesk and navigates to the 'Refund Request' section. the Customer Support Associate selects 'New Refund Request' and enters the required details, including reason for refund, amount, and account history. the Customer Support Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Customer Support Associate submits the Refund Request; MK-SupportDesk automatically routes it to the Support Manager for review. The Support Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SUPPORT-005

---

## TCK3-SUPPORT-00109 — Customer Onboarding (P3, Resolved)
**Created:** 2025-07-12 via Email  |  **Requester:** Siddharth Verma  |  **Assigned to:** Kavya Kapoor

**Description:** Siddharth Verma (Data & Analytics) reported an issue via Email related to 'Customer Onboarding Support Procedure'. Category: Customer Onboarding. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Onboarding Support Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-SUPPORT-009 to resolve. the Customer Support Associate confirms eligibility and prerequisites: walking the new customer through setup and key features. the Customer Support Associate raises a request in MK-SupportDesk specifying exactly which Customer Onboarding Session is required. The Support Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Customer Onboarding Session in the relevant system. the Customer Support Associate is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SUPPORT-009

---

## TCK3-SUPPORT-00079 — Live Support (P4, In Progress)
**Created:** 2025-07-30 via Walk-in  |  **Requester:** Anjali Iyer  |  **Assigned to:** Aditya Nair

**Description:** Anjali Iyer (Procurement / Purchasing) reported an issue via Walk-in related to 'Live Chat Support Procedure'. Category: Live Support. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Live Chat Support Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SUPPORT-013

---

## TCK3-SUPPORT-00060 — Customer Retention (P3, Closed)
**Created:** 2025-07-31 via Portal  |  **Requester:** Yash Mehta  |  **Assigned to:** Kavya Desai

**Description:** Yash Mehta (Software Engineering / Development) reported an issue via Portal related to 'Customer Churn Risk Flagging Procedure'. Category: Customer Retention. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Customer Churn Risk Flagging Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-SUPPORT-011 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SupportDesk. the Support Team Lead gathers the required data and documents, including repeated escalations, negative sentiment, or usage decline. The review team examines the Churn Risk Flag against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Customer Experience Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SUPPORT-011

---

## TCK3-SUPPORT-00021 — Onboarding (P3, Resolved)
**Created:** 2025-08-16 via Portal  |  **Requester:** Divya Joshi  |  **Assigned to:** Meera Chauhan

**Description:** Divya Joshi (Finance & Accounting) reported an issue via Portal related to 'Support Onboarding for New Hires'. Category: Onboarding. Logged against MK-SupportDesk.

**Investigation:** The assigned specialist reviewed the MK-SupportDesk record, confirmed the reported symptom against 'Support Onboarding for New Hires', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-SUPPORT-012 to resolve. HR notifies the relevant department and the MK-SupportDesk owner ahead of the employee's start or end date. the Support Team Lead prepares the required Support Onboarding, including MK-SupportDesk access, product training, and shadowing live tickets. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Support Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SUPPORT-012

---
