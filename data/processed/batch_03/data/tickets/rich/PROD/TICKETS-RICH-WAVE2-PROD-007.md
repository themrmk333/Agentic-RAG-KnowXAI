# Product Management — Rich Historical Ticket Archive (wave2, Page 7)

## TCK3-PROD-00145 — Beta Testing (P4, Closed)
**Created:** 2026-05-11 via Slack  |  **Requester:** Arjun Gupta  |  **Assigned to:** Karan Pillai

**Description:** Arjun Gupta (Data & Analytics) reported an issue via Slack related to 'Beta Program Management Procedure'. Category: Beta Testing. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Beta Program Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-PROD-008 to resolve. the Product Manager confirms eligibility and prerequisites: selecting beta participants and defining feedback collection cadence. the Product Manager raises a request in MK-ProductHub specifying exactly which Beta Program is required. The Product Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Beta Program in the relevant system. the Product Manager is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROD-008

---

## TCK3-PROD-00079 — Pricing (P3, Closed)
**Created:** 2026-05-29 via Walk-in  |  **Requester:** Harsh Chauhan  |  **Assigned to:** Siddharth Singh

**Description:** Harsh Chauhan (QA / Testing) reported an issue via Walk-in related to 'Pricing Change Request Procedure'. Category: Pricing. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Pricing Change Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-PROD-009 to resolve. the Product Manager logs into MK-ProductHub and navigates to the 'Pricing Change Request' section. the Product Manager selects 'New Pricing Change Request' and enters the required details, including revenue impact analysis and competitor pricing benchmark. the Product Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Product Manager submits the Pricing Change Request; MK-ProductHub automatically routes it to the VP Product for review. The VP Product reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROD-009

---

## TCK3-PROD-00095 — Pricing (P2, Resolved)
**Created:** 2026-06-07 via Walk-in  |  **Requester:** Riya Desai  |  **Assigned to:** Manoj Mehta

**Description:** Riya Desai (Procurement / Purchasing) reported an issue via Walk-in related to 'Pricing Change Request Procedure'. Category: Pricing. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Pricing Change Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-PROD-009 to resolve. the Product Manager logs into MK-ProductHub and navigates to the 'Pricing Change Request' section. the Product Manager selects 'New Pricing Change Request' and enters the required details, including revenue impact analysis and competitor pricing benchmark. the Product Manager attaches any supporting documentation and reviews the entry for accuracy before submitting. the Product Manager submits the Pricing Change Request; MK-ProductHub automatically routes it to the VP Product for review. The VP Product reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-PROD-009

---

## TCK3-PROD-00150 — Market Research (P3, Resolved)
**Created:** 2026-06-12 via Phone  |  **Requester:** Alisha Bhatt  |  **Assigned to:** Sneha Verma

**Description:** Alisha Bhatt (Management / Leadership) reported an issue via Phone related to 'Competitive Analysis Procedure'. Category: Market Research. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Competitive Analysis Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-PROD-006 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProductHub. the Product Manager gathers the required data and documents, including feature comparison, pricing, and positioning against key competitors. The review team examines the Competitive Analysis Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Head of Product discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROD-006

---

## TCK3-PROD-00138 — Beta Testing (P3, In Progress)
**Created:** 2026-07-03 via Slack  |  **Requester:** Sahil Bhatt  |  **Assigned to:** Preeti Kapoor

**Description:** Sahil Bhatt (Project Management / PMO) reported an issue via Slack related to 'Beta Program Management Procedure'. Category: Beta Testing. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Beta Program Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROD-008

---

## TCK3-PROD-00043 — Onboarding (P3, Resolved)
**Created:** 2026-07-13 via Slack  |  **Requester:** Simran Agarwal  |  **Assigned to:** Dev Sharma

**Description:** Simran Agarwal (Research & Development) reported an issue via Slack related to 'Product Onboarding for New PMs'. Category: Onboarding. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Product Onboarding for New PMs', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-PROD-012 to resolve. HR notifies the relevant department and the MK-ProductHub owner ahead of the employee's start or end date. the Head of Product prepares the required Product Onboarding, including MK-ProductHub access, roadmap walkthrough, and customer call shadowing. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The VP Product verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-PROD-012

---

## TCK3-PROD-00109 — Analytics (P3, Resolved)
**Created:** 2026-07-28 via Portal  |  **Requester:** Dev Malhotra  |  **Assigned to:** Sneha Verma

**Description:** Dev Malhotra (Cybersecurity / Information Security) reported an issue via Portal related to 'Product Metrics Review Procedure'. Category: Analytics. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Product Metrics Review Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-PROD-010 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProductHub. the Product Manager gathers the required data and documents, including adoption, retention, and engagement metrics from MK-DataLake dashboards. The review team examines the Metrics Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Head of Product discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROD-010

---

## TCK3-PROD-00126 — Backlog Management (P3, Closed)
**Created:** 2026-07-31 via Email  |  **Requester:** Swati Sharma  |  **Assigned to:** Pooja Mehta

**Description:** Swati Sharma (QA / Testing) reported an issue via Email related to 'Product Backlog Grooming Procedure'. Category: Backlog Management. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Product Backlog Grooming Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-PROD-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProductHub. the Product Manager gathers the required data and documents, including refining acceptance criteria and confirming feasibility with Engineering. The review team examines the Product Backlog against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROD-007

---

## TCK3-PROD-00141 — Roadmap Planning (P3, Resolved)
**Created:** 2026-08-06 via Portal  |  **Requester:** Manoj Sharma  |  **Assigned to:** Karan Pillai

**Description:** Manoj Sharma (Research & Development) reported an issue via Portal related to 'Feature Prioritization Procedure'. Category: Roadmap Planning. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Feature Prioritization Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-PROD-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProductHub. the Product Manager gathers the required data and documents, including scoring features against reach, impact, confidence, and effort (RICE). The review team examines the Product Roadmap against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Head of Product discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROD-002

---

## TCK3-PROD-00116 — Customer Engagement (P4, Closed)
**Created:** 2026-08-08 via Email  |  **Requester:** Simran Joshi  |  **Assigned to:** Varun Reddy

**Description:** Simran Joshi (Management / Leadership) reported an issue via Email related to 'Customer Advisory Board Session Procedure'. Category: Customer Engagement. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Customer Advisory Board Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-PROD-015 to resolve. the Product Manager confirms eligibility and prerequisites: preparing the agenda and roadmap preview for key customers. the Product Manager raises a request in MK-ProductHub specifying exactly which Advisory Board Session is required. The VP Product reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Advisory Board Session in the relevant system. the Product Manager is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-PROD-015

---

## TCK3-PROD-00112 — Market Research (P4, Resolved)
**Created:** 2026-08-15 via Portal  |  **Requester:** Aditya Verma  |  **Assigned to:** Preeti Kapoor

**Description:** Aditya Verma (Administration / Facilities) reported an issue via Portal related to 'Competitive Analysis Procedure'. Category: Market Research. Logged against MK-ProductHub.

**Investigation:** The assigned specialist reviewed the MK-ProductHub record, confirmed the reported symptom against 'Competitive Analysis Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-PROD-006 to resolve. The review is scheduled in advance and stakeholders are notified through MK-ProductHub. the Product Manager gathers the required data and documents, including feature comparison, pricing, and positioning against key competitors. The review team examines the Competitive Analysis Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Head of Product discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-PROD-006

---
