---
id: "rtx-cmsis-rtos2-api-osrtxerrorclibmutex"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxErrorClibMutex"
summary: "Standard C/C++ library mutex initialization failed."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxErrorClibMutex
```

 Standard C/C++ library mutex initialization failed.

This error identifier is used with osRtxErrorNotify when RTX5 fails to create mutexes needed
to lock global C/C++ library resources.
