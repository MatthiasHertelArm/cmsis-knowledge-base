---
id: "rtx-cmsis-rtos2-api-osrtxerrorisrqueueoverflow"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxErrorISRQueueOverflow"
summary: "ISR Queue overflow detected when inserting object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxErrorISRQueueOverflow
```

 ISR Queue overflow detected when inserting object.

This error identifier is used with osRtxErrorNotify when RTX5 detects an overflow of the
interrupt post processing message queue. The object_id can be used to identify the affected
object.

**Warning:** Whenever this error identifier is signaled the system state is already inconsistent.
