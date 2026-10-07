# Testing Strategy

<!--
PURPOSE

This document defines the project's shared testing and validation strategy.

It applies to all contributors, including humans and AI agents.

The goal is to define how changes are verified before they are considered
complete, without depending on a specific programming language, framework,
or AI coding assistant.

General project conventions belong in conventions.md.
Architecture belongs in architecture.md.
Agent-specific instructions belong in AGENTS.md, CLAUDE.md, .codex/,
or .claude/.

Replace the placeholders below with project-specific information and
remove sections that are not relevant to the project.
-->

## 1. Testing Goals

<!--
Describe what the project's testing strategy is intended to protect.

Possible goals:
- prevent regressions
- verify business rules
- validate interfaces and contracts
- protect data integrity
- verify integration behavior
- provide confidence during refactoring
- detect unintended side effects

Focus on outcomes rather than tools.
-->

The testing strategy should provide confidence that:

- <Testing goal>
- <Testing goal>
- <Testing goal>

---

## 2. Test Levels

<!--
Define which levels of testing are used by the project.

Not every project requires every level.
Remove sections that are not applicable.
-->

### Unit Tests

<!--
Test isolated units of behavior with minimal external dependencies.
-->

**Purpose**

<Describe what unit tests should verify.>

**Scope**

<Define what belongs in unit tests.>

**Out of scope**

<Define what should not be tested at this level.>

### Integration Tests

<!--
Test interactions between components, services, databases, file systems,
APIs, or other dependencies.
-->

**Purpose**

<Describe what integration tests should verify.>

**Scope**

<Define important integration boundaries.>

### End-to-End Tests

<!--
Test complete workflows across relevant system boundaries.

Use these tests selectively because they are usually slower and more
expensive to maintain than lower-level tests.
-->

**Purpose**

<Describe which critical workflows require end-to-end validation.>

### Acceptance or Domain Validation

<!--
Optional.

Use this section when correctness depends on business rules, domain
requirements, data contracts, migration rules, or acceptance criteria.
-->

<Describe domain-specific validation requirements.>

---

## 3. Test Organization

<!--
Describe where tests live and how they are organized.

Possible approaches:
- tests mirror the source structure
- tests live beside implementation files
- separate directories exist for different test levels

Do not prescribe a structure that the project does not use.
-->

<Test directory and organization conventions.>

---

## 4. Test Naming

<!--
Define how tests should be named so their intent is clear.

A test name should ideally communicate:
- the behavior being tested
- the relevant condition
- the expected outcome

Avoid coupling this section to a specific framework unless required.
-->

<Define test naming conventions.>

---

## 5. Test Data

<!--
Define how test data should be created and maintained.

Possible sources:
- fixtures
- factories
- generated data
- synthetic datasets
- sanitized production-derived datasets
- snapshots
- reference datasets

Test data should be deterministic whenever practical.
-->

### Test Data Principles

- <Test data principle>
- <Test data principle>

### Production Data

<!--
Define whether production-derived data may be used in tests.

Consider:
- privacy
- confidentiality
- licensing
- reproducibility
- sanitization
- data retention

Never place sensitive production data in the repository unless explicitly
approved and appropriately protected.
-->

<Define rules for production-derived test data.>

---

## 6. Fixtures, Mocks, and Test Doubles

<!--
Define when dependencies should be replaced by fixtures, mocks, stubs,
fakes, or other test doubles.

Mocks should not hide important integration behavior.

For systems where correctness depends on real reference data or contracts,
define which dependencies must not be replaced by neutral substitutes.
-->

<Define fixture and mocking conventions.>

---

## 7. External Systems

<!--
Define how tests interact with external systems.

Examples:
- databases
- APIs
- message brokers
- cloud services
- ERP systems
- file shares
- MCP servers

Clarify which tests may use real systems and which must use isolated
test environments.
-->

### Local or Isolated Testing

<Describe how external dependencies are represented locally.>

### Shared Test Environments

<Describe rules for shared test systems, if applicable.>

### Production Systems

<!--
Tests should generally not modify production systems.

If read-only production validation is permitted, document the exact
boundaries and safeguards.
-->

<Define production-system restrictions.>

---

## 8. Regression Testing

<!--
Define how defects are converted into lasting regression protection.

A useful general principle is that a fixed defect should receive a
regression test whenever the failure can reasonably be reproduced.
-->

<Define regression-testing expectations.>

---

## 9. Contract and Schema Testing

<!--
Optional.

Use when components exchange structured data or depend on explicit
contracts.

Examples:
- API schemas
- database schemas
- event schemas
- file formats
- migration mappings
- data contracts
-->

<Define contract and schema validation requirements.>

---

## 10. Data Quality Validation

<!--
Optional.

Particularly relevant for data engineering, migrations, analytics,
ETL/ELT, and integration projects.

Possible checks:
- completeness
- uniqueness
- referential integrity
- allowed values
- type correctness
- reconciliation
- row counts
- business-rule validation
-->

<Define data quality checks and acceptance criteria.>

---

## 11. Test Execution

<!--
Document how the relevant test suites are executed.

Prefer referencing executable scripts or native project configuration
instead of duplicating complex commands here.
-->

### Fast Validation

<!--
Define the smallest useful validation set for rapid feedback during
development.
-->

<Describe the fast validation workflow.>

### Full Validation

<!--
Define the validation required before a change is considered ready for
merge or release.
-->

<Describe the full validation workflow.>

---

## 12. Change-Based Validation

<!--
Define how the scope of testing should relate to the scope and risk of
a change.

A small documentation change should not necessarily require the same
validation as a database migration or security-sensitive change.
-->

### Low-Risk Changes

<Required validation.>

### Normal Changes

<Required validation.>

### High-Risk Changes

<Required validation.>

---

## 13. Continuous Integration

<!--
Describe which checks are executed automatically by CI.

The actual workflow configuration belongs under .github/workflows/.

Possible checks:
- formatting
- linting
- static analysis
- unit tests
- integration tests
- security checks
- build validation
-->

<Describe required CI checks.>

A change must not be considered successfully validated if required CI
checks are failing or have not been executed.

---

## 14. Test Failures

<!--
Define how failures should be handled.

A failing test should be investigated rather than automatically modified,
disabled, skipped, or deleted.

Changing a test is appropriate only when the expected behavior itself has
intentionally changed or the test is demonstrably incorrect.
-->

When a test fails:

1. Determine whether the implementation, test, environment, or test data
   caused the failure.
2. Identify the underlying cause before changing behavior.
3. Do not weaken or remove a valid test merely to make the suite pass.
4. Document intentional behavior changes where appropriate.
5. Add regression coverage when fixing reproducible defects.

<Add project-specific failure-handling rules if required.>

---

## 15. Flaky Tests

<!--
Define how non-deterministic tests are handled.

Repeated retries should not be used to permanently hide unstable tests.
-->

<Define how flaky tests are identified, tracked, and corrected.>

---

## 16. Test Coverage

<!--
Define whether code or behavior coverage is measured.

Avoid treating a coverage percentage as proof of correctness.

If a numerical threshold is used, document it here or reference the
authoritative tool configuration.
-->

<Define coverage expectations, or remove this section if not applicable.>

---

## 17. Performance Testing

<!--
Optional.

Define performance requirements when latency, throughput, memory usage,
processing time, or scalability materially affect correctness or usability.
-->

<Define performance testing requirements.>

---

## 18. Security Testing

<!--
Optional.

Possible checks:
- dependency vulnerabilities
- static security analysis
- authentication and authorization
- input validation
- secret detection
- permission boundaries

Reference dedicated security documentation where appropriate.
-->

<Define security testing requirements.>

---

## 19. Validation Evidence

<!--
Define what evidence should be available to demonstrate that a change
was actually validated.

This is especially useful for AI-assisted development.

Possible evidence:
- executed test commands
- test results
- CI run
- validation report
- relevant logs
- before/after comparison

Do not claim that a test passed unless it was actually executed and its
result is known.
-->

For completed changes, validation should record:

- what was tested
- how it was tested
- the result
- any tests that could not be executed
- any remaining uncertainty

<Add project-specific evidence requirements if necessary.>

---

## 20. Validation Before Completion

<!--
Define the minimum validation required before a contributor or AI agent
may consider work complete.

This section should align with the Definition of Done in conventions.md.
-->

Before a change is considered complete:

- relevant tests have been executed
- required validation has passed
- required CI checks have passed or their status is explicitly known
- new behavior has appropriate test coverage where applicable
- fixed defects have regression coverage where practical
- documentation has been updated when behavior or architecture changed
- unexecuted tests or unresolved risks are explicitly reported

<Add project-specific completion requirements.>

---

## Exceptions

<!--
Document how intentional exceptions to the testing strategy are handled.

Examples:
- unavailable external test environment
- temporarily disabled test
- accepted known failure
- emergency change

Exceptions should be explicit rather than silently ignored.
-->

<Describe how testing exceptions must be documented or approved.>

---

## Related Documentation

- [Project architecture](./architecture.md)
- [Project conventions](./conventions.md)
- [AI usage](./ai-usage.md)
- [Architecture decisions](./decisions/)