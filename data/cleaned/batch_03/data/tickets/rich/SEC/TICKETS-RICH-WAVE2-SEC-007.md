# Cybersecurity / Information Security — Rich Historical Ticket Archive (wave2, Page 7)

## TCK3-SEC-00121 — Vendor Risk (P4, Resolved)
**Created:** 2026-07-03 via Slack  |  **Requester:** Bhavna Pillai  |  **Assigned to:** Rohan Agarwal

**Description:** Bhavna Pillai (Sales) reported an issue via Slack related to 'Third-Party Vendor Security Assessment'. Category: Vendor Risk. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Third-Party Vendor Security Assessment', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-SEC-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a completed security questionnaire and any recent audit/certification evidence. The review team examines the Vendor Security Assessment against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-009

---

## TCK3-SEC-00053 — Incident Response (P3, Resolved)
**Created:** 2026-07-05 via Slack  |  **Requester:** Ritika Mehta  |  **Assigned to:** Rahul Reddy

**Description:** Ritika Mehta (Research & Development) reported an issue via Slack related to 'Data Breach Notification Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Breach Notification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-SEC-016 to resolve. the Incident Response Lead confirms the exact symptom, when it started, and whether it affects one system or several. the Incident Response Lead performs the standard first-line check: confirming scope of affected data and impacted individuals. If the issue persists, the Incident Response Lead applies the documented workaround for this issue type. the Incident Response Lead checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Incident Response Lead raises a ticket in MK-SecGuard categorised under 'Breach Notification', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-016

---

## TCK3-SEC-00148 — Endpoint Security (P3, Resolved)
**Created:** 2026-07-11 via Slack  |  **Requester:** Neel Agarwal  |  **Assigned to:** Rohan Agarwal

**Description:** Neel Agarwal (Research & Development) reported an issue via Slack related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00043 — Vulnerability Management (P4, Resolved)
**Created:** 2026-07-16 via Portal  |  **Requester:** Swati Sharma  |  **Assigned to:** Shreya Reddy

**Description:** Swati Sharma (QA / Testing) reported an issue via Portal related to 'Vulnerability Scanning and Remediation'. Category: Vulnerability Management. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Vulnerability Scanning and Remediation', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-SEC-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scanning production and staging environments on the scheduled cadence. The review team examines the Vulnerability Scan Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-005

---

## TCK3-SEC-00092 — Vendor Risk (P4, Closed)
**Created:** 2026-07-17 via Slack  |  **Requester:** Bhavna Gupta  |  **Assigned to:** Shreya Reddy

**Description:** Bhavna Gupta (Legal & Compliance) reported an issue via Slack related to 'Third-Party Vendor Security Assessment'. Category: Vendor Risk. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Third-Party Vendor Security Assessment', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-SEC-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a completed security questionnaire and any recent audit/certification evidence. The review team examines the Vendor Security Assessment against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-009

---

## TCK3-SEC-00129 — Access Control (P2, Resolved)
**Created:** 2026-07-24 via Slack  |  **Requester:** Sahil Menon  |  **Assigned to:** Siddharth Joshi

**Description:** Sahil Menon (QA / Testing) reported an issue via Slack related to 'Privileged Access Management (PAM) Request'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Privileged Access Management (PAM) Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SEC-014 to resolve. the requester logs into MK-SecGuard and navigates to the 'Privileged Access Request' section. the requester selects 'New Privileged Access Request' and enters the required details, including the specific system, duration, and business justification for elevated access. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Privileged Access Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-014

---

## TCK3-SEC-00125 — Training (P3, Resolved)
**Created:** 2026-08-02 via Portal  |  **Requester:** Anjali Gupta  |  **Assigned to:** Siddharth Joshi

**Description:** Anjali Gupta (Legal & Compliance) reported an issue via Portal related to 'Security Awareness Training Assignment'. Category: Training. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Awareness Training Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-SEC-008 to resolve. the Security Analyst confirms eligibility and prerequisites: assigning the mandatory annual module in MK-SecGuard Learning. the Security Analyst raises a request in MK-SecGuard specifying exactly which Training Assignment is required. The HR Business Partner reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Training Assignment in the relevant system. the Security Analyst is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-008

---

## TCK3-SEC-00109 — Vendor Risk (P3, Resolved)
**Created:** 2026-08-04 via Walk-in  |  **Requester:** Ritika Desai  |  **Assigned to:** Dev Malhotra

**Description:** Ritika Desai (Legal & Compliance) reported an issue via Walk-in related to 'Third-Party Vendor Security Assessment'. Category: Vendor Risk. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Third-Party Vendor Security Assessment', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-SEC-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a completed security questionnaire and any recent audit/certification evidence. The review team examines the Vendor Security Assessment against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-009

---

## TCK3-SEC-00132 — Endpoint Security (P3, Resolved)
**Created:** 2026-08-13 via Portal  |  **Requester:** Arjun Chowdhury  |  **Assigned to:** Siddharth Joshi

**Description:** Arjun Chowdhury (Finance & Accounting) reported an issue via Portal related to 'Endpoint Security Alert Triage'. Category: Endpoint Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Endpoint Security Alert Triage', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-SEC-011 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: checking MK-SecGuard EDR console for the alert classification. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'Endpoint Alert', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-011

---

## TCK3-SEC-00100 — Onboarding (P4, Resolved)
**Created:** 2026-08-18 via Email  |  **Requester:** Shreya Nair  |  **Assigned to:** Manoj Nair

**Description:** Shreya Nair (Project Management / PMO) reported an issue via Email related to 'New Employee Security Onboarding'. Category: Onboarding. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'New Employee Security Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-SEC-007 to resolve. HR notifies the relevant department and the MK-SecGuard owner ahead of the employee's start or end date. the Security Analyst prepares the required Security Onboarding, including MFA enrollment, security awareness training assignment, and acceptable use acknowledgment. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Security Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SEC-007

---

## TCK3-SEC-00142 — Access Security (P2, Resolved)
**Created:** 2026-08-20 via Walk-in  |  **Requester:** Bhavna Gupta  |  **Assigned to:** Arjun Chowdhury

**Description:** Bhavna Gupta (Legal & Compliance) reported an issue via Walk-in related to 'Multi-Factor Authentication (MFA) Enrollment'. Category: Access Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Multi-Factor Authentication (MFA) Enrollment', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-SEC-002 to resolve. the employee confirms eligibility and prerequisites: installing the MK-Authenticator app and scanning the enrollment QR code. the employee raises a request in MK-SecGuard specifying exactly which MFA Enrollment is required. The Security Analyst reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the MFA Enrollment in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-002

---