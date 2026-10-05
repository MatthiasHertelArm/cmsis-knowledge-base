---
id: "view-event-recorder-api-eventrecorderstart"
type: "concept"
domain: "trace"
title: "Event Recorder API: EventRecorderStart"
summary: "The function EventRecorderStart enables the recording of the events that are configured for recording using EventRecorderEnable or EventRecorderInitialize"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t EventRecorderStart (void)
```


The function **EventRecorderStart** enables the recording of the events that are configured for recording using EventRecorderEnable or EventRecorderInitialize

**Code** **Example**
```
  EventRecorderStart ();        // start with the recording of events that pass filtering
```
