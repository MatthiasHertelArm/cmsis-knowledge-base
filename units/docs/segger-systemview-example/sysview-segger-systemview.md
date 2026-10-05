---
id: "sysview-segger-systemview"
type: "concept"
domain: "trace"
title: "SEGGER-SystemView"
summary: "This example project shows how to use SEGGER SystemView with pyOCD."
status: "draft"
collection: "segger-systemview-example"
source: "Arm-Examples/SEGGER-SystemView@9be0601:README.md"
doc_source: "https://github.com/Arm-Examples/SEGGER-SystemView/blob/9be0601/README.md"
license: "Apache-2.0"
mode: "V"
---

This example project shows how to use SEGGER SystemView with pyOCD.

It streams FreeRTOS and system activity to the SEGGER SystemView application for graphical inspection:

(figure: SystemView GUI)

pyOCD reads RTT data directly from target memory.

This example uses the NUCLEO-H743ZI2 board. The same approach also works with other devices and boards.
