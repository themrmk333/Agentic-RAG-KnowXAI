# DevOps & Cloud — Frequently Asked Questions (28 total)

## FAQ-DEVOPS-001: How do I complete: Service Deployment Procedure?
**Category:** Deployment | **Difficulty:** Basic | **Access Level:** general | **Roles:** DevOps Engineer, DevOps Manager

**Short Answer:** Follow the 7-step Service Deployment Procedure procedure in MK-CloudOps, starting with the SOP-DEVOPS-001 SOP.

**Detailed Answer:** The Service Deployment Procedure process (SOP-DEVOPS-001) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and DevOps Manager is responsible for approval/sign-off. Production deployments outside business hours require prior sign-off.

**Step-by-step:**
1. the DevOps Engineer confirms eligibility and prerequisites: verifying the build passed all MK-CI pipeline gates.
2. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Deployment is required.
3. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Deployment in the relevant system.
5. the DevOps Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.
7. MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Production deployments outside business hours require prior sign-off.

**Related Documents:** SOP-DEVOPS-001
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-002: How do I complete: CI/CD Pipeline Configuration?
**Category:** CI/CD | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** DevOps Engineer, DevOps Manager

**Short Answer:** Follow the 7-step CI/CD Pipeline Configuration procedure in MK-CloudOps, starting with the SOP-DEVOPS-002 SOP.

**Detailed Answer:** The CI/CD Pipeline Configuration process (SOP-DEVOPS-002) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and DevOps Manager is responsible for approval/sign-off. Pipelines deploying to production must include an automated rollback stage.

**Step-by-step:**
1. the DevOps Engineer confirms eligibility and prerequisites: defining build, test, and deploy stages with required approvals.
2. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which CI/CD Pipeline is required.
3. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the CI/CD Pipeline in the relevant system.
5. the DevOps Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.
7. MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Pipelines deploying to production must include an automated rollback stage.

**Related Documents:** SOP-DEVOPS-002
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-003: How do I complete: Cloud Resource Provisioning Request?
**Category:** Cloud Infrastructure | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** requester, Cloud Architect

**Short Answer:** Follow the 7-step Cloud Resource Provisioning Request procedure in MK-CloudOps, starting with the SOP-DEVOPS-003 SOP.

**Detailed Answer:** The Cloud Resource Provisioning Request process (SOP-DEVOPS-003) is owned by the DevOps & Cloud department. The requester initiates the request in MK-CloudOps and Cloud Architect is responsible for approval/sign-off. Resources exceeding budget thresholds require Finance co-approval.

**Step-by-step:**
1. the requester logs into MK-CloudOps and navigates to the 'Cloud Resource Request' section.
2. the requester selects 'New Cloud Resource Request' and enters the required details, including resource type, sizing, environment, and estimated monthly cost.
3. the requester attaches any supporting documentation and reviews the entry for accuracy before submitting.
4. the requester submits the Cloud Resource Request; MK-CloudOps automatically routes it to the Cloud Architect for review.
5. The Cloud Architect reviews the request against company policy and either approves, rejects, or returns it for clarification.
6. On approval, MK-CloudOps updates the status to 'Approved' and notifies the requester by email/in-app notification.
7. The approved Cloud Resource Request is processed and the record is retained in MK-CloudOps for audit purposes. Resources exceeding budget thresholds require Finance co-approval.

**Related Documents:** SOP-DEVOPS-003
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-004: How do I complete: Production Incident Response (DevOps)?
**Category:** Incident Management | **Difficulty:** Advanced | **Access Level:** general | **Roles:** on-call DevOps Engineer, DevOps Manager

**Short Answer:** Follow the 7-step Production Incident Response (DevOps) procedure in MK-CloudOps, starting with the SOP-DEVOPS-004 SOP.

**Detailed Answer:** The Production Incident Response (DevOps) process (SOP-DEVOPS-004) is owned by the DevOps & Cloud department. The on-call devops engineer initiates the request in MK-CloudOps and DevOps Manager is responsible for approval/sign-off. Sev-1 outages trigger an incident bridge call within 10 minutes.

**Step-by-step:**
1. the on-call DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several.
2. the on-call DevOps Engineer performs the standard first-line check: checking MK-CloudOps monitoring dashboards for alerts and anomalies.
3. If the issue persists, the on-call DevOps Engineer applies the documented workaround for this issue type.
4. the on-call DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.
5. If still unresolved, the on-call DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Infrastructure Incident', attaching screenshots or error logs.
6. The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.
7. the on-call DevOps Engineer confirms the fix works; the ticket is closed in MK-CloudOps with the root cause logged. Sev-1 outages trigger an incident bridge call within 10 minutes.

**Related Documents:** SOP-DEVOPS-004
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-005: How do I complete: Infrastructure as Code (IaC) Change Procedure?
**Category:** Infrastructure | **Difficulty:** Basic | **Access Level:** manager | **Roles:** DevOps Engineer, Cloud Architect

**Short Answer:** Follow the 7-step Infrastructure as Code (IaC) Change Procedure procedure in MK-CloudOps, starting with the SOP-DEVOPS-005 SOP.

**Detailed Answer:** The Infrastructure as Code (IaC) Change Procedure process (SOP-DEVOPS-005) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and Cloud Architect is responsible for approval/sign-off. Changes to production Terraform state require a second engineer to review the plan.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-CloudOps.
2. the DevOps Engineer gathers the required data and documents, including a plan/diff output reviewed before apply.
3. The review team examines the IaC Change against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Cloud Architect discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-CloudOps with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Changes to production Terraform state require a second engineer to review the plan.

**Related Documents:** SOP-DEVOPS-005
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-006: How do I complete: Auto-scaling Configuration Procedure?
**Category:** Cloud Infrastructure | **Difficulty:** Basic | **Access Level:** general | **Roles:** DevOps Engineer, Cloud Architect

**Short Answer:** Follow the 7-step Auto-scaling Configuration Procedure procedure in MK-CloudOps, starting with the SOP-DEVOPS-006 SOP.

**Detailed Answer:** The Auto-scaling Configuration Procedure process (SOP-DEVOPS-006) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and Cloud Architect is responsible for approval/sign-off. Scaling policies are load-tested before being applied to production.

**Step-by-step:**
1. the DevOps Engineer confirms eligibility and prerequisites: target CPU/memory thresholds and min/max instance counts.
2. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Auto-scaling Policy is required.
3. The Cloud Architect reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Auto-scaling Policy in the relevant system.
5. the DevOps Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.
7. MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Scaling policies are load-tested before being applied to production.

**Related Documents:** SOP-DEVOPS-006
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-007: How do I complete: Backup and Disaster Recovery Test?
**Category:** Disaster Recovery | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** Site Reliability Engineer, DevOps Manager

**Short Answer:** Follow the 7-step Backup and Disaster Recovery Test procedure in MK-CloudOps, starting with the SOP-DEVOPS-007 SOP.

**Detailed Answer:** The Backup and Disaster Recovery Test process (SOP-DEVOPS-007) is owned by the DevOps & Cloud department. The site reliability engineer initiates the request in MK-CloudOps and DevOps Manager is responsible for approval/sign-off. DR tests are conducted quarterly and results are reported to Management.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-CloudOps.
2. the Site Reliability Engineer gathers the required data and documents, including restoring a sample backup to a sandbox environment and validating integrity.
3. The review team examines the DR Test against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-CloudOps with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. DR tests are conducted quarterly and results are reported to Management.

**Related Documents:** SOP-DEVOPS-007
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-008: How do I complete: Secrets and Credentials Management?
**Category:** Security | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** DevOps Engineer, Security Manager

**Short Answer:** Follow the 7-step Secrets and Credentials Management procedure in MK-CloudOps, starting with the SOP-DEVOPS-008 SOP.

**Detailed Answer:** The Secrets and Credentials Management process (SOP-DEVOPS-008) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and Security Manager is responsible for approval/sign-off. Secrets are never stored in plaintext configuration files.

**Step-by-step:**
1. the DevOps Engineer confirms eligibility and prerequisites: storing the credential in the approved MK-CloudOps secrets vault only.
2. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Secrets Vault Entry is required.
3. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Secrets Vault Entry in the relevant system.
5. the DevOps Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.
7. MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Secrets are never stored in plaintext configuration files.

**Related Documents:** SOP-DEVOPS-008
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-009: How do I complete: Monitoring and Alerting Setup?
**Category:** Observability | **Difficulty:** Advanced | **Access Level:** general | **Roles:** DevOps Engineer, DevOps Manager

**Short Answer:** Follow the 7-step Monitoring and Alerting Setup procedure in MK-CloudOps, starting with the SOP-DEVOPS-009 SOP.

**Detailed Answer:** The Monitoring and Alerting Setup process (SOP-DEVOPS-009) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and DevOps Manager is responsible for approval/sign-off. Every production service must have at least CPU, memory, and error-rate alerts.

**Step-by-step:**
1. the DevOps Engineer confirms eligibility and prerequisites: defining alert thresholds and the on-call notification channel.
2. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Monitoring Alert is required.
3. The DevOps Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Monitoring Alert in the relevant system.
5. the DevOps Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.
7. MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Every production service must have at least CPU, memory, and error-rate alerts.

**Related Documents:** SOP-DEVOPS-009
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-010: How do I complete: Container Image Build and Publish?
**Category:** Containers | **Difficulty:** Basic | **Access Level:** general | **Roles:** DevOps Engineer, Tech Lead

**Short Answer:** Follow the 7-step Container Image Build and Publish procedure in MK-CloudOps, starting with the SOP-DEVOPS-010 SOP.

**Detailed Answer:** The Container Image Build and Publish process (SOP-DEVOPS-010) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and Tech Lead is responsible for approval/sign-off. Images with critical vulnerabilities are blocked from publishing automatically.

**Step-by-step:**
1. the DevOps Engineer confirms eligibility and prerequisites: scanning the image for vulnerabilities before publishing to the registry.
2. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Container Image is required.
3. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Container Image in the relevant system.
5. the DevOps Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.
7. MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Images with critical vulnerabilities are blocked from publishing automatically.

**Related Documents:** SOP-DEVOPS-010
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-011: How do I complete: Environment Promotion Procedure (Dev → Staging → Prod)?
**Category:** Release Management | **Difficulty:** Basic | **Access Level:** employee | **Roles:** DevOps Engineer, Engineering Manager

**Short Answer:** Follow the 7-step Environment Promotion Procedure (Dev → Staging → Prod) procedure in MK-CloudOps, starting with the SOP-DEVOPS-011 SOP.

**Detailed Answer:** The Environment Promotion Procedure (Dev → Staging → Prod) process (SOP-DEVOPS-011) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and Engineering Manager is responsible for approval/sign-off. Promotions to production require QA sign-off attached to the request.

**Step-by-step:**
1. the DevOps Engineer logs into MK-CloudOps and navigates to the 'Promotion Request' section.
2. the DevOps Engineer selects 'New Promotion Request' and enters the required details, including staging sign-off evidence and change ticket reference.
3. the DevOps Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting.
4. the DevOps Engineer submits the Promotion Request; MK-CloudOps automatically routes it to the Engineering Manager for review.
5. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.
6. On approval, MK-CloudOps updates the status to 'Approved' and notifies the DevOps Engineer by email/in-app notification.
7. The approved Promotion Request is processed and the record is retained in MK-CloudOps for audit purposes. Promotions to production require QA sign-off attached to the request.

**Related Documents:** SOP-DEVOPS-011
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-012: How do I complete: Rollback Procedure?
**Category:** Deployment | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** DevOps Engineer, DevOps Manager

**Short Answer:** Follow the 7-step Rollback Procedure procedure in MK-CloudOps, starting with the SOP-DEVOPS-012 SOP.

**Detailed Answer:** The Rollback Procedure process (SOP-DEVOPS-012) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and DevOps Manager is responsible for approval/sign-off. Rollbacks are performed without waiting for full root cause analysis.

**Step-by-step:**
1. the DevOps Engineer confirms the exact symptom, when it started, and whether it affects one system or several.
2. the DevOps Engineer performs the standard first-line check: identifying the last known good deployment version in MK-CloudOps.
3. If the issue persists, the DevOps Engineer applies the documented workaround for this issue type.
4. the DevOps Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.
5. If still unresolved, the DevOps Engineer raises a ticket in MK-CloudOps categorised under 'Deployment Rollback', attaching screenshots or error logs.
6. The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.
7. the DevOps Engineer confirms the fix works; the ticket is closed in MK-CloudOps with the root cause logged. Rollbacks are performed without waiting for full root cause analysis.

**Related Documents:** SOP-DEVOPS-012
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-013: How do I complete: Cost Optimization Review?
**Category:** Cost Management | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** Cloud Architect, DevOps Director

**Short Answer:** Follow the 7-step Cost Optimization Review procedure in MK-CloudOps, starting with the SOP-DEVOPS-013 SOP.

**Detailed Answer:** The Cost Optimization Review process (SOP-DEVOPS-013) is owned by the DevOps & Cloud department. The cloud architect initiates the request in MK-CloudOps and DevOps Director is responsible for approval/sign-off. Findings are shared with department owners for remediation within 2 weeks.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-CloudOps.
2. the Cloud Architect gathers the required data and documents, including idle resources, oversized instances, and unused storage.
3. The review team examines the Cloud Cost Report against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The DevOps Director discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-CloudOps with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Findings are shared with department owners for remediation within 2 weeks.

**Related Documents:** SOP-DEVOPS-013
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-014: How do I complete: DevOps New Engineer Onboarding?
**Category:** Onboarding | **Difficulty:** Advanced | **Access Level:** employee | **Roles:** DevOps Manager, DevOps Director

**Short Answer:** Follow the 7-step DevOps New Engineer Onboarding procedure in MK-CloudOps, starting with the SOP-DEVOPS-014 SOP.

**Detailed Answer:** The DevOps New Engineer Onboarding process (SOP-DEVOPS-014) is owned by the DevOps & Cloud department. The devops manager initiates the request in MK-CloudOps and DevOps Director is responsible for approval/sign-off. New DevOps engineers do not join the on-call rotation until week 3.

**Step-by-step:**
1. HR notifies the relevant department and the MK-CloudOps owner ahead of the employee's start or end date.
2. the DevOps Manager prepares the required DevOps Onboarding Plan, including cloud console access, IaC repo access, and an on-call shadowing schedule.
3. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding).
4. The DevOps Director verifies that every item on the checklist is complete.
5. The employee, or their manager for offboarding cases, confirms receipt or completion.
6. Any exceptions or missing items are escalated to the DevOps Director for same-day resolution.
7. MK-CloudOps is updated to reflect the completed status and the record is archived. New DevOps engineers do not join the on-call rotation until week 3.

**Related Documents:** SOP-DEVOPS-014
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-015: How do I complete: Patch Management for Infrastructure?
**Category:** Patch Management | **Difficulty:** Basic | **Access Level:** general | **Roles:** DevOps Engineer, Security Manager

**Short Answer:** Follow the 7-step Patch Management for Infrastructure procedure in MK-CloudOps, starting with the SOP-DEVOPS-015 SOP.

**Detailed Answer:** The Patch Management for Infrastructure process (SOP-DEVOPS-015) is owned by the DevOps & Cloud department. The devops engineer initiates the request in MK-CloudOps and Security Manager is responsible for approval/sign-off. Critical security patches are applied within 72 hours of release.

**Step-by-step:**
1. the DevOps Engineer confirms eligibility and prerequisites: testing the patch in staging before production rollout.
2. the DevOps Engineer raises a request in MK-CloudOps specifying exactly which Patch Deployment is required.
3. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Patch Deployment in the relevant system.
5. the DevOps Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CloudOps and corrected before sign-off.
7. MK-CloudOps marks the request 'Complete' and the configuration is logged for audit and future reference. Critical security patches are applied within 72 hours of release.

**Related Documents:** SOP-DEVOPS-015
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-016: How do I complete: On-call Rotation and Handover?
**Category:** Operations | **Difficulty:** Basic | **Access Level:** employee | **Roles:** outgoing on-call Engineer, DevOps Manager

**Short Answer:** Follow the 7-step On-call Rotation and Handover procedure in MK-CloudOps, starting with the SOP-DEVOPS-016 SOP.

**Detailed Answer:** The On-call Rotation and Handover process (SOP-DEVOPS-016) is owned by the DevOps & Cloud department. The outgoing on-call engineer initiates the request in MK-CloudOps and DevOps Manager is responsible for approval/sign-off. Handover must happen via a written note in MK-CloudOps, not verbally only.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-CloudOps.
2. the outgoing on-call Engineer gathers the required data and documents, including open incidents, known issues, and any suppressed alerts.
3. The review team examines the On-call Handover against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The DevOps Manager discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-CloudOps with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Handover must happen via a written note in MK-CloudOps, not verbally only.

**Related Documents:** SOP-DEVOPS-016
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-017: What is the Production Change Policy?
**Category:** Change Management | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** DevOps, Engineering

**Short Answer:** All production deployments must pass through the MK-CI pipeline; manual production changes are prohibited except during a declared incident.

**Detailed Answer:** All production deployments must pass through the MK-CI pipeline; manual production changes are prohibited except during a declared incident. High-risk changes require a peer-reviewed rollback plan before execution. Deployments outside business hours require prior sign-off from the DevOps Manager.

**Related Documents:** POL-DEVOPS-001
**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-018: Who do I contact in the DevOps & Cloud department for help?
**Category:** Department Contacts | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Reach out to: Siddharth Menon (DevOps Manager, siddharth.menon@mkinfinite-ai.com); Isha Bhatt (Cloud Architect, isha.bhatt@mkinfinite-ai.com).

**Detailed Answer:** For general queries to DevOps & Cloud, use MK-CloudOps to log a request so it is tracked; for urgent matters, contact one of the department contacts directly: Siddharth Menon (DevOps Manager, siddharth.menon@mkinfinite-ai.com); Isha Bhatt (Cloud Architect, isha.bhatt@mkinfinite-ai.com).

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-019: What system does the DevOps & Cloud department use?
**Category:** Systems & Tools | **Difficulty:** Advanced | **Access Level:** general | **Roles:** All Employees

**Short Answer:** DevOps & Cloud primarily uses MK-CloudOps for its workflows.

**Detailed Answer:** MK-CloudOps is the system of record for DevOps & Cloud. All requests, approvals, and records for this department's processes should go through MK-CloudOps rather than informal channels, so they are tracked and auditable.

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-020: What are the key performance indicators (KPIs) for the DevOps & Cloud department?
**Category:** KPIs | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Deployment frequency (target: multiple deployments per week per service)

**Detailed Answer:** Deployment frequency (target: multiple deployments per week per service) Change failure rate (target: under 10%) Mean time to recovery (MTTR) (target: under 1 hour for Sev-1) Infrastructure cost variance (target: within 5% of forecast)

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-021: What is the escalation path within the DevOps & Cloud department?
**Category:** Escalation | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Escalate in this order: DevOps Engineer -> DevOps Manager -> DevOps Director.

**Detailed Answer:** If a request or issue with DevOps & Cloud is not addressed within the expected timeframe, escalate step by step through: DevOps Engineer -> DevOps Manager -> DevOps Director. Always reference the original ticket/request ID when escalating.

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-022: What are common mistakes employees make when working with DevOps & Cloud?
**Category:** Best Practices | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Making manual changes directly in production instead of through the IaC pipeline.

**Detailed Answer:** Making manual changes directly in production instead of through the IaC pipeline. Deploying without a tested rollback plan. Not updating monitoring alerts when a new service is introduced.

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-023: What does 'MK-CloudOps' mean in the context of DevOps & Cloud?
**Category:** Terminology | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** The internal cloud infrastructure management and monitoring console.

**Detailed Answer:** The internal cloud infrastructure management and monitoring console. This term is commonly used in DevOps & Cloud SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-024: What does 'IaC' mean in the context of DevOps & Cloud?
**Category:** Terminology | **Difficulty:** Advanced | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Infrastructure as Code, defining infrastructure through version-controlled scripts.

**Detailed Answer:** Infrastructure as Code, defining infrastructure through version-controlled scripts. This term is commonly used in DevOps & Cloud SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-025: What does 'MTTR' mean in the context of DevOps & Cloud?
**Category:** Terminology | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Mean Time To Recovery, the average time to restore service after an incident.

**Detailed Answer:** Mean Time To Recovery, the average time to restore service after an incident. This term is commonly used in DevOps & Cloud SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-026: What does 'Blue-Green Deployment' mean in the context of DevOps & Cloud?
**Category:** Terminology | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** A release strategy running two environments to minimize downtime.

**Detailed Answer:** A release strategy running two environments to minimize downtime. This term is commonly used in DevOps & Cloud SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-027: What does 'On-call' mean in the context of DevOps & Cloud?
**Category:** Terminology | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** A rotating responsibility for responding to production incidents outside business hours.

**Detailed Answer:** A rotating responsibility for responding to production incidents outside business hours. This term is commonly used in DevOps & Cloud SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-DEVOPS-028: Can an employee from a different department ask a DevOps & Cloud question?
**Category:** Cross-Department Access | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Yes. DevOps & Cloud knowledge is retrievable company-wide; only documents marked restricted or management-level require extra authorization.

**Detailed Answer:** MK-Infinite-AI's knowledge base does not gate department knowledge behind the requester's own department. An employee from any department can ask a DevOps & Cloud question (for example, an IT employee asking about the leave policy). Access is instead controlled per-document via the 'access_level' and 'allowed_departments' metadata, so general employee-facing knowledge remains available company-wide while restricted or management-level documents stay protected.

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---
