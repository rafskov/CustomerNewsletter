---
name: territory-intelligence
description: >
  Generates strategic territory intelligence briefings by synthesizing
  structured data from the territory_intel.py pipeline (engagement scores,
  revenue trends, PR adoption, book-level adoption, multi-threading maps)
  into narrative account plans, call lists, and executive summaries.
metadata:
  category: sales-enablement
  phase: "6"
  inputs:
    - territory_intel_{date}.json (from territory_intel.py)
  outputs:
    - territory_briefing_{date}.md (narrative briefing)
    - weekly_call_list_{date}.md (prioritized call list with talk tracks)
---

# Skill: Territory Intelligence (Phase 6)

## Purpose

Transform raw territory data into actionable sales intelligence. This skill
consumes the structured JSON output from `territory_intel.py` and generates
narrative briefings that combine quantitative signals with strategic judgment.

## Quick Start

1. Run `territory_intel.py` with fresh CSV exports → produces `territory_intel_{date}.json`
2. Feed the JSON to this skill
3. Specify output type: `briefing`, `call_list`, or `account_plan`
4. Skill generates markdown output with strategic recommendations

## Core Workflow

### Input: `territory_intel_{date}.json`

The JSON artifact contains:
- `scorecards[]` — account-level scorecards with flags, adoption metrics, contacts
- `copilot_trends` — MoM revenue trends per account
- `actions_trends` — MoM Actions revenue trends
- `pr_adoption` — PR/Code Review adoption rates
- `threading` — multi-threading persona coverage maps
- `sequences` — sequence effectiveness analysis
- `prospect_summary` — bot detection stats

### Output Types

#### 1. Territory Briefing (`briefing`)
Weekly executive summary covering:
- Book snapshot (ARR, seats, attach rates)
- Top 8 priority accounts with combined signals and specific actions
- Territory health metrics (Copilot attach, GHAS attach, renewal risk)
- Strategic moves (ranked by impact)

**Tone:** Direct, data-driven, action-oriented. Every account gets a specific
"Action:" recommendation, not a generic suggestion.

#### 2. Weekly Call List (`call_list`)
Prioritized call list for the week:
- Ordered by urgency (renewal proximity × flag count × engagement score)
- Each entry includes: who to call, why now, what to say, what to ask for
- Groups contacts by account for multi-threading
- Excludes bot-engaged contacts

**Tone:** Tactical. Phone-ready. Include specific numbers the rep can reference
in the conversation.

#### 3. Account Plan (`account_plan`)
Deep dive on a single account:
- Full product adoption breakdown
- Revenue trajectory with MoM chart
- Org chart / threading map with persona gaps
- PR/Code Review adoption detail
- Hiring signals (if available)
- 30/60/90 day action plan

## Signal Hierarchy

When combining signals, weight them in this order:

1. **Renewal proximity** — anything within 90 days is urgent
2. **Seat movement** — CfB/GHAS shrinking = immediate risk
3. **Revenue trend** — declining MoM = churn signal
4. **Engagement quality** — corrected scores (bot-filtered), not raw
5. **Adoption gaps** — 0% CfB on 400 GHE seats = expansion opp
6. **Persona coverage** — no security contact = can't sell GHAS
7. **Hiring signals** — growing eng team = budget exists
8. **PR adoption** — low Code Review % = enablement conversation

## Critical Rules

- L01: NEVER use raw Outreach engagement scores. Always use corrected scores from the pipeline (bot-filtered, recency-decayed).
- L02: Flag any account with >$50K ARR and zero Outreach contacts as a coverage emergency.
- L03: Copilot seats shrinking into a renewal (within 90 days) is the highest-priority flag.
- L04: When an account has both growing and declining products, lead with the growth story and investigate the decline separately.
- L05: Multi-threading recommendations must be specific: "prospect into CISO" not "add more contacts."
- L06: Every account recommendation must include a concrete next action with a named contact (or "need net-new contacts" if none exist).
- L07: Sequence recommendations should cite the advance rate and sample size. Never recommend stopping a sequence with n<10.
