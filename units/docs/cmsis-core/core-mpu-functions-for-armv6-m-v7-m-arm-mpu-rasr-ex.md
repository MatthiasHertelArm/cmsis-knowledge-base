---
id: "core-mpu-functions-for-armv6-m-v7-m-arm-mpu-rasr-ex"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: ARM_MPU_RASR_EX"
summary: "MPU Region Attribute and Size Register Value"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MPU_RASR_EX
```

 MPU Region Attribute and Size Register Value

This macro is used to construct a valid RASR value.
The ENABLE bit of the RASR value is implicitly set to 1.

- `DisableExec`:       Instruction access disable bit, 1= disable instruction fetches.
- `AccessPermission`:  Data access permission configures read/write access for User and Privileged mode. Possible values see ARM_MPU_AP_xxx.
- `AccessAttributes`:  Memory access attribution, see ARM_MPU_ACCESS_xxx.
- `SubRegionDisable`:  Sub-region disable field (8 bits).
- `Size`:              Region size with values defined under ARM_MPU_REGION_SIZE_xxx.
