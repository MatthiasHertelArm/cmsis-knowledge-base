---
id: "view-event-recorder-api-eventrecorderdisable"
type: "concept"
domain: "trace"
title: "Event Recorder API: EventRecorderDisable"
summary: "The function EventRecorderDisable configures the event filter for a software component."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t EventRecorderDisable (uint32_t recording, uint32_t comp_start, uint32_t comp_end)
```


The function EventRecorderDisable configures the event filter for a software component.

The events will be generated for the event level **\b** recording and between the range specified with **comp_start** and **comp_end.**

The parameter **\b** recording takes values from EventRecorder_recdefs.

Multiple calls to EventRecorderDisable are permitted and disable the recording of event messages.

**Code** **Example**
```
  EventRecorderDisable (EventRecordDetail, 0, 0xFE);                 // stop recording 'Detail' events of component number 0 - 0xFE
    :
  EventRecorderDisable (EventRecordAPI+EventRecordOp, 0x80, 0xBF);   // stop recording 'API' and 'Op' events of component number 0x80 - 0xFE
  EventRecorderDisable (EventRecordAll, 0xC0, 0xCF);                 // stop recording all events of component number 0xC0 - 0xCF
```
