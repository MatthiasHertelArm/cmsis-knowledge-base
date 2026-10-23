---
id: "zep-ci-test-plan-selector-test-plan-v2-node-count-calculation"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2): Node count calculation"
summary: "TWISTER_NODES in .testplan is computed as follows:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

`TWISTER_NODES` in `.testplan` is computed as follows:

* `0` — no tests were selected.
* `1` — fewer than `--tests-per-builder` tests were selected (fits in one
  builder).
* `ceil(total / tests_per_builder)` — otherwise.  The ceiling ensures that
  no builder is over-capacity when the division is not exact.

The default value of `--tests-per-builder` is `900`.
