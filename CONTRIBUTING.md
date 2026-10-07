# Contributing

Thank you for contributing to this project.

This repository is designed to support both human and AI-assisted
development. Contributions are evaluated by the same project standards
regardless of whether AI tools were involved in creating them.

This document describes the general contribution workflow.

Project-specific requirements are defined in the shared documentation
under `docs/`.

---

## 1. Before You Start

Before making a significant change, review the project documentation
relevant to your task.

The primary sources of project knowledge are:

- Architecture: `docs/architecture.md`
- Project conventions: `docs/conventions.md`
- Testing and validation: `docs/testing.md`
- AI-assisted development: `docs/ai-usage.md`
- Architecture decisions: `docs/decisions/`

Do not assume that ecosystem defaults or personal preferences override
explicit project conventions.

---

## 2. Understand the Scope

Keep changes focused on a clear purpose.

Before implementation, identify:

- what should change
- what should remain unchanged
- which components are affected
- which tests or validation are required
- whether documentation must be updated
- whether an architectural decision is involved

Avoid combining unrelated refactoring, dependency updates, formatting,
or structural changes with the primary contribution unless they are
required for the change.

---

## 3. Issues

<!--
Customize this section to match the project's issue workflow.

Projects that do not use GitHub Issues may remove or replace this section.
-->

Use issues when they help document, discuss, or track work.

Before creating a new issue:

- check whether the topic is already tracked
- provide enough context to understand the problem or proposal
- distinguish observed behavior from assumptions
- include reproduction information when reporting defects
- describe the intended outcome where possible

A contribution does not necessarily require an issue unless the project
defines that requirement.

---

## 4. Branches

Branch naming and lifecycle conventions are defined in:

`docs/conventions.md`

<!--
If the project adopts a specific branch workflow, document or reference
it here.

Avoid duplicating detailed branch rules when docs/conventions.md is the
authoritative source.
-->

Create changes on an appropriate branch unless the project workflow
explicitly permits direct changes to the target branch.

Keep branches focused on one coherent piece of work where practical.

---

## 5. Implementing Changes

Follow the project architecture and conventions while implementing a
change.

Prefer:

- focused changes
- small and reviewable diffs
- established project patterns
- explicit handling of edge cases
- minimal necessary dependencies
- updates to affected documentation

Avoid:

- unrelated cleanup
- unnecessary abstractions
- silent behavior changes
- speculative compatibility changes
- replacing working implementations solely for stylistic reasons

If the requested change requires a broader modification than originally
expected, make that relationship explicit.

---

## 6. Architecture Decisions

Significant architectural or technical decisions should be documented
when their context and rationale are likely to matter in the future.

Architecture Decision Records are stored in:

`docs/decisions/`

Use:

`docs/decisions/0000-template.md`

as the starting point for a new decision record.

Routine implementation details generally do not require an ADR.

---

## 7. Testing and Validation

All contributions must follow the project's testing and validation
strategy:

`docs/testing.md`

Validation should be appropriate to the scope and risk of the change.

Do not report validation as successful unless it was actually performed.

When validation cannot be completed, document:

- what was validated
- what was not validated
- why it could not be validated
- any remaining uncertainty or risk

Do not remove, weaken, skip, or rewrite valid tests merely to make a
change pass.

---

## 8. Documentation

Update documentation when a contribution changes information that
contributors, users, operators, or AI agents rely on.

This may include changes to:

- architecture
- behavior
- interfaces
- configuration
- workflows
- dependencies
- operational requirements
- project conventions

Update the authoritative source rather than duplicating the same
information across multiple files.

---

## 9. Dependencies

New dependencies should be introduced deliberately.

Before adding a dependency, consider:

- whether it is necessary
- whether existing project capabilities can satisfy the requirement
- maintenance status
- security implications
- licensing
- portability
- compatibility
- operational impact

Follow the dependency-management conventions defined in:

`docs/conventions.md`

Dependency changes should remain within the scope of the contribution.

---

## 10. Secrets and Sensitive Information

Do not commit secrets or credentials.

This includes:

- passwords
- API keys
- access tokens
- private keys
- authentication cookies
- confidential connection strings

Use the project's approved configuration and secret-management
mechanisms.

If sensitive information is accidentally committed, removing it in a
later commit may not be sufficient because it can remain in Git history.

Follow the project's security and incident procedures where applicable.

---

## 11. AI-Assisted Contributions

AI-assisted contributions are welcome when they follow the same project
standards as other contributions.

The shared principles for AI-assisted development are defined in:

`docs/ai-usage.md`

Project-level AI instructions are available through:

### Codex

- `AGENTS.md`
- `.codex/`

### Claude Code

- `CLAUDE.md`
- `.claude/`
- `.mcp.json` where project MCP configuration is used

Using an AI assistant does not make generated output automatically
correct or project-compliant.

AI-assisted changes must still be:

- understood sufficiently for responsible review
- scoped appropriately
- validated
- reviewed for unintended changes
- documented where necessary

Do not commit secrets or sensitive information through prompts,
generated configuration, logs, transcripts, or tool output.

---

## 12. Commits

Follow the commit conventions defined in:

`docs/conventions.md`

Commits should make the history understandable.

Where practical:

- keep commits focused
- avoid mixing unrelated changes
- use meaningful commit messages
- do not include generated or temporary files unintentionally

<!--
Add project-specific requirements such as Conventional Commits only if
the project actually adopts them.
-->

---

## 13. Pull Requests

<!--
Customize this section to match the project's review and merge workflow.
-->

Before opening a pull request:

- review the complete diff
- remove unintended changes
- perform the required validation
- update relevant documentation
- identify known limitations or unresolved issues
- confirm that no secrets or sensitive information were introduced

A pull request should explain:

- what changed
- why the change was made
- how it was validated
- what was not validated
- relevant risks or limitations
- related issues or decisions where applicable

Keep pull requests focused enough to be reviewed effectively.

---

## 14. Review

Review should focus on the contribution itself rather than whether the
implementation was written manually or with AI assistance.

Relevant review areas may include:

- correctness
- scope
- architecture
- maintainability
- security
- compatibility
- tests
- documentation
- unintended behavior

Review findings should distinguish required corrections from optional
suggestions where practical.

---

## 15. Merge

Merge strategy and branch requirements are defined by the project
configuration and:

`docs/conventions.md`

Do not merge a change solely because automated checks are green.

Automated validation provides evidence. It does not replace appropriate
review and judgment.

<!--
Projects may define required reviews, protected branches, required
status checks, or additional merge conditions.
-->

---

## 16. After Merge

<!--
Remove or customize this section when the project has no relevant
post-merge workflow.
-->

After a change is merged, verify any required follow-up activities.

These may include:

- deployment
- release preparation
- migration execution
- monitoring
- issue closure
- documentation publication
- cleanup of temporary resources

Do not assume that merging a change automatically completes operational
work outside the repository.

---

## Project-Specific Contribution Requirements

<!--
Add contribution requirements that are specific to this project.

Before adding information here, consider whether it belongs instead in:

- docs/architecture.md
- docs/conventions.md
- docs/testing.md
- docs/ai-usage.md
- docs/decisions/

Keep this section focused on the contribution workflow rather than
turning CONTRIBUTING.md into another general project specification.
-->

<Add project-specific contribution requirements here, or remove this section.>