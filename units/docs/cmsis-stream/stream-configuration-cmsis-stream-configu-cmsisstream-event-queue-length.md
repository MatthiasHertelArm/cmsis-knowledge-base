---
id: "stream-configuration-cmsis-stream-configu-cmsisstream-event-queue-length"
type: "concept"
domain: "cmsis-stream"
title: "Configuration {#cmsis_stream_configuration}: CMSISSTREAM_EVENT_QUEUE_LENGTH"
summary: "This is the number of events that can be queued in an event queue. In case of overflow of the queue, new events are dropped."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/03_configuration.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/03_configuration.md#cmsisstream-event-queue-length"
license: "Apache-2.0"
mode: "V"
---

Length of an event queue.

This is the number of events that can be queued in an event queue. In case of
overflow of the queue, new events are dropped.

Default value:

```C
#define CMSISSTREAM_EVENT_QUEUE_LENGTH 20
```
