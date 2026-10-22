---
id: "view-theory-of-operation-event-recorder-heartbeat"
type: "concept"
domain: "trace"
title: "Theory of operation: Event Recorder heartbeat"
summary: "The Event Recorder timer is a 32-bit counter that can overflow. To avoid overflow problems, send a \"heartbeat\" event within the limits of this 32-bit counter."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/event_recorder.md#event-recorder-heartbeat"
license: "Apache-2.0"
mode: "V"
---

The Event Recorder timer is a 32-bit counter that can overflow. To avoid overflow problems, send a "heartbeat" event within the limits of this 32-bit counter.

**Calculation Example**

Assuming that your application is running at 168 MHz, you can calculate the time between two heartbeats like the following:

```
2^32 / 168000000 Hz = 25.57 s
```

So you need to generate an event every 25 s. This can be an event with an event ID that you don't need and thus filter from the display in Event Recorder or an event that you use to check if your application is still running.
