# QA / Testing — Rich Historical Ticket Archive (wave2, Page 5)

## TCK3-QA-00059 — Reporting (P4, Resolved)
**Created:** 2025-10-28 via Live Chat  |  **Requester:** Sahil Sharma  |  **Assigned to:** Vikram Malhotra

**Description:** Sahil Sharma (Sales) reported an issue via Live Chat related to 'QA Metrics Reporting Procedure'. Category: Reporting. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Metrics Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-QA-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including defect leakage rate, test coverage %, and automation pass rate. The review team examines the QA Metrics Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-016

---

## TCK3-QA-00022 — Defect Management (P3, Resolved)
**Created:** 2025-11-04 via Walk-in  |  **Requester:** Ritika Desai  |  **Assigned to:** Alisha Verma

**Description:** Ritika Desai (Marketing) reported an issue via Walk-in related to 'Software Defect Reporting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Software Defect Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-QA-001 to resolve. the QA Engineer logs into MK-TestHub and navigates to the 'Defect Report' section. the QA Engineer selects 'New Defect Report' and enters the required details, including steps to reproduce, expected vs actual result, and severity. the QA Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the QA Engineer submits the Defect Report; MK-TestHub automatically routes it to the QA Lead for review. The QA Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-QA-001

---

## TCK3-QA-00100 — Reporting (P2, Closed)
**Created:** 2025-11-06 via Portal  |  **Requester:** Alisha Bhatt  |  **Assigned to:** Rahul Desai

**Description:** Alisha Bhatt (Management / Leadership) reported an issue via Portal related to 'QA Metrics Reporting Procedure'. Category: Reporting. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Metrics Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-QA-016 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including defect leakage rate, test coverage %, and automation pass rate. The review team examines the QA Metrics Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-016

---

## TCK3-QA-00050 — Test Execution (P3, Resolved)
**Created:** 2025-11-07 via Slack  |  **Requester:** Shreya Joshi  |  **Assigned to:** Kabir Reddy

**Description:** Shreya Joshi (Legal & Compliance) reported an issue via Slack related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00066 — Test Data (P2, In Progress)
**Created:** 2025-11-16 via Walk-in  |  **Requester:** Neel Joshi  |  **Assigned to:** Rahul Desai

**Description:** Neel Joshi (DevOps & Cloud) reported an issue via Walk-in related to 'Test Data Management Procedure'. Category: Test Data. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Data Management Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-014

---

## TCK3-QA-00134 — Security Testing (P4, Resolved)
**Created:** 2025-11-22 via Live Chat  |  **Requester:** Siddharth Singh  |  **Assigned to:** Divya Bose

**Description:** Siddharth Singh (Product Management) reported an issue via Live Chat related to 'Security Regression Testing Coordination'. Category: Security Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Security Regression Testing Coordination', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-QA-013 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release. The review team examines the Security Test Pass against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Security Analyst discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-013

---

## TCK3-QA-00067 — Release Management (P3, Resolved)
**Created:** 2025-11-23 via Portal  |  **Requester:** Divya Joshi  |  **Assigned to:** Rahul Desai

**Description:** Divya Joshi (Finance & Accounting) reported an issue via Portal related to 'Release Sign-off / Go-No-Go Procedure'. Category: Release Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Release Sign-off / Go-No-Go Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-QA-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including open defect count by severity and outstanding test coverage gaps. The review team examines the Release Readiness Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-005

---

## TCK3-QA-00144 — Onboarding (P4, Resolved)
**Created:** 2025-11-26 via Portal  |  **Requester:** Sneha Singh  |  **Assigned to:** Divya Menon

**Description:** Sneha Singh (Procurement / Purchasing) reported an issue via Portal related to 'QA Onboarding Procedure'. Category: Onboarding. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-QA-012 to resolve. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The QA Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-QA-012

---

## TCK3-QA-00089 — Onboarding (P3, Resolved)
**Created:** 2025-12-07 via Walk-in  |  **Requester:** Ananya Gupta  |  **Assigned to:** Swati Sharma

**Description:** Ananya Gupta (Product Management) reported an issue via Walk-in related to 'QA Onboarding Procedure'. Category: Onboarding. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-QA-012 to resolve. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The QA Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-QA-012

---

## TCK3-QA-00024 — Test Automation (P3, Resolved)
**Created:** 2025-12-13 via Email  |  **Requester:** Vivek Gupta  |  **Assigned to:** Divya Gupta

**Description:** Vivek Gupta (Sales) reported an issue via Email related to 'Test Automation Script Development'. Category: Test Automation. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Automation Script Development', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-004 to resolve. the QA Automation Engineer confirms eligibility and prerequisites: adding the script to the MK-TestHub automation pipeline with tagging. the QA Automation Engineer raises a request in MK-TestHub specifying exactly which Automation Script is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Automation Script in the relevant system. the QA Automation Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-004

---

## TCK3-QA-00080 — Onboarding (P3, Resolved)
**Created:** 2025-12-24 via Walk-in  |  **Requester:** Aditya Verma  |  **Assigned to:** Divya Bose

**Description:** Aditya Verma (Administration / Facilities) reported an issue via Walk-in related to 'QA Onboarding Procedure'. Category: Onboarding. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A step assumed to be automatic was actually still manual and got missed in a busy period.

**Resolution:** Followed SOP-QA-012 to resolve. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The QA Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-QA-012

---

## TCK3-QA-00091 — Defect Management (P3, Resolved)
**Created:** 2025-12-26 via Email  |  **Requester:** Yash Iyer  |  **Assigned to:** Harsh Chauhan

**Description:** Yash Iyer (Research & Development) reported an issue via Email related to 'Software Defect Reporting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Software Defect Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-QA-001 to resolve. the QA Engineer logs into MK-TestHub and navigates to the 'Defect Report' section. the QA Engineer selects 'New Defect Report' and enters the required details, including steps to reproduce, expected vs actual result, and severity. the QA Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the QA Engineer submits the Defect Report; MK-TestHub automatically routes it to the QA Lead for review. The QA Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-QA-001

---

## TCK3-QA-00052 — Test Execution (P3, Closed)
**Created:** 2026-01-06 via Walk-in  |  **Requester:** Arjun Verma  |  **Assigned to:** Swati Sharma

**Description:** Arjun Verma (Administration / Facilities) reported an issue via Walk-in related to 'Mobile App Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Mobile App Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-010 to resolve. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-010

---

## TCK3-QA-00139 — Test Execution (P1, Resolved)
**Created:** 2026-01-06 via Email  |  **Requester:** Divya Menon  |  **Assigned to:** Divya Bose

**Description:** Divya Menon (Project Management / PMO) reported an issue via Email related to 'API Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'API Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-011 to resolve. the QA Engineer confirms eligibility and prerequisites: validating response schema, status codes, and error handling. the QA Engineer raises a request in MK-TestHub specifying exactly which API Test Suite is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the API Test Suite in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-011

---

## TCK3-QA-00092 — Release Management (P3, Resolved)
**Created:** 2026-01-08 via Live Chat  |  **Requester:** Dev Menon  |  **Assigned to:** Varun Menon

**Description:** Dev Menon (Research & Development) reported an issue via Live Chat related to 'Release Sign-off / Go-No-Go Procedure'. Category: Release Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Release Sign-off / Go-No-Go Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Followed SOP-QA-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including open defect count by severity and outstanding test coverage gaps. The review team examines the Release Readiness Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-005

---

## TCK3-QA-00140 — Onboarding (P3, Resolved)
**Created:** 2026-01-16 via Phone  |  **Requester:** Bhavna Kapoor  |  **Assigned to:** Sneha Reddy

**Description:** Bhavna Kapoor (Project Management / PMO) reported an issue via Phone related to 'QA Onboarding Procedure'. Category: Onboarding. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A dependency (e.g., asset return) was not completed before the dependent step was attempted.

**Resolution:** Followed SOP-QA-012 to resolve. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The QA Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-QA-012

---

## TCK3-QA-00072 — Test Execution (P2, Resolved)
**Created:** 2026-01-20 via Phone  |  **Requester:** Vikram Iyer  |  **Assigned to:** Divya Menon

**Description:** Vikram Iyer (Management / Leadership) reported an issue via Phone related to 'Regression Test Cycle Execution'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Regression Test Cycle Execution', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-QA-003 to resolve. the QA Engineer confirms eligibility and prerequisites: selecting the regression suite relevant to the changed modules. the QA Engineer raises a request in MK-TestHub specifying exactly which Regression Cycle is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Regression Cycle in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-003

---

## TCK3-QA-00127 — Release Management (P3, Closed)
**Created:** 2026-01-22 via Live Chat  |  **Requester:** Kabir Chauhan  |  **Assigned to:** Divya Gupta

**Description:** Kabir Chauhan (Sales) reported an issue via Live Chat related to 'Release Sign-off / Go-No-Go Procedure'. Category: Release Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Release Sign-off / Go-No-Go Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A recent policy change hadn't been fully propagated to every downstream checklist yet.

**Resolution:** Followed SOP-QA-005 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including open defect count by severity and outstanding test coverage gaps. The review team examines the Release Readiness Report against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-005

---

## TCK3-QA-00128 — Test Execution (P3, Resolved)
**Created:** 2026-01-25 via Walk-in  |  **Requester:** Aditya Nair  |  **Assigned to:** Rahul Desai

**Description:** Aditya Nair (Customer Support / Helpdesk) reported an issue via Walk-in related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00073 — Test Execution (P3, Resolved)
**Created:** 2026-01-27 via Live Chat  |  **Requester:** Vivek Singh  |  **Assigned to:** Kabir Reddy

**Description:** Vivek Singh (Procurement / Purchasing) reported an issue via Live Chat related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---
