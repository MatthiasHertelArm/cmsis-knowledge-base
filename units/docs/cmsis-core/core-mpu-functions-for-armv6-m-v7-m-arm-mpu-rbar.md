---
id: "core-mpu-functions-for-armv6-m-v7-m-arm-mpu-rbar"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: ARM_MPU_RBAR"
summary: "This preprocessor function can be used to construct a valid RBAR value. The VALID bit is implicitly set to 1."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MPU_RBAR
```

 MPU Region Base Address Register Value

This preprocessor function can be used to construct a valid RBAR value.
The VALID bit is implicitly set to 1.

- `Region`: The region to be configured, number 0 to 15.
- `BaseAddress`: The base address for the region.
