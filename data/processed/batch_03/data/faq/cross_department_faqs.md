# Cross-Department FAQs — Difficult / Multi-Department Questions

_These FAQs deliberately test cases where the answer requires knowledge from more than one department's SOPs and policies, and where the requester's own department does not match the department that owns the answer._

## FAQ-XDEPT-001: I'm an Engineer and I paid for a conference out of pocket — how do I get reimbursed, and does Engineering need to approve it too?
**Primary Department:** FIN | **Also Involves:** ENG | **Category:** Cross-Department: Expenses | **Difficulty:** Intermediate

**Answer:** Use the Finance Expense Reimbursement Procedure (SOP-FIN-001): submit the claim in MK-Finance360 with the conference invoice and business justification. Your Reporting Manager (Engineering Manager or Tech Lead) approves it first as your line manager, then Finance Lead reviews per the Expense Reimbursement Policy. Engineering does not need a separate sign-off beyond your manager's approval as requester.

**Related Documents:** SOP-FIN-001, POL-FIN-001

**Escalation Path:** Accountant -> Finance Lead -> Finance Manager -> Finance Director

---

## FAQ-XDEPT-002: An HR employee's laptop won't connect to Wi-Fi during a confidential compensation review meeting — what's the fastest path?
**Primary Department:** IT | **Also Involves:** HR | **Category:** Cross-Department: IT Support | **Difficulty:** Basic

**Answer:** Follow the standard Corporate Wi-Fi Troubleshooting Escalation (SOP-IT-006): toggle Wi-Fi and confirm Airplane Mode is off, then reconnect to the corporate network. If unresolved, raise a P2 ticket in MK-ServiceDesk — HR data sensitivity does not change the IT troubleshooting steps, but the employee should avoid discussing confidential details over an unsecured guest network while the primary connection is down.

**Related Documents:** SOP-IT-006

**Escalation Path:** IT Support Engineer -> IT Manager -> IT Director

---

## FAQ-XDEPT-003: A Sales rep wants to give a customer a bigger discount than they're authorized for, but the deal will fall through by end of day. What do they do?
**Primary Department:** SALES | **Also Involves:** FIN | **Category:** Cross-Department: Deal Approval | **Difficulty:** Advanced

**Answer:** This is exactly the Urgent/Expedited Path edge case for SOP-SALES-003 (Discount Approval Procedure): the Account Executive should contact the Sales Director directly (not only via MK-CRM) for verbal pre-approval, proceed if granted, and file the formal Discount Request in MK-CRM within 24 hours marked 'Emergency — Retroactive Approval'. Discounts above 25% still require Finance Director co-approval even under this path.

**Related Documents:** SOP-SALES-003-EDGE-B, POL-SALES-001

**Escalation Path:** Account Executive -> Sales Team Lead -> Sales Manager -> Sales Director

---

## FAQ-XDEPT-004: A Marketing employee wants to reference a specific enterprise customer by name in a case study — what approvals are needed across departments?
**Primary Department:** MKT | **Also Involves:** SALES, LEGAL | **Category:** Cross-Department: Content Approval | **Difficulty:** Advanced

**Answer:** Marketing drafts the case study per SOP-MKT-015 (Customer Case Study Development Procedure), but it cannot be published without written customer approval of the final draft. Additionally, referencing the customer's name/logo requires prior written consent per the Brand and Content Approval Policy (POL-MKT-001), and Sales (the account owner) should be looped in via the Customer Reference Request Procedure (SOP-SALES-011) to avoid over-contacting the same reference customer more than once a quarter.

**Related Documents:** SOP-MKT-015, SOP-SALES-011, POL-MKT-001

**Escalation Path:** Marketing Executive -> Marketing Team Lead -> Marketing Manager -> Marketing Director

---

## FAQ-XDEPT-005: An intern in Finance wants to approve a small vendor invoice while their manager is out — is that allowed?
**Primary Department:** FIN | **Also Involves:** HR | **Category:** Cross-Department: Authorization Limits | **Difficulty:** Intermediate

**Answer:** No. Per the Finance Intern Onboarding Procedure (SOP-FIN-015), interns are never given payment approval rights regardless of invoice size. If the Finance Lead is unavailable, use the Approver-Unavailable edge case (SOP-FIN-004-EDGE-A) to route the invoice to the designated delegate — never to an intern.

**Related Documents:** SOP-FIN-015, SOP-FIN-004-EDGE-A

**Escalation Path:** Accountant -> Finance Lead -> Finance Manager -> Finance Director

---

## FAQ-XDEPT-006: A customer's data may have been exposed through a Support ticket attachment — who owns the response, Support or Security?
**Primary Department:** SEC | **Also Involves:** SUPPORT, LEGAL | **Category:** Cross-Department: Incident Response | **Difficulty:** Advanced

**Answer:** Security owns incident response. The Support Associate should immediately report this to Security following the Security Incident Response Procedure (SOP-SEC-003) rather than trying to resolve it within Support alone. If confirmed, Security notifies Legal within 4 hours per the Incident Response Policy (POL-SEC-003), and Support continues to own the customer communication once Security/Legal confirm what can be disclosed.

**Related Documents:** SOP-SEC-003, POL-SEC-003

**Escalation Path:** Security Analyst -> Incident Response Lead -> Security Manager -> CISO

---

## FAQ-XDEPT-007: A Product Manager wants to launch a feature that stores new customer personal data — what has to happen before launch?
**Primary Department:** PROD | **Also Involves:** LEGAL, DATA | **Category:** Cross-Department: Compliance | **Difficulty:** Advanced

**Answer:** Two things must happen before launch, not just Product's own Launch Readiness Checklist (SOP-PROD-004): (1) Legal must complete a Data Privacy Impact Assessment via the DPIA Procedure (SOP-LEGAL-006) because this is a high-risk processing activity, and (2) the Product Risk & Compliance Review (SOP-PROD-016) must get Legal sign-off. Launch is blocked until both are complete, per the Feature Launch Policy (POL-PROD-001).

**Related Documents:** SOP-PROD-004, SOP-LEGAL-006, POL-PROD-001

**Escalation Path:** Associate Product Manager -> Product Manager -> Product Lead -> Head of Product

---

## FAQ-XDEPT-008: Someone in R&D wants to use a dataset scraped from a public website for a new experiment — is that OK?
**Primary Department:** RND | **Also Involves:** LEGAL | **Category:** Cross-Department: Data Governance | **Difficulty:** Advanced

**Answer:** Not without a check first. Per the Dataset Acquisition and Licensing Procedure (SOP-RND-005), the Research Associate must confirm the dataset's licence terms with Legal before use — 'publicly available' does not automatically mean it's licensed for this purpose. If licensing is unclear, the dataset cannot be used per the Responsible AI Policy (POL-RND-001) until Legal confirms permissibility.

**Related Documents:** SOP-RND-005, POL-RND-001

**Escalation Path:** Research Associate -> Research Lead -> R&D Manager -> R&D Director

---

## FAQ-XDEPT-009: A Procurement Specialist needs a vendor onboarded urgently for a DevOps tool, but the vendor hasn't completed a security review yet. Can they proceed?
**Primary Department:** PROC | **Also Involves:** SEC, DEVOPS | **Category:** Cross-Department: Vendor Risk | **Difficulty:** Advanced

**Answer:** No — this is a hard authorization boundary, not a discretionary one. The Vendor Onboarding Policy (POL-PROC-001) requires vendors handling company/customer data to complete a Security Assessment (SOP-SEC-009) before onboarding, and DevOps tooling typically has infrastructure access, so Security's review cannot be skipped even under the Emergency/Urgent Procurement Procedure (SOP-PROC-008).

**Related Documents:** SOP-PROC-008, SOP-SEC-009, POL-PROC-001

**Escalation Path:** Procurement Executive -> Procurement Specialist -> Procurement Manager -> Procurement Director

---

## FAQ-XDEPT-010: An Admin team member needs IT to move network ports during an office seating change — whose SOP governs this?
**Primary Department:** ADMIN | **Also Involves:** IT | **Category:** Cross-Department: Facilities | **Difficulty:** Basic

**Answer:** Both are involved but Admin leads. The Office Relocation/Seating Change Procedure (SOP-ADMIN-010) is the primary SOP; it explicitly requires notifying IT in advance to move network/phone connections, which IT then handles under its own Server/Network procedures. Admin owns the timeline; IT owns the technical execution.

**Related Documents:** SOP-ADMIN-010

**Escalation Path:** Facilities Executive -> Facilities Coordinator -> Facilities Manager -> Head of Administration

---

## FAQ-XDEPT-011: A Data Analyst wants to share a dashboard containing employee salary data with a department head who isn't in Finance or HR — allowed?
**Primary Department:** DATA | **Also Involves:** FIN, HR, SEC | **Category:** Cross-Department: Data Access | **Difficulty:** Advanced

**Answer:** Only after classification and access checks. Salary data is Restricted per the Payroll Administration Policy (POL-FIN-007), so it must be classified accordingly (SOP-DATA-005) and access requires Security Manager co-approval per the Data Access Request Procedure (SOP-DATA-001) — the requester's department alone doesn't grant access to Restricted data, regardless of their seniority.

**Related Documents:** SOP-DATA-001, SOP-DATA-005, POL-FIN-007

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-XDEPT-012: A QA Engineer found a bug that looks like it could be a security vulnerability — do they log it as a defect or report it to Security?
**Primary Department:** QA | **Also Involves:** SEC, ENG | **Category:** Cross-Department: Security Testing | **Difficulty:** Intermediate

**Answer:** Both, but in a specific order: report it to Security immediately via the Phishing/Incident channels is wrong here — for a code vulnerability, follow the Security Regression Testing Coordination process (SOP-QA-013) which routes findings to a Security Analyst for validation, and separately log it as a defect (SOP-QA-001) tagged Security-related so Engineering can track and fix it through the normal pipeline.

**Related Documents:** SOP-QA-001, SOP-QA-013

**Escalation Path:** QA Engineer -> QA Lead -> QA Manager -> QA Director

---

## FAQ-XDEPT-013: A new employee's manager is on leave on their first day — who completes the onboarding sign-off?
**Primary Department:** HR | **Also Involves:** IT, SEC | **Category:** Cross-Department: Onboarding | **Difficulty:** Intermediate

**Answer:** Use the Approver-Unavailable edge case pattern: HR's New Employee Onboarding Procedure (SOP-HR-002) still proceeds on schedule (IT/Security onboarding are not manager-dependent), but for any step requiring the manager's sign-off, the delegate identified in the escalation chain (typically the manager's own manager) signs off instead, and the returning manager is notified per the standard edge-case pattern.

**Related Documents:** SOP-HR-002, SOP-HR-002-EDGE-A

**Escalation Path:** HR Executive -> HR Business Partner -> HR Manager -> HR Director

---

## FAQ-XDEPT-014: Can a Support Manager approve their own customer refund if the customer is a personal friend, to avoid awkwardness with a peer?
**Primary Department:** SUPPORT | **Also Involves:** HR | **Category:** Cross-Department: Conflict of Interest | **Difficulty:** Advanced

**Answer:** No — this is a conflict-of-interest situation. Per the Employee Conduct Policy (POL-HR-004), conflicts of interest must be disclosed to the Reporting Manager and HR Business Partner, and the Support Manager should recuse themselves from the Refund/Credit Request Procedure (SOP-SUPPORT-005), routing the approval to their own manager instead.

**Related Documents:** SOP-SUPPORT-005, POL-HR-004

**Escalation Path:** Support Associate -> Support Team Lead -> Support Manager -> Customer Experience Director

---

## FAQ-XDEPT-015: A DevOps engineer wants to deploy a fix at 2 AM without going through the normal MK-CI pipeline because production is down — is that allowed?
**Primary Department:** DEVOPS | **Also Involves:** ENG, SEC | **Category:** Cross-Department: Incident Response | **Difficulty:** Advanced

**Answer:** During a declared Sev-1 incident, yes, with conditions. The Production Change Policy (POL-DEVOPS-001) prohibits manual production changes except during a declared incident; the engineer should follow the Production Incident Response procedure (SOP-DEVOPS-004) and the Rollback Procedure (SOP-DEVOPS-012) if applicable, and any manual change must still be retroactively logged and reviewed the next business day.

**Related Documents:** SOP-DEVOPS-004, POL-DEVOPS-001

**Escalation Path:** DevOps Engineer -> DevOps Manager -> DevOps Director

---

## FAQ-XDEPT-016: A Legal Associate wants Engineering to add a clause enforcement check directly into the product — is this a Legal SOP or an Engineering one?
**Primary Department:** LEGAL | **Also Involves:** PROD, ENG | **Category:** Cross-Department: Requirement Handoff | **Difficulty:** Advanced

**Answer:** Neither owns it alone — it starts as a Legal requirement flowing into Product/Engineering delivery. Legal documents the requirement via the Policy Drafting and Approval Procedure (SOP-LEGAL-015) or a Contract Review Request if customer-specific, then Product creates a PRD (SOP-PROD-001) so Engineering can scope and build it through the normal technical design and sprint planning process (SOP-ENG-011, SOP-ENG-009).

**Related Documents:** SOP-LEGAL-015, SOP-PROD-001, SOP-ENG-011

**Escalation Path:** Legal Associate -> Contracts Specialist -> Legal Manager -> General Counsel

---

## FAQ-XDEPT-017: An employee wants to expense a gift for a vendor contact to say thank you — is this allowed and does Procurement need to know?
**Primary Department:** FIN | **Also Involves:** PROC | **Category:** Cross-Department: Ethics & Expenses | **Difficulty:** Intermediate

**Answer:** It depends on value and intent, and yes, flag it. Submit via the standard Expense Reimbursement Procedure (SOP-FIN-001), but gifts to vendor contacts can raise ethical sourcing concerns — check with Procurement's Sustainable/Ethical Sourcing Review (SOP-PROC-012) guidance and keep the value modest; anything that could be seen as influencing a vendor decision should be disclosed to the Procurement Manager beforehand.

**Related Documents:** SOP-FIN-001, SOP-PROC-012

**Escalation Path:** Accountant -> Finance Lead -> Finance Manager -> Finance Director

---

## FAQ-XDEPT-018: A Data Engineer wants to use anonymized production data in an R&D research experiment — whose approval chain applies?
**Primary Department:** DATA | **Also Involves:** RND, SEC | **Category:** Cross-Department: Data Sharing | **Difficulty:** Advanced

**Answer:** Both departments' controls apply, layered. Data & Analytics' Data Anonymization for Testing Procedure (SOP-DATA-013) governs how the data is anonymized and by whom (Security Manager approval required), and then R&D's Experiment Design and Tracking Procedure (SOP-RND-002) governs how it's used in the experiment — R&D cannot skip DATA's anonymization step even for internal research.

**Related Documents:** SOP-DATA-013, SOP-RND-002

**Escalation Path:** Data Analyst -> Analytics Lead -> Data Manager -> Director of Data & Analytics

---

## FAQ-XDEPT-019: Management wants a same-day answer on whether the company can afford a new hire — who do they ask?
**Primary Department:** MGMT | **Also Involves:** FIN, HR | **Category:** Cross-Department: Budget & Headcount | **Difficulty:** Advanced

**Answer:** This routes through Finance and HR together under Management's authority. Finance provides current budget headroom against the Departmental Budget Approval Procedure (SOP-MGMT-003), HR confirms the role is within an approved headcount plan via the Recruitment Requisition Procedure (SOP-HR-008), and Management makes the final call — Executive Hiring Approval (SOP-MGMT-008) is required if the role is at director level or above.

**Related Documents:** SOP-MGMT-003, SOP-HR-008, SOP-MGMT-008

**Escalation Path:** Manager -> Director -> Vice President -> CEO Office

---

## FAQ-XDEPT-020: A contractor's engagement is ending — does IT, Security, or HR own revoking their access?
**Primary Department:** IT | **Also Involves:** SEC, HR, PMO | **Category:** Cross-Department: Offboarding | **Difficulty:** Advanced

**Answer:** All three, in sequence, coordinated by the engaging department (often PMO or Procurement for contractor engagements). HR/PMO triggers the exit per the contract end date, IT executes the IT Asset Return and account deactivation (SOP-IT-016), and Security confirms all access — VPN, privileged access, badges — is revoked within the same 4-hour SLA as any other departing individual, per the Access Control Policy.

**Related Documents:** SOP-IT-016, POL-SEC-001

**Escalation Path:** IT Support Engineer -> IT Manager -> IT Director

---
