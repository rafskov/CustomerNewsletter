# February 2026 Newsletter (Feb 14-23)

This is a personally curated newsletter for my customers, focused on the most relevant GitHub updates from the past week. Highlights include the Copilot coding agent expanding to Visual Studio and Windows projects, a new coding agent model picker for Business and Enterprise, Gemini 3.1 Pro arriving in public preview, organization-level Copilot usage dashboards, and a wave of model deprecations requiring attention. The Copilot CLI continues its rapid release cadence with v0.0.412-414. If you have feedback or want to dive deeper into any topic, please let me know. Feel free to share this newsletter with your team. You can find an archive of past newsletters [here](https://github.com/briancl2/CustomerNewsletter).

---

# Copilot

## Latest Releases

-   **Claude Sonnet 4.6 (`GA`)** -- Anthropic's Claude Sonnet 4.6 is now generally available in GitHub Copilot, offering a strong balance of speed and reasoning quality for everyday coding tasks. - [Changelog](https://github.blog/changelog/2026-02-17-claude-sonnet-4-6-is-now-generally-available-in-github-copilot)

-   **Gemini 3.1 Pro (`PREVIEW`)** -- Google's Gemini 3.1 Pro model is now available in public preview for GitHub Copilot, expanding the model roster for code generation and chat. Admins must enable new models in organizational settings. - [Changelog](https://github.blog/changelog/2026-02-19-gemini-3-1-pro-is-now-in-public-preview-for-github-copilot)

-   **Claude Opus 4.6 Extended to More IDEs** -- Claude Opus 4.6 is now available in Visual Studio, JetBrains IDEs, Xcode, and Eclipse, in addition to VS Code and github.com. - [Changelog](https://github.blog/changelog/2026-02-18-claude-opus-4-6-now-available-in-visual-studio-jetbrains-xcode-and-eclipse)

-   **Coding Agent Model Picker (`PREVIEW`)** -- Copilot Business and Enterprise users now have a model picker for the coding agent, allowing dynamic selection of AI models to optimize for speed, accuracy, or specific capabilities. - [Changelog](https://github.blog/changelog/2026-02-19-copilot-coding-agent-model-picker-for-business-and-enterprise)

-   **Delegate to Coding Agent from Visual Studio** -- You can now assign tasks directly to the Copilot coding agent from Visual Studio, bringing the same delegation workflow previously available in VS Code and JetBrains to the Visual Studio experience. - [Changelog](https://github.blog/changelog/2026-02-17-delegate-tasks-to-copilot-coding-agent-from-visual-studio)

-   **Coding Agent with Windows Projects** -- The Copilot coding agent now supports Windows projects, streamlining agent workflows for Windows-based development environments. - [Changelog](https://github.blog/changelog/2026-02-18-copilot-coding-agent-with-windows-projects)

-   **Coding Agent Supports Code Referencing** -- The coding agent can now use external code references, allowing it to pull in relevant code patterns and examples when generating solutions. - [Changelog](https://github.blog/changelog/2026-02-18-copilot-coding-agent-supports-code-referencing)

-   **Copilot in Zed (`GA`)** -- Full Copilot authentication and model support for the Zed editor is now generally available, adding another officially supported surface for Copilot users who prefer lightweight, fast editors. - [Changelog](https://github.blog/changelog/2026-02-19-github-copilot-support-in-zed-is-generally-available)

-   **Model Deprecations** -- Claude Opus 4.1, GPT-5, and GPT-5-Codex have been officially deprecated across all Copilot experiences (chat, agent, and code completion). Switch to newer supported models such as GPT-5.2, Claude Opus 4.6, or use Auto Model Selection. - [Changelog](https://github.blog/changelog/2026-01-13-upcoming-deprecation-of-select-github-copilot-models-from-claude-and-openai)

-   **Organization-Level Usage Metrics Dashboard (`PREVIEW`)** -- Organization owners can now access a dedicated Copilot usage metrics dashboard at the org level, previously only available at the enterprise tier. This enables more targeted adoption tracking and team-level visibility. - [Changelog](https://github.blog/changelog/2026-02-20-organization-level-copilot-usage-metrics-dashboard)

-   **PR Throughput and Time-to-Merge in Usage Metrics API** -- The Copilot usage metrics API now includes pull request throughput and time-to-merge data, giving leadership deeper analytics on engineering impact. - [Changelog](https://github.blog/changelog/2026-02-19-pull-request-throughput-and-time-to-merge-in-copilot-usage-metrics-api)

-   **Copilot CLI (v0.0.412-v0.0.414)** -- Three releases this week continue the CLI's rapid velocity. v0.0.414 brings the explore agent using GitHub MCP tools, improved tool permission prompts, remote plugin sources, configurable status lines with custom scripts, and migration to the default model. v0.0.413 increases LSP request timeouts to 90s, fixes Copilot API URL and model selection issues, and improves YAML skill file handling. v0.0.412 adds major accessibility improvements (screen reader-friendly help), signed Windows prebuilds, new `/update` and `/mcp reload` commands, and more robust startup feedback. Note: Copilot CLI is covered under the [GitHub Data Protection Agreement](https://docs.github.com/en/site-policy/github-terms/github-dpa-previews) and [Pre-Release License Terms (indemnity)](https://docs.github.com/en/site-policy/github-terms/github-pre-release-license-terms) while in preview. - [CLI Releases](https://github.com/github/copilot-cli/releases) | [CLI Changelog](https://github.com/github/copilot-cli/blob/main/changelog.md)

-   **VS Code v1.110 Insiders** -- The February Insiders build adds Kitty graphics protocol support in terminal (inline images), pixel-dimension reporting, OSC 99 desktop notifications, improved chat session history headings, screen reader notifications for chat steering, and Ctrl/Cmd+W to unmaximize chat instead of closing. - [Release Notes](https://code.visualstudio.com/updates/v1_110)

Stay current with the latest changes: [Copilot Feature Matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=ides) | [GitHub Changelog (Copilot)](https://github.blog/changelog/label/copilot/) | [VS Code Release Notes](https://code.visualstudio.com/updates/) | [Copilot CLI Releases](https://github.com/github/copilot-cli/releases)

---

# Enterprise and Security Updates

-   **API Access to Billing Usage Reports (`PREVIEW`)** -- Enterprise administrators can now programmatically access billing usage reports via API, improving cost management and reporting automation. - [Changelog](https://github.blog/changelog/2026-02-17-api-access-to-billing-usage-reports)

-   **Enterprise Credential Management for Incident Response** -- New enterprise-wide credential management tools help security teams respond to incidents faster, including the ability to revoke and rotate credentials at scale. - [Changelog](https://github.blog/changelog/2026-02-17-enterprise-credential-management-tools)

-   **Required Reviewer Rule (`GA`)** -- The required reviewer rule is now generally available, giving repository administrators more control over who must approve changes before they can be merged. - [Changelog](https://github.blog/changelog/2026-02-17-required-reviewer-rule-generally-available)

-   **Secret Scanning Improvements** -- Enhanced extended metadata checks for secret scanning strengthen coverage and provide richer context for detected secrets. - [Changelog](https://github.blog/changelog/2026-02-18-secret-scanning-improvements)

-   **npm Bulk Trusted Publishing and Script Security (`GA`)** -- Bulk trusted publishing configuration and script security controls are now generally available for npm, strengthening supply chain security for JavaScript ecosystems. - [Changelog](https://github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-and-script-security)

-   **Self-Hosted Runner Minimum Version Brownout** -- The brownout period for self-hosted runner minimum version enforcement (v2.329.0+) runs Feb 16 to Mar 16, 2026. Runners older than v2.329.0 may experience temporary connection blocks during this period. After Mar 16, older runners will be permanently blocked. Review your fleet. - [Changelog](https://github.blog/changelog/2026-02-05-github-actions-self-hosted-runner-minimum-version-enforcement-extended)

---

# GitHub Platform Updates

-   **Workflow Dispatch API Returns Run IDs** -- The workflow dispatch API now returns run IDs in the response, making it significantly easier to track and automate workflows programmatically. - [Changelog](https://github.blog/changelog/2026-02-19-workflow-dispatch-api-returns-run-ids)

-   **GitHub Projects: Import by Query and Hierarchy View** -- Import items into Projects based on search queries, and the hierarchy view now supports improved multi-level issue structures for better planning and tracking. - [Changelog](https://github.blog/changelog/2026-02-19-github-projects-import-items-by-query)

-   **Access All PR Comments in Files Changed** -- Review all pull request comments directly from the "Files changed" tab without navigating away, streamlining the code review workflow. - [Changelog](https://github.blog/changelog/2026-02-19-access-all-pr-comments-in-files-changed)

-   **Test Merge Commit Generation Changes** -- Improvements to how test merge commits are generated for pull requests, affecting CI/CD workflows that depend on merge commit behavior. - [Changelog](https://github.blog/changelog/2026-02-19-test-merge-commit-generation-changes)

-   **Custom Properties and Rule Insights Improvements** -- Organization custom properties and rule insights have been improved, enabling better governance and policy targeting across enterprise structures. - [Changelog](https://github.blog/changelog/2026-02-17-custom-properties-and-rule-insights-improvements)

-   **GitHub Desktop 3.5.5** -- Adds support for running hooks in user shell, bypassing commit hooks, one-time opening of a repo in alternate editor, and Warp terminal support on Windows. - [Release Notes](https://desktop.github.com/release-notes/)

---

# Resources and Best Practices

-   **How to Maximize Copilot's Agentic Capabilities** -- A comprehensive guide showing how agent mode transforms architecture, refactoring, migrations, and multi-file coordination into structured, AI-assisted workflows. Essential reading for teams working with complex or legacy codebases. - [Article](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)

-   **Using the Coding Agent to Improve a Project** -- Step-by-step tutorial on using the coding agent to reduce technical debt, streamline environment setup, and automate issue creation. A repeatable pattern for turning aging codebases into maintainable projects. - [Docs](https://docs.github.com/en/copilot/tutorials/coding-agent/improve-a-project)

-   **What AI Is Actually Good For, According to Developers** -- Survey data and analysis on where AI tools genuinely boost productivity versus where they add noise. Useful framing for adoption conversations with engineering leadership. - [Article](https://github.blog/ai-and-ml/generative-ai/what-ai-is-actually-good-for-according-to-developers/)

-   **Context Windows, Plan Agent, and TDD** -- Deep walkthrough (includes 1.5hr video) of building a real application with Copilot's Plan agent and custom agents, highlighting context management and test-driven development as essential AI-assisted engineering skills. - [Article](https://github.blog/developer-skills/application-development/context-windows-plan-agent-and-tdd-what-i-learned-building-a-countdown-app-with-github-copilot/) | [Video (1:33)](https://github.blog/developer-skills/application-development/context-windows-plan-agent-and-tdd-what-i-learned-building-a-countdown-app-with-github-copilot/)

## Official Microsoft Learn Training (Free)

| Course | Focus |
|--------|-------|
| [GitHub Copilot Fundamentals](https://learn.microsoft.com/en-us/training/paths/copilot/) | Setup, prompt crafting, core features |
| [Accelerate Development with Copilot](https://learn.microsoft.com/en-us/training/paths/accelerate-app-development-using-github-copilot/) | Real-world development workflows |

## Video Demos (Scott Hanselman Series)

| Video | Duration |
|-------|----------|
| [Using /share in Copilot CLI](https://www.youtube.com/watch?v=E17SXyL53w4) | 3:34 |
| [Using /delegate in Copilot CLI](https://www.youtube.com/watch?v=P2qK2BCdi-w) | 2:17 |
| [Switching Models in Copilot CLI](https://www.youtube.com/watch?v=dpxODnbIQgg) | 2:53 |
| [Configuring MCP in Copilot CLI](https://www.youtube.com/watch?v=O73egpvWcpY) | 4:07 |
| [YOLO Mode in Copilot CLI](https://www.youtube.com/watch?v=UMz8aQ4lOtE) | 2:20 |

---

*This newsletter covers GitHub updates from February 14-23, 2026. For the full February 2026 newsletter covering Dec 5 2025 to Feb 13 2026, see the [complete issue](2026-02_february_newsletter.md).*
