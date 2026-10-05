---
id: "view-event-execution-statistics"
type: "concept"
domain: "trace"
title: "Event Execution Statistics"
summary: "Macros that record start/stop events for the execution statistic display"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_evr.txt"
license: "Apache-2.0"
mode: "V"
---

Macros that record start/stop events for the execution statistic display

This section describes the macros that call event recorder functions from the user application to record start/stop events for program execution statistics.

The start/stop events allow to measure execution times with different slots (0 - 15) in four different groups (_G_ = A - D). The call to 'EventStart' starts a timer slot; the call to 'EventStop' stops the related timer.  A call to EventStop with slot 15  stops the timers of all slots in the specific group.

The macros allow to record either:
  - Filename and line number of the function call by using the variant EventStart_G_ or EventStop_G_.
  - Integer values v1 and v2 by using the variant EventStart_G_v or EventStop_G_v.

The start/stop events are using The four event groups (_G_ = A - D) that are available to the user are mapped to the level information in EventID and may be used for filtering. The mapping is as shown in the table below.

Start/stop group         | A                     | B                   | C                  | D
:------------------------|:---------------------:|:-------------------:|:------------------:|:-----------------------:
Event level              | Error                 | API                 | Op                 | Data
Parameter **recording**  | EventRecordError | EventRecordAPI | EventRecordOp | EventRecordDetail

It is required to call the EventRecorderInitialize function before using start/stop events. The parameter **recording** from the table above can be used in the functions EventRecorderInitialize, EventRecorderEnable, and EventRecorderDisable. er_filtering may be used to change the settings in the debugger.

The following code shows the setup of the Event Recorder for start/stop events:

- Record all events:
```
EventRecorderInitialize (EventRecordAll, 1);               // enable recording for all events
```

- Record only start/stop events for group A and group B.
```
EventRecorderInitialize (EventRecordNone, 1U);             // Initialize and start Event Recorder, record no events
EventRecorderEnable (EventRecordError+EventRecordAPI,      // Record group A and group B
                     EvtStatistics_No, EvtStatistics_No);  // for start/stop events
```

**Code example**
 - Refer to scvd_evt_stat
