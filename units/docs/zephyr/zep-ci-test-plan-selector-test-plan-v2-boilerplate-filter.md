---
id: "zep-ci-test-plan-selector-test-plan-v2-boilerplate-filter"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2): Boilerplate filter"
summary: "BoilerplateFilter runs immediately after IgnoreStrategy and before any test-selection strategy. It inspects the actual diff of each changed file (via git diff) and consumes those whose entire content change is non-substantive:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

`BoilerplateFilter` runs immediately after `IgnoreStrategy` and
before any test-selection strategy.  It inspects the actual diff of each
changed file (via `git diff`) and consumes those whose entire content change
is non-substantive:

* **Whitespace and blank-line changes** — detected by ``git diff -w
  --ignore-blank-lines``: if that command produces no output for a file,
  every changed line is whitespace or blank.

* **SPDX and copyright header edits** — lines that begin with
  `SPDX-License-Identifier:`, `SPDX-FileCopyrightText:`, or the word
  `Copyright`.

* **Comment-delimiter-only lines** — lines whose non-whitespace content
  consists entirely of `/*`, `*/`, `//`, `#`, or `*` characters
  (e.g. reformatted block-comment borders).

A file is consumed only when **every** added or removed line in its diff falls
into one of those categories.  A single substantive line (a changed statement,
macro, or declaration) causes the file to pass through to downstream
strategies unchanged.

The filter is a no-op when `--commits` is not supplied (e.g. when using
`--modified-files`), because the diff cannot be computed without a commit
range.  In that case all files remain in the pool.
