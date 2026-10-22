---
id: "zep-logging-stack-usage"
type: "concept"
domain: "debug"
title: "Logging: Stack usage"
summary: "When logging is enabled, it impacts the stack usage of the context that uses the logging API. If the stack is optimized, it may lead to stack overflow. Stack usage depends on mode and optimization."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

When logging is enabled, it impacts the stack usage of the context that uses
the logging API. If the stack is optimized, it may lead to stack overflow. Stack
usage depends on mode and optimization. It also significantly varies between
platforms. In general, when `CONFIG_LOG_MODE_DEFERRED` is
used, stack usage is smaller, since logging is limited to creating and storing
log messages. If `CONFIG_LOG_MODE_IMMEDIATE` is used, the log
message is processed by the backends, which includes string formatting, directly
in the context that uses the logging API. In case of that mode, the stack usage
will depend on which backends are used.

Some of the platforms characterization for log message with two `integer` arguments listed below:

+---------------+----------+----------------------------+-----------+-----------------------------+
| Platform      | Deferred | Deferred (no optimization) | Immediate | Immediate (no optimization) |
+===============+==========+============================+===========+=============================+
| ARM Cortex-M3 | 40       | 152                        | 412       | 783                         |
+---------------+----------+----------------------------+-----------+-----------------------------+
| x86           | 12       | 224                        | 388       | 796                         |
+---------------+----------+----------------------------+-----------+-----------------------------+
| riscv32       | 24       | 208                        | 456       | 844                         |
+---------------+----------+----------------------------+-----------+-----------------------------+
| xtensa        | 72       | 336                        | 504       | 944                         |
+---------------+----------+----------------------------+-----------+-----------------------------+
| x86_64        | 32       | 528                        | 1088      | 1440                        |
+---------------+----------+----------------------------+-----------+-----------------------------+
