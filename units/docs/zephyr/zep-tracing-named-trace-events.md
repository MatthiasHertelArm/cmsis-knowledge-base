---
id: "zep-tracing-named-trace-events"
type: "concept"
domain: "debug"
title: "Tracing: Named Trace Events"
summary: "Although the user can extend any of the supported serialization formats to enable additional tracing functions (or provide their own backend), zephyr also provides one generic named tracing function for convenience purposes, as well as to demonstrate how …"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

Although the user can extend any of the supported serialization formats
to enable additional tracing functions (or provide their own backend), zephyr
also provides one generic named tracing function for convenience purposes,
as well as to demonstrate how tracing frameworks could be extended.

Users can generate a custom trace event by calling
`sys_trace_named_event`, which takes an event name as well as two
arbitrary 4 byte arguments. Tracing backends may truncate the provided event
name if it is too long for the serialization format they support.
