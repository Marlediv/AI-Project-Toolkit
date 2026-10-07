# CLAUDE.md

<!--
PURPOSE

This file is the primary project-level instruction entry point for
Claude Code.

It should remain concise and point Claude Code to the authoritative
project documentation rather than duplicating that documentation here.

Shared project knowledge belongs in docs/.
Claude Code-specific configuration and extensions belong in .claude/.

Customize this file when creating a project from the template.
Remove instructions that are not relevant and add project-specific
Claude Code guidance only where necessary.
-->

## Project Context

Before making significant changes, read the project documentation relevant
to the task.

The shared project knowledge is maintained in:

- Architecture: `docs/architecture.md`
- Project conventions: `docs/conventions.md`
- Testing and validation: `docs/testing.md`
- AI-assisted development principles: `docs/ai-usage.md`
- Architecture decisions: `docs/decisions/`

Treat these files as authoritative for their respective concerns.

Do not duplicate their contents in this file unless Claude Code requires
a specific instruction that cannot be expressed appropriately in the shared
documentation.

---

## Working Principles

When working in this repository:

1. Understand the relevant context before modifying files.
2. Follow the existing architecture and project conventions.
3. Keep changes focused on the requested task.
4. Prefer existing project patterns over introducing new ones.
5. Do not make unrelated refactors or dependency changes.
6. State important assumptions when information is incomplete.
7. Preserve existing behavior unless changing it is part of the task.
8. Update authoritative documentation when a change affects documented
   behavior, architecture, interfaces, or workflows.

For broader AI collaboration principles, follow:

`docs/ai-usage.md`

---

## Planning

<!--
Customize the planning expectations for the project if necessary.

Not every small change requires a formal plan. The goal is to ensure that
non-trivial work is understood before implementation begins.
-->

For non-trivial changes:

1. identify the affected components
2. inspect relevant implementation and tests
3. identify applicable project documentation and ADRs
4. determine the required validation
5. consider risks, dependencies, and compatibility impact
6. implement the smallest coherent change that satisfies the task

Do not begin broad architectural changes without first understanding the
existing architecture and relevant decisions.

---

## Scope

Stay within the scope of the requested task.

Do not perform unrelated:

- refactoring
- formatting changes
- dependency upgrades
- file moves
- API changes
- configuration changes
- architectural changes

If an out-of-scope change is required to complete the task correctly,
make the dependency explicit.

---

## Implementation

<!--
Add Claude Code-specific implementation guidance here only when it cannot
be expressed through the shared project conventions.
-->

During implementation:

- prefer small, reviewable changes
- preserve established project patterns
- avoid unnecessary abstractions
- avoid introducing dependencies without clear justification
- keep generated and handwritten files consistent with project conventions
- do not modify unrelated files merely for stylistic consistency

Project-wide implementation conventions are defined in:

`docs/conventions.md`

---

## Testing and Validation

All changes must follow the testing and validation strategy defined in:

`docs/testing.md`

Select validation appropriate to the scope and risk of the change.

Do not claim that:

- tests passed
- a build succeeded
- a command succeeded
- an integration works
- a defect is fixed

unless the relevant validation was actually executed and its result is known.

If validation cannot be completed, report:

- what was validated
- what was not validated
- why it could not be validated
- any remaining risk or uncertainty

Do not weaken, remove, skip, or rewrite valid tests merely to make a change
appear successful.

---

## Failures

When a command, test, build, or integration fails:

1. inspect the failure
2. identify the likely cause
3. distinguish implementation failures from environment or test failures
4. make the smallest justified correction
5. rerun the relevant validation

Do not repeatedly apply speculative changes without reassessing the
underlying problem.

---

## Architecture

Follow the architecture documented in:

`docs/architecture.md`

Significant architectural changes should be documented through the
project's decision process.

Architecture Decision Records are stored in:

`docs/decisions/`

Use `docs/decisions/0000-template.md` as the starting point for new ADRs.

Do not create an ADR for routine implementation details that do not
represent a meaningful architectural or technical decision.

---

## External Systems and Tools

<!--
Claude Code may have access to external tools through MCP servers or
other configured integrations.

Project-scoped MCP configuration may be defined in .mcp.json.
Claude Code-specific permissions and behavior belong in .claude/.
-->

Access to a tool or external system does not automatically imply permission
to modify it.

Before performing operations that affect external systems:

- determine whether access is read-only or writable
- understand the expected impact
- respect project authorization boundaries
- prefer read-only inspection when modification is unnecessary
- prefer dry-run or reversible operations when available

Do not expose or commit credentials, tokens, private keys, or other secrets.

---

## High-Risk Operations

Do not perform destructive, irreversible, production-affecting, or
security-sensitive operations merely because the required tool access
is available.

Examples may include:

- deleting data
- destructive migrations
- force pushes
- production deployments
- infrastructure destruction
- credential changes
- modifying production systems
- external communication on behalf of a user or organization

Follow the authorization and review requirements defined in
`docs/ai-usage.md`.

<!--
Add stricter project-specific restrictions here where necessary.
-->

---

## Claude Code Configuration

Claude Code-specific project configuration is stored in:

`.claude/`

The template may provide:

- `.claude/settings.json` for project-level settings
- `.claude/rules/` for scoped or modular instructions
- `.claude/skills/` for reusable capabilities
- `.claude/commands/` for project commands
- `.claude/agents/` for specialized subagents
- `.claude/hooks/` for project hook implementations

Project-scoped MCP configuration may additionally be defined in:

`.mcp.json`

These mechanisms should extend Claude Code behavior without becoming
duplicate sources of shared project knowledge.

---

## Rules

<!--
Claude Code rules may provide additional instructions for specific parts
of the project.

Use them when instructions genuinely need narrower scope than CLAUDE.md.
-->

Project-specific rules may be stored in:

`.claude/rules/`

Rules should complement this file and the shared documentation rather than
restate them.

Prefer a scoped rule when guidance applies only to a particular part of
the repository.

---

## Skills and Commands

<!--
Skills and commands provide reusable workflows or capabilities.

Keep durable project knowledge in docs/ rather than embedding independent
copies of project rules into each skill or command.
-->

Reusable Claude Code capabilities may be stored in:

- `.claude/skills/`
- `.claude/commands/`

Use these mechanisms for repeatable tasks and workflows rather than as
alternative documentation stores.

---

## Specialized Agents

<!--
Specialized Claude Code subagents may be useful when a project benefits
from focused roles or isolated task contexts.
-->

Specialized agents may be defined in:

`.claude/agents/`

Create specialized agents only when they provide a clear advantage over
the default project instructions.

They should reference shared project knowledge where appropriate instead
of maintaining independent copies of it.

---

## Hooks

<!--
Hooks may automate checks or actions around Claude Code lifecycle events.

Keep hook behavior focused, predictable, and visible to project
contributors.
-->

Claude Code hook implementations may be stored in:

`.claude/hooks/`

Hook configuration should remain consistent with the project's Claude Code
settings and should not silently weaken validation or security controls.

Avoid using hooks for behavior that is better expressed as project
documentation, tests, or normal automation.

---

## Instruction Structure

This root `CLAUDE.md` defines the default Claude Code instructions for the
repository.

Use `.claude/rules/` when additional instructions genuinely require more
specific scope or modular organization.

Avoid creating multiple instruction layers that encode the same rule.

When guidance applies equally to humans, Codex, Claude Code, and other
tools, it probably belongs in `docs/` rather than here.

---

## Completion

Before reporting a task as complete:

1. confirm that the requested scope has been addressed
2. review the resulting changes for unintended modifications
3. execute the required validation from `docs/testing.md`
4. update relevant documentation when necessary
5. identify unresolved issues or uncertainty
6. report the actual validation status

A completion report should distinguish between:

### Changed

What was actually modified.

### Validated

What was actually tested or verified.

### Not Validated

What could not be tested or verified.

### Remaining Issues

Known limitations, risks, follow-up work, or unresolved questions.

Do not imply greater confidence than the available evidence supports.

---

## Project-Specific Claude Code Instructions

<!--
Add project-specific Claude Code instructions here only when they are
genuinely specific to Claude Code.

Before adding a rule here, ask whether it belongs instead in:

- docs/architecture.md
- docs/conventions.md
- docs/testing.md
- docs/ai-usage.md
- an Architecture Decision Record
- .claude/settings.json
- a Claude Code rule
- a skill
- a command
- a specialized agent
- a hook

Keeping shared knowledge out of CLAUDE.md makes the project easier to use
with multiple AI coding assistants.
-->

<Add project-specific Claude Code instructions here, or remove this section.>