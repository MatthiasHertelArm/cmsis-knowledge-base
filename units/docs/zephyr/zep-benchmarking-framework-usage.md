---
id: "zep-benchmarking-framework-usage"
type: "concept"
domain: "test"
title: "Benchmarking Framework: Usage"
summary: "A benchmark suite is defined similarly to the normal ztest testsuite by first defining the suite with ZTEST_BENCHMARK_SUITE and then adding individual benchmark tests to the suite using either ZTEST_BENCHMARK or ZTEST_BENCHMARK_TIMED macros."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/benchmark.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/benchmark.rst"
license: "Apache-2.0"
mode: "V"
---

A benchmark suite is defined similarly to the normal ztest testsuite by first
defining the suite with `ZTEST_BENCHMARK_SUITE` and then adding individual
benchmark tests to the suite using either `ZTEST_BENCHMARK` or `ZTEST_BENCHMARK_TIMED` macros.

```c

#include <zephyr/ztest.h>

ZTEST_BENCHMARK_SUITE(<test suite name>, <setup_fn>, <teardown_fn>);
```

### Standard Benchmarks


Standard benchmarks are sample-based, meaning they execute the test a specified number
of times and measure the total cycles taken. This is useful for benchmarking critical paths where
you want to understand the raw CPU performance in terms of cycles. It provides insights into the
efficiency of the code and helps identify bottlenecks in terms of CPU usage.
This benchmarking method is suitable for code that has consistent execution times and is not heavily
influenced by external factors such as I/O operations or context switches.

```c

#include <zephyr/ztest.h>

ZTEST_BENCHMARK_SUITE(<suite name>, NULL, NULL);

ZTEST_BENCHMARK(<suite name>, <benchmark name>, <number of samples>, <setup_fn>, <teardown_fn>)
{
    /* Code to benchmark */
}
```
A standard benchmark follows a flow where the setup function is called before each sample, the test
function is executed for the specified number of samples, and the teardown function is called after
each sample.


### Timed Benchmarks


Timed benchmarks in contrast to the standard benchmarks measures execution time of the code
instead of cycles. This is useful for benchmarking code that may have variable execution
times or when you want to measure the actual time taken rather than just CPU cycles of a critical
path. It provides a broader view of performance characteristics, especially for code that involves
I/O operations, context switches, or other factors that can influence execution time beyond raw CPU
performance.

```c

ZTEST_BENCHMARK_TIMED(<suite name>, <benchmark name>, <time in ms>, <setup_fn>, <teardown_fn>)
{
      /* Code to benchmark */
}
```
Unlike standard benchmarks that favor isolation, Timed Benchmarks executes setup and teardown
functions only once allowing the test function to run hot within a dedicated time window.
This will give a more realistic measurements as it includes the overhead of the system as it would
be in a real-world scenario, such as interrupts, context switches, and other background tasks.


### Manual Benchmarks


Standard and timed benchmarks are timed by the framework itself, which takes both timestamps in
thread context around each invocation of the benchmark body. Some measurements cannot be expressed
that way because their endpoints are captured in different execution contexts: for example the
latency from raising an interrupt to the first instruction of its ISR, or from the end of an ISR to
a woken thread running.

Manual benchmarks keep the loop, the setup and the teardown in the framework and hand the body
only the choice of what is measured, by bracketing it with `ztest_benchmark_start` and
`ztest_benchmark_end`. The framework computes and reports the same statistics as for
standard benchmarks.

```c

ZTEST_BENCHMARK_MANUAL(<suite name>, <benchmark name>, <samples>, <setup_fn>, <teardown_fn>)
{
      prepare();

      ztest_benchmark_start();
      operation_under_test();
      ztest_benchmark_end();
}
```
Both hooks only take a timestamp, so either may be called from an ISR and the span need not begin
and end in the same execution context. For the latency from an interrupt to the thread it wakes,
the ISR marks the start and the thread ends the span:

```c

static void my_isr(const void *arg)
{
      ztest_benchmark_start();
}

ZTEST_BENCHMARK_MANUAL(<suite name>, isr_exit_latency, 1000, NULL, NULL)
{
      trigger_the_interrupt();

      ztest_benchmark_end();
}
```
The sample itself is computed once the body has returned, which is what keeps the statistics out
of interrupt context: updating them uses floating point, which is not allowed in an ISR on every
architecture. An iteration whose body marks no span contributes no sample.

Manual benchmarks are corrected against a control of their own rather than the one the sampled
benchmarks use. A manual span costs the two timestamps that bracket it and nothing else, where the
sampled control also measures the indirect call to the benchmark body, which is not part of a
manual span. A span whose ends are captured in two different contexts pays neither exactly, and no
control can express that.

The warmup applies here exactly as it does to a sampled benchmark: the framework runs the body
`CONFIG_ZTEST_BENCHMARK_WARMUP` extra times and discards those spans, keeping the
first as the cold cost. The body never has to distinguish between the two phases, and every
measured iteration is preceded by exactly the same work as the one before it.
