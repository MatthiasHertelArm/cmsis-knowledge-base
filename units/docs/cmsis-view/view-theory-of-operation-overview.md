---
id: "view-theory-of-operation-overview"
type: "concept"
domain: "trace"
title: "Theory of operation: Overview"
summary: "The software component Event Recorder provides API functions for event annotations in the application code or software component libraries. These API functions record event timing and data information while the program is executing."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/event_recorder.md#overview"
license: "Apache-2.0"
mode: "V"
---

The software component **Event Recorder** provides API functions for event annotations in the application code or software component libraries. These API functions record event timing and data information while the program is executing.

The Event Filter which is controlled from the target application or the debugger allows to specify the event ids that are stored in the **event buffer** that is located in the memory of the target system. This **event buffer** may be continuously read by the debug unit and displayed in the **Event Recorder** window of the debugger.

During program execution, the debugger reads the content of the **event buffer** using a standard debug unit that is connected via JTAG or SWD to the CoreSight Debug Access Port (DAP). The **Event Recorder** requires no trace hardware and can be therefore used on any Cortex-M processor.

(figure: Event Recorder)

 - er_theory explains in details how the Event Recorder collects event data, generates time stamps, and transfers this information via a debug unit to a host computer.
 - er_use provides instructions on how to enable Event Recorder in a project.
