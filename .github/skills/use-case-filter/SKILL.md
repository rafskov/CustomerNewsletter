---
name: use-case-filter
description: "Extracts use-case-specific briefings from assembled newsletters. Use after Phase 4.5. Produces filtered, customer-ready views for scenarios like legacy migration, security compliance, developer productivity. Keywords: use case, filter, briefing, customer scenario, legacy migration."
metadata:
  category: domain
  phase: "5b"
---

# Use-Case Filter

Extract use-case-specific briefings from assembled newsletters, producing filtered, customer-ready views.

## Quick Start

1. Read assembled newsletter from `output/YYYY-MM_*_newsletter.md`
2. Read use-case definitions from `.github/skills/use-case-filter/references/use_case_definitions.yaml`
3. For each defined use case, scan newsletter items for matching signals
4. Assemble matched items into a focused briefing with use-case-specific framing
5. Write briefings to `output/briefings/YYYY-MM_<use_case_id>.md`

## Inputs

- **Assembled Newsletter**: `output/YYYY-MM_*_newsletter.md` (required)
- **Use-Case Definitions**: `.github/skills/use-case-filter/references/use_case_definitions.yaml` (required)
- **Archived Newsletters**: `archive/` (optional, for cross-issue analysis)

## Output

- **Directory**: `output/briefings/`
- **Files**: One file per use case that has >= 3 matching items
- **Naming**: `YYYY-MM_<use_case_id>.md` (e.g., `2026-02_legacy_migration.md`)
- **Content**: Customer-ready briefing with use-case-specific intro, matched items with context, and action-oriented closing

## Core Workflow

### Step 1: Load Use-Case Definitions

Read `references/use_case_definitions.yaml`. Each use case defines:
- `id`: kebab-case identifier
- `name`: Human-readable title
- `description`: One-line customer-facing description
- `audience`: Who this briefing targets
- `signals`: Keywords, feature categories, and patterns that indicate relevance
- `framing`: How to contextualize matched items for this use case

### Step 2: Parse Newsletter Into Items

Break the assembled newsletter into discrete items (bullets). For each item, extract:
- Section heading it belongs to (Copilot, Enterprise, Platform, etc.)
- Feature name and GA/PREVIEW status
- Description text
- Links
- Original formatting

### Step 3: Match Items to Use Cases

For each use case, scan all newsletter items for signal matches:

**Signal matching rules (in priority order):**
1. **Explicit keyword match** (3x weight) — item text contains a signal keyword
2. **Category match** (2x weight) — item's section aligns with use-case categories
3. **Capability match** (1.5x weight) — item describes a capability relevant to the use case (e.g., agent mode → migration tooling)
4. **Adjacency match** (1x weight) — item is closely related to a matched item (e.g., model availability supports agent usage)

An item can appear in multiple use-case briefings.

**Minimum threshold**: A use case must have >= 3 matched items to produce a briefing. Otherwise, skip it silently.

### Step 4: Assemble Briefings

For each qualifying use case, produce a briefing document:

```markdown
# [Use Case Name]: [Month Year] GitHub Updates

[1-2 sentence intro framing why these updates matter for this use case]

---

## Key Updates

[Matched items, re-ordered by relevance to the use case]
[Preserve original formatting: bold terms, GA/PREVIEW labels, links]
[Add a brief "Why this matters" annotation when the connection isn't obvious]

---

## Recommended Actions

[2-4 concrete next steps based on the matched items]

---

*This briefing was filtered from the [full February 2026 newsletter](../YYYY-MM_month_newsletter.md). For all updates, see the complete issue.*
```

### Step 5: Generate Index

Write `output/briefings/INDEX.md` summarizing all generated briefings:

```markdown
# Use-Case Briefings: [Month Year]

| Use Case | Items | Briefing |
|----------|-------|----------|
| Legacy Codebase Migration | 8 | [View](2026-02_legacy_migration.md) |
| Security & Compliance | 6 | [View](2026-02_security_compliance.md) |
```

### Step 6: Quality Check

Before writing output:
- [ ] Each briefing has >= 3 matched items
- [ ] Items preserve original formatting (bold, links, labels)
- [ ] Intro framing is specific to the use case (not generic)
- [ ] "Why this matters" annotations added for non-obvious matches
- [ ] Recommended Actions are concrete and actionable
- [ ] Links back to full newsletter are correct
- [ ] INDEX.md is accurate and complete
- [ ] No Copilot Free/Individual/Pro/Pro+ mentions
- [ ] Enterprise focus maintained

## Reference

- [Use-Case Definitions](references/use_case_definitions.yaml) — Defined customer scenarios and matching signals
- [Briefing Format Spec](references/briefing_format_spec.md) — Output format and style guide
- [Example: Legacy Migration](examples/legacy_migration_briefing.md) — Known-good example output

## Done When

- [ ] Briefing files exist at `output/briefings/YYYY-MM_<use_case_id>.md` for each qualifying use case
- [ ] INDEX.md exists at `output/briefings/INDEX.md`
- [ ] Each briefing has >= 3 items with proper formatting
- [ ] Each briefing has use-case-specific intro and recommended actions
- [ ] Full newsletter link is correct in each briefing
