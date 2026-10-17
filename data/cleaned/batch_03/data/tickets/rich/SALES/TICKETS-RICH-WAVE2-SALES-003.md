# Sales — Rich Historical Ticket Archive (wave2, Page 3)

## TCK3-SALES-00142 — Lead Management (P4, Resolved)
**Created:** 2025-01-07 via Slack  |  **Requester:** Rohan Singh  |  **Assigned to:** Sahil Sharma

**Description:** Rohan Singh (Sales) reported an issue via Slack related to 'New Lead Qualification Procedure'. Category: Lead Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'New Lead Qualification Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-SALES-001 to resolve. the Sales Development Representative confirms eligibility and prerequisites: budget, authority, need, and timeline (BANT) criteria. the Sales Development Representative raises a request in MK-CRM specifying exactly which Lead Qualification is required. The Sales Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Lead Qualification in the relevant system. the Sales Development Representative is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SALES-001

---

## TCK3-SALES-00110 — Quoting (P4, Resolved)
**Created:** 2025-01-15 via Walk-in  |  **Requester:** Tanya Mehta  |  **Assigned to:** Bhavna Pillai

**Description:** Tanya Mehta (Project Management / PMO) reported an issue via Walk-in related to 'Contract/Quote Generation Procedure'. Category: Quoting. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Contract/Quote Generation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-SALES-004 to resolve. the Account Executive confirms eligibility and prerequisites: pricing tier, contract term, and any custom clauses. the Account Executive raises a request in MK-CRM specifying exactly which Sales Quote is required. The Sales Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Sales Quote in the relevant system. the Account Executive is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SALES-004

---

## TCK3-SALES-00141 — Competitive Intelligence (P3, Resolved)
**Created:** 2025-01-16 via Slack  |  **Requester:** Tanya Malhotra  |  **Assigned to:** Aman Chauhan

**Description:** Tanya Malhotra (Sales) reported an issue via Slack related to 'Competitive Deal Support Request'. Category: Competitive Intelligence. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Competitive Deal Support Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SALES-009 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Competitive Intel Request' section. the Account Executive selects 'New Competitive Intel Request' and enters the required details, including the competitor name and specific objection raised by the prospect. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Competitive Intel Request; MK-CRM automatically routes it to the Product Manager for review. The Product Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-009

---

## TCK3-SALES-00042 — Order Management (P3, Resolved)
**Created:** 2025-01-19 via Portal  |  **Requester:** Preeti Verma  |  **Assigned to:** Sahil Sharma

**Description:** Preeti Verma (Software Engineering / Development) reported an issue via Portal related to 'Sales Order Booking Procedure'. Category: Order Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Order Booking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-SALES-016 to resolve. the Account Executive confirms eligibility and prerequisites: confirming signed contract terms match the order entered in MK-CRM. the Account Executive raises a request in MK-CRM specifying exactly which Sales Order is required. The Finance Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Sales Order in the relevant system. the Account Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-SALES-016

---

## TCK3-SALES-00100 — Sales Enablement (P2, In Progress)
**Created:** 2025-02-03 via Live Chat  |  **Requester:** Arjun Gupta  |  **Assigned to:** Bhavna Pillai

**Description:** Arjun Gupta (Data & Analytics) reported an issue via Live Chat related to 'Sales Enablement Content Request'. Category: Sales Enablement. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Enablement Content Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-014

---

## TCK3-SALES-00069 — Sales Enablement (P4, Resolved)
**Created:** 2025-02-19 via Live Chat  |  **Requester:** Rahul Reddy  |  **Assigned to:** Vivek Gupta

**Description:** Rahul Reddy (Cybersecurity / Information Security) reported an issue via Live Chat related to 'Sales Enablement Content Request'. Category: Sales Enablement. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Enablement Content Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SALES-014 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Enablement Content Request' section. the Account Executive selects 'New Enablement Content Request' and enters the required details, including the use case and target audience for the requested material. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Enablement Content Request; MK-CRM automatically routes it to the Marketing Manager for review. The Marketing Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-014

---

## TCK3-SALES-00079 — Renewals (P3, In Progress)
**Created:** 2025-03-05 via Slack  |  **Requester:** Ritika Singh  |  **Assigned to:** Anjali Verma

**Description:** Ritika Singh (Human Resources) reported an issue via Slack related to 'Customer Renewal Procedure'. Category: Renewals. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Customer Renewal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-007

---

## TCK3-SALES-00106 — Territory Management (P4, Resolved)
**Created:** 2025-03-17 via Walk-in  |  **Requester:** Harsh Chauhan  |  **Assigned to:** Rohan Singh

**Description:** Harsh Chauhan (QA / Testing) reported an issue via Walk-in related to 'Sales Territory Assignment Procedure'. Category: Territory Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Territory Assignment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-SALES-008 to resolve. the Sales Manager logs into MK-CRM and navigates to the 'Territory Assignment' section. the Sales Manager selects 'New Territory Assignment' and enters the required details, including account list, geography, and capacity balancing. the Sales Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Sales Manager submits the Territory Assignment; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-008

---

## TCK3-SALES-00115 — Deal Approval (P2, Resolved)
**Created:** 2025-03-28 via Email  |  **Requester:** Neel Sharma  |  **Assigned to:** Ananya Bose

**Description:** Neel Sharma (Software Engineering / Development) reported an issue via Email related to 'Discount Approval Procedure'. Category: Deal Approval. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Discount Approval Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-SALES-003 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Discount Request' section. the Account Executive selects 'New Discount Request' and enters the required details, including deal size, competitive context, and margin impact. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Discount Request; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-003

---

## TCK3-SALES-00065 — Account Management (P4, Resolved)
**Created:** 2025-04-05 via Phone  |  **Requester:** Varun Rao  |  **Assigned to:** Aman Chauhan

**Description:** Varun Rao (Management / Leadership) reported an issue via Phone related to 'Key Account Planning Procedure'. Category: Account Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Key Account Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-SALES-015 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CRM. the Senior Account Executive gathers the required data and documents, including whitespace analysis, stakeholder map, and growth targets. The review team examines the Account Plan against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Sales Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SALES-015

---

## TCK3-SALES-00073 — Customer References (P3, Resolved)
**Created:** 2025-04-12 via Portal  |  **Requester:** Ritika Agarwal  |  **Assigned to:** Rohan Singh

**Description:** Ritika Agarwal (Project Management / PMO) reported an issue via Portal related to 'Customer Reference Request Procedure'. Category: Customer References. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Customer Reference Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SALES-011 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Reference Request' section. the Account Executive selects 'New Reference Request' and enters the required details, including the target prospect profile and requested reference customer. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Reference Request; MK-CRM automatically routes it to the Marketing Manager for review. The Marketing Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-011

---

## TCK3-SALES-00083 — Compensation (P3, Resolved)
**Created:** 2025-04-12 via Slack  |  **Requester:** Siddharth Chauhan  |  **Assigned to:** Kabir Chauhan

**Description:** Siddharth Chauhan (Procurement / Purchasing) reported an issue via Slack related to 'Sales Commission Calculation Procedure'. Category: Compensation. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Commission Calculation Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-SALES-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CRM. the Sales Manager gathers the required data and documents, including closed-won deals, quota attainment, and accelerator tiers. The review team examines the Commission Calculation against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Finance Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SALES-012

---

## TCK3-SALES-00047 — Customer Handover (P3, In Progress)
**Created:** 2025-04-13 via Slack  |  **Requester:** Divya Nair  |  **Assigned to:** Simran Gupta

**Description:** Divya Nair (Management / Leadership) reported an issue via Slack related to 'Deal Closure and Handover to Customer Support'. Category: Customer Handover. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Deal Closure and Handover to Customer Support', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SALES-005

---

## TCK3-SALES-00121 — Onboarding (P2, Resolved)
**Created:** 2025-04-29 via Slack  |  **Requester:** Shreya Kapoor  |  **Assigned to:** Anjali Verma

**Description:** Shreya Kapoor (Cybersecurity / Information Security) reported an issue via Slack related to 'Sales Onboarding Procedure for New Hires'. Category: Onboarding. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Onboarding Procedure for New Hires', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-SALES-010 to resolve. HR notifies the relevant department and the MK-CRM owner ahead of the employee's start or end date. the Sales Manager prepares the required Sales Onboarding, including MK-CRM access, product certification, and shadow calls with a senior AE. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Sales Director verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-SALES-010

---

## TCK3-SALES-00151 — Territory Management (P3, Resolved)
**Created:** 2025-04-29 via Walk-in  |  **Requester:** Sahil Bhatt  |  **Assigned to:** Sahil Kapoor

**Description:** Sahil Bhatt (Project Management / PMO) reported an issue via Walk-in related to 'Sales Territory Assignment Procedure'. Category: Territory Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Territory Assignment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-SALES-008 to resolve. the Sales Manager logs into MK-CRM and navigates to the 'Territory Assignment' section. the Sales Manager selects 'New Territory Assignment' and enters the required details, including account list, geography, and capacity balancing. the Sales Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Sales Manager submits the Territory Assignment; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-008

---

## TCK3-SALES-00051 — Deal Approval (P3, Resolved)
**Created:** 2025-05-02 via Walk-in  |  **Requester:** Meera Chauhan  |  **Assigned to:** Kabir Chauhan

**Description:** Meera Chauhan (Procurement / Purchasing) reported an issue via Walk-in related to 'Discount Approval Procedure'. Category: Deal Approval. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Discount Approval Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SALES-003 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Discount Request' section. the Account Executive selects 'New Discount Request' and enters the required details, including deal size, competitive context, and margin impact. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Discount Request; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-003

---

## TCK3-SALES-00038 — Competitive Intelligence (P3, Resolved)
**Created:** 2025-05-05 via Email  |  **Requester:** Kabir Agarwal  |  **Assigned to:** Simran Gupta

**Description:** Kabir Agarwal (IT Support / Information Technology) reported an issue via Email related to 'Competitive Deal Support Request'. Category: Competitive Intelligence. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Competitive Deal Support Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-SALES-009 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Competitive Intel Request' section. the Account Executive selects 'New Competitive Intel Request' and enters the required details, including the competitor name and specific objection raised by the prospect. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Competitive Intel Request; MK-CRM automatically routes it to the Product Manager for review. The Product Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-009

---

## TCK3-SALES-00137 — Territory Management (P3, Resolved)
**Created:** 2025-05-15 via Portal  |  **Requester:** Arjun Verma  |  **Assigned to:** Anjali Verma

**Description:** Arjun Verma (Administration / Facilities) reported an issue via Portal related to 'Sales Territory Assignment Procedure'. Category: Territory Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Sales Territory Assignment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-SALES-008 to resolve. the Sales Manager logs into MK-CRM and navigates to the 'Territory Assignment' section. the Sales Manager selects 'New Territory Assignment' and enters the required details, including account list, geography, and capacity balancing. the Sales Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Sales Manager submits the Territory Assignment; MK-CRM automatically routes it to the Sales Director for review. The Sales Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-008

---

## TCK3-SALES-00037 — Account Management (P4, Closed)
**Created:** 2025-06-04 via Email  |  **Requester:** Priya Bose  |  **Assigned to:** Rohan Singh

**Description:** Priya Bose (Research & Development) reported an issue via Email related to 'Key Account Planning Procedure'. Category: Account Management. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Key Account Planning Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-SALES-015 to resolve. The review is scheduled in advance and stakeholders are notified through MK-CRM. the Senior Account Executive gathers the required data and documents, including whitespace analysis, stakeholder map, and growth targets. The review team examines the Account Plan against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Sales Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-SALES-015

---

## TCK3-SALES-00107 — Customer References (P4, Resolved)
**Created:** 2025-06-12 via Portal  |  **Requester:** Nidhi Malhotra  |  **Assigned to:** Rohan Singh

**Description:** Nidhi Malhotra (Sales) reported an issue via Portal related to 'Customer Reference Request Procedure'. Category: Customer References. Logged against MK-CRM.

**Investigation:** The assigned specialist reviewed the MK-CRM record, confirmed the reported symptom against 'Customer Reference Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-SALES-011 to resolve. the Account Executive logs into MK-CRM and navigates to the 'Reference Request' section. the Account Executive selects 'New Reference Request' and enters the required details, including the target prospect profile and requested reference customer. the Account Executive attaches any supporting documentation and reviews the entry for accuracy before submitting. the Account Executive submits the Reference Request; MK-CRM automatically routes it to the Marketing Manager for review. The Marketing Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-SALES-011

---