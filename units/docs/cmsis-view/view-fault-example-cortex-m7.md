---
id: "view-fault-example-cortex-m7"
type: "concept"
domain: "trace"
title: "Fault example (Cortex-M7)"
summary: "This project is a simple Fault component example running on an Arm Cortex-M7 microcontroller simulated by Arm Virtual Hardware with the FVPMPS2Cortex-M7 model simulator."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Examples/Fault/FVP_MPS2_Cortex-M7/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Examples/Fault/FVP_MPS2_Cortex-M7/README.md"
license: "Apache-2.0"
mode: "V"
---

This project is a simple **Fault** component example running on an **Arm Cortex-M7** microcontroller simulated by
[**Arm Virtual Hardware**](https://www.arm.com/products/development-tools/simulation/virtual-hardware) with the **FVP_MPS2_Cortex-M7** model simulator.

The application allows triggering of specific faults upon which the fault information is saved and system is reset.
When system restarts the fault information is output via the **Event Recorder**.

The fault information can also be inspected with **Component Viewer** in a debug session.

> **Note**  
> This example runs on the [**Arm Virtual Hardware**](https://www.arm.com/products/development-tools/simulation/virtual-hardware) simulator
> and does not require any hardware.
