# Procurement / Purchasing — Rich Historical Ticket Archive (wave2, Page 2)

## TCK3-PROC-00065 — Requisitioning (P3, Resolved)
**Created:** 2024-11-13 via Phone  |  **Requester:** Anjali Gupta  |  **Assigned to:** Vivek Singh

**Description:** Anjali Gupta (Legal & Compliance) reported an issue via Phone related to 'New Hardware/Equipment Request Procedure'. Category: Requisitioning. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'New Hardware/Equipment Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-PROC-001 to resolve. the employee logs into MK-ProcureX and navigates to the 'Purchase Requisition' section. the employee selects 'New Purchase Requisition' and enters the required details, including item specification, quantity, and cost centre. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Purchase Requisition; MK-ProcureX automatically routes it to the Procurement Lead for review. The Procurement Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-001

---

## TCK3-PROC-00059 — Purchase Orders (P3, Resolved)
**Created:** 2024-11-15 via Slack  |  **Requester:** Kabir Agarwal  |  **Assigned to:** Siddharth Singh

**Description:** Kabir Agarwal (IT Support / Information Technology) reported an issue via Slack related to 'Purchase Order Issuance Procedure'. Category: Purchase Orders. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Purchase Order Issuance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-PROC-003 to resolve. the Procurement Executive confirms eligibility and prerequisites: matching the PO to the approved requisition and negotiated price. the Procurement Executive raises a request in MK-ProcureX specifying exactly which Purchase Order is required. The Procurement Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Purchase Order in the relevant system. the Procurement Executive is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROC-003

---

## TCK3-PROC-00073 — Vendor Management (P4, Resolved)
**Created:** 2024-11-23 via Phone  |  **Requester:** Simran Iyer  |  **Assigned to:** Harsh Malhotra

**Description:** Simran Iyer (Project Management / PMO) reported an issue via Phone related to 'Vendor Performance Review Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Performance Review Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-PROC-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Vendor Manager gathers the required data and documents, including on-time delivery rate, quality issues, and responsiveness. The review team examines the Vendor Performance Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-007

---

## TCK3-PROC-00085 — Software Procurement (P3, Resolved)
**Created:** 2024-11-25 via Email  |  **Requester:** Shreya Iyer  |  **Assigned to:** Sneha Singh

**Description:** Shreya Iyer (Administration / Facilities) reported an issue via Email related to 'Software License Procurement Procedure'. Category: Software Procurement. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Software License Procurement Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-PROC-009 to resolve. the requester logs into MK-ProcureX and navigates to the 'Software License Request' section. the requester selects 'New Software License Request' and enters the required details, including number of seats, license term, and IT/Security review status. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting. the requester submits the Software License Request; MK-ProcureX automatically routes it to the Procurement Lead for review. The Procurement Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-009

---

## TCK3-PROC-00023 — Asset Management (P4, Resolved)
**Created:** 2024-11-28 via Slack  |  **Requester:** Ritika Agarwal  |  **Assigned to:** Vivek Singh

**Description:** Ritika Agarwal (Customer Support / Helpdesk) reported an issue via Slack related to 'Asset Disposal Procedure'. Category: Asset Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Asset Disposal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-PROC-013 to resolve. the Procurement Executive confirms eligibility and prerequisites: data wipe confirmation from IT before disposal of any IT asset. the Procurement Executive raises a request in MK-ProcureX specifying exactly which Asset Disposal Request is required. The Procurement Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Asset Disposal Request in the relevant system. the Procurement Executive is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROC-013

---

## TCK3-PROC-00102 — Purchase Orders (P3, Resolved)
**Created:** 2024-12-03 via Walk-in  |  **Requester:** Divya Malhotra  |  **Assigned to:** Riya Desai

**Description:** Divya Malhotra (Customer Support / Helpdesk) reported an issue via Walk-in related to 'Purchase Order Issuance Procedure'. Category: Purchase Orders. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Purchase Order Issuance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-PROC-003 to resolve. the Procurement Executive confirms eligibility and prerequisites: matching the PO to the approved requisition and negotiated price. the Procurement Executive raises a request in MK-ProcureX specifying exactly which Purchase Order is required. The Procurement Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Purchase Order in the relevant system. the Procurement Executive is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROC-003

---

## TCK3-PROC-00091 — Asset Management (P3, Closed)
**Created:** 2024-12-10 via Slack  |  **Requester:** Sneha Reddy  |  **Assigned to:** Riya Desai

**Description:** Sneha Reddy (QA / Testing) reported an issue via Slack related to 'Asset Disposal Procedure'. Category: Asset Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Asset Disposal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-PROC-013 to resolve. the Procurement Executive confirms eligibility and prerequisites: data wipe confirmation from IT before disposal of any IT asset. the Procurement Executive raises a request in MK-ProcureX specifying exactly which Asset Disposal Request is required. The Procurement Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Asset Disposal Request in the relevant system. the Procurement Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROC-013

---

## TCK3-PROC-00139 — Vendor Compliance (P3, Closed)
**Created:** 2024-12-15 via Slack  |  **Requester:** Riya Pillai  |  **Assigned to:** Kavya Desai

**Description:** Riya Pillai (Software Engineering / Development) reported an issue via Slack related to 'Sustainable/Ethical Sourcing Review'. Category: Vendor Compliance. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Sustainable/Ethical Sourcing Review', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-PROC-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Specialist gathers the required data and documents, including vendor labour practices and environmental compliance declarations. The review team examines the Sourcing Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-012

---

## TCK3-PROC-00125 — Vendor Management (P2, Resolved)
**Created:** 2024-12-21 via Live Chat  |  **Requester:** Nisha Bose  |  **Assigned to:** Meera Chauhan

**Description:** Nisha Bose (Customer Support / Helpdesk) reported an issue via Live Chat related to 'Vendor Performance Review Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Performance Review Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-PROC-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Vendor Manager gathers the required data and documents, including on-time delivery rate, quality issues, and responsiveness. The review team examines the Vendor Performance Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-007

---

## TCK3-PROC-00138 — Receiving (P3, Resolved)
**Created:** 2024-12-22 via Phone  |  **Requester:** Anjali Joshi  |  **Assigned to:** Meera Chauhan

**Description:** Anjali Joshi (Management / Leadership) reported an issue via Phone related to 'Goods Receipt and Inspection Procedure'. Category: Receiving. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Goods Receipt and Inspection Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-PROC-005 to resolve. the Procurement Executive confirms eligibility and prerequisites: checking quantity and condition against the purchase order. the Procurement Executive raises a request in MK-ProcureX specifying exactly which Goods Receipt is required. The Procurement Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Goods Receipt in the relevant system. the Procurement Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROC-005

---

## TCK3-PROC-00120 — Vendor Management (P3, Closed)
**Created:** 2024-12-26 via Live Chat  |  **Requester:** Simran Gupta  |  **Assigned to:** Vivek Singh

**Description:** Simran Gupta (Sales) reported an issue via Live Chat related to 'Vendor Selection and Onboarding Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Selection and Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-PROC-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Specialist gathers the required data and documents, including comparing at least 3 quotes on price, quality, and delivery timeline. The review team examines the Vendor Selection against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-002

---

## TCK3-PROC-00121 — Budget Management (P3, Resolved)
**Created:** 2024-12-28 via Email  |  **Requester:** Ananya Menon  |  **Assigned to:** Vivek Singh

**Description:** Ananya Menon (Human Resources) reported an issue via Email related to 'Procurement Budget Tracking Procedure'. Category: Budget Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Budget Tracking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-PROC-006 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Lead gathers the required data and documents, including committed vs actual spend by category. The review team examines the Procurement Budget Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-006

---

## TCK3-PROC-00106 — Vendor Management (P4, Resolved)
**Created:** 2024-12-30 via Phone  |  **Requester:** Varun Reddy  |  **Assigned to:** Kavya Desai

**Description:** Varun Reddy (Product Management) reported an issue via Phone related to 'Vendor Contract Renewal Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Contract Renewal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-PROC-004 to resolve. the Vendor Manager logs into MK-ProcureX and navigates to the 'Vendor Contract Renewal' section. the Vendor Manager selects 'New Vendor Contract Renewal' and enters the required details, including performance review and renegotiated pricing where applicable. the Vendor Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Vendor Manager submits the Vendor Contract Renewal; MK-ProcureX automatically routes it to the Procurement Manager for review. The Procurement Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-004

---

## TCK3-PROC-00024 — Budget Management (P3, Resolved)
**Created:** 2025-01-02 via Slack  |  **Requester:** Simran Desai  |  **Assigned to:** Anjali Iyer

**Description:** Simran Desai (Software Engineering / Development) reported an issue via Slack related to 'Procurement Budget Tracking Procedure'. Category: Budget Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Budget Tracking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-PROC-006 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Lead gathers the required data and documents, including committed vs actual spend by category. The review team examines the Procurement Budget Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-006

---

## TCK3-PROC-00049 — Vendor Management (P3, Resolved)
**Created:** 2025-01-03 via Email  |  **Requester:** Simran Malhotra  |  **Assigned to:** Ritika Singh

**Description:** Simran Malhotra (Finance & Accounting) reported an issue via Email related to 'Vendor Selection and Onboarding Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Selection and Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-PROC-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Specialist gathers the required data and documents, including comparing at least 3 quotes on price, quality, and delivery timeline. The review team examines the Vendor Selection against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-002

---

## TCK3-PROC-00046 — Vendor Management (P3, Resolved)
**Created:** 2025-01-04 via Phone  |  **Requester:** Siddharth Joshi  |  **Assigned to:** Riya Desai

**Description:** Siddharth Joshi (Cybersecurity / Information Security) reported an issue via Phone related to 'Vendor Contract Renewal Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Contract Renewal Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-PROC-004 to resolve. the Vendor Manager logs into MK-ProcureX and navigates to the 'Vendor Contract Renewal' section. the Vendor Manager selects 'New Vendor Contract Renewal' and enters the required details, including performance review and renegotiated pricing where applicable. the Vendor Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Vendor Manager submits the Vendor Contract Renewal; MK-ProcureX automatically routes it to the Procurement Manager for review. The Procurement Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROC-004

---

## TCK3-PROC-00034 — Budget Management (P1, Closed)
**Created:** 2025-01-07 via Live Chat  |  **Requester:** Tanya Malhotra  |  **Assigned to:** Yash Chauhan

**Description:** Tanya Malhotra (Sales) reported an issue via Live Chat related to 'Procurement Budget Tracking Procedure'. Category: Budget Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Budget Tracking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-PROC-006 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Lead gathers the required data and documents, including committed vs actual spend by category. The review team examines the Procurement Budget Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-006

---

## TCK3-PROC-00040 — Purchase Orders (P3, Resolved)
**Created:** 2025-01-08 via Portal  |  **Requester:** Vikram Bhatt  |  **Assigned to:** Harsh Malhotra

**Description:** Vikram Bhatt (Human Resources) reported an issue via Portal related to 'Purchase Order Issuance Procedure'. Category: Purchase Orders. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Purchase Order Issuance Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-PROC-003 to resolve. the Procurement Executive confirms eligibility and prerequisites: matching the PO to the approved requisition and negotiated price. the Procurement Executive raises a request in MK-ProcureX specifying exactly which Purchase Order is required. The Procurement Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Purchase Order in the relevant system. the Procurement Executive is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROC-003

---

## TCK3-PROC-00113 — Budget Management (P3, Resolved)
**Created:** 2025-01-11 via Walk-in  |  **Requester:** Divya Gupta  |  **Assigned to:** Anjali Iyer

**Description:** Divya Gupta (QA / Testing) reported an issue via Walk-in related to 'Procurement Budget Tracking Procedure'. Category: Budget Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Procurement Budget Tracking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-PROC-006 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProcureX. the Procurement Lead gathers the required data and documents, including committed vs actual spend by category. The review team examines the Procurement Budget Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Procurement Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROC-006

---

## TCK3-PROC-00074 — Vendor Management (P3, Closed)
**Created:** 2025-01-16 via Portal  |  **Requester:** Nisha Joshi  |  **Assigned to:** Sneha Singh

**Description:** Nisha Joshi (Research & Development) reported an issue via Portal related to 'Vendor Dispute Resolution Procedure'. Category: Vendor Management. Logged against MK-ProcureX.

**Investigation:** The assigned specialist reviewed the MK-ProcureX record, confirmed the reported symptom against 'Vendor Dispute Resolution Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An edge case in the underlying logic wasn't covered by the original design and only surfaced under specific conditions.

**Resolution:** Followed SOP-PROC-010 to resolve. the Procurement Specialist confirms the exact symptom, when it started, and whether it affects one system or several. the Procurement Specialist performs the standard first-line check: documenting the discrepancy against the PO and contract terms. If the issue persists, the Procurement Specialist applies the documented workaround for this issue type. the Procurement Specialist checks whether the issue is isolated to their own account/device or is affecting other users too. If still unresolved, the Procurement Specialist raises a ticket in MK-ProcureX categorised under 'Vendor Dispute', attaching screenshots or error logs.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a monitoring alert so this symptom is caught proactively rather than reported by a user.

**Related SOP:** SOP-PROC-010

---
