---
id: "zep-ci-test-plan-selector-test-plan-v2-consume-vs-additive-behaviour"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2): Consume vs. additive behaviour"
summary: "Every strategy subclass carries a class attribute consumes: bool."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

Every strategy subclass carries a class attribute `consumes: bool`.

When `consumes = True`:
  Files returned in the *handled* set are removed from the `remaining` pool
  before the next strategy runs.  Use this when the strategy is *authoritative*
  for its file type — i.e. when seeing the file in a later strategy would
  produce redundant or incorrect results.

When `consumes = False` (default):
  Files remain in the pool regardless of what the strategy returns.  All
  downstream strategies receive the same file list.  Use this for additive
  strategies that contribute *additional* test coverage without claiming
  exclusive ownership.


**Note:** The `Orchestrator` skips a strategy entirely when the `remaining` pool is empty.  Because non-consuming strategies see all files, "remaining" only shrinks through consuming strategies.  As soon as the pool is empty the orchestrator stops calling strategies.
