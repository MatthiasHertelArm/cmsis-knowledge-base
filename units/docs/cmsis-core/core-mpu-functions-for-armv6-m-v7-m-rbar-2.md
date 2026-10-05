---
id: "core-mpu-functions-for-armv6-m-v7-m-rbar-2"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: RBAR"
summary: "Holds the base address of the region identified by MPU_RNR. On a write, can also be used to update the base address of a specified region, in the range 0 to 15, updating MPU_RNR with the new region number."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
MPU_Type::RBAR
```

Holds the base address of the region identified by MPU_RNR. On a write, can also be used
to update the base address of a specified region, in the range 0 to 15, updating MPU_RNR
with the new region number.
 
| Bits    | Name          | Function                                                      |
| :------ | :------------ | :------------------------------------------------------------ |
| [31:5]  | ADDR          | Base address of the region.                                   |
| [4]     | VALID         | 1 - Update MPU_Type::RNR to the value obtained by zero extending the REGION value specified in this write, and apply the base address update to this region. |
| [3:0]   | REGION        | On writes, can specify the number of the region to update, see VALID field description. |
