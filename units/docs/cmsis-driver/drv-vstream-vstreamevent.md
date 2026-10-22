---
id: "drv-vstream-vstreamevent"
type: "concept"
domain: "drivers"
title: "vStream: vStreamEvent"
summary: "This user-implemented callback function is invoked by the driver to signal runtime events during streaming. It is registered by the vStreamInitialize function."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/vStream.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void vStreamEvent (uint32_t event_flags)
```


This user-implemented callback function is invoked by the driver to signal runtime events during streaming.  
It is registered by the vStreamInitialize function.

The event_flags parameter is a bitmask where each bit represents a specific event condition.

Multiple events may be reported simultaneously via combined bits. Use this function to respond to runtime conditions, such as processing data, handling errors, or updating application state.

The following events can be signaled:



| Parameter **event_flags** | Bit | Description |
|---|---|---|
| VSTREAM_EVENT_DATA | 0 | Occurs when a new block of incoming data is available or when a block of outgoing data was streamed out. |
| VSTREAM_EVENT_OVERFLOW | 1 | Occurs when a block of incoming data begins to be overwritten because it was not released in time using the vStreamReleaseBlock function. |
| VSTREAM_EVENT_UNDERFLOW | 2 | Occurs when a block of outgoing data was not ready (committed with vStreamReleaseBlock function) before streaming out required it. |
| VSTREAM_EVENT_EOS | 3 | Occurs when a streaming interface reached end of stream. |



*******************************************************************************
