---
id: "rtx-cmsis-rtos2-api-osrtxerrortimerqueueoverflow"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxErrorTimerQueueOverflow"
summary: "User Timer Callback Queue overflow detected for timer."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxErrorTimerQueueOverflow
```

 User Timer Callback Queue overflow detected for timer.

This error identifier is used with osRtxErrorNotify when RTX5 detects an overflow of the
timer callback queue. The object_id can be used to identify the affected timer.

**Warning:** Whenever this error identifier is signaled a timer callback is already lost.
