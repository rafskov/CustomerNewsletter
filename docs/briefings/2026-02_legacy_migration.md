# Legacy Codebase Migration: February 2026 GitHub Updates

This month brings a wave of capabilities directly useful for large-scale codebase modernization. Third-party coding agents (Claude and Codex) are now available alongside GitHub's own, giving migration teams the ability to pick the best agent for each task. VS Code has evolved into a multi-agent orchestration hub with parallel subagents, plan mode, and persistent memory, all of which support structured, multi-step migration workflows. If your team is planning or executing a legacy modernization effort, these are the updates to pay attention to.

---

## Key Updates

### Agents & Orchestration for Migration Workflows

-   **Third-Party Agents on Agent HQ (`PREVIEW`)** -- Claude by Anthropic and OpenAI Codex are now available in public preview directly on GitHub and VS Code. Enterprise subscribers can choose between GitHub's own Coding Agent, Claude, or Codex, selecting the best tool for each task. No additional cost, existing terms apply, consuming the same premium request units (PRUs). - [Changelog](https://github.blog/changelog/2026-02-04-claude-and-codex-are-now-available-in-public-preview-on-github) | [GitHub Blog](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)

    *Why this matters for migration: Different agents excel at different languages and patterns. Teams migrating heterogeneous codebases can use Claude for reasoning-heavy refactoring and Codex for bulk code transformation.*

-   **Copilot CLI and SDK (`PREVIEW`)** -- The Copilot CLI now includes [Plan mode](https://github.blog/changelog/2026-01-21-github-copilot-cli-plan-before-you-build-steer-as-you-go) for structured task planning with clarifying questions before code is written, [autopilot mode](https://github.com/github/copilot-cli/releases/tag/v0.0.400) for autonomous task completion, and [repository memory](https://github.blog/changelog/2026-01-21-github-copilot-cli-plan-before-you-build-steer-as-you-go) across sessions. The new [Copilot SDK](https://github.blog/changelog/2026-01-14-copilot-sdk-in-technical-preview) (technical preview) provides language-specific libraries for Node.js/TypeScript, Python, Go, and .NET, enabling platform teams to embed Copilot capabilities into migration tooling. - [CLI Releases](https://github.com/github/copilot-cli/releases) | [SDK Video (45m)](https://www.youtube.com/watch?v=LO7nf-dbURE)

    *Why this matters for migration: Plan mode lets you describe a migration task in plain language, get a structured plan with clarifying questions, then execute. Memory means the agent retains context about your codebase conventions across sessions.*

-   **Parallel Subagents** -- Subagents run in parallel with dedicated context windows, significantly speeding up complex tasks. Each subagent operates autonomously and returns only a summary to the main agent, reducing token usage. - [Release Notes](https://code.visualstudio.com/updates/v1_109#_subagents) | [Docs](https://code.visualstudio.com/docs/copilot/agents/subagents) | [Video (25m)](https://www.youtube.com/watch?v=GMAoTeD9siU)

    *Why this matters for migration: Decompose large migration tasks into parallel subtasks (e.g., one subagent handles API layer, another handles data models, another handles tests).*

-   **GitHub Agentic Workflows (`PREVIEW`)** -- [GitHub Agentic Workflows](https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/) let you write GitHub Actions automation in plain Markdown and let AI agents handle intelligent decision-making for CI failure analysis and repository maintenance. The [gh-aw framework](https://github.com/github/gh-aw) includes 50+ operational workflow examples. - [Documentation](https://github.github.io/gh-aw/) | [Video (1m)](https://www.youtube.com/watch?v=3_i03fGXs9U)

    *Why this matters for migration: Automate post-migration validation, regression testing, and continuous improvement workflows with AI-driven analysis.*

### Code Review & Quality During Migration

-   **Copilot Code Review (`GA`)** -- Organization members can now use Copilot code review on pull requests even without a Copilot license, expanding adoption across the entire team. - [Changelog](https://github.blog/changelog/2025-12-17-copilot-code-review-now-available-for-organization-members-without-a-license) | [Docs](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review)

    *Why this matters for migration: Large migrations generate many PRs. AI-assisted code review catches issues across the full team without requiring every developer to have a Copilot license.*

-   **Agent Skills (`GA`)** -- Agent Skills are now generally available and enabled by default in VS Code. Skills are also available as [slash commands](https://code.visualstudio.com/updates/v1_109#_use-skills-as-slash-commands). New [Agent Hooks](https://code.visualstudio.com/updates/v1_109#_agent-hooks-preview) (`PREVIEW`) let you run custom shell commands at key agent lifecycle points, enabling deterministic security policy enforcement and code quality gates. - [Changelog](https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills) | [Skills Docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills) | [Hooks Docs](https://code.visualstudio.com/docs/copilot/customization/hooks)

    *Why this matters for migration: Create reusable migration skills (e.g., "migrate-dao-to-repository-pattern") and enforce quality gates with hooks that run linters and tests after every agent change.*

-   **C++ Code Editing Tools (`PREVIEW`)** -- Copilot gains specialized code editing tools for C++ projects, improving the agent's ability to navigate and edit C++ codebases. - [Changelog](https://github.blog/changelog/2025-12-16-c-code-editing-tools-for-github-copilot-in-public-preview)

### Memory & Context for Long-Running Migrations

-   **Agentic Memory (`PREVIEW`)** -- A cross-agent memory system lets Copilot learn and improve across your development workflow, spanning coding agent, CLI, and code review. Memory persists across sessions, so the AI remembers your preferences and project conventions without repeated context. - [Changelog](https://github.blog/changelog/2026-01-15-agentic-memory-for-github-copilot-is-in-public-preview) | [Memory Docs](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)

    *Why this matters for migration: Migration projects span weeks or months. Memory means the agent accumulates knowledge about your codebase patterns, naming conventions, and migration decisions over time.*

### Relevant Events

| Date | Event | Focus |
|------|-------|-------|
| Feb 17 | [Modernize Your Java Apps in Days with AI Agents](https://developer.microsoft.com/en-us/reactor/events/26640/) | Copilot, Agentic DevOps |
| Mar 24 | [Modernizing .NET at Scale with the GitHub Copilot App Mod Agent](https://developer.microsoft.com/en-us/reactor/events/26782/) | Copilot, Agentic DevOps |

### From the December 2025 Archive

-   **AI-Assisted Modernization Pattern (Martin Fowler)** -- A three-stage "research, review, rebuild" approach to modernizing legacy systems using AI. Highly relevant for healthcare and regulated customers contemplating multi-year modernization of critical systems alongside Copilot and coding agent. - [Article](https://martinfowler.com/articles/research-review-rebuild.html) *[From: December 2025]*

-   **GitHub Billing Team Technical Debt Case Study** -- Real-world example of how GitHub's billing team uses the Coding Agent to continuously tackle technical debt, showing practical applications for enterprise teams. - [Case Study](https://github.blog/ai-and-ml/github-copilot/how-the-github-billing-team-uses-the-coding-agent-in-github-copilot-to-continuously-burn-down-technical-debt/) *[From: December 2025]*

-   **Spec-Kit for Spec-Driven Development** -- A framework for creating structured specifications that improve AI code generation quality and consistency. Use spec-driven development to get better, more predictable results from coding agents. - [Repo](https://github.com/github/spec-kit) | [Announcement](https://developer.microsoft.com/blog/spec-driven-development-spec-kit) *[From: December 2025]*

---

## Recommended Actions

1. **Try Plan Mode for your next migration task** -- Open Copilot CLI, describe a migration unit (e.g., "migrate the UserService from Spring 4 to Spring 6"), and let plan mode generate a structured approach before writing code. [Install CLI](https://github.blog/changelog/2026-01-21-install-and-use-github-copilot-cli-directly-from-the-github-cli)

2. **Register for the Java or .NET modernization events** -- These Microsoft Reactor sessions demonstrate the App Mod Agent pattern for framework-level migrations. [Java (Feb 17)](https://developer.microsoft.com/en-us/reactor/events/26640/) | [.NET (Mar 24)](https://developer.microsoft.com/en-us/reactor/events/26782/)

3. **Read Martin Fowler's Research-Review-Rebuild pattern** -- This provides a structured methodology for AI-assisted modernization that pairs well with Copilot's agent capabilities. [Article](https://martinfowler.com/articles/research-review-rebuild.html)

4. **Enable Copilot Code Review across your migration team** -- Code Review is now available for org members without a Copilot license, so your entire team can benefit during high-PR-volume migration sprints. [Docs](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review)

---

*This briefing was filtered from the [full February 2026 newsletter](https://github.com/rafskov/CustomerNewsletter/blob/main/output/2026-02_february_newsletter.md). For all updates, see the complete issue.*
