---
id: "view-event-recorder-api-eventrecorderenable"
type: "concept"
domain: "trace"
title: "Event Recorder API: EventRecorderEnable"
summary: "The function EventRecorderEnable configures the event filter for a software component."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t EventRecorderEnable (uint32_t recording, uint32_t comp_start, uint32_t comp_end)
```


The function **EventRecorderEnable** configures the event filter for a software component.

The events will be generated for the event level **\b** recording and between the range specified with **comp_start** and **comp_end.**

The parameter **\b** recording takes values from EventRecorder_recdefs.

Multiple calls to **EventRecorderEnable** are permitted and enable the recording of different event messages.

**Code** **Example**
```
  EventRecorderEnable (EventRecordAll, 0, 0xF);                    // record all events of component 0 - 15
    :
  EventRecorderEnable (EventRecordError, 0x80, 0xFE);              // record 'Error' events of component 0x80 - 0xFE
  EventRecorderEnable (EventRecordAPI+EventRecordOp, 0xC0, 0xC3);  // and record 'API' and 'Op' events of component groups 0xC0 - 0xC3
```
