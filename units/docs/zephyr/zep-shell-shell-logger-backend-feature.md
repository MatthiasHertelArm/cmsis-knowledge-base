---
id: "zep-shell-shell-logger-backend-feature"
type: "concept"
domain: "debug"
title: "Shell: Shell Logger Backend Feature"
summary: "Shell instance can act as the logging_api backend. Shell ensures that log messages are correctly multiplexed with shell output. Log messages from logger thread are enqueued and processed in the shell thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

Shell instance can act as the logging_api backend. Shell ensures that log
messages are correctly multiplexed with shell output. Log messages from logger
thread are enqueued and processed in the shell thread. Logger thread will block
for configurable amount of time if queue is full, blocking logger thread context
for that time. Oldest log message is removed from the queue after timeout and
new message is enqueued. Use the `shell stats show` command to retrieve
number of log messages dropped by the shell instance. Log queue size and timeout
are `SHELL_DEFINE` arguments.

This feature is activated by: `CONFIG_SHELL_LOG_BACKEND` set to `y`.


**Warning:** Enqueuing timeout must be set carefully when multiple backends are used in the system. The shell instance could    have a slow transport or could block, for example, by a UART with hardware flow control. If timeout is set too high, the logger thread could be blocked and impact other logger backends.


**Warning:** As the shell is a complex logger backend, it can not output logs if the application crashes before the shell thread is running. In this situation, you can enable one of the simple logging backends instead, such as UART (`CONFIG_LOG_BACKEND_UART`) or RTT (`CONFIG_LOG_BACKEND_RTT`), which are available earlier during system initialization.


**Note:** The shell log backend is enabled by `shell_start`. With shell thread, when it is scheduled for the first time. The shell thread runs at a low priority by default, so this moment depends on when higher priority threads, including the main thread executing system initialization, block or finish. Log messages and `printk()` output routed through the logger (`CONFIG_LOG_PRINTK`) issued before that point are handled by the logging core, not by the shell: * In deferred mode (`CONFIG_LOG_MODE_DEFERRED`) they are buffered and printed once the shell starts, as long as they fit in * In immediate mode (`CONFIG_LOG_MODE_IMMEDIATE`) they are lost, because there is no active backend to output them. If the application needs early output on the shell, set hook with a priority higher than the shell backend initialization priority (e.g. `CONFIG_SHELL_BACKEND_SERIAL_INIT_PRIORITY`). Alternatively, do not route `printk()` through the logger.
