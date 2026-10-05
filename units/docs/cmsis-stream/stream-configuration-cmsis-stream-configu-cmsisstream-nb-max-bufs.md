---
id: "stream-configuration-cmsis-stream-configu-cmsisstream-nb-max-bufs"
type: "concept"
domain: "cmsis-stream"
title: "Configuration {#cmsis_stream_configuration}: CMSISSTREAM_NB_MAX_BUFS"
summary: "Maximum number of buffers, tensors, and similar objects expected in the system at a given time."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/03_configuration.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/03_configuration.md#cmsisstream-nb-max-bufs"
license: "Apache-2.0"
mode: "V"
---

Maximum number of buffers, tensors, and similar objects expected in the system
at a given time.

This is used to size the memory pool involved in atomic reference counting of
buffers. An event may hold references to several buffers so this number may be
bigger than the number of events.

Default value:

```C
#define CMSISSTREAM_NB_MAX_BUFS 16
```
