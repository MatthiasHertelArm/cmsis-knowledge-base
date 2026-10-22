---
id: "rtos2-thread-management-name"
type: "concept"
domain: "rtos"
title: "Thread Management: name"
summary: "Pointer to a constant string with a human readable name (displayed during debugging) of the thread object."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadAttr_t::name
```


Pointer to a constant string with a human readable name (displayed during debugging) of the thread object.

Default: `NULL` no name specified (debugger may display function name instead).
