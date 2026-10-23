---
id: "core-mpu-functions-for-armv6-m-v7-m-type"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: TYPE"
summary: "The MPU Type Register indicates how many regions the MPU support. Software can use it to determine if the processor implements an MPU."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
MPU_Type::TYPE
```

The MPU Type Register indicates how many regions the MPU support. Software can use it
to determine if the processor implements an MPU.

| Bits    | Name          | Function                                                      |
| :------ | :------------ | :------------------------------------------------------------ |
| [31:24] | -             | Reserved.                                                     |
| [23:16] | IREGION       | Instruction region. RAZ. Armv7-M only supports a unified MPU. |
| [15:8]  | DREGION       | Number of regions supported by the MPU. If this field reads-as-zero the processor does not implement an MPU. |
| [7:1]   | -             | Reserved.                                                     |
| [0]     | SEPARATE      | Indicates support for separate instruction and data address maps. RAZ. Armv7-M only supports a unified MPU. |
