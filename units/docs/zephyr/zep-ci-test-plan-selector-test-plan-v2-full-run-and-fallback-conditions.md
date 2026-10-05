---
id: "zep-ci-test-plan-selector-test-plan-v2-full-run-and-fallback-conditions"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2): Full-run and fallback conditions"
summary: "The orchestrator signals TWISTER_FULL=True in .testplan when either of the following is true:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

The orchestrator signals `TWISTER_FULL=True` in `.testplan` when either of
the following is true:

1. **Unresolved files.** After all strategies have run, at least one changed
   file was not *handled* by any strategy.  Rather than silently skipping
   coverage for an unknown path, the script falls back to requesting a full
   run so no regression slips through.

2. **Explicit full-run signal.** A strategy returns a `TwisterCall`
   with `full_run=True`.  When the orchestrator encounters such a call, it
   immediately sets `TWISTER_FULL=True`, empties the remaining pool, and
   stops executing further calls.  This mechanism allows a strategy to opt out
   of targeted selection (e.g. when a core subsystem header used by the entire
   tree is modified).

When `TWISTER_FULL=True` the CI script is expected to discard
`testplan.json` and run twister without `--load-tests`.
