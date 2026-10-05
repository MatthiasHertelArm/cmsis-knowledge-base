---
id: "rtx-configure-rtx-v5-memory-pool-configuration"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: Memory Pool Configuration"
summary: "RTX5 provides several parameters to configure the CMSIS_RTOS_PoolMgmt functions."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#memory-pool-configuration"
license: "Apache-2.0"
mode: "V"
---

RTX5 provides several parameters to configure the CMSIS_RTOS_PoolMgmt functions.

**Memory Pool Configuration Options**

(figure: RTX_Config.h: Memory Pool Configuration)

Name                                   | \#define                 | Description
---------------------------------------|--------------------------|----------------------------------------------------------------
Object specific Memory allocation      | `OS_MEMPOOL_OBJ_MEM`    | Enables object specific memory allocation. See ObjectMemoryPool.
Number of Memory Pool objects          | `OS_MEMPOOL_NUM`        | Defines maximum number of objects that can be active at the same time. Applies to objects with system provided memory for control blocks. Value range is `[1-1000]`.
Data Storage Memory size [bytes]       | `OS_MEMPOOL_DATA_SIZE`  | Defines the combined data storage memory size. Applies to objects with system provided memory for data storage. Default value is `0`. Value range is `[0-1073741824]`, in multiples of `8`.
### Object-specific memory allocation

When object-specific memory is used, the number of pools for all MemoryPool objects is specified by `OS_MEMPOOL_NUM`. The total storage size reserved for all pools is configured in `OS_MEMPOOL_DATA_SIZE`. Refer to ObjectMemoryPool.
