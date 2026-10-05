---
id: "zep-benchmarking-framework-understanding-results"
type: "concept"
domain: "test"
title: "Benchmarking Framework: Understanding Results"
summary: "A benchmark is defined as three phases: the setup, then CONFIG_ZTEST_BENCHMARK_WARMUP iterations that are executed but not recorded, then the measured samples. The warmup applies to every benchmark in the image."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/benchmark.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/benchmark.rst"
license: "Apache-2.0"
mode: "V"
---

### Standard Benchmarking Results


```console

<suite name> ###############################################
<benchmark name> ===========================================
   Sample size:<number of samples>, total cycles: <total amount of cycles>
   Mean(u): <mean cycles per sample>
   Standard deviation(s): <cycles>
   Standard Error(SE): <cycles>
   Min: <cycles> (run #<sample number>)
   Max: <cycles> (run #<sample number>)
```

#### Statistical Metrics



**Note:** number of samples that exceed the median by more than percentage. The margin matters because the counter resolution spreads the baseline over a few counts; without it about half of any distribution would be reported. A latency distribution is usually a baseline plus a handful of disturbed runs rather than samples of one stochastic population, and a standard error over the two suggests an average that no single execution ever produced -- ten thousand runs of 760 cycles and one of 1240 give a standard error of 0.048, which reads as precision and is not, where `1 / 10000 (0.010%)` says what happened. Only the report changes; the standard error keeps its CSV column.

* **Mean (u)**: The average number of cycles taken per sample. It provides a
  central value representing the expected cost of execution.

* **Standard Deviation (s)**: Measures the amount of variation or fluctuation of
  the execution cost from the mean. A low standard deviation indicates that the
  behavior is deterministic and consistent.

* **Standard Error (SE)**: Estimates how far the sample mean is likely to be
  from the "true" mean of the system. It provides insight into the statistical
  reliability of the test. A lower SE indicates higher confidence in the
  result.

* **Min/Max**: The minimum and maximum cycle counts observed, along with which
  sample they occurred on.


#### Warmup and the cold cost


A benchmark is defined as three phases: the setup, then
`CONFIG_ZTEST_BENCHMARK_WARMUP` iterations that are executed but not recorded,
then the measured samples. The warmup applies to every benchmark in the image.

The very first execution is always unrecorded, whatever the warmup is set to. It runs with cold
caches, branch predictors and TLBs and can be an order of magnitude slower than the steady state,
and rather than discard that information the framework reports it on its own as the **cold cost**.
The two answer different questions — what an operation costs the first time it is reached, and
what it costs thereafter — and an application that runs a path once at startup cares about the
first.

Keeping it out of the distribution is what makes the distribution mean anything at the tail. A
benchmark that reported the cold start in both places would have it decide the far percentiles:
at ten thousand samples the nearest-rank p99.99 is the second largest value, so one cold start
would be read as the steady-state tail.

Raising the warmup beyond that costs accuracy on a micro benchmark whose whole cost is comparable
to a cache miss, and with a large enough sample count the early iterations have no measurable
effect on the mean, so the default of zero is the right starting point. Raise it when the
benchmark is large enough for cache state to matter and the steady state is what you are after.


#### Latency percentiles


The mean and the standard error describe how precisely the average was
estimated. That is the right question for throughput, but not for latency: a
real-time system is characterised by how bad an individual operation can be,
and that lives in the tail of the distribution rather than near the mean.

Enable `CONFIG_ZTEST_BENCHMARK_PERCENTILES` to retain the
individual samples and report `min`, `p50`, `p90`, `p99`, `p99.9`,
`p99.99` and `max` alongside the usual statistics. In CSV mode each
sampled and manual benchmark emits an additional `P` row; see
`CONFIG_ZTEST_BENCHMARK_OUTPUT_CSV` for the columns.

The difference this makes is clearest on a distribution with a tail. Measuring
interrupt entry latency on a loaded system gives a mean of 1264 cycles with a
standard error of 34, which describes no interrupt that actually occurred: the
percentiles show 1216 cycles all the way out to p99, and 25184 beyond it.

A percentile has to be resolvable by the number of samples taken. p99 needs at
least 100 samples, p99.9 at least 1000 and p99.99 at least 10000; with fewer,
the reported value degenerates to the maximum. Samples are retained in a
buffer of `CONFIG_ZTEST_BENCHMARK_MAX_SAMPLES` entries of
8 bytes each, which has to be at least as large as the sample count of the
largest benchmark. The retained samples are the first ones taken rather than a
sample of the whole run, so percentiles over a truncated prefix would miss
whatever happened after the buffer filled, which is where the tail tends to
live. A benchmark that overruns the buffer therefore reports no percentiles at
all, and says how many samples did not fit.

Plainly speaking, lower values are better for all metrics.
Lower mean, min, and max values indicates better raw performance.
Lower standard deviation and standard error values indicate more consistent and
therefore reliable performance.


### Timed Benchmarking Results


```console

<benchmark name> ===============================================
   Samples: <Number of samples executed during the benchmark>
   Total Time: <Gross execution time>
   Work Time: <Net execution time> ns (Net)
   Ops/Sec: <average operations per second>
   Cycles/Op: <average cycles per operation>
```

#### Statistical Metrics


* **Total Time**: The total time taken for all samples of the benchmark, including overhead.

* **Work Time**: The total time taken for the code under test, excluding the overhead of the
  benchmarking framework itself. This provides a more accurate measure of the actual performance of
  the code being benchmarked.

* **Ops/Sec**: The number of operations (samples) that can be performed per second, calculated by
  dividing the number of samples by the net work time (in seconds). This metric is particularly
  useful for understanding the throughput of the code being benchmarked.

* **Cycles/Op**: The average number of CPU cycles taken per operation, calculated by dividing the
  net number of cycles by the number of samples. This metric provides insight into the
  efficiency of the code in terms of CPU usage.

In general higher values for Ops/Sec are better as it indicates higher throughput, just as lower
values for Cycles/Op are better. As the Cycles/Op and Ops/Sec metrics are derived from the same
underlying data, they are reflecting the same performance characteristics from different
perspectives. A high Ops/Sec should correspond to a low Cycles/Op, and vice versa.



### Benchmark Output Options


The benchmarking framework provides several options for outputting results of benchmarking data. By
default, results are printed in a verbose human-readable format that is easy to understand and
interpret.
Alternatively, you can enable the `CONFIG_ZTEST_BENCHMARK_OUTPUT_CSV` Kconfig option
to output results in a CSV format that can be easily imported by scripts for further analysis.
The CSV output includes all the same metrics as the verbose output, but in a
format that is more conducive to automated analysis and reporting.

The standard benchmark csv output format is as follows:

```console

S,<suite name>,<benchmark name>,<sample size>,<total cycles>,<mean>,<stddev>,<stderr>,<min>,<min sample>,<max>,<max sample>
```
The timed benchmark csv output format is as follows:

```console

T,<suite name>,<benchmark name>,<samples>,<total time>,<work time>,<ops/sec>,<cycles/op>
```
