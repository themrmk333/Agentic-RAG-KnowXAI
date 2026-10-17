# Cybersecurity / Information Security — Rich Historical Ticket Archive (wave2, Page 2)

## TCK3-SEC-00037 — Endpoint Security (P3, Resolved)
**Created:** 2024-11-10 via Live Chat  |  **Requester:** Nisha Bose  |  **Assigned to:** Swati Chowdhury

**Description:** Nisha Bose (Customer Support / Helpdesk) reported an issue via Live Chat related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00061 — Access Control (P3, Resolved)
**Created:** 2024-11-10 via Live Chat  |  **Requester:** Manoj Desai  |  **Assigned to:** Dev Malhotra

**Description:** Manoj Desai (Finance & Accounting) reported an issue via Live Chat related to 'Privileged Access Management (PAM) Request'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Privileged Access Management (PAM) Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SEC-014 to resolve. the requester logs into MK-SecGuard and navigates to the 'Privileged Access Request' section. the requester selects 'New Privileged Access Request' and enters the required details, including the specific system, duration, and business justification for elevated access. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Privileged Access Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-014

---

## TCK3-SEC-00025 — Access Control (P3, Resolved)
**Created:** 2024-11-12 via Slack  |  **Requester:** Dev Chauhan  |  **Assigned to:** Aman Chauhan

**Description:** Dev Chauhan (Marketing) reported an issue via Slack related to 'Privileged Access Management (PAM) Request'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Privileged Access Management (PAM) Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SEC-014 to resolve. the requester logs into MK-SecGuard and navigates to the 'Privileged Access Request' section. the requester selects 'New Privileged Access Request' and enters the required details, including the specific system, duration, and business justification for elevated access. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Privileged Access Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-014

---

## TCK3-SEC-00038 — Data Protection (P3, Closed)
**Created:** 2024-11-15 via Email  |  **Requester:** Ritika Singh  |  **Assigned to:** Dev Malhotra

**Description:** Ritika Singh (Procurement / Purchasing) reported an issue via Email related to 'Data Classification and Labeling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Classification and Labeling', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-SEC-012 to resolve. the data owner confirms eligibility and prerequisites: applying the correct label (Public, Internal, Confidential, Restricted). the data owner raises a request in MK-SecGuard specifying exactly which Data Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Classification in the relevant system. the data owner is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-012

---

## TCK3-SEC-00099 — Incident Response (P4, Resolved)
**Created:** 2024-11-16 via Walk-in  |  **Requester:** Rohan Desai  |  **Assigned to:** Rahul Reddy

**Description:** Rohan Desai (Sales) reported an issue via Walk-in related to 'Security Incident Response Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Incident Response Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-SEC-003 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: containing the affected system by isolating it from the network. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Security Incident', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-003

---

## TCK3-SEC-00089 — Data Protection (P3, Resolved)
**Created:** 2024-11-17 via Email  |  **Requester:** Karan Kapoor  |  **Assigned to:** Alisha Pillai

**Description:** Karan Kapoor (Software Engineering / Development) reported an issue via Email related to 'Data Classification and Labeling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Classification and Labeling', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-SEC-012 to resolve. the data owner confirms eligibility and prerequisites: applying the correct label (Public, Internal, Confidential, Restricted). the data owner raises a request in MK-SecGuard specifying exactly which Data Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Classification in the relevant system. the data owner is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-012

---

## TCK3-SEC-00096 — Security Testing (P2, Closed)
**Created:** 2024-11-19 via Phone  |  **Requester:** Aman Chauhan  |  **Assigned to:** Arjun Chowdhury

**Description:** Aman Chauhan (Sales) reported an issue via Phone related to 'Penetration Test Coordination'. Category: Security Testing. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Penetration Test Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-SEC-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scope, rules of engagement, and testing window agreed with the approved vendor. The review team examines the Penetration Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The CISO discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-013

---

## TCK3-SEC-00047 — Access Control (P3, Resolved)
**Created:** 2024-11-22 via Email  |  **Requester:** Divya Chowdhury  |  **Assigned to:** Rohan Agarwal

**Description:** Divya Chowdhury (Human Resources) reported an issue via Email related to 'Access Control Review'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Access Control Review', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-SEC-004 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a full export of current access grants per system. The review team examines the Access Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-004

---

## TCK3-SEC-00138 — Access Control (P3, Closed)
**Created:** 2024-11-30 via Live Chat  |  **Requester:** Simran Gupta  |  **Assigned to:** Anjali Nair

**Description:** Simran Gupta (Management / Leadership) reported an issue via Live Chat related to 'Access Control Review'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Access Control Review', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-SEC-004 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a full export of current access grants per system. The review team examines the Access Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-004

---

## TCK3-SEC-00081 — Access Control (P3, Resolved)
**Created:** 2024-12-08 via Slack  |  **Requester:** Bhavna Pillai  |  **Assigned to:** Swati Chowdhury

**Description:** Bhavna Pillai (Sales) reported an issue via Slack related to 'Access Control Review'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Access Control Review', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-SEC-004 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a full export of current access grants per system. The review team examines the Access Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-004

---

## TCK3-SEC-00115 — Governance (P3, Closed)
**Created:** 2024-12-10 via Phone  |  **Requester:** Alisha Pillai  |  **Assigned to:** Aditya Rao

**Description:** Alisha Pillai (Cybersecurity / Information Security) reported an issue via Phone related to 'Security Policy Exception Request'. Category: Governance. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Policy Exception Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-SEC-015 to resolve. the requester logs into MK-SecGuard and navigates to the 'Policy Exception Request' section. the requester selects 'New Policy Exception Request' and enters the required details, including the specific policy clause, business reason, and compensating controls. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Policy Exception Request; MK-SecGuard automatically routes it to the CISO for review. The CISO reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-015

---

## TCK3-SEC-00118 — Endpoint Security (P3, Closed)
**Created:** 2024-12-20 via Email  |  **Requester:** Anjali Nair  |  **Assigned to:** Neel Malhotra

**Description:** Anjali Nair (Cybersecurity / Information Security) reported an issue via Email related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00032 — Data Protection (P4, Resolved)
**Created:** 2024-12-22 via Phone  |  **Requester:** Nisha Desai  |  **Assigned to:** Dev Malhotra

**Description:** Nisha Desai (Management / Leadership) reported an issue via Phone related to 'Data Loss Prevention (DLP) Alert Handling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Loss Prevention (DLP) Alert Handling', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-SEC-006 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: reviewing the flagged content and confirming whether it is a genuine policy violation. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'DLP Alert', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-006

---

## TCK3-SEC-00120 — Endpoint Security (P3, Resolved)
**Created:** 2024-12-27 via Live Chat  |  **Requester:** Manoj Nair  |  **Assigned to:** Rohan Agarwal

**Description:** Manoj Nair (QA / Testing) reported an issue via Live Chat related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00054 — Incident Response (P3, Resolved)
**Created:** 2025-01-14 via Phone  |  **Requester:** Kabir Iyer  |  **Assigned to:** Ananya Nair

**Description:** Kabir Iyer (Legal & Compliance) reported an issue via Phone related to 'Data Breach Notification Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Breach Notification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-SEC-016 to resolve. the Incident Response Lead confirms the exact symptom, when it started, and whether it affects one system or several. the Incident Response Lead performs the standard first-line check: confirming scope of affected data and impacted individuals. If the issue persists, the Incident Response Lead applies the documented workaround for this issue type. the Incident Response Lead checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Incident Response Lead raises a ticket in MK-SecGuard categorised under 'Breach Notification', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-016

---

## TCK3-SEC-00131 — Training (P3, Resolved)
**Created:** 2025-01-21 via Slack  |  **Requester:** Nisha Desai  |  **Assigned to:** Ananya Nair

**Description:** Nisha Desai (Management / Leadership) reported an issue via Slack related to 'Security Awareness Training Assignment'. Category: Training. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Awareness Training Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-SEC-008 to resolve. the Security Analyst confirms eligibility and prerequisites: assigning the mandatory annual module in MK-SecGuard Learning. the Security Analyst raises a request in MK-SecGuard specifying exactly which Training Assignment is required. The HR Business Partner reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Training Assignment in the relevant system. the Security Analyst is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-008

---

## TCK3-SEC-00140 — Governance (P1, Closed)
**Created:** 2025-01-23 via Phone  |  **Requester:** Preeti Kapoor  |  **Assigned to:** Alisha Pillai

**Description:** Preeti Kapoor (Marketing) reported an issue via Phone related to 'Security Policy Exception Request'. Category: Governance. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Policy Exception Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SEC-015 to resolve. the requester logs into MK-SecGuard and navigates to the 'Policy Exception Request' section. the requester selects 'New Policy Exception Request' and enters the required details, including the specific policy clause, business reason, and compensating controls. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Policy Exception Request; MK-SecGuard automatically routes it to the CISO for review. The CISO reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-015

---

## TCK3-SEC-00060 — Data Protection (P3, Resolved)
**Created:** 2025-01-28 via Phone  |  **Requester:** Priya Rao  |  **Assigned to:** Arjun Chowdhury

**Description:** Priya Rao (DevOps & Cloud) reported an issue via Phone related to 'Data Classification and Labeling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Classification and Labeling', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-SEC-012 to resolve. the data owner confirms eligibility and prerequisites: applying the correct label (Public, Internal, Confidential, Restricted). the data owner raises a request in MK-SecGuard specifying exactly which Data Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Classification in the relevant system. the data owner is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-012

---

## TCK3-SEC-00082 — Endpoint Security (P3, Resolved)
**Created:** 2025-02-03 via Walk-in  |  **Requester:** Dev Malhotra  |  **Assigned to:** Rahul Reddy

**Description:** Dev Malhotra (Cybersecurity / Information Security) reported an issue via Walk-in related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00063 — Incident Response (P2, Resolved)
**Created:** 2025-02-07 via Slack  |  **Requester:** Yash Sharma  |  **Assigned to:** Rohan Agarwal

**Description:** Yash Sharma (Administration / Facilities) reported an issue via Slack related to 'Data Breach Notification Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Breach Notification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-SEC-016 to resolve. the Incident Response Lead confirms the exact symptom, when it started, and whether it affects one system or several. the Incident Response Lead performs the standard first-line check: confirming scope of affected data and impacted individuals. If the issue persists, the Incident Response Lead applies the documented workaround for this issue type. the Incident Response Lead checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Incident Response Lead raises a ticket in MK-SecGuard categorised under 'Breach Notification', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-016

---