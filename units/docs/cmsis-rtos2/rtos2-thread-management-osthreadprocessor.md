---
id: "rtos2-thread-management-osthreadprocessor"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadProcessor"
summary: "The preprocessor macro osThreadProcessor constructs the value for the osThreadAttrt::affinitymask derived from n."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadProcessor(n)
```

- `n`: processor number, starting with n=0 for processor #0. The number of supported processors depend on the hardware.


The preprocessor macro **osThreadProcessor** constructs the value for the osThreadAttr_t::affinity_mask derived from _n._
