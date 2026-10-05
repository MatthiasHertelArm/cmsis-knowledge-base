---
id: "rtx-configure-rtx-v5-rtos-event-generation"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: Event Recorder Configuration / RTOS Event Generation"
summary: "Enable the event generation for specific RTX component groups. This requires the RTX source variant (refer to crertxprojer for more information)."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#rtos-event-generation"
license: "Apache-2.0"
mode: "V"
---

_Part of: Event Recorder Configuration_

Enable the event generation for specific RTX component groups. This requires the RTX source variant (refer to cre_rtx_proj_er for more information).

(figure: RTX_Config.h: Event generation configuration)

Name              | \#define                 | Description
------------------|--------------------------|----------------------------------------------------------------
Memory Management | `OS_EVR_MEMORY`         | Enables Memory Management events generation.
Kernel            | `OS_EVR_KERNEL`         | Enables Kernel events generation.
Thread            | `OS_EVR_THREAD`         | Enables Thread events generation.
Generic Wait      | `OS_EVR_WAIT`           | Enables Generic Wait events generation.
Thread Flags      | `OS_EVR_THFLAGS`        | Enables Thread Flags events generation.
Event Flags       | `OS_EVR_EVFLAGS`        | Enables Event Flags events generation.
Timer             | `OS_EVR_TIMER`          | Enables Timer events generation.
Mutex             | `OS_EVR_MUTEX`          | Enables Mutex events generation.
Semaphore         | `OS_EVR_SEMAPHORE`      | Enables Semaphore events generation.
Memory Pool       | `OS_EVR_MEMPOOL`        | Enables Memory Pool events generation.
Message Queue     | `OS_EVR_MSGQUEUE`       | Enables Message Queue events generation.

> **Note**
>
> - If event generation for a component is disabled, the code that generates the related events is not included. Thus, filters for this component will have no effect and the debugger is unable to display any events for the related component group.
