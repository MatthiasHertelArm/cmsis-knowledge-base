---
id: "core-mpu-functions-for-armv6-m-v7-m-arm-mpu-rasr"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: ARM_MPU_RASR"
summary: "MPU Region Attribute and Size Register Value"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MPU_RASR
```

 MPU Region Attribute and Size Register Value

This macro is used to construct a valid RASR value.
The ENABLE bit of the RASR value is implicitly set to 1.

- `DisableExec`:       Instruction access disable bit. 1 = disable instruction fetches. 
- `AccessPermission`:  Data access permission configures read/write access for User and Privileged mode. Possible values see ARM_MPU_AP_xxx.
- `TypeExtField`:      Type extension field, allows you to configure memory access type, for example strongly ordered, peripheral.
- `IsShareable`:       1 = region is shareable between multiple bus masters.
- `IsCacheable`:       1 = region is cacheable (values may be kept in cache).
- `IsBufferable`:      1 = region is bufferable (when using write-back caching). Cacheable but non-bufferable regions use write-through policy.
- `SubRegionDisable`:  Sub-region disable field (8 bits).
- `Size`:              Region size with values defined under ARM_MPU_REGION_SIZE_xxx.
