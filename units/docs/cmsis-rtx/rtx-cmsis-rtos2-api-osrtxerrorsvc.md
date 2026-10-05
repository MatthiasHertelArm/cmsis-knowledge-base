---
id: "rtx-cmsis-rtos2-api-osrtxerrorsvc"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxErrorSVC"
summary: "This error identifier is used with osRtxErrorNotify when RTX5 detects SVC function pointer that is not properly aligned or is located outside of the RTX5 SVC function table."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxErrorSVC
```

 Invalid SVC function called.

This error identifier is used with osRtxErrorNotify when RTX5 detects SVC function pointer that is not properly aligned
or is located outside of the RTX5 SVC function table.
