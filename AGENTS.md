# AGENTS.md

<!--
PURPOSE

This file is the primary project-level instruction entry point for Codex.

It should remain concise and point Codex to the authoritative project
documentation rather than duplicating that documentation here.

Shared project knowledge belongs in docs/.
Codex-specific configuration and extensions belong in .codex/.

Customize this file when creating a project from the template.
Remove instructions that are not relevant and add project-specific
Codex guidance only where necessary.
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

Do not duplicate their contents in this file unless Codex requires a
specific instruction that cannot be expressed appropriately in the shared
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
Add Codex-specific implementation guidance here only when it cannot be
expressed through the shared project conventions.
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
Codex may have access to external tools through MCP servers or other
configured integrations.

Project-specific MCP configuration for Codex belongs in .codex/config.toml.
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

## Codex Configuration

Codex-specific project configuration is stored in:

`.codex/`

The template may provide:

- `.codex/config.toml` for project-level Codex configuration
- `.codex/hooks.json` for hook configuration
- `.codex/agents/` for specialized agent definitions
- `.codex/skills/` for reusable project skills

These mechanisms should extend Codex behavior without becoming duplicate
sources of shared project knowledge.

---

## Instruction Hierarchy

<!--
Keep this section focused on project intent.

Codex may support additional instruction discovery or override mechanisms.
Those mechanisms should be used deliberately and documented when introduced.
-->

This root `AGENTS.md` defines the default Codex instructions for the
repository.

More specific instructions may be introduced for a project when different
parts of the repository genuinely require different behavior.

Avoid adding additional instruction files unless the scope difference is
intentional and useful.

Do not create `AGENTS.override.md` merely as part of the template setup.
Use override behavior only when a concrete project requires it.

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

## Project-Specific Codex Instructions

<!--
Add project-specific Codex instructions here only when they are genuinely
specific to Codex.

Before adding a rule here, ask whether it belongs instead in:

- docs/architecture.md
- docs/conventions.md
- docs/testing.md
- docs/ai-usage.md
- an Architecture Decision Record
- .codex/config.toml
- a Codex skill
- a specialized Codex agent

Keeping shared knowledge out of AGENTS.md makes the project easier to use
with multiple AI coding assistants.
-->

<Add project-specific Codex instructions here, or remove this section.>