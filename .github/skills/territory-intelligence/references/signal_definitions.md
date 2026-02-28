# Signal Definitions & Scoring Reference

## Bot Detection

Email security scanners (Proofpoint, Mimecast, etc.) pre-fetch all links in
emails within seconds of delivery, generating false "engagement" signals.

**Detection rule:** `abs(engaged_at - touched_at) <= 10 seconds` → bot

**Known scanner orgs (from Feb 2026 data):**
- Netomi (12 contacts), 23andMe (8), Masterclass (7), nference (7)
- Amperity (6), Life Fitness (6), Pragma (7), Certinia (3)

Any org where 3+ contacts all show instant engagement has an org-wide scanner.

## Corrected Engagement Score

```
if is_bot:
    score = 0
else:
    recency_decay = 1.0 / (1.0 + (days_since_engagement / 30))
    stage_bonus = 3.0 if Working/Qualified, 1.5 if Contacted, else 0
    phone_bonus = 0.5 if has_phone else 0
    score = raw_score * recency_decay + stage_bonus + phone_bonus
```

## Account Flag Definitions

| Flag | Trigger | Priority |
|------|---------|----------|
| RENEWAL in Nd | Days to renewal ≤ 90 | P0 |
| CfB shrinking | 30d CfB change < -5 | P0 |
| Rev declining | Copilot MoM delta < -$200 | P1 |
| NO COPILOT | 0 CfB seats, >20 GHE | P1 |
| NO GHAS | 0 GHAS seats, >20 GHE | P2 |
| CfB low | CfB attach < 20%, >50 GHE | P2 |
| Low CR | Code Review < 5%, >500 PRs | P2 |
| NO CONTACTS | 0 prospects in Outreach | P1 |
| TEAMS ONLY | Teams seats > 0, GHE = 0 | P2 |
| Persona gaps | Missing buyer/champion/security | P3 |

## Persona Classification

| Persona | Title Keywords | Role in Deal |
|---------|---------------|--------------|
| Economic Buyer | CEO, CTO, CIO, VP, President | Signs the contract |
| Technical Champion | Director, Head of, Principal | Evaluates and recommends |
| Security | Security, SecOps, CISO, InfoSec | GHAS buyer |
| DevOps/Platform | DevOps, Platform, SRE, Infra | Actions/CI buyer |
| Manager/Lead | Manager, Lead, Architect, Staff | Influences team adoption |
| IC | Engineer, Developer | End user |

## Sequence Effectiveness Thresholds

| Advance Rate | Verdict |
|-------------|---------|
| >50% | Top performer — double down |
| 30-50% | Solid — maintain |
| 10-30% | Average — optimize messaging |
| <10% | Underperformer — consider stopping (if n>20) |
| 0% (n>15) | Dead — stop immediately |
