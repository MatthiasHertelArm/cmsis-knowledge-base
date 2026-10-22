---
id: "core-mpu-functions-for-armv8-m"
type: "concept"
domain: "core"
title: "MPU Functions for Armv8-M"
summary: "Functions that relate to the Memory Protection Unit."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_mpu8.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_mpu8.txt"
license: "Apache-2.0"
mode: "V"
---

Functions that relate to the Memory Protection Unit.

The following functions support the optional Memory Protection Unit (MPU) that is available on the Cortex-M23, M33, M35P processor.

The MPU is used to prevent from illegal memory accesses that are typically caused by errors in an application software.

**Example:**
```
int main() 
{
  // Set Region 0 using Attr 0
  ARM_MPU_SetMemAttr(0UL, ARM_MPU_ATTR( /* Normal memory */
    MPU_ATTR_NORMAL_OUTER_WT_TR_RA_WA,  /* Outer Write-Back transient with read and write allocate */
    MPU_ATTR_NORMAL_INNER_WT_TR_RA_WA   /* Inner Write-Through transient with read and write allocate */
  ));
  
  ARM_MPU_SetRegion(0UL,
    ARM_MPU_RBAR(0x08000000UL, ARM_MPU_SH_NON, ARM_MPU_AP_RW, ARM_MPU_AP_NP, ARM_MPU_XN),  /* Non-shareable, read/write, non-privileged, execute-never */
    ARM_MPU_RLAR(0x080FFFFFUL, MAIR_ATTR(0))                        /* 1MB memory block using Attr 0 */
  );
  
  ARM_MPU_Enable(0);
  
  // Execute application code that is access protected by the MPU
  
  ARM_MPU_Disable();
}
```
