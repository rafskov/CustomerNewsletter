# Legacy Codebase Migration: Late February 2026 GitHub Updates (Feb 14-23)

This week's updates significantly expand the tooling available for legacy modernization efforts. The Copilot coding agent now reaches Visual Studio and Windows projects, two surfaces critical for teams working with enterprise .NET and Windows-native legacy codebases. A new model picker lets migration teams choose the optimal AI model per task, and code referencing support means the agent can pull in target patterns when transforming legacy code. Combined with three CLI releases and a comprehensive agentic capabilities guide, this is a strong week for migration teams.

---

## Key Updates

### Coding Agent Expansion

-   **Delegate to Coding Agent from Visual Studio** -- You can now assign tasks directly to the Copilot coding agent from Visual Studio, bringing the same delegation workflow previously available in VS Code and JetBrains to the Visual Studio experience. - [Changelog](https://github.blog/changelog/2026-02-17-delegate-tasks-to-copilot-coding-agent-from-visual-studio)

    *Why this matters for migration: Many legacy enterprise codebases live in Visual Studio (.NET, C++, C#). Delegation from VS means migration teams can now assign refactoring and modernization tasks to the coding agent without leaving their primary IDE.*

-   **Coding Agent with Windows Projects** -- The Copilot coding agent now supports Windows projects, streamlining agent workflows for Windows-based development environments. - [Changelog](https://github.blog/changelog/2026-02-18-copilot-coding-agent-with-windows-projects)

    *Why this matters for migration: A large share of legacy enterprise software targets Windows. This unlocks agent-assisted migration for WinForms, WPF, Windows Services, and other Windows-native projects.*

-   **Coding Agent Supports Code Referencing** -- The coding agent can now use external code references, allowing it to pull in relevant code patterns and examples when generating solutions. - [Changelog](https://github.blog/changelog/2026-02-18-copilot-coding-agent-supports-code-referencing)

    *Why this matters for migration: Point the agent at target framework patterns (e.g., a reference implementation in .NET 8) and it can use those patterns when transforming legacy code, improving consistency and accuracy.*

-   **Coding Agent Model Picker (`PREVIEW`)** -- Copilot Business and Enterprise users now have a model picker for the coding agent, allowing dynamic selection of AI models to optimize for speed, accuracy, or specific capabilities. - [Changelog](https://github.blog/changelog/2026-02-19-copilot-coding-agent-model-picker-for-business-and-enterprise)

    *Why this matters for migration: Use a high-reasoning model (Claude Opus 4.6) for complex architectural refactoring and a faster model (Sonnet, GPT-5.2-Codex) for bulk file transformations, matching the model to the task.*

### Models for Migration Workloads

-   **Claude Sonnet 4.6 (`GA`)** -- Anthropic's Claude Sonnet 4.6 is now generally available in GitHub Copilot, offering a strong balance of speed and reasoning quality for everyday coding tasks. - [Changelog](https://github.blog/changelog/2026-02-17-claude-sonnet-4-6-is-now-generally-available-in-github-copilot)

-   **Claude Opus 4.6 Extended to More IDEs** -- Claude Opus 4.6 is now available in Visual Studio, JetBrains IDEs, Xcode, and Eclipse, in addition to VS Code and github.com. - [Changelog](https://github.blog/changelog/2026-02-18-claude-opus-4-6-now-available-in-visual-studio-jetbrains-xcode-and-eclipse)

    *Why this matters for migration: Claude Opus 4.6 excels at reasoning-heavy tasks like understanding legacy code intent and planning multi-step refactors. Having it available across all IDEs means every team member can access it regardless of their editor.*

-   **Model Deprecations** -- Claude Opus 4.1, GPT-5, and GPT-5-Codex have been officially deprecated across all Copilot experiences. Switch to newer supported models such as GPT-5.2, Claude Opus 4.6, or use Auto Model Selection. - [Changelog](https://github.blog/changelog/2026-01-13-upcoming-deprecation-of-select-github-copilot-models-from-claude-and-openai)

    *Action required: If your migration workflows reference specific models, update them before the deprecated models are removed.*

### CLI & Tooling

-   **Copilot CLI (v0.0.412-v0.0.414)** -- v0.0.414 brings the explore agent using GitHub MCP tools and remote plugin sources. v0.0.412 adds new `/update` and `/mcp reload` commands and major accessibility improvements. - [CLI Releases](https://github.com/github/copilot-cli/releases) | [CLI Changelog](https://github.com/github/copilot-cli/blob/main/changelog.md)

    *Why this matters for migration: The explore agent with MCP tools enables rapid codebase analysis directly from the terminal, useful for discovery phases of migration projects.*

### Measuring Migration Impact

-   **Organization-Level Usage Metrics Dashboard (`PREVIEW`)** -- Organization owners can now access a dedicated Copilot usage metrics dashboard at the org level. - [Changelog](https://github.blog/changelog/2026-02-20-organization-level-copilot-usage-metrics-dashboard)

-   **PR Throughput and Time-to-Merge in Usage Metrics API** -- The Copilot usage metrics API now includes pull request throughput and time-to-merge data. - [Changelog](https://github.blog/changelog/2026-02-19-pull-request-throughput-and-time-to-merge-in-copilot-usage-metrics-api)

    *Why this matters for migration: Track whether AI-assisted migration is actually accelerating delivery. Compare PR throughput and time-to-merge before and during migration sprints to quantify the impact.*

### Guides & Learning

-   **How to Maximize Copilot's Agentic Capabilities** -- A comprehensive guide showing how agent mode transforms architecture, refactoring, migrations, and multi-file coordination into structured, AI-assisted workflows. Essential reading for teams working with complex or legacy codebases. - [Article](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)

-   **Using the Coding Agent to Improve a Project** -- Step-by-step tutorial on using the coding agent to reduce technical debt, streamline environment setup, and automate issue creation. A repeatable pattern for turning aging codebases into maintainable projects. - [Docs](https://docs.github.com/en/copilot/tutorials/coding-agent/improve-a-project)

---

## Recommended Actions

1. **Try delegating a migration task from Visual Studio** -- If your legacy codebase lives in VS, use the new delegation feature to assign a refactoring task to the coding agent and evaluate the results. [Changelog](https://github.blog/changelog/2026-02-17-delegate-tasks-to-copilot-coding-agent-from-visual-studio)

2. **Use the model picker to match models to migration tasks** -- Select Claude Opus 4.6 for complex reasoning (understanding legacy patterns, planning refactors) and a faster model for bulk transformations (file renames, API signature updates). [Changelog](https://github.blog/changelog/2026-02-19-copilot-coding-agent-model-picker-for-business-and-enterprise)

3. **Read the agentic capabilities guide** -- This is the most migration-relevant resource published this period, covering architecture, refactoring, and multi-file coordination patterns. [Article](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)

4. **Update any workflows referencing deprecated models** -- Claude Opus 4.1, GPT-5, and GPT-5-Codex are being removed. Audit your custom agents, skills, and CI configurations. [Changelog](https://github.blog/changelog/2026-01-13-upcoming-deprecation-of-select-github-copilot-models-from-claude-and-openai)

---

*This briefing was filtered from the [late February 2026 newsletter (Feb 14-23)](../2026-02-late_february_newsletter.md). For all updates, see the complete issue.*
