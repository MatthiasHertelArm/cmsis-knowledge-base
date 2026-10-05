---
id: "rtx-configure-rtx-v5-message-queue-configuration"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: Message Queue Configuration"
summary: "RTX5 provides several parameters to configure the CMSIS_RTOS_Message functions."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#message-queue-configuration"
license: "Apache-2.0"
mode: "V"
---

RTX5 provides several parameters to configure the CMSIS_RTOS_Message functions.

**MessageQueue Configuration Options**

(figure: RTX_Config.h: Message Queue Configuration)

Name                                   | \#define                 | Description
---------------------------------------|--------------------------|----------------------------------------------------------------
Object specific Memory allocation      | `OS_MSGQUEUE_OBJ_MEM`   | Enables object specific memory allocation. See ObjectMemoryPool.
Number of Message Queue objects        | `OS_MSGQUEUE_NUM`       | Defines maximum number of objects that can be active at the same time. Applies to objects with system provided memory for control blocks. Value range is `[1-1000]`.
Data Storage Memory size [bytes]       | `OS_MSGQUEUE_DATA_SIZE` | Defines the combined data storage memory size. Applies to objects with system provided memory for data storage. Default value is `0`. Value range is `[0-1073741824]`, in multiples of `8`.
### Object-specific memory allocation

When Object-specific Memory is used, the number of queues for all Message Queue objects is specified by `OS_MSGQUEUE_NUM`. The total storage size reserved for all queues is configured in `OS_MSGQUEUE_DATA_SIZE`. Refer to ObjectMemoryPool.
