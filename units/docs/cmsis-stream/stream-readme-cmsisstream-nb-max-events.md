---
id: "stream-readme-cmsisstream-nb-max-events"
type: "concept"
domain: "cmsis-stream"
title: "README: CMSISSTREAM_NB_MAX_EVENTS"
summary: "Maximum number of events expected in the system at a given time."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:platform/cmsis_rtos_runtime/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/platform/cmsis_rtos_runtime/README.md#cmsisstream-nb-max-events"
license: "Apache-2.0"
mode: "V"
---

Maximum number of events expected in the system at a given time.

This is used to size the memory pools involved in event creation.
Several event queues will use the same pool so this number
may be bigger than the event queue length.

In current `stream_runtime_init` APIs, each application (even paused) has its own queue but they all share the same pool.

Default value:
```C
#define CMSISSTREAM_NB_MAX_EVENTS 16
```
