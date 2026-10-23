---
id: "view-event-recorder-api-eventid"
type: "concept"
domain: "trace"
title: "Event Recorder API: EventID"
summary: "The macro EventID generates an id value that combines level, component number, and message number. The level value should be set to EventLevelError, EventLevelAPI, EventLevelOp, or EventLevelDetail."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
EventID
```

- `level`: EventRecorder_leveldefs of the **id**
- `comp_no`:  component number of the **id**
- `msg_no`:   message number of the **id**

The macro EventID generates an **id** value that combines **level,** **component** **number,** and **message** **number.**
The **level** value should be set to EventLevelError, EventLevelAPI, EventLevelOp, or EventLevelDetail.

The **id** value is used by the functions EventRecordData, EventRecord2, and EventRecord4.
