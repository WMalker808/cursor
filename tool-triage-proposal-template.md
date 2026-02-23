# New Tool / Feature Triage Proposal (Template)

This template is required for **any** request to build a new internal tool, a major new tool-like subsystem, or a significant new capability in an existing tool.

The intent is to prevent “tool sprawl” by forcing clarity on **need, reuse, ownership, access control, dependencies, and long-term maintenance** (mirroring the patterns in the tools audit).

**Expected effort**: 30–60 minutes to complete.  
**Expected length**: ideally ≤ 2 pages (excluding links).

## Submission gates (must be true to submit)

- [ ] There is a named **Sponsor** who is accountable for the decision and prioritisation.
- [ ] There is a named **Primary owner** who will run/maintain the tool if approved.
- [ ] Internal **reuse/extension** has been checked (Section 3.1), with links.
- [ ] External **buy/partner** has been considered (Section 3.2), with links.
- [ ] A **failure mode / “died tomorrow”** answer exists (Section 5.1).
- [ ] A **decommissioning/consolidation** plan exists (Section 8), even if it’s “none”.

---

## Meta

| Field | Value |
| :---- | :---- |
| **Proposal name** |  |
| **Proposer** |  |
| **Date submitted** |  |
| **Team / department** |  |
| **Sponsor (accountable decision-maker)** |  |
| **Primary owner if approved (team/person)** |  |
| **Primary users** |  |
| **Estimated user count / frequency** |  |

---

## 1) Problem / opportunity (be specific)

- **What is the problem or opportunity?**
- **Who experiences it?** (roles/teams)
- **How often?** (daily/weekly/incident-driven)
- **Evidence**: link to incidents, support tickets, user research, metrics, screenshots, examples.

---

## 2) What happens if we don’t do this?

- **Cost of inaction** (time, editorial impact, revenue risk, compliance/legal risk, morale)
- **Urgency**: why now? any deadlines or external drivers?
- **Workarounds today**: what do people do instead?

---

## 3) Does this already exist? (required checks)

### 3.1 Internal reuse / extension

- **Existing tools checked** (list tools + links, and why they don’t fit):
  - 
  - 
- **Why can’t we extend an existing tool instead of creating a new one?**

### 3.2 External buy / partner

- **External options considered** (vendors/open source/managed services):
  - 
  - 
- **Why is “buy” not viable?** (cost, security, data residency, workflow mismatch, integrations, contract constraints)

### 3.3 Duplication risk

- **Which teams were consulted to confirm no parallel work exists?** (names/teams, date)

---

## 4) Proposed solution (what, not how)

- **What are we proposing?** (build/buy/extend)
- **Core user journeys** (top 3–5 tasks the tool must support)
- **Non-goals** (what we will not do)
- **Dependencies / integrations** (systems, APIs, services, auth, data sources)

---

## 5) Criticality, dependency map, and failure mode

### 5.1 “If it died tomorrow…”

Answer as if you’re on-call and it’s down:

- **What breaks immediately?**
- **Who is blocked?**
- **What manual workaround exists?** (and how long can we tolerate it?)
- **What must be restored first?** (minimum viable service)

### 5.2 Dependents (blast radius)

- **Downstream dependents** (tools/workflows that will rely on this)
- **Upstream dependencies** (services this relies on)
- **Cross-team ownership points** (who owns each dependency)

### 5.3 Organisational criticality (Product view)

- **Business criticality score (1–20)**:
- **Justification** (short, plain English):

### 5.4 Support tier expectation

- **Is 24/7 coverage required?** Yes / No
- If **Yes**, describe why, and what “outage” means (SLO/expectations).

---

## 6) Access control, security, and editorial risk (required)

- **Who should be able to access this?** (roles/groups; least privilege)
- **How will access be granted/removed/audited?**
- **Authentication model** (SSO/Panda/etc.) and any special constraints
- **Permissions model**: are permissions managed centrally (recommended) or per-tool? Why?
- **Data handled** (types, sensitivity, retention):
  - Personal data? Y/N
  - Confidential sources / sensitive investigations? Y/N
  - Rights-managed media? Y/N
- **Worst-case risk if misused or misconfigured** (editorial/legal/security)

---

## 7) Maintenance burden (Engineering view)

Be honest—this is where tool sprawl gets expensive.

- **Expected maintenance burden**: XXS / XS / S / M / L / XL
- **Why that size?** (key drivers: legacy deps, statefulness, integrations, security surface area, UI complexity, data model)
- **Operational requirements**:
  - Monitoring/alerts needed:
  - Runbooks needed:
  - Backups/DR requirements:
  - On-call ownership:
- **Documentation plan** (what must exist before launch)

---

## 8) Lifecycle: adoption, decommissioning, and consolidation (required)

- **Adoption plan**: onboarding, training, comms, support model
- **Success metrics / telemetry plan** (what you will measure, where it’s visible, and who reviews it)
- **What tools/processes does this replace or allow us to retire?**
  - Tool/process to retire:
  - Timeline:
  - Migration approach:
- **Sunset plan**: if usage is low or value isn’t proven, how do we shut it down safely?

---

## 9) Delivery approach and cost (enough detail for a decision)

- **Option A (recommended)**:
  - Scope (MVP):
  - Rough timeline:
  - People/time needed:
  - Key risks:
- **Option B (fallback / cheaper / buy)**:
  - 
- **One-way door?** (what decisions are hard to reverse, e.g. data model, vendor lock-in)

---

## 10) Triage decision (filled in by triage group)

| Field | Value |
| :---- | :---- |
| **Triage date** |  |
| **Members** |  |
| **Decision** | Approve / Reject / Defer / Needs more info |
| **Priority** | Critical / High / Medium / Low |
| **Business criticality (1–20)** |  |
| **Maintenance burden (XXS–XL)** |  |
| **24/7 required** | Yes / No |
| **Rationale** |  |
| **Conditions / next steps** |  |

