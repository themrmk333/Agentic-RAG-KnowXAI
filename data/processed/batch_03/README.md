# MK-INFINITE-AI PRIVATE LIMITED — Synthetic Enterprise Knowledge Base
### Dataset for Agentic-RAG-KnowXAI (Agentic RAG Enterprise Knowledge Assistant)

> **SYNTHETIC DATA DISCLAIMER:** Every company name, employee, email address, project, ticket, policy figure,
> office location, vendor, and financial amount in this dataset is 100% fictional, generated for the purpose of
> building and evaluating an Agentic-RAG enterprise knowledge assistant. MK-INFINITE-AI PRIVATE LIMITED does not
> represent any real company. No real people, credentials, API keys, or confidential information are included.

---

## 1. Company

**MK-INFINITE-AI PRIVATE LIMITED** is a fictional mid-sized IT/AI company used as the setting for this dataset.
It operates a hybrid workforce across 5 fictional India-based office locations, organized into **18 departments**
covering the full span of a modern enterprise: engineering and product delivery, corporate functions (HR, Finance,
Legal, Procurement, Administration), go-to-market (Sales, Marketing, Customer Support), and governance (PMO,
Management/Leadership), plus specialist functions (Cybersecurity, DevOps & Cloud, QA, Data & Analytics, R&D).

## 2. Departments

| Code | Department | Primary System |
|---|---|---|
| IT | IT Support / Information Technology | MK-ServiceDesk |
| ENG | Software Engineering / Development | MK-CodeForge |
| QA | QA / Testing | MK-TestHub |
| DEVOPS | DevOps & Cloud | MK-CloudOps |
| SEC | Cybersecurity / Information Security | MK-SecGuard |
| HR | Human Resources | MK-HRMS |
| FIN | Finance & Accounting | MK-Finance360 |
| PMO | Project Management / PMO | MK-PMTrack |
| PROD | Product Management | MK-ProductHub |
| SALES | Sales | MK-CRM |
| MKT | Marketing | MK-MarketHub |
| SUPPORT | Customer Support / Helpdesk | MK-SupportDesk |
| LEGAL | Legal & Compliance | MK-LegalVault |
| PROC | Procurement / Purchasing | MK-ProcureX |
| ADMIN | Administration / Facilities | MK-FacilitiesDesk |
| DATA | Data & Analytics | MK-DataLake |
| RND | Research & Development | MK-Labs |
| MGMT | Management / Leadership | MK-ExecDash |

Each department directory (`data/departments/<CODE>/`) contains:
- `department_overview.md` — mission, responsibilities, KPIs, terminology, escalation path, contacts
- `roles.json` — the department's role ladder (Intern → Director) with permissions per level
- `team_roster.md` — synthetic employees in that department
- `troubleshooting/` — standalone diagnostic guides for common issues

`data/sop/<CODE>/` holds 15+ Standard Operating Procedures per department (each with a 7-step procedure,
preconditions, exceptions, escalation, responsible/approval roles, and full metadata).

`data/faq/<CODE>/` holds 25+ FAQs per department in both `faqs.json` (structured, for ingestion) and
`faqs.md` (human-readable, for chunked RAG retrieval), combining SOP-derived how-to questions,
policy-derived "what is X policy" questions, and quick-fact questions (contacts, KPIs, terminology,
escalation paths, cross-department access).

`data/policies/<CODE>/` holds formal company policies with concrete, internally-consistent rules
(e.g., leave entitlements, expense limits, discount authorization tiers, password requirements).

## 3. Roles

"Intern" is treated as an **employment level**, not a department, per the dataset's design requirement.
Every department has its own role ladder from Intern/entry-level through Director, e.g.:

- **IT:** IT Intern → IT Support Engineer → Senior IT Support Engineer → System Administrator →
  Network Administrator → IT Manager → IT Director
- **HR:** HR Intern → HR Executive → HR Specialist → HR Business Partner → HR Team Lead → HR Manager → HR Director
- **Finance:** Finance Intern → Finance Executive → Accountant → Senior Accountant → Finance Lead →
  Finance Manager → Finance Director

Full ladders for all 18 departments are in each department's `roles.json`.

## 4. Projects

Exactly **5 current company projects** are documented under `data/projects/<PROJECT_ID>/`, each with a full
`project.md` (architecture, stack, APIs, AI models, RAG/agent architecture, security, dev/test/deploy/CI-CD
workflows, risks, milestones, backlog, roadmap, terminology) and a `faqs.json` of project-specific Q&As:

1. **PRJ-001** — Agentic RAG Enterprise Knowledge Assistant (the flagship project this dataset supports)
2. **PRJ-002** — Enterprise AI Agent Platform
3. **PRJ-003** — Intelligent Customer Support Automation
4. **PRJ-004** — AI-Powered Business Analytics Platform
5. **PRJ-005** — Secure Computer Vision / Intelligent Automation Platform

## 5. Dataset Structure

```
data/
  company/            company-wide profile (see department overviews for org-wide policies)
  employees/           employees.json, employees.csv (all synthetic employees, interns, contractors)
  departments/<CODE>/  overview, roles, roster, troubleshooting guides
  sop/<CODE>/           15+ SOP markdown documents per department
  faq/<CODE>/           25+ FAQ entries per department (json + md)
  policies/<CODE>/      formal policy documents with authorization metadata
  projects/<PROJECT_ID>/ project documentation + project-specific FAQs
  tickets/              tickets.json, tickets.csv, and per-department ticket markdown samples
  communications/       announcements, meeting summaries
```

## 6. Document Types

JSON, Markdown, and CSV are all used:
- **JSON** — employees, tickets, FAQ collections, roles (structured, ideal for direct ingestion)
- **Markdown** — SOPs, policies, department overviews, troubleshooting guides, project docs, announcements
  (each markdown file embeds a JSON metadata block for consistent schema extraction)
- **CSV** — employees.csv, tickets.csv (flat tabular views)

## 7. Metadata Schema

Every SOP, Policy, Troubleshooting Guide, Project, and Announcement document embeds a JSON metadata block with:

```json
{
  "document_id": "SOP-IT-001",
  "title": "...",
  "document_type": "SOP | Policy | Troubleshooting Guide | Project Documentation | Announcement | ...",
  "department": "...",
  "department_code": "IT",
  "category": "...",
  "subcategory": "...",
  "roles": ["..."],
  "access_level": "general | employee | manager | restricted | management",
  "allowed_departments": ["ALL"] ,
  "confidentiality": "Internal | Confidential | Restricted",
  "keywords": ["..."],
  "created_date": "YYYY-MM-DD",
  "updated_date": "YYYY-MM-DD",
  "version": "1.0",
  "status": "Active",
  "owner": "...",
  "source": "synthetic-generated"
}
```

FAQ JSON objects additionally include: `question`, `short_answer`, `detailed_answer`, `step_by_step`,
`role_applicability`, `difficulty`, `related_documents`, `escalation_path`. SOPs additionally embed
`steps` (as numbered steps in the body), `preconditions`, `exceptions`, `escalation`.

## 8. Access-Control / Authorization Model

Every document carries an `access_level`:

| access_level | Meaning | Example |
|---|---|---|
| `general` | Any employee, any department | HR Leave Policy, IT Password Policy |
| `employee` | Standard employee-facing operational knowledge | Finance Reimbursement Policy |
| `manager` | Manager-level visibility | Budget Approval Policy |
| `restricted` | Narrow, need-to-know | Payroll Administration Policy, Security Incident docs |
| `management` | Director/VP/CEO Office only | Executive Compensation Policy |

**Design principle:** the requester's own department does **not** gate which knowledge they can ask about —
an IT employee can ask about the Leave Policy, and an HR employee can ask how to reset a password. Authorization
is enforced per-document via `access_level`/`allowed_departments`, not by the requester's department. Normal
employee-facing knowledge is `general`/`employee` and cross-department accessible by design; only genuinely
sensitive material (payroll internals, executive compensation, active security incidents, litigation) is
`restricted`/`management`.

## 9. RAG Usage

This dataset is designed for ingestion into **PostgreSQL + pgvector** (or an equivalent vector store) as the
knowledge source for **Agentic-RAG-KnowXAI**:
1. Chunk each markdown/JSON document (SOPs and FAQs are already sized for clean chunking — one SOP or one FAQ
   entry per chunk).
2. Embed chunks and store the metadata block (`access_level`, `department`, `category`, etc.) as row metadata.
3. On a query, run intent detection, dispatch to the relevant department's specialist retrieval agent(s),
   filter candidate chunks by the requester's role/department against each chunk's `access_level`, then
   generate a grounded, cited answer.
4. Cross-department questions should fan out to multiple specialist agents and merge results (see PRJ-001
   documentation for the reference architecture).

## 10. Build Process, Manifest & Scaling

This dataset was generated by a Python pipeline (department content banks → SOP/FAQ/policy template engine →
project/ticket/communication generators) rather than hand-written per document, so it can be extended in further
batches without regenerating existing content. A persistent **`manifest.json`** at the dataset root tracks every
generated document (id, path, type, department, word count, batch) plus running totals (`total_documents`,
`total_words`, `pages_equivalent`, `target_pages_equivalent`).

**Current status (see `manifest.json` and `validation_report.json` for exact figures):**
- Total documents: **3160**
- Total words: **4,110,118**
- Pages-equivalent (400 words/page): **10275.3**
- Target: **10,000 pages-equivalent**

**Batch 1** established every structural minimum in the original specification (18 departments, 15+ SOPs/department,
25+ FAQs/department, policies, troubleshooting guides, cross-department knowledge, authorization metadata, exactly
5 projects, employees/interns/contractors, tickets, communications).

**Batch 2** added *depth*, not repetition, on top of Batch 1 without touching any existing document:
- **566 SOP edge-case addenda** (2 per SOP: "approver unavailable" delegation path, and an "urgent/expedited"
  path with retroactive approval) — genuine procedural variants, not copies.
- **43 policy version-history documents** — one per policy, showing a superseded v1.0, what changed, and the
  effective date of the current version, per the "no contradictions unless versioned" requirement.
- **108 additional troubleshooting scenarios** (6 new, distinct symptoms per department, none overlapping Batch 1).
- **36 approval/escalation scenario narratives** (2 per department: a real escalation-delay walkthrough and a
  policy-exception walkthrough, each with a stated lesson).
- **20 hand-curated difficult cross-department FAQs** — questions specifically designed to require synthesizing
  two or three departments' SOPs/policies (e.g., an Engineer's personal conference-expense reimbursement, a
  Sales urgent-discount edge case, a contractor offboarding spanning IT/Security/HR).
- **30 project-specific technical runbooks** (6 per project) — concrete operational procedures like "Embedding
  Re-index Procedure" and "Fiscal Calendar Date-Range Bug Resolution Procedure" that go beyond the original
  project overview documents.
- **2,700 historical support tickets** spanning an 18-month window (Jan 2025–Aug 2026) across all 18 departments,
  in JSON, CSV, and paginated markdown archives, each tied to a real SOP and a real synthetic employee.
- **68 additional communications**: 30 incident postmortems, 20 release announcements, and 18 monthly all-hands
  recaps spanning the same 18-month history.
- **144 labeled RAG evaluation scenarios** (`data/rag_eval/`) across five types — same-department retrieval,
  cross-department retrieval, authorization-denial cases, multi-department synthesis, and ambiguous queries —
  each with an expected department, expected document IDs, expected access level, and an expected
  authorization outcome, for directly measuring Agentic-RAG-KnowXAI's retrieval and authorization accuracy.

**Batch 3** closed the remaining gap to the 10,000-page-equivalent target through further genuine depth (not
repetition), while leaving every Batch 1 and Batch 2 document byte-identical and untouched:
- **849 additional SOP edge-case documents** — three more edge-case types per existing SOP (system/portal
  unavailable, rejected-or-duplicate-request handling, missing-documentation/incorrect-submission handling),
  on top of Batch 2's approver-unavailable and urgent-path variants — each with situation, detection, decision
  criteria, steps, responsible role, approval, escalation, and expected result, as specified.
- **90 advanced SOPs** — five new procedure categories per department not present in the original SOP lists:
  Business Continuity, Compliance Audit, Role Handoff, Dependency Failure Recovery, and After-Hours Emergency
  Workflow.
- **291 meeting records** with real agenda/discussion/decisions/action-item structure, across all 18
  departments and the 5 projects (sprint reviews).
- **23 additional communications** — training announcements, process changes, operational reminders, quarterly
  updates, and project milestone updates.
- **547 advanced FAQs** — genuine what-if/edge-case questions, policy-interpretation questions (referencing the
  version-history documents), and standard-vs-emergency-path comparison questions, distinctly worded from the
  underlying edge-case/policy documents rather than restating them.
- **32 cross-department scenario narratives** covering 17 of the specified department pairs (IT+HR, IT+Finance,
  Finance+Procurement, Engineering+QA, Engineering+DevOps, Security+IT, Security+Legal, PMO+Engineering,
  PMO+Finance, Product+Engineering, Sales+Legal, Sales+Finance, Marketing+Product, Support+Engineering,
  Support+Product, Data+Management, R&D+Product), each with situation/resolution/lesson.
- **12 process forms** (hardware request, expense claim, contract review, incident report, defect report, etc.)
  explaining required fields and how each is processed.
- **61 authorization test scenarios** plus **144+54 RAG evaluation scenarios** (original + extended v2 with
  `expected_answer`, `expected_citations`, and `reasoning_type` fields) — covering same-department retrieval,
  cross-department retrieval, authorization denial, multi-step reasoning, policy versioning, and ambiguous/
  conflicting-looking questions.
- **180 employee lifecycle workflow records** (onboarding, leave, training, performance, promotion/transfer
  events) for a representative sample of employees, classified Restricted per HR data-handling rules.
- **30 deep project documents** per the 5 existing projects (6 each: Disaster Recovery Plan, Operational
  Checklist, Architecture Decision Record, Integration Procedure, Failure Scenario Playbook, Monitoring &
  Alerting Procedure) — no 6th project was created; all five original projects remain the only current projects.
- **2,718 additional historical tickets** (calibration batch + wave 2) with genuinely differentiated
  investigation, root-cause, verification, and prevention fields drawn from cause banks keyed to each SOP's
  underlying workflow shape — not simply ID-varied copies of earlier tickets.

**Final cumulative status (see `manifest.json` and `validation_report.json` for exact figures):**
- Total documents: **3160**
- Total words: **4,110,118**
- Pages-equivalent (400 words/page): **10275.3**
- Target: **10,000 pages-equivalent — reached**
- 32 total batches, zero duplicate document IDs, all Batch 1/2 documents verified byte-intact by spot-check
  (see `validation_report.json`)

The methodology never changed to hit this number: every batch added a new, named content category (edge-case
types, advanced SOPs, meetings, forms, scenarios, lifecycle records, deep project docs, richer tickets) rather
than re-running earlier generators with different random seeds. The historical ticket archive is the single
largest contributor by design — real enterprise ticketing systems are naturally the highest-volume knowledge
category — but each ticket carries genuine, differentiated investigation/root-cause/prevention content rather
than templated filler.

## 11. Validation

`validation_report.json` (generated by `validate.py`) checks, per department: overview/roles/SOP/FAQ presence
and minimums, 7-step SOP structure, cross-department answerability of representative test questions, presence
of authorization metadata with multiple access levels, exactly 5 projects, no department literally named
"Intern", absence of any API-key/secret/private-key patterns, and non-trivial document length. All checks
passed for Batch 1.

## 12. Synthetic-Data Disclaimer

All content — company name, employees, emails, projects, tickets, policies, financial figures, office
locations, vendors, and clients — is synthetic and fictional, generated specifically for the
Agentic-RAG-KnowXAI evaluation project. No real individuals, real companies, real credentials, or real
confidential data are represented anywhere in this dataset.
