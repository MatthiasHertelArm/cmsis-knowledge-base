---
id: "rtos2-thread-management-osthreadinactive"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadInactive"
summary: "The thread is created but not actively used, or has been terminated (returned for static control block allocation, when memory pools are used osThreadError is returned as the control block is no longer valid)"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadState_t::osThreadInactive
```

 The thread is created but not actively used, or has been terminated (returned for static control block allocation, when memory pools are used osThreadError is returned as the control block is no longer valid)
