---
id: "zep-benchmarking-framework-important-considerations"
type: "concept"
domain: "test"
title: "Benchmarking Framework: Important Considerations"
summary: "Benchmarking Framework: Important Considerations"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/benchmark.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/benchmark.rst"
license: "Apache-2.0"
mode: "V"
---

* **Noise**: Benchmarking is inherently sensitive to system noise. To obtain as
  accurate results as possible, disable unnecessary background tasks and
  interrupts that may interfere with timing.

* **Cache Warming**: The first sample of a benchmark may often be slower
  due to cache misses and this can skew results slightly on small sample sizes,
  choose a sufficiently large number of samples to mitigate this effect.

* **Use setup/teardown functions**: It is *highly* encouraged to utilize the
  setup and teardown functions to isolate the code under test as much as
  possible. Excessive setup/teardown code in the benchmark code can introduce
  noise and skew results *significantly* for small critical paths.
