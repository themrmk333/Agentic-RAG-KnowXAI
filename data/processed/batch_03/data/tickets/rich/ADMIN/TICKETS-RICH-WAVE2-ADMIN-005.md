# Administration / Facilities — Rich Historical Ticket Archive (wave2, Page 5)

## TCK3-ADMIN-00044 — Facilities (P3, Resolved)
**Created:** 2025-09-12 via Live Chat  |  **Requester:** Tanya Singh  |  **Assigned to:** Rohan Sharma

**Description:** Tanya Singh (Software Engineering / Development) reported an issue via Live Chat related to 'Meeting Room Booking Procedure'. Category: Facilities. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Meeting Room Booking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ADMIN-003 to resolve. the employee confirms eligibility and prerequisites: booking through MK-FacilitiesDesk with attendee count and duration. the employee raises a request in MK-FacilitiesDesk specifying exactly which Meeting Room Booking is required. The Facilities Coordinator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Meeting Room Booking in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-003

---

## TCK3-ADMIN-00134 — Facilities (P4, Resolved)
**Created:** 2025-09-14 via Slack  |  **Requester:** Harsh Malhotra  |  **Assigned to:** Nidhi Mehta

**Description:** Harsh Malhotra (Procurement / Purchasing) reported an issue via Slack related to 'Meeting Room Booking Procedure'. Category: Facilities. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Meeting Room Booking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ADMIN-003 to resolve. the employee confirms eligibility and prerequisites: booking through MK-FacilitiesDesk with attendee count and duration. the employee raises a request in MK-FacilitiesDesk specifying exactly which Meeting Room Booking is required. The Facilities Coordinator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Meeting Room Booking in the relevant system. the employee is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-003

---

## TCK3-ADMIN-00029 — Travel Administration (P2, Resolved)
**Created:** 2025-09-27 via Slack  |  **Requester:** Karan Pillai  |  **Assigned to:** Manoj Chauhan

**Description:** Karan Pillai (Product Management) reported an issue via Slack related to 'Business Travel Booking Procedure'. Category: Travel Administration. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Business Travel Booking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-ADMIN-008 to resolve. the employee logs into MK-FacilitiesDesk and navigates to the 'Travel Booking Request' section. the employee selects 'New Travel Booking Request' and enters the required details, including travel dates, destination, and budget category per travel policy. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Travel Booking Request; MK-FacilitiesDesk automatically routes it to the Reporting Manager for review. The Reporting Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-008

---

## TCK3-ADMIN-00025 — Facilities (P4, Resolved)
**Created:** 2025-10-19 via Portal  |  **Requester:** Tanya Sharma  |  **Assigned to:** Kabir Nair

**Description:** Tanya Sharma (Customer Support / Helpdesk) reported an issue via Portal related to 'Office Relocation/Seating Change Procedure'. Category: Facilities. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Relocation/Seating Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ADMIN-010 to resolve. the Facilities Coordinator confirms eligibility and prerequisites: updated floor plan and affected employee notifications. the Facilities Coordinator raises a request in MK-FacilitiesDesk specifying exactly which Seating Change Request is required. The Office Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Seating Change Request in the relevant system. the Facilities Coordinator is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-010

---

## TCK3-ADMIN-00108 — Budget Management (P4, Resolved)
**Created:** 2025-11-01 via Portal  |  **Requester:** Kavya Desai  |  **Assigned to:** Kabir Nair

**Description:** Kavya Desai (Procurement / Purchasing) reported an issue via Portal related to 'Office Budget and Vendor Invoice Approval (Admin)'. Category: Budget Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Budget and Vendor Invoice Approval (Admin)', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-ADMIN-014 to resolve. the Facilities Manager logs into MK-FacilitiesDesk and navigates to the 'Admin Invoice Approval' section. the Facilities Manager selects 'New Admin Invoice Approval' and enters the required details, including matching the invoice to the facility service contract. the Facilities Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Facilities Manager submits the Admin Invoice Approval; MK-FacilitiesDesk automatically routes it to the Finance Manager for review. The Finance Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-014

---

## TCK3-ADMIN-00094 — Budget Management (P1, In Progress)
**Created:** 2025-11-04 via Slack  |  **Requester:** Dev Mehta  |  **Assigned to:** Sneha Pillai

**Description:** Dev Mehta (Sales) reported an issue via Slack related to 'Office Budget and Vendor Invoice Approval (Admin)'. Category: Budget Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Budget and Vendor Invoice Approval (Admin)', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-014

---

## TCK3-ADMIN-00084 — Supplies (P4, Resolved)
**Created:** 2025-11-06 via Walk-in  |  **Requester:** Ritika Desai  |  **Assigned to:** Aditya Verma

**Description:** Ritika Desai (Marketing) reported an issue via Walk-in related to 'Office Supplies Replenishment Procedure'. Category: Supplies. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Supplies Replenishment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ADMIN-005 to resolve. the Facilities Executive confirms eligibility and prerequisites: stock levels checked weekly against the reorder threshold. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Supplies Request is required. The Admin Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Supplies Request in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-005

---

## TCK3-ADMIN-00087 — Facility Access (P3, Resolved)
**Created:** 2025-11-07 via Slack  |  **Requester:** Tanya Mehta  |  **Assigned to:** Rohan Sharma

**Description:** Tanya Mehta (Project Management / PMO) reported an issue via Slack related to 'Office Access Card Issuance Procedure'. Category: Facility Access. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Access Card Issuance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-ADMIN-002 to resolve. the Facilities Executive confirms eligibility and prerequisites: verifying employee ID and department before issuing the card. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Access Card is required. The Office Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Access Card in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-002

---

## TCK3-ADMIN-00072 — Visitor Management (P4, Resolved)
**Created:** 2025-11-14 via Portal  |  **Requester:** Simran Joshi  |  **Assigned to:** Nidhi Mehta

**Description:** Simran Joshi (Management / Leadership) reported an issue via Portal related to 'Visitor Management Procedure'. Category: Visitor Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Visitor Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ADMIN-006 to resolve. the receptionist confirms eligibility and prerequisites: pre-registration by the host employee and ID verification at entry. the receptionist raises a request in MK-FacilitiesDesk specifying exactly which Visitor Pass is required. The Facilities Coordinator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Visitor Pass in the relevant system. the receptionist is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-006

---

## TCK3-ADMIN-00049 — Mailroom (P4, Closed)
**Created:** 2025-11-15 via Portal  |  **Requester:** Vivek Singh  |  **Assigned to:** Aditya Nair

**Description:** Vivek Singh (Procurement / Purchasing) reported an issue via Portal related to 'Courier and Mail Handling Procedure'. Category: Mailroom. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Courier and Mail Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ADMIN-009 to resolve. the Facilities Executive confirms eligibility and prerequisites: recipient details and confirming contents comply with shipping policy. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Courier Request is required. The Admin Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Courier Request in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-009

---

## TCK3-ADMIN-00150 — Facility Access (P3, Resolved)
**Created:** 2025-11-24 via Walk-in  |  **Requester:** Bhavna Desai  |  **Assigned to:** Rohan Sharma

**Description:** Bhavna Desai (Project Management / PMO) reported an issue via Walk-in related to 'Office Access Card Issuance Procedure'. Category: Facility Access. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Access Card Issuance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ADMIN-002 to resolve. the Facilities Executive confirms eligibility and prerequisites: verifying employee ID and department before issuing the card. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Access Card is required. The Office Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Access Card in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-002

---

## TCK3-ADMIN-00061 — Facilities (P3, Resolved)
**Created:** 2025-11-25 via Phone  |  **Requester:** Aman Verma  |  **Assigned to:** Aditya Chauhan

**Description:** Aman Verma (Research & Development) reported an issue via Phone related to 'Office Relocation/Seating Change Procedure'. Category: Facilities. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Relocation/Seating Change Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ADMIN-010 to resolve. the Facilities Coordinator confirms eligibility and prerequisites: updated floor plan and affected employee notifications. the Facilities Coordinator raises a request in MK-FacilitiesDesk specifying exactly which Seating Change Request is required. The Office Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Seating Change Request in the relevant system. the Facilities Coordinator is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-010

---

## TCK3-ADMIN-00028 — Supplies (P1, Resolved)
**Created:** 2025-12-05 via Email  |  **Requester:** Divya Malhotra  |  **Assigned to:** Nidhi Mehta

**Description:** Divya Malhotra (Customer Support / Helpdesk) reported an issue via Email related to 'Office Supplies Replenishment Procedure'. Category: Supplies. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Supplies Replenishment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-ADMIN-005 to resolve. the Facilities Executive confirms eligibility and prerequisites: stock levels checked weekly against the reorder threshold. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Supplies Request is required. The Admin Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Supplies Request in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-005

---

## TCK3-ADMIN-00033 — Visitor Management (P3, Resolved)
**Created:** 2025-12-07 via Slack  |  **Requester:** Meera Pillai  |  **Assigned to:** Aditya Nair

**Description:** Meera Pillai (Research & Development) reported an issue via Slack related to 'Visitor Management Procedure'. Category: Visitor Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Visitor Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ADMIN-006 to resolve. the receptionist confirms eligibility and prerequisites: pre-registration by the host employee and ID verification at entry. the receptionist raises a request in MK-FacilitiesDesk specifying exactly which Visitor Pass is required. The Facilities Coordinator reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Visitor Pass in the relevant system. the receptionist is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-006

---

## TCK3-ADMIN-00121 — Visitor Management (P4, In Progress)
**Created:** 2025-12-20 via Portal  |  **Requester:** Kavya Verma  |  **Assigned to:** Kabir Nair

**Description:** Kavya Verma (Administration / Facilities) reported an issue via Portal related to 'Visitor Management Procedure'. Category: Visitor Management. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Visitor Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-006

---

## TCK3-ADMIN-00098 — Facility Access (P3, Resolved)
**Created:** 2025-12-23 via Phone  |  **Requester:** Yash Malhotra  |  **Assigned to:** Manoj Chauhan

**Description:** Yash Malhotra (Management / Leadership) reported an issue via Phone related to 'Office Access Card Issuance Procedure'. Category: Facility Access. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Access Card Issuance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-ADMIN-002 to resolve. the Facilities Executive confirms eligibility and prerequisites: verifying employee ID and department before issuing the card. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Access Card is required. The Office Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Access Card in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-002

---

## TCK3-ADMIN-00069 — Mailroom (P4, Closed)
**Created:** 2025-12-28 via Slack  |  **Requester:** Preeti Desai  |  **Assigned to:** Rohan Sharma

**Description:** Preeti Desai (Legal & Compliance) reported an issue via Slack related to 'Courier and Mail Handling Procedure'. Category: Mailroom. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Courier and Mail Handling Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-ADMIN-009 to resolve. the Facilities Executive confirms eligibility and prerequisites: recipient details and confirming contents comply with shipping policy. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Courier Request is required. The Admin Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Courier Request in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-009

---

## TCK3-ADMIN-00057 — Facility Access (P4, Resolved)
**Created:** 2025-12-31 via Slack  |  **Requester:** Preeti Reddy  |  **Assigned to:** Manoj Chauhan

**Description:** Preeti Reddy (Management / Leadership) reported an issue via Slack related to 'Office Access Card Issuance Procedure'. Category: Facility Access. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Office Access Card Issuance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ADMIN-002 to resolve. the Facilities Executive confirms eligibility and prerequisites: verifying employee ID and department before issuing the card. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Access Card is required. The Office Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Access Card in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-002

---

## TCK3-ADMIN-00085 — Facilities (P3, Resolved)
**Created:** 2026-01-09 via Walk-in  |  **Requester:** Nisha Chauhan  |  **Assigned to:** Kabir Nair

**Description:** Nisha Chauhan (IT Support / Information Technology) reported an issue via Walk-in related to 'Cafeteria/Pantry Services Management Procedure'. Category: Facilities. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Cafeteria/Pantry Services Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-ADMIN-015 to resolve. the Facilities Executive confirms eligibility and prerequisites: coordinating with the catering vendor on menu and headcount. the Facilities Executive raises a request in MK-FacilitiesDesk specifying exactly which Pantry Services is required. The Admin Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Pantry Services in the relevant system. the Facilities Executive is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-ADMIN-015

---

## TCK3-ADMIN-00064 — Maintenance (P3, Closed)
**Created:** 2026-01-12 via Phone  |  **Requester:** Aman Bhatt  |  **Assigned to:** Shreya Iyer

**Description:** Aman Bhatt (Marketing) reported an issue via Phone related to 'Facility Maintenance Request Procedure'. Category: Maintenance. Logged against MK-FacilitiesDesk.

**Investigation:** The assigned specialist reviewed the MK-FacilitiesDesk record, confirmed the reported symptom against 'Facility Maintenance Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-ADMIN-004 to resolve. the employee logs into MK-FacilitiesDesk and navigates to the 'Maintenance Request' section. the employee selects 'New Maintenance Request' and enters the required details, including the issue location, description, and urgency level. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Maintenance Request; MK-FacilitiesDesk automatically routes it to the Facilities Coordinator for review. The Facilities Coordinator reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-ADMIN-004

---
