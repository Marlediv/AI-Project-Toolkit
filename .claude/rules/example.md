---
paths:
  - "<path-or-glob>"
---

# Example Scoped Rule

<!--
PURPOSE

This file demonstrates how project-specific Claude Code rules can be
organized under .claude/rules/.

Rules are useful when additional instructions apply only to a specific
part of the repository or when Claude-specific guidance benefits from
being separated into a focused module.

This example is not intended to define an actual project rule.

When creating a project from this template:

1. Copy or rename this file for a concrete rule.
2. Replace the example path pattern with the intended scope.
3. Replace the placeholder instructions with actual guidance.
4. Remove the paths frontmatter when the rule should apply globally.
5. Remove this example if the project does not require additional rules.

Shared project knowledge belongs in docs/.
General Claude Code instructions belong in CLAUDE.md.
-->

## Scope

<!--
The paths frontmatter determines when this rule applies.

Use path patterns that are narrow enough to represent the intended scope.

Examples of possible scopes might include:

- source files for a particular component
- database migrations
- API definitions
- infrastructure configuration
- tests
- documentation

Do not use a scoped rule merely to duplicate instructions that already
apply to the entire project.
-->

This rule applies to:

`<Describe the affected part of the repository.>`

---

## Instructions

<!--
Define only the additional behavior required for this scope.

Good scoped instructions describe requirements that genuinely differ
from the repository-wide defaults.

Examples may include:

- component-specific implementation constraints
- framework-specific conventions
- migration safety requirements
- API compatibility requirements
- generated-file restrictions

Do not repeat architecture, conventions, testing requirements, or AI
collaboration principles that are already defined in shared documentation.
-->

- <Scoped instruction>
- <Scoped instruction>
- <Scoped instruction>

---

## Relevant Context

<!--
Reference authoritative project documentation when the rule depends on it.

Do not copy the documentation into this file.
-->

Consult the relevant shared project documentation:

- `docs/architecture.md`
- `docs/conventions.md`
- `docs/testing.md`
- `docs/ai-usage.md`

<Add additional context relevant to this rule.>

---

## Validation

<!--
Add validation requirements here only when this scope requires something
beyond the general testing strategy.

General validation requirements remain authoritative in:

docs/testing.md
-->

Follow the project's testing and validation strategy.

Additional validation for this scope:

- <Additional validation requirement>

---

## Exceptions

<!--
Optional.

Document exceptions only when this scoped rule requires them.
Remove this section when it is not needed.
-->

<Describe any scope-specific exceptions.>

---

## Customization

<!--
When turning this example into a real rule:

1. Give the file a descriptive name.
2. Define the narrowest useful path scope.
3. Remove the paths frontmatter if the rule should apply globally.
4. Keep instructions specific to the purpose of the rule.
5. Reference shared documentation instead of duplicating it.
6. Remove unused sections and instructional comments.

Delete this example file if the project does not require additional
Claude Code rules.
-->