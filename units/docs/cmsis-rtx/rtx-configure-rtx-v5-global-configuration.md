---
id: "rtx-configure-rtx-v5-global-configuration"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: Event Recorder Configuration / Global Configuration"
summary: "Initialize Event Recorder during the osKernelInitialize and optionally start event recording."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#global-configuration"
license: "Apache-2.0"
mode: "V"
---

_Part of: Event Recorder Configuration_

Initialize Event Recorder during the osKernelInitialize and optionally start event recording.

(figure: RTX_Config.h: Global Configuration)

Name                  | \#define        | Description
----------------------|-----------------|----------------------------------------------------------------
Global Initialization | `OS_EVR_INIT`  | Initialize Event Recorder during osKernelInitialize.
Start Recording       | `OS_EVR_START` | Start event recording after initialization.

> **Note**
>
> - If **Global Initialization** (`OS_EVR_INIT`) is set, an explicit call to `EventRecorderInitialize` is not required.
> - If **Start Recording** (`OS_EVR_START`) is set, an explicit call to `EventRecorderStart` is not required. You may call the function `EventRecorderStop` to stop recording.

**Global Event Filter Setup**

These event filter settings are applied to all software component numbers, including MDK middleware and user components.

(figure: RTX_Config.h: Global Event Filter Setup)

Name                      | \#define         | Description
--------------------------|------------------|----------------------------------------------------------------
Error events              | `OS_EVR_LEVEL`  | Enable error events.
API function call events  | `OS_EVR_LEVEL`  | Enable API function call events.
Operation events          | `OS_EVR_LEVEL`  | Enable operation events.
Detailed operation events | `OS_EVR_LEVEL`  | Enable detailed operation events.

> **Note**
>
> - You may disable event recording for specific software components by calling the function `EventRecorderDisable`.

**RTOS Event Filter Setup**

These event filter settings are applied to specific RTX component groups with sub-options for:

- Error events
- API function call events
- Operation events
- Detailed operation events

The generation of events must be enabled as explained under evtrecConfigEvtGen.

(figure: RTX_Config.h: RTOS Event Filter Setup)

Name              | \#define                   | Description
------------------|----------------------------|----------------------------------------------------------------
Memory Management | `OS_EVR_MEMORY_LEVEL`     | Recording level for Memory Management events.
Kernel            | `OS_EVR_KERNEL_LEVEL`     | Recording level for Kernel events.
Thread            | `OS_EVR_THREAD_LEVEL`     | Recording level for Thread events.
Generic Wait      | `OS_EVR_WAIT_LEVEL`       | Recording level for Generic Wait events.
Thread Flags      | `OS_EVR_THFLAGS_LEVEL`    | Recording level for Thread Flags events.
Event Flags       | `OS_EVR_EVFLAGS_LEVEL`    | Recording level for Event Flags events.
Timer             | `OS_EVR_TIMER_LEVEL`      | Recording level for Timer events.
Mutex             | `OS_EVR_MUTEX_LEVEL`      | Recording level for Mutex events.
Semaphore         | `OS_EVR_SEMAPHORE_LEVEL`  | Recording level for Semaphore events.
Memory Pool       | `OS_EVR_MEMPOOL_LEVEL`    | Recording level for Memory Pool events.
Message Queue     | `OS_EVR_MSGQUEUE_LEVEL`   | Recording level for Message Queue events.
