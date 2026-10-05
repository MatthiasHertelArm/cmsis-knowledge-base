---
id: "rtx-configure-rtx-v5-mutex-configuration"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: Mutex Configuration"
summary: "RTX5 provides several parameters to configure the CMSIS_RTOS_MutexMgmt functions."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#mutex-configuration"
license: "Apache-2.0"
mode: "V"
---

RTX5 provides several parameters to configure the CMSIS_RTOS_MutexMgmt functions.

**Mutex Configuration Options**

(figure: RTX_Config.h: Mutex Configuration)

Name                                   | \#define                 | Description
---------------------------------------|--------------------------|----------------------------------------------------------------
Object specific Memory allocation      | `OS_MUTEX_OBJ_MEM`      | Enables object specific memory allocation. See ObjectMemoryPool.
Number of Mutex objects                | `OS_MUTEX_NUM`          | Defines maximum number of objects that can be active at the same time. Applies to objects with system provided memory for control blocks. Value range is `[1-1000]`.
### Object-specific Memory Allocation

When object-specific memory is used, the pool size for all Mutex objects is specified by `OS_MUTEX_NUM`. Refer to ObjectMemoryPool.
