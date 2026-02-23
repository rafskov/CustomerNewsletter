# Briefing Format Specification

## File Naming

`YYYY-MM_<use_case_id>.md`

Example: `2026-02_legacy_migration.md`

## Structure

```markdown
# [Use Case Name]: [Month Year] GitHub Updates

[1-2 sentence intro. Use the `framing` text from use_case_definitions.yaml as a base,
then tailor to the specific matched items found this month.]

---

## Key Updates

[Matched items grouped by theme, not by original newsletter section.
Each item preserves its original formatting: bold terms, GA/PREVIEW labels, links.
Add a brief italic "Why this matters for [use case]" annotation when the
connection between the item and the use case isn't immediately obvious.]

---

## Recommended Actions

[2-4 concrete, numbered next steps. Each should reference a specific item above
and include a link. Focus on what the customer should DO, not just be aware of.]

---

*This briefing was filtered from the [full [Month Year] newsletter](../YYYY-MM_month_newsletter.md). For all updates, see the complete issue.*
```

## Formatting Rules

- Preserve all original item formatting (bold, links, labels)
- Do not add new links that weren't in the original newsletter
- Use the same professional-but-conversational tone as the main newsletter
- "Why this matters" annotations are italic and 1 sentence max
- Recommended Actions are numbered, not bulleted
- No Copilot Free/Individual/Pro/Pro+ mentions
- Enterprise focus throughout

## Grouping Rules

Items in the briefing should be re-ordered by relevance to the use case, not by their
original newsletter section. Group related items together under thematic subheadings
when 3+ items share a theme.

## Minimum Viable Briefing

A briefing must have:
- >= 3 matched items
- A use-case-specific intro (not just the generic framing text)
- At least 2 recommended actions
- The footer link back to the full newsletter
