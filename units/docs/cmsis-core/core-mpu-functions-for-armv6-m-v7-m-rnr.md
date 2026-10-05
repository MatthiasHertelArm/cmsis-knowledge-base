---
id: "core-mpu-functions-for-armv6-m-v7-m-rnr"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: RNR"
summary: "Selects the region currently accessed by MPUType::RBAR and MPUType::RASR."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
MPU_Type::RNR
```

Selects the region currently accessed by MPU_Type::RBAR and MPU_Type::RASR.

| Bits    | Name          | Function                                                      |
| :------ | :------------ | :------------------------------------------------------------ |
| [31:8]  | -             | Reserved.                                                     |
| [7:0]   | REGION        | Indicates the memory region accessed.                         |
