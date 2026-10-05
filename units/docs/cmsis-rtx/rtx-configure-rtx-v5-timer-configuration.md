---
id: "rtx-configure-rtx-v5-timer-configuration"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: Timer Configuration"
summary: "RTX5 provides several parameters to configure the CMSISRTOSTimerMgmt functions."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#timer-configuration"
license: "Apache-2.0"
mode: "V"
---

RTX5 provides several parameters to configure the CMSIS_RTOS_TimerMgmt functions.

**Timer Configuration Options**

(figure: RTX_Config.h: Timer Configuration)

Name                                   | \#define                 | Description
---------------------------------------|--------------------------------|----------------------------------------------------------------
Object specific Memory allocation      | `OS_TIMER_OBJ_MEM`      | Enables object specific memory allocation.
Number of Timer objects                | `OS_TIMER_NUM`          | Defines maximum number of objects that can be active at the same time. Applies to objects with system provided memory for control blocks. Value range is `[1-1000]`.
Timer Thread Priority                  | `OS_TIMER_THREAD_PRIO`        | Defines priority for timer thread. Default value is `40`. Value range is `[8-48]`, in multiples of `8`. The numbers have the following priority correlation: `8=Low`; `16=Below Normal`; `24=Normal`; `32=Above Normal`; `40=High`; `48=Realtime`
Timer Thread Stack size [bytes]        | `OS_TIMER_THREAD_STACK_SIZE`  | Defines stack size for Timer thread. May be set to 0 when timers are not used. Default value is `512`. Value range is `[0-1073741824]`, in multiples of `8`.
Timer Thread TrustZone Module ID       | `OS_TIMER_THREAD_TZ_MOD_ID`   | Defines the TrustZone Module ID the Timer Thread shall use. This needs to be set to a non-zero value if any Timer Callbacks need to call secure functions. Default value is `0`.
Timer Thread Safety Class              | `OS_TIMER_THREAD_CLASS`        | Defines the the Safety Class for the Timer thread. Applied only if Safety class functionality is enabled in systemConfig. Default value is `0`.
Timer Thread Zone                      | `OS_TIMER_THREAD_ZONE`         | Defines the MPU Protected Zone for the Timer thread. Applied only if MPU protected Zone functionality is enabled in systemConfig. Default value is `0`.
Timer Callback Queue entries           | `OS_TIMER_CB_QUEUE`           | Number of concurrent active timer callback functions. May be set to 0 when timers are not used. Default value is `4`. Value range is `[0-256]`.
### Object-specific memory allocation

See ObjectMemoryPool.
### User Timer Thread

The RTX5 function **osRtxTimerThread** executes callback functions when a time period expires. The priority of the timer subsystem within the complete RTOS system is inherited from the priority of the **osRtxTimerThread**. This is configured by `OS_TIMER_THREAD_PRIO`. Stack for callback functions is supplied by **osRtxTimerThread**. `OS_TIMER_THREAD_STACK_SIZE` must satisfy the stack requirements of the callback function with the highest stack usage.
