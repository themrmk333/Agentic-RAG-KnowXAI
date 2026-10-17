# Cybersecurity / Information Security — Rich Historical Ticket Archive (wave2, Page 6)

## TCK3-SEC-00044 — Data Protection (P3, Closed)
**Created:** 2026-03-02 via Portal  |  **Requester:** Aman Chauhan  |  **Assigned to:** Shreya Kapoor

**Description:** Aman Chauhan (Cybersecurity / Information Security) reported an issue via Portal related to 'Data Classification and Labeling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Classification and Labeling', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-SEC-012 to resolve. the data owner confirms eligibility and prerequisites: applying the correct label (Public, Internal, Confidential, Restricted). the data owner raises a request in MK-SecGuard specifying exactly which Data Classification is required. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Data Classification in the relevant system. the data owner is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-012

---

## TCK3-SEC-00151 — Network Security (P3, Closed)
**Created:** 2026-03-15 via Phone  |  **Requester:** Dev Malhotra  |  **Assigned to:** Rohan Agarwal

**Description:** Dev Malhotra (Cybersecurity / Information Security) reported an issue via Phone related to 'Firewall / Network Access Change Request'. Category: Network Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Firewall / Network Access Change Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SEC-010 to resolve. the requester logs into MK-SecGuard and navigates to the 'Firewall Change Request' section. the requester selects 'New Firewall Change Request' and enters the required details, including source, destination, port, and business justification. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Firewall Change Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-010

---

## TCK3-SEC-00137 — Access Control (P4, Resolved)
**Created:** 2026-03-17 via Portal  |  **Requester:** Karan Bhatt  |  **Assigned to:** Ananya Nair

**Description:** Karan Bhatt (DevOps & Cloud) reported an issue via Portal related to 'Privileged Access Management (PAM) Request'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Privileged Access Management (PAM) Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SEC-014 to resolve. the requester logs into MK-SecGuard and navigates to the 'Privileged Access Request' section. the requester selects 'New Privileged Access Request' and enters the required details, including the specific system, duration, and business justification for elevated access. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Privileged Access Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-014

---

## TCK3-SEC-00034 — Data Protection (P3, Resolved)
**Created:** 2026-03-28 via Live Chat  |  **Requester:** Tanya Singh  |  **Assigned to:** Shreya Kapoor

**Description:** Tanya Singh (Software Engineering / Development) reported an issue via Live Chat related to 'Data Loss Prevention (DLP) Alert Handling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Loss Prevention (DLP) Alert Handling', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-SEC-006 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: reviewing the flagged content and confirming whether it is a genuine policy violation. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'DLP Alert', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-006

---

## TCK3-SEC-00103 — Network Security (P3, Resolved)
**Created:** 2026-03-31 via Email  |  **Requester:** Riya Pillai  |  **Assigned to:** Neel Malhotra

**Description:** Riya Pillai (Legal & Compliance) reported an issue via Email related to 'Firewall / Network Access Change Request'. Category: Network Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Firewall / Network Access Change Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SEC-010 to resolve. the requester logs into MK-SecGuard and navigates to the 'Firewall Change Request' section. the requester selects 'New Firewall Change Request' and enters the required details, including source, destination, port, and business justification. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Firewall Change Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-010

---

## TCK3-SEC-00107 — Access Control (P3, Resolved)
**Created:** 2026-04-08 via Email  |  **Requester:** Bhavna Pillai  |  **Assigned to:** Siddharth Joshi

**Description:** Bhavna Pillai (Sales) reported an issue via Email related to 'Access Control Review'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Access Control Review', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-SEC-004 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a full export of current access grants per system. The review team examines the Access Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-004

---

## TCK3-SEC-00058 — Endpoint Security (P3, Closed)
**Created:** 2026-04-15 via Portal  |  **Requester:** Gaurav Sharma  |  **Assigned to:** Manoj Nair

**Description:** Gaurav Sharma (IT Support / Information Technology) reported an issue via Portal related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00141 — Incident Response (P3, In Progress)
**Created:** 2026-04-18 via Live Chat  |  **Requester:** Karan Kapoor  |  **Assigned to:** Ananya Nair

**Description:** Karan Kapoor (Software Engineering / Development) reported an issue via Live Chat related to 'Data Breach Notification Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Breach Notification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-016

---

## TCK3-SEC-00135 — Security Testing (P4, Resolved)
**Created:** 2026-04-26 via Email  |  **Requester:** Simran Verma  |  **Assigned to:** Rahul Reddy

**Description:** Simran Verma (IT Support / Information Technology) reported an issue via Email related to 'Penetration Test Coordination'. Category: Security Testing. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Penetration Test Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-SEC-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scope, rules of engagement, and testing window agreed with the approved vendor. The review team examines the Penetration Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The CISO discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-013

---

## TCK3-SEC-00076 — Security Testing (P3, Resolved)
**Created:** 2026-05-06 via Walk-in  |  **Requester:** Rohan Sharma  |  **Assigned to:** Aman Chauhan

**Description:** Rohan Sharma (Administration / Facilities) reported an issue via Walk-in related to 'Penetration Test Coordination'. Category: Security Testing. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Penetration Test Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-SEC-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scope, rules of engagement, and testing window agreed with the approved vendor. The review team examines the Penetration Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The CISO discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-013

---

## TCK3-SEC-00083 — Data Protection (P3, Resolved)
**Created:** 2026-05-15 via Slack  |  **Requester:** Simran Agarwal  |  **Assigned to:** Manoj Nair

**Description:** Simran Agarwal (Finance & Accounting) reported an issue via Slack related to 'Data Loss Prevention (DLP) Alert Handling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Loss Prevention (DLP) Alert Handling', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-SEC-006 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: reviewing the flagged content and confirming whether it is a genuine policy violation. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'DLP Alert', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-006

---

## TCK3-SEC-00084 — Network Security (P4, Resolved)
**Created:** 2026-05-18 via Walk-in  |  **Requester:** Meera Joshi  |  **Assigned to:** Shreya Kapoor

**Description:** Meera Joshi (DevOps & Cloud) reported an issue via Walk-in related to 'Firewall / Network Access Change Request'. Category: Network Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Firewall / Network Access Change Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SEC-010 to resolve. the requester logs into MK-SecGuard and navigates to the 'Firewall Change Request' section. the requester selects 'New Firewall Change Request' and enters the required details, including source, destination, port, and business justification. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Firewall Change Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-010

---

## TCK3-SEC-00128 — Endpoint Security (P4, Resolved)
**Created:** 2026-05-22 via Walk-in  |  **Requester:** Aditya Singh  |  **Assigned to:** Neel Malhotra

**Description:** Aditya Singh (Research & Development) reported an issue via Walk-in related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00052 — Security Testing (P3, Resolved)
**Created:** 2026-05-24 via Phone  |  **Requester:** Arjun Gupta  |  **Assigned to:** Neel Malhotra

**Description:** Arjun Gupta (Data & Analytics) reported an issue via Phone related to 'Penetration Test Coordination'. Category: Security Testing. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Penetration Test Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-SEC-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scope, rules of engagement, and testing window agreed with the approved vendor. The review team examines the Penetration Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The CISO discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-013

---

## TCK3-SEC-00023 — Access Security (P4, Resolved)
**Created:** 2026-06-01 via Walk-in  |  **Requester:** Neel Mehta  |  **Assigned to:** Ananya Nair

**Description:** Neel Mehta (Legal & Compliance) reported an issue via Walk-in related to 'Multi-Factor Authentication (MFA) Enrollment'. Category: Access Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Multi-Factor Authentication (MFA) Enrollment', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-SEC-002 to resolve. the employee confirms eligibility and prerequisites: installing the MK-Authenticator app and scanning the enrollment QR code. the employee raises a request in MK-SecGuard specifying exactly which MFA Enrollment is required. The Security Analyst reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the MFA Enrollment in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-002

---

## TCK3-SEC-00098 — Incident Response (P3, Resolved)
**Created:** 2026-06-08 via Portal  |  **Requester:** Naveen Bose  |  **Assigned to:** Anjali Nair

**Description:** Naveen Bose (Project Management / PMO) reported an issue via Portal related to 'Security Incident Response Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Incident Response Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-SEC-003 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: containing the affected system by isolating it from the network. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Security Incident', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-003

---

## TCK3-SEC-00105 — Vendor Risk (P4, Resolved)
**Created:** 2026-06-10 via Walk-in  |  **Requester:** Preeti Verma  |  **Assigned to:** Dev Malhotra

**Description:** Preeti Verma (Software Engineering / Development) reported an issue via Walk-in related to 'Third-Party Vendor Security Assessment'. Category: Vendor Risk. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Third-Party Vendor Security Assessment', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-SEC-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a completed security questionnaire and any recent audit/certification evidence. The review team examines the Vendor Security Assessment against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-009

---

## TCK3-SEC-00050 — Incident Response (P2, Closed)
**Created:** 2026-06-14 via Slack  |  **Requester:** Sneha Kapoor  |  **Assigned to:** Ananya Nair

**Description:** Sneha Kapoor (Data & Analytics) reported an issue via Slack related to 'Security Incident Response Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Incident Response Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-SEC-003 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: containing the affected system by isolating it from the network. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Security Incident', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-003

---

## TCK3-SEC-00126 — Vulnerability Management (P2, Resolved)
**Created:** 2026-06-22 via Email  |  **Requester:** Neel Mehta  |  **Assigned to:** Neel Malhotra

**Description:** Neel Mehta (Legal & Compliance) reported an issue via Email related to 'Vulnerability Scanning and Remediation'. Category: Vulnerability Management. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Vulnerability Scanning and Remediation', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-SEC-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scanning production and staging environments on the scheduled cadence. The review team examines the Vulnerability Scan Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-005

---

## TCK3-SEC-00079 — Governance (P3, In Progress)
**Created:** 2026-06-24 via Walk-in  |  **Requester:** Simran Malhotra  |  **Assigned to:** Ananya Nair

**Description:** Simran Malhotra (Finance & Accounting) reported an issue via Walk-in related to 'Security Policy Exception Request'. Category: Governance. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Policy Exception Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-015

---
