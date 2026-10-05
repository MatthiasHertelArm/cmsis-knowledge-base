---
id: "txmw-chapter-5-generating-trace-buffers-defining-time-stamp-constants"
type: "concept"
domain: "trace"
title: "Chapter 5 - Generating trace buffers: Defining Time-Stamp Constants"
summary: "The time-stamp constants are designed to provide the developer control over the time-stamp used in the event trace entries. The two time-stamp constants and their default values are as follows:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter5.md#defining-time-stamp-constants"
license: "MIT"
mode: "V"
---

The time-stamp constants are designed to provide the developer control over the time-stamp used in the event trace entries. The two time-stamp constants and their default values are as follows:

```c
#ifndef TX_TRACE_TIME_SOURCE
#define TX_TRACE_TIME_SOURCE ++_tx_trace_simulated_time
#endif
#ifndef TX_TRACE_TIME_MASK
#define TX_TRACE_TIME_MASK   0xFFFFFFFFUL
#endif
```

The above constants are defined in **tx_port.h** and create a "fake" time-stamp that simply increments by one on each event. The following is an example of an actual timestamp definition:

```c
#ifndef TX_TRACE_TIME_SOURCE
#define TX_TRACE_TIME_SOURCE ((ULONG) 0x0x13000004)
#endif
#ifndef TX_TRACE_TIME_MASK
#define TX_TRACE_TIME_MASK 0xFFFFFFFFUL
#endif
```

The above constants specify a 32-bit timer that is obtained by reading the address 0x13000004. Most application specific time-stamps should be setup in a similar fashion.
