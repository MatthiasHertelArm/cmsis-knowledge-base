---
id: "stream-readme-cmsisstream-max-number-event-arguments"
type: "concept"
domain: "cmsis-stream"
title: "README: CMSISSTREAM_MAX_NUMBER_EVENT_ARGUMENTS"
summary: "Maximum number of arguments in an event."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:platform/cmsis_rtos_runtime/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/platform/cmsis_rtos_runtime/README.md#cmsisstream-max-number-event-arguments"
license: "Apache-2.0"
mode: "V"
---

Maximum number of arguments in an event.

It defines the maximum number of arguments that can be passed in an event.
This number impacts the size of memory pools used by the event system.

Default value:
```C
#define CMSISSTREAM_MAX_NUMBER_EVENT_ARGUMENTS 8
```
