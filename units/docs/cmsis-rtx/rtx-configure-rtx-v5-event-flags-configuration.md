---
id: "rtx-configure-rtx-v5-event-flags-configuration"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: Event Flags Configuration"
summary: "RTX5 provides several parameters to configure the CMSISRTOSEventFlags functions."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#event-flags-configuration"
license: "Apache-2.0"
mode: "V"
---

RTX5 provides several parameters to configure the CMSIS_RTOS_EventFlags functions.

**Event Configuration Options**

(figure: RTX_Config.h: Event Flags Configuration)

Name                                   | \#define                 | Description
---------------------------------------|--------------------------|----------------------------------------------------------------
Object specific Memory allocation      | `OS_EVFLAGS_OBJ_MEM`    | Enables object specific memory allocation. See ObjectMemoryPool.
Number of Event Flags objects          | `OS_EVFLAGS_NUM`        | Defines maximum number of objects that can be active at the same time. Applies to objects with system provided memory for control blocks. Value range is `[1-1000]`.
### Object-specific memory allocation

When object-specific memory is used, the pool size for all Event objects is specified by `OS_EVFLAGS_NUM`. Refer to ObjectMemoryPool.
