# Cybersecurity / Information Security — Rich Historical Ticket Archive (wave2, Page 1)

## TCK3-SEC-00147 — Governance (P1, Resolved)
**Created:** 2024-06-08 via Email  |  **Requester:** Rahul Desai  |  **Assigned to:** Siddharth Joshi

**Description:** Rahul Desai (QA / Testing) reported an issue via Email related to 'Security Policy Exception Request'. Category: Governance. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Policy Exception Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SEC-015 to resolve. the requester logs into MK-SecGuard and navigates to the 'Policy Exception Request' section. the requester selects 'New Policy Exception Request' and enters the required details, including the specific policy clause, business reason, and compensating controls. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Policy Exception Request; MK-SecGuard automatically routes it to the CISO for review. The CISO reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-015

---

## TCK3-SEC-00093 — Data Protection (P2, Resolved)
**Created:** 2024-06-24 via Email  |  **Requester:** Gaurav Pillai  |  **Assigned to:** Swati Chowdhury

**Description:** Gaurav Pillai (Data & Analytics) reported an issue via Email related to 'Data Classification and Labeling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Classification and Labeling', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-SEC-012 to resolve. the data owner confirms eligibility and prerequisites: applying the correct label (Public, Internal, Confidential, Restricted). the data owner raises a request in MK-SecGuard specifying exactly which Data Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Classification in the relevant system. the data owner is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-012

---

## TCK3-SEC-00066 — Network Security (P3, Resolved)
**Created:** 2024-06-27 via Walk-in  |  **Requester:** Sneha Reddy  |  **Assigned to:** Harsh Nair

**Description:** Sneha Reddy (QA / Testing) reported an issue via Walk-in related to 'Firewall / Network Access Change Request'. Category: Network Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Firewall / Network Access Change Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SEC-010 to resolve. the requester logs into MK-SecGuard and navigates to the 'Firewall Change Request' section. the requester selects 'New Firewall Change Request' and enters the required details, including source, destination, port, and business justification. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Firewall Change Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-010

---

## TCK3-SEC-00028 — Access Security (P2, Resolved)
**Created:** 2024-07-03 via Slack  |  **Requester:** Harsh Chauhan  |  **Assigned to:** Siddharth Joshi

**Description:** Harsh Chauhan (QA / Testing) reported an issue via Slack related to 'Multi-Factor Authentication (MFA) Enrollment'. Category: Access Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Multi-Factor Authentication (MFA) Enrollment', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-SEC-002 to resolve. the employee confirms eligibility and prerequisites: installing the MK-Authenticator app and scanning the enrollment QR code. the employee raises a request in MK-SecGuard specifying exactly which MFA Enrollment is required. The Security Analyst reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the MFA Enrollment in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-002

---

## TCK3-SEC-00049 — Incident Response (P3, Closed)
**Created:** 2024-07-16 via Live Chat  |  **Requester:** Divya Menon  |  **Assigned to:** Alisha Pillai

**Description:** Divya Menon (QA / Testing) reported an issue via Live Chat related to 'Data Breach Notification Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Breach Notification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-SEC-016 to resolve. the Incident Response Lead confirms the exact symptom, when it started, and whether it affects one system or several. the Incident Response Lead performs the standard first-line check: confirming scope of affected data and impacted individuals. If the issue persists, the Incident Response Lead applies the documented workaround for this issue type. the Incident Response Lead checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Incident Response Lead raises a ticket in MK-SecGuard categorised under 'Breach Notification', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-016

---

## TCK3-SEC-00130 — Access Control (P4, Resolved)
**Created:** 2024-07-17 via Phone  |  **Requester:** Vivek Gupta  |  **Assigned to:** Siddharth Joshi

**Description:** Vivek Gupta (Sales) reported an issue via Phone related to 'Privileged Access Management (PAM) Request'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Privileged Access Management (PAM) Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SEC-014 to resolve. the requester logs into MK-SecGuard and navigates to the 'Privileged Access Request' section. the requester selects 'New Privileged Access Request' and enters the required details, including the specific system, duration, and business justification for elevated access. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Privileged Access Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-014

---

## TCK3-SEC-00095 — Network Security (P4, Resolved)
**Created:** 2024-07-30 via Phone  |  **Requester:** Riya Pillai  |  **Assigned to:** Aman Chauhan

**Description:** Riya Pillai (Software Engineering / Development) reported an issue via Phone related to 'Firewall / Network Access Change Request'. Category: Network Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Firewall / Network Access Change Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SEC-010 to resolve. the requester logs into MK-SecGuard and navigates to the 'Firewall Change Request' section. the requester selects 'New Firewall Change Request' and enters the required details, including source, destination, port, and business justification. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Firewall Change Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-010

---

## TCK3-SEC-00106 — Incident Response (P3, Resolved)
**Created:** 2024-08-10 via Portal  |  **Requester:** Kabir Reddy  |  **Assigned to:** Aman Chauhan

**Description:** Kabir Reddy (QA / Testing) reported an issue via Portal related to 'Security Incident Response Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Incident Response Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-SEC-003 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: containing the affected system by isolating it from the network. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Security Incident', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-003

---

## TCK3-SEC-00062 — Data Protection (P3, Resolved)
**Created:** 2024-08-12 via Email  |  **Requester:** Yash Bose  |  **Assigned to:** Shreya Reddy

**Description:** Yash Bose (Software Engineering / Development) reported an issue via Email related to 'Data Loss Prevention (DLP) Alert Handling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Loss Prevention (DLP) Alert Handling', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-SEC-006 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: reviewing the flagged content and confirming whether it is a genuine policy violation. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'DLP Alert', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-006

---

## TCK3-SEC-00029 — Vendor Risk (P3, Resolved)
**Created:** 2024-08-13 via Phone  |  **Requester:** Meera Joshi  |  **Assigned to:** Harsh Nair

**Description:** Meera Joshi (DevOps & Cloud) reported an issue via Phone related to 'Third-Party Vendor Security Assessment'. Category: Vendor Risk. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Third-Party Vendor Security Assessment', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-SEC-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a completed security questionnaire and any recent audit/certification evidence. The review team examines the Vendor Security Assessment against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-009

---

## TCK3-SEC-00067 — Access Control (P4, Resolved)
**Created:** 2024-08-14 via Phone  |  **Requester:** Ritika Agarwal  |  **Assigned to:** Shreya Kapoor

**Description:** Ritika Agarwal (Customer Support / Helpdesk) reported an issue via Phone related to 'Privileged Access Management (PAM) Request'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Privileged Access Management (PAM) Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SEC-014 to resolve. the requester logs into MK-SecGuard and navigates to the 'Privileged Access Request' section. the requester selects 'New Privileged Access Request' and enters the required details, including the specific system, duration, and business justification for elevated access. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Privileged Access Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-014

---

## TCK3-SEC-00094 — Endpoint Security (P3, Resolved)
**Created:** 2024-08-22 via Live Chat  |  **Requester:** Ritika Desai  |  **Assigned to:** Aditya Rao

**Description:** Ritika Desai (Legal & Compliance) reported an issue via Live Chat related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00074 — Access Control (P2, Resolved)
**Created:** 2024-08-23 via Live Chat  |  **Requester:** Vikram Malhotra  |  **Assigned to:** Shreya Kapoor

**Description:** Vikram Malhotra (QA / Testing) reported an issue via Live Chat related to 'Access Control Review'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Access Control Review', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-SEC-004 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a full export of current access grants per system. The review team examines the Access Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-004

---

## TCK3-SEC-00149 — Endpoint Security (P2, Resolved)
**Created:** 2024-09-01 via Walk-in  |  **Requester:** Siddharth Reddy  |  **Assigned to:** Arjun Chowdhury

**Description:** Siddharth Reddy (Human Resources) reported an issue via Walk-in related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00104 — Access Security (P3, Resolved)
**Created:** 2024-09-05 via Email  |  **Requester:** Shreya Reddy  |  **Assigned to:** Shreya Kapoor

**Description:** Shreya Reddy (Product Management) reported an issue via Email related to 'Multi-Factor Authentication (MFA) Enrollment'. Category: Access Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Multi-Factor Authentication (MFA) Enrollment', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-SEC-002 to resolve. the employee confirms eligibility and prerequisites: installing the MK-Authenticator app and scanning the enrollment QR code. the employee raises a request in MK-SecGuard specifying exactly which MFA Enrollment is required. The Security Analyst reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the MFA Enrollment in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-002

---

## TCK3-SEC-00114 — Access Control (P3, Closed)
**Created:** 2024-09-06 via Portal  |  **Requester:** Varun Iyer  |  **Assigned to:** Dev Malhotra

**Description:** Varun Iyer (Legal & Compliance) reported an issue via Portal related to 'Privileged Access Management (PAM) Request'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Privileged Access Management (PAM) Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SEC-014 to resolve. the requester logs into MK-SecGuard and navigates to the 'Privileged Access Request' section. the requester selects 'New Privileged Access Request' and enters the required details, including the specific system, duration, and business justification for elevated access. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Privileged Access Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-014

---

## TCK3-SEC-00136 — Access Control (P4, Resolved)
**Created:** 2024-09-08 via Live Chat  |  **Requester:** Alisha Verma  |  **Assigned to:** Neel Malhotra

**Description:** Alisha Verma (QA / Testing) reported an issue via Live Chat related to 'Privileged Access Management (PAM) Request'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Privileged Access Management (PAM) Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SEC-014 to resolve. the requester logs into MK-SecGuard and navigates to the 'Privileged Access Request' section. the requester selects 'New Privileged Access Request' and enters the required details, including the specific system, duration, and business justification for elevated access. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Privileged Access Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-014

---

## TCK3-SEC-00124 — Data Protection (P3, Closed)
**Created:** 2024-09-18 via Walk-in  |  **Requester:** Rahul Nair  |  **Assigned to:** Rahul Reddy

**Description:** Rahul Nair (Administration / Facilities) reported an issue via Walk-in related to 'Data Loss Prevention (DLP) Alert Handling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Loss Prevention (DLP) Alert Handling', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-SEC-006 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: reviewing the flagged content and confirming whether it is a genuine policy violation. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'DLP Alert', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-006

---

## TCK3-SEC-00068 — Incident Response (P4, Resolved)
**Created:** 2024-09-27 via Slack  |  **Requester:** Neel Joshi  |  **Assigned to:** Manoj Nair

**Description:** Neel Joshi (Software Engineering / Development) reported an issue via Slack related to 'Data Breach Notification Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Breach Notification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-SEC-016 to resolve. the Incident Response Lead confirms the exact symptom, when it started, and whether it affects one system or several. the Incident Response Lead performs the standard first-line check: confirming scope of affected data and impacted individuals. If the issue persists, the Incident Response Lead applies the documented workaround for this issue type. the Incident Response Lead checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Incident Response Lead raises a ticket in MK-SecGuard categorised under 'Breach Notification', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-016

---

## TCK3-SEC-00075 — Data Protection (P3, Closed)
**Created:** 2024-10-15 via Phone  |  **Requester:** Simran Gupta  |  **Assigned to:** Aditya Rao

**Description:** Simran Gupta (Sales) reported an issue via Phone related to 'Data Classification and Labeling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Classification and Labeling', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-SEC-012 to resolve. the data owner confirms eligibility and prerequisites: applying the correct label (Public, Internal, Confidential, Restricted). the data owner raises a request in MK-SecGuard specifying exactly which Data Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Classification in the relevant system. the data owner is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-012

---