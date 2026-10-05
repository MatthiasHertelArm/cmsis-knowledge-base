---
id: "zep-logging"
type: "concept"
domain: "debug"
title: "Logging"
summary: "The logging API provides a common interface to process messages issued by developers. Messages are passed through a frontend and then processed by active backends."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

The logging API provides a common interface to process messages issued by
developers. Messages are passed through a frontend and then
processed by active backends.
The frontend is responsible for immediate filtering and queueing of log messages, so it needs to
be fast. Backends may run later and take more time. They format the log message and send it to a
destination, for example UART, RTT or BLE.
A custom frontend and custom backends can be used if needed.

Summary of the logging features:

- Deferred logging reduces the time needed to log a message by shifting time
  consuming operations to a known context, instead of processing and sending
  the log message when called.
- Multiple backends supported (up to 9 backends).
- Custom frontend support, which can work together with standard backends.
- Compile time filtering on module level.
- Independent runtime filtering for each backend.
- Additional runtime filtering on module instance level.
- Timestamping with a user provided function. Timestamps can be 32 or 64 bits large.
- Dedicated API for dumping data.
- Dedicated API for handling transient strings.
- Panic support - in panic mode, logging switches to blocking, synchronous
  processing.
- Printk support - printk messages can be redirected to the logging system.
- Design ready for multi-domain/multi-processor systems.
- Support for logging floating point and `long long` values.
- Built-in copying of transient strings used as arguments.
- Support for multi-domain logging.
- Rate-limited logging macros to prevent log flooding when messages are generated frequently.

The logging API is highly configurable at compile time as well as at runtime. Using
Kconfig options (see logging_kconfig), logs can be gradually removed from
compilation to reduce image size and execution time when logs are not needed.
During compilation, logs can be filtered out by module and severity level.

Logs can also be compiled in but filtered at runtime using a dedicate API. Runtime
filtering is independent for each backend and each source of log messages.
The source of a log message can be a module or specific instance of a module.

There are four severity levels available in the system: error, warning, info
and debug. For each severity level, the logging API (`include/zephyr/logging/log.h`)
has a set of dedicated macros. There are also macros for logging data.

For each severity level, the following set of macros is available:

- `LOG_X` for standard printf-like messages, e.g. `LOG_ERR`.
- `LOG_HEXDUMP_X` for dumping data, e.g. `LOG_HEXDUMP_WRN`.
- `LOG_INST_X` for standard printf-like messages associated with a
  particular instance, e.g. `LOG_INST_INF`.
- `LOG_INST_HEXDUMP_X` for dumping data associated with a particular
  instance, e.g. `LOG_INST_HEXDUMP_DBG`

The warning level also exposes the following additional macro:

- `LOG_WRN_ONCE` for warnings where only the first occurrence is of interest.

Rate-limited logging macros are also available for all severity levels to prevent log flooding:

- `LOG_X_RATELIMIT` for rate-limited standard printf-like messages using the default rate,
  e.g. `LOG_ERR_RATELIMIT`.
- `LOG_X_RATELIMIT_RATE` for rate-limited standard printf-like messages with a custom rate,
  e.g. `LOG_ERR_RATELIMIT_RATE`.
- `LOG_HEXDUMP_X_RATELIMIT` for rate-limited data dumping using the default rate,
  e.g. `LOG_HEXDUMP_WRN_RATELIMIT`.
- `LOG_HEXDUMP_X_RATELIMIT_RATE` for rate-limited data dumping with a custom rate,
  e.g. `LOG_HEXDUMP_WRN_RATELIMIT_RATE`.

The convenience macros use the default rate specified by `CONFIG_LOG_RATELIMIT_INTERVAL_MS`,
while the explicit rate macros take a rate parameter (in milliseconds) that specifies the minimum interval between log messages.

There are two configuration categories: configurations per module and global
configuration. When logging is enabled globally, it is enabled for all modules by default. However,
modules can disable logging locally. Every module can specify its own logging
level. The module must define the `LOG_LEVEL` macro before using the
API. Unless a global override is set, the module logging level will be honored.
The global override can only increase the logging level. It cannot be used to
lower module logging levels that were previously set higher. It is also possible
to globally limit logs by providing a maximal severity level present in the
system, where maximal means lowest severity (e.g. if maximal level in the system
is set to info, it means that errors, warnings and info levels are present, but
debug messages are excluded).

Each module which is using the logging must specify its unique name and
register itself to the logging. If a module consists of more than one file,
then registration is performed in only one file, but each file must specify the module name.

The logger's default frontend is designed to be thread safe and minimizes the time needed
to log the message. Time consuming operations like string formatting or access to the
transport are not performed by default when the logging API is called. When the logging
API is called, a message is created and added to the list. A dedicated,
configurable buffer for a pool of log messages is used. There are 2 types of messages:
standard and hexdump. Each message contains a source ID (module or instance ID and
domain ID, which might be used for multiprocessor systems), timestamp and
severity level. A standard message contains pointers to the string and arguments.
A hexdump message contains the copied data and string.
