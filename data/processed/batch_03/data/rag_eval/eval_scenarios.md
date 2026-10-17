# RAG Evaluation Scenario Set

_144 labeled test cases for evaluating Agentic-RAG-KnowXAI's retrieval accuracy, authorization enforcement, and cross-department synthesis. Grouped by eval_type below._

## same_department_retrieval (108 scenarios)

- **EVAL-0001**: "As a IT employee, how do I complete: Password Reset Procedure?" — requester_dept=IT, expected_dept=IT, expected_docs=['SOP-IT-001'], should_be_authorized=True
- **EVAL-0002**: "As a IT employee, how do I complete: New Hardware Request Fulfillment?" — requester_dept=IT, expected_dept=IT, expected_docs=['SOP-IT-002'], should_be_authorized=True
- **EVAL-0003**: "As a IT employee, how do I complete: Software Installation Request?" — requester_dept=IT, expected_dept=IT, expected_docs=['SOP-IT-003'], should_be_authorized=True
- **EVAL-0004**: "As a IT employee, how do I complete: Corporate VPN Access Setup?" — requester_dept=IT, expected_dept=IT, expected_docs=['SOP-IT-004'], should_be_authorized=True
- **EVAL-0005**: "As a IT employee, how do I complete: Laptop Replacement Process?" — requester_dept=IT, expected_dept=IT, expected_docs=['SOP-IT-005'], should_be_authorized=True
- **EVAL-0006**: "As a IT employee, how do I complete: Corporate Wi-Fi Troubleshooting Escalation?" — requester_dept=IT, expected_dept=IT, expected_docs=['SOP-IT-006'], should_be_authorized=True
- **EVAL-0007**: "As a ENG employee, how do I complete: Feature Branch Creation and Naming?" — requester_dept=ENG, expected_dept=ENG, expected_docs=['SOP-ENG-001'], should_be_authorized=True
- **EVAL-0008**: "As a ENG employee, how do I complete: Code Review Process?" — requester_dept=ENG, expected_dept=ENG, expected_docs=['SOP-ENG-002'], should_be_authorized=True
- **EVAL-0009**: "As a ENG employee, how do I complete: New Repository Setup?" — requester_dept=ENG, expected_dept=ENG, expected_docs=['SOP-ENG-003'], should_be_authorized=True
- **EVAL-0010**: "As a ENG employee, how do I complete: Production Hotfix Deployment?" — requester_dept=ENG, expected_dept=ENG, expected_docs=['SOP-ENG-004'], should_be_authorized=True
- **EVAL-0011**: "As a ENG employee, how do I complete: Local Development Environment Setup?" — requester_dept=ENG, expected_dept=ENG, expected_docs=['SOP-ENG-005'], should_be_authorized=True
- **EVAL-0012**: "As a ENG employee, how do I complete: API Key and Secret Rotation?" — requester_dept=ENG, expected_dept=ENG, expected_docs=['SOP-ENG-006'], should_be_authorized=True
- **EVAL-0013**: "As a QA employee, how do I complete: Software Defect Reporting Procedure?" — requester_dept=QA, expected_dept=QA, expected_docs=['SOP-QA-001'], should_be_authorized=True
- **EVAL-0014**: "As a QA employee, how do I complete: Test Case Design and Review?" — requester_dept=QA, expected_dept=QA, expected_docs=['SOP-QA-002'], should_be_authorized=True
- **EVAL-0015**: "As a QA employee, how do I complete: Regression Test Cycle Execution?" — requester_dept=QA, expected_dept=QA, expected_docs=['SOP-QA-003'], should_be_authorized=True
- **EVAL-0016**: "As a QA employee, how do I complete: Test Automation Script Development?" — requester_dept=QA, expected_dept=QA, expected_docs=['SOP-QA-004'], should_be_authorized=True
- **EVAL-0017**: "As a QA employee, how do I complete: Release Sign-off / Go-No-Go Procedure?" — requester_dept=QA, expected_dept=QA, expected_docs=['SOP-QA-005'], should_be_authorized=True
- **EVAL-0018**: "As a QA employee, how do I complete: Performance Test Execution?" — requester_dept=QA, expected_dept=QA, expected_docs=['SOP-QA-006'], should_be_authorized=True
- **EVAL-0019**: "As a DEVOPS employee, how do I complete: Service Deployment Procedure?" — requester_dept=DEVOPS, expected_dept=DEVOPS, expected_docs=['SOP-DEVOPS-001'], should_be_authorized=True
- **EVAL-0020**: "As a DEVOPS employee, how do I complete: CI/CD Pipeline Configuration?" — requester_dept=DEVOPS, expected_dept=DEVOPS, expected_docs=['SOP-DEVOPS-002'], should_be_authorized=True
- **EVAL-0021**: "As a DEVOPS employee, how do I complete: Cloud Resource Provisioning Request?" — requester_dept=DEVOPS, expected_dept=DEVOPS, expected_docs=['SOP-DEVOPS-003'], should_be_authorized=True
- **EVAL-0022**: "As a DEVOPS employee, how do I complete: Production Incident Response (DevOps)?" — requester_dept=DEVOPS, expected_dept=DEVOPS, expected_docs=['SOP-DEVOPS-004'], should_be_authorized=True
- **EVAL-0023**: "As a DEVOPS employee, how do I complete: Infrastructure as Code (IaC) Change Procedure?" — requester_dept=DEVOPS, expected_dept=DEVOPS, expected_docs=['SOP-DEVOPS-005'], should_be_authorized=True
- **EVAL-0024**: "As a DEVOPS employee, how do I complete: Auto-scaling Configuration Procedure?" — requester_dept=DEVOPS, expected_dept=DEVOPS, expected_docs=['SOP-DEVOPS-006'], should_be_authorized=True
- **EVAL-0025**: "As a SEC employee, how do I complete: Phishing Email Reporting Procedure?" — requester_dept=SEC, expected_dept=SEC, expected_docs=['SOP-SEC-001'], should_be_authorized=True
- **EVAL-0026**: "As a SEC employee, how do I complete: Multi-Factor Authentication (MFA) Enrollment?" — requester_dept=SEC, expected_dept=SEC, expected_docs=['SOP-SEC-002'], should_be_authorized=True
- **EVAL-0027**: "As a SEC employee, how do I complete: Security Incident Response Procedure?" — requester_dept=SEC, expected_dept=SEC, expected_docs=['SOP-SEC-003'], should_be_authorized=True
- **EVAL-0028**: "As a SEC employee, how do I complete: Access Control Review?" — requester_dept=SEC, expected_dept=SEC, expected_docs=['SOP-SEC-004'], should_be_authorized=True
- **EVAL-0029**: "As a SEC employee, how do I complete: Vulnerability Scanning and Remediation?" — requester_dept=SEC, expected_dept=SEC, expected_docs=['SOP-SEC-005'], should_be_authorized=True
- **EVAL-0030**: "As a SEC employee, how do I complete: Data Loss Prevention (DLP) Alert Handling?" — requester_dept=SEC, expected_dept=SEC, expected_docs=['SOP-SEC-006'], should_be_authorized=True
- **EVAL-0031**: "As a HR employee, how do I complete: Leave Application Procedure?" — requester_dept=HR, expected_dept=HR, expected_docs=['SOP-HR-001'], should_be_authorized=True
- **EVAL-0032**: "As a HR employee, how do I complete: New Employee Onboarding Procedure?" — requester_dept=HR, expected_dept=HR, expected_docs=['SOP-HR-002'], should_be_authorized=True
- **EVAL-0033**: "As a HR employee, how do I complete: Employee Exit / Offboarding Procedure?" — requester_dept=HR, expected_dept=HR, expected_docs=['SOP-HR-003'], should_be_authorized=True
- **EVAL-0034**: "As a HR employee, how do I complete: Performance Review Cycle Procedure?" — requester_dept=HR, expected_dept=HR, expected_docs=['SOP-HR-004'], should_be_authorized=True
- **EVAL-0035**: "As a HR employee, how do I complete: Promotion Nomination Procedure?" — requester_dept=HR, expected_dept=HR, expected_docs=['SOP-HR-005'], should_be_authorized=True
- **EVAL-0036**: "As a HR employee, how do I complete: Internal Job Transfer Procedure?" — requester_dept=HR, expected_dept=HR, expected_docs=['SOP-HR-006'], should_be_authorized=True
- **EVAL-0037**: "As a FIN employee, how do I complete: Expense Reimbursement Procedure?" — requester_dept=FIN, expected_dept=FIN, expected_docs=['SOP-FIN-001'], should_be_authorized=True
- **EVAL-0038**: "As a FIN employee, how do I complete: Travel Expense Reimbursement Procedure?" — requester_dept=FIN, expected_dept=FIN, expected_docs=['SOP-FIN-002'], should_be_authorized=True
- **EVAL-0039**: "As a FIN employee, how do I complete: Purchase Approval Procedure?" — requester_dept=FIN, expected_dept=FIN, expected_docs=['SOP-FIN-003'], should_be_authorized=True
- **EVAL-0040**: "As a FIN employee, how do I complete: Invoice Processing Procedure?" — requester_dept=FIN, expected_dept=FIN, expected_docs=['SOP-FIN-004'], should_be_authorized=True
- **EVAL-0041**: "As a FIN employee, how do I complete: Vendor Payment Procedure?" — requester_dept=FIN, expected_dept=FIN, expected_docs=['SOP-FIN-005'], should_be_authorized=True
- **EVAL-0042**: "As a FIN employee, how do I complete: Budget Approval Procedure?" — requester_dept=FIN, expected_dept=FIN, expected_docs=['SOP-FIN-006'], should_be_authorized=True
- **EVAL-0043**: "As a PMO employee, how do I complete: Project Creation and Charter Approval Procedure?" — requester_dept=PMO, expected_dept=PMO, expected_docs=['SOP-PMO-001'], should_be_authorized=True
- **EVAL-0044**: "As a PMO employee, how do I complete: Project Risk Register Update Procedure?" — requester_dept=PMO, expected_dept=PMO, expected_docs=['SOP-PMO-002'], should_be_authorized=True
- **EVAL-0045**: "As a PMO employee, how do I complete: Project Status Reporting Procedure?" — requester_dept=PMO, expected_dept=PMO, expected_docs=['SOP-PMO-003'], should_be_authorized=True
- **EVAL-0046**: "As a PMO employee, how do I complete: Change Request Procedure?" — requester_dept=PMO, expected_dept=PMO, expected_docs=['SOP-PMO-004'], should_be_authorized=True
- **EVAL-0047**: "As a PMO employee, how do I complete: Project Escalation Procedure?" — requester_dept=PMO, expected_dept=PMO, expected_docs=['SOP-PMO-005'], should_be_authorized=True
- **EVAL-0048**: "As a PMO employee, how do I complete: Resource Allocation Request Procedure?" — requester_dept=PMO, expected_dept=PMO, expected_docs=['SOP-PMO-006'], should_be_authorized=True
- **EVAL-0049**: "As a PROD employee, how do I complete: Product Requirement Document (PRD) Creation?" — requester_dept=PROD, expected_dept=PROD, expected_docs=['SOP-PROD-001'], should_be_authorized=True
- **EVAL-0050**: "As a PROD employee, how do I complete: Feature Prioritization Procedure?" — requester_dept=PROD, expected_dept=PROD, expected_docs=['SOP-PROD-002'], should_be_authorized=True
- **EVAL-0051**: "As a PROD employee, how do I complete: Customer Feedback Intake and Triage?" — requester_dept=PROD, expected_dept=PROD, expected_docs=['SOP-PROD-003'], should_be_authorized=True
- **EVAL-0052**: "As a PROD employee, how do I complete: Product Launch Readiness Procedure?" — requester_dept=PROD, expected_dept=PROD, expected_docs=['SOP-PROD-004'], should_be_authorized=True
- **EVAL-0053**: "As a PROD employee, how do I complete: A/B Experiment Design Procedure?" — requester_dept=PROD, expected_dept=PROD, expected_docs=['SOP-PROD-005'], should_be_authorized=True
- **EVAL-0054**: "As a PROD employee, how do I complete: Competitive Analysis Procedure?" — requester_dept=PROD, expected_dept=PROD, expected_docs=['SOP-PROD-006'], should_be_authorized=True
- **EVAL-0055**: "As a SALES employee, how do I complete: New Lead Qualification Procedure?" — requester_dept=SALES, expected_dept=SALES, expected_docs=['SOP-SALES-001'], should_be_authorized=True
- **EVAL-0056**: "As a SALES employee, how do I complete: Opportunity Creation and Pipeline Entry?" — requester_dept=SALES, expected_dept=SALES, expected_docs=['SOP-SALES-002'], should_be_authorized=True
- **EVAL-0057**: "As a SALES employee, how do I complete: Discount Approval Procedure?" — requester_dept=SALES, expected_dept=SALES, expected_docs=['SOP-SALES-003'], should_be_authorized=True
- **EVAL-0058**: "As a SALES employee, how do I complete: Contract/Quote Generation Procedure?" — requester_dept=SALES, expected_dept=SALES, expected_docs=['SOP-SALES-004'], should_be_authorized=True
- **EVAL-0059**: "As a SALES employee, how do I complete: Deal Closure and Handover to Customer Support?" — requester_dept=SALES, expected_dept=SALES, expected_docs=['SOP-SALES-005'], should_be_authorized=True
- **EVAL-0060**: "As a SALES employee, how do I complete: Sales Forecast Submission Procedure?" — requester_dept=SALES, expected_dept=SALES, expected_docs=['SOP-SALES-006'], should_be_authorized=True
- **EVAL-0061**: "As a MKT employee, how do I complete: Campaign Planning and Approval Procedure?" — requester_dept=MKT, expected_dept=MKT, expected_docs=['SOP-MKT-001'], should_be_authorized=True
- **EVAL-0062**: "As a MKT employee, how do I complete: Content Creation and Review Procedure?" — requester_dept=MKT, expected_dept=MKT, expected_docs=['SOP-MKT-002'], should_be_authorized=True
- **EVAL-0063**: "As a MKT employee, how do I complete: Website Update Request Procedure?" — requester_dept=MKT, expected_dept=MKT, expected_docs=['SOP-MKT-003'], should_be_authorized=True
- **EVAL-0064**: "As a MKT employee, how do I complete: Event Planning and Coordination Procedure?" — requester_dept=MKT, expected_dept=MKT, expected_docs=['SOP-MKT-004'], should_be_authorized=True
- **EVAL-0065**: "As a MKT employee, how do I complete: Marketing Qualified Lead (MQL) Handover to Sales?" — requester_dept=MKT, expected_dept=MKT, expected_docs=['SOP-MKT-005'], should_be_authorized=True
- **EVAL-0066**: "As a MKT employee, how do I complete: Social Media Publishing Procedure?" — requester_dept=MKT, expected_dept=MKT, expected_docs=['SOP-MKT-006'], should_be_authorized=True
- **EVAL-0067**: "As a SUPPORT employee, how do I complete: Customer Ticket Intake and Categorization?" — requester_dept=SUPPORT, expected_dept=SUPPORT, expected_docs=['SOP-SUPPORT-001'], should_be_authorized=True
- **EVAL-0068**: "As a SUPPORT employee, how do I complete: Customer Ticket Escalation Procedure?" — requester_dept=SUPPORT, expected_dept=SUPPORT, expected_docs=['SOP-SUPPORT-002'], should_be_authorized=True
- **EVAL-0069**: "As a SUPPORT employee, how do I complete: SLA Breach Handling Procedure?" — requester_dept=SUPPORT, expected_dept=SUPPORT, expected_docs=['SOP-SUPPORT-003'], should_be_authorized=True
- **EVAL-0070**: "As a SUPPORT employee, how do I complete: Bug Report Handover to Engineering?" — requester_dept=SUPPORT, expected_dept=SUPPORT, expected_docs=['SOP-SUPPORT-004'], should_be_authorized=True
- **EVAL-0071**: "As a SUPPORT employee, how do I complete: Customer Refund/Credit Request Procedure?" — requester_dept=SUPPORT, expected_dept=SUPPORT, expected_docs=['SOP-SUPPORT-005'], should_be_authorized=True
- **EVAL-0072**: "As a SUPPORT employee, how do I complete: Knowledge Base Article Creation Procedure?" — requester_dept=SUPPORT, expected_dept=SUPPORT, expected_docs=['SOP-SUPPORT-006'], should_be_authorized=True
- **EVAL-0073**: "As a LEGAL employee, how do I complete: Contract Review Request Procedure?" — requester_dept=LEGAL, expected_dept=LEGAL, expected_docs=['SOP-LEGAL-001'], should_be_authorized=True
- **EVAL-0074**: "As a LEGAL employee, how do I complete: NDA Execution Procedure?" — requester_dept=LEGAL, expected_dept=LEGAL, expected_docs=['SOP-LEGAL-002'], should_be_authorized=True
- **EVAL-0075**: "As a LEGAL employee, how do I complete: Vendor Contract Negotiation Support?" — requester_dept=LEGAL, expected_dept=LEGAL, expected_docs=['SOP-LEGAL-003'], should_be_authorized=True
- **EVAL-0076**: "As a LEGAL employee, how do I complete: Regulatory Compliance Monitoring Procedure?" — requester_dept=LEGAL, expected_dept=LEGAL, expected_docs=['SOP-LEGAL-004'], should_be_authorized=True
- **EVAL-0077**: "As a LEGAL employee, how do I complete: Intellectual Property Filing Procedure?" — requester_dept=LEGAL, expected_dept=LEGAL, expected_docs=['SOP-LEGAL-005'], should_be_authorized=True
- **EVAL-0078**: "As a LEGAL employee, how do I complete: Data Privacy Impact Assessment (DPIA) Procedure?" — requester_dept=LEGAL, expected_dept=LEGAL, expected_docs=['SOP-LEGAL-006'], should_be_authorized=True
- **EVAL-0079**: "As a PROC employee, how do I complete: New Hardware/Equipment Request Procedure?" — requester_dept=PROC, expected_dept=PROC, expected_docs=['SOP-PROC-001'], should_be_authorized=True
- **EVAL-0080**: "As a PROC employee, how do I complete: Vendor Selection and Onboarding Procedure?" — requester_dept=PROC, expected_dept=PROC, expected_docs=['SOP-PROC-002'], should_be_authorized=True
- **EVAL-0081**: "As a PROC employee, how do I complete: Purchase Order Issuance Procedure?" — requester_dept=PROC, expected_dept=PROC, expected_docs=['SOP-PROC-003'], should_be_authorized=True
- **EVAL-0082**: "As a PROC employee, how do I complete: Vendor Contract Renewal Procedure?" — requester_dept=PROC, expected_dept=PROC, expected_docs=['SOP-PROC-004'], should_be_authorized=True
- **EVAL-0083**: "As a PROC employee, how do I complete: Goods Receipt and Inspection Procedure?" — requester_dept=PROC, expected_dept=PROC, expected_docs=['SOP-PROC-005'], should_be_authorized=True
- **EVAL-0084**: "As a PROC employee, how do I complete: Procurement Budget Tracking Procedure?" — requester_dept=PROC, expected_dept=PROC, expected_docs=['SOP-PROC-006'], should_be_authorized=True
- **EVAL-0085**: "As a ADMIN employee, how do I complete: New Employee Workspace Setup Procedure?" — requester_dept=ADMIN, expected_dept=ADMIN, expected_docs=['SOP-ADMIN-001'], should_be_authorized=True
- **EVAL-0086**: "As a ADMIN employee, how do I complete: Office Access Card Issuance Procedure?" — requester_dept=ADMIN, expected_dept=ADMIN, expected_docs=['SOP-ADMIN-002'], should_be_authorized=True
- **EVAL-0087**: "As a ADMIN employee, how do I complete: Meeting Room Booking Procedure?" — requester_dept=ADMIN, expected_dept=ADMIN, expected_docs=['SOP-ADMIN-003'], should_be_authorized=True
- **EVAL-0088**: "As a ADMIN employee, how do I complete: Facility Maintenance Request Procedure?" — requester_dept=ADMIN, expected_dept=ADMIN, expected_docs=['SOP-ADMIN-004'], should_be_authorized=True
- **EVAL-0089**: "As a ADMIN employee, how do I complete: Office Supplies Replenishment Procedure?" — requester_dept=ADMIN, expected_dept=ADMIN, expected_docs=['SOP-ADMIN-005'], should_be_authorized=True
- **EVAL-0090**: "As a ADMIN employee, how do I complete: Visitor Management Procedure?" — requester_dept=ADMIN, expected_dept=ADMIN, expected_docs=['SOP-ADMIN-006'], should_be_authorized=True
- **EVAL-0091**: "As a DATA employee, how do I complete: Data Access Request Procedure?" — requester_dept=DATA, expected_dept=DATA, expected_docs=['SOP-DATA-001'], should_be_authorized=True
- **EVAL-0092**: "As a DATA employee, how do I complete: Dashboard/Report Request Procedure?" — requester_dept=DATA, expected_dept=DATA, expected_docs=['SOP-DATA-002'], should_be_authorized=True
- **EVAL-0093**: "As a DATA employee, how do I complete: Data Pipeline Development Procedure?" — requester_dept=DATA, expected_dept=DATA, expected_docs=['SOP-DATA-003'], should_be_authorized=True
- **EVAL-0094**: "As a DATA employee, how do I complete: Data Quality Issue Resolution Procedure?" — requester_dept=DATA, expected_dept=DATA, expected_docs=['SOP-DATA-004'], should_be_authorized=True
- **EVAL-0095**: "As a DATA employee, how do I complete: Data Classification for Analytics Datasets?" — requester_dept=DATA, expected_dept=DATA, expected_docs=['SOP-DATA-005'], should_be_authorized=True
- **EVAL-0096**: "As a DATA employee, how do I complete: Ad-hoc Data Analysis Request Procedure?" — requester_dept=DATA, expected_dept=DATA, expected_docs=['SOP-DATA-006'], should_be_authorized=True
- **EVAL-0097**: "As a RND employee, how do I complete: Research Proposal Submission Procedure?" — requester_dept=RND, expected_dept=RND, expected_docs=['SOP-RND-001'], should_be_authorized=True
- **EVAL-0098**: "As a RND employee, how do I complete: Experiment Design and Tracking Procedure?" — requester_dept=RND, expected_dept=RND, expected_docs=['SOP-RND-002'], should_be_authorized=True
- **EVAL-0099**: "As a RND employee, how do I complete: Model Evaluation and Benchmarking Procedure?" — requester_dept=RND, expected_dept=RND, expected_docs=['SOP-RND-003'], should_be_authorized=True
- **EVAL-0100**: "As a RND employee, how do I complete: Research-to-Production Handover Procedure?" — requester_dept=RND, expected_dept=RND, expected_docs=['SOP-RND-004'], should_be_authorized=True
- **EVAL-0101**: "As a RND employee, how do I complete: Dataset Acquisition and Licensing Procedure?" — requester_dept=RND, expected_dept=RND, expected_docs=['SOP-RND-005'], should_be_authorized=True
- **EVAL-0102**: "As a RND employee, how do I complete: Research Publication Approval Procedure?" — requester_dept=RND, expected_dept=RND, expected_docs=['SOP-RND-006'], should_be_authorized=True
- **EVAL-0103**: "As a MGMT employee, how do I complete: Company Strategy Planning Procedure?" — requester_dept=MGMT, expected_dept=MGMT, expected_docs=['SOP-MGMT-001'], should_be_authorized=True
- **EVAL-0104**: "As a MGMT employee, how do I complete: Project Portfolio Review Procedure (Management)?" — requester_dept=MGMT, expected_dept=MGMT, expected_docs=['SOP-MGMT-002'], should_be_authorized=True
- **EVAL-0105**: "As a MGMT employee, how do I complete: Departmental Budget Approval Procedure?" — requester_dept=MGMT, expected_dept=MGMT, expected_docs=['SOP-MGMT-003'], should_be_authorized=True
- **EVAL-0106**: "As a MGMT employee, how do I complete: Executive Decision Escalation Procedure?" — requester_dept=MGMT, expected_dept=MGMT, expected_docs=['SOP-MGMT-004'], should_be_authorized=True
- **EVAL-0107**: "As a MGMT employee, how do I complete: Organizational Change / Restructuring Procedure?" — requester_dept=MGMT, expected_dept=MGMT, expected_docs=['SOP-MGMT-005'], should_be_authorized=True
- **EVAL-0108**: "As a MGMT employee, how do I complete: Board Reporting Procedure?" — requester_dept=MGMT, expected_dept=MGMT, expected_docs=['SOP-MGMT-006'], should_be_authorized=True

## cross_department_retrieval (18 scenarios)

- **EVAL-0109**: "As a IT employee, endpoint security alert triage — how do I do that?" — requester_dept=IT, expected_dept=SEC, expected_docs=['SOP-SEC-011'], should_be_authorized=True
- **EVAL-0110**: "As a ENG employee, company-wide policy approval procedure — how do I do that?" — requester_dept=ENG, expected_dept=MGMT, expected_docs=['SOP-MGMT-009'], should_be_authorized=True
- **EVAL-0111**: "As a QA employee, security awareness training assignment — how do I do that?" — requester_dept=QA, expected_dept=SEC, expected_docs=['SOP-SEC-008'], should_be_authorized=True
- **EVAL-0112**: "As a DEVOPS employee, emergency evacuation procedure — how do I do that?" — requester_dept=DEVOPS, expected_dept=ADMIN, expected_docs=['SOP-ADMIN-013'], should_be_authorized=True
- **EVAL-0113**: "As a SEC employee, external research collaboration procedure — how do I do that?" — requester_dept=SEC, expected_dept=RND, expected_docs=['SOP-RND-013'], should_be_authorized=True
- **EVAL-0114**: "As a HR employee, data quality issue resolution procedure — how do I do that?" — requester_dept=HR, expected_dept=DATA, expected_docs=['SOP-DATA-004'], should_be_authorized=True
- **EVAL-0115**: "As a FIN employee, software installation request — how do I do that?" — requester_dept=FIN, expected_dept=IT, expected_docs=['SOP-IT-003'], should_be_authorized=True
- **EVAL-0116**: "As a PMO employee, container image build and publish — how do I do that?" — requester_dept=PMO, expected_dept=DEVOPS, expected_docs=['SOP-DEVOPS-010'], should_be_authorized=True
- **EVAL-0117**: "As a PROD employee, patch management for infrastructure — how do I do that?" — requester_dept=PROD, expected_dept=DEVOPS, expected_docs=['SOP-DEVOPS-015'], should_be_authorized=True
- **EVAL-0118**: "As a SALES employee, it asset return on exit — how do I do that?" — requester_dept=SALES, expected_dept=IT, expected_docs=['SOP-IT-016'], should_be_authorized=True
- **EVAL-0119**: "As a MKT employee, bug report handover to engineering — how do I do that?" — requester_dept=MKT, expected_dept=SUPPORT, expected_docs=['SOP-SUPPORT-004'], should_be_authorized=True
- **EVAL-0120**: "As a SUPPORT employee, goods receipt and inspection procedure — how do I do that?" — requester_dept=SUPPORT, expected_dept=PROC, expected_docs=['SOP-PROC-005'], should_be_authorized=True
- **EVAL-0121**: "As a LEGAL employee, customer complaint handling procedure — how do I do that?" — requester_dept=LEGAL, expected_dept=SUPPORT, expected_docs=['SOP-SUPPORT-015'], should_be_authorized=True
- **EVAL-0122**: "As a PROC employee, live chat support procedure — how do I do that?" — requester_dept=PROC, expected_dept=SUPPORT, expected_docs=['SOP-SUPPORT-013'], should_be_authorized=True
- **EVAL-0123**: "As a ADMIN employee, vendor contract negotiation support — how do I do that?" — requester_dept=ADMIN, expected_dept=LEGAL, expected_docs=['SOP-LEGAL-003'], should_be_authorized=True
- **EVAL-0124**: "As a DATA employee, website update request procedure — how do I do that?" — requester_dept=DATA, expected_dept=MKT, expected_docs=['SOP-MKT-003'], should_be_authorized=True
- **EVAL-0125**: "As a RND employee, sales onboarding procedure for new hires — how do I do that?" — requester_dept=RND, expected_dept=SALES, expected_docs=['SOP-SALES-010'], should_be_authorized=True
- **EVAL-0126**: "As a MGMT employee, meeting room booking procedure — how do I do that?" — requester_dept=MGMT, expected_dept=ADMIN, expected_docs=['SOP-ADMIN-003'], should_be_authorized=True

## authorization_denial (8 scenarios)

- **EVAL-0127**: "As a general employee outside SEC, what are the details of the Access Control Policy?" — requester_dept=MKT, expected_dept=SEC, expected_docs=['POL-SEC-001'], should_be_authorized=False
- **EVAL-0128**: "As a general employee outside SEC, what are the details of the Incident Response Policy?" — requester_dept=IT, expected_dept=SEC, expected_docs=['POL-SEC-003'], should_be_authorized=False
- **EVAL-0129**: "As a general employee outside SEC, what are the details of the Data Protection Policy?" — requester_dept=LEGAL, expected_dept=SEC, expected_docs=['POL-SEC-005'], should_be_authorized=False
- **EVAL-0130**: "As a general employee outside FIN, what are the details of the Vendor Payment Policy?" — requester_dept=LEGAL, expected_dept=FIN, expected_docs=['POL-FIN-005'], should_be_authorized=False
- **EVAL-0131**: "As a general employee outside FIN, what are the details of the Payroll Administration Policy?" — requester_dept=DATA, expected_dept=FIN, expected_docs=['POL-FIN-007'], should_be_authorized=False
- **EVAL-0132**: "As a general employee outside FIN, what are the details of the Executive Compensation Policy?" — requester_dept=ADMIN, expected_dept=FIN, expected_docs=['POL-FIN-008'], should_be_authorized=False
- **EVAL-0133**: "As a general employee outside LEGAL, what are the details of the Data Privacy Compliance Policy?" — requester_dept=QA, expected_dept=LEGAL, expected_docs=['POL-LEGAL-002'], should_be_authorized=False
- **EVAL-0134**: "As a general employee outside MGMT, what are the details of the Corporate Governance Policy?" — requester_dept=LEGAL, expected_dept=MGMT, expected_docs=['POL-MGMT-001'], should_be_authorized=False

## cross_department_synthesis (5 scenarios)

- **EVAL-0135**: "How do I get reimbursed for a conference I paid for personally, and does my manager need to approve it?" — requester_dept=FIN, expected_dept=['FIN', 'HR'], expected_docs=['SOP-FIN-001', 'POL-FIN-001'], should_be_authorized=True
- **EVAL-0136**: "A feature I'm building stores new customer personal data — what approvals do I need before launch?" — requester_dept=PROD, expected_dept=['PROD', 'LEGAL'], expected_docs=['SOP-PROD-004', 'SOP-LEGAL-006'], should_be_authorized=True
- **EVAL-0137**: "My laptop won't connect to Wi-Fi during a confidential HR meeting — what do I do?" — requester_dept=IT, expected_dept=['IT', 'HR'], expected_docs=['SOP-IT-006'], should_be_authorized=True
- **EVAL-0138**: "I want to give a customer a bigger discount than I'm authorized for and the deal closes today — what's the process?" — requester_dept=SALES, expected_dept=['SALES', 'FIN'], expected_docs=['SOP-SALES-003-EDGE-B'], should_be_authorized=True
- **EVAL-0139**: "A contractor's engagement is ending — who handles their access and asset return?" — requester_dept=IT, expected_dept=['IT', 'SEC', 'HR'], expected_docs=['SOP-IT-016'], should_be_authorized=True

## ambiguous_query (5 scenarios)

- **EVAL-0140**: "How do I request access?" — requester_dept=UNSPECIFIED, expected_dept=AMBIGUOUS, expected_docs=[], should_be_authorized=True
- **EVAL-0141**: "What's the approval process?" — requester_dept=UNSPECIFIED, expected_dept=AMBIGUOUS, expected_docs=[], should_be_authorized=True
- **EVAL-0142**: "Who do I contact about my request?" — requester_dept=UNSPECIFIED, expected_dept=AMBIGUOUS, expected_docs=[], should_be_authorized=True
- **EVAL-0143**: "How long does reimbursement take?" — requester_dept=UNSPECIFIED, expected_dept=AMBIGUOUS, expected_docs=[], should_be_authorized=True
- **EVAL-0144**: "What's the escalation path?" — requester_dept=UNSPECIFIED, expected_dept=AMBIGUOUS, expected_docs=[], should_be_authorized=True
