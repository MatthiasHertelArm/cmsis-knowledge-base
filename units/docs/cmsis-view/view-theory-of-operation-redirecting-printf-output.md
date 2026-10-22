---
id: "view-theory-of-operation-redirecting-printf-output"
type: "concept"
domain: "trace"
title: "Theory of operation: Redirecting printf output"
summary: "The Event Recorder can be used to retarget printf output. This is especially interesting for targets without ITM, such as Cortex-M0/M0+/M23. Steps to enable this:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/event_recorder.md#redirecting-printf-output"
license: "Apache-2.0"
mode: "V"
---

The Event Recorder can be used to retarget printf output. This is especially interesting for targets without ITM, such as Cortex-M0/M0+/M23. Steps to enable this:

 1. In the Manage Run-Time Environment window, select the component **CMSIS-Compiler:STDOUT:Event Recorder**.
 2. Select the component **CMSIS-View:Event Recorder** or use the **Resolve** button.
 3. In the user code, include *EventRecorder.h* and call the `EventRecorderInitialize()` function in `main()`.

Also see [CMSIS-Compiler documentation](https://arm-software.github.io/CMSIS-Compiler/latest/index.html) for addition details about printf redirecting.
