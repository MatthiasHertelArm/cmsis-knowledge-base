---
id: "view-fault-example-cortex-m7-user-interface"
type: "concept"
domain: "trace"
title: "Fault example (Cortex-M7): User Interface"
summary: "This example uses simulator console for User Interface."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Examples/Fault/FVP_MPS2_Cortex-M7/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Examples/Fault/FVP_MPS2_Cortex-M7/README.md#user-interface"
license: "Apache-2.0"
mode: "V"
---

This example uses **simulator console** for User Interface.

The fault triggering is done by entering a number via **simulator console**, see possible values below:

- `0` : Terminate the example
- `1` : trigger the Data access (precise) Memory Management fault
- `2` : trigger the Data access (precise) Bus fault
- `3` : trigger the Data access (imprecise) Bus fault
- `4` : trigger the Instruction execution Bus fault
- `5` : trigger the Undefined instruction Usage fault
- `6` : trigger the Divide by 0 Usage fault
