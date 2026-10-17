# Cybersecurity / Information Security — Rich Historical Ticket Archive (wave2, Page 4)

## TCK3-SEC-00144 — Vendor Risk (P3, Closed)
**Created:** 2025-05-29 via Walk-in  |  **Requester:** Sneha Agarwal  |  **Assigned to:** Anjali Nair

**Description:** Sneha Agarwal (Research & Development) reported an issue via Walk-in related to 'Third-Party Vendor Security Assessment'. Category: Vendor Risk. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Third-Party Vendor Security Assessment', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-SEC-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a completed security questionnaire and any recent audit/certification evidence. The review team examines the Vendor Security Assessment against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-009

---

## TCK3-SEC-00027 — Vulnerability Management (P2, Resolved)
**Created:** 2025-06-01 via Live Chat  |  **Requester:** Sahil Menon  |  **Assigned to:** Manoj Nair

**Description:** Sahil Menon (QA / Testing) reported an issue via Live Chat related to 'Vulnerability Scanning and Remediation'. Category: Vulnerability Management. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Vulnerability Scanning and Remediation', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-SEC-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scanning production and staging environments on the scheduled cadence. The review team examines the Vulnerability Scan Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-005

---

## TCK3-SEC-00112 — Network Security (P3, Resolved)
**Created:** 2025-06-01 via Email  |  **Requester:** Rohan Mehta  |  **Assigned to:** Siddharth Joshi

**Description:** Rohan Mehta (Data & Analytics) reported an issue via Email related to 'Firewall / Network Access Change Request'. Category: Network Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Firewall / Network Access Change Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SEC-010 to resolve. the requester logs into MK-SecGuard and navigates to the 'Firewall Change Request' section. the requester selects 'New Firewall Change Request' and enters the required details, including source, destination, port, and business justification. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Firewall Change Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-010

---

## TCK3-SEC-00069 — Network Security (P2, In Progress)
**Created:** 2025-06-03 via Slack  |  **Requester:** Ananya Menon  |  **Assigned to:** Shreya Kapoor

**Description:** Ananya Menon (Human Resources) reported an issue via Slack related to 'Firewall / Network Access Change Request'. Category: Network Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Firewall / Network Access Change Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-010

---

## TCK3-SEC-00071 — Access Security (P4, Resolved)
**Created:** 2025-06-05 via Portal  |  **Requester:** Arjun Verma  |  **Assigned to:** Shreya Reddy

**Description:** Arjun Verma (Administration / Facilities) reported an issue via Portal related to 'Multi-Factor Authentication (MFA) Enrollment'. Category: Access Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Multi-Factor Authentication (MFA) Enrollment', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-SEC-002 to resolve. the employee confirms eligibility and prerequisites: installing the MK-Authenticator app and scanning the enrollment QR code. the employee raises a request in MK-SecGuard specifying exactly which MFA Enrollment is required. The Security Analyst reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the MFA Enrollment in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-002

---

## TCK3-SEC-00026 — Access Control (P3, Resolved)
**Created:** 2025-06-13 via Portal  |  **Requester:** Rohan Sharma  |  **Assigned to:** Ananya Nair

**Description:** Rohan Sharma (Project Management / PMO) reported an issue via Portal related to 'Privileged Access Management (PAM) Request'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Privileged Access Management (PAM) Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SEC-014 to resolve. the requester logs into MK-SecGuard and navigates to the 'Privileged Access Request' section. the requester selects 'New Privileged Access Request' and enters the required details, including the specific system, duration, and business justification for elevated access. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Privileged Access Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-014

---

## TCK3-SEC-00046 — Access Security (P2, Resolved)
**Created:** 2025-07-15 via Phone  |  **Requester:** Varun Kapoor  |  **Assigned to:** Neel Malhotra

**Description:** Varun Kapoor (Data & Analytics) reported an issue via Phone related to 'Multi-Factor Authentication (MFA) Enrollment'. Category: Access Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Multi-Factor Authentication (MFA) Enrollment', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-SEC-002 to resolve. the employee confirms eligibility and prerequisites: installing the MK-Authenticator app and scanning the enrollment QR code. the employee raises a request in MK-SecGuard specifying exactly which MFA Enrollment is required. The Security Analyst reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the MFA Enrollment in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-002

---

## TCK3-SEC-00042 — Vulnerability Management (P4, Resolved)
**Created:** 2025-07-17 via Portal  |  **Requester:** Kavya Verma  |  **Assigned to:** Alisha Pillai

**Description:** Kavya Verma (Administration / Facilities) reported an issue via Portal related to 'Vulnerability Scanning and Remediation'. Category: Vulnerability Management. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Vulnerability Scanning and Remediation', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-SEC-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scanning production and staging environments on the scheduled cadence. The review team examines the Vulnerability Scan Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-005

---

## TCK3-SEC-00113 — Security Testing (P3, Resolved)
**Created:** 2025-07-20 via Email  |  **Requester:** Neel Malhotra  |  **Assigned to:** Rohan Agarwal

**Description:** Neel Malhotra (Cybersecurity / Information Security) reported an issue via Email related to 'Penetration Test Coordination'. Category: Security Testing. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Penetration Test Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-SEC-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scope, rules of engagement, and testing window agreed with the approved vendor. The review team examines the Penetration Test against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The CISO discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-013

---

## TCK3-SEC-00101 — Access Control (P4, Closed)
**Created:** 2025-07-21 via Phone  |  **Requester:** Alisha Bhatt  |  **Assigned to:** Swati Chowdhury

**Description:** Alisha Bhatt (Management / Leadership) reported an issue via Phone related to 'Access Control Review'. Category: Access Control. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Access Control Review', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-SEC-004 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Analyst gathers the required data and documents, including a full export of current access grants per system. The review team examines the Access Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-004

---

## TCK3-SEC-00119 — Incident Response (P3, Resolved)
**Created:** 2025-07-29 via Phone  |  **Requester:** Divya Menon  |  **Assigned to:** Aman Chauhan

**Description:** Divya Menon (Project Management / PMO) reported an issue via Phone related to 'Data Breach Notification Procedure'. Category: Incident Response. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Breach Notification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-SEC-016 to resolve. the Incident Response Lead confirms the exact symptom, when it started, and whether it affects one system or several. the Incident Response Lead performs the standard first-line check: confirming scope of affected data and impacted individuals. If the issue persists, the Incident Response Lead applies the documented workaround for this issue type. the Incident Response Lead checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Incident Response Lead raises a ticket in MK-SecGuard categorised under 'Breach Notification', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-016

---

## TCK3-SEC-00033 — Vulnerability Management (P2, Resolved)
**Created:** 2025-08-03 via Walk-in  |  **Requester:** Alisha Reddy  |  **Assigned to:** Arjun Chowdhury

**Description:** Alisha Reddy (Data & Analytics) reported an issue via Walk-in related to 'Vulnerability Scanning and Remediation'. Category: Vulnerability Management. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Vulnerability Scanning and Remediation', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-SEC-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-SecGuard. the Security Engineer gathers the required data and documents, including scanning production and staging environments on the scheduled cadence. The review team examines the Vulnerability Scan Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SEC-005

---

## TCK3-SEC-00146 — Network Security (P3, Resolved)
**Created:** 2025-08-25 via Walk-in  |  **Requester:** Kabir Nair  |  **Assigned to:** Aditya Rao

**Description:** Kabir Nair (Administration / Facilities) reported an issue via Walk-in related to 'Firewall / Network Access Change Request'. Category: Network Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Firewall / Network Access Change Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SEC-010 to resolve. the requester logs into MK-SecGuard and navigates to the 'Firewall Change Request' section. the requester selects 'New Firewall Change Request' and enters the required details, including source, destination, port, and business justification. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Firewall Change Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-010

---

## TCK3-SEC-00143 — Access Security (P3, Closed)
**Created:** 2025-08-30 via Portal  |  **Requester:** Sahil Malhotra  |  **Assigned to:** Swati Chowdhury

**Description:** Sahil Malhotra (Legal & Compliance) reported an issue via Portal related to 'Multi-Factor Authentication (MFA) Enrollment'. Category: Access Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Multi-Factor Authentication (MFA) Enrollment', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-SEC-002 to resolve. the employee confirms eligibility and prerequisites: installing the MK-Authenticator app and scanning the enrollment QR code. the employee raises a request in MK-SecGuard specifying exactly which MFA Enrollment is required. The Security Analyst reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the MFA Enrollment in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-002

---

## TCK3-SEC-00139 — Governance (P1, Resolved)
**Created:** 2025-09-02 via Slack  |  **Requester:** Divya Menon  |  **Assigned to:** Shreya Kapoor

**Description:** Divya Menon (QA / Testing) reported an issue via Slack related to 'Security Policy Exception Request'. Category: Governance. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Policy Exception Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SEC-015 to resolve. the requester logs into MK-SecGuard and navigates to the 'Policy Exception Request' section. the requester selects 'New Policy Exception Request' and enters the required details, including the specific policy clause, business reason, and compensating controls. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Policy Exception Request; MK-SecGuard automatically routes it to the CISO for review. The CISO reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-015

---

## TCK3-SEC-00134 — Data Protection (P4, Resolved)
**Created:** 2025-09-07 via Portal  |  **Requester:** Harsh Gupta  |  **Assigned to:** Aditya Rao

**Description:** Harsh Gupta (Research & Development) reported an issue via Portal related to 'Data Loss Prevention (DLP) Alert Handling'. Category: Data Protection. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Data Loss Prevention (DLP) Alert Handling', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-SEC-006 to resolve. the Security Analyst confirms the exact symptom, when it started, and whether it affects one system or several. the Security Analyst performs the standard first-line check: reviewing the flagged content and confirming whether it is a genuine policy violation. If the issue persists, the Security Analyst applies the documented workaround for this issue type. the Security Analyst checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Security Analyst raises a ticket in MK-SecGuard categorised under 'DLP Alert', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-SEC-006

---

## TCK3-SEC-00078 — Network Security (P4, Resolved)
**Created:** 2025-09-13 via Portal  |  **Requester:** Meera Malhotra  |  **Assigned to:** Anjali Nair

**Description:** Meera Malhotra (Procurement / Purchasing) reported an issue via Portal related to 'Firewall / Network Access Change Request'. Category: Network Security. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Firewall / Network Access Change Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SEC-010 to resolve. the requester logs into MK-SecGuard and navigates to the 'Firewall Change Request' section. the requester selects 'New Firewall Change Request' and enters the required details, including source, destination, port, and business justification. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Firewall Change Request; MK-SecGuard automatically routes it to the Security Manager for review. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-010

---

## TCK3-SEC-00059 — Onboarding (P4, Resolved)
**Created:** 2025-09-14 via Walk-in  |  **Requester:** Simran Malhotra  |  **Assigned to:** Shreya Kapoor

**Description:** Simran Malhotra (Finance & Accounting) reported an issue via Walk-in related to 'New Employee Security Onboarding'. Category: Onboarding. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'New Employee Security Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-SEC-007 to resolve. HR notifies the relevant department and the MK-SecGuard owner ahead of the employee's start or end date. the Security Analyst prepares the required Security Onboarding, including MFA enrollment, security awareness training assignment, and acceptable use acknowledgment. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Security Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SEC-007

---

## TCK3-SEC-00055 — Training (P3, Resolved)
**Created:** 2025-10-04 via Walk-in  |  **Requester:** Karan Kapoor  |  **Assigned to:** Aditya Rao

**Description:** Karan Kapoor (Software Engineering / Development) reported an issue via Walk-in related to 'Security Awareness Training Assignment'. Category: Training. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Awareness Training Assignment', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-SEC-008 to resolve. the Security Analyst confirms eligibility and prerequisites: assigning the mandatory annual module in MK-SecGuard Learning. the Security Analyst raises a request in MK-SecGuard specifying exactly which Training Assignment is required. The HR Business Partner reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Training Assignment in the relevant system. the Security Analyst is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SEC-008

---

## TCK3-SEC-00051 — Governance (P4, In Progress)
**Created:** 2025-10-12 via Live Chat  |  **Requester:** Nisha Desai  |  **Assigned to:** Shreya Reddy

**Description:** Nisha Desai (Project Management / PMO) reported an issue via Live Chat related to 'Security Policy Exception Request'. Category: Governance. Logged against MK-SecGuard.

**Investigation:** The assigned specialist reviewed the MK-SecGuard record, confirmed the reported symptom against 'Security Policy Exception Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SEC-015

---
