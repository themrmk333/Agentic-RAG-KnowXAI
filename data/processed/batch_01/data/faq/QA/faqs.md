# QA / Testing — Frequently Asked Questions (28 total)

## FAQ-QA-001: How do I complete: Software Defect Reporting Procedure?
**Category:** Defect Management | **Difficulty:** Basic | **Access Level:** general | **Roles:** QA Engineer, QA Lead

**Short Answer:** Follow the 7-step Software Defect Reporting Procedure procedure in MK-TestHub, starting with the SOP-QA-001 SOP.

**Detailed Answer:** The Software Defect Reporting Procedure process (SOP-QA-001) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and QA Lead is responsible for approval/sign-off. Sev-1 defects blocking release are reported to the Engineering Manager immediately.

**Step-by-step:**
1. the QA Engineer logs into MK-TestHub and navigates to the 'Defect Report' section.
2. the QA Engineer selects 'New Defect Report' and enters the required details, including steps to reproduce, expected vs actual result, and severity.
3. the QA Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting.
4. the QA Engineer submits the Defect Report; MK-TestHub automatically routes it to the QA Lead for review.
5. The QA Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.
6. On approval, MK-TestHub updates the status to 'Approved' and notifies the QA Engineer by email/in-app notification.
7. The approved Defect Report is processed and the record is retained in MK-TestHub for audit purposes. Sev-1 defects blocking release are reported to the Engineering Manager immediately.

**Related Documents:** SOP-QA-001
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-002: How do I complete: Test Case Design and Review?
**Category:** Test Planning | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** QA Engineer, QA Lead

**Short Answer:** Follow the 7-step Test Case Design and Review procedure in MK-TestHub, starting with the SOP-QA-002 SOP.

**Detailed Answer:** The Test Case Design and Review process (SOP-QA-002) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and QA Lead is responsible for approval/sign-off. Test cases without traceability to a requirement are rejected during review.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-TestHub.
2. the QA Engineer gathers the required data and documents, including requirement traceability and edge-case coverage.
3. The review team examines the Test Case Suite against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The QA Lead discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-TestHub with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Test cases without traceability to a requirement are rejected during review.

**Related Documents:** SOP-QA-002
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-003: How do I complete: Regression Test Cycle Execution?
**Category:** Test Execution | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** QA Engineer, QA Lead

**Short Answer:** Follow the 7-step Regression Test Cycle Execution procedure in MK-TestHub, starting with the SOP-QA-003 SOP.

**Detailed Answer:** The Regression Test Cycle Execution process (SOP-QA-003) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and QA Lead is responsible for approval/sign-off. A failed regression cycle blocks release sign-off until re-tested.

**Step-by-step:**
1. the QA Engineer confirms eligibility and prerequisites: selecting the regression suite relevant to the changed modules.
2. the QA Engineer raises a request in MK-TestHub specifying exactly which Regression Cycle is required.
3. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Regression Cycle in the relevant system.
5. the QA Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-TestHub and corrected before sign-off.
7. MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. A failed regression cycle blocks release sign-off until re-tested.

**Related Documents:** SOP-QA-003
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-004: How do I complete: Test Automation Script Development?
**Category:** Test Automation | **Difficulty:** Advanced | **Access Level:** general | **Roles:** QA Automation Engineer, QA Lead

**Short Answer:** Follow the 7-step Test Automation Script Development procedure in MK-TestHub, starting with the SOP-QA-004 SOP.

**Detailed Answer:** The Test Automation Script Development process (SOP-QA-004) is owned by the QA / Testing department. The qa automation engineer initiates the request in MK-TestHub and QA Lead is responsible for approval/sign-off. Flaky automated tests are quarantined and tracked for a fix within one sprint.

**Step-by-step:**
1. the QA Automation Engineer confirms eligibility and prerequisites: adding the script to the MK-TestHub automation pipeline with tagging.
2. the QA Automation Engineer raises a request in MK-TestHub specifying exactly which Automation Script is required.
3. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Automation Script in the relevant system.
5. the QA Automation Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-TestHub and corrected before sign-off.
7. MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. Flaky automated tests are quarantined and tracked for a fix within one sprint.

**Related Documents:** SOP-QA-004
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-005: How do I complete: Release Sign-off / Go-No-Go Procedure?
**Category:** Release Management | **Difficulty:** Basic | **Access Level:** manager | **Roles:** QA Lead, QA Manager

**Short Answer:** Follow the 7-step Release Sign-off / Go-No-Go Procedure procedure in MK-TestHub, starting with the SOP-QA-005 SOP.

**Detailed Answer:** The Release Sign-off / Go-No-Go Procedure process (SOP-QA-005) is owned by the QA / Testing department. The qa lead initiates the request in MK-TestHub and QA Manager is responsible for approval/sign-off. A single open Sev-1 defect is sufficient to block sign-off.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-TestHub.
2. the QA Lead gathers the required data and documents, including open defect count by severity and outstanding test coverage gaps.
3. The review team examines the Release Readiness Report against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The QA Manager discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-TestHub with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. A single open Sev-1 defect is sufficient to block sign-off.

**Related Documents:** SOP-QA-005
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-006: How do I complete: Performance Test Execution?
**Category:** Performance Testing | **Difficulty:** Basic | **Access Level:** general | **Roles:** QA Engineer, QA Lead

**Short Answer:** Follow the 7-step Performance Test Execution procedure in MK-TestHub, starting with the SOP-QA-006 SOP.

**Detailed Answer:** The Performance Test Execution process (SOP-QA-006) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and QA Lead is responsible for approval/sign-off. Performance regressions of more than 15% are reported to Engineering before release.

**Step-by-step:**
1. the QA Engineer confirms eligibility and prerequisites: defining load profile, target throughput, and acceptable latency thresholds.
2. the QA Engineer raises a request in MK-TestHub specifying exactly which Performance Test is required.
3. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Performance Test in the relevant system.
5. the QA Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-TestHub and corrected before sign-off.
7. MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. Performance regressions of more than 15% are reported to Engineering before release.

**Related Documents:** SOP-QA-006
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-007: How do I complete: User Acceptance Testing (UAT) Coordination?
**Category:** UAT | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** QA Lead, Product Manager

**Short Answer:** Follow the 7-step User Acceptance Testing (UAT) Coordination procedure in MK-TestHub, starting with the SOP-QA-007 SOP.

**Detailed Answer:** The User Acceptance Testing (UAT) Coordination process (SOP-QA-007) is owned by the QA / Testing department. The qa lead initiates the request in MK-TestHub and Product Manager is responsible for approval/sign-off. UAT sign-off must be obtained in writing via MK-PMTrack before go-live.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-TestHub.
2. the QA Lead gathers the required data and documents, including business scenarios and sign-off criteria agreed with stakeholders.
3. The review team examines the UAT Cycle against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Product Manager discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-TestHub with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. UAT sign-off must be obtained in writing via MK-PMTrack before go-live.

**Related Documents:** SOP-QA-007
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-008: How do I complete: Test Environment Setup Request?
**Category:** Environment Management | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** QA Engineer, DevOps Engineer

**Short Answer:** Follow the 7-step Test Environment Setup Request procedure in MK-TestHub, starting with the SOP-QA-008 SOP.

**Detailed Answer:** The Test Environment Setup Request process (SOP-QA-008) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and DevOps Engineer is responsible for approval/sign-off. Test environments are refreshed weekly to avoid data drift.

**Step-by-step:**
1. the QA Engineer confirms eligibility and prerequisites: the required data set, build version, and configuration.
2. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Environment is required.
3. The DevOps Engineer reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Test Environment in the relevant system.
5. the QA Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-TestHub and corrected before sign-off.
7. MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. Test environments are refreshed weekly to avoid data drift.

**Related Documents:** SOP-QA-008
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-009: How do I complete: Defect Triage Meeting Procedure?
**Category:** Defect Management | **Difficulty:** Advanced | **Access Level:** general | **Roles:** QA Lead, Engineering Manager

**Short Answer:** Follow the 7-step Defect Triage Meeting Procedure procedure in MK-TestHub, starting with the SOP-QA-009 SOP.

**Detailed Answer:** The Defect Triage Meeting Procedure process (SOP-QA-009) is owned by the QA / Testing department. The qa lead initiates the request in MK-TestHub and Engineering Manager is responsible for approval/sign-off. Defects unassigned after triage are escalated to the QA Manager.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-TestHub.
2. the QA Lead gathers the required data and documents, including reviewing all newly logged defects and assigning priority.
3. The review team examines the Defect Triage against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-TestHub with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Defects unassigned after triage are escalated to the QA Manager.

**Related Documents:** SOP-QA-009
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-010: How do I complete: Mobile App Testing Procedure?
**Category:** Test Execution | **Difficulty:** Basic | **Access Level:** general | **Roles:** QA Engineer, QA Lead

**Short Answer:** Follow the 7-step Mobile App Testing Procedure procedure in MK-TestHub, starting with the SOP-QA-010 SOP.

**Detailed Answer:** The Mobile App Testing Procedure process (SOP-QA-010) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and QA Lead is responsible for approval/sign-off. Critical device coverage gaps are flagged to QA Manager before sign-off.

**Step-by-step:**
1. the QA Engineer confirms eligibility and prerequisites: the device/OS matrix required for the release.
2. the QA Engineer raises a request in MK-TestHub specifying exactly which Mobile Test Pass is required.
3. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Mobile Test Pass in the relevant system.
5. the QA Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-TestHub and corrected before sign-off.
7. MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. Critical device coverage gaps are flagged to QA Manager before sign-off.

**Related Documents:** SOP-QA-010
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-011: How do I complete: API Testing Procedure?
**Category:** Test Execution | **Difficulty:** Basic | **Access Level:** employee | **Roles:** QA Engineer, QA Lead

**Short Answer:** Follow the 7-step API Testing Procedure procedure in MK-TestHub, starting with the SOP-QA-011 SOP.

**Detailed Answer:** The API Testing Procedure process (SOP-QA-011) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and QA Lead is responsible for approval/sign-off. Breaking API changes without version bump are logged as a defect against Engineering.

**Step-by-step:**
1. the QA Engineer confirms eligibility and prerequisites: validating response schema, status codes, and error handling.
2. the QA Engineer raises a request in MK-TestHub specifying exactly which API Test Suite is required.
3. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the API Test Suite in the relevant system.
5. the QA Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-TestHub and corrected before sign-off.
7. MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. Breaking API changes without version bump are logged as a defect against Engineering.

**Related Documents:** SOP-QA-011
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-012: How do I complete: QA Onboarding Procedure?
**Category:** Onboarding | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** QA Lead, QA Manager

**Short Answer:** Follow the 7-step QA Onboarding Procedure procedure in MK-TestHub, starting with the SOP-QA-012 SOP.

**Detailed Answer:** The QA Onboarding Procedure process (SOP-QA-012) is owned by the QA / Testing department. The qa lead initiates the request in MK-TestHub and QA Manager is responsible for approval/sign-off. New QA hires shadow a full regression cycle in week one.

**Step-by-step:**
1. HR notifies the relevant department and the MK-TestHub owner ahead of the employee's start or end date.
2. the QA Lead prepares the required QA Onboarding Plan, including MK-TestHub access, sample test suite walkthrough, and an onboarding buddy.
3. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding).
4. The QA Manager verifies that every item on the checklist is complete.
5. The employee, or their manager for offboarding cases, confirms receipt or completion.
6. Any exceptions or missing items are escalated to the QA Manager for same-day resolution.
7. MK-TestHub is updated to reflect the completed status and the record is archived. New QA hires shadow a full regression cycle in week one.

**Related Documents:** SOP-QA-012
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-013: How do I complete: Security Regression Testing Coordination?
**Category:** Security Testing | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** QA Engineer, Security Analyst

**Short Answer:** Follow the 7-step Security Regression Testing Coordination procedure in MK-TestHub, starting with the SOP-QA-013 SOP.

**Detailed Answer:** The Security Regression Testing Coordination process (SOP-QA-013) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and Security Analyst is responsible for approval/sign-off. Any new high-severity finding blocks release until remediated.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-TestHub.
2. the QA Engineer gathers the required data and documents, including known vulnerability classes to test (OWASP Top 10) for this release.
3. The review team examines the Security Test Pass against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Security Analyst discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-TestHub with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Any new high-severity finding blocks release until remediated.

**Related Documents:** SOP-QA-013
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-014: How do I complete: Test Data Management Procedure?
**Category:** Test Data | **Difficulty:** Advanced | **Access Level:** employee | **Roles:** QA Engineer, QA Lead

**Short Answer:** Follow the 7-step Test Data Management Procedure procedure in MK-TestHub, starting with the SOP-QA-014 SOP.

**Detailed Answer:** The Test Data Management Procedure process (SOP-QA-014) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and QA Lead is responsible for approval/sign-off. Real customer data is never used in test environments.

**Step-by-step:**
1. the QA Engineer confirms eligibility and prerequisites: masking any production-like sensitive fields before use.
2. the QA Engineer raises a request in MK-TestHub specifying exactly which Test Data Set is required.
3. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Test Data Set in the relevant system.
5. the QA Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-TestHub and corrected before sign-off.
7. MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. Real customer data is never used in test environments.

**Related Documents:** SOP-QA-014
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-015: How do I complete: Exploratory Testing Session Procedure?
**Category:** Test Execution | **Difficulty:** Basic | **Access Level:** general | **Roles:** QA Engineer, QA Lead

**Short Answer:** Follow the 7-step Exploratory Testing Session Procedure procedure in MK-TestHub, starting with the SOP-QA-015 SOP.

**Detailed Answer:** The Exploratory Testing Session Procedure process (SOP-QA-015) is owned by the QA / Testing department. The qa engineer initiates the request in MK-TestHub and QA Lead is responsible for approval/sign-off. Findings from exploratory sessions are logged as defects or improvement notes.

**Step-by-step:**
1. the QA Engineer confirms eligibility and prerequisites: defining a time-boxed charter with a testing focus area.
2. the QA Engineer raises a request in MK-TestHub specifying exactly which Exploratory Test Charter is required.
3. The QA Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Exploratory Test Charter in the relevant system.
5. the QA Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-TestHub and corrected before sign-off.
7. MK-TestHub marks the request 'Complete' and the configuration is logged for audit and future reference. Findings from exploratory sessions are logged as defects or improvement notes.

**Related Documents:** SOP-QA-015
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-016: How do I complete: QA Metrics Reporting Procedure?
**Category:** Reporting | **Difficulty:** Basic | **Access Level:** employee | **Roles:** QA Lead, QA Manager

**Short Answer:** Follow the 7-step QA Metrics Reporting Procedure procedure in MK-TestHub, starting with the SOP-QA-016 SOP.

**Detailed Answer:** The QA Metrics Reporting Procedure process (SOP-QA-016) is owned by the QA / Testing department. The qa lead initiates the request in MK-TestHub and QA Manager is responsible for approval/sign-off. Metrics trending negative for two cycles trigger a QA process review.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-TestHub.
2. the QA Lead gathers the required data and documents, including defect leakage rate, test coverage %, and automation pass rate.
3. The review team examines the QA Metrics Report against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The QA Manager discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-TestHub with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Metrics trending negative for two cycles trigger a QA process review.

**Related Documents:** SOP-QA-016
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-017: What is the Release Sign-off Policy?
**Category:** Release Management | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** QA, Engineering

**Short Answer:** No release proceeds to production with an open Sev-1 defect.

**Detailed Answer:** No release proceeds to production with an open Sev-1 defect. Regression suites must pass at 100% before sign-off; failing tests must be triaged, not skipped. QA sign-off is documented in MK-TestHub and referenced in the release notes.

**Related Documents:** POL-QA-001
**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-018: Who do I contact in the QA / Testing department for help?
**Category:** Department Contacts | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Reach out to: Kavya Iyer (QA Manager, kavya.iyer@mkinfinite-ai.com); Varun Singh (QA Lead, varun.singh@mkinfinite-ai.com).

**Detailed Answer:** For general queries to QA / Testing, use MK-TestHub to log a request so it is tracked; for urgent matters, contact one of the department contacts directly: Kavya Iyer (QA Manager, kavya.iyer@mkinfinite-ai.com); Varun Singh (QA Lead, varun.singh@mkinfinite-ai.com).

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-019: What system does the QA / Testing department use?
**Category:** Systems & Tools | **Difficulty:** Advanced | **Access Level:** general | **Roles:** All Employees

**Short Answer:** QA / Testing primarily uses MK-TestHub for its workflows.

**Detailed Answer:** MK-TestHub is the system of record for QA / Testing. All requests, approvals, and records for this department's processes should go through MK-TestHub rather than informal channels, so they are tracked and auditable.

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-020: What are the key performance indicators (KPIs) for the QA / Testing department?
**Category:** KPIs | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Defect leakage rate to production (target: under 3%)

**Detailed Answer:** Defect leakage rate to production (target: under 3%) Test automation coverage (target: above 60% of regression suite) Average defect turnaround time (target: under 3 days for Sev-2) Release sign-off on-time rate (target: above 95%)

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-021: What is the escalation path within the QA / Testing department?
**Category:** Escalation | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Escalate in this order: QA Engineer -> QA Lead -> QA Manager -> QA Director.

**Detailed Answer:** If a request or issue with QA / Testing is not addressed within the expected timeframe, escalate step by step through: QA Engineer -> QA Lead -> QA Manager -> QA Director. Always reference the original ticket/request ID when escalating.

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-022: What are common mistakes employees make when working with QA / Testing?
**Category:** Best Practices | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Logging defects without clear reproduction steps, causing rework during triage.

**Detailed Answer:** Logging defects without clear reproduction steps, causing rework during triage. Skipping regression testing on 'small' changes that later cause production issues. Not tagging defect severity accurately, causing Sev-1 issues to be missed in triage.

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-023: What does 'MK-TestHub' mean in the context of QA / Testing?
**Category:** Terminology | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** The internal test case management and automation platform.

**Detailed Answer:** The internal test case management and automation platform. This term is commonly used in QA / Testing SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-024: What does 'Regression Suite' mean in the context of QA / Testing?
**Category:** Terminology | **Difficulty:** Advanced | **Access Level:** general | **Roles:** All Employees

**Short Answer:** The set of test cases re-run to confirm existing functionality still works.

**Detailed Answer:** The set of test cases re-run to confirm existing functionality still works. This term is commonly used in QA / Testing SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-025: What does 'UAT' mean in the context of QA / Testing?
**Category:** Terminology | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** User Acceptance Testing performed by business stakeholders before go-live.

**Detailed Answer:** User Acceptance Testing performed by business stakeholders before go-live. This term is commonly used in QA / Testing SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-026: What does 'Sev-1/2/3' mean in the context of QA / Testing?
**Category:** Terminology | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Defect severity levels indicating business impact.

**Detailed Answer:** Defect severity levels indicating business impact. This term is commonly used in QA / Testing SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-027: What does 'Flaky Test' mean in the context of QA / Testing?
**Category:** Terminology | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** An automated test that passes/fails inconsistently without code changes.

**Detailed Answer:** An automated test that passes/fails inconsistently without code changes. This term is commonly used in QA / Testing SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-QA-028: Can an employee from a different department ask a QA / Testing question?
**Category:** Cross-Department Access | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Yes. QA / Testing knowledge is retrievable company-wide; only documents marked restricted or management-level require extra authorization.

**Detailed Answer:** MK-Infinite-AI's knowledge base does not gate department knowledge behind the requester's own department. An employee from any department can ask a QA / Testing question (for example, an IT employee asking about the leave policy). Access is instead controlled per-document via the 'access_level' and 'allowed_departments' metadata, so general employee-facing knowledge remains available company-wide while restricted or management-level documents stay protected.

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---
