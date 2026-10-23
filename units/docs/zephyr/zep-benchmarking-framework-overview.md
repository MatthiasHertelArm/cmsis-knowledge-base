---
id: "zep-benchmarking-framework-overview"
type: "concept"
domain: "test"
title: "Benchmarking Framework: Overview"
summary: "This framework helps identify regressions and optimize critical paths by providing:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/benchmark.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/benchmark.rst"
license: "Apache-2.0"
mode: "V"
---

This framework helps identify regressions and optimize critical paths by
providing:

* **Standardized API**: Macros that align with existing `ztest` conventions.
* **Statistical Analysis**: Calculations of Mean, Standard Deviation, Standard
  Error, and Min/Max values.
* **Overhead Compensation**: Inclusion of a control test to account for the
  benchmarking frameworks own execution time. The control is subtracted from
  every reported statistic identically, so the corrected values are real
  numbers that generally do not coincide with any single measurement.
