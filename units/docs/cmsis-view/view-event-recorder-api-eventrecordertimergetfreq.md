---
id: "view-event-recorder-api-eventrecordertimergetfreq"
type: "concept"
domain: "trace"
title: "Event Recorder API: EventRecorderTimerGetFreq"
summary: "This function is called by EventRecorderInitialize to initialize the timer that is used by the Event Recorder. For time stamp source User Timer (Power-On Reset) this function is only called for the first call to EventRecorderInitialize."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t EventRecorderTimerGetFreq (void)
```


This function is called by EventRecorderInitialize to initialize the timer that is used by the Event Recorder.
For time stamp source User Timer (Power-On Reset) this function is only called for the first call to EventRecorderInitialize.

**Note:**
µVision is using currently a fixed frequency that is defined by `EVENT_TIMESTAMP_FREQ.`
