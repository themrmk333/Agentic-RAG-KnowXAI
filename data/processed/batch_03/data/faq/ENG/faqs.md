# Software Engineering / Development — Frequently Asked Questions (28 total)

## FAQ-ENG-001: How do I complete: Feature Branch Creation and Naming?
**Category:** Version Control | **Difficulty:** Basic | **Access Level:** general | **Roles:** Software Engineer, Tech Lead

**Short Answer:** Follow the 7-step Feature Branch Creation and Naming procedure in MK-CodeForge, starting with the SOP-ENG-001 SOP.

**Detailed Answer:** The Feature Branch Creation and Naming process (SOP-ENG-001) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Tech Lead is responsible for approval/sign-off. Branch names must follow the pattern feature/MK-<ticket-id>-short-description.

**Step-by-step:**
1. the Software Engineer confirms eligibility and prerequisites: the JIRA-equivalent MK-PMTrack ticket ID and a short kebab-case description.
2. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Branch is required.
3. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Feature Branch in the relevant system.
5. the Software Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CodeForge and corrected before sign-off.
7. MK-CodeForge marks the request 'Complete' and the configuration is logged for audit and future reference. Branch names must follow the pattern feature/MK-<ticket-id>-short-description.

**Related Documents:** SOP-ENG-001
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-002: How do I complete: Code Review Process?
**Category:** Code Quality | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** Software Engineer, Tech Lead

**Short Answer:** Follow the 7-step Code Review Process procedure in MK-CodeForge, starting with the SOP-ENG-002 SOP.

**Detailed Answer:** The Code Review Process process (SOP-ENG-002) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Tech Lead is responsible for approval/sign-off. PRs touching shared libraries require two approvals instead of one.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-CodeForge.
2. the Software Engineer gathers the required data and documents, including unit test coverage, linting results, and a clear PR description.
3. The review team examines the Pull Request against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-CodeForge with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. PRs touching shared libraries require two approvals instead of one.

**Related Documents:** SOP-ENG-002
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-003: How do I complete: New Repository Setup?
**Category:** Version Control | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** Software Engineer, Engineering Manager

**Short Answer:** Follow the 7-step New Repository Setup procedure in MK-CodeForge, starting with the SOP-ENG-003 SOP.

**Detailed Answer:** The New Repository Setup process (SOP-ENG-003) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Engineering Manager is responsible for approval/sign-off. All new repositories must enable required status checks before merge.

**Step-by-step:**
1. the Software Engineer confirms eligibility and prerequisites: repository name, visibility, and initial branch protection rules.
2. the Software Engineer raises a request in MK-CodeForge specifying exactly which Repository is required.
3. The Engineering Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Repository in the relevant system.
5. the Software Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CodeForge and corrected before sign-off.
7. MK-CodeForge marks the request 'Complete' and the configuration is logged for audit and future reference. All new repositories must enable required status checks before merge.

**Related Documents:** SOP-ENG-003
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-004: How do I complete: Production Hotfix Deployment?
**Category:** Release Management | **Difficulty:** Advanced | **Access Level:** general | **Roles:** Software Engineer, Engineering Manager

**Short Answer:** Follow the 7-step Production Hotfix Deployment procedure in MK-CodeForge, starting with the SOP-ENG-004 SOP.

**Detailed Answer:** The Production Hotfix Deployment process (SOP-ENG-004) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Engineering Manager is responsible for approval/sign-off. Hotfixes bypass the normal sprint cycle but still require a peer review.

**Step-by-step:**
1. the Software Engineer logs into MK-CodeForge and navigates to the 'Hotfix Request' section.
2. the Software Engineer selects 'New Hotfix Request' and enters the required details, including the incident ID, root cause summary, and rollback plan.
3. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting.
4. the Software Engineer submits the Hotfix Request; MK-CodeForge automatically routes it to the Engineering Manager for review.
5. The Engineering Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.
6. On approval, MK-CodeForge updates the status to 'Approved' and notifies the Software Engineer by email/in-app notification.
7. The approved Hotfix Request is processed and the record is retained in MK-CodeForge for audit purposes. Hotfixes bypass the normal sprint cycle but still require a peer review.

**Related Documents:** SOP-ENG-004
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-005: How do I complete: Local Development Environment Setup?
**Category:** Onboarding | **Difficulty:** Basic | **Access Level:** employee | **Roles:** new Software Engineer, Tech Lead

**Short Answer:** Follow the 7-step Local Development Environment Setup procedure in MK-CodeForge, starting with the SOP-ENG-005 SOP.

**Detailed Answer:** The Local Development Environment Setup process (SOP-ENG-005) is owned by the Software Engineering / Development department. The new software engineer initiates the request in MK-CodeForge and Tech Lead is responsible for approval/sign-off. Environment issues unresolved after 1 day should be escalated to the Tech Lead.

**Step-by-step:**
1. the new Software Engineer confirms eligibility and prerequisites: cloning the onboarding repo and running the setup script documented in MK-CodeForge.
2. the new Software Engineer raises a request in MK-CodeForge specifying exactly which Dev Environment is required.
3. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Dev Environment in the relevant system.
5. the new Software Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CodeForge and corrected before sign-off.
7. MK-CodeForge marks the request 'Complete' and the configuration is logged for audit and future reference. Environment issues unresolved after 1 day should be escalated to the Tech Lead.

**Related Documents:** SOP-ENG-005
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-006: How do I complete: API Key and Secret Rotation?
**Category:** Security | **Difficulty:** Basic | **Access Level:** general | **Roles:** Software Engineer, Security Manager

**Short Answer:** Follow the 7-step API Key and Secret Rotation procedure in MK-CodeForge, starting with the SOP-ENG-006 SOP.

**Detailed Answer:** The API Key and Secret Rotation process (SOP-ENG-006) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Security Manager is responsible for approval/sign-off. Secrets are never committed to MK-CodeForge; violations trigger an automatic Security alert.

**Step-by-step:**
1. the Software Engineer confirms eligibility and prerequisites: identifying every service referencing the current secret.
2. the Software Engineer raises a request in MK-CodeForge specifying exactly which Secret Rotation is required.
3. The Security Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Secret Rotation in the relevant system.
5. the Software Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CodeForge and corrected before sign-off.
7. MK-CodeForge marks the request 'Complete' and the configuration is logged for audit and future reference. Secrets are never committed to MK-CodeForge; violations trigger an automatic Security alert.

**Related Documents:** SOP-ENG-006
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-007: How do I complete: Bug Triage and Assignment?
**Category:** Quality | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** Tech Lead, Engineering Manager

**Short Answer:** Follow the 7-step Bug Triage and Assignment procedure in MK-CodeForge, starting with the SOP-ENG-007 SOP.

**Detailed Answer:** The Bug Triage and Assignment process (SOP-ENG-007) is owned by the Software Engineering / Development department. The tech lead initiates the request in MK-CodeForge and Engineering Manager is responsible for approval/sign-off. Sev-1 bugs are assigned within 1 business hour of triage.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-CodeForge.
2. the Tech Lead gathers the required data and documents, including severity, reproducibility, and affected module for each open bug.
3. The review team examines the Bug Backlog against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-CodeForge with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Sev-1 bugs are assigned within 1 business hour of triage.

**Related Documents:** SOP-ENG-007
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-008: How do I complete: Third-Party Library Approval?
**Category:** Dependency Management | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** Software Engineer, Security Manager

**Short Answer:** Follow the 7-step Third-Party Library Approval procedure in MK-CodeForge, starting with the SOP-ENG-008 SOP.

**Detailed Answer:** The Third-Party Library Approval process (SOP-ENG-008) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Security Manager is responsible for approval/sign-off. GPL-licensed libraries require Legal review before approval.

**Step-by-step:**
1. the Software Engineer logs into MK-CodeForge and navigates to the 'Library Approval Request' section.
2. the Software Engineer selects 'New Library Approval Request' and enters the required details, including the library name, licence type, and known vulnerability scan results.
3. the Software Engineer attaches any supporting documentation and reviews the entry for accuracy before submitting.
4. the Software Engineer submits the Library Approval Request; MK-CodeForge automatically routes it to the Security Manager for review.
5. The Security Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.
6. On approval, MK-CodeForge updates the status to 'Approved' and notifies the Software Engineer by email/in-app notification.
7. The approved Library Approval Request is processed and the record is retained in MK-CodeForge for audit purposes. GPL-licensed libraries require Legal review before approval.

**Related Documents:** SOP-ENG-008
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-009: How do I complete: Sprint Planning Procedure?
**Category:** Agile Process | **Difficulty:** Advanced | **Access Level:** general | **Roles:** Software Engineer, Engineering Manager

**Short Answer:** Follow the 7-step Sprint Planning Procedure procedure in MK-CodeForge, starting with the SOP-ENG-009 SOP.

**Detailed Answer:** The Sprint Planning Procedure process (SOP-ENG-009) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Engineering Manager is responsible for approval/sign-off. Stories without acceptance criteria are not pulled into a sprint.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-CodeForge.
2. the Software Engineer gathers the required data and documents, including story point estimates and dependency mapping for each backlog item.
3. The review team examines the Sprint Backlog against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-CodeForge with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Stories without acceptance criteria are not pulled into a sprint.

**Related Documents:** SOP-ENG-009
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-010: How do I complete: Code Freeze Procedure?
**Category:** Release Management | **Difficulty:** Basic | **Access Level:** employee | **Roles:** Tech Lead, Engineering Manager

**Short Answer:** Follow the 7-step Code Freeze Procedure procedure in MK-CodeForge, starting with the SOP-ENG-010 SOP.

**Detailed Answer:** The Code Freeze Procedure process (SOP-ENG-010) is owned by the Software Engineering / Development department. The tech lead initiates the request in MK-CodeForge and Engineering Manager is responsible for approval/sign-off. Only critical bug fixes are merged after code freeze, with Engineering Manager sign-off.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-CodeForge.
2. the Tech Lead gathers the required data and documents, including listing all open PRs targeting the release branch.
3. The review team examines the Release Branch against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Engineering Manager discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-CodeForge with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Only critical bug fixes are merged after code freeze, with Engineering Manager sign-off.

**Related Documents:** SOP-ENG-010
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-011: How do I complete: Technical Design Document Review?
**Category:** Architecture | **Difficulty:** Basic | **Access Level:** manager | **Roles:** Software Engineer, Tech Lead

**Short Answer:** Follow the 7-step Technical Design Document Review procedure in MK-CodeForge, starting with the SOP-ENG-011 SOP.

**Detailed Answer:** The Technical Design Document Review process (SOP-ENG-011) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Tech Lead is responsible for approval/sign-off. Designs impacting more than one service require a cross-team review meeting.

**Step-by-step:**
1. The review is scheduled in advance and stakeholders are notified through MK-CodeForge.
2. the Software Engineer gathers the required data and documents, including architecture diagrams, data flow, and rollback/monitoring plan.
3. The review team examines the Design Document against the applicable policy or checklist.
4. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned.
5. The Tech Lead discusses the findings with the relevant department and agrees remediation actions.
6. Remediation actions are tracked in MK-CodeForge with due dates and status.
7. The review is closed once all actions are completed, and the outcome is recorded for future audits. Designs impacting more than one service require a cross-team review meeting.

**Related Documents:** SOP-ENG-011
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-012: How do I complete: Engineering Onboarding Procedure?
**Category:** Onboarding | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** Engineering Manager, Tech Lead

**Short Answer:** Follow the 7-step Engineering Onboarding Procedure procedure in MK-CodeForge, starting with the SOP-ENG-012 SOP.

**Detailed Answer:** The Engineering Onboarding Procedure process (SOP-ENG-012) is owned by the Software Engineering / Development department. The engineering manager initiates the request in MK-CodeForge and Tech Lead is responsible for approval/sign-off. New engineers ship their first small PR within the first week wherever possible.

**Step-by-step:**
1. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date.
2. the Engineering Manager prepares the required Engineering Onboarding Plan, including repository access, MK-CodeForge SSH keys, and assigning an onboarding buddy.
3. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding).
4. The Tech Lead verifies that every item on the checklist is complete.
5. The employee, or their manager for offboarding cases, confirms receipt or completion.
6. Any exceptions or missing items are escalated to the Tech Lead for same-day resolution.
7. MK-CodeForge is updated to reflect the completed status and the record is archived. New engineers ship their first small PR within the first week wherever possible.

**Related Documents:** SOP-ENG-012
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-013: How do I complete: Production Incident Response (Engineering)?
**Category:** Incident Management | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** on-call Software Engineer, Engineering Manager

**Short Answer:** Follow the 7-step Production Incident Response (Engineering) procedure in MK-CodeForge, starting with the SOP-ENG-013 SOP.

**Detailed Answer:** The Production Incident Response (Engineering) process (SOP-ENG-013) is owned by the Software Engineering / Development department. The on-call software engineer initiates the request in MK-CodeForge and Engineering Manager is responsible for approval/sign-off. Sev-1 incidents require a written postmortem within 48 hours.

**Step-by-step:**
1. the on-call Software Engineer confirms the exact symptom, when it started, and whether it affects one system or several.
2. the on-call Software Engineer performs the standard first-line check: checking MK-CloudOps dashboards and recent deployments for correlation.
3. If the issue persists, the on-call Software Engineer applies the documented workaround for this issue type.
4. the on-call Software Engineer checks whether the issue is isolated to their own account/device or is affecting other users too.
5. If still unresolved, the on-call Software Engineer raises a ticket in MK-CodeForge categorised under 'Production Incident', attaching screenshots or error logs.
6. The assigned specialist reproduces the issue, diagnoses the root cause, and applies a fix or a temporary workaround.
7. the on-call Software Engineer confirms the fix works; the ticket is closed in MK-CodeForge with the root cause logged. Sev-1 incidents require a written postmortem within 48 hours.

**Related Documents:** SOP-ENG-013
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-014: How do I complete: Database Schema Migration?
**Category:** Data Management | **Difficulty:** Advanced | **Access Level:** employee | **Roles:** Software Engineer, Tech Lead

**Short Answer:** Follow the 7-step Database Schema Migration procedure in MK-CodeForge, starting with the SOP-ENG-014 SOP.

**Detailed Answer:** The Database Schema Migration process (SOP-ENG-014) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Tech Lead is responsible for approval/sign-off. Migrations on production databases require a DevOps engineer present during execution.

**Step-by-step:**
1. the Software Engineer confirms eligibility and prerequisites: a backward-compatible migration script and rollback script.
2. the Software Engineer raises a request in MK-CodeForge specifying exactly which Schema Migration is required.
3. The Tech Lead reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Schema Migration in the relevant system.
5. the Software Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CodeForge and corrected before sign-off.
7. MK-CodeForge marks the request 'Complete' and the configuration is logged for audit and future reference. Migrations on production databases require a DevOps engineer present during execution.

**Related Documents:** SOP-ENG-014
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-015: How do I complete: Feature Flag Rollout Procedure?
**Category:** Release Management | **Difficulty:** Basic | **Access Level:** general | **Roles:** Software Engineer, Product Manager

**Short Answer:** Follow the 7-step Feature Flag Rollout Procedure procedure in MK-CodeForge, starting with the SOP-ENG-015 SOP.

**Detailed Answer:** The Feature Flag Rollout Procedure process (SOP-ENG-015) is owned by the Software Engineering / Development department. The software engineer initiates the request in MK-CodeForge and Product Manager is responsible for approval/sign-off. Flags are removed from the codebase within 60 days of full rollout.

**Step-by-step:**
1. the Software Engineer confirms eligibility and prerequisites: the target user percentage and success metrics to monitor.
2. the Software Engineer raises a request in MK-CodeForge specifying exactly which Feature Flag is required.
3. The Product Manager reviews and approves the request, applying least-privilege / need-basis principles.
4. Once approved, the assigned engineer provisions or configures the Feature Flag in the relevant system.
5. the Software Engineer is notified and asked to test and verify the access or functionality.
6. Any issues found during verification are logged in MK-CodeForge and corrected before sign-off.
7. MK-CodeForge marks the request 'Complete' and the configuration is logged for audit and future reference. Flags are removed from the codebase within 60 days of full rollout.

**Related Documents:** SOP-ENG-015
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-016: How do I complete: Engineering Exit Handover?
**Category:** Offboarding | **Difficulty:** Basic | **Access Level:** employee | **Roles:** departing Software Engineer, Engineering Manager

**Short Answer:** Follow the 7-step Engineering Exit Handover procedure in MK-CodeForge, starting with the SOP-ENG-016 SOP.

**Detailed Answer:** The Engineering Exit Handover process (SOP-ENG-016) is owned by the Software Engineering / Development department. The departing software engineer initiates the request in MK-CodeForge and Engineering Manager is responsible for approval/sign-off. Handover documents are stored in MK-CodeForge wiki for team reference.

**Step-by-step:**
1. HR notifies the relevant department and the MK-CodeForge owner ahead of the employee's start or end date.
2. the departing Software Engineer prepares the required Knowledge Handover, including documenting owned services, open PRs, and pending on-call responsibilities.
3. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding).
4. The Engineering Manager verifies that every item on the checklist is complete.
5. The employee, or their manager for offboarding cases, confirms receipt or completion.
6. Any exceptions or missing items are escalated to the Engineering Manager for same-day resolution.
7. MK-CodeForge is updated to reflect the completed status and the record is archived. Handover documents are stored in MK-CodeForge wiki for team reference.

**Related Documents:** SOP-ENG-016
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-017: What is the Code Review Policy?
**Category:** Code Quality | **Difficulty:** Intermediate | **Access Level:** employee | **Roles:** Engineering

**Short Answer:** No code is merged to the main branch without at least one approving review.

**Detailed Answer:** No code is merged to the main branch without at least one approving review. Changes to shared libraries or authentication code require two approvals. Automated test coverage for new code must not fall below the team's agreed threshold (typically 80%).

**Related Documents:** POL-ENG-001
**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-018: Who do I contact in the Software Engineering / Development department for help?
**Category:** Department Contacts | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Reach out to: Aditya Rao (Engineering Manager, aditya.rao@mkinfinite-ai.com); Neel Kapoor (Tech Lead, neel.kapoor@mkinfinite-ai.com).

**Detailed Answer:** For general queries to Software Engineering / Development, use MK-CodeForge to log a request so it is tracked; for urgent matters, contact one of the department contacts directly: Aditya Rao (Engineering Manager, aditya.rao@mkinfinite-ai.com); Neel Kapoor (Tech Lead, neel.kapoor@mkinfinite-ai.com).

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-019: What system does the Software Engineering / Development department use?
**Category:** Systems & Tools | **Difficulty:** Advanced | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Software Engineering / Development primarily uses MK-CodeForge for its workflows.

**Detailed Answer:** MK-CodeForge is the system of record for Software Engineering / Development. All requests, approvals, and records for this department's processes should go through MK-CodeForge rather than informal channels, so they are tracked and auditable.

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-020: What are the key performance indicators (KPIs) for the Software Engineering / Development department?
**Category:** KPIs | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Sprint velocity consistency (target: within 15% variance across sprints)

**Detailed Answer:** Sprint velocity consistency (target: within 15% variance across sprints) Code review turnaround time (target: under 24 hours) Production incident rate (target: fewer than 2 Sev-1 incidents per quarter) Test coverage on new code (target: above 80%)

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-021: What is the escalation path within the Software Engineering / Development department?
**Category:** Escalation | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Escalate in this order: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director.

**Detailed Answer:** If a request or issue with Software Engineering / Development is not addressed within the expected timeframe, escalate step by step through: Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director. Always reference the original ticket/request ID when escalating.

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-022: What are common mistakes employees make when working with Software Engineering / Development?
**Category:** Best Practices | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Merging a PR without the required second approval on shared libraries.

**Detailed Answer:** Merging a PR without the required second approval on shared libraries. Committing secrets or API keys directly into MK-CodeForge repositories. Skipping the technical design review for changes that impact multiple services.

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-023: What does 'MK-CodeForge' mean in the context of Software Engineering / Development?
**Category:** Terminology | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** The internal Git-based source code hosting and review platform.

**Detailed Answer:** The internal Git-based source code hosting and review platform. This term is commonly used in Software Engineering / Development SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-024: What does 'PR' mean in the context of Software Engineering / Development?
**Category:** Terminology | **Difficulty:** Advanced | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Pull Request, a proposed code change submitted for review before merging.

**Detailed Answer:** Pull Request, a proposed code change submitted for review before merging. This term is commonly used in Software Engineering / Development SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-025: What does 'Tech Debt' mean in the context of Software Engineering / Development?
**Category:** Terminology | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Deferred engineering work accepted for short-term speed, tracked for future remediation.

**Detailed Answer:** Deferred engineering work accepted for short-term speed, tracked for future remediation. This term is commonly used in Software Engineering / Development SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-026: What does 'Hotfix' mean in the context of Software Engineering / Development?
**Category:** Terminology | **Difficulty:** Basic | **Access Level:** general | **Roles:** All Employees

**Short Answer:** An urgent, out-of-cycle production fix.

**Detailed Answer:** An urgent, out-of-cycle production fix. This term is commonly used in Software Engineering / Development SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-027: What does 'Feature Flag' mean in the context of Software Engineering / Development?
**Category:** Terminology | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** A toggle allowing a feature to be enabled/disabled without a new deployment.

**Detailed Answer:** A toggle allowing a feature to be enabled/disabled without a new deployment. This term is commonly used in Software Engineering / Development SOPs, FAQs, and reports at MK-Infinite-AI.

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---

## FAQ-ENG-028: Can an employee from a different department ask a Software Engineering / Development question?
**Category:** Cross-Department Access | **Difficulty:** Intermediate | **Access Level:** general | **Roles:** All Employees

**Short Answer:** Yes. Software Engineering / Development knowledge is retrievable company-wide; only documents marked restricted or management-level require extra authorization.

**Detailed Answer:** MK-Infinite-AI's knowledge base does not gate department knowledge behind the requester's own department. An employee from any department can ask a Software Engineering / Development question (for example, an IT employee asking about the leave policy). Access is instead controlled per-document via the 'access_level' and 'allowed_departments' metadata, so general employee-facing knowledge remains available company-wide while restricted or management-level documents stay protected.

**Escalation Path:** Software Engineer -> Tech Lead -> Engineering Manager -> Engineering Director

---
