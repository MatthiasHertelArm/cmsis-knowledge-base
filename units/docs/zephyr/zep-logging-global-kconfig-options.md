---
id: "zep-logging-global-kconfig-options"
type: "concept"
domain: "debug"
title: "Logging: Global Kconfig Options"
summary: "These options can be found in the following file: subsys/logging/Kconfig."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

These options can be found in the following file: `subsys/logging/Kconfig`.

`CONFIG_LOG`: Global switch, turns on/off the logging.

Mode of operations:

`CONFIG_LOG_MODE_DEFERRED`: Deferred mode.

`CONFIG_LOG_MODE_IMMEDIATE`: Immediate (synchronous) mode.

`CONFIG_LOG_MODE_MINIMAL`: Minimal footprint mode.

Filtering options:

`CONFIG_LOG_RUNTIME_FILTERING`: Enables runtime reconfiguration of the
filtering.

`CONFIG_LOG_DEFAULT_LEVEL`: Default level, sets the logging level
used by modules that are not setting their own logging level.

`CONFIG_LOG_OVERRIDE_LEVEL`: It overrides module logging level when
it is not set or set lower than the override value.

`CONFIG_LOG_MAX_LEVEL`: Maximal (lowest severity) level which is
compiled in.

Processing options:

`CONFIG_LOG_MODE_OVERFLOW`: When new message cannot be allocated,
oldest one are discarded.

`CONFIG_LOG_BLOCK_IN_THREAD`: If enabled and new log message cannot
be allocated thread context will block for up to
`CONFIG_LOG_BLOCK_IN_THREAD_TIMEOUT_MS` or until log message is
allocated.

`CONFIG_LOG_PRINTK`: Redirect printk calls to the logging.

`CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD`: When the number of buffered log
messages reaches the threshold, the dedicated thread (see `log_thread_set`)
is woken up. If `CONFIG_LOG_PROCESS_THREAD` is enabled then this
threshold is used by the internal thread.

`CONFIG_LOG_PROCESS_THREAD`: When enabled, logging thread is created
which handles log processing.

`CONFIG_LOG_PROCESS_THREAD_STARTUP_DELAY_MS`: Delay in milliseconds
after which logging thread is started.

`CONFIG_LOG_BUFFER_SIZE`: Number of bytes dedicated for the circular
packet buffer.

`CONFIG_LOG_FRONTEND`: Direct logs to a custom frontend.

`CONFIG_LOG_FRONTEND_ONLY`: No backends are used when messages goes to frontend.

`CONFIG_LOG_FRONTEND_OPT_API`: Optional API optimized for the most common
simple messages.

`CONFIG_LOG_CUSTOM_HEADER`: Injects an application provided header into log.h

`CONFIG_LOG_TIMESTAMP_64BIT`: 64 bit timestamp.

`CONFIG_LOG_SIMPLE_MSG_OPTIMIZE`: Optimizes simple log messages for size
and performance. Option available only for 32 bit architectures.

Formatting options:

`CONFIG_LOG_FUNC_NAME_PREFIX_ERR`: Prepend standard ERROR log messages
with function name. Hexdump messages are not prepended.

`CONFIG_LOG_FUNC_NAME_PREFIX_WRN`: Prepend standard WARNING log messages
with function name. Hexdump messages are not prepended.

`CONFIG_LOG_FUNC_NAME_PREFIX_INF`: Prepend standard INFO log messages
with function name. Hexdump messages are not prepended.

`CONFIG_LOG_FUNC_NAME_PREFIX_DBG`: Prepend standard DEBUG log messages
with function name. Hexdump messages are not prepended.

`CONFIG_LOG_BACKEND_SHOW_TIMESTAMP`: Enables backend to print timestamps
with log.

`CONFIG_LOG_BACKEND_SHOW_LEVEL`: Enables backend to print levels with log.

`CONFIG_LOG_BACKEND_SHOW_COLOR`: Enables coloring of errors (red)
and warnings (yellow).

`CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP`: If enabled timestamp is
formatted to *hh:mm:ss:mmm,uuu*. Otherwise is printed in raw format.

Backend options:

`CONFIG_LOG_BACKEND_UART`: Enable built-in UART backend.

`CONFIG_LOG_BACKEND_NET`: Enable built-in Networking backend to send syslog messages
to a network server.
