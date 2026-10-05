---
id: "view-theory-of-operation-add-event-recorder-component"
type: "concept"
domain: "trace"
title: "Theory of operation: Add Event Recorder Component"
summary: "To use the Event Recorder in an application, you need to:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/event_recorder.md#add-event-recorder-component"
license: "Apache-2.0"
mode: "V"
---

To use the Event Recorder in an application, you need to:

 - Select the software component **CMSIS-View:Event Recorder** using the RTE management dialog.

    (figure: Select Event Recorder)
    **Note:** Usually, you select the **DAP** variant. If you are using a simulation model (FastModel or Arm Virtual Hardware), you can select er_semihosting to write the Event Recorder data into a file on the PC.
 - Include the *EventRecorder.h* header file and add the event recorder initialization function to the source code:

```c
    :
  #include "EventRecorder.h"                        // ARM::CMSIS-View:Event Recorder
    :
  int main (void) {
    :
    HAL_Init();                                     // configure hardware abstraction layer
    SystemClock_Config();                           // configure system clock
    MemoryBus_Config();                             // configure external memory bus
    EventRecorderInitialize (EventRecordAll, 1);    // initialize and start Event Recorder
    :
    // other application code
  }
```

> **Note**
> - By default, the Event Recorder uses the DWT Cycle Counter as a time stamp source. This is not available on Cortex-M0/M0+/M23. Change the configuration to use an alternative timer instead.
> - For Keil RTX5 (version 5.4.0 and above), no call to EventRecorderInitialize is required. Instead enable **Event Recorder Configuration - Global Initialization** in the RTX_Config.h file. Refer to the [CMSIS-RTX Event Recorder Configuration](https://arm-software.github.io/CMSIS-RTX/latest/config_rtx5.html#evtrecConfig) for more information.
