---
id: "view-fault-example-for-b-u585i-iot02a-b"
type: "concept"
domain: "trace"
title: "Fault example for B-U585I-IOT02A board (Cortex-M33)"
summary: "This project is a simple Fault component example running on an Arm Cortex-M33 microcontroller on a STMicroelectronics B-U585I-IOT02A evaluation board."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Examples/Fault/B-U585I-IOT02A/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Examples/Fault/B-U585I-IOT02A/README.md"
license: "Apache-2.0"
mode: "V"
---

This project is a simple **Fault** component example running on an **Arm Cortex-M33** microcontroller
on a STMicroelectronics [**B-U585I-IOT02A**](https://www.st.com/en/evaluation-tools/b-u585i-iot02a.html) evaluation board.

The application allows triggering of specific faults upon which the fault information is saved and system is reset.
When system restarts the fault information is output via the **Event Recorder** and via the **STDIO (STLink Virtual COM Port)**.

The fault information can also be inspected with **Component Viewer** in a debug session.
