---
id: "view-theory-of-operation-features-and-benefits"
type: "concept"
domain: "trace"
title: "Theory of operation: Features and Benefits"
summary: "This section describes how the Event Recorder collects event data, generates time stamps, and transfers this information via a debug unit to a host computer."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/event_recorder.md#features-and-benefits"
license: "Apache-2.0"
mode: "V"
---

- Provides visibility to the dynamic execution of an application at little (memory) cost.
 - Works on all Cortex-M devices with JTAG or SWD debug ports.
 - Adds RTOS awareness to a development tool without complex DLL programming.
 - printf re-targeting for devices without ITM, such as Arm Cortex-M0/M0+/M23.
 - Fast time-deterministic execution of event recorder functions with minimal code and timing overhead.
 - For Arm Cortex-M3/M4/M7/M33/M55/M85 processor based devices, Event Recorder functions will not disable interrupts.
 - No need for a debug or release build as the event annotations can remain in production code.
 - Collecting the data from the on-chip memory is done using simple read commands.
 - Using the DWT Cycle Count register for creating time stamps reduces code overhead (available on Arm Cortex-M3/M4/M7/M33/M55/M85).
# Theory of operation

This section describes how the **Event Recorder** collects event data, generates time stamps, and transfers this information via a debug unit to a host computer.

The **Event Recorder** is implemented in the target application using the software component
**CMSIS-View:Event Recorder** which adds the source file *EventRecorder.c* to the application. Each event is stored in a 16-byte structure that is composed of a 16-bit *id*, 32-bit time stamp, two 32-bit data values and consistency check values.

To store these events, a circular buffer is provided that can store a minimum of 8 events. The size of this circular buffer is configurable with the `#define EVENT_RECORD_COUNT`.
