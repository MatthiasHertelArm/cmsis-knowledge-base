---
id: "zep-ci-test-plan-selector-test-plan-v2-shared-pipeline-context"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2): Shared pipeline context"
summary: "PipelineContext is a dataclass threaded through all strategies via build_strategies. It currently carries:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

`PipelineContext` is a dataclass threaded through all strategies via
`build_strategies`.  It currently carries:

* `complexity_score` — aggregate patchset score written by
  `ComplexityStrategy` and read by `RiskClassifierStrategy`.
* `file_metrics` — per-file `ComplexityMetrics` mappings for
  detailed logging and downstream decision-making.

New cross-strategy state should be added as typed fields on
`PipelineContext` rather than as strategy-level instance variables.
