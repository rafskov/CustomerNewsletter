# Legacy Codebase Migration: Full February 2026 GitHub Updates

February 2026 was a landmark month for AI-assisted codebase modernization. Third-party coding agents (Claude and Codex) arrived on Agent HQ, VS Code evolved into a multi-agent orchestration hub with parallel subagents, plan mode, and persistent memory, and the coding agent expanded to Visual Studio and Windows projects. A new model picker lets migration teams choose the optimal AI model per task, and code referencing support means the agent can pull in target patterns when transforming legacy code. If your team is planning or executing a legacy modernization effort, this briefing collects every relevant update from the full month.

---

## Agents & Orchestration for Migration Workflows

-   **Third-Party Agents on Agent HQ (`PREVIEW`)** -- Claude by Anthropic and OpenAI Codex are now available in public preview directly on GitHub and VS Code. Enterprise subscribers can choose between GitHub's own Coding Agent, Claude, or Codex, selecting the best tool for each task. No additional cost, existing terms apply, consuming the same premium request units (PRUs). - [Changelog](https://github.blog/changelog/2026-02-04-claude-and-codex-are-now-available-in-public-preview-on-github) | [GitHub Blog](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)

    *Why this matters for migration: Different agents excel at different languages and patterns. Teams migrating heterogeneous codebases can use Claude for reasoning-heavy refactoring and Codex for bulk code transformation.*

-   **Delegate to Coding Agent from Visual Studio** -- You can now assign tasks directly to the Copilot coding agent from Visual Studio, bringing the same delegation workflow previously available in VS Code and JetBrains to the Visual Studio experience. - [Changelog](https://github.blog/changelog/2026-02-17-delegate-tasks-to-copilot-coding-agent-from-visual-studio)

    *Why this matters for migration: Many legacy enterprise codebases live in Visual Studio (.NET, C++, C#). Delegation from VS means migration teams can now assign refactoring and modernization tasks to the coding agent without leaving their primary IDE.*

-   **Coding Agent with Windows Projects** -- The Copilot coding agent now supports Windows projects, streamlining agent workflows for Windows-based development environments. - [Changelog](https://github.blog/changelog/2026-02-18-copilot-coding-agent-with-windows-projects)

    *Why this matters for migration: A large share of legacy enterprise software targets Windows. This unlocks agent-assisted migration for WinForms, WPF, Windows Services, and other Windows-native projects.*

-   **Coding Agent Supports Code Referencing** -- The coding agent can now use external code references, allowing it to pull in relevant code patterns and examples when generating solutions. - [Changelog](https://github.blog/changelog/2026-02-18-copilot-coding-agent-supports-code-referencing)

    *Why this matters for migration: Point the agent at target framework patterns (e.g., a reference implementation in .NET 8) and it can use those patterns when transforming legacy code, improving consistency and accuracy.*

-   **Coding Agent Model Picker (`PREVIEW`)** -- Copilot Business and Enterprise users now have a model picker for the coding agent, allowing dynamic selection of AI models to optimize for speed, accuracy, or specific capabilities. - [Changelog](https://github.blog/changelog/2026-02-19-copilot-coding-agent-model-picker-for-business-and-enterprise)

    *Why this matters for migration: Use a high-reasoning model (Claude Opus 4.6) for complex architectural refactoring and a faster model (Sonnet, GPT-5.2-Codex) for bulk file transformations, matching the model to the task.*

-   **Parallel Subagents** -- Subagents run in parallel with dedicated context windows, significantly speeding up complex tasks. Each subagent operates autonomously and returns only a summary to the main agent, reducing token usage. - [Release Notes](https://code.visualstudio.com/updates/v1_109#_subagents) | [Docs](https://code.visualstudio.com/docs/copilot/agents/subagents) | [Video (25m)](https://www.youtube.com/watch?v=GMAoTeD9siU)

    *Why this matters for migration: Decompose large migration tasks into parallel subtasks (e.g., one subagent handles API layer, another handles data models, another handles tests).*

-   **GitHub Agentic Workflows (`PREVIEW`)** -- [GitHub Agentic Workflows](https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/) let you write GitHub Actions automation in plain Markdown and let AI agents handle intelligent decision-making for CI failure analysis and repository maintenance. The [gh-aw framework](https://github.com/github/gh-aw) includes 50+ operational workflow examples. - [Documentation](https://github.github.io/gh-aw/) | [Video (1m)](https://www.youtube.com/watch?v=3_i03fGXs9U)

    *Why this matters for migration: Automate post-migration validation, regression testing, and continuous improvement workflows with AI-driven analysis.*

---

## Code Review & Quality During Migration

-   **Copilot Code Review (`GA`)** -- Organization members can now use Copilot code review on pull requests even without a Copilot license, expanding adoption across the entire team. - [Changelog](https://github.blog/changelog/2025-12-17-copilot-code-review-now-available-for-organization-members-without-a-license) | [Docs](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review)

    *Why this matters for migration: Large migrations generate many PRs. AI-assisted code review catches issues across the full team without requiring every developer to have a Copilot license.*

-   **Agent Skills (`GA`)** -- Agent Skills are now generally available and enabled by default in VS Code. Skills are also available as [slash commands](https://code.visualstudio.com/updates/v1_109#_use-skills-as-slash-commands). New [Agent Hooks](https://code.visualstudio.com/updates/v1_109#_agent-hooks-preview) (`PREVIEW`) let you run custom shell commands at key agent lifecycle points, enabling deterministic security policy enforcement and code quality gates. - [Changelog](https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills) | [Skills Docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills) | [Hooks Docs](https://code.visualstudio.com/docs/copilot/customization/hooks)

    *Why this matters for migration: Create reusable migration skills (e.g., "migrate-dao-to-repository-pattern") and enforce quality gates with hooks that run linters and tests after every agent change.*

-   **C++ Code Editing Tools (`PREVIEW`)** -- Copilot gains specialized code editing tools for C++ projects, improving the agent's ability to navigate and edit C++ codebases. - [Changelog](https://github.blog/changelog/2025-12-16-c-code-editing-tools-for-github-copilot-in-public-preview)

---

## Models for Migration Workloads

-   **Claude Sonnet 4.6 (`GA`)** -- Anthropic's Claude Sonnet 4.6 is now generally available in GitHub Copilot, offering a strong balance of speed and reasoning quality for everyday coding tasks. - [Changelog](https://github.blog/changelog/2026-02-17-claude-sonnet-4-6-is-now-generally-available-in-github-copilot)

-   **Claude Opus 4.6 Extended to More IDEs** -- Claude Opus 4.6 is now available in Visual Studio, JetBrains IDEs, Xcode, and Eclipse, in addition to VS Code and github.com. - [Changelog](https://github.blog/changelog/2026-02-18-claude-opus-4-6-now-available-in-visual-studio-jetbrains-xcode-and-eclipse)

    *Why this matters for migration: Claude Opus 4.6 excels at reasoning-heavy tasks like understanding legacy code intent and planning multi-step refactors. Having it available across all IDEs means every team member can access it regardless of their editor.*

-   **Model Deprecations** -- Claude Opus 4.1, GPT-5, and GPT-5-Codex have been officially deprecated across all Copilot experiences. Switch to newer supported models such as GPT-5.2, Claude Opus 4.6, or use Auto Model Selection. - [Changelog](https://github.blog/changelog/2026-01-13-upcoming-deprecation-of-select-github-copilot-models-from-claude-and-openai)

    *Action required: If your migration workflows reference specific models, update them before the deprecated models are removed.*

---

## Memory, Context & CLI Tooling

-   **Agentic Memory (`PREVIEW`)** -- A cross-agent memory system lets Copilot learn and improve across your development workflow, spanning coding agent, CLI, and code review. Memory persists across sessions, so the AI remembers your preferences and project conventions without repeated context. - [Changelog](https://github.blog/changelog/2026-01-15-agentic-memory-for-github-copilot-is-in-public-preview) | [Memory Docs](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)

    *Why this matters for migration: Migration projects span weeks or months. Memory means the agent accumulates knowledge about your codebase patterns, naming conventions, and migration decisions over time.*

-   **Copilot CLI and SDK (`PREVIEW`)** -- The Copilot CLI now includes [Plan mode](https://github.blog/changelog/2026-01-21-github-copilot-cli-plan-before-you-build-steer-as-you-go) for structured task planning, [autopilot mode](https://github.com/github/copilot-cli/releases/tag/v0.0.400) for autonomous task completion, and [repository memory](https://github.blog/changelog/2026-01-21-github-copilot-cli-plan-before-you-build-steer-as-you-go) across sessions. The new [Copilot SDK](https://github.blog/changelog/2026-01-14-copilot-sdk-in-technical-preview) (technical preview) provides language-specific libraries for Node.js/TypeScript, Python, Go, and .NET. - [CLI Releases](https://github.com/github/copilot-cli/releases) | [SDK Video (45m)](https://www.youtube.com/watch?v=LO7nf-dbURE)

-   **Copilot CLI (v0.0.412-v0.0.414)** -- v0.0.414 brings the explore agent using GitHub MCP tools and remote plugin sources. v0.0.412 adds new `/update` and `/mcp reload` commands and major accessibility improvements. - [CLI Changelog](https://github.com/github/copilot-cli/blob/main/changelog.md)

    *Why this matters for migration: Plan mode lets you describe a migration task in plain language and get a structured plan. The explore agent with MCP tools enables rapid codebase analysis from the terminal, useful for discovery phases.*

---

## Measuring Migration Impact

-   **Organization-Level Usage Metrics Dashboard (`PREVIEW`)** -- Organization owners can now access a dedicated Copilot usage metrics dashboard at the org level, previously only available at the enterprise tier. - [Changelog](https://github.blog/changelog/2026-02-20-organization-level-copilot-usage-metrics-dashboard)

-   **PR Throughput and Time-to-Merge in Usage Metrics API** -- The Copilot usage metrics API now includes pull request throughput and time-to-merge data, giving leadership deeper analytics on engineering impact. - [Changelog](https://github.blog/changelog/2026-02-19-pull-request-throughput-and-time-to-merge-in-copilot-usage-metrics-api)

    *Why this matters for migration: Track whether AI-assisted migration is actually accelerating delivery. Compare PR throughput and time-to-merge before and during migration sprints to quantify the impact.*

---

## Relevant Events

| Date | Event | Focus |
|------|-------|-------|
| Feb 17 | [Modernize Your Java Apps in Days with AI Agents](https://developer.microsoft.com/en-us/reactor/events/26640/) | Copilot, Agentic DevOps |
| Mar 24 | [Modernizing .NET at Scale with the GitHub Copilot App Mod Agent](https://developer.microsoft.com/en-us/reactor/events/26782/) | Copilot, Agentic DevOps |

---

## Guides & Learning

-   **How to Maximize Copilot's Agentic Capabilities** -- A comprehensive guide showing how agent mode transforms architecture, refactoring, migrations, and multi-file coordination into structured, AI-assisted workflows. Essential reading for teams working with complex or legacy codebases. - [Article](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)

-   **Using the Coding Agent to Improve a Project** -- Step-by-step tutorial on using the coding agent to reduce technical debt, streamline environment setup, and automate issue creation. A repeatable pattern for turning aging codebases into maintainable projects. - [Docs](https://docs.github.com/en/copilot/tutorials/coding-agent/improve-a-project)

### From the December 2025 Archive

-   **AI-Assisted Modernization Pattern (Martin Fowler)** -- A three-stage "research, review, rebuild" approach to modernizing legacy systems using AI. Highly relevant for healthcare and regulated customers contemplating multi-year modernization. - [Article](https://martinfowler.com/articles/research-review-rebuild.html) *[From: December 2025]*

-   **GitHub Billing Team Technical Debt Case Study** -- Real-world example of how GitHub's billing team uses the Coding Agent to continuously tackle technical debt. - [Case Study](https://github.blog/ai-and-ml/github-copilot/how-the-github-billing-team-uses-the-coding-agent-in-github-copilot-to-continuously-burn-down-technical-debt/) *[From: December 2025]*

-   **Spec-Kit for Spec-Driven Development** -- A framework for creating structured specifications that improve AI code generation quality and consistency. - [Repo](https://github.com/github/spec-kit) | [Announcement](https://developer.microsoft.com/blog/spec-driven-development-spec-kit) *[From: December 2025]*

---

## Recommended Actions

1. **Try delegating a migration task from Visual Studio** -- If your legacy codebase lives in VS, use the new delegation feature to assign a refactoring task to the coding agent and evaluate the results. [Changelog](https://github.blog/changelog/2026-02-17-delegate-tasks-to-copilot-coding-agent-from-visual-studio)

2. **Use the model picker to match models to migration tasks** -- Select Claude Opus 4.6 for complex reasoning (understanding legacy patterns, planning refactors) and a faster model for bulk transformations (file renames, API signature updates). [Changelog](https://github.blog/changelog/2026-02-19-copilot-coding-agent-model-picker-for-business-and-enterprise)

3. **Try Plan Mode for your next migration task** -- Open Copilot CLI, describe a migration unit (e.g., "migrate the UserService from Spring 4 to Spring 6"), and let plan mode generate a structured approach before writing code. [Install CLI](https://github.blog/changelog/2026-01-21-install-and-use-github-copilot-cli-directly-from-the-github-cli)

4. **Read the agentic capabilities guide** -- This is the most migration-relevant resource published this month, covering architecture, refactoring, and multi-file coordination patterns. [Article](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)

5. **Register for the .NET modernization event (Mar 24)** -- This Microsoft Reactor session demonstrates the App Mod Agent pattern for framework-level migrations at scale. [Register](https://developer.microsoft.com/en-us/reactor/events/26782/)

6. **Enable Copilot Code Review across your migration team** -- Code Review is now available for org members without a Copilot license, so your entire team can benefit during high-PR-volume migration sprints. [Docs](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review)

7. **Update any workflows referencing deprecated models** -- Claude Opus 4.1, GPT-5, and GPT-5-Codex are being removed. Audit your custom agents, skills, and CI configurations. [Changelog](https://github.blog/changelog/2026-01-13-upcoming-deprecation-of-select-github-copilot-models-from-claude-and-openai)

---

*This briefing was filtered from the February 2026 newsletters ([Dec 5 - Feb 13](https://github.com/rafskov/CustomerNewsletter/blob/main/output/2026-02_february_newsletter.md) and [Feb 14-23](https://github.com/rafskov/CustomerNewsletter/blob/main/output/2026-02-late_february_newsletter.md)). For all updates, see the complete issues.*
