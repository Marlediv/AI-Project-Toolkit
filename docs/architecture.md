# Project Architecture

<!--
PURPOSE

This document describes the architecture of the project.

It is part of the shared project knowledge and should remain independent
of any specific AI coding assistant.

Both human contributors and AI agents should treat this document as the
primary source for architectural information.

Keep agent-specific instructions out of this file. Instructions for
Codex belong in AGENTS.md or .codex/. Instructions for Claude Code belong
in CLAUDE.md or .claude/.

Replace the placeholders below with project-specific information and
remove sections that are not relevant to the project.
-->

## 1. Architecture Overview

<!--
Describe the system at a high level.

Useful information may include:
- the overall architecture style
- major components
- important boundaries
- external systems
- major data flows
- deployment topology

Keep this section understandable without requiring knowledge of the
implementation details.
-->

<Describe the overall architecture of the project.>

---

## 2. Architecture Goals

<!--
Describe the qualities the architecture is intended to optimize for.

Examples may include:
- maintainability
- portability
- scalability
- simplicity
- security
- observability
- testability
- low operational complexity

Only include goals that actually matter to the project.
-->

- <Architecture goal>
- <Architecture goal>
- <Architecture goal>

---

## 3. System Context

<!--
Describe the environment in which the project operates.

Identify:
- users or actors
- external systems
- upstream dependencies
- downstream consumers
- external APIs or services

A diagram may be referenced or embedded here if useful.
-->

<Describe the system context.>

---

## 4. Major Components

<!--
Describe the major logical or physical components of the project.

Do not document every file or class here. Focus on architectural
responsibilities and boundaries.
-->

### <Component Name>

**Responsibility**

<Describe what this component is responsible for.>

**Inputs**

<Describe important inputs.>

**Outputs**

<Describe important outputs.>

**Dependencies**

<Describe important dependencies.>

---

## 5. Data Flow

<!--
Describe how information moves through the system.

For data-oriented projects this may include:
- ingestion
- validation
- transformation
- storage
- serving
- export

For application projects this may instead describe request flows,
events, messages, or other important interactions.
-->

<Describe the primary data or information flows.>

---

## 6. Project Structure

<!--
Describe the project-specific directory structure.

The template intentionally does not prescribe a particular application
architecture. Replace the example below with the actual structure of
the project.

Example:

project/
├── src/
├── tests/
├── scripts/
└── docs/
-->

<Describe the project structure and the responsibility of important directories.>

---

## 7. Technology Decisions

<!--
List important technologies and explain why they are used.

Do not merely create an inventory of dependencies. Focus on technologies
that materially influence the architecture.
-->

| Technology | Purpose | Rationale |
|------------|---------|-----------|
| <Technology> | <Purpose> | <Why it was selected> |

---

## 8. Interfaces and Integrations

<!--
Describe important interfaces between components and external systems.

Examples:
- APIs
- databases
- message brokers
- file exchanges
- MCP servers
- external services
- command-line interfaces

Do not place credentials, tokens, connection strings, or other secrets
in this document.
-->

### <Interface or Integration>

**Purpose**

<Describe the integration.>

**Direction**

<Inbound, outbound, or bidirectional.>

**Contract**

<Reference the relevant specification, schema, API documentation, or contract.>

---

## 9. Constraints

<!--
Document architectural constraints that contributors and AI agents must
respect.

Examples:
- required platforms
- portability requirements
- regulatory requirements
- compatibility requirements
- prohibited dependencies
- infrastructure limitations

These should describe constraints of the project, not instructions for
a particular AI agent.
-->

- <Constraint>
- <Constraint>

---

## 10. Security Boundaries

<!--
Describe security-relevant architectural boundaries.

Examples:
- trust boundaries
- authentication boundaries
- sensitive data locations
- privileged components
- external network boundaries

Never store actual credentials or secrets here.
-->

<Describe relevant security boundaries.>

---

## 11. Deployment and Runtime

<!--
Describe how and where the system runs.

Possible topics:
- local development
- containers
- cloud infrastructure
- on-premises infrastructure
- environments
- runtime dependencies

Remove this section if deployment is irrelevant to the project.
-->

<Describe the runtime and deployment architecture.>

---

## 12. Observability

<!--
Describe how the system can be observed and diagnosed.

Possible topics:
- logging
- metrics
- tracing
- audit information
- operational diagnostics

Remove this section if it is not relevant.
-->

<Describe the observability approach.>

---

## 13. Architectural Decisions

Significant architectural decisions should be documented separately in:

`docs/decisions/`

<!--
Use Architecture Decision Records (ADRs) for decisions that require
context, alternatives, or justification.

This keeps this document focused on the current architecture while the
decision records preserve why the architecture evolved this way.
-->

---

## 14. Known Limitations

<!--
Document known architectural limitations, technical compromises, or
areas intentionally left unresolved.

Do not hide known weaknesses. Making them explicit helps both human
contributors and AI agents avoid treating them as accidental omissions.
-->

- <Known limitation>
- <Known limitation>

---

## 15. Future Architecture

<!--
Document planned architectural changes only when they are sufficiently
concrete to influence current decisions.

Do not turn this section into a general feature wishlist.
-->

<Describe relevant planned architectural evolution, or remove this section.>

---

## Related Documentation

- [Project conventions](./conventions.md)
- [Testing strategy](./testing.md)
- [AI usage](./ai-usage.md)
- [Architecture decisions](./decisions/)