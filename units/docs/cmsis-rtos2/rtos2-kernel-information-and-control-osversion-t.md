---
id: "rtos2-kernel-information-and-control-osversion-t"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osVersion_t"
summary: "Identifies the underlying RTOS kernel and API version number. The version is represented in a combined decimal number in the format: major.minor.rev: mmnnnrrrr"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osVersion_t
```


Identifies the underlying RTOS kernel and API version number. The version is represented in a combined decimal number in the
format: major.minor.rev: mmnnnrrrr 

Use osKernelGetInfo to retrieve the version numbers.
