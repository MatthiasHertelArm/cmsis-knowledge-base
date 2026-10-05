---
id: "rtos2-process-isolation-define-mpu-protected-zones"
type: "concept"
domain: "rtos"
title: "Process Isolation: Define MPU Protected Zones"
summary: "In the architectural design phase an application is logically split into functionalities with the same integrity level (same safety requirements). They can safely operate within the same MPU Protected Zone and hence access same memory areas and peripherals."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md#define-mpu-protected-zones"
license: "Apache-2.0"
mode: "V"
---

In the architectural design phase an application is logically split into functionalities with the same integrity level (same safety requirements). They can safely operate within the same MPU Protected Zone and hence access same memory areas and peripherals. 

MPU protected zones are defined in an MPU table where each row describes an individual MPU zone and each cell in the row specifies an MPU region within that zone. For details see section [MPU Functions](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/../Core/group__mpu__functions.html) in CMSIS-Core(M) documentation.

> **Note**
> - Interrupt handlers bypass the MPU protection. For this reason, it is required that potential impact of all interrupt handlers is strictly analyzed to exclude unintended memory accesses.

**Zone Identifier** (Zone ID) is used to refer to a specific MPU protected zone. Zone ID value equals to the row index (starting from 0) in the MPU table that describes corresponding MPU Protected Zone.

An MPU Protected Zone is assigned to one or more RTOS threads. This is done by providing the Zone ID value in thread attributes osThreadAttr_t when creating the thread with the osThreadNew function.

**Example:**

```c
/* ThreadA thread attributes */
const osThreadAttr_t thread_A_attr = {
  .name       = "ThreadA",       // human readable thread name
  .attr_bits  = osThreadZone(3U) // assign thread to MPU protected zone with Zone Id 3
};
osThreadNew(ThreadA, NULL, &thread_A_attr);
```

[CMSIS-Zone](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/../Zone/index.html) provides a utility that allows graphic configuration of MPU protected zones and generates MPU table in the CMSIS format.
