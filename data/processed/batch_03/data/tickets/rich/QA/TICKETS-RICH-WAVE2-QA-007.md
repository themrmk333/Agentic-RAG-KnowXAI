# QA / Testing — Rich Historical Ticket Archive (wave2, Page 7)

## TCK3-QA-00093 — Test Execution (P4, Resolved)
**Created:** 2026-07-05 via Email  |  **Requester:** Harsh Joshi  |  **Assigned to:** Preeti Menon

**Description:** Harsh Joshi (Marketing) reported an issue via Email related to 'Exploratory Testing Session Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Exploratory Testing Session Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-015 to resolve. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-015

---

## TCK3-QA-00083 — Onboarding (P4, Closed)
**Created:** 2026-07-14 via Portal  |  **Requester:** Anjali Joshi  |  **Assigned to:** Harsh Chauhan

**Description:** Anjali Joshi (Management / Leadership) reported an issue via Portal related to 'QA Onboarding Procedure'. Category: Onboarding. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-QA-012 to resolve. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The QA Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-QA-012

---

## TCK3-QA-00150 — Environment Management (P2, Resolved)
**Created:** 2026-07-17 via Email  |  **Requester:** Divya Menon  |  **Assigned to:** Varun Menon

**Description:** Divya Menon (QA / Testing) reported an issue via Email related to 'Test Environment Setup Request'. Category: Environment Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Environment Setup Request', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-008 to resolve. the QA Engineer confirms eligibility and prerequisites: the required data set, build version, and configuration. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Environment is required. The DevOps Engineer reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Test Environment in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-008

---

## TCK3-QA-00031 — Test Execution (P3, Resolved)
**Created:** 2026-07-30 via Walk-in  |  **Requester:** Nidhi Mehta  |  **Assigned to:** Manoj Nair

**Description:** Nidhi Mehta (Administration / Facilities) reported an issue via Walk-in related to 'Regression Test Cycle Execution'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Regression Test Cycle Execution', and checked recent related changes before identifying the cause below.

**Root Cause:** A naming convention mismatch caused the new resource to not link correctly to the parent request.

**Resolution:** Followed SOP-QA-003 to resolve. the QA Engineer confirms eligibility and prerequisites: selecting the regression suite relevant to the changed modules. the QA Engineer raises a request in MK-TestHub specifying exactly which Regression Cycle is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Regression Cycle in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-003

---

## TCK3-QA-00047 — Test Execution (P2, Closed)
**Created:** 2026-08-03 via Live Chat  |  **Requester:** Vivek Sharma  |  **Assigned to:** Divya Gupta

**Description:** Vivek Sharma (DevOps & Cloud) reported an issue via Live Chat related to 'Mobile App Testing Procedure'. Category: Test Execution. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Mobile App Testing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The provisioning request was correctly approved but the automated fulfillment step failed silently.

**Resolution:** Followed SOP-QA-010 to resolve. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-010

---

## TCK3-QA-00039 — Test Planning (P3, Resolved)
**Created:** 2026-08-04 via Slack  |  **Requester:** Dev Sharma  |  **Assigned to:** Divya Gupta

**Description:** Dev Sharma (Product Management) reported an issue via Slack related to 'Test Case Design and Review'. Category: Test Planning. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Test Case Design and Review', and checked recent related changes before identifying the cause below.

**Root Cause:** Two systems that should show the same figure were pulling from data as of different points in time.

**Resolution:** Followed SOP-QA-002 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Engineer gathers the required data and documents, including requirement traceability and edge-case coverage. The review team examines the Test Case Suite against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The QA Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-002

---

## TCK3-QA-00069 — Performance Testing (P3, Resolved)
**Created:** 2026-08-09 via Walk-in  |  **Requester:** Aditya Nair  |  **Assigned to:** Harsh Chauhan

**Description:** Aditya Nair (Customer Support / Helpdesk) reported an issue via Walk-in related to 'Performance Test Execution'. Category: Performance Testing. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Performance Test Execution', and checked recent related changes before identifying the cause below.

**Root Cause:** A permissions template used for provisioning was out of date relative to the current access model.

**Resolution:** Followed SOP-QA-006 to resolve. the QA Engineer confirms eligibility and prerequisites: defining load profile, target throughput, and acceptable latency thresholds. the QA Engineer raises a request in MK-TestHub specifying exactly which Performance Test is required. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Performance Test in the relevant system. the QA Engineer is notified and asked to test and verify the access or functionality.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-QA-006

---

## TCK3-QA-00077 — Onboarding (P4, Closed)
**Created:** 2026-08-10 via Walk-in  |  **Requester:** Preeti Desai  |  **Assigned to:** Manoj Nair

**Description:** Preeti Desai (Administration / Facilities) reported an issue via Walk-in related to 'QA Onboarding Procedure'. Category: Onboarding. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'QA Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The handover checklist used was an older version missing a step added since.

**Resolution:** Followed SOP-QA-012 to resolve. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The QA Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-QA-012

---

## TCK3-QA-00116 — Defect Management (P3, In Progress)
**Created:** 2026-08-11 via Portal  |  **Requester:** Neel Malhotra  |  **Assigned to:** Sahil Menon

**Description:** Neel Malhotra (Cybersecurity / Information Security) reported an issue via Portal related to 'Software Defect Reporting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Software Defect Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A required approval step was skipped due to a misunderstanding of the delegated authority limits.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-QA-001

---

## TCK3-QA-00098 — Defect Management (P4, Resolved)
**Created:** 2026-08-14 via Portal  |  **Requester:** Divya Bose  |  **Assigned to:** Alisha Menon

**Description:** Divya Bose (QA / Testing) reported an issue via Portal related to 'Software Defect Reporting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Software Defect Reporting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester used an outdated version of the request form that was missing a now-mandatory field.

**Resolution:** Followed SOP-QA-001 to resolve. the QA Engineer logs into MK-TestHub and navigates to the 'Defect Report' section. the QA Engineer selects 'New Defect Report' and enters the required details, including steps to reproduce, expected vs actual result, and severity. the QA Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting. the QA Engineer submits the Defect Report; MK-TestHub automatically routes it to the QA Lead for review. The QA Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-QA-001

---

## TCK3-QA-00030 — Defect Management (P4, Resolved)
**Created:** 2026-08-15 via Live Chat  |  **Requester:** Nidhi Mehta  |  **Assigned to:** Divya Bose

**Description:** Nidhi Mehta (Administration / Facilities) reported an issue via Live Chat related to 'Defect Triage Meeting Procedure'. Category: Defect Management. Logged against MK-TestHub.

**Investigation:** The assigned specialist reviewed the MK-TestHub record, confirmed the reported symptom against 'Defect Triage Meeting Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** A periodic review had not been completed on schedule, allowing the issue to persist undetected.

**Resolution:** Followed SOP-QA-009 to resolve. The review is scheduled in advance and stakeholders are notified through MK-TestHub. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority. The review team examines the Defect Triage against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-QA-009

---
