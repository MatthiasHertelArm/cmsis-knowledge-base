---
id: "rtos2-generic-definitions-osflagserrorresource"
type: "concept"
domain: "rtos"
title: "Generic Definitions: osFlagsErrorResource"
summary: "This error is returned when you try to get a flag that was not set and timeout 0 was specified. Is also returned when the specified object identifier is corrupt or invalid."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osFlagsErrorResource
```

 This error is returned when you try to get a flag that was not set _and_ timeout 0 was
specified. Is also returned when the specified object identifier is corrupt or invalid.

Reference: 
 - osThreadFlagsSet
 - osThreadFlagsClear
 - osThreadFlagsWait
 - osEventFlagsSet
 - osEventFlagsClear
 - osEventFlagsWait
