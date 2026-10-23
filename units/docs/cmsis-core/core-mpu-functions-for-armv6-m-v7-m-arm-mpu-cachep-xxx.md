---
id: "core-mpu-functions-for-armv6-m-v7-m-arm-mpu-cachep-xxx"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: ARM_MPU_CACHEP_xxx"
summary: "Cache policy values for MPU region access attributes (in RASR field)"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MPU_CACHEP_xxx
```

 Cache policy values for MPU region access attributes (in RASR field)

The following define values are used to compose the cacheability flags within the
access attributes for an MPU region:
|\#define                      | Value | Cacheability policy     |
|:-----------------------------|:------|:------------------------|
| ARM_MPU_CACHEP_NOCACHE       | 00b   | Non-cacheable           |
| ARM_MPU_CACHEP_WB_WRA        | 01b   | Write-back, write and read allocate |
| ARM_MPU_CACHEP_WT_NWA        | 10b   | Write-through, no write allocate    |
| ARM_MPU_CACHEP_WB_NWA        | 11b   | Write-back, no write allocate       |
