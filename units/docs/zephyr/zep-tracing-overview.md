---
id: "zep-tracing-overview"
type: "concept"
domain: "debug"
title: "Tracing: Overview"
summary: "The tracing feature provides hooks that permits you to collect data from your application and allows tools running on a host to visualize the inner-working of the kernel and various subsystems."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

The tracing feature provides hooks that permits you to collect data from
your application and allows tools running on a host to visualize the inner-working of
the kernel and various subsystems.

Every system has application-specific events to trace out.  Historically,
that has implied:

1. Determining the application-specific payload,
2. Choosing suitable serialization-format,
3. Writing the on-target serialization code,
4. Deciding on and writing the I/O transport mechanics,
5. Writing the PC-side deserializer/parser,
6. Writing custom ad-hoc tools for filtering and presentation.

An application can use one of the existing formats or define a custom format by
overriding the macros declared in `include/zephyr/tracing/tracing.h`.

Different formats, transports and host tools are available and supported in
Zephyr.

In fact, I/O varies greatly from system to system.  Therefore, it is
instructive to create a taxonomy for I/O types when we must ensure the
interface between payload/format (Top Layer) and the transport mechanics
(bottom Layer) is generic and efficient enough to model these. See the
*I/O taxonomy* section below.
