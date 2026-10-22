---
id: "ceed-ceedling-s-delta-builds-delta-build-special-cases"
type: "concept"
domain: "test"
title: "Ceedling’s Delta Builds: Delta build special cases"
summary: "Add the --force-test-rerun flag to test build tasks to bypass the checks for only running changed test fixture executables. This command line flag forces those executables to run and produce fresh test results."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/getting-started/builds.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/builds/#delta-build-special-cases"
license: "MIT"
mode: "V"
---

Add the [`--force-test-rerun`](https://throwtheswitch.github.io/Ceedling/getting-started/builds/command-line.md#ceedling-build-tasks) flag to test build tasks to bypass the checks for only running changed test fixture executables. This command line flag forces those executables to run and produce fresh test results.

When [Unity’s test shuffling feature](https://throwtheswitch.github.io/Ceedling/getting-started/builds/../configuration/reference/unity.md#shuffle_tests) is enabled, delta builds automatically rerun test fixture executables to randomize test case order regardless of change or lack thereof in a test’s dependency tree. That is, since the feature requires test executables to run in order to shuffle test case order, effectively, delta builds are disabled for test fixture executables.
