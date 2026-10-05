---
id: "core-mpu-functions-for-armv6-m-v7-m-rbar"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: RBAR"
summary: "This value specifies the start address of the MPU protected memory region. The address must be a multiple of the region size (size aligned)."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MPU_Region_t::RBAR
```

This value specifies the start address of the MPU protected memory region. The address must be a multiple of the region size (size aligned).

See MPU_Type::RBAR for details about field bit format.
