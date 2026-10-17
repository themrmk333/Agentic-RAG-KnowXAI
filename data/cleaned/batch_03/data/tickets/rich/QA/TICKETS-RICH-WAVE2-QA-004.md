# QA / Testing — Rich Historical Ticket Archive (wave2, Page 4)

## TCK3-QA-00033 — Reporting (P4, Resolved)
**Created:** 2025-07-13 via Live Chat  |  **Requester:** Ananya Bose  |  **Assigned to:** Manoj Nair

**Description:** Ananya Bose (DevOps & Cloud) reported an issue via Live Chat related to 'QA Metrics Reporting Procedure'. Category: Reporting. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Metrics Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-QA-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including defect leakage rate, test coverage %, and automation pass rate. The review team examines the QA Metrics Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-016

---

## TCK3-QA-00096 — Defect Management (P3, Closed)
**Created:** 2025-07-15 via Portal  |  **Requester:** Varun Chowdhury  |  **Assigned to:** Sneha Reddy

**Description:** Varun Chowdhury (Sales) reported an issue via Portal related to 'Defect Triage Meeting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Defect Triage Meeting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-QA-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority. The review team examines the Defect Triage against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-009

---

## TCK3-QA-00028 — Defect Management (P3, Resolved)
**Created:** 2025-07-16 via Walk-in  |  **Requester:** Sneha Reddy  |  **Assigned to:** Rahul Desai

**Description:** Sneha Reddy (QA / Testing) reported an issue via Walk-in related to 'Defect Triage Meeting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Defect Triage Meeting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-QA-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority. The review team examines the Defect Triage against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-009

---

## TCK3-QA-00068 — Security Testing (P1, Resolved)
**Created:** 2025-07-18 via Portal  |  **Requester:** Ananya Desai  |  **Assigned to:** Vikram Malhotra

**Description:** Ananya Desai (Legal & Compliance) reported an issue via Portal related to 'Security Regression Testing Coordination'. Category: Security Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Security Regression Testing Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release. The review team examines the Security Test Pass against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Analyst discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-013

---

## TCK3-QA-00074 — Test Data (P3, Resolved)
**Created:** 2025-07-18 via Phone  |  **Requester:** Pooja Agarwal  |  **Assigned to:** Harsh Chauhan

**Description:** Pooja Agarwal (Marketing) reported an issue via Phone related to 'Test Data Management Procedure'. Category: Test Data. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Data Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-014 to resolve. the QA Engineer confirms eligibility and prerequisites: masking any production-like sensitive fields before use. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Data Set is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Test Data Set in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-014

---

## TCK3-QA-00099 — Performance Testing (P3, In Progress)
**Created:** 2025-07-26 via Portal  |  **Requester:** Yash Mehta  |  **Assigned to:** Divya Bose

**Description:** Yash Mehta (Software Engineering / Development) reported an issue via Portal related to 'Performance Test Execution'. Category: Performance Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Performance Test Execution', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-006

---

## TCK3-QA-00055 — Security Testing (P4, Resolved)
**Created:** 2025-08-15 via Slack  |  **Requester:** Dev Malhotra  |  **Assigned to:** Kabir Reddy

**Description:** Dev Malhotra (Cybersecurity / Information Security) reported an issue via Slack related to 'Security Regression Testing Coordination'. Category: Security Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Security Regression Testing Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-QA-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release. The review team examines the Security Test Pass against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Analyst discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-013

---

## TCK3-QA-00113 — Test Data (P3, Resolved)
**Created:** 2025-08-21 via Slack  |  **Requester:** Nidhi Mehta  |  **Assigned to:** Sahil Menon

**Description:** Nidhi Mehta (Human Resources) reported an issue via Slack related to 'Test Data Management Procedure'. Category: Test Data. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Data Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-014 to resolve. the QA Engineer confirms eligibility and prerequisites: masking any production-like sensitive fields before use. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Data Set is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Test Data Set in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-014

---

## TCK3-QA-00079 — Defect Management (P4, Resolved)
**Created:** 2025-09-05 via Walk-in  |  **Requester:** Divya Malhotra  |  **Assigned to:** Varun Menon

**Description:** Divya Malhotra (Product Management) reported an issue via Walk-in related to 'Defect Triage Meeting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Defect Triage Meeting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-QA-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority. The review team examines the Defect Triage against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-009

---

## TCK3-QA-00075 — Test Execution (P4, Resolved)
**Created:** 2025-09-07 via Walk-in  |  **Requester:** Simran Malhotra  |  **Assigned to:** Divya Gupta

**Description:** Simran Malhotra (Finance & Accounting) reported an issue via Walk-in related to 'Regression Test Cycle Execution'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Regression Test Cycle Execution', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-003 to resolve. the QA Engineer confirms eligibility and prerequisites: selecting the regression suite relevant to the changed modules. the QA Engineer raises a request in MK-TestHub specifying exactly which Regression Cycle is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Regression Cycle in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-003

---

## TCK3-QA-00056 — Defect Management (P4, Resolved)
**Created:** 2025-09-13 via Walk-in  |  **Requester:** Riya Pillai  |  **Assigned to:** Sneha Reddy

**Description:** Riya Pillai (Software Engineering / Development) reported an issue via Walk-in related to 'Defect Triage Meeting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Defect Triage Meeting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-QA-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority. The review team examines the Defect Triage against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-009

---

## TCK3-QA-00146 — Test Execution (P3, Resolved)
**Created:** 2025-09-14 via Walk-in  |  **Requester:** Aditya Sharma  |  **Assigned to:** Divya Gupta

**Description:** Aditya Sharma (Finance & Accounting) reported an issue via Walk-in related to 'Regression Test Cycle Execution'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Regression Test Cycle Execution', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-QA-003 to resolve. the QA Engineer confirms eligibility and prerequisites: selecting the regression suite relevant to the changed modules. the QA Engineer raises a request in MK-TestHub specifying exactly which Regression Cycle is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Regression Cycle in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-003

---

## TCK3-QA-00133 — Test Planning (P4, Resolved)
**Created:** 2025-09-16 via Portal  |  **Requester:** Bhavna Gupta  |  **Assigned to:** Varun Menon

**Description:** Bhavna Gupta (Legal & Compliance) reported an issue via Portal related to 'Test Case Design and Review'. Category: Test Planning. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Case Design and Review', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including requirement traceability and edge-case coverage. The review team examines the Test Case Suite against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-002

---

## TCK3-QA-00032 — Test Execution (P3, Resolved)
**Created:** 2025-09-23 via Live Chat  |  **Requester:** Dev Sharma  |  **Assigned to:** Manoj Nair

**Description:** Dev Sharma (Product Management) reported an issue via Live Chat related to 'API Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'API Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-011 to resolve. the QA Engineer confirms eligibility and prerequisites: validating response schema, status codes, and error handling. the QA Engineer raises a request in MK-TestHub specifying exactly which API Test Suite is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the API Test Suite in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-011

---

## TCK3-QA-00145 — Defect Management (P4, Resolved)
**Created:** 2025-09-27 via Slack  |  **Requester:** Karan Bhatt  |  **Assigned to:** Preeti Menon

**Description:** Karan Bhatt (DevOps & Cloud) reported an issue via Slack related to 'Defect Triage Meeting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Defect Triage Meeting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority. The review team examines the Defect Triage against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-009

---

## TCK3-QA-00037 — Test Execution (P3, Resolved)
**Created:** 2025-10-01 via Slack  |  **Requester:** Neel Reddy  |  **Assigned to:** Divya Gupta

**Description:** Neel Reddy (Data & Analytics) reported an issue via Slack related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00035 — UAT (P3, Resolved)
**Created:** 2025-10-03 via Phone  |  **Requester:** Sneha Sharma  |  **Assigned to:** Varun Menon

**Description:** Sneha Sharma (Research & Development) reported an issue via Phone related to 'User Acceptance Testing (UAT) Coordination'. Category: UAT. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'User Acceptance Testing (UAT) Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-QA-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including business scenarios and sign-off criteria agreed with stakeholders. The review team examines the UAT Cycle against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Product Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-007

---

## TCK3-QA-00087 — Onboarding (P4, Resolved)
**Created:** 2025-10-12 via Walk-in  |  **Requester:** Swati Malhotra  |  **Assigned to:** Varun Menon

**Description:** Swati Malhotra (IT Support / Information Technology) reported an issue via Walk-in related to 'QA Onboarding Procedure'. Category: Onboarding. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-QA-012 to resolve. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The QA Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-QA-012

---

## TCK3-QA-00109 — Onboarding (P3, Resolved)
**Created:** 2025-10-13 via Email  |  **Requester:** Riya Pillai  |  **Assigned to:** Divya Menon

**Description:** Riya Pillai (Software Engineering / Development) reported an issue via Email related to 'QA Onboarding Procedure'. Category: Onboarding. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-QA-012 to resolve. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The QA Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-QA-012

---

## TCK3-QA-00143 — Test Execution (P3, In Progress)
**Created:** 2025-10-14 via Slack  |  **Requester:** Siddharth Iyer  |  **Assigned to:** Sneha Reddy

**Description:** Siddharth Iyer (Management / Leadership) reported an issue via Slack related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---