---
id: "core-mpu-functions-for-armv6-m-v7-m"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M"
summary: "Functions that relate to the Memory Protection Unit."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

Functions that relate to the Memory Protection Unit.

The following functions support the optional Memory Protection Unit (MPU) that is available on the Cortex-M0+, M3, M4 and M7 processor.

The MPU is used to prevent from illegal memory accesses that are typically caused by errors in an application software.

**Example:**
```
int main() 
{
  // Set Region 0
  ARM_MPU_SetRegionEx(0UL, 0x08000000UL, ARM_MPU_RASR(0UL, ARM_MPU_AP_FULL, 0UL, 0UL, 1UL, 1UL, 0x00UL, ARM_MPU_REGION_SIZE_1MB));
  
  ARM_MPU_Enable(0);
  
  // Execute application code that is access protected by the MPU
  
  ARM_MPU_Disable();
}
```
