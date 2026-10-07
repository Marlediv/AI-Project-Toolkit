# AI-Assisted Project Template

A vendor-neutral GitHub project template for structured AI-assisted software development with support for **OpenAI Codex** and **Anthropic Claude Code**.

The template provides a shared project knowledge layer, agent-specific configuration, reusable AI workflows, testing guidance, Architecture Decision Records, MCP integration points, and a foundation for continuous integration.

The central principle is simple:

> **The project is the source of truth. AI agents are tools that consume and work with that knowledge.**

Project architecture, conventions, testing requirements, and important decisions should therefore remain in version-controlled, human-readable documentation rather than being hidden inside prompts or duplicated across AI-specific configuration.

---

## Why This Template Exists

AI coding assistants are increasingly capable of working across entire repositories.

Without a deliberate project structure, however, AI-assisted development can quickly accumulate:

- duplicated instructions
- conflicting prompts
- undocumented assumptions
- agent-specific project knowledge
- inconsistent testing behavior
- overly broad tool permissions
- configuration that only works with one AI provider

This template provides a starting point for avoiding those problems.

It separates:

1. **shared project knowledge**
2. **AI-agent instructions**
3. **agent-specific configuration**
4. **reusable AI capabilities**
5. **automation and external integrations**

The result is a repository that can evolve independently of any single AI coding assistant.

---

## Design Principles

### The Repository Is the Source of Truth

Important project knowledge should be stored in the repository.

AI agents should consume that knowledge rather than becoming the only place where it exists.

---

### Shared Knowledge Is Vendor-Neutral

Information that applies to the project regardless of which AI assistant is being used belongs in `docs/`.

Examples include:

- architecture
- conventions
- testing strategy
- AI collaboration principles
- architectural decisions

---

### AI Tools Are Adapters

Agent-specific files connect an AI tool to the shared project context.

For example:

```text
Shared project knowledge
        │
        ├── docs/architecture.md
        ├── docs/conventions.md
        ├── docs/testing.md
        ├── docs/ai-usage.md
        └── docs/decisions/
        │
        ├───────────────┐
        ▼               ▼
    AGENTS.md       CLAUDE.md
        │               │
        ▼               ▼
     .codex/         .claude/
```

Codex and Claude Code may use different configuration mechanisms, but they should operate on the same underlying project knowledge.

---

### Structure Fully, Activate Minimally

The template exposes the major extension mechanisms supported by the included AI tools without enabling arbitrary project behavior.

Templates are provided for:

- agents
- skills
- rules
- hooks
- MCP
- CI

Project-specific behavior should be enabled deliberately after creating a project from the template.

---

### Validation Is Evidence

AI-generated changes are not considered correct merely because an AI agent reports success.

Testing and validation should produce actual evidence.

The project testing strategy is defined in:

`docs/testing.md`

---

### Access Is Not Authorization

An AI agent having access to a tool, MCP server, database, shell, API, or external system does not automatically mean that it is authorized to modify that system.

Projects should define explicit boundaries for high-risk, destructive, or externally visible operations.

---

## Repository Structure

```text
ai-assisted-project-template/
│
├── .claude/
│   ├── agents/
│   │   └── example.md.example
│   ├── hooks/
│   │   └── example.py
│   ├── rules/
│   │   └── example.md.example
│   ├── skills/
│   │   └── example-skill/
│   │       └── SKILL.md.example
│   └── settings.json
│
├── .agents/
│   └── skills/
│       └── example-skill/
│           └── SKILL.md
│
├── .codex/
│   ├── agents/
│   │   └── example.toml
│   ├── config.toml
│   └── hooks.json
│
├── .github/
│   └── workflows/
│       └── ci.yml.example
│
├── docs/
│   ├── decisions/
│   │   └── 0000-template.md
│   ├── ai-usage.md
│   ├── architecture.md
│   ├── conventions.md
│   └── testing.md
│
├── scripts/
│   └── .gitkeep
├── src/
│   └── .gitkeep
├── tests/
│   └── .gitkeep
│
├── .editorconfig
├── .gitignore
├── .mcp.json
├── AGENTS.md
├── CLAUDE.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

The application directories are intentionally generic.

A project created from this template may replace `src/`, `tests/`, or `scripts/` with a structure more appropriate for its technology stack or architecture.

---

# Getting Started

## 1. Create a Repository from the Template

Use GitHub's **Use this template** feature to create a new repository.

Clone the new repository and open it in your preferred development environment.

The repository should then be customized for the actual project rather than preserving the template unchanged.

---

## 2. Define the Project

Start with the shared documentation.

Recommended order:

1. `docs/architecture.md`
2. `docs/conventions.md`
3. `docs/testing.md`
4. `docs/ai-usage.md`

Replace placeholders, remove irrelevant sections, and add project-specific information.

Do not keep template sections merely because they already exist.

---

## 3. Review the Architecture Decision Process

Architecture Decision Records are stored in:

```text
docs/decisions/
```

The included:

```text
docs/decisions/0000-template.md
```

can be copied when a significant architectural or technical decision requires durable context and rationale.

Use sequential filenames such as:

```text
0001-database-selection.md
0002-api-versioning.md
0003-deployment-platform.md
```

Do not create ADRs for routine implementation details.

---

## 4. Choose the AI Tools

The template supports both Codex and Claude Code, but a project does not need to use both.

### Codex

Keep:

```text
AGENTS.md
.codex/
```

Customize these files for the project.

### Claude Code

Keep:

```text
CLAUDE.md
.claude/
.mcp.json
```

Customize these files for the project.

### Using Both

Keep both integrations.

Shared project knowledge should remain in `docs/` rather than being duplicated between the two AI configurations.

### Using Neither

The shared documentation structure can also be used without an AI coding assistant.

Remove the AI-specific configuration that the project does not require.

---

## 5. Configure the Technology Stack

The template intentionally does not assume a programming language, framework, database, package manager, or deployment platform.

After choosing the project stack:

- replace the generic application directory structure where appropriate
- extend `.gitignore`
- extend `.editorconfig` if required
- add dependency-management files
- add formatter and linter configuration
- define build and runtime requirements
- update `docs/conventions.md`
- update `docs/testing.md`
- configure CI

---

## 6. Configure Continuous Integration

The template contains:

```text
.github/workflows/ci.yml.example
```

It is intentionally not an active GitHub Actions workflow.

To enable CI:

1. define the validation required by the project
2. update the example workflow
3. add the required runtime and dependency setup
4. add formatting, linting, type checking, tests, or other validation
5. rename the file to:

```text
.github/workflows/ci.yml
```

The workflow should automate the validation strategy defined in:

`docs/testing.md`

CI should implement project requirements rather than becoming a separate source of testing policy.

---

# Shared Project Knowledge

## Architecture

`docs/architecture.md`

Describes the current architecture of the project, including components, boundaries, integrations, constraints, deployment, and relevant architectural characteristics.

---

## Conventions

`docs/conventions.md`

Defines shared contribution and implementation conventions.

Possible topics include:

- naming
- code style
- Git workflow
- dependency management
- configuration
- logging
- data conventions
- compatibility
- generated files
- Definition of Done

---

## Testing

`docs/testing.md`

Defines how project changes are validated.

It should describe the project's expectations for areas such as:

- unit testing
- integration testing
- regression testing
- static analysis
- security validation
- performance validation
- CI
- validation evidence

AI agents and human contributors should follow the same testing strategy.

---

## AI-Assisted Development

`docs/ai-usage.md`

Defines vendor-neutral principles for working with AI agents.

It covers areas such as:

- sources of truth
- responsibility
- scope
- assumptions
- validation
- failure handling
- security
- external tools
- MCP
- high-risk operations
- completion reporting

---

## Architecture Decisions

`docs/decisions/`

Stores Architecture Decision Records.

ADRs preserve the reasoning behind significant decisions without turning the main architecture document into a historical log.

---

# Codex Integration

Codex-specific project configuration is divided between:

```text
AGENTS.md
.codex/
```

## `AGENTS.md`

The repository-level Codex instruction entry point.

It directs Codex toward the shared project documentation and defines project-level working behavior.

Keep shared project knowledge out of this file whenever possible.

---

## `.codex/config.toml`

Project-level Codex configuration.

This is the appropriate location for supported Codex configuration such as project-specific MCP integration and other Codex runtime behavior.

The template intentionally enables no project-specific MCP server or other external integration.

---

## `.codex/agents/`

Contains neutral templates and concrete project-specific Codex agent
configuration files.

The included:

```text
.codex/agents/example.toml
```

is a neutral starting point.

To activate a concrete role, copy or rename the template, add the supported
role configuration, and register the role in `.codex/config.toml` under
`[agents.<name>]` with `config_file = "agents/<file>.toml"`.

The template does not register an agent by default.

---

## `.agents/skills/`

Contains reusable repository-scoped Codex project skills.

The example skill is located at:

```text
.agents/skills/example-skill/SKILL.md
```

A skill should represent a focused, reusable capability or workflow.

Shared project knowledge should not be copied into individual skills.

---

## `.codex/hooks.json`

Reserved for project-level Codex lifecycle hook configuration.

No hooks are enabled by default.

Hooks should only be introduced when the project has a concrete automation requirement.

---

# Claude Code Integration

Claude Code project configuration is divided between:

```text
CLAUDE.md
.claude/
.mcp.json
```

## `CLAUDE.md`

The repository-level Claude Code instruction entry point.

It connects Claude Code to the shared project documentation and defines general Claude-specific working behavior.

---

## `.claude/settings.json`

Contains project-level Claude Code settings.

The template starts with minimal configuration and does not enable project-specific hooks or external behavior.

Review permissions deliberately when adapting the template.

---

## `.claude/rules/`

Contains additional Claude Code rules.

Rules are useful when instructions apply to a particular part of the repository or when Claude-specific guidance should be modularized.

The included:

```text
.claude/rules/example.md.example
```

is a disabled template. Copy or rename it to a `.md` file under
`.claude/rules/` before using it as a rule.

Avoid using rules to duplicate shared project documentation.

---

## `.claude/skills/`

Contains reusable Claude Code skills.

The example is located at:

```text
.claude/skills/example-skill/SKILL.md.example
```

This is a disabled template. Create
`.claude/skills/<skill-name>/SKILL.md` for a concrete skill. Skills should
represent focused capabilities rather than independent copies of project
documentation.

---

## `.claude/agents/`

Contains specialized Claude Code agents.

The included:

```text
.claude/agents/example.md.example
```

is a disabled template. Copy or rename it to a `.md` file under
`.claude/agents/` before using it as a specialized agent.

Specialized agents should have narrower responsibilities than the default project agent.

---

## `.claude/hooks/`

Contains project-specific hook implementations.

The included:

```text
.claude/hooks/example.py
```

is intentionally not enabled.

Hook activation belongs in Claude Code configuration.

Do not enable hooks merely because an example implementation exists.

Hooks execute code automatically during configured lifecycle events and should therefore be reviewed carefully before activation.

---

# Model Context Protocol

MCP can provide AI agents with access to external tools and data sources.

The two supported AI integrations use separate project configuration mechanisms.

## Claude Code

Project MCP configuration is represented by:

```text
.mcp.json
```

The template contains:

```json
{
  "mcpServers": {}
}
```

No MCP servers are configured by default.

---

## Codex

Codex MCP servers are configured through:

```text
.codex/config.toml
```

using the supported Codex MCP configuration mechanism.

---

## MCP Security

Before enabling an MCP server, consider:

- why the project requires it
- whether access should be read-only or writable
- which tools should be exposed
- what external systems become reachable
- what credentials are required
- what destructive operations are possible

Do not store secrets directly in version-controlled MCP configuration.

Use appropriate environment variables, secret stores, authentication mechanisms, or other secure configuration supported by the selected MCP integration.

Access to an MCP server does not automatically authorize every operation exposed by that server.

---

# AI Extension Model

The template intentionally exposes several different AI extension mechanisms.

They serve different purposes.

| Mechanism | Purpose |
|---|---|
| Shared documentation | Authoritative project knowledge |
| Agent instructions | General behavior for a specific AI tool |
| Rules | Additional contextual or scoped instructions |
| Skills | Reusable capabilities and workflows |
| Specialized agents | Focused roles with separate responsibilities |
| Hooks | Automated lifecycle behavior |
| MCP | Access to external tools and systems |

Do not use multiple mechanisms to encode the same rule.

When information applies to the project generally, prefer placing it in shared documentation.

---

# Human and AI Collaboration

Human-authored and AI-assisted changes follow the same project standards.

AI-generated output should not be treated as inherently correct.

Contributors remain responsible for:

- understanding the impact of changes
- reviewing generated output
- maintaining appropriate scope
- validating behavior
- protecting sensitive information
- documenting important decisions

The detailed collaboration model is defined in:

`docs/ai-usage.md`

---

# Security

Do not commit:

- passwords
- API keys
- access tokens
- private keys
- authentication cookies
- confidential connection strings
- other secrets

The default `.gitignore` excludes common local environment files:

```text
.env
.env.*
```

while allowing a deliberately maintained:

```text
.env.example
```

if the project later requires one.

The template itself does not include an `.env` or `.env.example` because it defines no environment variables by default.

Review AI tool permissions, MCP integrations, hooks, CI permissions, and external-system access before enabling them.

---

# GitHub and Dependency Management

The repository is intended to work well with standard GitHub project features.

Depending on the project, consider configuring:

- branch protection or repository rulesets
- required pull request reviews
- required CI checks
- Dependabot version updates
- security scanning
- release workflows
- CODEOWNERS
- pull request templates
- issue templates

These are intentionally not fully prescribed by the base template because their correct configuration depends on the project and its governance requirements.

---

# Customizing the Template

A project created from this repository should not preserve every template file merely for completeness.

Remove mechanisms that are not useful.

Examples:

- remove `.codex/` and `AGENTS.md` if Codex is not used
- remove `.claude/`, `CLAUDE.md`, and `.mcp.json` if Claude Code is not used
- remove example skills when custom skills are unnecessary
- remove example agents when specialized agents are unnecessary
- remove unused rules
- replace `.gitkeep` files when real project files populate the directories
- replace the generic source layout when the project requires another structure

A smaller configuration that accurately represents the project is preferable to unused configuration that merely looks comprehensive.

---

# New Project Checklist

After creating a repository from this template:

- [ ] Update the repository name and description.
- [ ] Replace this README with project-specific introductory information while retaining useful operational guidance.
- [ ] Complete `docs/architecture.md`.
- [ ] Complete `docs/conventions.md`.
- [ ] Complete `docs/testing.md`.
- [ ] Review and customize `docs/ai-usage.md`.
- [ ] Review the ADR process in `docs/decisions/`.
- [ ] Decide whether Codex will be used.
- [ ] Customize or remove `AGENTS.md`.
- [ ] Customize or remove `.codex/`.
- [ ] Decide whether Claude Code will be used.
- [ ] Customize or remove `CLAUDE.md`.
- [ ] Customize or remove `.claude/`.
- [ ] Configure or remove `.mcp.json` as appropriate.
- [ ] Remove unused example agents.
- [ ] Remove unused example skills.
- [ ] Remove unused example rules.
- [ ] Remove unused example hooks.
- [ ] Define the project's source and test directory structure.
- [ ] Extend `.gitignore` for the selected technology stack.
- [ ] Extend `.editorconfig` where necessary.
- [ ] Configure dependency management.
- [ ] Configure formatting, linting, and static analysis.
- [ ] Configure project testing.
- [ ] Adapt `.github/workflows/ci.yml.example`.
- [ ] Rename the workflow to `ci.yml` when CI is ready to be enabled.
- [ ] Configure appropriate GitHub repository rules and security features.
- [ ] Review all AI tool permissions and external integrations.
- [ ] Verify that no secrets or credentials are committed.
- [ ] Remove remaining template placeholders and instructional comments.
- [ ] Perform an initial repository-wide validation.
- [ ] Commit the initialized project baseline.

---

# Contributing

Contributions are welcome.

See:

`CONTRIBUTING.md`

for the contribution workflow and:

`docs/conventions.md`

for project conventions.

AI-assisted contributions are subject to the same quality and validation requirements as manually authored contributions.

---

# License

This project is licensed under the MIT License.

See:

`LICENSE`

for the complete license text.
