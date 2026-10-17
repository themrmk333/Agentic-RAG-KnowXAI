# IT Support / Information Technology — Rich Historical Ticket Archive (wave2, Page 6)

## TCK3-IT-00100 — Offboarding (P2, Resolved)
**Created:** 2026-03-02 via Slack  |  **Requester:** Kabir Reddy  |  **Assigned to:** Gaurav Sharma

**Description:** Kabir Reddy (QA / Testing) reported an issue via Slack related to 'Employee Offboarding IT Checklist'. Category: Offboarding. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Employee Offboarding IT Checklist', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-IT-008 to resolve. HR notifies the relevant department and the MK-ServiceDesk owner ahead of the employee's start or end date. the IT Support Engineer prepares the required IT Offboarding Checklist, including disabling the account, wiping the device, and revoking VPN/SSO access. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The IT Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-IT-008

---

## TCK3-IT-00121 — Hardware (P2, Closed)
**Created:** 2026-03-09 via Email  |  **Requester:** Kabir Chauhan  |  **Assigned to:** Kabir Agarwal

**Description:** Kabir Chauhan (Sales) reported an issue via Email related to 'New Hardware Request Fulfillment'. Category: Hardware. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'New Hardware Request Fulfillment', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-IT-002 to resolve. the employee logs into MK-ServiceDesk and navigates to the 'Hardware Request' section. the employee selects 'New Hardware Request' and enters the required details, including device type, business justification, and cost centre. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Hardware Request; MK-ServiceDesk automatically routes it to the IT Manager for review. The IT Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-IT-002

---

## TCK3-IT-00138 — Access Management (P3, Closed)
**Created:** 2026-03-10 via Email  |  **Requester:** Rohan Sharma  |  **Assigned to:** Simran Verma

**Description:** Rohan Sharma (Administration / Facilities) reported an issue via Email related to 'Server Access Request Procedure'. Category: Access Management. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Server Access Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-IT-009 to resolve. the employee confirms eligibility and prerequisites: the specific server name, environment, and business justification. the employee raises a request in MK-ServiceDesk specifying exactly which Server Access is required. The System Administrator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Server Access in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-009

---

## TCK3-IT-00032 — Software (P3, Closed)
**Created:** 2026-04-01 via Walk-in  |  **Requester:** Dev Chauhan  |  **Assigned to:** Ananya Nair

**Description:** Dev Chauhan (Marketing) reported an issue via Walk-in related to 'Software Installation Request'. Category: Software. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Software Installation Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-IT-003 to resolve. the employee logs into MK-ServiceDesk and navigates to the 'Software Request' section. the employee selects 'New Software Request' and enters the required details, including the software name, version, and licence type required. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Software Request; MK-ServiceDesk automatically routes it to the IT Support Engineer for review. The IT Support Engineer reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-IT-003

---

## TCK3-IT-00044 — Hardware (P3, Resolved)
**Created:** 2026-04-08 via Portal  |  **Requester:** Aditya Desai  |  **Assigned to:** Isha Pillai

**Description:** Aditya Desai (Management / Leadership) reported an issue via Portal related to 'New Hardware Request Fulfillment'. Category: Hardware. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'New Hardware Request Fulfillment', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-IT-002 to resolve. the employee logs into MK-ServiceDesk and navigates to the 'Hardware Request' section. the employee selects 'New Hardware Request' and enters the required details, including device type, business justification, and cost centre. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Hardware Request; MK-ServiceDesk automatically routes it to the IT Manager for review. The IT Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-IT-002

---

## TCK3-IT-00093 — Account Access (P3, Resolved)
**Created:** 2026-04-13 via Email  |  **Requester:** Swati Chowdhury  |  **Assigned to:** Gaurav Sharma

**Description:** Swati Chowdhury (Cybersecurity / Information Security) reported an issue via Email related to 'Password Reset Procedure'. Category: Account Access. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Password Reset Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-IT-001 to resolve. the employee confirms the exact symptom, when it started, and whether it affects one system or several. the employee performs the standard first-line check: verifying that Caps Lock is off and trying the reset link on MK-ServiceDesk. If the issue persists, the employee applies the documented workaround for this issue type. the employee checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the employee raises a ticket in MK-ServiceDesk categorised under 'Account Access', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-001

---

## TCK3-IT-00077 — Hardware (P3, Closed)
**Created:** 2026-04-23 via Portal  |  **Requester:** Arjun Chowdhury  |  **Assigned to:** Aditya Menon

**Description:** Arjun Chowdhury (Finance & Accounting) reported an issue via Portal related to 'Printer and Peripheral Setup'. Category: Hardware. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Printer and Peripheral Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-IT-011 to resolve. the employee confirms eligibility and prerequisites: the printer/peripheral model and the employee's floor/office location. the employee raises a request in MK-ServiceDesk specifying exactly which Peripheral Setup is required. The IT Support Engineer reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Peripheral Setup in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-011

---

## TCK3-IT-00040 — Hardware (P3, Closed)
**Created:** 2026-04-27 via Phone  |  **Requester:** Karan Pillai  |  **Assigned to:** Isha Pillai

**Description:** Karan Pillai (Product Management) reported an issue via Phone related to 'Printer and Peripheral Setup'. Category: Hardware. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Printer and Peripheral Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-IT-011 to resolve. the employee confirms eligibility and prerequisites: the printer/peripheral model and the employee's floor/office location. the employee raises a request in MK-ServiceDesk specifying exactly which Peripheral Setup is required. The IT Support Engineer reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Peripheral Setup in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-011

---

## TCK3-IT-00132 — Mobile Devices (P3, Resolved)
**Created:** 2026-04-29 via Walk-in  |  **Requester:** Swati Verma  |  **Assigned to:** Varun Nair

**Description:** Swati Verma (Human Resources) reported an issue via Walk-in related to 'Mobile Device Enrollment (MDM)'. Category: Mobile Devices. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Mobile Device Enrollment (MDM)', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-IT-015 to resolve. the employee confirms eligibility and prerequisites: installing the MK-MDM profile and accepting the corporate device management policy. the employee raises a request in MK-ServiceDesk specifying exactly which MDM Enrollment is required. The IT Support Engineer reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the MDM Enrollment in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-015

---

## TCK3-IT-00033 — Access Management (P2, Resolved)
**Created:** 2026-05-08 via Slack  |  **Requester:** Isha Agarwal  |  **Assigned to:** Ananya Nair

**Description:** Isha Agarwal (Human Resources) reported an issue via Slack related to 'Server Access Request Procedure'. Category: Access Management. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Server Access Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-IT-009 to resolve. the employee confirms eligibility and prerequisites: the specific server name, environment, and business justification. the employee raises a request in MK-ServiceDesk specifying exactly which Server Access is required. The System Administrator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Server Access in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-009

---

## TCK3-IT-00053 — Software (P3, Resolved)
**Created:** 2026-05-08 via Email  |  **Requester:** Gaurav Malhotra  |  **Assigned to:** Varun Nair

**Description:** Gaurav Malhotra (Procurement / Purchasing) reported an issue via Email related to 'Software Installation Request'. Category: Software. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Software Installation Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-IT-003 to resolve. the employee logs into MK-ServiceDesk and navigates to the 'Software Request' section. the employee selects 'New Software Request' and enters the required details, including the software name, version, and licence type required. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Software Request; MK-ServiceDesk automatically routes it to the IT Support Engineer for review. The IT Support Engineer reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-IT-003

---

## TCK3-IT-00063 — Access Management (P3, In Progress)
**Created:** 2026-05-08 via Portal  |  **Requester:** Kavya Bhatt  |  **Assigned to:** Simran Verma

**Description:** Kavya Bhatt (Procurement / Purchasing) reported an issue via Portal related to 'Server Access Request Procedure'. Category: Access Management. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Server Access Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-009

---

## TCK3-IT-00078 — Network (P3, Resolved)
**Created:** 2026-05-08 via Portal  |  **Requester:** Riya Pillai  |  **Assigned to:** Divya Rao

**Description:** Riya Pillai (Legal & Compliance) reported an issue via Portal related to 'Corporate Wi-Fi Troubleshooting Escalation'. Category: Network. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Corporate Wi-Fi Troubleshooting Escalation', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-IT-006 to resolve. the employee confirms the exact symptom, when it started, and whether it affects one system or several. the employee performs the standard first-line check: toggling Wi-Fi off/on and confirming Airplane Mode is disabled. If the issue persists, the employee applies the documented workaround for this issue type. the employee checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the employee raises a ticket in MK-ServiceDesk categorised under 'Network Connectivity', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-006

---

## TCK3-IT-00073 — Hardware (P3, Resolved)
**Created:** 2026-05-09 via Walk-in  |  **Requester:** Simran Joshi  |  **Assigned to:** Nisha Chauhan

**Description:** Simran Joshi (Management / Leadership) reported an issue via Walk-in related to 'New Hardware Request Fulfillment'. Category: Hardware. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'New Hardware Request Fulfillment', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-IT-002 to resolve. the employee logs into MK-ServiceDesk and navigates to the 'Hardware Request' section. the employee selects 'New Hardware Request' and enters the required details, including device type, business justification, and cost centre. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Hardware Request; MK-ServiceDesk automatically routes it to the IT Manager for review. The IT Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-IT-002

---

## TCK3-IT-00059 — Offboarding (P2, In Progress)
**Created:** 2026-05-10 via Walk-in  |  **Requester:** Aditya Verma  |  **Assigned to:** Swati Malhotra

**Description:** Aditya Verma (Administration / Facilities) reported an issue via Walk-in related to 'IT Asset Return on Exit'. Category: Offboarding. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'IT Asset Return on Exit', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-IT-016

---

## TCK3-IT-00129 — Account Access (P2, Resolved)
**Created:** 2026-05-14 via Portal  |  **Requester:** Bhavna Pillai  |  **Assigned to:** Simran Verma

**Description:** Bhavna Pillai (Sales) reported an issue via Portal related to 'Password Reset Procedure'. Category: Account Access. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Password Reset Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-IT-001 to resolve. the employee confirms the exact symptom, when it started, and whether it affects one system or several. the employee performs the standard first-line check: verifying that Caps Lock is off and trying the reset link on MK-ServiceDesk. If the issue persists, the employee applies the documented workaround for this issue type. the employee checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the employee raises a ticket in MK-ServiceDesk categorised under 'Account Access', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-001

---

## TCK3-IT-00124 — Network (P4, Resolved)
**Created:** 2026-05-15 via Slack  |  **Requester:** Ananya Menon  |  **Assigned to:** Varun Nair

**Description:** Ananya Menon (Human Resources) reported an issue via Slack related to 'Corporate VPN Access Setup'. Category: Network. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Corporate VPN Access Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-IT-004 to resolve. the employee confirms eligibility and prerequisites: manager approval and a valid business need for remote access. the employee raises a request in MK-ServiceDesk specifying exactly which VPN Access is required. The System Administrator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the VPN Access in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-004

---

## TCK3-IT-00140 — Support Operations (P1, Resolved)
**Created:** 2026-05-30 via Phone  |  **Requester:** Aman Nair  |  **Assigned to:** Simran Verma

**Description:** Aman Nair (Finance & Accounting) reported an issue via Phone related to 'IT Ticket Escalation Procedure'. Category: Support Operations. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'IT Ticket Escalation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-IT-012 to resolve. the IT Support Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the IT Support Engineer performs the standard first-line check: reviewing the ticket SLA timer in MK-ServiceDesk. If the issue persists, the IT Support Engineer applies the documented workaround for this issue type. the IT Support Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the IT Support Engineer raises a ticket in MK-ServiceDesk categorised under 'Ticket Escalation', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-012

---

## TCK3-IT-00057 — Support Operations (P4, Closed)
**Created:** 2026-06-01 via Phone  |  **Requester:** Meera Pillai  |  **Assigned to:** Ananya Gupta

**Description:** Meera Pillai (Research & Development) reported an issue via Phone related to 'Remote Desktop / Screen Share Support Session'. Category: Support Operations. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Remote Desktop / Screen Share Support Session', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-IT-014 to resolve. the employee confirms the exact symptom, when it started, and whether it affects one system or several. the employee performs the standard first-line check: confirming the employee's consent before starting a remote session via MK-ServiceDesk Remote. If the issue persists, the employee applies the documented workaround for this issue type. the employee checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the employee raises a ticket in MK-ServiceDesk categorised under 'Remote Support Session', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-014

---

## TCK3-IT-00133 — Offboarding (P1, Resolved)
**Created:** 2026-06-08 via Slack  |  **Requester:** Harsh Joshi  |  **Assigned to:** Divya Joshi

**Description:** Harsh Joshi (Marketing) reported an issue via Slack related to 'Employee Offboarding IT Checklist'. Category: Offboarding. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Employee Offboarding IT Checklist', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-IT-008 to resolve. HR notifies the relevant department and the MK-ServiceDesk owner ahead of the employee's start or end date. the IT Support Engineer prepares the required IT Offboarding Checklist, including disabling the account, wiping the device, and revoking VPN/SSO access. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The IT Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-IT-008

---