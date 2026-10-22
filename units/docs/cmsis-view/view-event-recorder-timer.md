---
id: "view-event-recorder-timer"
type: "concept"
domain: "trace"
title: "Event Recorder - Timer"
summary: "Functions that access a configurable hardware timer"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

Functions that access a configurable hardware timer

This section contains user-provided functions, which configure and provide timing information for recorded events.
It is required to implement these functions, when User Timer is selected as time stamp source.

The source file **EventRecorder.c** implements `__WEAK` functions for EventRecorderTimerSetup, EventRecorderTimerGetFreq and EventRecorderTimerGetCount.
This allows to overwrite the functions by a user application.

**Note:** ARM Cortex-M3/M4/M7/M33 processors provide a debug timer (DWT CYCCNT) that can be used during debug. Refer to
DWT Programmers' model
for more information.

**Code** **Example**
```
```
