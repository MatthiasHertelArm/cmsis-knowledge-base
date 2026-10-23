---
id: "zep-logging-default-frontend"
type: "concept"
domain: "debug"
title: "Logging: Architecture / Default Frontend"
summary: "The default frontend is engaged when the logging API is called by a source of logging (e.g."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Architecture_

The default frontend is engaged when the logging API is called by a source of logging (e.g.
`LOG_INF`) and is responsible for filtering a message (compile and runtime),
allocating a buffer for the message, creating the message and committing that
message. Since the logging API can be called in an interrupt, the frontend is optimized
to log the message as fast as possible.


#### Log message


A log message contains a message descriptor (source, domain and level), timestamp,
formatted string details (see cbprintf_packaging) and optional data.
Log messages are stored in a continuous block of memory.
Memory is allocated from a circular packet buffer (mpsc_pbuf), which has
a few consequences:

 * Each message is a self-contained, continuous block of memory. Thus, it is suited
   for copying the message (e.g. for offline processing).
 * Messages must be freed sequentially. Backend processing is synchronous. Backends
   can make a copy for deferred processing.

A log message has the following format:

+------------------+----------------------------------------------------+
| Message Header   | 2 bits: MPSC packet buffer header                  |
|                  +----------------------------------------------------+
|                  | 1 bit: Trace/Log message flag                      |
|                  +----------------------------------------------------+
|                  | 3 bits: Domain ID                                  |
|                  +----------------------------------------------------+
|                  | 3 bits: Level                                      |
|                  +----------------------------------------------------+
|                  | 11 bits: Cbprintf Package Length                   |
|                  +----------------------------------------------------+
|                  | 12 bits: Data length                               |
|                  +----------------------------------------------------+
|                  | pointer: Pointer to the source descriptor [#l0]_   |
|                  +----------------------------------------------------+
|                  | 32 or 64 bits: Timestamp [#l0]_                    |
|                  +----------------------------------------------------+
|                  | pointer: Pointer to thread ID (optional) [#l1]_    |
|                  +----------------------------------------------------+
|                  | 8 bits: core ID (optional) [#l2]_                  |
|                  +----------------------------------------------------+
|                  | Optional padding [#l3]_                            |
+------------------+----------------------------------------------------+
| Cbprintf         | Header                                             |
|                  +----------------------------------------------------+
| | package        | Arguments                                          |
| | (optional)     +----------------------------------------------------+
|                  | Appended strings                                   |
+------------------+----------------------------------------------------+
| Hexdump data (optional)                                               |
+------------------+----------------------------------------------------+
| Alignment padding (optional)                                          |
+------------------+----------------------------------------------------+

.. [#l0] Depending on their size, the source descriptor and timestamp fields may be swapped,
         in order to reduce the amount of padding.
.. [#l1] Only present if CONFIG_LOG_THREAD_ID_PREFIX is enabled.
.. [#l2] Only present if CONFIG_LOG_CORE_ID_PREFIX is enabled.
.. [#l3] It may be required for cbprintf package alignment.


#### Log message allocation


It may happen that the frontend cannot allocate a message. This happens if the
system is generating more log messages than it can process in a certain time
frame. There are two strategies to handle that case:

- No overflow - the new log is dropped if space for a message cannot be allocated.
- Overflow - the oldest pending messages are freed, until the new message can be
  allocated. Enabled by `CONFIG_LOG_MODE_OVERFLOW`. Note that it degrades
  performance thus it is recommended to adjust buffer size and amount of enabled
  logs to limit dropping.


#### Runtime filtering


If runtime filtering is enabled, then for each source of logging a filter
structure in RAM is declared. Such a filter is using 32 bits divided into ten 3
bit slots. Except for *slot 0*, each slot stores the current filter for one backend in
the system. *Slot 0* (bits 0-2) is used to aggregate the maximal filter setting for a
given source of logging. The aggregate slot determines if a log message is created
for a given entry, since it indicates if there is at least one backend expecting
that log entry. Backend slots are examined when a message is processed by the core
to determine if the message is accepted by the given backend. Compared to compile
time filtering, the binary footprint is increased, because discarded logs are still compiled in.

In the example below, backend 1 is set to receive errors (*slot 1*) and backend
2 up to info level (*slot 2*). Slots 3-9 are not used. The aggregated filter
(*slot 0*) is set to info level, meaning that up to this level, message from that
particular source will be buffered.

+------+------+------+------+-----+------+
|slot 0|slot 1|slot 2|slot 3| ... |slot 9|
+------+------+------+------+-----+------+
| INF  | ERR  | INF  | OFF  | ... | OFF  |
+------+------+------+------+-----+------+
