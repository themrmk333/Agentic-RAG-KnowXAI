# Procurement / Purchasing — Rich Historical Ticket Archive (wave2, Page 4)

## TCK3-PROC-00097 — Asset Management (P4, Resolved)
**Created:** 2025-06-14 via Live Chat  |  **Requester:** Nisha Desai  |  **Assigned to:** Harsh Malhotra

**Description:** Nisha Desai (Project Management / PMO) reported an issue via Live Chat related to 'Asset Disposal Procedure'. Category: Asset Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Asset Disposal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-PROC-013 to resolve. the Procurement Executive confirms eligibility and prerequisites: data wipe confirmation from IT before disposal of any IT asset. the Procurement Executive raises a request in MK-ProcureX specifying exactly which Asset Disposal Request is required. The Procurement Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Asset Disposal Request in the relevant system. the Procurement Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROC-013

---

## TCK3-PROC-00047 — Onboarding (P3, Resolved)
**Created:** 2025-06-21 via Email  |  **Requester:** Dev Pillai  |  **Assigned to:** Kavya Bhatt

**Description:** Dev Pillai (Software Engineering / Development) reported an issue via Email related to 'Procurement Onboarding Procedure'. Category: Onboarding. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two people each assumed the other was completing a specific step.

**Resolution:** Followed SOP-PROC-011 to resolve. HR notifies the relevant department and the MK-ProcureX owner ahead of the employee's start or end date. the Procurement Lead prepares the required Procurement Onboarding, including MK-ProcureX access and vendor master data training. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Procurement Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-PROC-011

---

## TCK3-PROC-00101 — Requisitioning (P4, Resolved)
**Created:** 2025-06-27 via Live Chat  |  **Requester:** Simran Agarwal  |  **Assigned to:** Gaurav Malhotra

**Description:** Simran Agarwal (Research & Development) reported an issue via Live Chat related to 'New Hardware/Equipment Request Procedure'. Category: Requisitioning. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'New Hardware/Equipment Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-PROC-001 to resolve. the employee logs into MK-ProcureX and navigates to the 'Purchase Requisition' section. the employee selects 'New Purchase Requisition' and enters the required details, including item specification, quantity, and cost centre. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Purchase Requisition; MK-ProcureX automatically routes it to the Procurement Lead for review. The Procurement Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-001

---

## TCK3-PROC-00142 — Vendor Management (P4, Resolved)
**Created:** 2025-06-28 via Portal  |  **Requester:** Tanya Sharma  |  **Assigned to:** Riya Desai

**Description:** Tanya Sharma (Customer Support / Helpdesk) reported an issue via Portal related to 'Vendor Selection and Onboarding Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Selection and Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-PROC-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Specialist gathers the required data and documents, including comparing at least 3 quotes on price, quality, and delivery timeline. The review team examines the Vendor Selection against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-002

---

## TCK3-PROC-00060 — Requisitioning (P3, In Progress)
**Created:** 2025-07-12 via Email  |  **Requester:** Neel Joshi  |  **Assigned to:** Aditya Rao

**Description:** Neel Joshi (Software Engineering / Development) reported an issue via Email related to 'New Hardware/Equipment Request Procedure'. Category: Requisitioning. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'New Hardware/Equipment Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-001

---

## TCK3-PROC-00050 — Vendor Management (P3, Resolved)
**Created:** 2025-07-25 via Live Chat  |  **Requester:** Nidhi Mehta  |  **Assigned to:** Yash Chauhan

**Description:** Nidhi Mehta (Human Resources) reported an issue via Live Chat related to 'Vendor Selection and Onboarding Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Selection and Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-PROC-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Specialist gathers the required data and documents, including comparing at least 3 quotes on price, quality, and delivery timeline. The review team examines the Vendor Selection against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-002

---

## TCK3-PROC-00115 — Requisitioning (P3, Closed)
**Created:** 2025-07-25 via Live Chat  |  **Requester:** Gaurav Sharma  |  **Assigned to:** Riya Desai

**Description:** Gaurav Sharma (IT Support / Information Technology) reported an issue via Live Chat related to 'New Hardware/Equipment Request Procedure'. Category: Requisitioning. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'New Hardware/Equipment Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-PROC-001 to resolve. the employee logs into MK-ProcureX and navigates to the 'Purchase Requisition' section. the employee selects 'New Purchase Requisition' and enters the required details, including item specification, quantity, and cost centre. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Purchase Requisition; MK-ProcureX automatically routes it to the Procurement Lead for review. The Procurement Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-001

---

## TCK3-PROC-00126 — Purchase Orders (P3, Resolved)
**Created:** 2025-08-18 via Email  |  **Requester:** Rohan Mehta  |  **Assigned to:** Rohan Reddy

**Description:** Rohan Mehta (Data & Analytics) reported an issue via Email related to 'Purchase Order Issuance Procedure'. Category: Purchase Orders. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Purchase Order Issuance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-PROC-003 to resolve. the Procurement Executive confirms eligibility and prerequisites: matching the PO to the approved requisition and negotiated price. the Procurement Executive raises a request in MK-ProcureX specifying exactly which Purchase Order is required. The Procurement Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Purchase Order in the relevant system. the Procurement Executive is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROC-003

---

## TCK3-PROC-00109 — Budget Management (P1, Closed)
**Created:** 2025-08-19 via Walk-in  |  **Requester:** Arjun Verma  |  **Assigned to:** Ritika Singh

**Description:** Arjun Verma (Administration / Facilities) reported an issue via Walk-in related to 'Procurement Budget Tracking Procedure'. Category: Budget Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Budget Tracking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-PROC-006 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Lead gathers the required data and documents, including committed vs actual spend by category. The review team examines the Procurement Budget Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-006

---

## TCK3-PROC-00088 — Vendor Management (P3, Resolved)
**Created:** 2025-09-02 via Email  |  **Requester:** Aditya Sharma  |  **Assigned to:** Harsh Malhotra

**Description:** Aditya Sharma (Finance & Accounting) reported an issue via Email related to 'Vendor Contract Renewal Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Contract Renewal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-PROC-004 to resolve. the Vendor Manager logs into MK-ProcureX and navigates to the 'Vendor Contract Renewal' section. the Vendor Manager selects 'New Vendor Contract Renewal' and enters the required details, including performance review and renegotiated pricing where applicable. the Vendor Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Vendor Manager submits the Vendor Contract Renewal; MK-ProcureX automatically routes it to the Procurement Manager for review. The Procurement Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-004

---

## TCK3-PROC-00036 — Software Procurement (P3, Closed)
**Created:** 2025-09-08 via Phone  |  **Requester:** Vikram Mehta  |  **Assigned to:** Meera Chauhan

**Description:** Vikram Mehta (DevOps & Cloud) reported an issue via Phone related to 'Software License Procurement Procedure'. Category: Software Procurement. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Software License Procurement Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-PROC-009 to resolve. the requester logs into MK-ProcureX and navigates to the 'Software License Request' section. the requester selects 'New Software License Request' and enters the required details, including number of seats, license term, and IT/Security review status. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Software License Request; MK-ProcureX automatically routes it to the Procurement Lead for review. The Procurement Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-009

---

## TCK3-PROC-00063 — Budget Management (P4, Closed)
**Created:** 2025-09-10 via Live Chat  |  **Requester:** Nisha Joshi  |  **Assigned to:** Meera Malhotra

**Description:** Nisha Joshi (Research & Development) reported an issue via Live Chat related to 'Procurement Budget Tracking Procedure'. Category: Budget Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Budget Tracking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-PROC-006 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Lead gathers the required data and documents, including committed vs actual spend by category. The review team examines the Procurement Budget Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-006

---

## TCK3-PROC-00133 — Requisitioning (P4, Resolved)
**Created:** 2025-09-11 via Slack  |  **Requester:** Nidhi Pillai  |  **Assigned to:** Yash Chauhan

**Description:** Nidhi Pillai (Human Resources) reported an issue via Slack related to 'Emergency/Urgent Procurement Procedure'. Category: Requisitioning. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Emergency/Urgent Procurement Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-PROC-008 to resolve. the requester logs into MK-ProcureX and navigates to the 'Urgent Purchase Request' section. the requester selects 'New Urgent Purchase Request' and enters the required details, including business justification for bypassing the standard 3-quote process. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Urgent Purchase Request; MK-ProcureX automatically routes it to the Procurement Manager for review. The Procurement Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-008

---

## TCK3-PROC-00067 — Governance (P3, Resolved)
**Created:** 2025-09-17 via Portal  |  **Requester:** Riya Pillai  |  **Assigned to:** Ritika Singh

**Description:** Riya Pillai (Software Engineering / Development) reported an issue via Portal related to 'Procurement Policy Exception Request'. Category: Governance. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Policy Exception Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-PROC-015 to resolve. the requester logs into MK-ProcureX and navigates to the 'Procurement Policy Exception' section. the requester selects 'New Procurement Policy Exception' and enters the required details, including the specific policy clause and business justification for exception. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Procurement Policy Exception; MK-ProcureX automatically routes it to the Procurement Director for review. The Procurement Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-015

---

## TCK3-PROC-00038 — Onboarding (P3, Resolved)
**Created:** 2025-09-29 via Portal  |  **Requester:** Isha Pillai  |  **Assigned to:** Anjali Iyer

**Description:** Isha Pillai (IT Support / Information Technology) reported an issue via Portal related to 'Procurement Onboarding Procedure'. Category: Onboarding. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-PROC-011 to resolve. HR notifies the relevant department and the MK-ProcureX owner ahead of the employee's start or end date. the Procurement Lead prepares the required Procurement Onboarding, including MK-ProcureX access and vendor master data training. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Procurement Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-PROC-011

---

## TCK3-PROC-00031 — Receiving (P2, Resolved)
**Created:** 2025-09-30 via Slack  |  **Requester:** Rohan Singh  |  **Assigned to:** Ritika Singh

**Description:** Rohan Singh (Marketing) reported an issue via Slack related to 'Goods Receipt and Inspection Procedure'. Category: Receiving. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Goods Receipt and Inspection Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-PROC-005 to resolve. the Procurement Executive confirms eligibility and prerequisites: checking quantity and condition against the purchase order. the Procurement Executive raises a request in MK-ProcureX specifying exactly which Goods Receipt is required. The Procurement Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Goods Receipt in the relevant system. the Procurement Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROC-005

---

## TCK3-PROC-00090 — Requisitioning (P4, Closed)
**Created:** 2025-10-06 via Live Chat  |  **Requester:** Varun Menon  |  **Assigned to:** Siddharth Chauhan

**Description:** Varun Menon (QA / Testing) reported an issue via Live Chat related to 'Emergency/Urgent Procurement Procedure'. Category: Requisitioning. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Emergency/Urgent Procurement Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-PROC-008 to resolve. the requester logs into MK-ProcureX and navigates to the 'Urgent Purchase Request' section. the requester selects 'New Urgent Purchase Request' and enters the required details, including business justification for bypassing the standard 3-quote process. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Urgent Purchase Request; MK-ProcureX automatically routes it to the Procurement Manager for review. The Procurement Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-008

---

## TCK3-PROC-00099 — Vendor Management (P4, Resolved)
**Created:** 2025-10-21 via Portal  |  **Requester:** Neel Menon  |  **Assigned to:** Aditya Rao

**Description:** Neel Menon (IT Support / Information Technology) reported an issue via Portal related to 'Vendor Contract Renewal Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Contract Renewal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-PROC-004 to resolve. the Vendor Manager logs into MK-ProcureX and navigates to the 'Vendor Contract Renewal' section. the Vendor Manager selects 'New Vendor Contract Renewal' and enters the required details, including performance review and renegotiated pricing where applicable. the Vendor Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Vendor Manager submits the Vendor Contract Renewal; MK-ProcureX automatically routes it to the Procurement Manager for review. The Procurement Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-004

---

## TCK3-PROC-00100 — Onboarding (P4, Closed)
**Created:** 2025-10-30 via Slack  |  **Requester:** Aman Verma  |  **Assigned to:** Siddharth Singh

**Description:** Aman Verma (Human Resources) reported an issue via Slack related to 'Procurement Onboarding Procedure'. Category: Onboarding. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-PROC-011 to resolve. HR notifies the relevant department and the MK-ProcureX owner ahead of the employee's start or end date. the Procurement Lead prepares the required Procurement Onboarding, including MK-ProcureX access and vendor master data training. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Procurement Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-PROC-011

---

## TCK3-PROC-00041 — Requisitioning (P3, Resolved)
**Created:** 2025-11-08 via Slack  |  **Requester:** Meera Chauhan  |  **Assigned to:** Yash Chauhan

**Description:** Meera Chauhan (Customer Support / Helpdesk) reported an issue via Slack related to 'New Hardware/Equipment Request Procedure'. Category: Requisitioning. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'New Hardware/Equipment Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-PROC-001 to resolve. the employee logs into MK-ProcureX and navigates to the 'Purchase Requisition' section. the employee selects 'New Purchase Requisition' and enters the required details, including item specification, quantity, and cost centre. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Purchase Requisition; MK-ProcureX automatically routes it to the Procurement Lead for review. The Procurement Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-001

---
