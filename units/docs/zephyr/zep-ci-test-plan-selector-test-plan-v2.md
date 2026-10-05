---
id: "zep-ci-test-plan-selector-test-plan-v2"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2)"
summary: "The CI test plan selector is a modular Python script located at scripts/ci/test_plan_v2.py."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

The CI test plan selector is a modular Python script located at
`scripts/ci/test_plan_v2.py`.  Its purpose is to analyse the set of files
changed in a Pull Request and emit a targeted twister test plan — exercising
only the tests that are plausibly affected by the change while avoiding a
full tree-wide run on every commit.

The script writes two artefacts:

* `testplan.json` — passed to twister via `twister --load-tests`.
* `.testplan` — a plain `KEY=value` environment file consumed by CI
  orchestration scripts, containing `TWISTER_TESTS`, `TWISTER_NODES`, and
  `TWISTER_FULL`.
