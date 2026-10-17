# Data & Analytics — Frequently Asked Questions (27 total)

## FAQ-DATA-001: How do I complete: Data Access Request Procedure?
**Category:** Data Access | **Difficulty:** Basic | **Access Level:** general | **Roles:** requester, Data Manager

**Short Answer:** Follow the 7-step Data Access Request Procedure procedure in MK-DataLake, starting with the SOP-DATA-001 SOP.

**Detailed Answer:** The Data Access Request Procedure process (SOP-DATA-001) is owned by the Data & Analytics department. The requester initiates the request in MK-DataLake and Data Manager is responsible for approval/sign-off. Access to Restricted-classified data requires Security Manager co-approval.

**Step-by-step:**
1. the requester logs into MK-DataLake and navigates to the 'Data Access Request' section.
2. the requester selects 'New Data Access Request' and enters the required details, including the specific dataset, business purpose, and required access level.
3. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting.
4. the requester submits the Data Access Request; MK-DataLake automatically routes it to the Data Manager for review.
5. The Data Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.
6. On approval, MK-DataLake updates the status to 'Approved' and notifies the requester by email/in-app notification.
7. The approved Data Access Request is processed and the record is retained in MK-DataLake for audit purposes. Access to Restricted-classified data requires Security Manager co-approval.

**Related Documents:** SOP-DATA-001
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-002: How do I complete: Dashboard/Report Request Procedure?
**Category:** Reporting | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** requester, Analytics Lead

**Short Answer:** Follow the 7-step Dashboard/Report Request Procedure procedure in MK-DataLake, starting with the SOP-DATA-002 SOP.

**Detailed Answer:** The Dashboard/Report Request Procedure process (SOP-DATA-002) is owned by the Data & Analytics department. The requester initiates the request in MK-DataLake and Analytics Lead is responsible for approval/sign-off. Requests requiring new data pipelines are routed to the Data Engineering backlog.

**Step-by-step:**
1. the requester logs into MK-DataLake and navigates to the 'Dashboard Request' section.
2. the requester selects 'New Dashboard Request' and enters the required details, including the business question, required metrics, and refresh frequency.
3. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting.
4. the requester submits the Dashboard Request; MK-DataLake automatically routes it to the Analytics Lead for review.
5. The Analytics Lead reviews the request against company policy and either approves, rejects, or returns it for clarification.
6. On approval, MK-DataLake updates the status to 'Approved' and notifies the requester by email/in-app notification.
7. The approved Dashboard Request is processed and the record is retained in MK-DataLake for audit purposes. Requests requiring new data pipelines are routed to the Data Engineering backlog.

**Related Documents:** SOP-DATA-002
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-003: How do I complete: Data Pipeline Development Procedure?
**Category:** Data Engineering | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** Data Engineer, Data Manager

**Short Answer:** Follow the 7-step Data Pipeline Development Procedure procedure in MK-DataLake, starting with the SOP-DATA-003 SOP.

**Detailed Answer:** The Data Pipeline Development Procedure process (SOP-DATA-003) is owned by the Data & Analytics department. The data engineer initiates the request in MK-DataLake and Data Manager is responsible for approval/sign-off. Pipelines feeding executive dashboards require a peer review before deployment.

**Step-by-step:**
1. the Data Engineer confirms eligibility and prerequisites: source system, transformation logic, and data quality checks.
2. the Data Engineer raises a request in MK-DataLake specifying exactly which Data Pipeline is required.
3. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Data Pipeline in the relevant system.
5. the Data Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-DataLake and corrected before sign-off.
7. MK-DataLake marks the request 'Complete' and the configuration is logged for audit and future reference. Pipelines feeding executive dashboards require a peer review before deployment.

**Related Documents:** SOP-DATA-003
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-004: How do I complete: Data Quality Issue Resolution Procedure?
**Category:** Data Quality | **Difficulty:** Advanced | **Access Level:** general | **Roles:** Data Analyst, Analytics Lead

**Short Answer:** Follow the 7-step Data Quality Issue Resolution Procedure procedure in MK-DataLake, starting with the SOP-DATA-004 SOP.

**Detailed Answer:** The Data Quality Issue Resolution Procedure process (SOP-DATA-004) is owned by the Data & Analytics department. The data analyst initiates the request in MK-DataLake and Analytics Lead is responsible for approval/sign-off. Data quality incidents affecting Finance reporting are flagged to Finance immediately.

**Step-by-step:**
1. the Data Analyst confirms the exact symptom, when it started, and whether it affects one system or several.
2. the Data Analyst performs the standard first-line check: identifying the affected table and the scope of impacted reports.
3. If the issue persists, the Data Analyst applies the documented workaround for this issue type.
4. the Data Analyst checks whether the issue is isolated to their own account/device or is affecting other users too.
5. If still unresolved, the Data Analyst raises a ticket in MK-DataLake categorised under 'Data Quality Incident', attaching screenshots or error logs.
6. The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.
7. the Data Analyst confirms the fix works; the ticket is closed in MK-DataLake with the root cause logged. Data quality incidents affecting Finance reporting are flagged to Finance immediately.

**Related Documents:** SOP-DATA-004
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-005: How do I complete: Data Classification for Analytics Datasets?
**Category:** Data Governance | **Difficulty:** Basic | **Access Level:** employee | **Roles:** Data Analyst, Security Manager

**Short Answer:** Follow the 7-step Data Classification for Analytics Datasets procedure in MK-DataLake, starting with the SOP-DATA-005 SOP.

**Detailed Answer:** The Data Classification for Analytics Datasets process (SOP-DATA-005) is owned by the Data & Analytics department. The data analyst initiates the request in MK-DataLake and Security Manager is responsible for approval/sign-off. Personally identifiable fields are masked in any broadly shared dataset.

**Step-by-step:**
1. the Data Analyst confirms eligibility and prerequisites: applying the correct sensitivity label before granting broader access.
2. the Data Analyst raises a request in MK-DataLake specifying exactly which Dataset Classification is required.
3. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Dataset Classification in the relevant system.
5. the Data Analyst is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-DataLake and corrected before sign-off.
7. MK-DataLake marks the request 'Complete' and the configuration is logged for audit and future reference. Personally identifiable fields are masked in any broadly shared dataset.

**Related Documents:** SOP-DATA-005
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-006: How do I complete: Ad-hoc Data Analysis Request Procedure?
**Category:** Analytics | **Difficulty:** Basic | **Access Level:** general | **Roles:** requester, Data Analyst

**Short Answer:** Follow the 7-step Ad-hoc Data Analysis Request Procedure procedure in MK-DataLake, starting with the SOP-DATA-006 SOP.

**Detailed Answer:** The Ad-hoc Data Analysis Request Procedure process (SOP-DATA-006) is owned by the Data & Analytics department. The requester initiates the request in MK-DataLake and Data Analyst is responsible for approval/sign-off. Requests without a clear business question are sent back for clarification.

**Step-by-step:**
1. the requester logs into MK-DataLake and navigates to the 'Analysis Request' section.
2. the requester selects 'New Analysis Request' and enters the required details, including the business question and desired timeline.
3. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting.
4. the requester submits the Analysis Request; MK-DataLake automatically routes it to the Data Analyst for review.
5. The Data Analyst reviews the request against company policy and either approves, rejects, or returns it for clarification.
6. On approval, MK-DataLake updates the status to 'Approved' and notifies the requester by email/in-app notification.
7. The approved Analysis Request is processed and the record is retained in MK-DataLake for audit purposes. Requests without a clear business question are sent back for clarification.

**Related Documents:** SOP-DATA-006
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-007: How do I complete: Machine Learning Model Deployment Procedure?
**Category:** Machine Learning | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** Data Engineer, Director of Data & Analytics

**Short Answer:** Follow the 7-step Machine Learning Model Deployment Procedure procedure in MK-DataLake, starting with the SOP-DATA-007 SOP.

**Detailed Answer:** The Machine Learning Model Deployment Procedure process (SOP-DATA-007) is owned by the Data & Analytics department. The data engineer initiates the request in MK-DataLake and Director of Data & Analytics is responsible for approval/sign-off. Models impacting customer-facing decisions require a bias/fairness review.

**Step-by-step:**
1. the Data Engineer confirms eligibility and prerequisites: model validation metrics and a monitoring plan for drift.
2. the Data Engineer raises a request in MK-DataLake specifying exactly which ML Model Deployment is required.
3. The Director of Data & Analytics reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the ML Model Deployment in the relevant system.
5. the Data Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-DataLake and corrected before sign-off.
7. MK-DataLake marks the request 'Complete' and the configuration is logged for audit and future reference. Models impacting customer-facing decisions require a bias/fairness review.

**Related Documents:** SOP-DATA-007
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-008: How do I complete: Data Retention and Deletion Procedure?
**Category:** Data Governance | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** Data Manager, Director of Data & Analytics

**Short Answer:** Follow the 7-step Data Retention and Deletion Procedure procedure in MK-DataLake, starting with the SOP-DATA-008 SOP.

**Detailed Answer:** The Data Retention and Deletion Procedure process (SOP-DATA-008) is owned by the Data & Analytics department. The data manager initiates the request in MK-DataLake and Director of Data & Analytics is responsible for approval/sign-off. Deletion of data under legal hold is blocked until the hold is lifted.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-DataLake.
2. the Data Manager gathers the required data and documents, including checking each dataset against the retention schedule defined by Legal.
3. The review team examines the Data Retention Review against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-DataLake with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Deletion of data under legal hold is blocked until the hold is lifted.

**Related Documents:** SOP-DATA-008
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-009: How do I complete: Data Warehouse Schema Change Procedure?
**Category:** Data Engineering | **Difficulty:** Advanced | **Access Level:** general | **Roles:** Data Engineer, Data Manager

**Short Answer:** Follow the 7-step Data Warehouse Schema Change Procedure procedure in MK-DataLake, starting with the SOP-DATA-009 SOP.

**Detailed Answer:** The Data Warehouse Schema Change Procedure process (SOP-DATA-009) is owned by the Data & Analytics department. The data engineer initiates the request in MK-DataLake and Data Manager is responsible for approval/sign-off. Breaking schema changes are communicated to all dashboard owners a week in advance.

**Step-by-step:**
1. the Data Engineer confirms eligibility and prerequisites: impact analysis on downstream dashboards and reports.
2. the Data Engineer raises a request in MK-DataLake specifying exactly which Schema Change is required.
3. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Schema Change in the relevant system.
5. the Data Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-DataLake and corrected before sign-off.
7. MK-DataLake marks the request 'Complete' and the configuration is logged for audit and future reference. Breaking schema changes are communicated to all dashboard owners a week in advance.

**Related Documents:** SOP-DATA-009
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-010: How do I complete: KPI Definition and Governance Procedure?
**Category:** Data Governance | **Difficulty:** Basic | **Access Level:** employee | **Roles:** Analytics Lead, Director of Data & Analytics

**Short Answer:** Follow the 7-step KPI Definition and Governance Procedure procedure in MK-DataLake, starting with the SOP-DATA-010 SOP.

**Detailed Answer:** The KPI Definition and Governance Procedure process (SOP-DATA-010) is owned by the Data & Analytics department. The analytics lead initiates the request in MK-DataLake and Director of Data & Analytics is responsible for approval/sign-off. KPI definitions are version-controlled; changes require a company-wide notice.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-DataLake.
2. the Analytics Lead gathers the required data and documents, including a single agreed formula and data source per KPI to avoid conflicting numbers.
3. The review team examines the KPI Definition against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-DataLake with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. KPI definitions are version-controlled; changes require a company-wide notice.

**Related Documents:** SOP-DATA-010
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-011: How do I complete: Data Onboarding for New Team Members?
**Category:** Onboarding | **Difficulty:** Basic | **Access Level:** employee | **Roles:** Data Manager, Director of Data & Analytics

**Short Answer:** Follow the 7-step Data Onboarding for New Team Members procedure in MK-DataLake, starting with the SOP-DATA-011 SOP.

**Detailed Answer:** The Data Onboarding for New Team Members process (SOP-DATA-011) is owned by the Data & Analytics department. The data manager initiates the request in MK-DataLake and Director of Data & Analytics is responsible for approval/sign-off. New hires complete a data-privacy module before touching production data.

**Step-by-step:**
1. HR notifies the relevant department and the MK-DataLake owner ahead of the employee's start or end date.
2. the Data Manager prepares the required Data Onboarding, including MK-DataLake access, SQL style guide, and a shadowing assignment.
3. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding).
4. The Director of Data & Analytics verifies that every item on the checklist is complete.
5. The employee, or their manager for offboarding cases, confirms receipt or completion.
6. Any exceptions or missing items are escalated to the Director of Data & Analytics for same-day resolution.
7. MK-DataLake is updated to reflect the completed status and the record is archived. New hires complete a data-privacy module before touching production data.

**Related Documents:** SOP-DATA-011
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-012: How do I complete: Executive Reporting Package Preparation?
**Category:** Executive Reporting | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** Analytics Lead, Director of Data & Analytics

**Short Answer:** Follow the 7-step Executive Reporting Package Preparation procedure in MK-DataLake, starting with the SOP-DATA-012 SOP.

**Detailed Answer:** The Executive Reporting Package Preparation process (SOP-DATA-012) is owned by the Data & Analytics department. The analytics lead initiates the request in MK-DataLake and Director of Data & Analytics is responsible for approval/sign-off. Executive reports are reviewed by a second analyst before sending.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-DataLake.
2. the Analytics Lead gathers the required data and documents, including validating figures against source systems before distribution.
3. The review team examines the Executive Report against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Director of Data & Analytics discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-DataLake with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Executive reports are reviewed by a second analyst before sending.

**Related Documents:** SOP-DATA-012
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-013: How do I complete: Data Anonymization for Testing Procedure?
**Category:** Data Privacy | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** Data Engineer, Security Manager

**Short Answer:** Follow the 7-step Data Anonymization for Testing Procedure procedure in MK-DataLake, starting with the SOP-DATA-013 SOP.

**Detailed Answer:** The Data Anonymization for Testing Procedure process (SOP-DATA-013) is owned by the Data & Analytics department. The data engineer initiates the request in MK-DataLake and Security Manager is responsible for approval/sign-off. Anonymized datasets are re-validated quarterly to confirm no re-identification risk.

**Step-by-step:**
1. the Data Engineer confirms eligibility and prerequisites: applying masking rules to all personally identifiable fields.
2. the Data Engineer raises a request in MK-DataLake specifying exactly which Anonymized Test Dataset is required.
3. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Anonymized Test Dataset in the relevant system.
5. the Data Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-DataLake and corrected before sign-off.
7. MK-DataLake marks the request 'Complete' and the configuration is logged for audit and future reference. Anonymized datasets are re-validated quarterly to confirm no re-identification risk.

**Related Documents:** SOP-DATA-013
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-014: How do I complete: Third-Party Data Sharing Request?
**Category:** Data Sharing | **Difficulty:** Advanced | **Access Level:** employee | **Roles:** requester, Legal Manager

**Short Answer:** Follow the 7-step Third-Party Data Sharing Request procedure in MK-DataLake, starting with the SOP-DATA-014 SOP.

**Detailed Answer:** The Third-Party Data Sharing Request process (SOP-DATA-014) is owned by the Data & Analytics department. The requester initiates the request in MK-DataLake and Legal Manager is responsible for approval/sign-off. Cross-border data sharing requires an additional Legal & Compliance review.

**Step-by-step:**
1. the requester logs into MK-DataLake and navigates to the 'Data Sharing Request' section.
2. the requester selects 'New Data Sharing Request' and enters the required details, including the recipient organisation, purpose, and data fields to be shared.
3. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting.
4. the requester submits the Data Sharing Request; MK-DataLake automatically routes it to the Legal Manager for review.
5. The Legal Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.
6. On approval, MK-DataLake updates the status to 'Approved' and notifies the requester by email/in-app notification.
7. The approved Data Sharing Request is processed and the record is retained in MK-DataLake for audit purposes. Cross-border data sharing requires an additional Legal & Compliance review.

**Related Documents:** SOP-DATA-014
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-015: How do I complete: Analytics Tool Access Provisioning?
**Category:** Data Access | **Difficulty:** Basic | **Access Level:** general | **Roles:** requester, Data Manager

**Short Answer:** Follow the 7-step Analytics Tool Access Provisioning procedure in MK-DataLake, starting with the SOP-DATA-015 SOP.

**Detailed Answer:** The Analytics Tool Access Provisioning process (SOP-DATA-015) is owned by the Data & Analytics department. The requester initiates the request in MK-DataLake and Data Manager is responsible for approval/sign-off. Write access to production data models is limited to Data Engineers.

**Step-by-step:**
1. the requester confirms eligibility and prerequisites: the specific tool (MK-DataLake, BI dashboards) and role required.
2. the requester raises a request in MK-DataLake specifying exactly which Analytics Tool Access is required.
3. The Data Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Analytics Tool Access in the relevant system.
5. the requester is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-DataLake and corrected before sign-off.
7. MK-DataLake marks the request 'Complete' and the configuration is logged for audit and future reference. Write access to production data models is limited to Data Engineers.

**Related Documents:** SOP-DATA-015
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-016: What is the Data Governance Policy?
**Category:** Data Governance | **Difficulty:** Basic | **Access Level:** employee | **Roles:** All Employees

**Short Answer:** All datasets must be classified (Public, Internal, Confidential, Restricted) before broader access is granted.

**Detailed Answer:** All datasets must be classified (Public, Internal, Confidential, Restricted) before broader access is granted. Personally identifiable fields must be masked in any dataset shared outside the owning team. Data access requests are reviewed within 3 business days.

**Related Documents:** POL-DATA-001
**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-017: Who do I contact in the Data & Analytics department for help?
**Category:** Department Contacts | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Reach out to: Anjali Rao (Director of Data & Analytics, anjali.rao@mkinfinite-ai.com); Aman Nair (Analytics Lead, aman.nair@mkinfinite-ai.com).

**Detailed Answer:** For general queries to Data & Analytics, use MK-DataLake to log a request so it is tracked; for urgent matters, contact one of the department contacts directly: Anjali Rao (Director of Data & Analytics, anjali.rao@mkinfinite-ai.com); Aman Nair (Analytics Lead, aman.nair@mkinfinite-ai.com).

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-018: What system does the Data & Analytics department use?
**Category:** Systems & Tools | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Data & Analytics primarily uses MK-DataLake for its workflows.

**Detailed Answer:** MK-DataLake is the system of record for Data & Analytics. All requests, approvals, and records for this department's processes should go through MK-DataLake rather than informal channels, so they are tracked and auditable.

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-019: What are the key performance indicators (KPIs) for the Data & Analytics department?
**Category:** KPIs | **Difficulty:** Advanced | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Dashboard/report request turnaround (target: under 5 business days)

**Detailed Answer:** Dashboard/report request turnaround (target: under 5 business days) Data pipeline uptime (target: above 99%) Data quality incident rate (target: fewer than 2 per month) Percentage of datasets with current classification labels (target: 100%)

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-020: What is the escalation path within the Data & Analytics department?
**Category:** Escalation | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Escalate in this order: Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics.

**Detailed Answer:** If a request or issue with Data & Analytics is not addressed within the expected timeframe, escalate step by step through: Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics. Always reference the original ticket/request ID when escalating.

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-021: What are common mistakes employees make when working with Data & Analytics?
**Category:** Best Practices | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Sharing raw datasets containing PII without masking.

**Detailed Answer:** Sharing raw datasets containing PII without masking. Building dashboards on ungoverned KPI definitions, creating conflicting numbers. Deploying pipeline changes without validating downstream report impact.

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-022: What does 'MK-DataLake' mean in the context of Data & Analytics?
**Category:** Terminology | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** The internal data warehouse and analytics platform.

**Detailed Answer:** The internal data warehouse and analytics platform. This term is commonly used in Data & Analytics SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-023: What does 'ETL/ELT' mean in the context of Data & Analytics?
**Category:** Terminology | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Processes that Extract, Transform/Load data between systems.

**Detailed Answer:** Processes that Extract, Transform/Load data between systems. This term is commonly used in Data & Analytics SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-024: What does 'PII' mean in the context of Data & Analytics?
**Category:** Terminology | **Difficulty:** Advanced | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Personally Identifiable Information requiring special handling.

**Detailed Answer:** Personally Identifiable Information requiring special handling. This term is commonly used in Data & Analytics SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-025: What does 'Data Drift' mean in the context of Data & Analytics?
**Category:** Terminology | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** A change in the statistical properties of data affecting model/report accuracy.

**Detailed Answer:** A change in the statistical properties of data affecting model/report accuracy. This term is commonly used in Data & Analytics SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-026: What does 'KPI Governance' mean in the context of Data & Analytics?
**Category:** Terminology | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** The practice of maintaining a single agreed definition per business metric.

**Detailed Answer:** The practice of maintaining a single agreed definition per business metric. This term is commonly used in Data & Analytics SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-DATA-027: Can an employee from a different department ask a Data & Analytics question?
**Category:** Cross-Department Access | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Yes. Data & Analytics knowledge is retrievable company-wide; only documents marked restricted or management-level require extra authorization.

**Detailed Answer:** MK-Infinite-AI's knowledge base does not gate department knowledge behind the requester's own department. An employee from any department can ask a Data & Analytics question (for example, an IT employee asking about the leave policy). Access is instead controlled per-document via the 'access_level' and 'allowed_departments' metadata, so general employee-facing knowledge remains available company-wide while restricted or management-level documents stay protected.

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---
