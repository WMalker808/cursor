# New Tool / Feature Triage (Short Form)

Use this for **any request** to build a new tool (or a major tool-like capability).  
Goal: reduce tool sprawl by requiring the **minimum** answers we need to make a good decision (based on the tools audit themes: reuse, criticality, access control, dependents, and maintenance burden).

**Expected effort**: 10–20 minutes. **Target length**: ~1 page (+ links).

## Submission gates (must be true to submit)

- [ ] Named **Sponsor** (accountable decision-maker).
- [ ] Named **Owner** (team/person who will run it after launch).
- [ ] Internal **reuse/extend** checked (links).
- [ ] External **buy/partner** checked (links).
- [ ] **“If it died tomorrow”** answered (workaround + tolerance).
- [ ] **Sunset/retire** plan stated (even if “none”).

---

## 1) Meta

| Field | Value |
| :---- | :---- |
| **Proposal name** |  |
| **Proposer** |  |
| **Date submitted** |  |
| **Team / department** |  |
| **Sponsor (accountable decision-maker)** |  |
| **Owner if approved (team/person)** |  |
| **Primary users** |  |
| **Estimated user count / frequency** |  |

---

## 2) Problem (and evidence)

- **What is the problem?** (1–3 sentences)
- **Who is affected + how often?**
- **Evidence** (at least one): incident, ticket, user quotes, metrics, screenshots, examples.

---

## 3) If we do nothing

- **Cost of inaction** (time, editorial, revenue, compliance/legal).
- **Urgency**: why now? any deadlines?
- **Current workaround** (1–2 sentences).

---

## 4) Reuse / buy checks (links required)

### 4.1 Reuse or extend an existing internal tool

- Tools checked (links + 1-line reason each):
  - 
  - 
- Why extension isn’t sufficient (1–3 bullets):
  -

### 4.2 Buy / partner externally

- Options checked (links + 1-line reason each):
  - 
  - 
- Why “buy” isn’t viable (1–3 bullets):
  -

### 4.3 Duplication risk

- Teams consulted to confirm no parallel work (names/teams + date):
  -

---

## 5) Proposed solution (what you want, not implementation)

- **What are we proposing?** Build / Extend / Buy
- **Top 3 user tasks** it must support:
  1. 
  2. 
  3. 
- **Key dependencies/integrations** (names only):
  -

---

## 6) Criticality + failure mode (audit-style)

### 6.1 “If it died tomorrow…”

- What breaks + who is blocked (1–2 sentences):
- Manual workaround + how long we can tolerate it:
- Minimum thing to restore first:

### 6.2 Dependents / blast radius

- **Downstream dependents** (what will rely on this):
  -
- **Upstream dependencies** (what it relies on):
  -

### 6.3 Business criticality (1–20)

- Score:
- 1–2 sentence justification:

### 6.4 Support expectation

- 24/7 required? Yes / No
- If yes, define “outage” + expected response time:

---

## 7) Access control + risk (required)

- Who can access (roles/groups; least privilege):
- How access is granted/removed/audited:
- Auth model (SSO/Panda/etc.):
- Permissions model: Central / Per-tool (why):
- Data handled:
  - Personal data? Y/N
  - Confidential sources / sensitive investigations? Y/N
  - Rights-managed media? Y/N
- Worst-case risk if misused/misconfigured (1–2 sentences):

---

## 8) Maintenance burden (Engineering view)

- Burden: XXS / XS / S / M / L / XL
- Why (1–3 bullets):
  -
- Who is on the hook for ops/on-call? (team/person):

---

## 9) Lifecycle (required)

- Adoption (who will roll it out, how users learn it?):
- Success metric (pick 1–2) + where we’ll measure it:
- Replaces/retire anything? (what + when):
- Sunset plan (how to shut down safely if it’s not used/valuable):

---

## 10) Rough cost (enough for a decision)

- MVP scope (3–5 bullets):
  -
- Timeline (rough):
- People needed (rough):
- One-way door / lock-in risk? (1 sentence):

---

## 11) Triage decision (filled in by triage group)

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

