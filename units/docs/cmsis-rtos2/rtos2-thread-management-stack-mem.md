---
id: "rtos2-thread-management-stack-mem"
type: "concept"
domain: "rtos"
title: "Thread Management: stack_mem"
summary: "Pointer to a memory location for the thread stack (64-bit aligned)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadAttr_t::stack_mem
```


Pointer to a memory location for the thread stack (64-bit aligned). 

Default: `NULL` - the memory for the stack is provided by the system based on the configuration of underlying RTOS kernel .
