---
id: "core-mpu-functions-for-armv6-m-v7-m-arm-mpu-region-size-xxx"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: ARM_MPU_REGION_SIZE_xxx"
summary: "Size values of a MPU region (in RASR field)"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MPU_REGION_SIZE_xxx
```

 Size values of a MPU region (in RASR field)

The following define values are used to compose the size information for an MPU region:

|\#define                  | Value            | Description                                              |
|:-------------------------|:-----------------|:---------------------------------------------------------|
|ARM_MPU_REGION_SIZE_32B   | 0x04U            | Region size 32 Bytes
|ARM_MPU_REGION_SIZE_64B   | 0x05U            | Region size 64 Bytes
|ARM_MPU_REGION_SIZE_128B  | 0x06U            | Region size 128 Bytes
|ARM_MPU_REGION_SIZE_256B  | 0x07U            | Region size 256 Bytes
|ARM_MPU_REGION_SIZE_512B  | 0x08U            | Region size 512 Bytes
|ARM_MPU_REGION_SIZE_1KB   | 0x09U            | Region size 1 KByte
|ARM_MPU_REGION_SIZE_2KB   | 0x0AU            | Region size 2 KBytes
|ARM_MPU_REGION_SIZE_4KB   | 0x0BU            | Region size 4 KBytes
|ARM_MPU_REGION_SIZE_8KB   | 0x0CU            | Region size 8 KBytes
|ARM_MPU_REGION_SIZE_16KB  | 0x0DU            | Region size 16 KBytes
|ARM_MPU_REGION_SIZE_32KB  | 0x0EU            | Region size 32 KBytes
|ARM_MPU_REGION_SIZE_64KB  | 0x0FU            | Region size 64 KBytes
|ARM_MPU_REGION_SIZE_128KB | 0x10U            | Region size 128 KBytes
|ARM_MPU_REGION_SIZE_256KB | 0x11U            | Region size 256 KBytes
|ARM_MPU_REGION_SIZE_512KB | 0x12U            | Region size 512 KBytes
|ARM_MPU_REGION_SIZE_1MB   | 0x13U            | Region size 1 MByte
|ARM_MPU_REGION_SIZE_2MB   | 0x14U            | Region size 2 MBytes
|ARM_MPU_REGION_SIZE_4MB   | 0x15U            | Region size 4 MBytes
|ARM_MPU_REGION_SIZE_8MB   | 0x16U            | Region size 8 MBytes
|ARM_MPU_REGION_SIZE_16MB  | 0x17U            | Region size 16 MBytes
|ARM_MPU_REGION_SIZE_32MB  | 0x18U            | Region size 32 MBytes
|ARM_MPU_REGION_SIZE_64MB  | 0x19U            | Region size 64 MBytes
|ARM_MPU_REGION_SIZE_128MB | 0x1AU            | Region size 128 MBytes
|ARM_MPU_REGION_SIZE_256MB | 0x1BU            | Region size 256 MBytes
|ARM_MPU_REGION_SIZE_512MB | 0x1CU            | Region size 512 MBytes
|ARM_MPU_REGION_SIZE_1GB   | 0x1DU            | Region size 1 GByte
|ARM_MPU_REGION_SIZE_2GB   | 0x1EU            | Region size 2 GBytes
|ARM_MPU_REGION_SIZE_4GB   | 0x1FU            | Region size 4 GBytes
