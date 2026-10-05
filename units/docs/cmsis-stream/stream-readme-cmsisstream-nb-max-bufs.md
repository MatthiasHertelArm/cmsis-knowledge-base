---
id: "stream-readme-cmsisstream-nb-max-bufs"
type: "concept"
domain: "cmsis-stream"
title: "README: CMSISSTREAM_NB_MAX_BUFS"
summary: "Maximum number of buffers (tensors ...) expected in the system at a given time."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:platform/cmsis_rtos_runtime/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/platform/cmsis_rtos_runtime/README.md#cmsisstream-nb-max-bufs"
license: "Apache-2.0"
mode: "V"
---

Maximum number of buffers (tensors ...) expected in the system at a given time.

This used to size the memory pool involved in atomic
reference counting of buffers (tensors ...).
An event may hold references to several buffers so this number
may be bigger than the number of events.

Default value:
```C
#define CMSISSTREAM_NB_MAX_BUFS 16
```
