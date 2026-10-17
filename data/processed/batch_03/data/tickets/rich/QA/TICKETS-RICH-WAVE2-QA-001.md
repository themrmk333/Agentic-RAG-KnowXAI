# QA / Testing — Rich Historical Ticket Archive (wave2, Page 1)

## TCK3-QA-00040 — Test Execution (P4, Resolved)
**Created:** 2024-06-04 via Email  |  **Requester:** Nisha Desai  |  **Assigned to:** Divya Bose

**Description:** Nisha Desai (Management / Leadership) reported an issue via Email related to 'API Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'API Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-011 to resolve. the QA Engineer confirms eligibility and prerequisites: validating response schema, status codes, and error handling. the QA Engineer raises a request in MK-TestHub specifying exactly which API Test Suite is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the API Test Suite in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-011

---

## TCK3-QA-00112 — Release Management (P4, Closed)
**Created:** 2024-06-06 via Walk-in  |  **Requester:** Kabir Nair  |  **Assigned to:** Varun Menon

**Description:** Kabir Nair (Administration / Facilities) reported an issue via Walk-in related to 'Release Sign-off / Go-No-Go Procedure'. Category: Release Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Release Sign-off / Go-No-Go Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-QA-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including open defect count by severity and outstanding test coverage gaps. The review team examines the Release Readiness Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-005

---

## TCK3-QA-00097 — UAT (P3, Resolved)
**Created:** 2024-06-13 via Portal  |  **Requester:** Neel Malhotra  |  **Assigned to:** Kabir Reddy

**Description:** Neel Malhotra (Cybersecurity / Information Security) reported an issue via Portal related to 'User Acceptance Testing (UAT) Coordination'. Category: UAT. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'User Acceptance Testing (UAT) Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-QA-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including business scenarios and sign-off criteria agreed with stakeholders. The review team examines the UAT Cycle against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Product Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-007

---

## TCK3-QA-00123 — Test Planning (P3, Resolved)
**Created:** 2024-06-15 via Live Chat  |  **Requester:** Riya Chauhan  |  **Assigned to:** Harsh Chauhan

**Description:** Riya Chauhan (DevOps & Cloud) reported an issue via Live Chat related to 'Test Case Design and Review'. Category: Test Planning. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Case Design and Review', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-QA-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including requirement traceability and edge-case coverage. The review team examines the Test Case Suite against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-002

---

## TCK3-QA-00125 — Reporting (P3, Resolved)
**Created:** 2024-06-15 via Portal  |  **Requester:** Gaurav Mehta  |  **Assigned to:** Sahil Menon

**Description:** Gaurav Mehta (Data & Analytics) reported an issue via Portal related to 'QA Metrics Reporting Procedure'. Category: Reporting. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Metrics Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-QA-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including defect leakage rate, test coverage %, and automation pass rate. The review team examines the QA Metrics Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-016

---

## TCK3-QA-00104 — Test Execution (P3, Resolved)
**Created:** 2024-07-11 via Email  |  **Requester:** Siddharth Verma  |  **Assigned to:** Varun Menon

**Description:** Siddharth Verma (Data & Analytics) reported an issue via Email related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00136 — Test Automation (P3, Resolved)
**Created:** 2024-07-13 via Live Chat  |  **Requester:** Anjali Nair  |  **Assigned to:** Divya Menon

**Description:** Anjali Nair (Cybersecurity / Information Security) reported an issue via Live Chat related to 'Test Automation Script Development'. Category: Test Automation. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Automation Script Development', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-004 to resolve. the QA Automation Engineer confirms eligibility and prerequisites: adding the script to the MK-TestHub automation pipeline with tagging. the QA Automation Engineer raises a request in MK-TestHub specifying exactly which Automation Script is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Automation Script in the relevant system. the QA Automation Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-004

---

## TCK3-QA-00120 — Test Execution (P4, Closed)
**Created:** 2024-07-21 via Walk-in  |  **Requester:** Manoj Nair  |  **Assigned to:** Divya Gupta

**Description:** Manoj Nair (Cybersecurity / Information Security) reported an issue via Walk-in related to 'Mobile App Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Mobile App Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-QA-010 to resolve. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-010

---

## TCK3-QA-00107 — Defect Management (P3, Closed)
**Created:** 2024-07-24 via Phone  |  **Requester:** Aditya Rao  |  **Assigned to:** Divya Gupta

**Description:** Aditya Rao (Procurement / Purchasing) reported an issue via Phone related to 'Defect Triage Meeting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Defect Triage Meeting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority. The review team examines the Defect Triage against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-009

---

## TCK3-QA-00082 — Test Execution (P2, Closed)
**Created:** 2024-08-03 via Email  |  **Requester:** Nidhi Pillai  |  **Assigned to:** Alisha Verma

**Description:** Nidhi Pillai (Human Resources) reported an issue via Email related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00124 — Environment Management (P4, Resolved)
**Created:** 2024-08-07 via Live Chat  |  **Requester:** Naveen Singh  |  **Assigned to:** Alisha Verma

**Description:** Naveen Singh (Human Resources) reported an issue via Live Chat related to 'Test Environment Setup Request'. Category: Environment Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Environment Setup Request', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-008 to resolve. the QA Engineer confirms eligibility and prerequisites: the required data set, build version, and configuration. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Environment is required. The DevOps Engineer reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Test Environment in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-008

---

## TCK3-QA-00114 — Defect Management (P4, Resolved)
**Created:** 2024-08-20 via Portal  |  **Requester:** Shreya Reddy  |  **Assigned to:** Alisha Verma

**Description:** Shreya Reddy (Product Management) reported an issue via Portal related to 'Software Defect Reporting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Software Defect Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-QA-001 to resolve. the QA Engineer logs into MK-TestHub and navigates to the 'Defect Report' section. the QA Engineer selects 'New Defect Report' and enters the required details, including steps to reproduce, expected vs actual result, and severity. the QA Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the QA Engineer submits the Defect Report; MK-TestHub automatically routes it to the QA Lead for review. The QA Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-QA-001

---

## TCK3-QA-00119 — Test Execution (P3, Closed)
**Created:** 2024-08-27 via Phone  |  **Requester:** Bhavna Kapoor  |  **Assigned to:** Rahul Desai

**Description:** Bhavna Kapoor (DevOps & Cloud) reported an issue via Phone related to 'Regression Test Cycle Execution'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Regression Test Cycle Execution', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-003 to resolve. the QA Engineer confirms eligibility and prerequisites: selecting the regression suite relevant to the changed modules. the QA Engineer raises a request in MK-TestHub specifying exactly which Regression Cycle is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Regression Cycle in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-003

---

## TCK3-QA-00042 — Test Execution (P2, Closed)
**Created:** 2024-09-07 via Email  |  **Requester:** Sahil Chowdhury  |  **Assigned to:** Harsh Chauhan

**Description:** Sahil Chowdhury (Legal & Compliance) reported an issue via Email related to 'Regression Test Cycle Execution'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Regression Test Cycle Execution', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-QA-003 to resolve. the QA Engineer confirms eligibility and prerequisites: selecting the regression suite relevant to the changed modules. the QA Engineer raises a request in MK-TestHub specifying exactly which Regression Cycle is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Regression Cycle in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-003

---

## TCK3-QA-00078 — Test Execution (P3, Resolved)
**Created:** 2024-09-08 via Phone  |  **Requester:** Harsh Chauhan  |  **Assigned to:** Varun Menon

**Description:** Harsh Chauhan (QA / Testing) reported an issue via Phone related to 'Mobile App Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Mobile App Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-010 to resolve. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-010

---

## TCK3-QA-00106 — Test Execution (P2, Resolved)
**Created:** 2024-09-19 via Slack  |  **Requester:** Arjun Pillai  |  **Assigned to:** Sahil Menon

**Description:** Arjun Pillai (IT Support / Information Technology) reported an issue via Slack related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00151 — UAT (P3, Closed)
**Created:** 2024-09-19 via Live Chat  |  **Requester:** Varun Rao  |  **Assigned to:** Vikram Malhotra

**Description:** Varun Rao (Management / Leadership) reported an issue via Live Chat related to 'User Acceptance Testing (UAT) Coordination'. Category: UAT. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'User Acceptance Testing (UAT) Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-QA-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including business scenarios and sign-off criteria agreed with stakeholders. The review team examines the UAT Cycle against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Product Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-007

---

## TCK3-QA-00060 — Reporting (P3, Resolved)
**Created:** 2024-10-15 via Phone  |  **Requester:** Rohan Singh  |  **Assigned to:** Varun Menon

**Description:** Rohan Singh (Sales) reported an issue via Phone related to 'QA Metrics Reporting Procedure'. Category: Reporting. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Metrics Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-QA-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including defect leakage rate, test coverage %, and automation pass rate. The review team examines the QA Metrics Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-016

---

## TCK3-QA-00085 — Security Testing (P4, Resolved)
**Created:** 2024-10-17 via Walk-in  |  **Requester:** Shreya Joshi  |  **Assigned to:** Swati Sharma

**Description:** Shreya Joshi (Legal & Compliance) reported an issue via Walk-in related to 'Security Regression Testing Coordination'. Category: Security Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Security Regression Testing Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-QA-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release. The review team examines the Security Test Pass against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Analyst discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-013

---

## TCK3-QA-00105 — Test Execution (P3, Resolved)
**Created:** 2024-10-18 via Phone  |  **Requester:** Harsh Gupta  |  **Assigned to:** Vikram Malhotra

**Description:** Harsh Gupta (Research & Development) reported an issue via Phone related to 'Mobile App Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Mobile App Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-010 to resolve. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-010

---
