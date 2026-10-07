# AI-Assisted Development

<!--
PURPOSE

This document defines the shared principles for using AI agents within
the project.

It applies to all supported AI coding assistants and should remain
vendor-neutral wherever possible.

Project knowledge belongs in the shared documentation under docs/.
Agent-specific instructions belong in AGENTS.md, CLAUDE.md, .codex/,
or .claude/.

The purpose of this document is not to configure an AI agent. It defines
how AI-assisted work should be performed within the project.

Replace project-specific placeholders and remove sections that are not
relevant.
-->

## 1. Core Principle

AI agents are tools for working with the project. They are not the
authoritative source of project knowledge.

Authoritative project information should live in version-controlled,
human-readable project documentation and configuration.

When project documentation and an AI agent's assumptions conflict,
the documented project state takes precedence.

---

## 2. Sources of Truth

<!--
Define the authoritative sources an AI agent should consult before
making significant changes.

Avoid duplicating information between these documents.
-->

The shared project knowledge is organized as follows:

- Architecture: `docs/architecture.md`
- Project conventions: `docs/conventions.md`
- Testing and validation: `docs/testing.md`
- Architecture decisions: `docs/decisions/`

<Add additional project-specific sources of truth here.>

Agent-specific instruction files may reference these sources but should
not unnecessarily duplicate their contents.

---

## 3. Supported AI Agents

<!--
List the AI coding assistants intentionally supported by the project.

Remove entries that are not used by the project.
-->

### Codex

Project-level instructions:

`AGENTS.md`

Project-specific configuration:

`.codex/`

### Claude Code

Project-level instructions:

`CLAUDE.md`

Project-specific configuration:

`.claude/`

<!--
Additional AI agents may be documented here.

When adding another agent, prefer adapting it to the existing shared
project knowledge rather than creating another independent copy of the
project rules.
-->

---

## 4. Responsibility Model

<!--
Define the relationship between human contributors and AI agents.

The exact level of autonomy may vary by project.
-->

AI agents may assist with activities such as:

- analysis
- implementation
- refactoring
- testing
- documentation
- code review
- debugging
- research
- repetitive project maintenance

AI assistance does not remove the need for validation.

The contributor responsible for a change remains responsible for
understanding its impact and ensuring that required validation has
been performed.

<Add project-specific responsibility rules if required.>

---

## 5. Working with Project Context

Before making significant changes, an AI agent should identify and
consult the relevant project context.

Depending on the task, this may include:

- architecture documentation
- project conventions
- testing strategy
- architecture decision records
- existing implementation
- tests
- schemas and contracts
- configuration
- related issues or pull requests

The agent should not assume that general ecosystem conventions override
explicit project conventions.

---

## 6. Scope Discipline

AI-assisted changes should remain within the intended scope of the task.

Avoid unrelated:

- refactoring
- formatting changes
- dependency updates
- file restructuring
- API changes
- configuration changes

when they are not required to complete the requested work.

If additional changes are necessary, their relationship to the task
should be made explicit.

---

## 7. Assumptions and Uncertainty

AI agents should distinguish between:

- verified facts
- documented project decisions
- reasonable assumptions
- unresolved uncertainty

Important assumptions should be stated rather than silently treated as
facts.

When missing information materially affects correctness, the uncertainty
should be surfaced before irreversible or high-impact changes are made.

---

## 8. Change Strategy

<!--
Define general expectations for how AI agents should modify the project.
-->

Prefer:

- focused changes
- small reviewable diffs
- existing project patterns
- reversible changes where practical
- explicit reasoning for significant architectural changes

Avoid replacing working implementations solely because another approach
appears stylistically preferable.

Architectural changes should follow the project's decision process and,
where appropriate, be documented in `docs/decisions/`.

---

## 9. Validation

AI-generated or AI-assisted changes must follow the same validation
requirements as human-authored changes.

The authoritative testing and validation strategy is defined in:

`docs/testing.md`

An AI agent must not claim that:

- tests passed
- a build succeeded
- a command completed successfully
- an integration works
- a defect is resolved

unless the relevant validation was actually performed and the result is
known.

If validation could not be performed, this must be reported explicitly.

---

## 10. Failure Handling

When an implementation, test, command, or integration fails, the agent
should investigate the cause before attempting broad corrective changes.

Do not:

- remove valid tests merely to make a suite pass
- weaken validation without justification
- suppress errors without understanding their cause
- repeatedly apply speculative fixes without reassessing the problem

Prefer identifying the failure mode and making the smallest justified
correction.

---

## 11. Documentation

AI-assisted changes should update documentation when they change:

- architecture
- behavior
- interfaces
- configuration
- workflows
- operational requirements
- important project conventions

Do not duplicate information when an authoritative document already
exists.

Update the authoritative source and reference it where necessary.

---

## 12. Generated Content

<!--
Define how AI-generated artifacts should be treated.

Possible artifacts:
- source code
- tests
- documentation
- configuration
- SQL
- schemas
- migration files
- scripts
-->

AI-generated content should be treated as project content, not as
automatically trusted output.

It should meet the same quality, security, documentation, and validation
requirements as manually created content.

<Add project-specific requirements if needed.>

---

## 13. Security and Sensitive Information

AI agents must not intentionally place secrets or sensitive credentials
in version-controlled files.

Examples include:

- passwords
- API keys
- access tokens
- private keys
- authentication cookies
- confidential connection strings

Use the project's approved secret-management mechanism instead.

<!--
Projects handling confidential, regulated, personal, or otherwise
sensitive information should define additional requirements here or
reference dedicated security documentation.
-->

<Add project-specific security requirements.>

---

## 14. External Tools and Services

<!--
Document general rules for AI access to external systems.

Examples:
- MCP servers
- databases
- APIs
- cloud environments
- issue trackers
- CI systems
- file systems
-->

Access to an external system does not automatically imply permission to
modify it.

Read and write operations should be treated separately.

Potentially destructive, irreversible, production-affecting, or
security-sensitive operations require the level of authorization defined
by the project.

<Define project-specific authorization boundaries.>

---

## 15. MCP

<!--
Model Context Protocol (MCP) may provide AI agents with access to external
tools and data sources.

Agent-specific MCP configuration may differ between supported AI tools.
Keep shared usage principles here and tool-specific configuration in the
appropriate agent configuration.
-->

MCP integrations should:

- have a clear project purpose
- use the minimum permissions required
- avoid embedding secrets in version-controlled configuration
- distinguish read access from write access
- document important external dependencies

Project-specific MCP configuration may be defined through the supported
agent configuration mechanisms.

---

## 16. Skills, Agents, and Hooks

<!--
Supported AI tools may provide different extension mechanisms.

Examples include:
- reusable skills
- specialized subagents
- lifecycle hooks

Their exact implementation belongs in `.agents/`, `.codex/`, or `.claude/`.
For reusable Claude Code workflows, use Skills under `.claude/skills/`.
-->

Extensions should exist to solve a clear project need.

Avoid creating multiple mechanisms that encode the same project rule.

Shared project knowledge should remain in `docs/` rather than being
duplicated across skills, agents, and hooks.

---

## 17. Human Review

<!--
Define which changes require human review.

The appropriate level depends on project risk and governance.
-->

Consider requiring explicit human review for changes involving:

- architecture
- security boundaries
- authentication or authorization
- production infrastructure
- destructive data operations
- dependency trust
- external system writes
- irreversible migrations

<Define project-specific review requirements.>

---

## 18. High-Risk and Irreversible Operations

<!--
Define operations where AI autonomy should be restricted.

Examples:
- deleting production data
- destructive database migrations
- force pushes
- credential rotation
- infrastructure destruction
- production deployment
- external communication
-->

Before performing a high-risk or irreversible operation, the agent should:

1. identify the operation
2. explain the expected impact
3. verify required prerequisites
4. confirm that the operation is authorized
5. prefer a reversible or dry-run approach when available

<Define project-specific high-risk operations.>

---

## 19. Completion Reporting

When reporting completed work, an AI agent should clearly distinguish:

### Changed

What was actually modified.

### Validated

What was actually tested or verified.

### Not Validated

What could not be tested or verified.

### Remaining Issues

Known limitations, risks, follow-up work, or unresolved questions.

The completion report should not imply greater confidence than the
available evidence supports.

---

## 20. Agent-Specific Instructions

Shared project principles belong in this document.

Agent-specific behavior belongs in:

### Codex

- `AGENTS.md`
- `.codex/`

### Claude Code

- `CLAUDE.md`
- `.claude/`

Agent-specific files should reference shared documentation rather than
maintaining independent copies of project rules.

---

## Customization

<!--
When creating a new project from this template:

1. Review every section of this document.
2. Replace project-specific placeholders.
3. Remove sections that are not relevant.
4. Define authorization and review boundaries.
5. Remove configuration for AI agents that the project does not use.
6. Keep shared rules vendor-neutral whenever practical.

The goal is not to preserve this template unchanged.
The goal is to create a clear AI collaboration model for the project.
-->

<Add additional project-specific AI collaboration rules here.>

---

## Related Documentation

- [Project architecture](./architecture.md)
- [Project conventions](./conventions.md)
- [Testing strategy](./testing.md)
- [Architecture decisions](./decisions/)
