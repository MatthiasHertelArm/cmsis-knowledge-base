---
id: "rtx-cmsis-rtos2-api-osrtxerrorclibspace"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxErrorClibSpace"
summary: "Standard C/C++ library libspace not available."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxErrorClibSpace
```

 Standard C/C++ library libspace not available.

This error identifier is used with osRtxErrorNotify when RTX5 detects usage of libspace
but not enough memory was reserved using `OS_THREAD_LIBSPACE_NUM.`
