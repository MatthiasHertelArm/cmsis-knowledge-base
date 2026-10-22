---
id: "rtos2-thread-management-affinity-mask"
type: "concept"
domain: "rtos"
title: "Thread Management: affinity_mask"
summary: "Use the osThreadProcessor macro to create the mask value. Multiple processors can be specified by OR-ing values."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadAttr_t::affinity_mask
```


Use the osThreadProcessor macro to create the mask value. Multiple processors can be specified by OR-ing values.

Default: value `0` is RTOS implementation specific and may map to running on processor #0 or on any processor.
