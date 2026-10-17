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
- Total documents: **500**
- Total words: **467,351**
- Pages-equivalent (400 words/page): **1168.4**
- Target: **10,000 pages-equivalent**

This is **Batch 1**, and it satisfies every structural minimum in the original specification (18 departments,
15+ SOPs/department, 25+ FAQs/department, policies, troubleshooting guides, cross-department knowledge,
authorization metadata, exactly 5 projects, employees/interns/contractors, tickets, communications). It does
**not yet** reach the 10,000-page-equivalent target — reaching that volume with genuinely distinct,
non-repetitive enterprise content requires additional sequential batches (e.g., deeper per-department SOP/FAQ
expansion, a larger ticket history, more communications/meeting archives, additional synthetic employees).
The manifest is structured precisely so that a future batch can `load_manifest()`, skip any `document_id`
already present, and append new documents without duplication or regeneration.

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