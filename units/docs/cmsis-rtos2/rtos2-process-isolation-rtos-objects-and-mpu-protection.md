---
id: "rtos2-process-isolation-rtos-objects-and-mpu-protection"
type: "concept"
domain: "rtos"
title: "Process Isolation: RTOS Objects and MPU Protection"
summary: "To access RTOS objects from the application RTOS APIs rely on a numeric xxx_id parameter associated with the object as explained in rtos_objects. For example as evt_flags in this code:"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md#rtos-objects-and-mpu-protection"
license: "Apache-2.0"
mode: "V"
---

To access RTOS objects from the application RTOS APIs rely on a numeric `xxx_id` parameter associated with the object as explained in rtos_objects. For example as `evt_flags` in this code:

```c
osEventFlagsId_t evt_flags;
evt_flags = osEventFlagsNew(NULL);
osEventFlagsSet(evt_flags, 1);
```

The allocation of an RTOS object to the memory in a specific MPU Protected Zone does not provide access restriction. The access restriction can be bypassed if another thread calls the CMSIS-RTOS2 API with the object ID of the RTOS object as argument. The CMSIS-RTOS2 function is executed in handler mode and therefore can access and modify the RTOS object without raising a Memory Fault.

To enable access control for RTOS objects the rtos_process_isolation_safety_class concept is introduced in CMSIS-RTOS2.
