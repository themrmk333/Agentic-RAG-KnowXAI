# IT Support / Information Technology — Rich Historical Ticket Archive (wave2, Page 3)

## TCK3-IT-00090 — Offboarding (P4, In Progress)
**Created:** 2025-02-10 via Phone  |  **Requester:** Kavya Kapoor  |  **Assigned to:** Divya Rao

**Description:** Kavya Kapoor (Customer Support / Helpdesk) reported an issue via Phone related to 'IT Asset Return on Exit'. Category: Offboarding. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'IT Asset Return on Exit', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-IT-016

---

## TCK3-IT-00068 — Onboarding (P3, Resolved)
**Created:** 2025-02-15 via Walk-in  |  **Requester:** Ritika Mehta  |  **Assigned to:** Nisha Chauhan

**Description:** Ritika Mehta (Research & Development) reported an issue via Walk-in related to 'New Employee IT Onboarding'. Category: Onboarding. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'New Employee IT Onboarding', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-IT-007 to resolve. HR notifies the relevant department and the MK-ServiceDesk owner ahead of the employee's start or end date. the IT Support Engineer prepares the required IT Onboarding Kit, including a provisioned laptop, email account, VPN profile, and required software. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The IT Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-IT-007

---

## TCK3-IT-00146 — Offboarding (P3, Resolved)
**Created:** 2025-02-20 via Email  |  **Requester:** Dev Pillai  |  **Assigned to:** Gaurav Sharma

**Description:** Dev Pillai (Software Engineering / Development) reported an issue via Email related to 'Employee Offboarding IT Checklist'. Category: Offboarding. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Employee Offboarding IT Checklist', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-IT-008 to resolve. HR notifies the relevant department and the MK-ServiceDesk owner ahead of the employee's start or end date. the IT Support Engineer prepares the required IT Offboarding Checklist, including disabling the account, wiping the device, and revoking VPN/SSO access. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The IT Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-IT-008

---

## TCK3-IT-00069 — Email (P3, Resolved)
**Created:** 2025-02-21 via Portal  |  **Requester:** Ananya Nair  |  **Assigned to:** Nisha Chauhan

**Description:** Ananya Nair (Cybersecurity / Information Security) reported an issue via Portal related to 'Corporate Email Account Setup'. Category: Email. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Corporate Email Account Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-IT-010 to resolve. the IT Support Engineer confirms eligibility and prerequisites: the employee's full name, department, and manager for the distribution list. the IT Support Engineer raises a request in MK-ServiceDesk specifying exactly which Email Account is required. The IT Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Email Account in the relevant system. the IT Support Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-010

---

## TCK3-IT-00062 — Asset Management (P4, Closed)
**Created:** 2025-03-11 via Email  |  **Requester:** Rohan Iyer  |  **Assigned to:** Divya Rao

**Description:** Rohan Iyer (Marketing) reported an issue via Email related to 'Asset Tagging and Inventory Update'. Category: Asset Management. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Asset Tagging and Inventory Update', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-IT-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ServiceDesk. the IT Support Engineer gathers the required data and documents, including serial numbers, purchase dates, and current assignees for all devices. The review team examines the IT Asset Register against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The IT Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-IT-013

---

## TCK3-IT-00096 — Mobile Devices (P3, Closed)
**Created:** 2025-03-12 via Live Chat  |  **Requester:** Bhavna Kapoor  |  **Assigned to:** Divya Rao

**Description:** Bhavna Kapoor (Project Management / PMO) reported an issue via Live Chat related to 'Mobile Device Enrollment (MDM)'. Category: Mobile Devices. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Mobile Device Enrollment (MDM)', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-IT-015 to resolve. the employee confirms eligibility and prerequisites: installing the MK-MDM profile and accepting the corporate device management policy. the employee raises a request in MK-ServiceDesk specifying exactly which MDM Enrollment is required. The IT Support Engineer reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the MDM Enrollment in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-015

---

## TCK3-IT-00104 — Account Access (P4, Resolved)
**Created:** 2025-03-12 via Phone  |  **Requester:** Gaurav Chowdhury  |  **Assigned to:** Divya Joshi

**Description:** Gaurav Chowdhury (Marketing) reported an issue via Phone related to 'Password Reset Procedure'. Category: Account Access. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Password Reset Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-IT-001 to resolve. the employee confirms the exact symptom, when it started, and whether it affects one system or several. the employee performs the standard first-line check: verifying that Caps Lock is off and trying the reset link on MK-ServiceDesk. If the issue persists, the employee applies the documented workaround for this issue type. the employee checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the employee raises a ticket in MK-ServiceDesk categorised under 'Account Access', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-001

---

## TCK3-IT-00109 — Hardware (P3, Resolved)
**Created:** 2025-03-13 via Live Chat  |  **Requester:** Bhavna Gupta  |  **Assigned to:** Vikram Bose

**Description:** Bhavna Gupta (Legal & Compliance) reported an issue via Live Chat related to 'New Hardware Request Fulfillment'. Category: Hardware. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'New Hardware Request Fulfillment', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-IT-002 to resolve. the employee logs into MK-ServiceDesk and navigates to the 'Hardware Request' section. the employee selects 'New Hardware Request' and enters the required details, including device type, business justification, and cost centre. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Hardware Request; MK-ServiceDesk automatically routes it to the IT Manager for review. The IT Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-IT-002

---

## TCK3-IT-00036 — Network (P3, Resolved)
**Created:** 2025-03-15 via Portal  |  **Requester:** Aman Pillai  |  **Assigned to:** Varun Nair

**Description:** Aman Pillai (Data & Analytics) reported an issue via Portal related to 'Corporate VPN Access Setup'. Category: Network. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Corporate VPN Access Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-IT-004 to resolve. the employee confirms eligibility and prerequisites: manager approval and a valid business need for remote access. the employee raises a request in MK-ServiceDesk specifying exactly which VPN Access is required. The System Administrator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the VPN Access in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-004

---

## TCK3-IT-00074 — Hardware (P3, Resolved)
**Created:** 2025-03-21 via Phone  |  **Requester:** Bhavna Gupta  |  **Assigned to:** Kabir Agarwal

**Description:** Bhavna Gupta (Legal & Compliance) reported an issue via Phone related to 'Printer and Peripheral Setup'. Category: Hardware. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Printer and Peripheral Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-IT-011 to resolve. the employee confirms eligibility and prerequisites: the printer/peripheral model and the employee's floor/office location. the employee raises a request in MK-ServiceDesk specifying exactly which Peripheral Setup is required. The IT Support Engineer reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Peripheral Setup in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-011

---

## TCK3-IT-00071 — Hardware (P4, In Progress)
**Created:** 2025-03-23 via Slack  |  **Requester:** Vivek Chauhan  |  **Assigned to:** Kabir Agarwal

**Description:** Vivek Chauhan (Marketing) reported an issue via Slack related to 'Laptop Replacement Process'. Category: Hardware. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Laptop Replacement Process', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-005

---

## TCK3-IT-00147 — Asset Management (P4, Resolved)
**Created:** 2025-04-10 via Email  |  **Requester:** Shreya Kapoor  |  **Assigned to:** Ananya Nair

**Description:** Shreya Kapoor (Cybersecurity / Information Security) reported an issue via Email related to 'Asset Tagging and Inventory Update'. Category: Asset Management. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Asset Tagging and Inventory Update', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-IT-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ServiceDesk. the IT Support Engineer gathers the required data and documents, including serial numbers, purchase dates, and current assignees for all devices. The review team examines the IT Asset Register against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The IT Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-IT-013

---

## TCK3-IT-00089 — Support Operations (P2, Closed)
**Created:** 2025-04-13 via Phone  |  **Requester:** Siddharth Mehta  |  **Assigned to:** Divya Rao

**Description:** Siddharth Mehta (DevOps & Cloud) reported an issue via Phone related to 'IT Ticket Escalation Procedure'. Category: Support Operations. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'IT Ticket Escalation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-IT-012 to resolve. the IT Support Engineer confirms the exact symptom, when it started, and whether it affects one system or several. the IT Support Engineer performs the standard first-line check: reviewing the ticket SLA timer in MK-ServiceDesk. If the issue persists, the IT Support Engineer applies the documented workaround for this issue type. the IT Support Engineer checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the IT Support Engineer raises a ticket in MK-ServiceDesk categorised under 'Ticket Escalation', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-012

---

## TCK3-IT-00029 — Offboarding (P3, Resolved)
**Created:** 2025-04-14 via Walk-in  |  **Requester:** Sahil Menon  |  **Assigned to:** Arjun Pillai

**Description:** Sahil Menon (QA / Testing) reported an issue via Walk-in related to 'Employee Offboarding IT Checklist'. Category: Offboarding. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Employee Offboarding IT Checklist', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-IT-008 to resolve. HR notifies the relevant department and the MK-ServiceDesk owner ahead of the employee's start or end date. the IT Support Engineer prepares the required IT Offboarding Checklist, including disabling the account, wiping the device, and revoking VPN/SSO access. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The IT Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-IT-008

---

## TCK3-IT-00080 — Network (P3, Resolved)
**Created:** 2025-04-28 via Live Chat  |  **Requester:** Tanya Singh  |  **Assigned to:** Arjun Pillai

**Description:** Tanya Singh (Software Engineering / Development) reported an issue via Live Chat related to 'Corporate VPN Access Setup'. Category: Network. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Corporate VPN Access Setup', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-IT-004 to resolve. the employee confirms eligibility and prerequisites: manager approval and a valid business need for remote access. the employee raises a request in MK-ServiceDesk specifying exactly which VPN Access is required. The System Administrator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the VPN Access in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-004

---

## TCK3-IT-00039 — Account Access (P3, Closed)
**Created:** 2025-04-30 via Phone  |  **Requester:** Karan Bhatt  |  **Assigned to:** Simran Verma

**Description:** Karan Bhatt (DevOps & Cloud) reported an issue via Phone related to 'Password Reset Procedure'. Category: Account Access. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Password Reset Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The user's local environment/device had a conflicting setting that wasn't present on other machines.

**Resolution:** Followed SOP-IT-001 to resolve. the employee confirms the exact symptom, when it started, and whether it affects one system or several. the employee performs the standard first-line check: verifying that Caps Lock is off and trying the reset link on MK-ServiceDesk. If the issue persists, the employee applies the documented workaround for this issue type. the employee checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the employee raises a ticket in MK-ServiceDesk categorised under 'Account Access', attaching screenshots or error logs.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-001

---

## TCK3-IT-00106 — Support Operations (P4, Resolved)
**Created:** 2025-04-30 via Phone  |  **Requester:** Harsh Joshi  |  **Assigned to:** Neel Menon

**Description:** Harsh Joshi (Marketing) reported an issue via Phone related to 'Remote Desktop / Screen Share Support Session'. Category: Support Operations. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Remote Desktop / Screen Share Support Session', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-IT-014 to resolve. the employee confirms the exact symptom, when it started, and whether it affects one system or several. the employee performs the standard first-line check: confirming the employee's consent before starting a remote session via MK-ServiceDesk Remote. If the issue persists, the employee applies the documented workaround for this issue type. the employee checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the employee raises a ticket in MK-ServiceDesk categorised under 'Remote Support Session', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-014

---

## TCK3-IT-00065 — Offboarding (P3, Resolved)
**Created:** 2025-05-07 via Email  |  **Requester:** Tanya Mehta  |  **Assigned to:** Arjun Pillai

**Description:** Tanya Mehta (Human Resources) reported an issue via Email related to 'Employee Offboarding IT Checklist'. Category: Offboarding. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Employee Offboarding IT Checklist', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-IT-008 to resolve. HR notifies the relevant department and the MK-ServiceDesk owner ahead of the employee's start or end date. the IT Support Engineer prepares the required IT Offboarding Checklist, including disabling the account, wiping the device, and revoking VPN/SSO access. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The IT Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-IT-008

---

## TCK3-IT-00113 — Network (P2, Closed)
**Created:** 2025-05-11 via Live Chat  |  **Requester:** Shreya Reddy  |  **Assigned to:** Aditya Menon

**Description:** Shreya Reddy (Product Management) reported an issue via Live Chat related to 'Corporate Wi-Fi Troubleshooting Escalation'. Category: Network. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Corporate Wi-Fi Troubleshooting Escalation', and checked recent related changes before identifying the cause below.

**Root Cause:** The issue was caused by a stale cache that hadn't refreshed after a recent update.

**Resolution:** Followed SOP-IT-006 to resolve. the employee confirms the exact symptom, when it started, and whether it affects one system or several. the employee performs the standard first-line check: toggling Wi-Fi off/on and confirming Airplane Mode is disabled. If the issue persists, the employee applies the documented workaround for this issue type. the employee checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the employee raises a ticket in MK-ServiceDesk categorised under 'Network Connectivity', attaching screenshots or error logs.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-IT-006

---

## TCK3-IT-00131 — Hardware (P3, Resolved)
**Created:** 2025-05-24 via Live Chat  |  **Requester:** Vikram Mehta  |  **Assigned to:** Ananya Gupta

**Description:** Vikram Mehta (DevOps & Cloud) reported an issue via Live Chat related to 'Laptop Replacement Process'. Category: Hardware. Logged against MK-ServiceDesk.

**Investigation:** The assigned specialist reviewed the MK-ServiceDesk record, confirmed the reported symptom against 'Laptop Replacement Process', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-IT-005 to resolve. the employee confirms eligibility and prerequisites: the asset tag of the current device and the reason for replacement. the employee raises a request in MK-ServiceDesk specifying exactly which Laptop Replacement is required. The IT Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Laptop Replacement in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-IT-005

---