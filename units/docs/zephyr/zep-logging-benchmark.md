---
id: "zep-logging-benchmark"
type: "concept"
domain: "debug"
title: "Logging: Benchmark"
summary: "Benchmark numbers from tests/subsys/logging/log_benchmark performed on qemu_x86. It is a rough comparison to give a general overview."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

Benchmark numbers from `tests/subsys/logging/log_benchmark` performed
on `qemu_x86`. It is a rough comparison to give a general overview.

+--------------------------------------------+------------------+
| Feature                                    |                  |
+============================================+==================+
| Kernel logging                             | 7us [#f0]_/11us  |
|                                            |                  |
+--------------------------------------------+------------------+
| User logging                               | 13us             |
|                                            |                  |
+--------------------------------------------+------------------+
| kernel logging with overwrite              | 10us [#f0]_/15us |
+--------------------------------------------+------------------+
| Logging transient string                   | 42us             |
+--------------------------------------------+------------------+
| Logging transient string from user         | 50us             |
+--------------------------------------------+------------------+
| Memory utilization [#f1]_                  | 518              |
|                                            |                  |
+--------------------------------------------+------------------+
| Memory footprint (test) [#f2]_             | 2k               |
+--------------------------------------------+------------------+
| Memory footprint (application) [#f3]_      | 3.5k             |
+--------------------------------------------+------------------+
| Message footprint [#f4]_                   | 47 [#f0]_/32     |
|                                            | bytes            |
+--------------------------------------------+------------------+

.. [#f0] `CONFIG_LOG_SPEED` enabled.

.. [#f1] Number of log messages with various number of arguments that fits in 2048
  bytes dedicated for logging.

.. [#f2] Logging subsystem memory footprint in `tests/subsys/logging/log_benchmark`
  where filtering and formatting features are not used.

.. [#f3] Logging subsystem memory footprint in `samples/subsys/logging/logger`.

.. [#f4] Average size of a log message (excluding string) with 2 arguments on `Cortex M3`
