# Project Conventions

<!--
PURPOSE

This document defines the shared conventions for contributing to the project.

These conventions apply to all contributors, including humans and AI agents.

Keep this document independent of any specific AI coding assistant.
Agent-specific behavior belongs in AGENTS.md, CLAUDE.md, .codex/, or .claude/.

Architecture decisions belong in architecture.md or docs/decisions/.
Testing-specific conventions belong in testing.md.

Replace the placeholders below with project-specific conventions and
remove sections that are not relevant to the project.
-->

## 1. General Principles

<!--
Define the fundamental principles contributors should follow when
working on the project.

Examples may include:
- prefer simple solutions over unnecessary abstraction
- preserve existing behavior unless a change is intentional
- keep changes focused on the requested scope
- avoid unnecessary dependencies
- document non-obvious decisions

Only include principles that should genuinely apply to the project.
-->

- <Principle>
- <Principle>
- <Principle>

---

## 2. Naming Conventions

<!--
Define naming rules used throughout the project.

Depending on the technology stack, this may include:
- files and directories
- variables
- functions or methods
- classes
- database objects
- API resources
- configuration keys
- environment variables

Avoid defining conventions for technologies the project does not use.
-->

### Files and Directories

<Define naming conventions for files and directories.>

### Code

<Define naming conventions for code elements.>

### Data and Database Objects

<!-- Remove if not applicable. -->

<Define naming conventions for tables, columns, schemas, models, or datasets.>

---

## 3. Code Style

<!--
Define project-wide expectations for code style.

Prefer automated formatters and linters where appropriate instead of
documenting formatting rules manually.

Possible topics:
- formatting
- imports
- type annotations
- comments
- function or method size
- module organization
- language-specific style guides

Reference configuration files when possible rather than duplicating them.
-->

<Describe the project's code style conventions.>

### Automated Formatting

<!--
Reference formatters or formatting configuration used by the project.
-->

<Formatter or configuration, if applicable.>

### Linting and Static Analysis

<!--
Reference linting or static-analysis tools used by the project.
-->

<Linter or static-analysis configuration, if applicable.>

---

## 4. Project Structure Conventions

<!--
Define rules for where different types of project artifacts belong.

The actual architecture and directory structure should be described in
architecture.md. This section should only define conventions for adding
or organizing new content.

Examples:
- where application code belongs
- where documentation belongs
- where scripts belong
- where generated artifacts belong
- where configuration belongs
-->

<Define conventions for organizing project files and directories.>

---

## 5. Documentation

<!--
Define expectations for project documentation.

Possible topics:
- when documentation must be updated
- preferred documentation format
- inline comments
- API documentation
- diagrams
- decision records
- README responsibilities

Avoid documenting the same information in multiple places.
Prefer linking to the authoritative source.
-->

### Project Documentation

<Define expectations for maintaining documentation.>

### Code Comments

<!--
Describe when comments are useful.

A common principle is to explain why something exists rather than merely
restating what the code does.
-->

<Define expectations for code comments.>

### Architecture Decisions

Significant architectural decisions should be documented in:

`docs/decisions/`

<Define when an Architecture Decision Record should be created.>

---

## 6. Git Conventions

<!--
Define how changes are managed in Git.

Possible topics:
- branch naming
- commit style
- commit scope
- pull requests
- merge strategy
- protected branches

Do not assume a particular workflow unless the project has chosen one.
-->

### Branches

<Define branch naming and branch lifecycle conventions.>

### Commits

<Define commit message and commit scope conventions.>

### Pull Requests

<Define expectations for pull requests and reviews.>

### Merge Strategy

<Define the preferred merge strategy.>

---

## 7. Dependency Management

<!--
Define how new dependencies should be evaluated and maintained.

Possible considerations:
- necessity
- maintenance status
- licensing
- security
- portability
- dependency size
- version pinning
- update strategy

Technology-specific package-manager configuration should remain in its
native configuration files.
-->

<Define dependency management conventions.>

---

## 8. Configuration

<!--
Define how application and project configuration should be handled.

Possible topics:
- configuration files
- environment variables
- defaults
- environment-specific configuration
- local overrides

Never store credentials or secrets in version-controlled configuration.
-->

<Define configuration conventions.>

---

## 9. Secrets and Sensitive Information

<!--
Define rules for handling secrets and sensitive information.

Examples may include:
- API keys
- passwords
- access tokens
- private keys
- connection strings
- personal or confidential data

Reference the project's security documentation if a dedicated security
policy exists.
-->

<Define how secrets and sensitive information must be handled.>

---

## 10. Error Handling

<!--
Define general expectations for handling failures.

Possible topics:
- fail-fast behavior
- recoverable errors
- retries
- validation failures
- exception handling
- user-facing errors
- error propagation

Keep implementation-specific details in the relevant technical documentation.
-->

<Define error-handling conventions.>

---

## 11. Logging

<!--
Define expectations for logging and diagnostics.

Possible topics:
- log levels
- structured logging
- contextual information
- sensitive information
- correlation identifiers
- operational usefulness

Never log credentials, secrets, or sensitive data unless explicitly
required and appropriately protected.
-->

<Define logging conventions.>

---

## 12. Data Conventions

<!--
Remove this section if the project does not process or store meaningful data.

Possible topics:
- schemas
- identifiers
- timestamps
- time zones
- null handling
- encoding
- numeric precision
- units
- validation
- data lineage
-->

### Data Types and Formats

<Define important data format conventions.>

### Dates and Times

<Define date, time, and timezone conventions.>

### Missing Values

<Define how missing or unknown values are represented.>

### Identifiers

<Define identifier conventions where relevant.>

---

## 13. API and Interface Conventions

<!--
Remove this section if the project exposes no APIs or interfaces.

Possible topics:
- API naming
- versioning
- compatibility
- request and response formats
- error responses
- schema evolution
- command-line interfaces
- file-based interfaces
-->

<Define conventions for external and internal interfaces.>

---

## 14. Backward Compatibility

<!--
Define whether backward compatibility is required and how breaking
changes should be handled.

Remove this section if compatibility guarantees are irrelevant.
-->

<Define compatibility expectations.>

---

## 15. Generated Files

<!--
Define how generated artifacts are handled.

Possible topics:
- whether generated files are committed
- where they are stored
- how they are regenerated
- which source files are authoritative

This is especially useful for generated code, schemas, documentation,
exports, build artifacts, or derived datasets.
-->

<Define conventions for generated artifacts.>

---

## 16. Definition of Done

<!--
Define the minimum conditions for considering a change complete.

Keep detailed testing requirements in testing.md and reference them here
instead of duplicating them.

Possible criteria:
- implementation complete
- relevant tests pass
- documentation updated
- no unintended changes
- required reviews complete
-->

A change is considered complete when:

- <Completion criterion>
- <Completion criterion>
- Testing requirements defined in `docs/testing.md` have been satisfied.
- <Completion criterion>

---

## Exceptions

<!--
Document how intentional deviations from these conventions should be handled.

For significant or permanent exceptions, consider creating an ADR.
-->

<Describe how exceptions should be documented or approved.>

---

## Related Documentation

- [Project architecture](./architecture.md)
- [Testing strategy](./testing.md)
- [AI usage](./ai-usage.md)
- [Architecture decisions](./decisions/)