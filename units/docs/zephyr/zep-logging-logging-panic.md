---
id: "zep-logging-logging-panic"
type: "concept"
domain: "debug"
title: "Logging: Logging panic"
summary: "In case of an error condition, the system usually can no longer rely on the scheduler or interrupts. In that situation, deferred log message processing is not an option."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

In case of an error condition, the system usually can no longer rely on the scheduler or
interrupts. In that situation, deferred log message processing is not an option.
The logger controlling API provides a function for entering into panic mode
(`log_panic`), which should be called in such a situation.

When `log_panic` is called, a *panic* notification is sent to all active
backends. Once all backends are notified, all buffered messages are flushed. From
that moment forward, all logs are processed in a blocking way.
