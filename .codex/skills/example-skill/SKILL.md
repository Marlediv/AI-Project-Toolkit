---
name: example-skill
description: Example project skill demonstrating the structure of a reusable Codex skill.
---

# Example Skill

<!--
PURPOSE

This is an example project-level Codex skill.

It demonstrates where reusable, task-specific instructions can be stored
without turning the skill into another source of general project knowledge.

When creating a project from this template:

1. Copy or rename this directory for a concrete skill.
2. Replace the example metadata and instructions.
3. Add supporting files only when they are useful to the skill.
4. Remove this example if the project does not require custom skills.

Shared project knowledge belongs in docs/.
General Codex instructions belong in AGENTS.md.
-->

## Purpose

<!--
Describe the capability this skill provides.

A skill should represent a reusable task, workflow, or specialized body
of instructions.

Examples may include:

- validating a database migration
- generating a release summary
- analyzing a data-quality report
- reviewing an API contract
- preparing a deployment checklist

Keep the purpose narrow enough that it is clear when the skill should
and should not be used.
-->

<Describe what this skill does.>

---

## When to Use

<!--
Describe situations in which this skill is appropriate.

This helps distinguish the skill from general project instructions and
from other specialized skills.
-->

Use this skill when:

- <Trigger or use case>
- <Trigger or use case>

Do not use this skill when:

- <Out-of-scope situation>

---

## Required Context

<!--
List information that should be inspected before performing the skill.

Reference authoritative project documentation instead of copying it.
-->

Before performing this skill, inspect the project context relevant to
the task.

Possible sources include:

- `AGENTS.md`
- `docs/architecture.md`
- `docs/conventions.md`
- `docs/testing.md`
- `docs/ai-usage.md`
- relevant Architecture Decision Records
- relevant implementation and tests

<Add skill-specific required context.>

---

## Inputs

<!--
Describe the information or artifacts required by the skill.

Examples:

- source files
- issue description
- migration script
- schema
- test output
- diff
- configuration
-->

- <Required input>
- <Required input>

---

## Procedure

<!--
Describe the reusable workflow.

Keep the procedure focused on this skill.

Do not repeat general project rules already defined elsewhere.
-->

1. <Step>
2. <Step>
3. <Step>
4. <Step>

---

## Validation

<!--
Describe validation that is specific to this skill.

General project validation requirements remain authoritative in
docs/testing.md.
-->

Follow the project's testing and validation strategy:

`docs/testing.md`

In addition:

- <Skill-specific validation>
- <Skill-specific validation>

---

## Output

<!--
Describe what the skill should produce.

Examples:

- implementation changes
- review findings
- validation results
- generated artifact
- structured report

Be explicit when the skill should not modify files.
-->

The expected output is:

- <Output>
- <Output>

---

## Constraints

<!--
Document restrictions specific to this skill.

Do not duplicate general project security, scope, or authorization rules
unless the skill requires a stricter constraint.
-->

- <Constraint>
- <Constraint>

---

## Failure Handling

<!--
Describe skill-specific behavior when the workflow cannot be completed.

Examples:

- missing required input
- unavailable external dependency
- failed validation
- ambiguous result

Do not silently treat incomplete execution as success.
-->

If the skill cannot be completed:

1. identify the blocking condition
2. preserve any useful validation evidence
3. avoid speculative or destructive workarounds
4. report what remains unresolved

<Add skill-specific failure behavior if required.>

---

## Resources

<!--
Optional.

A skill may use supporting resources when the workflow benefits from them.

Depending on the skill, these may include project-local:

- scripts
- references
- templates
- examples
- schemas

Keep supporting resources with the skill when they exist specifically
for that skill.

Do not copy general project documentation into the skill directory.
-->

<Reference supporting resources, or remove this section.>

---

## Customization

<!--
When turning this example into a real project skill:

1. Give the skill a clear and specific name.
2. Write a description that makes its purpose discoverable.
3. Define clear usage boundaries.
4. Reference shared project documentation instead of duplicating it.
5. Add supporting resources only when they provide concrete value.
6. Remove all unused template sections and instructional comments.

Delete the entire example-skill directory if the project does not need
custom Codex skills.
-->