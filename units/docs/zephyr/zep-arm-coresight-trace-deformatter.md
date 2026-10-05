---
id: "zep-arm-coresight-trace-deformatter"
type: "concept"
domain: "debug"
title: "ARM Coresight Trace Deformatter"
summary: "Formatter is a method of wrapping multiple trace streams (specified by 7 bit ID) into a single output stream. Formatter is using 16 byte frames which wraps up to 15 bytes of data."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/debugging/cs_trace_defmt.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/debugging/cs_trace_defmt.rst"
license: "Apache-2.0"
mode: "V"
---

Formatter is a method of wrapping multiple trace streams (specified by 7 bit ID) into a
single output stream. Formatter is using 16 byte frames which wraps up to 15 bytes of
data. It is used, for example, by ETR (Embedded Trace Router) which is a circular RAM
buffer where data from various trace streams can be saved. Typically tracing data is
decoded offline by the host but deformatter can be used on-chip to decode the data during
application runtime.
