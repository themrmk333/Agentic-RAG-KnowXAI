# RAG Evaluation Scenario Set v2 (Extended)

_54 additional labeled cases with richer fields (expected_answer, expected_citations, reasoning_type) extending the original eval_scenarios.json._

## EVAL2-0001 (multi_step_reasoning)
**Q:** Under the Password Policy, what's the first thing I need before I can even start the Password Reset Procedure process?
**Expected department:** IT | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Password Policy's core rule ('Passwords must be a minimum of 12 characters with uppercase, lowercase, number, and symbol.') before Password Reset Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0002 (multi_step_reasoning)
**Q:** Under the Code Review Policy, what's the first thing I need before I can even start the Feature Branch Creation and Naming process?
**Expected department:** ENG | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Code Review Policy's core rule ('No code is merged to the main branch without at least one approving review.') before Feature Branch Creation and Naming can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0003 (multi_step_reasoning)
**Q:** Under the Release Sign-off Policy, what's the first thing I need before I can even start the Software Defect Reporting Procedure process?
**Expected department:** QA | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Release Sign-off Policy's core rule ('No release proceeds to production with an open Sev-1 defect.') before Software Defect Reporting Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0004 (multi_step_reasoning)
**Q:** Under the Production Change Policy, what's the first thing I need before I can even start the Service Deployment Procedure process?
**Expected department:** DEVOPS | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Production Change Policy's core rule ('All production deployments must pass through the MK-CI pipeline; manual production changes are prohibited except during a declared incident.') before Service Deployment Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0005 (multi_step_reasoning)
**Q:** Under the Access Control Policy, what's the first thing I need before I can even start the Phishing Email Reporting Procedure process?
**Expected department:** SEC | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Access Control Policy's core rule ('Access is granted on a least-privilege, need-to-know basis and reviewed quarterly.') before Phishing Email Reporting Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0006 (multi_step_reasoning)
**Q:** Under the Leave Policy, what's the first thing I need before I can even start the Leave Application Procedure process?
**Expected department:** HR | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Leave Policy's core rule ('All full-time employees are entitled to 18 days of Paid Annual Leave (PAL) per calendar year, credited monthly at 1.5 days.') before Leave Application Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0007 (multi_step_reasoning)
**Q:** Under the Expense Reimbursement Policy, what's the first thing I need before I can even start the Expense Reimbursement Procedure process?
**Expected department:** FIN | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Expense Reimbursement Policy's core rule ('Business expenses must be submitted in MK-Finance360 within 30 days of the expense date.') before Expense Reimbursement Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0008 (multi_step_reasoning)
**Q:** Under the Project Change Management Policy, what's the first thing I need before I can even start the Project Creation and Charter Approval Procedure process?
**Expected department:** PMO | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Project Change Management Policy's core rule ('Any change impacting scope, budget, or timeline by more than 10% requires a formal Change Request.') before Project Creation and Charter Approval Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0009 (multi_step_reasoning)
**Q:** Under the Feature Launch Policy, what's the first thing I need before I can even start the Product Requirement Document (PRD) Creation process?
**Expected department:** PROD | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Feature Launch Policy's core rule ('Every feature launch requires a completed Launch Readiness Checklist covering support, docs, and rollout plan.') before Product Requirement Document (PRD) Creation can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0010 (multi_step_reasoning)
**Q:** Under the Discount Authorization Policy, what's the first thing I need before I can even start the New Lead Qualification Procedure process?
**Expected department:** SALES | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Discount Authorization Policy's core rule ('Discounts up to 10% may be approved by the Sales Team Lead.') before New Lead Qualification Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0011 (multi_step_reasoning)
**Q:** Under the Brand and Content Approval Policy, what's the first thing I need before I can even start the Campaign Planning and Approval Procedure process?
**Expected department:** MKT | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Brand and Content Approval Policy's core rule ('All externally published content must follow the current Brand Guidelines document.') before Campaign Planning and Approval Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0012 (multi_step_reasoning)
**Q:** Under the Support SLA Policy, what's the first thing I need before I can even start the Customer Ticket Intake and Categorization process?
**Expected department:** SUPPORT | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Support SLA Policy's core rule ('Sev-1 (system down) tickets: first response within 30 minutes, resolution target 4 hours.') before Customer Ticket Intake and Categorization can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0013 (multi_step_reasoning)
**Q:** Under the Contract Approval Policy, what's the first thing I need before I can even start the Contract Review Request Procedure process?
**Expected department:** LEGAL | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Contract Approval Policy's core rule ('All external contracts must be reviewed by Legal before signature; no employee may sign on the company's behalf without delegated authority.') before Contract Review Request Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0014 (multi_step_reasoning)
**Q:** Under the Vendor Onboarding Policy, what's the first thing I need before I can even start the New Hardware/Equipment Request Procedure process?
**Expected department:** PROC | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Vendor Onboarding Policy's core rule ('New vendors require at least 3 competitive quotes unless a documented sole-source justification is approved.') before New Hardware/Equipment Request Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0015 (multi_step_reasoning)
**Q:** Under the Facility Access Policy, what's the first thing I need before I can even start the New Employee Workspace Setup Procedure process?
**Expected department:** ADMIN | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Facility Access Policy's core rule ('Access cards are personal and must not be shared or lent to other employees or visitors.') before New Employee Workspace Setup Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0016 (multi_step_reasoning)
**Q:** Under the Data Governance Policy, what's the first thing I need before I can even start the Data Access Request Procedure process?
**Expected department:** DATA | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Data Governance Policy's core rule ('All datasets must be classified (Public, Internal, Confidential, Restricted) before broader access is granted.') before Data Access Request Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0017 (multi_step_reasoning)
**Q:** Under the Responsible AI Policy, what's the first thing I need before I can even start the Research Proposal Submission Procedure process?
**Expected department:** RND | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Responsible AI Policy's core rule ('All research involving customer-facing model behaviour requires a documented bias and fairness assessment.') before Research Proposal Submission Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0018 (multi_step_reasoning)
**Q:** Under the Corporate Governance Policy, what's the first thing I need before I can even start the Company Strategy Planning Procedure process?
**Expected department:** MGMT | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** You need to satisfy the Corporate Governance Policy's core rule ('Material business decisions above INR 5,00,00,000 require CEO Office and Board notification.') before Company Strategy Planning Procedure can begin, since the SOP assumes policy compliance as a precondition.

## EVAL2-0019 (policy_versioning)
**Q:** I saw an old note saying the Password Policy used to work differently — which version is correct now?
**Expected department:** IT | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-IT-001) is authoritative; the older rule is documented only in POL-IT-001-HISTORY for context on what changed and when.

## EVAL2-0020 (policy_versioning)
**Q:** I saw an old note saying the Code Review Policy used to work differently — which version is correct now?
**Expected department:** ENG | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-ENG-001) is authoritative; the older rule is documented only in POL-ENG-001-HISTORY for context on what changed and when.

## EVAL2-0021 (policy_versioning)
**Q:** I saw an old note saying the Release Sign-off Policy used to work differently — which version is correct now?
**Expected department:** QA | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-QA-001) is authoritative; the older rule is documented only in POL-QA-001-HISTORY for context on what changed and when.

## EVAL2-0022 (policy_versioning)
**Q:** I saw an old note saying the Production Change Policy used to work differently — which version is correct now?
**Expected department:** DEVOPS | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-DEVOPS-001) is authoritative; the older rule is documented only in POL-DEVOPS-001-HISTORY for context on what changed and when.

## EVAL2-0023 (policy_versioning)
**Q:** I saw an old note saying the Access Control Policy used to work differently — which version is correct now?
**Expected department:** SEC | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-SEC-001) is authoritative; the older rule is documented only in POL-SEC-001-HISTORY for context on what changed and when.

## EVAL2-0024 (policy_versioning)
**Q:** I saw an old note saying the Leave Policy used to work differently — which version is correct now?
**Expected department:** HR | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-HR-001) is authoritative; the older rule is documented only in POL-HR-001-HISTORY for context on what changed and when.

## EVAL2-0025 (policy_versioning)
**Q:** I saw an old note saying the Expense Reimbursement Policy used to work differently — which version is correct now?
**Expected department:** FIN | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-FIN-001) is authoritative; the older rule is documented only in POL-FIN-001-HISTORY for context on what changed and when.

## EVAL2-0026 (policy_versioning)
**Q:** I saw an old note saying the Project Change Management Policy used to work differently — which version is correct now?
**Expected department:** PMO | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-PMO-001) is authoritative; the older rule is documented only in POL-PMO-001-HISTORY for context on what changed and when.

## EVAL2-0027 (policy_versioning)
**Q:** I saw an old note saying the Feature Launch Policy used to work differently — which version is correct now?
**Expected department:** PROD | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-PROD-001) is authoritative; the older rule is documented only in POL-PROD-001-HISTORY for context on what changed and when.

## EVAL2-0028 (policy_versioning)
**Q:** I saw an old note saying the Discount Authorization Policy used to work differently — which version is correct now?
**Expected department:** SALES | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-SALES-001) is authoritative; the older rule is documented only in POL-SALES-001-HISTORY for context on what changed and when.

## EVAL2-0029 (policy_versioning)
**Q:** I saw an old note saying the Brand and Content Approval Policy used to work differently — which version is correct now?
**Expected department:** MKT | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-MKT-001) is authoritative; the older rule is documented only in POL-MKT-001-HISTORY for context on what changed and when.

## EVAL2-0030 (policy_versioning)
**Q:** I saw an old note saying the Support SLA Policy used to work differently — which version is correct now?
**Expected department:** SUPPORT | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-SUPPORT-001) is authoritative; the older rule is documented only in POL-SUPPORT-001-HISTORY for context on what changed and when.

## EVAL2-0031 (policy_versioning)
**Q:** I saw an old note saying the Contract Approval Policy used to work differently — which version is correct now?
**Expected department:** LEGAL | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-LEGAL-001) is authoritative; the older rule is documented only in POL-LEGAL-001-HISTORY for context on what changed and when.

## EVAL2-0032 (policy_versioning)
**Q:** I saw an old note saying the Vendor Onboarding Policy used to work differently — which version is correct now?
**Expected department:** PROC | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-PROC-001) is authoritative; the older rule is documented only in POL-PROC-001-HISTORY for context on what changed and when.

## EVAL2-0033 (policy_versioning)
**Q:** I saw an old note saying the Facility Access Policy used to work differently — which version is correct now?
**Expected department:** ADMIN | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-ADMIN-001) is authoritative; the older rule is documented only in POL-ADMIN-001-HISTORY for context on what changed and when.

## EVAL2-0034 (policy_versioning)
**Q:** I saw an old note saying the Data Governance Policy used to work differently — which version is correct now?
**Expected department:** DATA | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-DATA-001) is authoritative; the older rule is documented only in POL-DATA-001-HISTORY for context on what changed and when.

## EVAL2-0035 (policy_versioning)
**Q:** I saw an old note saying the Responsible AI Policy used to work differently — which version is correct now?
**Expected department:** RND | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-RND-001) is authoritative; the older rule is documented only in POL-RND-001-HISTORY for context on what changed and when.

## EVAL2-0036 (policy_versioning)
**Q:** I saw an old note saying the Corporate Governance Policy used to work differently — which version is correct now?
**Expected department:** MGMT | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** The current version (POL-MGMT-001) is authoritative; the older rule is documented only in POL-MGMT-001-HISTORY for context on what changed and when.

## EVAL2-0037 (restricted_document)
**Q:** As someone in LEGAL, can you show me the full Access Control Policy document?
**Expected department:** SEC | **Difficulty:** Advanced | **Authorization:** denied
**Expected answer:** No — POL-SEC-001 has access_level='restricted', restricted to Security, Manager. A LEGAL employee should be told the document exists but is restricted, and pointed to the owning role (CISO).

## EVAL2-0038 (restricted_document)
**Q:** As someone in DEVOPS, can you show me the full Incident Response Policy document?
**Expected department:** SEC | **Difficulty:** Advanced | **Authorization:** denied
**Expected answer:** No — POL-SEC-003 has access_level='restricted', restricted to Security. A DEVOPS employee should be told the document exists but is restricted, and pointed to the owning role (CISO).

## EVAL2-0039 (restricted_document)
**Q:** As someone in FIN, can you show me the full Data Protection Policy document?
**Expected department:** SEC | **Difficulty:** Advanced | **Authorization:** denied
**Expected answer:** No — POL-SEC-005 has access_level='restricted', restricted to All Employees. A FIN employee should be told the document exists but is restricted, and pointed to the owning role (CISO).

## EVAL2-0040 (restricted_document)
**Q:** As someone in IT, can you show me the full Vendor Payment Policy document?
**Expected department:** FIN | **Difficulty:** Advanced | **Authorization:** denied
**Expected answer:** No — POL-FIN-005 has access_level='restricted', restricted to Finance Manager, Finance Director. A IT employee should be told the document exists but is restricted, and pointed to the owning role (Finance Director).

## EVAL2-0041 (restricted_document)
**Q:** As someone in PROC, can you show me the full Payroll Administration Policy document?
**Expected department:** FIN | **Difficulty:** Advanced | **Authorization:** denied
**Expected answer:** No — POL-FIN-007 has access_level='restricted', restricted to Finance Manager, HR Director. A PROC employee should be told the document exists but is restricted, and pointed to the owning role (Finance Director).

## EVAL2-0042 (restricted_document)
**Q:** As someone in HR, can you show me the full Executive Compensation Policy document?
**Expected department:** FIN | **Difficulty:** Advanced | **Authorization:** denied
**Expected answer:** No — POL-FIN-008 has access_level='management', restricted to CEO Office, HR Director, Finance Director. A HR employee should be told the document exists but is restricted, and pointed to the owning role (CEO Office).

## EVAL2-0043 (restricted_document)
**Q:** As someone in SALES, can you show me the full Data Privacy Compliance Policy document?
**Expected department:** LEGAL | **Difficulty:** Advanced | **Authorization:** denied
**Expected answer:** No — POL-LEGAL-002 has access_level='restricted', restricted to Legal, Data Owners. A SALES employee should be told the document exists but is restricted, and pointed to the owning role (General Counsel).

## EVAL2-0044 (restricted_document)
**Q:** As someone in QA, can you show me the full Corporate Governance Policy document?
**Expected department:** MGMT | **Difficulty:** Advanced | **Authorization:** denied
**Expected answer:** No — POL-MGMT-001 has access_level='management', restricted to Director, Vice President, CEO Office. A QA employee should be told the document exists but is restricted, and pointed to the owning role (CEO Office).

## EVAL2-0045 (project_questions)
**Q:** What runbooks exist for PRJ-001 and what do they cover?
**Expected department:** Cross-Department | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** PRJ-001 has 6 technical runbooks covering distinct operational procedures specific to that project (see PRJ-001/runbooks/ for the full set) — these are separate from the main project.md overview.

## EVAL2-0046 (project_questions)
**Q:** What runbooks exist for PRJ-002 and what do they cover?
**Expected department:** Cross-Department | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** PRJ-002 has 6 technical runbooks covering distinct operational procedures specific to that project (see PRJ-002/runbooks/ for the full set) — these are separate from the main project.md overview.

## EVAL2-0047 (project_questions)
**Q:** What runbooks exist for PRJ-003 and what do they cover?
**Expected department:** Cross-Department | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** PRJ-003 has 6 technical runbooks covering distinct operational procedures specific to that project (see PRJ-003/runbooks/ for the full set) — these are separate from the main project.md overview.

## EVAL2-0048 (project_questions)
**Q:** What runbooks exist for PRJ-004 and what do they cover?
**Expected department:** Cross-Department | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** PRJ-004 has 6 technical runbooks covering distinct operational procedures specific to that project (see PRJ-004/runbooks/ for the full set) — these are separate from the main project.md overview.

## EVAL2-0049 (project_questions)
**Q:** What runbooks exist for PRJ-005 and what do they cover?
**Expected department:** Cross-Department | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** PRJ-005 has 6 technical runbooks covering distinct operational procedures specific to that project (see PRJ-005/runbooks/ for the full set) — these are separate from the main project.md overview.

## EVAL2-0050 (conflicting_looking_information)
**Q:** Is the leave carry-forward limit 5 days or 10 days?
**Expected department:** AMBIGUOUS | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** 10 days is the current limit (see the Leave Policy, POL-HR-001); an older reference to 5 days is the superseded value — check POL-HR-001-HISTORY for that transition.

## EVAL2-0051 (conflicting_looking_information)
**Q:** Is the discount approval limit 10% or 25% before Sales Director sign-off?
**Expected department:** AMBIGUOUS | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** The Sales Team Lead can approve up to 25% only via the Urgent/Expedited edge case; the standard non-emergency limit for Team Lead approval is 10%, escalating to Sales Director beyond that (POL-SALES-001).

## EVAL2-0052 (conflicting_looking_information)
**Q:** Does IT onboarding happen before or after HR onboarding?
**Expected department:** AMBIGUOUS | **Difficulty:** Advanced | **Authorization:** granted
**Expected answer:** They run in parallel: HR's onboarding procedure (SOP-HR-002) triggers IT's onboarding (SOP-IT-007) to start the same day, not sequentially after HR finishes.

## EVAL2-0053 (employee_workflow)
**Q:** What happens to my system access when I change departments internally?
**Expected department:** HR | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** Access for your old department's systems is reviewed and typically revoked, while your new department's IT/Security onboarding provisions fresh access — follow the Internal Job Transfer Procedure (SOP-HR-006).

## EVAL2-0054 (employee_workflow)
**Q:** If I'm promoted, does my system access change automatically?
**Expected department:** HR | **Difficulty:** Intermediate | **Authorization:** granted
**Expected answer:** Not automatically — the Promotion Nomination Procedure (SOP-HR-005) updates your role in MK-HRMS, but any resulting access-level change (e.g., approval rights) must be separately requested through the relevant department's access procedure.
