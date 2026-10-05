---
id: "rtx-create-an-rtx5-project-add-event-recorder-visibility"
type: "concept"
domain: "rtos"
title: "Create an RTX5 Project: Add Event Recorder Visibility"
summary: "\\ifnot FuSaRTS RTX5 interfaces to the Event Recorder to provide event information which helps you to understand and analyze the operation."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/project.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/project.md#add-event-recorder-visibility"
license: "Apache-2.0"
mode: "V"
---

\ifnot FuSaRTS
RTX5 interfaces to the [Event Recorder](https://arm-software.github.io/CMSIS-View/latest/evr.html) to provide event
information which helps you to understand and analyze the operation.

- To use the Event Recorder together with RTX5, select the software component **CMSIS-View:Event Recorder**.
- Select the **Source** variant of the software component **CMSIS:RTOS2 (API):Keil RTX5**.
- Enable the related settings under evtrecConfig.
- Build the application code and download it to the debug hardware.

\endif

Once the target application generates event information, it can be viewed for example with the
[eventlist](https://github.com/ARM-software/CMSIS-View/tree/main/tools/eventlist) tool.

\ifnot FuSaRTS
