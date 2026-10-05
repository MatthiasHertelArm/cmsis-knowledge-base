---
id: "rtx-configure-rtx-v5"
type: "concept"
domain: "rtos"
title: "Configure RTX v5"
summary: "The file RTX_Config.h defines the configuration parameters of CMSIS-RTOS RTX and must be part of every project that is using the CMSIS-RTOS2 RTX kernel. The configuration options are explained in detail in the following sections:"
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md"
license: "Apache-2.0"
mode: "V"
---

The file **RTX_Config.h** defines the configuration parameters of CMSIS-RTOS RTX and must be part of every project that is using the CMSIS-RTOS2 RTX kernel. The configuration options are explained in detail in the following sections:

- systemConfig covers system-wide settings for the global memory pool, tick frequency, ISR event buffer and round-robin thread switching as well as process isolation-related features.
- threadConfig provides several parameters to configure the CMSIS_RTOS_ThreadMgmt functions.
- timerConfig provides several parameters to configure the CMSIS_RTOS_TimerMgmt functions.
- eventFlagsConfig provides several parameters to configure the CMSIS_RTOS_EventFlags functions.
- mutexConfig provides several parameters to configure the CMSIS_RTOS_MutexMgmt functions.
- semaphoreConfig provides several parameters to configure the CMSIS_RTOS_SemaphoreMgmt functions.
- memPoolConfig provides several parameters to configure the CMSIS_RTOS_PoolMgmt functions.
- msgQueueConfig provides several parameters to configure the CMSIS_RTOS_Message functions.
- evtrecConfig provides several parameters to configure RTX for usage with [Event Recorder](https://arm-software.github.io/CMSIS-View/latest/evr.html).

The file `RTX_Config.c` contains default implementations of the functions osRtxIdleThread and osRtxErrorNotify. Both functions can simply be overwritten with a customized behavior by redefining them as part of the user code.

The configuration file uses **Configuration Wizard Annotations**. Refer to **Pack - Configuration Wizard Annotations** for details.

Depending on the development tool, the annotations might lead to a more user-friendly graphical representation of the settings. The picture below shows the **Configuration Wizard** view in µVision MDK:

(figure: RTX_Config.h in Configuration Wizard View)

Alternatively one can provide configuration options using the compiler command line.

For example one can customize the used tick frequency to 100us by (overwriting) the configuration using

```
cc -DOS_TICK_FREQ=100
```
