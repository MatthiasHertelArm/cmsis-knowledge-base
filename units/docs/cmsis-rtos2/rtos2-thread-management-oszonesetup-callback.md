---
id: "rtos2-thread-management-oszonesetup-callback"
type: "concept"
domain: "rtos"
title: "Thread Management: osZoneSetup_Callback"
summary: "The callback function osZoneSetup_Callback is called by the kernel when MPU Protected Zone changes. The function shall be implemented in user application."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void osZoneSetup_Callback (uint32_t zone);
```


The callback function **osZoneSetup_Callback** is called by the kernel when MPU Protected Zone changes.
The function shall be implemented in user application.

**Code Example:**
```
/* Update MPU settings for newly activating Zone */
void osZoneSetup_Callback (uint32_t zone) {
 
  if (zone >= ZONES_NUM) {
    //Issue an error for incorrect zone value
  }
 
  ARM_MPU_Disable();
  ARM_MPU_Load(mpu_table[zone], MPU_REGIONS);
  ARM_MPU_Enable(MPU_CTRL_PRIVDEFENA_Msk);
}
```

`ZONES_NUM` is the total amount of zones allocated by the application.
For `ARM_MPU_...` functions refer to **MPU Functions** in CMSIS-Core documentation.
