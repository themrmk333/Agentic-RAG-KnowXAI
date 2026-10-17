# Administration / Facilities — Rich Historical Ticket Archive (wave2, Page 4)

## TCK3-ADMIN-00036 — Facility Access (P3, Resolved)
**Created:** 2025-06-02 via Portal  |  **Requester:** Simran Gupta  |  **Assigned to:** Aditya Chauhan

**Description:** Simran Gupta (Management / Leadership) reported an issue via Portal related to 'Vendor Access for Facility Work Procedure'. Category: Facility Access. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Vendor Access for Facility Work Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ADMIN-011 to resolve. the Facilities Coordinator confirms eligibility and prerequisites: verifying vendor ID and scope of work before granting building access. the Facilities Coordinator raises a request in MK-FacilitiesDesk specifying exactly which Vendor Facility Access is required. The Facilities Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Vendor Facility Access in the relevant system. the Facilities Coordinator is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-011

---

## TCK3-ADMIN-00124 — Budget Management (P3, Resolved)
**Created:** 2025-06-02 via Phone  |  **Requester:** Arjun Verma  |  **Assigned to:** Shreya Iyer

**Description:** Arjun Verma (Administration / Facilities) reported an issue via Phone related to 'Office Budget and Vendor Invoice Approval (Admin)'. Category: Budget Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Budget and Vendor Invoice Approval (Admin)', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-ADMIN-014 to resolve. the Facilities Manager logs into MK-FacilitiesDesk and navigates to the 'Admin Invoice Approval' section. the Facilities Manager selects 'New Admin Invoice Approval' and enters the required details, including matching the invoice to the facility service contract. the Facilities Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Facilities Manager submits the Admin Invoice Approval; MK-FacilitiesDesk automatically routes it to the Finance Manager for review. The Finance Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-014

---

## TCK3-ADMIN-00062 — Health & Safety (P2, Closed)
**Created:** 2025-06-05 via Live Chat  |  **Requester:** Swati Verma  |  **Assigned to:** Preeti Desai

**Description:** Swati Verma (Human Resources) reported an issue via Live Chat related to 'Office Safety Drill Procedure'. Category: Health & Safety. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Safety Drill Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-ADMIN-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-FacilitiesDesk. the Facilities Manager gathers the required data and documents, including evacuation time, headcount reconciliation, and identified gaps. The review team examines the Safety Drill Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Head of Administration discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-ADMIN-007

---

## TCK3-ADMIN-00145 — Mailroom (P3, Resolved)
**Created:** 2025-06-06 via Email  |  **Requester:** Arjun Gupta  |  **Assigned to:** Nidhi Mehta

**Description:** Arjun Gupta (Data & Analytics) reported an issue via Email related to 'Courier and Mail Handling Procedure'. Category: Mailroom. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Courier and Mail Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ADMIN-009 to resolve. the Facilities Executive confirms eligibility and prerequisites: recipient details and confirming contents comply with shipping policy. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Courier Request is required. The Admin Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Courier Request in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-009

---

## TCK3-ADMIN-00092 — Health & Safety (P4, Resolved)
**Created:** 2025-06-14 via Live Chat  |  **Requester:** Dev Pillai  |  **Assigned to:** Aditya Nair

**Description:** Dev Pillai (Software Engineering / Development) reported an issue via Live Chat related to 'Emergency Evacuation Procedure'. Category: Health & Safety. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Emergency Evacuation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent configuration change had an unintended side effect on this specific workflow.

**Resolution:** Followed SOP-ADMIN-013 to resolve. the Facilities Coordinator confirms the exact symptom, when it started, and whether it affects one system or several. the Facilities Coordinator performs the standard first-line check: triggering the building alarm and directing employees to assembly points. If the issue persists, the Facilities Coordinator applies the documented workaround for this issue type. the Facilities Coordinator checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Facilities Coordinator raises a ticket in MK-FacilitiesDesk categorised under 'Emergency Evacuation', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-ADMIN-013

---

## TCK3-ADMIN-00095 — Budget Management (P3, Resolved)
**Created:** 2025-06-16 via Live Chat  |  **Requester:** Shreya Reddy  |  **Assigned to:** Kavya Verma

**Description:** Shreya Reddy (Cybersecurity / Information Security) reported an issue via Live Chat related to 'Office Budget and Vendor Invoice Approval (Admin)'. Category: Budget Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Budget and Vendor Invoice Approval (Admin)', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-ADMIN-014 to resolve. the Facilities Manager logs into MK-FacilitiesDesk and navigates to the 'Admin Invoice Approval' section. the Facilities Manager selects 'New Admin Invoice Approval' and enters the required details, including matching the invoice to the facility service contract. the Facilities Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Facilities Manager submits the Admin Invoice Approval; MK-FacilitiesDesk automatically routes it to the Finance Manager for review. The Finance Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-014

---

## TCK3-ADMIN-00110 — Facilities (P4, In Progress)
**Created:** 2025-06-19 via Slack  |  **Requester:** Varun Nair  |  **Assigned to:** Arjun Verma

**Description:** Varun Nair (IT Support / Information Technology) reported an issue via Slack related to 'Office Relocation/Seating Change Procedure'. Category: Facilities. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Relocation/Seating Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-010

---

## TCK3-ADMIN-00132 — Health & Safety (P3, Closed)
**Created:** 2025-06-23 via Phone  |  **Requester:** Arjun Chowdhury  |  **Assigned to:** Manoj Chauhan

**Description:** Arjun Chowdhury (Finance & Accounting) reported an issue via Phone related to 'Emergency Evacuation Procedure'. Category: Health & Safety. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Emergency Evacuation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency on another team's system was degraded at the time, causing a cascading symptom here.

**Resolution:** Followed SOP-ADMIN-013 to resolve. the Facilities Coordinator confirms the exact symptom, when it started, and whether it affects one system or several. the Facilities Coordinator performs the standard first-line check: triggering the building alarm and directing employees to assembly points. If the issue persists, the Facilities Coordinator applies the documented workaround for this issue type. the Facilities Coordinator checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Facilities Coordinator raises a ticket in MK-FacilitiesDesk categorised under 'Emergency Evacuation', attaching screenshots or error logs.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-ADMIN-013

---

## TCK3-ADMIN-00146 — Facilities (P3, Resolved)
**Created:** 2025-06-27 via Phone  |  **Requester:** Neel Joshi  |  **Assigned to:** Aditya Nair

**Description:** Neel Joshi (DevOps & Cloud) reported an issue via Phone related to 'Cafeteria/Pantry Services Management Procedure'. Category: Facilities. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Cafeteria/Pantry Services Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ADMIN-015 to resolve. the Facilities Executive confirms eligibility and prerequisites: coordinating with the catering vendor on menu and headcount. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Pantry Services is required. The Admin Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Pantry Services in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-015

---

## TCK3-ADMIN-00109 — Mailroom (P3, Resolved)
**Created:** 2025-06-29 via Walk-in  |  **Requester:** Dev Sharma  |  **Assigned to:** Kavya Verma

**Description:** Dev Sharma (Product Management) reported an issue via Walk-in related to 'Courier and Mail Handling Procedure'. Category: Mailroom. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Courier and Mail Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ADMIN-009 to resolve. the Facilities Executive confirms eligibility and prerequisites: recipient details and confirming contents comply with shipping policy. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Courier Request is required. The Admin Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Courier Request in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-009

---

## TCK3-ADMIN-00135 — Travel Administration (P3, Closed)
**Created:** 2025-07-06 via Email  |  **Requester:** Meera Chauhan  |  **Assigned to:** Arjun Verma

**Description:** Meera Chauhan (Procurement / Purchasing) reported an issue via Email related to 'Business Travel Booking Procedure'. Category: Travel Administration. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Business Travel Booking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-ADMIN-008 to resolve. the employee logs into MK-FacilitiesDesk and navigates to the 'Travel Booking Request' section. the employee selects 'New Travel Booking Request' and enters the required details, including travel dates, destination, and budget category per travel policy. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Travel Booking Request; MK-FacilitiesDesk automatically routes it to the Reporting Manager for review. The Reporting Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-008

---

## TCK3-ADMIN-00065 — Visitor Management (P3, Closed)
**Created:** 2025-07-10 via Walk-in  |  **Requester:** Rahul Pillai  |  **Assigned to:** Sneha Pillai

**Description:** Rahul Pillai (Software Engineering / Development) reported an issue via Walk-in related to 'Visitor Management Procedure'. Category: Visitor Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Visitor Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ADMIN-006 to resolve. the receptionist confirms eligibility and prerequisites: pre-registration by the host employee and ID verification at entry. the receptionist raises a request in MK-FacilitiesDesk specifying exactly which Visitor Pass is required. The Facilities Coordinator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Visitor Pass in the relevant system. the receptionist is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-006

---

## TCK3-ADMIN-00073 — Budget Management (P3, Resolved)
**Created:** 2025-07-14 via Email  |  **Requester:** Aditya Rao  |  **Assigned to:** Aditya Verma

**Description:** Aditya Rao (Procurement / Purchasing) reported an issue via Email related to 'Office Budget and Vendor Invoice Approval (Admin)'. Category: Budget Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Budget and Vendor Invoice Approval (Admin)', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-ADMIN-014 to resolve. the Facilities Manager logs into MK-FacilitiesDesk and navigates to the 'Admin Invoice Approval' section. the Facilities Manager selects 'New Admin Invoice Approval' and enters the required details, including matching the invoice to the facility service contract. the Facilities Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Facilities Manager submits the Admin Invoice Approval; MK-FacilitiesDesk automatically routes it to the Finance Manager for review. The Finance Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-014

---

## TCK3-ADMIN-00021 — Facility Access (P3, Resolved)
**Created:** 2025-07-20 via Portal  |  **Requester:** Manoj Chauhan  |  **Assigned to:** Manoj Chauhan

**Description:** Manoj Chauhan (Administration / Facilities) reported an issue via Portal related to 'Office Access Card Issuance Procedure'. Category: Facility Access. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Access Card Issuance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ADMIN-002 to resolve. the Facilities Executive confirms eligibility and prerequisites: verifying employee ID and department before issuing the card. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Access Card is required. The Office Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Access Card in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-002

---

## TCK3-ADMIN-00058 — Visitor Management (P1, Resolved)
**Created:** 2025-07-23 via Portal  |  **Requester:** Alisha Verma  |  **Assigned to:** Preeti Desai

**Description:** Alisha Verma (QA / Testing) reported an issue via Portal related to 'Visitor Management Procedure'. Category: Visitor Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Visitor Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ADMIN-006 to resolve. the receptionist confirms eligibility and prerequisites: pre-registration by the host employee and ID verification at entry. the receptionist raises a request in MK-FacilitiesDesk specifying exactly which Visitor Pass is required. The Facilities Coordinator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Visitor Pass in the relevant system. the receptionist is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-006

---

## TCK3-ADMIN-00086 — Mailroom (P3, Resolved)
**Created:** 2025-07-29 via Live Chat  |  **Requester:** Kavya Desai  |  **Assigned to:** Aditya Verma

**Description:** Kavya Desai (Procurement / Purchasing) reported an issue via Live Chat related to 'Courier and Mail Handling Procedure'. Category: Mailroom. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Courier and Mail Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ADMIN-009 to resolve. the Facilities Executive confirms eligibility and prerequisites: recipient details and confirming contents comply with shipping policy. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Courier Request is required. The Admin Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Courier Request in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-009

---

## TCK3-ADMIN-00130 — Facilities (P3, Resolved)
**Created:** 2025-08-20 via Walk-in  |  **Requester:** Ritika Agarwal  |  **Assigned to:** Rahul Nair

**Description:** Ritika Agarwal (Customer Support / Helpdesk) reported an issue via Walk-in related to 'Meeting Room Booking Procedure'. Category: Facilities. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Meeting Room Booking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ADMIN-003 to resolve. the employee confirms eligibility and prerequisites: booking through MK-FacilitiesDesk with attendee count and duration. the employee raises a request in MK-FacilitiesDesk specifying exactly which Meeting Room Booking is required. The Facilities Coordinator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Meeting Room Booking in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-003

---

## TCK3-ADMIN-00080 — Budget Management (P3, Resolved)
**Created:** 2025-08-25 via Live Chat  |  **Requester:** Preeti Desai  |  **Assigned to:** Rohan Sharma

**Description:** Preeti Desai (Legal & Compliance) reported an issue via Live Chat related to 'Office Budget and Vendor Invoice Approval (Admin)'. Category: Budget Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Budget and Vendor Invoice Approval (Admin)', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-ADMIN-014 to resolve. the Facilities Manager logs into MK-FacilitiesDesk and navigates to the 'Admin Invoice Approval' section. the Facilities Manager selects 'New Admin Invoice Approval' and enters the required details, including matching the invoice to the facility service contract. the Facilities Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Facilities Manager submits the Admin Invoice Approval; MK-FacilitiesDesk automatically routes it to the Finance Manager for review. The Finance Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-014

---

## TCK3-ADMIN-00125 — Facilities (P3, Closed)
**Created:** 2025-08-30 via Email  |  **Requester:** Kavya Iyer  |  **Assigned to:** Shreya Bhatt

**Description:** Kavya Iyer (Finance & Accounting) reported an issue via Email related to 'Office Relocation/Seating Change Procedure'. Category: Facilities. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Relocation/Seating Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ADMIN-010 to resolve. the Facilities Coordinator confirms eligibility and prerequisites: updated floor plan and affected employee notifications. the Facilities Coordinator raises a request in MK-FacilitiesDesk specifying exactly which Seating Change Request is required. The Office Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Seating Change Request in the relevant system. the Facilities Coordinator is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-010

---

## TCK3-ADMIN-00047 — Maintenance (P4, Closed)
**Created:** 2025-09-09 via Slack  |  **Requester:** Divya Menon  |  **Assigned to:** Kavya Verma

**Description:** Divya Menon (QA / Testing) reported an issue via Slack related to 'Facility Maintenance Request Procedure'. Category: Maintenance. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Facility Maintenance Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-ADMIN-004 to resolve. the employee logs into MK-FacilitiesDesk and navigates to the 'Maintenance Request' section. the employee selects 'New Maintenance Request' and enters the required details, including the issue location, description, and urgency level. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Maintenance Request; MK-FacilitiesDesk automatically routes it to the Facilities Coordinator for review. The Facilities Coordinator reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-004

---
