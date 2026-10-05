---
id: "zep-ci-test-plan-selector-test-plan-v2-test-strategy-for-validating-selection-b"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2): Test strategy for validating selection behaviour"
summary: "The test suite lives in scripts/tests/ci/test_test_plan_v2.py and is run with pytest:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

The test suite lives in `scripts/tests/ci/test_test_plan_v2.py` and is run
with pytest:

```bash

pytest scripts/tests/ci/test_test_plan_v2.py -v
```
Tests are organised into one class per strategy or shared component.  The
following categories of tests are expected for each new strategy:

**Unit tests (no Zephyr tree required)**
  Use a `tmp_path` fixture to create the minimum filesystem structures
  (`board.yml`, `snippet.yml`, `testcase.yaml`, etc.) needed to exercise
  each code path.  These tests should be fast and hermetic.

**Helper method tests**
  Test internal methods (path-walking, YAML parsing, regex extraction) in
  isolation.  Pass synthetic content rather than relying on real files in the
  repository.

**Orchestrator integration tests**
  Use mock strategies and a mock `TwisterExecutor` to test the
  orchestrator's consume-vs-additive logic, full-run signalling, and
  `.testplan` output without invoking twister.

**Real-tree integration tests** (optional, `@pytest.mark.integration`)
  May be added and marked with `@pytest.mark.integration` to be excluded
  from the default run.  These are only meaningful on a complete Zephyr
  checkout.


### Minimal test checklist for a new strategy


* The strategy returns no calls and no handled files when no relevant files
  are in the input list.
* The strategy correctly identifies and returns the expected `TwisterCall`
  for a known-good input.
* The strategy does not crash when required files are absent from the filesystem.
* For consuming strategies: the handled set equals the matched files and
  nothing else.
* For additive strategies: the handled set is empty or equals only the files
  the strategy is authoritative for.
