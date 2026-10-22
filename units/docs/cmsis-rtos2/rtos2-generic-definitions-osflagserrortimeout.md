---
id: "rtos2-generic-definitions-osflagserrortimeout"
type: "concept"
domain: "rtos"
title: "Generic Definitions: osFlagsErrorTimeout"
summary: "This error is returned if a timeout was specified and the specified flags were not set, when the timeout occurred."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osFlagsErrorTimeout
```

 This error is returned if a timeout was specified and the specified flags were not set, when the
timeout occurred.

Reference: 
 - osThreadFlagsSet
 - osThreadFlagsClear
 - osThreadFlagsWait
 - osEventFlagsSet
 - osEventFlagsClear
 - osEventFlagsWait
