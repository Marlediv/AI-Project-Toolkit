---
name: example-agent
description: Example specialized Claude Code agent. Replace with a clear description of when this agent should be used.
---

# Example Agent

<!--
PURPOSE

This file demonstrates how a specialized project-level Claude Code agent
can be defined.

Specialized agents are useful when a task benefits from a focused role,
separate context, specific tools, or narrower responsibilities.

This example does not define an actual project role.

When creating a project from this template:

1. Copy or rename this file for a concrete agent.
2. Replace the example metadata.
3. Define a narrow and useful responsibility.
4. Configure additional agent capabilities only when required.
5. Remove this example if the project does not require specialized agents.

Shared project knowledge belongs in docs/.
General Claude Code instructions belong in CLAUDE.md.
-->

## Role

<!--
Describe the specialized responsibility of this agent.

A good role should make clear:

- what the agent is responsible for
- what kinds of tasks it should handle
- what expertise or perspective it provides

Examples might include:

- reviewing database migrations
- investigating test failures
- analyzing security-sensitive changes
- reviewing API compatibility
- validating data-quality rules

Avoid creating broad roles that merely reproduce the default Claude Code
behavior.
-->

<Describe the agent's role.>

---

## When to Use

<!--
Define situations in which this specialized agent should be used.

The description in the frontmatter should provide a concise summary.
This section may provide more detailed boundaries.
-->

Use this agent when:

- <Use case>
- <Use case>

Do not use this agent when:

- <Out-of-scope situation>

---

## Responsibilities

<!--
Define what this agent is expected to do.

Keep responsibilities specific to the role.
-->

The agent is responsible for:

- <Responsibility>
- <Responsibility>
- <Responsibility>

---

## Boundaries

<!--
Define what the agent must not do or what remains outside its role.

Narrow boundaries help prevent specialized agents from expanding a task
beyond their intended responsibility.
-->

The agent should not:

- <Boundary>
- <Boundary>

---

## Required Context

<!--
Reference authoritative project sources instead of copying their contents.

Add only context that is relevant to this specialized role.
-->

Before performing work, inspect the project context relevant to the task.

Possible sources include:

- `CLAUDE.md`
- `docs/architecture.md`
- `docs/conventions.md`
- `docs/testing.md`
- `docs/ai-usage.md`
- relevant Architecture Decision Records
- relevant implementation
- relevant tests
- relevant schemas or contracts

<Add role-specific required context.>

---

## Working Method

<!--
Describe how this specialized agent should approach its work.

Keep this focused on behavior that differs from the repository-wide
instructions.
-->

1. <Step or working principle>
2. <Step or working principle>
3. <Step or working principle>

---

## Tools and Access

<!--
Optional.

Define tool requirements or restrictions when the role needs them.

Depending on the project and supported Claude Code configuration, this
may include restrictions or requirements involving:

- file access
- shell commands
- MCP tools
- external systems
- read-only versus write access

Prefer the minimum capabilities required for the role.

Access to a tool does not automatically imply authorization to modify
the system behind it.
-->

<Define role-specific tool requirements or restrictions.>

---

## Validation

<!--
General project validation remains authoritative in:

docs/testing.md

Define additional validation here only when this role requires it.
-->

Follow the project's testing and validation strategy:

`docs/testing.md`

Additional role-specific validation:

- <Validation requirement>

---

## Output

<!--
Define what the agent should return after completing its task.

Examples:

- implementation
- review findings
- diagnostic report
- risk assessment
- validation result
- recommended changes

For review-only agents, explicitly state that they should not modify
project files.
-->

The expected output is:

- <Output>
- <Output>

---

## Escalation

<!--
Define situations where the specialized agent should stop or return the
issue instead of making assumptions or expanding its authority.

Examples:

- architectural decision required
- insufficient project context
- destructive operation required
- security boundary unclear
- contradictory requirements
- required external system unavailable
-->

Escalate or report the issue when:

- <Escalation condition>
- <Escalation condition>

Do not silently resolve uncertainty by expanding the scope or authority
of the agent.

---

## Failure Handling

If the assigned task cannot be completed:

1. identify the blocking condition
2. distinguish verified facts from assumptions
3. preserve useful diagnostic or validation evidence
4. avoid unrelated or speculative changes
5. report what remains unresolved

<Add role-specific failure handling if required.>

---

## Project Knowledge

This agent should use the repository's shared sources of truth rather
than maintaining independent copies of project knowledge.

Relevant shared documentation includes:

- `docs/architecture.md`
- `docs/conventions.md`
- `docs/testing.md`
- `docs/ai-usage.md`
- `docs/decisions/`

If this agent repeatedly requires information that applies beyond its
specialized role, consider moving that information into the appropriate
shared project documentation.

---

## Customization

<!--
When turning this example into a real specialized agent:

1. Give the agent a clear and specific name.
2. Write a description that makes delegation behavior understandable.
3. Define a narrow responsibility.
4. Define explicit boundaries.
5. Grant only capabilities required for the role.
6. Reference shared project documentation instead of duplicating it.
7. Define expected output and escalation conditions.
8. Remove unused sections and instructional comments.

Delete this example file if the project does not require specialized
Claude Code agents.
-->