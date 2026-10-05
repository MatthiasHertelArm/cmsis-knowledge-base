---
id: "core-mpu-functions-for-armv6-m-v7-m-rasr"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: RASR"
summary: "Defines the size and access behavior of the region identified by MPU_RNR, and enables that region."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
MPU_Type::RASR
```

Defines the size and access behavior of the region identified by MPU_RNR, and enables
that region.

| Bits    | Name          | Function                                                      |
| :------ | :------------ | :------------------------------------------------------------ |
| [31:29] | -             | Reserved.                                                     |
| [28]    | XN            | Execute Never.                                                |
| [27]    | -             | Reserved.                                                     |
| [26:24] | AP            | Access Permissions, see ARM_MPU_AP_xxx.                  |
| [23:22] | -             | Reserved.                                                     |
| [21:19] | TEX           | Type Extension.                                               |
| [18]    | S             | Shareable.                                                    |
| [17]    | C             | Cacheable.                                                    |
| [16]    | B             | Bufferable.                                                   |
| [15:8]  | SRD           | Subregion Disable. For regions of 256 bytes or larger, each bit of this field controls whether one of the eight equal subregions is enabled (0) or disabled (1). 
| [7:6]   | -             | Reserved.                                                     |
| [5:1]   | SIZE          | Indicates the region size. The region size, in bytes, is 2(SIZE+1). SIZE field values less than 4 are reserved, because the smallest supported region size is 32 bytes. |
| [0]     | ENABLE        | 0 - This region is disabled. 1 - This region is enabled.      |
