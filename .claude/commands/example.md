---
description: Example project command demonstrating a reusable Claude Code workflow.
argument-hint: "<optional arguments>"
---

# Example Command

<!--
PURPOSE

This file demonstrates how a reusable project command can be defined
for Claude Code.

Commands are appropriate for workflows that a user intentionally invokes.

This example does not implement an actual project workflow.

When creating a project from this template:

1. Copy or rename this file for a concrete command.
2. Replace the example metadata.
3. Define the workflow the command should perform.
4. Define arguments only when the command requires them.
5. Remove this example if the project does not require custom commands.

Shared project knowledge belongs in docs/.
General Claude Code instructions belong in CLAUDE.md.
Automatically applicable instructions belong in .claude/rules/.
-->

## Purpose

<!--
Describe the task this command performs.

Good commands represent deliberate, repeatable actions.

Examples may include:

- preparing a release
- reviewing a migration
- generating a changelog
- running a project health check
- analyzing test failures
- preparing a pull request summary

Avoid creating commands for behavior that should happen automatically.
-->

<Describe what this command does.>

---

## Arguments

<!--
Describe arguments accepted by the command.

Remove this section and the argument-hint frontmatter if the command
does not require arguments.

Document:
- expected arguments
- optional arguments
- accepted formats
- relevant defaults

Do not silently guess required values when doing so could materially
change the result.
-->

<Describe the accepted arguments.>

---

## Required Context

<!--
Define what Claude should inspect before performing the command.

Reference authoritative project sources rather than duplicating them.
-->

Before executing this command, inspect the context relevant to the task.

Possible sources include:

- `CLAUDE.md`
- `docs/architecture.md`
- `docs/conventions.md`
- `docs/testing.md`
- `docs/ai-usage.md`
- relevant Architecture Decision Records
- relevant implementation and tests
- command arguments supplied by the user

<Add command-specific required context.>

---

## Procedure

<!--
Define the workflow performed when the command is invoked.

Keep the procedure deterministic where practical.

Do not duplicate general project instructions already defined elsewhere.
-->

1. <Step>
2. <Step>
3. <Step>
4. <Step>

---

## Validation

<!--
Describe validation specific to this command.

General testing requirements remain authoritative in:

docs/testing.md
-->

Follow the project's testing and validation strategy where the command
modifies or evaluates project behavior.

Additional command-specific validation:

- <Validation requirement>

---

## Output

<!--
Describe what should be returned or produced after successful execution.

Examples:

- structured analysis
- implementation changes
- generated documentation
- validation report
- summary
- checklist

Be explicit when the command is intended to be read-only.
-->

The command should produce:

- <Expected output>
- <Expected output>

---

## Side Effects

<!--
Explicitly document whether the command may modify files or external systems.

This section is important for commands that may have effects beyond
producing a response.
-->

This command:

- <Does or does not modify repository files>
- <Does or does not execute project commands>
- <Does or does not access external systems>
- <Does or does not modify external systems>

---

## Failure Handling

<!--
Describe what should happen when the workflow cannot be completed.

Do not report partial or failed execution as success.
-->

If the command cannot be completed:

1. identify the blocking condition
2. preserve useful diagnostic information
3. avoid destructive or speculative workarounds
4. report completed and incomplete steps separately

<Add command-specific failure handling if required.>

---

## Safety and Authorization

<!--
Optional.

Use this section when the command can perform operations that require
specific authorization.

Examples:

- modifying external systems
- deploying software
- deleting data
- publishing content
- changing infrastructure

Remove this section for commands without meaningful side effects.
-->

<Define command-specific authorization requirements.>

---

## Customization

<!--
When turning this example into a real command:

1. Give the command file a descriptive name.
2. Write a clear description.
3. Define arguments only when they are useful.
4. Keep the workflow focused on one coherent task.
5. Document side effects explicitly.
6. Reference shared project documentation instead of duplicating it.
7. Remove unused sections and instructional comments.

Delete this example file if the project does not require custom
Claude Code commands.
-->