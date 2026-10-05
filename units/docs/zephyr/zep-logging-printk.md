---
id: "zep-logging-printk"
type: "concept"
domain: "debug"
title: "Logging: Printk"
summary: "Typically, logging and printk use the same output, which they compete for. This can lead to issues if the output does not support preemption, but it may also result in corrupted output because logging data is interleaved with printk data."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

Typically, logging and `printk` use the same output, which they compete
for. This can lead to issues if the output does not support preemption, but it may
also result in corrupted output because logging data is interleaved with printk
data. However, it is possible to redirect printk messages to the
logging subsystem by enabling `CONFIG_LOG_PRINTK`. In that case,
printk entries are treated as log messages with level 0 (they cannot be disabled).
When enabled, logging manages the output, so there is no interleaving. However,
in deferred mode, the printk behaviour is changed since the output is delayed
until the logging thread processes the data. `CONFIG_LOG_PRINTK`
is enabled by default.
