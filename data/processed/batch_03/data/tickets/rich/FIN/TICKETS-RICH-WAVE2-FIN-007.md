# Finance & Accounting — Rich Historical Ticket Archive (wave2, Page 7)

## TCK3-FIN-00147 — Payroll (P4, Resolved)
**Created:** 2026-06-25 via Portal  |  **Requester:** Kabir Reddy  |  **Assigned to:** Arjun Chowdhury

**Description:** Kabir Reddy (QA / Testing) reported an issue via Portal related to 'Salary Advance Request Procedure'. Category: Payroll. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Salary Advance Request Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-FIN-016 to resolve. the employee logs into MK-Finance360 and navigates to the 'Salary Advance Request' section. the employee selects 'New Salary Advance Request' and enters the required details, including reason for advance and requested repayment schedule. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Salary Advance Request; MK-Finance360 automatically routes it to the HR Business Partner for review. The HR Business Partner reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-FIN-016

---

## TCK3-FIN-00030 — Payroll (P2, Closed)
**Created:** 2026-07-01 via Walk-in  |  **Requester:** Aditya Nair  |  **Assigned to:** Aditya Sharma

**Description:** Aditya Nair (Administration / Facilities) reported an issue via Walk-in related to 'Payroll Processing Procedure'. Category: Payroll. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Payroll Processing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-FIN-008 to resolve. the Accountant confirms eligibility and prerequisites: validating attendance, leave deductions, and statutory contributions. the Accountant raises a request in MK-Finance360 specifying exactly which Payroll Run is required. The Finance Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Payroll Run in the relevant system. the Accountant is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-FIN-008

---

## TCK3-FIN-00065 — Procurement Finance (P3, Resolved)
**Created:** 2026-07-04 via Email  |  **Requester:** Ananya Nair  |  **Assigned to:** Divya Joshi

**Description:** Ananya Nair (IT Support / Information Technology) reported an issue via Email related to 'Purchase Approval Procedure'. Category: Procurement Finance. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Purchase Approval Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The approver was on leave and no delegate had been assigned, causing the request to stall.

**Resolution:** Followed SOP-FIN-003 to resolve. the employee logs into MK-Finance360 and navigates to the 'Purchase Request' section. the employee selects 'New Purchase Request' and enters the required details, including vendor quote, budget line, and cost centre. the employee attaches any supporting documentation and reviews the entry for accuracy before submitting. the employee submits the Purchase Request; MK-Finance360 automatically routes it to the Finance Manager for review. The Finance Manager reviews the request against company policy and either approves, rejects, or returns it for clarification.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Added a validation check to catch this class of issue automatically before submission.

**Related SOP:** SOP-FIN-003

---

## TCK3-FIN-00094 — Vendor Management (P3, Resolved)
**Created:** 2026-07-09 via Portal  |  **Requester:** Manoj Sharma  |  **Assigned to:** Manoj Desai

**Description:** Manoj Sharma (Research & Development) reported an issue via Portal related to 'Vendor Onboarding (Finance Steps)'. Category: Vendor Management. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Vendor Onboarding (Finance Steps)', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-FIN-013 to resolve. the Finance Executive confirms eligibility and prerequisites: PAN/GST verification and bank account confirmation. the Finance Executive raises a request in MK-Finance360 specifying exactly which Vendor Master Record is required. The Finance Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Vendor Master Record in the relevant system. the Finance Executive is notified and asked to test and verify the access or functionality.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-FIN-013

---

## TCK3-FIN-00114 — Internship (P3, Resolved)
**Created:** 2026-07-20 via Slack  |  **Requester:** Isha Iyer  |  **Assigned to:** Simran Malhotra

**Description:** Isha Iyer (Data & Analytics) reported an issue via Slack related to 'Finance Intern Onboarding Procedure'. Category: Internship. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Finance Intern Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-FIN-015 to resolve. HR notifies the relevant department and the MK-Finance360 owner ahead of the employee's start or end date. the Finance Executive prepares the required Finance Intern Onboarding, including MK-Finance360 read-only access and confidentiality agreement. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Finance Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-FIN-015

---

## TCK3-FIN-00052 — Accounts Payable (P3, Resolved)
**Created:** 2026-07-25 via Phone  |  **Requester:** Aman Verma  |  **Assigned to:** Manoj Desai

**Description:** Aman Verma (Research & Development) reported an issue via Phone related to 'Invoice Processing Procedure'. Category: Accounts Payable. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Invoice Processing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-FIN-004 to resolve. the Accountant confirms eligibility and prerequisites: a three-way match against the purchase order and goods receipt. the Accountant raises a request in MK-Finance360 specifying exactly which Vendor Invoice is required. The Finance Lead reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Vendor Invoice in the relevant system. the Accountant is notified and asked to test and verify the access or functionality.

**Verification:** The fix was verified against the original reported symptom before closing.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-FIN-004

---

## TCK3-FIN-00100 — Fixed Assets (P3, Resolved)
**Created:** 2026-07-27 via Email  |  **Requester:** Rahul Verma  |  **Assigned to:** Aditya Sharma

**Description:** Rahul Verma (Legal & Compliance) reported an issue via Email related to 'Fixed Asset Capitalization Procedure'. Category: Fixed Assets. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Fixed Asset Capitalization Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The requester's underlying prerequisite (e.g., a linked account) wasn't fully set up before this request was submitted.

**Resolution:** Followed SOP-FIN-011 to resolve. the Accountant confirms eligibility and prerequisites: invoice, useful life estimate, and depreciation method. the Accountant raises a request in MK-Finance360 specifying exactly which Asset Capitalization is required. The Finance Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Asset Capitalization in the relevant system. the Accountant is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-FIN-011

---

## TCK3-FIN-00046 — Internship (P4, Resolved)
**Created:** 2026-07-31 via Phone  |  **Requester:** Kavya Bhatt  |  **Assigned to:** Alisha Rao

**Description:** Kavya Bhatt (Procurement / Purchasing) reported an issue via Phone related to 'Finance Intern Onboarding Procedure'. Category: Internship. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Finance Intern Onboarding Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The employee's status change hadn't yet propagated from the source system to this one.

**Resolution:** Followed SOP-FIN-015 to resolve. HR notifies the relevant department and the MK-Finance360 owner ahead of the employee's start or end date. the Finance Executive prepares the required Finance Intern Onboarding, including MK-Finance360 read-only access and confidentiality agreement. Access, equipment, or accounts are provisioned (onboarding) or scheduled for deactivation (offboarding). The Finance Manager verifies that every item on the checklist is complete. The employee, or their manager for offboarding cases, confirms receipt or completion.

**Verification:** A follow-up check one business day later confirmed the issue had not recurred.

**Prevention:** Updated the handover/checklist template to make the missed step explicit and mandatory.

**Related SOP:** SOP-FIN-015

---

## TCK3-FIN-00142 — Payroll (P3, Closed)
**Created:** 2026-08-06 via Portal  |  **Requester:** Kabir Agarwal  |  **Assigned to:** Swati Nair

**Description:** Kabir Agarwal (Customer Support / Helpdesk) reported an issue via Portal related to 'Payroll Processing Procedure'. Category: Payroll. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Payroll Processing Procedure', and checked recent related changes before identifying the cause below.

**Root Cause:** The target system had reached a soft capacity limit that blocked new provisioning until cleared.

**Resolution:** Followed SOP-FIN-008 to resolve. the Accountant confirms eligibility and prerequisites: validating attendance, leave deductions, and statutory contributions. the Accountant raises a request in MK-Finance360 specifying exactly which Payroll Run is required. The Finance Manager reviews and approves the request, applying least-privilege / need-basis principles. Once approved, the assigned engineer provisions or configures the Payroll Run in the relevant system. the Accountant is notified and asked to test and verify the access or functionality.

**Verification:** The requester confirmed the fix resolved the issue and closed the ticket satisfied.

**Prevention:** Updated the provisioning automation to fail loudly rather than silently on this condition.

**Related SOP:** SOP-FIN-008

---

## TCK3-FIN-00072 — Expense Reimbursement (P2, Resolved)
**Created:** 2026-08-17 via Portal  |  **Requester:** Siddharth Reddy  |  **Assigned to:** Kavya Iyer

**Description:** Siddharth Reddy (Human Resources) reported an issue via Portal related to 'Corporate Credit Card Reconciliation'. Category: Expense Reimbursement. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Corporate Credit Card Reconciliation', and checked recent related changes before identifying the cause below.

**Root Cause:** The review sample missed this specific case due to how the sample was selected.

**Resolution:** Followed SOP-FIN-012 to resolve. The review is scheduled in advance and stakeholders are notified through MK-Finance360. the Finance Executive gathers the required data and documents, including matching each transaction to a submitted receipt. The review team examines the Card Statement Reconciliation against the applicable policy or checklist. Gaps, risks, or non-conformities are documented with a severity rating and an owner assigned. The Finance Lead discusses the findings with the relevant department and agrees remediation actions.

**Verification:** The assigned specialist re-tested the exact original scenario to confirm resolution.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-FIN-012

---

## TCK3-FIN-00105 — Expense Reimbursement (P4, In Progress)
**Created:** 2026-08-17 via Live Chat  |  **Requester:** Arjun Verma  |  **Assigned to:** Divya Joshi

**Description:** Arjun Verma (Administration / Facilities) reported an issue via Live Chat related to 'Corporate Credit Card Reconciliation'. Category: Expense Reimbursement. Logged against MK-Finance360.

**Investigation:** The assigned specialist reviewed the MK-Finance360 record, confirmed the reported symptom against 'Corporate Credit Card Reconciliation', and checked recent related changes before identifying the cause below.

**Root Cause:** An owner was not clearly assigned for this specific check, so it fell through the cracks.

**Resolution:** Root cause identified; fix in progress, next update pending.

**Verification:** Pending — will be confirmed once the fix is deployed.

**Prevention:** Added the missed check explicitly to the next review cycle's checklist with a named owner.

**Related SOP:** SOP-FIN-012

---
