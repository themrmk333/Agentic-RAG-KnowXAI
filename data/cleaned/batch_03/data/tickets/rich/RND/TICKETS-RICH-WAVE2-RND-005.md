# Research & Development — Rich Historical Ticket Archive (wave2, Page 5)

## TCK3-RND-00131 — Publications (P3, Resolved)
**Created:** 2025-10-03 via Walk-in  |  **Requester:** Vikram Bhatt  |  **Assigned to:** Harsh Gupta

**Description:** Vikram Bhatt (Human Resources) reported an issue via Walk-in related to 'Research Publication Approval Procedure'. Category: Publications. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Publication Approval Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-RND-006 to resolve. the Research Engineer logs into MK-Labs and navigates to the 'Publication Request' section. the Research Engineer selects 'New Publication Request' and enters the required details, including checking for any confidential or IP-sensitive content before submission. the Research Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Research Engineer submits the Publication Request; MK-Labs automatically routes it to the R&D Director for review. The R&D Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-RND-006

---

## TCK3-RND-00049 — Risk Management (P4, Resolved)
**Created:** 2025-10-17 via Portal  |  **Requester:** Ritika Singh  |  **Assigned to:** Aditya Singh

**Description:** Ritika Singh (Procurement / Purchasing) reported an issue via Portal related to 'Research Risk Assessment Procedure'. Category: Risk Management. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Risk Assessment Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-RND-015 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Research Lead gathers the required data and documents, including technical risk, timeline risk, and dependency on external data/tools. The review team examines the Research Risk Assessment against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The R&D Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-015

---

## TCK3-RND-00055 — Onboarding (P3, In Progress)
**Created:** 2025-10-31 via Email  |  **Requester:** Tanya Mehta  |  **Assigned to:** Aditya Joshi

**Description:** Tanya Mehta (Human Resources) reported an issue via Email related to 'Research Onboarding Procedure'. Category: Onboarding. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-RND-010

---

## TCK3-RND-00146 — Responsible AI (P3, Resolved)
**Created:** 2025-10-31 via Walk-in  |  **Requester:** Isha Iyer  |  **Assigned to:** Aditya Singh

**Description:** Isha Iyer (Data & Analytics) reported an issue via Walk-in related to 'Responsible AI / Ethics Review Procedure'. Category: Responsible AI. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Responsible AI / Ethics Review Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-RND-008 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Research Lead gathers the required data and documents, including assessing bias, fairness, and potential misuse of the research direction. The review team examines the Ethics Review against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The R&D Director discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-008

---

## TCK3-RND-00135 — Infrastructure (P3, Resolved)
**Created:** 2025-11-02 via Slack  |  **Requester:** Alisha Pillai  |  **Assigned to:** Meera Pillai

**Description:** Alisha Pillai (Cybersecurity / Information Security) reported an issue via Slack related to 'Compute Resource Request for Research'. Category: Infrastructure. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Compute Resource Request for Research', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-RND-007 to resolve. the AI Research Engineer logs into MK-Labs and navigates to the 'Compute Request' section. the AI Research Engineer selects 'New Compute Request' and enters the required details, including GPU/TPU hours required and expected experiment duration. the AI Research Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the AI Research Engineer submits the Compute Request; MK-Labs automatically routes it to the R&D Manager for review. The R&D Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-RND-007

---

## TCK3-RND-00075 — Experimentation (P3, Resolved)
**Created:** 2025-11-11 via Walk-in  |  **Requester:** Siddharth Verma  |  **Assigned to:** Dev Menon

**Description:** Siddharth Verma (Data & Analytics) reported an issue via Walk-in related to 'Experiment Design and Tracking Procedure'. Category: Experimentation. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Experiment Design and Tracking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-RND-002 to resolve. the AI Research Engineer confirms eligibility and prerequisites: logging hyperparameters, dataset version, and evaluation metrics in MK-Labs. the AI Research Engineer raises a request in MK-Labs specifying exactly which Research Experiment is required. The Research Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Research Experiment in the relevant system. the AI Research Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-RND-002

---

## TCK3-RND-00141 — Technology Transfer (P3, Resolved)
**Created:** 2025-11-16 via Email  |  **Requester:** Ritika Agarwal  |  **Assigned to:** Aditya Singh

**Description:** Ritika Agarwal (Project Management / PMO) reported an issue via Email related to 'Research-to-Production Handover Procedure'. Category: Technology Transfer. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research-to-Production Handover Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-RND-004 to resolve. the Research Lead logs into MK-Labs and navigates to the 'Research Handover' section. the Research Lead selects 'New Research Handover' and enters the required details, including model artifacts, evaluation results, and known limitations documentation. the Research Lead attaches any supporting documentation and reviews the entry for accuracy before submitting. the Research Lead submits the Research Handover; MK-Labs automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-RND-004

---

## TCK3-RND-00052 — Publications (P4, Resolved)
**Created:** 2025-11-17 via Walk-in  |  **Requester:** Divya Chowdhury  |  **Assigned to:** Aditya Joshi

**Description:** Divya Chowdhury (Human Resources) reported an issue via Walk-in related to 'Research Publication Approval Procedure'. Category: Publications. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Publication Approval Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-RND-006 to resolve. the Research Engineer logs into MK-Labs and navigates to the 'Publication Request' section. the Research Engineer selects 'New Publication Request' and enters the required details, including checking for any confidential or IP-sensitive content before submission. the Research Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the Research Engineer submits the Publication Request; MK-Labs automatically routes it to the R&D Director for review. The R&D Director reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-RND-006

---

## TCK3-RND-00069 — Data Governance (P4, Resolved)
**Created:** 2025-11-21 via Walk-in  |  **Requester:** Ananya Menon  |  **Assigned to:** Manoj Sharma

**Description:** Ananya Menon (Human Resources) reported an issue via Walk-in related to 'Research Data Retention Procedure'. Category: Data Governance. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Data Retention Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-RND-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Research Associate gathers the required data and documents, including reviewing experiment artifacts against the retention schedule. The review team examines the Research Data Retention against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The R&D Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-012

---

## TCK3-RND-00073 — Infrastructure (P3, Resolved)
**Created:** 2025-11-24 via Email  |  **Requester:** Ananya Nair  |  **Assigned to:** Priya Bose

**Description:** Ananya Nair (IT Support / Information Technology) reported an issue via Email related to 'Compute Resource Request for Research'. Category: Infrastructure. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Compute Resource Request for Research', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-RND-007 to resolve. the AI Research Engineer logs into MK-Labs and navigates to the 'Compute Request' section. the AI Research Engineer selects 'New Compute Request' and enters the required details, including GPU/TPU hours required and expected experiment duration. the AI Research Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the AI Research Engineer submits the Compute Request; MK-Labs automatically routes it to the R&D Manager for review. The R&D Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-RND-007

---

## TCK3-RND-00070 — Technology Transfer (P4, Resolved)
**Created:** 2025-11-26 via Email  |  **Requester:** Nisha Bose  |  **Assigned to:** Simran Agarwal

**Description:** Nisha Bose (Customer Support / Helpdesk) reported an issue via Email related to 'Research-to-Production Handover Procedure'. Category: Technology Transfer. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research-to-Production Handover Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-RND-004 to resolve. the Research Lead logs into MK-Labs and navigates to the 'Research Handover' section. the Research Lead selects 'New Research Handover' and enters the required details, including model artifacts, evaluation results, and known limitations documentation. the Research Lead attaches any supporting documentation and reviews the entry for accuracy before submitting. the Research Lead submits the Research Handover; MK-Labs automatically routes it to the Engineering Manager for review. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-RND-004

---

## TCK3-RND-00087 — Model Evaluation (P2, Resolved)
**Created:** 2025-12-16 via Portal  |  **Requester:** Kavya Desai  |  **Assigned to:** Meera Pillai

**Description:** Kavya Desai (Procurement / Purchasing) reported an issue via Portal related to 'Model Evaluation and Benchmarking Procedure'. Category: Model Evaluation. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Model Evaluation and Benchmarking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-RND-003 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Senior Research Engineer gathers the required data and documents, including comparing against the current production baseline on the standard eval suite. The review team examines the Model Benchmark against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Research Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-003

---

## TCK3-RND-00149 — Data Governance (P3, Resolved)
**Created:** 2025-12-19 via Portal  |  **Requester:** Varun Nair  |  **Assigned to:** Sneha Sharma

**Description:** Varun Nair (IT Support / Information Technology) reported an issue via Portal related to 'Research Data Retention Procedure'. Category: Data Governance. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Data Retention Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-RND-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Research Associate gathers the required data and documents, including reviewing experiment artifacts against the retention schedule. The review team examines the Research Data Retention against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The R&D Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-012

---

## TCK3-RND-00066 — Model Evaluation (P3, Resolved)
**Created:** 2025-12-20 via Portal  |  **Requester:** Simran Agarwal  |  **Assigned to:** Neel Agarwal

**Description:** Simran Agarwal (Finance & Accounting) reported an issue via Portal related to 'Model Evaluation and Benchmarking Procedure'. Category: Model Evaluation. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Model Evaluation and Benchmarking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-RND-003 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Senior Research Engineer gathers the required data and documents, including comparing against the current production baseline on the standard eval suite. The review team examines the Model Benchmark against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Research Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-003

---

## TCK3-RND-00034 — Model Evaluation (P4, Resolved)
**Created:** 2025-12-26 via Slack  |  **Requester:** Ritika Mehta  |  **Assigned to:** Nisha Joshi

**Description:** Ritika Mehta (Research & Development) reported an issue via Slack related to 'Model Evaluation and Benchmarking Procedure'. Category: Model Evaluation. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Model Evaluation and Benchmarking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-RND-003 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Senior Research Engineer gathers the required data and documents, including comparing against the current production baseline on the standard eval suite. The review team examines the Model Benchmark against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Research Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-003

---

## TCK3-RND-00091 — Data Governance (P3, Resolved)
**Created:** 2025-12-29 via Phone  |  **Requester:** Aman Singh  |  **Assigned to:** Aman Verma

**Description:** Aman Singh (Marketing) reported an issue via Phone related to 'Research Data Retention Procedure'. Category: Data Governance. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Data Retention Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-RND-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Research Associate gathers the required data and documents, including reviewing experiment artifacts against the retention schedule. The review team examines the Research Data Retention against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The R&D Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-012

---

## TCK3-RND-00101 — Model Evaluation (P4, Resolved)
**Created:** 2025-12-30 via Email  |  **Requester:** Aman Singh  |  **Assigned to:** Neel Agarwal

**Description:** Aman Singh (Marketing) reported an issue via Email related to 'Model Evaluation and Benchmarking Procedure'. Category: Model Evaluation. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Model Evaluation and Benchmarking Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-RND-003 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Senior Research Engineer gathers the required data and documents, including comparing against the current production baseline on the standard eval suite. The review team examines the Model Benchmark against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Research Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-003

---

## TCK3-RND-00058 — Research Planning (P4, Resolved)
**Created:** 2026-01-02 via Slack  |  **Requester:** Preeti Verma  |  **Assigned to:** Nisha Joshi

**Description:** Preeti Verma (Software Engineering / Development) reported an issue via Slack related to 'Research Proposal Submission Procedure'. Category: Research Planning. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Proposal Submission Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A budget/cost-centre code entered was inactive for the current fiscal period.

**Resolution:** Followed SOP-RND-001 to resolve. the Research Associate logs into MK-Labs and navigates to the 'Research Proposal' section. the Research Associate selects 'New Research Proposal' and enters the required details, including hypothesis, expected impact, and required resources. the Research Associate attaches any supporting documentation and reviews the entry for accuracy before submitting. the Research Associate submits the Research Proposal; MK-Labs automatically routes it to the R&D Manager for review. The R&D Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-RND-001

---

## TCK3-RND-00033 — Data Governance (P4, In Progress)
**Created:** 2026-01-14 via Portal  |  **Requester:** Aman Pillai  |  **Assigned to:** Aditya Singh

**Description:** Aman Pillai (Data & Analytics) reported an issue via Portal related to 'Research Data Retention Procedure'. Category: Data Governance. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Data Retention Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-012

---

## TCK3-RND-00032 — Data Governance (P4, Closed)
**Created:** 2026-01-20 via Walk-in  |  **Requester:** Dev Menon  |  **Assigned to:** Yash Iyer

**Description:** Dev Menon (Research & Development) reported an issue via Walk-in related to 'Research Data Retention Procedure'. Category: Data Governance. Logged against MK-Labs.

**Investigation:** The assigned specialist reviewed the MK-Labs record, confirmed the reported symptom against 'Research Data Retention Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-RND-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Labs. the Research Associate gathers the required data and documents, including reviewing experiment artifacts against the retention schedule. The review team examines the Research Data Retention against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The R&D Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-RND-012

---