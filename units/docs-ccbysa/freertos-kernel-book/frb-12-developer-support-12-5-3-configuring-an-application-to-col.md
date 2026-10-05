---
id: "frb-12-developer-support-12-5-3-configuring-an-application-to-col"
type: "concept"
domain: "rtos"
title: "12 Developer Support: 12.5 Viewing Run-time and Task State Information / 12.5.3 Configuring an Application to Collect Run-Time Statistics"
summary: "Part of: 12.5 Viewing Run-time and Task State Information"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch12.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch12.md#12-5-3-configuring-an-application-to-collect-run-time-statistics"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 12.5 Viewing Run-time and Task State Information_

Below are details on the macros necessary to collect task run-time
statistics. Originally, the macros were intended to be included in
the RTOS port layer, which is why the macros are prefixed 'port', but it
has proven more practical to define them in `FreeRTOSConfig.h`.

**Macros used in the collection of run-time statistics**

- `configGENERATE_RUN_TIME_STATS`

  This macro must be set to 1 in FreeRTOSConfig.h. When this macro is
  set to 1 the scheduler will call the other macros detailed in this section
  at the appropriate times.

- `portCONFIGURE_TIMER_FOR_RUN_TIME_STATS()`

  This macro must be provided to initialize whichever peripheral is
  used to provide the run-time statistics clock.

- `portGET_RUN_TIME_COUNTER_VALUE()`, or `portALT_GET_RUN_TIME_COUNTER_VALUE(Time)`

  One of these two macros must be provided to return the current
  run-time statistics clock value. This is the total time the application
  has been running, in run-time statistics clock units, since the
  application first booted.

  If the first macro is used, it must be defined to evaluate to the
  current clock value. If the second macro is used, it must be defined to
  set its 'Time' parameter to the current clock value.
