# Sales — Rich Historical Ticket Archive (wave2, Page 6)

## TCK3-SALES-00104 — Deal Approval (P3, Resolved)
**Created:** 2026-03-28 via Portal  |  **Requester:** Divya Gupta  |  **Assigned to:** Dev Mehta

**Description:** Divya Gupta (QA / Testing) reported an issue via Portal related to 'Discount Approval Procedure'. Category: Deal Approval. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Discount Approval Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SALES-003 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Discount Request' section. the Account Executive selects 'New Discount Request' and enters the required details, including deal size, competitive context, and margin impact. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Discount Request; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-003

---

## TCK3-SALES-00075 — Order Management (P3, Closed)
**Created:** 2026-03-31 via Phone  |  **Requester:** Priya Sharma  |  **Assigned to:** Nidhi Malhotra

**Description:** Priya Sharma (Data & Analytics) reported an issue via Phone related to 'Sales Order Booking Procedure'. Category: Order Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Order Booking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-SALES-016 to resolve. the Account Executive confirms eligibility and prerequisites: confirming signed contract terms match the order entered in MK-CRM. the Account Executive raises a request in MK-CRM specifying exactly which Sales Order is required. The Finance Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Sales Order in the relevant system. the Account Executive is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SALES-016

---

## TCK3-SALES-00116 — Compensation (P3, Closed)
**Created:** 2026-04-13 via Slack  |  **Requester:** Rohan Agarwal  |  **Assigned to:** Rohan Desai

**Description:** Rohan Agarwal (Cybersecurity / Information Security) reported an issue via Slack related to 'Sales Commission Calculation Procedure'. Category: Compensation. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Commission Calculation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-SALES-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CRM. the Sales Manager gathers the required data and documents, including closed-won deals, quota attainment, and accelerator tiers. The review team examines the Commission Calculation against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Finance Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SALES-012

---

## TCK3-SALES-00045 — Renewals (P3, Resolved)
**Created:** 2026-04-18 via Email  |  **Requester:** Pooja Menon  |  **Assigned to:** Rohan Singh

**Description:** Pooja Menon (Marketing) reported an issue via Email related to 'Customer Renewal Procedure'. Category: Renewals. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Customer Renewal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-SALES-007 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Renewal Request' section. the Account Executive selects 'New Renewal Request' and enters the required details, including usage history, satisfaction indicators, and proposed renewal terms. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Renewal Request; MK-CRM automatically routes it to the Sales Manager for review. The Sales Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-007

---

## TCK3-SALES-00081 — Lead Management (P3, Closed)
**Created:** 2026-04-19 via Portal  |  **Requester:** Anjali Iyer  |  **Assigned to:** Dev Mehta

**Description:** Anjali Iyer (Procurement / Purchasing) reported an issue via Portal related to 'New Lead Qualification Procedure'. Category: Lead Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'New Lead Qualification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-SALES-001 to resolve. the Sales Development Representative confirms eligibility and prerequisites: budget, authority, need, and timeline (BANT) criteria. the Sales Development Representative raises a request in MK-CRM specifying exactly which Lead Qualification is required. The Sales Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Lead Qualification in the relevant system. the Sales Development Representative is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SALES-001

---

## TCK3-SALES-00087 — Order Management (P2, Resolved)
**Created:** 2026-04-19 via Phone  |  **Requester:** Nisha Desai  |  **Assigned to:** Dev Mehta

**Description:** Nisha Desai (Project Management / PMO) reported an issue via Phone related to 'Sales Order Booking Procedure'. Category: Order Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Order Booking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-SALES-016 to resolve. the Account Executive confirms eligibility and prerequisites: confirming signed contract terms match the order entered in MK-CRM. the Account Executive raises a request in MK-CRM specifying exactly which Sales Order is required. The Finance Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Sales Order in the relevant system. the Account Executive is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SALES-016

---

## TCK3-SALES-00134 — Deal Approval (P4, Resolved)
**Created:** 2026-04-29 via Email  |  **Requester:** Preeti Menon  |  **Assigned to:** Tanya Malhotra

**Description:** Preeti Menon (QA / Testing) reported an issue via Email related to 'Discount Approval Procedure'. Category: Deal Approval. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Discount Approval Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SALES-003 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Discount Request' section. the Account Executive selects 'New Discount Request' and enters the required details, including deal size, competitive context, and margin impact. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Discount Request; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-003

---

## TCK3-SALES-00089 — Compensation (P3, Resolved)
**Created:** 2026-05-01 via Phone  |  **Requester:** Rohan Kapoor  |  **Assigned to:** Sahil Kapoor

**Description:** Rohan Kapoor (Marketing) reported an issue via Phone related to 'Sales Commission Calculation Procedure'. Category: Compensation. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Commission Calculation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-SALES-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CRM. the Sales Manager gathers the required data and documents, including closed-won deals, quota attainment, and accelerator tiers. The review team examines the Commission Calculation against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Finance Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SALES-012

---

## TCK3-SALES-00131 — Renewals (P2, Closed)
**Created:** 2026-05-01 via Phone  |  **Requester:** Ananya Bose  |  **Assigned to:** Dev Mehta

**Description:** Ananya Bose (DevOps & Cloud) reported an issue via Phone related to 'Customer Renewal Procedure'. Category: Renewals. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Customer Renewal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SALES-007 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Renewal Request' section. the Account Executive selects 'New Renewal Request' and enters the required details, including usage history, satisfaction indicators, and proposed renewal terms. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Renewal Request; MK-CRM automatically routes it to the Sales Manager for review. The Sales Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-007

---

## TCK3-SALES-00032 — Territory Management (P3, Closed)
**Created:** 2026-05-03 via Live Chat  |  **Requester:** Ritika Singh  |  **Assigned to:** Simran Gupta

**Description:** Ritika Singh (Human Resources) reported an issue via Live Chat related to 'Sales Territory Assignment Procedure'. Category: Territory Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Territory Assignment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SALES-008 to resolve. the Sales Manager logs into MK-CRM and navigates to the 'Territory Assignment' section. the Sales Manager selects 'New Territory Assignment' and enters the required details, including account list, geography, and capacity balancing. the Sales Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Sales Manager submits the Territory Assignment; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-008

---

## TCK3-SALES-00028 — Sales Enablement (P3, Resolved)
**Created:** 2026-05-05 via Email  |  **Requester:** Siddharth Chauhan  |  **Assigned to:** Tanya Malhotra

**Description:** Siddharth Chauhan (Procurement / Purchasing) reported an issue via Email related to 'Sales Enablement Content Request'. Category: Sales Enablement. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Enablement Content Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SALES-014 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Enablement Content Request' section. the Account Executive selects 'New Enablement Content Request' and enters the required details, including the use case and target audience for the requested material. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Enablement Content Request; MK-CRM automatically routes it to the Marketing Manager for review. The Marketing Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-014

---

## TCK3-SALES-00143 — Customer References (P4, Resolved)
**Created:** 2026-05-08 via Slack  |  **Requester:** Bhavna Pillai  |  **Assigned to:** Kabir Chauhan

**Description:** Bhavna Pillai (Sales) reported an issue via Slack related to 'Customer Reference Request Procedure'. Category: Customer References. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Customer Reference Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SALES-011 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Reference Request' section. the Account Executive selects 'New Reference Request' and enters the required details, including the target prospect profile and requested reference customer. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Reference Request; MK-CRM automatically routes it to the Marketing Manager for review. The Marketing Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-011

---

## TCK3-SALES-00039 — Sales Enablement (P2, Closed)
**Created:** 2026-05-16 via Live Chat  |  **Requester:** Simran Kapoor  |  **Assigned to:** Kabir Chauhan

**Description:** Simran Kapoor (Product Management) reported an issue via Live Chat related to 'Sales Enablement Content Request'. Category: Sales Enablement. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Enablement Content Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SALES-014 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Enablement Content Request' section. the Account Executive selects 'New Enablement Content Request' and enters the required details, including the use case and target audience for the requested material. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Enablement Content Request; MK-CRM automatically routes it to the Marketing Manager for review. The Marketing Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-014

---

## TCK3-SALES-00109 — Deal Approval (P4, Closed)
**Created:** 2026-05-20 via Phone  |  **Requester:** Naveen Bose  |  **Assigned to:** Ananya Bose

**Description:** Naveen Bose (Project Management / PMO) reported an issue via Phone related to 'Discount Approval Procedure'. Category: Deal Approval. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Discount Approval Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-SALES-003 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Discount Request' section. the Account Executive selects 'New Discount Request' and enters the required details, including deal size, competitive context, and margin impact. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Discount Request; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-003

---

## TCK3-SALES-00070 — Renewals (P2, Closed)
**Created:** 2026-05-21 via Slack  |  **Requester:** Tanya Singh  |  **Assigned to:** Rohan Singh

**Description:** Tanya Singh (Software Engineering / Development) reported an issue via Slack related to 'Customer Renewal Procedure'. Category: Renewals. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Customer Renewal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SALES-007 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Renewal Request' section. the Account Executive selects 'New Renewal Request' and enters the required details, including usage history, satisfaction indicators, and proposed renewal terms. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Renewal Request; MK-CRM automatically routes it to the Sales Manager for review. The Sales Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-007

---

## TCK3-SALES-00084 — Pipeline Management (P3, Resolved)
**Created:** 2026-05-29 via Walk-in  |  **Requester:** Shreya Joshi  |  **Assigned to:** Tanya Malhotra

**Description:** Shreya Joshi (Legal & Compliance) reported an issue via Walk-in related to 'Opportunity Creation and Pipeline Entry'. Category: Pipeline Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Opportunity Creation and Pipeline Entry', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-SALES-002 to resolve. the Account Executive confirms eligibility and prerequisites: deal size, expected close date, and stage in MK-CRM. the Account Executive raises a request in MK-CRM specifying exactly which Sales Opportunity is required. The Sales Team Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Sales Opportunity in the relevant system. the Account Executive is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SALES-002

---

## TCK3-SALES-00086 — Territory Management (P2, Resolved)
**Created:** 2026-05-31 via Live Chat  |  **Requester:** Pooja Mehta  |  **Assigned to:** Rohan Desai

**Description:** Pooja Mehta (Product Management) reported an issue via Live Chat related to 'Sales Territory Assignment Procedure'. Category: Territory Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Territory Assignment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SALES-008 to resolve. the Sales Manager logs into MK-CRM and navigates to the 'Territory Assignment' section. the Sales Manager selects 'New Territory Assignment' and enters the required details, including account list, geography, and capacity balancing. the Sales Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Sales Manager submits the Territory Assignment; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-008

---

## TCK3-SALES-00052 — Lead Management (P3, Closed)
**Created:** 2026-06-08 via Email  |  **Requester:** Nisha Joshi  |  **Assigned to:** Bhavna Pillai

**Description:** Nisha Joshi (Research & Development) reported an issue via Email related to 'New Lead Qualification Procedure'. Category: Lead Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'New Lead Qualification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-SALES-001 to resolve. the Sales Development Representative confirms eligibility and prerequisites: budget, authority, need, and timeline (BANT) criteria. the Sales Development Representative raises a request in MK-CRM specifying exactly which Lead Qualification is required. The Sales Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Lead Qualification in the relevant system. the Sales Development Representative is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SALES-001

---

## TCK3-SALES-00112 — Customer Handover (P4, Closed)
**Created:** 2026-06-10 via Portal  |  **Requester:** Varun Chowdhury  |  **Assigned to:** Sahil Sharma

**Description:** Varun Chowdhury (Sales) reported an issue via Portal related to 'Deal Closure and Handover to Customer Support'. Category: Customer Handover. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Deal Closure and Handover to Customer Support', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-SALES-005 to resolve. HR notifies the relevant department and the MK-CRM owner ahead of the employee's start or end date. the Account Executive prepares the required Customer Handover, including account details, agreed SLAs, and key contacts. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Sales Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SALES-005

---

## TCK3-SALES-00123 — Renewals (P2, Resolved)
**Created:** 2026-06-18 via Phone  |  **Requester:** Ananya Desai  |  **Assigned to:** Sahil Sharma

**Description:** Ananya Desai (Legal & Compliance) reported an issue via Phone related to 'Customer Renewal Procedure'. Category: Renewals. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Customer Renewal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SALES-007 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Renewal Request' section. the Account Executive selects 'New Renewal Request' and enters the required details, including usage history, satisfaction indicators, and proposed renewal terms. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Renewal Request; MK-CRM automatically routes it to the Sales Manager for review. The Sales Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-007

---