---
id: "core-mpu-functions-for-armv6-m-v7-m-arm-mpu-access-xxx"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: ARM_MPU_ACCESS_xxx"
summary: "Values for MPU region access attributes (in RASR field)"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MPU_ACCESS_xxx
```

 Values for MPU region access attributes (in RASR field)

The following define values are used to compose the access attributes for an MPU region:
|\#define                      | TEX  | Shareable | Cacheable | Bufferable | Description             |
|:-----------------------------|:-----|:----------|:----------|:-----------|:------------------------|
| ARM_MPU_ACCESS_ORDERED       | 000b | 1         | 0         | 0          | Strongly ordered memory |
| ARM_MPU_ACCESS_DEVICE(S)     | 0s0b | S         | 0         | S          | Memory mapped peripheral device, shared (S=1) or non-shared (S=0) |
| ARM_MPU_ACCESS_NORMAL(O,I,S) | 1BBb | S         | A         | A          | Normal memory, with outer/inner cache policy (O/I=ARM_MPU_CACHEP_xxx, shared (S=1) or non-share (S=0) |
