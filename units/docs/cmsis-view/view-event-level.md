---
id: "view-event-level"
type: "concept"
domain: "trace"
title: "Event level"
summary: "Defines for parameter level for EventID"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

Defines for parameter **level** for EventID

The following defines specify the **level** for the **id.** This defines may be used for:
 - EventRecorder_Setup functions as parameter **recording**
 - EventID as parameter **level**

er_filtering may be used to change the settings in the debugger. The event level define settings map as described in the following table:

Recording level            | Error                 | API                 | Op                 | Data
:--------------------------|:---------------------:|:-------------------:|:------------------:|:-----------------------:
Event level define setting | EventRecordError | EventRecordAPI | EventRecordOp | EventRecordDetail


### EventLevelError

```c
EventLevelError
```


### EventLevelAPI

```c
EventLevelAPI
```


### EventLevelOp

```c
EventLevelOp
```


### EventLevelDetail

```c
EventLevelDetail
```
