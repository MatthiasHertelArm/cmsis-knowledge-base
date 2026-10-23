---
id: "zep-ci-test-plan-selector-test-plan-v2-architecture"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2): Architecture"
summary: "The selector is built around a strategy pipeline. Each strategy is an independent analyser that:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

The selector is built around a *strategy pipeline*.  Each strategy is an
independent analyser that:

1. Receives the list of changed files (or the subset not yet consumed by
   earlier strategies).
2. Inspects those files according to its own logic.
3. Returns a list of `TwisterCall` descriptors and the set of files it
   has *handled*.

The `Orchestrator` drives the pipeline, merges all results into a
`PlanAccumulator`, deduplicates test suites, and writes the output
files.
