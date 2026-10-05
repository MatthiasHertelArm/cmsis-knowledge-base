---
id: "rtx-event-functions-evrrtxthreadfeedwatchdog"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFeedWatchdog"
summary: "The event ThreadFeedWatchdog is generated when the function osThreadFeedWatchdog is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFeedWatchdog (uint32_t ticks)
```



The event **ThreadFeedWatchdog** is generated when the function osThreadFeedWatchdog is called.

**Value** in the Event Recorder shows:
  - **ticks** : watchdog timeout in number of kernel ticks.
