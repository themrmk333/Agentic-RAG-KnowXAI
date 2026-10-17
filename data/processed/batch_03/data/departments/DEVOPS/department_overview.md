# DevOps & Cloud — Department Overview

**Department Code:** DEVOPS  
**Primary System:** MK-CloudOps  
**Owner:** DevOps Director

## Overview

The DevOps & Cloud department at MK-INFINITE-AI PRIVATE LIMITED is responsible for: Provide reliable, automated, secure infrastructure and deployment pipelines. This department operates using MK-CloudOps as its primary system of record for department workflows, and coordinates with other departments on cross-functional processes described in the individual SOP documents.

## Department Responsibilities

- Build and operate CI/CD pipelines for all engineering teams.
- Provision, configure, and monitor cloud infrastructure.
- Own incident response for infrastructure-level production issues.
- Manage cost optimization and capacity planning for cloud resources.
- Maintain infrastructure-as-code and disaster recovery readiness.

## Organizational Structure & Roles

The department follows the following role ladder, from entry-level to leadership:

| Level | Role | Permissions |
|---|---|---|
| 1 | DevOps Intern | Read-only access to standard department tools; cannot approve requests; requires mentor sign-off on deliverables. |
| 2 | DevOps Engineer | Standard operational access to department systems; can execute assigned workflows; cannot approve budget or policy exceptions. |
| 3 | Senior DevOps Engineer | Standard operational access to department systems; can execute assigned workflows; cannot approve budget or policy exceptions. |
| 4 | Site Reliability Engineer | Standard operational access to department systems; can execute assigned workflows; cannot approve budget or policy exceptions. |
| 5 | Cloud Architect | Can approve first-line requests within delegated authority limits; escalates high-value or high-risk items upward. |
| 6 | DevOps Manager | Can approve first-line requests within delegated authority limits; escalates high-value or high-risk items upward. |
| 7 | DevOps Director | Full department authority including budget approval, policy exceptions, and escalation resolution; reports to the next level of Management. |

## Key Performance Indicators (KPIs)

- Deployment frequency (target: multiple deployments per week per service)
- Change failure rate (target: under 10%)
- Mean time to recovery (MTTR) (target: under 1 hour for Sev-1)
- Infrastructure cost variance (target: within 5% of forecast)

## Department Terminology

| Term | Definition |
|---|---|
| MK-CloudOps | The internal cloud infrastructure management and monitoring console. |
| IaC | Infrastructure as Code, defining infrastructure through version-controlled scripts. |
| MTTR | Mean Time To Recovery, the average time to restore service after an incident. |
| Blue-Green Deployment | A release strategy running two environments to minimize downtime. |
| On-call | A rotating responsibility for responding to production incidents outside business hours. |

## Common Mistakes to Avoid

- Making manual changes directly in production instead of through the IaC pipeline.
- Deploying without a tested rollback plan.
- Not updating monitoring alerts when a new service is introduced.

## Escalation Path

DevOps Engineer → DevOps Manager → DevOps Director

## Department Contacts (Synthetic)

| Name | Email | Role |
|---|---|---|
| Siddharth Menon | siddharth.menon@mkinfinite-ai.com | DevOps Manager |
| Isha Bhatt | isha.bhatt@mkinfinite-ai.com | Cloud Architect |

## Cross-Department Note

Employees in **any** department may ask DevOps & Cloud questions — department SOPs, FAQs, and troubleshooting guides are retrievable regardless of the requester's own department, subject to the access-level and confidentiality controls defined on each document (see `document metadata`).

_This document is 100% synthetic content generated for the Agentic-RAG-KnowXAI evaluation dataset._
