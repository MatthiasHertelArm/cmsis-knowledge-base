---
id: "rtos2-process-isolation-load-mpu-protected-zone"
type: "concept"
domain: "rtos"
title: "Process Isolation: Load MPU Protected Zone"
summary: "When switching threads the RTOS kernel compares Zone IDs of the currently running thread and the next thread to be executed. If the Zone Ids are different then a callback function osZoneSetup_Callback is called."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md#load-mpu-protected-zone"
license: "Apache-2.0"
mode: "V"
---

When switching threads the RTOS kernel compares Zone IDs of the currently running thread and the next thread to be executed. If the Zone Ids are different then a callback function osZoneSetup_Callback is called. This callback function shall be implemented in the user application code to actually switch to the new MPU Protected Zone. In the function the user should load the MPU Protected Zone according to the Zone Id provided in the argument.

**Example:**

```c
/* Update MPU settings for newly activating Zone */
void osZoneSetup_Callback (uint32_t zone) {

  if (zone >= ZONES_NUM) {
    // Here issue an error for incorrect zone value
  }

  ARM_MPU_Load(mpu_table[zone], MPU_REGIONS);
}
```
