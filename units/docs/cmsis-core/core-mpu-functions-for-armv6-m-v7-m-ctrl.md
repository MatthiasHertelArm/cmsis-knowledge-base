---
id: "core-mpu-functions-for-armv6-m-v7-m-ctrl"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: CTRL"
summary: "Enables the MPU, and when the MPU is enabled, controls whether the default memory map is enabled as a background region for privileged accesses, and whether the MPU is enabled for HardFaults, NMIs, and exception handlers when FAULTMASK …"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
MPU_Type::CTRL
```

Enables the MPU, and when the MPU is enabled, controls whether the default memory map
is enabled as a background region for privileged accesses, and whether the MPU is enabled
for HardFaults, NMIs, and exception handlers when FAULTMASK is set to 1.

| Bits    | Name          | Function                                                      |
| :------ | :------------ | :------------------------------------------------------------ |
| [31:3]  | -             | Reserved.                                                     |
| [2]     | PRIVDEFENA    | 0 - Disables the default memory map. 1 - Enables the default memory map as a background region for privileged access. |
| [1]     | HFNMIENA      | 0 - Disables the MPU for exception handlers. 1 - Use the MPU for memory accesses by exception handlers. |
| [0]     | ENABLE        | 0 - The MPU is disabled. 1 - The MPU is enabled.              |
