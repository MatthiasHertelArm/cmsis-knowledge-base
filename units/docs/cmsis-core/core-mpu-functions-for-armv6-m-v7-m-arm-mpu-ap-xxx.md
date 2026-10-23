---
id: "core-mpu-functions-for-armv6-m-v7-m-arm-mpu-ap-xxx"
type: "concept"
domain: "core"
title: "MPU Functions for Armv6-M/v7-M: ARM_MPU_AP_xxx"
summary: "Values for MPU region access permissions (in RASR field)"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_mpu.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MPU_AP_xxx
```

 Values for MPU region access permissions (in RASR field)

The following define values are used to compose the access permission for an MPU region:
|\#define                  | Value            | Access permissions               |
|:-------------------------|:-----------------|:---------------------------------------------------------|
|ARM_MPU_AP_NONE           | 0x0U             | None: any access generates a permission fault.
|ARM_MPU_AP_PRIV           | 0x1U             | Privileged Read/Write: privileged access only; any unprivileged access generates a permission fault.
|ARM_MPU_AP_URO            | 0x2U             | Privileged Read/Write; Unprivileged Read-only: any unprivileged write generates a permission fault.
|ARM_MPU_AP_FULL           | 0x3U             | Privileged Read/Write. Unprivileged Read/Write: full access, permission faults are never generated.
|ARM_MPU_AP_PRO            | 0x5U             | Privileged Read-only: any unprivileged access or privileged write generates a permission fault.
|ARM_MPU_AP_RO             | 0x6U             | Privileged and Unprivileged Read-only: any write generates a permission fault.
