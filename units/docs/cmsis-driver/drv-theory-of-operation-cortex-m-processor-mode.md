---
id: "drv-theory-of-operation-cortex-m-processor-mode"
type: "concept"
domain: "drivers"
title: "Theory of Operation: Cortex-M Processor Mode"
summary: "The CMSIS-Driver functions access peripherals and interrupts and are designed to execute in Privileged mode. When calling CMSIS-Driver functions from RTOS threads, it should be ensure that these threads execute in Privileged mode."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/operation.md#cortex-m-processor-mode"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Driver functions access peripherals and interrupts and are designed to execute in **Privileged** mode. When calling CMSIS-Driver functions from RTOS threads, it should be ensure that these threads execute in **Privileged** mode.
