---
id: "rtx-cmsis-rtos2-api-osrtxerrorstackoverflow"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxErrorStackOverflow"
summary: "Stack overflow, i.e. stack pointer below its lower memory limit for descending stacks."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxErrorStackOverflow
```

 Stack overflow, i.e. stack pointer below its lower memory limit for descending stacks.

This error identifier is used with osRtxErrorNotify when RTX5 detects a thread stack overflow.
The object_id announced along this error can be used to identify the affected thread.

threadConfig_watermark used together with larger stack sizes can help to figure out actual
memory requirements for threads.

**Warning:** Whenever this error identifier is signaled memory corruption has already happened.
