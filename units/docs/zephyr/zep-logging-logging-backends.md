---
id: "zep-logging-logging-backends"
type: "concept"
domain: "debug"
title: "Logging: Architecture / Logging backends"
summary: "Logging backends are registered using LOG_BACKEND_DEFINE. The macro creates an instance in the dedicated memory section. Backends can be dynamically enabled (log_backend_enable) and disabled."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Architecture_

Logging backends are registered using `LOG_BACKEND_DEFINE`. The macro
creates an instance in the dedicated memory section. Backends can be dynamically
enabled (`log_backend_enable`) and disabled. When
logging_runtime_filtering is enabled, `log_filter_set` can be used
to dynamically change filtering of a module's logs for a given backend. A module is
identified by source ID and domain ID. The source ID can be retrieved if the source name
is known by iterating through all registered sources.

Logging supports up to 9 concurrent backends. A log message is passed to
each backend in the processing phase. Additionally, a backend is notified when logging
enters panic mode with `log_backend_panic`. When that happens, the backend should
switch to synchronous, interrupt-less operation or shut itself down if that is
not supported.  Occasionally, logging may inform the backend about the number of dropped
messages with `log_backend_dropped`. The message processing API is version
specific.

`log_backend_msg_process` is used for processing a message. It is common for
standard and hexdump messages, because a standard message holds its formatting arguments
in the same place where a hexdump message holds its data. It is also common for deferred
and immediate logging.


#### Message formatting


Logging provides a set of functions that can be used by the backend to format a
message. Helper functions are available in `include/zephyr/logging/log_output.h`.

Example message formatted using `log_output_msg_process`:

```console

[00:00:00.000,274] <info> sample_instance.inst1: logging message
```
