---
id: "zep-ci-test-plan-selector-test-plan-v2-strategy-ordering"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2): Strategy ordering"
summary: "Strategies run in a fixed order that reflects two principles:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

Strategies run in a fixed order that reflects two principles:

**Specificity over generality.**
The most precise strategies run first.  A file that lives inside
`tests/kernel/sched/` is handled definitively by `DirectTestStrategy`
(run exactly those tests) before the catch-all `MaintainerAreaStrategy`
can add an entire Kernel area sweep.

**Consume-before-additive.**
Consuming strategies run before additive ones.  Once a consuming strategy
claims a file, downstream strategies never see it.  This prevents a change
to a board file from also triggering a driver compat scan and a Kconfig sweep
for the same path.

The current order is:


* - #
  - Strategy
  - Consumes
  - Rationale
* - 0
  - `ComplexityStrategy`
  - No
  - Scores the patchset using pydriller and lizard.  Must run first so the
    score is available to `RiskClassifierStrategy`.  Emits no twister
    calls.
* - 1
  - `IgnoreStrategy`
  - Yes
  - Silently drops files that can never affect tests (documentation, CI
    workflows, tooling).  Runs early so later strategies never waste effort
    on ignored paths.
* - 1b
  - `BoilerplateFilter`
  - Yes
  - Consumes files whose entire diff consists of whitespace adjustments,
    blank-line changes, SPDX licence identifiers, copyright notices, or
    bare comment delimiters.  Such changes cannot affect runtime behaviour,
    so removing them early keeps the pool clean for substantive strategies.
    Requires a git commit range; no-op otherwise.
* - 2
  - `DirectTestStrategy`
  - Yes
  - A changed test or sample file must trigger *only* that test, not an
    entire area-wide sweep.  Consuming this file prevents
    Kernel area when `tests/kernel/sched/main.c` is modified.
* - 3
  - `SnippetStrategy`
  - Yes
  - Snippet changes are self-contained: only tests that declare the snippet
    in `required_snippets` need to run.  Consuming prevents downstream
    strategies from treating a snippet YAML as an unknown configuration
    file.
* - 4
  - `BoardStrategy`
  - Yes
  - Board-specific changes require a targeted integration test on every
    board variant.  Consuming prevents a board `.yaml` file from also
    matching Kconfig and Header strategies.
* - 5
  - `SoCStrategy`
  - Yes
  - SoC-level changes affect every board built on that SoC family.
    Consuming prevents the same `soc/` path from reaching the Kconfig
    sweep.
* - 6
  - `ManifestStrategy`
  - Yes
  - A changed `west.yml` requires module-tagged integration tests, not a
    generic maintainer-area run.  Consuming the manifest file prevents the
    catch-all from adding unrelated tests.
* - 7
  - `DriverCompatStrategy`
  - No
  - Additive: driver files may also be covered by area patterns, so the
    file is not consumed and `KconfigImpactStrategy` and
* - 8
  - `DtsBindingStrategy`
  - No
  - Additive: binding changes combine overlay-based test selection with
    board-targeted area calls.
* - 9
  - `KconfigImpactStrategy`
  - No
  - Additive: Kconfig changes may affect many unrelated files; only consumes
    when a non-widespread symbol is found, leaving widespread-symbol files
    for the catch-all.
* - 10
  - `HeaderImpactStrategy`
  - No
  - Additive: header changes trace include users back to maintainer areas.
    Widespread headers (included in more than the configured threshold) are
    skipped.
* - 11
  - `MaintainerAreaStrategy`
  - No
  - Catch-all: matches any remaining file against `MAINTAINERS.yml` area
    patterns and emits `--test-pattern` calls for each matching area that
    has a non-empty `tests:` list.
