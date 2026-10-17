# QA / Testing — Rich Historical Ticket Archive (wave2, Page 2)

## TCK3-QA-00115 — Test Planning (P3, Closed)
**Created:** 2024-10-21 via Walk-in  |  **Requester:** Ananya Nair  |  **Assigned to:** Divya Bose

**Description:** Ananya Nair (Cybersecurity / Information Security) reported an issue via Walk-in related to 'Test Case Design and Review'. Category: Test Planning. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Case Design and Review', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-QA-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including requirement traceability and edge-case coverage. The review team examines the Test Case Suite against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-002

---

## TCK3-QA-00147 — Reporting (P2, Resolved)
**Created:** 2024-10-23 via Slack  |  **Requester:** Arjun Chowdhury  |  **Assigned to:** Vikram Malhotra

**Description:** Arjun Chowdhury (Finance & Accounting) reported an issue via Slack related to 'QA Metrics Reporting Procedure'. Category: Reporting. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Metrics Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-QA-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including defect leakage rate, test coverage %, and automation pass rate. The review team examines the QA Metrics Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-016

---

## TCK3-QA-00141 — Test Execution (P2, Closed)
**Created:** 2024-11-04 via Portal  |  **Requester:** Rohan Reddy  |  **Assigned to:** Rahul Desai

**Description:** Rohan Reddy (Procurement / Purchasing) reported an issue via Portal related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00101 — Test Automation (P4, Closed)
**Created:** 2024-11-17 via Live Chat  |  **Requester:** Simran Malhotra  |  **Assigned to:** Sneha Reddy

**Description:** Simran Malhotra (Finance & Accounting) reported an issue via Live Chat related to 'Test Automation Script Development'. Category: Test Automation. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Automation Script Development', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-004 to resolve. the QA Automation Engineer confirms eligibility and prerequisites: adding the script to the MK-TestHub automation pipeline with tagging. the QA Automation Engineer raises a request in MK-TestHub specifying exactly which Automation Script is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Automation Script in the relevant system. the QA Automation Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-004

---

## TCK3-QA-00062 — Test Execution (P3, Resolved)
**Created:** 2024-11-26 via Email  |  **Requester:** Alisha Menon  |  **Assigned to:** Alisha Verma

**Description:** Alisha Menon (QA / Testing) reported an issue via Email related to 'Mobile App Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Mobile App Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-010 to resolve. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-010

---

## TCK3-QA-00025 — Test Data (P4, Resolved)
**Created:** 2024-11-30 via Portal  |  **Requester:** Kavya Reddy  |  **Assigned to:** Divya Menon

**Description:** Kavya Reddy (Finance & Accounting) reported an issue via Portal related to 'Test Data Management Procedure'. Category: Test Data. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Data Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-014 to resolve. the QA Engineer confirms eligibility and prerequisites: masking any production-like sensitive fields before use. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Data Set is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Test Data Set in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-014

---

## TCK3-QA-00071 — Defect Management (P4, Resolved)
**Created:** 2024-12-02 via Live Chat  |  **Requester:** Ritika Rao  |  **Assigned to:** Rahul Desai

**Description:** Ritika Rao (Human Resources) reported an issue via Live Chat related to 'Software Defect Reporting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Software Defect Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-QA-001 to resolve. the QA Engineer logs into MK-TestHub and navigates to the 'Defect Report' section. the QA Engineer selects 'New Defect Report' and enters the required details, including steps to reproduce, expected vs actual result, and severity. the QA Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the QA Engineer submits the Defect Report; MK-TestHub automatically routes it to the QA Lead for review. The QA Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-QA-001

---

## TCK3-QA-00108 — Environment Management (P4, Resolved)
**Created:** 2024-12-06 via Slack  |  **Requester:** Kavya Iyer  |  **Assigned to:** Rahul Desai

**Description:** Kavya Iyer (Finance & Accounting) reported an issue via Slack related to 'Test Environment Setup Request'. Category: Environment Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Environment Setup Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-008 to resolve. the QA Engineer confirms eligibility and prerequisites: the required data set, build version, and configuration. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Environment is required. The DevOps Engineer reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Test Environment in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-008

---

## TCK3-QA-00135 — Test Execution (P1, Resolved)
**Created:** 2024-12-08 via Portal  |  **Requester:** Gaurav Chowdhury  |  **Assigned to:** Manoj Nair

**Description:** Gaurav Chowdhury (Marketing) reported an issue via Portal related to 'Mobile App Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Mobile App Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-QA-010 to resolve. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-010

---

## TCK3-QA-00121 — Release Management (P3, Resolved)
**Created:** 2024-12-10 via Slack  |  **Requester:** Preeti Kapoor  |  **Assigned to:** Alisha Verma

**Description:** Preeti Kapoor (Product Management) reported an issue via Slack related to 'Release Sign-off / Go-No-Go Procedure'. Category: Release Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Release Sign-off / Go-No-Go Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including open defect count by severity and outstanding test coverage gaps. The review team examines the Release Readiness Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-005

---

## TCK3-QA-00049 — Reporting (P4, Resolved)
**Created:** 2024-12-18 via Walk-in  |  **Requester:** Aditya Rao  |  **Assigned to:** Divya Gupta

**Description:** Aditya Rao (Procurement / Purchasing) reported an issue via Walk-in related to 'QA Metrics Reporting Procedure'. Category: Reporting. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Metrics Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including defect leakage rate, test coverage %, and automation pass rate. The review team examines the QA Metrics Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-016

---

## TCK3-QA-00131 — Onboarding (P4, Resolved)
**Created:** 2024-12-18 via Portal  |  **Requester:** Aditya Rao  |  **Assigned to:** Divya Gupta

**Description:** Aditya Rao (DevOps & Cloud) reported an issue via Portal related to 'QA Onboarding Procedure'. Category: Onboarding. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-QA-012 to resolve. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The QA Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-QA-012

---

## TCK3-QA-00021 — UAT (P3, Closed)
**Created:** 2024-12-25 via Phone  |  **Requester:** Ritika Singh  |  **Assigned to:** Alisha Verma

**Description:** Ritika Singh (Human Resources) reported an issue via Phone related to 'User Acceptance Testing (UAT) Coordination'. Category: UAT. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'User Acceptance Testing (UAT) Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-QA-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including business scenarios and sign-off criteria agreed with stakeholders. The review team examines the UAT Cycle against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Product Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-007

---

## TCK3-QA-00051 — Security Testing (P3, Resolved)
**Created:** 2025-01-11 via Portal  |  **Requester:** Bhavna Desai  |  **Assigned to:** Alisha Verma

**Description:** Bhavna Desai (Project Management / PMO) reported an issue via Portal related to 'Security Regression Testing Coordination'. Category: Security Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Security Regression Testing Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release. The review team examines the Security Test Pass against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Analyst discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-013

---

## TCK3-QA-00036 — Test Automation (P4, Resolved)
**Created:** 2025-01-21 via Slack  |  **Requester:** Swati Nair  |  **Assigned to:** Divya Gupta

**Description:** Swati Nair (Finance & Accounting) reported an issue via Slack related to 'Test Automation Script Development'. Category: Test Automation. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Automation Script Development', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-004 to resolve. the QA Automation Engineer confirms eligibility and prerequisites: adding the script to the MK-TestHub automation pipeline with tagging. the QA Automation Engineer raises a request in MK-TestHub specifying exactly which Automation Script is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Automation Script in the relevant system. the QA Automation Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-004

---

## TCK3-QA-00142 — Test Execution (P3, Resolved)
**Created:** 2025-01-24 via Slack  |  **Requester:** Dev Malhotra  |  **Assigned to:** Divya Gupta

**Description:** Dev Malhotra (Cybersecurity / Information Security) reported an issue via Slack related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00118 — Environment Management (P2, In Progress)
**Created:** 2025-02-04 via Live Chat  |  **Requester:** Aditya Sharma  |  **Assigned to:** Divya Bose

**Description:** Aditya Sharma (Finance & Accounting) reported an issue via Live Chat related to 'Test Environment Setup Request'. Category: Environment Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Environment Setup Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-008

---

## TCK3-QA-00102 — Test Automation (P4, Resolved)
**Created:** 2025-02-06 via Slack  |  **Requester:** Simran Agarwal  |  **Assigned to:** Vikram Malhotra

**Description:** Simran Agarwal (Research & Development) reported an issue via Slack related to 'Test Automation Script Development'. Category: Test Automation. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Automation Script Development', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-004 to resolve. the QA Automation Engineer confirms eligibility and prerequisites: adding the script to the MK-TestHub automation pipeline with tagging. the QA Automation Engineer raises a request in MK-TestHub specifying exactly which Automation Script is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Automation Script in the relevant system. the QA Automation Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-004

---

## TCK3-QA-00126 — Test Execution (P2, Resolved)
**Created:** 2025-02-07 via Phone  |  **Requester:** Kabir Nair  |  **Assigned to:** Divya Bose

**Description:** Kabir Nair (Administration / Facilities) reported an issue via Phone related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00130 — Test Execution (P2, In Progress)
**Created:** 2025-02-10 via Email  |  **Requester:** Siddharth Singh  |  **Assigned to:** Divya Menon

**Description:** Siddharth Singh (Procurement / Purchasing) reported an issue via Email related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---