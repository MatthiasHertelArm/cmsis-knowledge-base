---
id: "rtos2-generic-definitions-osflagserrorisr"
type: "concept"
domain: "rtos"
title: "Generic Definitions: osFlagsErrorISR"
summary: "This error is returned when a non-ISR-callable function was called from an ISR."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osFlagsErrorISR
```

 This error is returned when a non-ISR-callable function was called from an ISR.

Reference: 
 - osThreadFlagsSet
 - osThreadFlagsClear
 - osThreadFlagsWait
 - osEventFlagsSet
 - osEventFlagsClear
 - osEventFlagsWait
