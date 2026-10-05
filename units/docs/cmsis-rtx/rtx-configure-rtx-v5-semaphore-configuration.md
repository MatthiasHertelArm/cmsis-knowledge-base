---
id: "rtx-configure-rtx-v5-semaphore-configuration"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: Semaphore Configuration"
summary: "RTX5 provides several parameters to configure the CMSIS_RTOS_SemaphoreMgmt functions."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#semaphore-configuration"
license: "Apache-2.0"
mode: "V"
---

RTX5 provides several parameters to configure the CMSIS_RTOS_SemaphoreMgmt functions.

**Semaphore Configuration Options**

(figure: RTX_Config.h: Semaphore Configuration)

Name                                   | \#define                 | Description
---------------------------------------|--------------------------|----------------------------------------------------------------
Object specific Memory allocation      | `OS_SEMAPHORE_OBJ_MEM`  | Enables object specific memory allocation. See ObjectMemoryPool.
Number of Semaphore objects            | `OS_SEMAPHORE_NUM`      | Defines maximum number of objects that can be active at the same time. Applies to objects with system provided memory for control blocks. Value range is `[1-1000]`.
### Object-specific memory allocation

When Object-specific Memory is used, the pool size for all Semaphore objects is specified by `OS_SEMAPHORE_NUM`. Refer to ObjectMemoryPool.
