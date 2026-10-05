---
id: "view-event-recorder-api-eventrecordertimersetup"
type: "concept"
domain: "trace"
title: "Event Recorder API: EventRecorderTimerSetup"
summary: "This function is called by EventRecorderInitialize to initialize the timer that is used by the Event Recorder. For time stamp source User Timer (Power-On Reset) this function is only called for the first call to EventRecorderInitialize."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t EventRecorderTimerSetup (void)
```


This function is called by EventRecorderInitialize to initialize the timer that is used by the Event Recorder.
For time stamp source User Timer (Power-On Reset) this function is only called for the first call to EventRecorderInitialize.
