# QA / Testing — Rich Historical Ticket Archive (wave2, Page 6)

## TCK3-QA-00046 — Environment Management (P3, Resolved)
**Created:** 2026-02-03 via Slack  |  **Requester:** Varun Nair  |  **Assigned to:** Divya Bose

**Description:** Varun Nair (IT Support / Information Technology) reported an issue via Slack related to 'Test Environment Setup Request'. Category: Environment Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Environment Setup Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-008 to resolve. the QA Engineer confirms eligibility and prerequisites: the required data set, build version, and configuration. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Environment is required. The DevOps Engineer reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Test Environment in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-008

---

## TCK3-QA-00034 — Test Execution (P2, Resolved)
**Created:** 2026-02-09 via Live Chat  |  **Requester:** Siddharth Rao  |  **Assigned to:** Varun Menon

**Description:** Siddharth Rao (Finance & Accounting) reported an issue via Live Chat related to 'API Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'API Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-011 to resolve. the QA Engineer confirms eligibility and prerequisites: validating response schema, status codes, and error handling. the QA Engineer raises a request in MK-TestHub specifying exactly which API Test Suite is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the API Test Suite in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-011

---

## TCK3-QA-00088 — Defect Management (P3, Resolved)
**Created:** 2026-02-14 via Phone  |  **Requester:** Yash Iyer  |  **Assigned to:** Divya Bose

**Description:** Yash Iyer (Research & Development) reported an issue via Phone related to 'Software Defect Reporting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Software Defect Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The request was submitted against the wrong category, causing it to route to the wrong approver.

**Resolution:** Followed SOP-QA-001 to resolve. the QA Engineer logs into MK-TestHub and navigates to the 'Defect Report' section. the QA Engineer selects 'New Defect Report' and enters the required details, including steps to reproduce, expected vs actual result, and severity. the QA Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the QA Engineer submits the Defect Report; MK-TestHub automatically routes it to the QA Lead for review. The QA Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-QA-001

---

## TCK3-QA-00117 — Security Testing (P3, Resolved)
**Created:** 2026-02-14 via Portal  |  **Requester:** Kavya Kapoor  |  **Assigned to:** Vikram Malhotra

**Description:** Kavya Kapoor (Customer Support / Helpdesk) reported an issue via Portal related to 'Security Regression Testing Coordination'. Category: Security Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Security Regression Testing Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-QA-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release. The review team examines the Security Test Pass against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Analyst discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-013

---

## TCK3-QA-00058 — Security Testing (P4, Closed)
**Created:** 2026-02-20 via Walk-in  |  **Requester:** Riya Chauhan  |  **Assigned to:** Divya Menon

**Description:** Riya Chauhan (DevOps & Cloud) reported an issue via Walk-in related to 'Security Regression Testing Coordination'. Category: Security Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Security Regression Testing Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release. The review team examines the Security Test Pass against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Analyst discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-013

---

## TCK3-QA-00041 — Test Execution (P3, Resolved)
**Created:** 2026-03-02 via Walk-in  |  **Requester:** Simran Malhotra  |  **Assigned to:** Sahil Menon

**Description:** Simran Malhotra (Finance & Accounting) reported an issue via Walk-in related to 'Mobile App Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Mobile App Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-010 to resolve. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-010

---

## TCK3-QA-00084 — Test Execution (P3, Resolved)
**Created:** 2026-03-09 via Slack  |  **Requester:** Nidhi Pillai  |  **Assigned to:** Alisha Verma

**Description:** Nidhi Pillai (Human Resources) reported an issue via Slack related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00057 — Test Data (P3, In Progress)
**Created:** 2026-03-17 via Live Chat  |  **Requester:** Meera Malhotra  |  **Assigned to:** Kabir Reddy

**Description:** Meera Malhotra (Procurement / Purchasing) reported an issue via Live Chat related to 'Test Data Management Procedure'. Category: Test Data. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Data Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-014

---

## TCK3-QA-00149 — Release Management (P4, Resolved)
**Created:** 2026-04-19 via Portal  |  **Requester:** Manoj Chauhan  |  **Assigned to:** Rahul Desai

**Description:** Manoj Chauhan (Administration / Facilities) reported an issue via Portal related to 'Release Sign-off / Go-No-Go Procedure'. Category: Release Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Release Sign-off / Go-No-Go Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-QA-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including open defect count by severity and outstanding test coverage gaps. The review team examines the Release Readiness Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-005

---

## TCK3-QA-00043 — Test Execution (P3, Resolved)
**Created:** 2026-05-04 via Email  |  **Requester:** Nidhi Mehta  |  **Assigned to:** Divya Gupta

**Description:** Nidhi Mehta (Human Resources) reported an issue via Email related to 'Mobile App Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Mobile App Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-010 to resolve. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-010

---

## TCK3-QA-00054 — UAT (P3, Resolved)
**Created:** 2026-05-04 via Phone  |  **Requester:** Dev Chauhan  |  **Assigned to:** Manoj Nair

**Description:** Dev Chauhan (Marketing) reported an issue via Phone related to 'User Acceptance Testing (UAT) Coordination'. Category: UAT. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'User Acceptance Testing (UAT) Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-QA-007 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including business scenarios and sign-off criteria agreed with stakeholders. The review team examines the UAT Cycle against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Product Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-007

---

## TCK3-QA-00148 — Reporting (P4, In Progress)
**Created:** 2026-05-07 via Live Chat  |  **Requester:** Isha Iyer  |  **Assigned to:** Divya Bose

**Description:** Isha Iyer (Product Management) reported an issue via Live Chat related to 'QA Metrics Reporting Procedure'. Category: Reporting. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Metrics Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-016

---

## TCK3-QA-00065 — Security Testing (P2, Resolved)
**Created:** 2026-05-30 via Slack  |  **Requester:** Simran Iyer  |  **Assigned to:** Divya Bose

**Description:** Simran Iyer (Project Management / PMO) reported an issue via Slack related to 'Security Regression Testing Coordination'. Category: Security Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Security Regression Testing Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-QA-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release. The review team examines the Security Test Pass against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Analyst discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-013

---

## TCK3-QA-00103 — Test Execution (P3, Closed)
**Created:** 2026-06-05 via Email  |  **Requester:** Tanya Malhotra  |  **Assigned to:** Divya Gupta

**Description:** Tanya Malhotra (Sales) reported an issue via Email related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00029 — Defect Management (P4, Resolved)
**Created:** 2026-06-09 via Phone  |  **Requester:** Ananya Gupta  |  **Assigned to:** Sneha Reddy

**Description:** Ananya Gupta (IT Support / Information Technology) reported an issue via Phone related to 'Defect Triage Meeting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Defect Triage Meeting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority. The review team examines the Defect Triage against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-009

---

## TCK3-QA-00137 — Defect Management (P2, Resolved)
**Created:** 2026-06-09 via Phone  |  **Requester:** Sahil Chowdhury  |  **Assigned to:** Varun Menon

**Description:** Sahil Chowdhury (Legal & Compliance) reported an issue via Phone related to 'Defect Triage Meeting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Defect Triage Meeting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority. The review team examines the Defect Triage against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-009

---

## TCK3-QA-00086 — Test Execution (P2, In Progress)
**Created:** 2026-06-12 via Portal  |  **Requester:** Kavya Desai  |  **Assigned to:** Rahul Desai

**Description:** Kavya Desai (Customer Support / Helpdesk) reported an issue via Portal related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00132 — Test Data (P3, Resolved)
**Created:** 2026-06-14 via Email  |  **Requester:** Divya Joshi  |  **Assigned to:** Kabir Reddy

**Description:** Divya Joshi (Finance & Accounting) reported an issue via Email related to 'Test Data Management Procedure'. Category: Test Data. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Data Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-014 to resolve. the QA Engineer confirms eligibility and prerequisites: masking any production-like sensitive fields before use. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Data Set is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Test Data Set in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-014

---

## TCK3-QA-00111 — Defect Management (P3, Resolved)
**Created:** 2026-07-01 via Phone  |  **Requester:** Rahul Sharma  |  **Assigned to:** Rahul Desai

**Description:** Rahul Sharma (Finance & Accounting) reported an issue via Phone related to 'Software Defect Reporting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Software Defect Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Followed SOP-QA-001 to resolve. the QA Engineer logs into MK-TestHub and navigates to the 'Defect Report' section. the QA Engineer selects 'New Defect Report' and enters the required details, including steps to reproduce, expected vs actual result, and severity. the QA Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the QA Engineer submits the Defect Report; MK-TestHub automatically routes it to the QA Lead for review. The QA Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-QA-001

---

## TCK3-QA-00070 — Test Data (P3, Closed)
**Created:** 2026-07-04 via Portal  |  **Requester:** Aman Verma  |  **Assigned to:** Kabir Reddy

**Description:** Aman Verma (Human Resources) reported an issue via Portal related to 'Test Data Management Procedure'. Category: Test Data. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Data Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-014 to resolve. the QA Engineer confirms eligibility and prerequisites: masking any production-like sensitive fields before use. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Data Set is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Test Data Set in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-014

---
