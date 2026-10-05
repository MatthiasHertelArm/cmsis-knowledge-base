---
id: "rtos2-memory-pool-cb-mem"
type: "concept"
domain: "rtos"
title: "Memory Pool: cb_mem"
summary: "Pointer to a memory location for the memory pool control block object. This can optionally be used for custom memory management systems.\\n Default: NULL (uses kernel memory management)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMemoryPoolAttr_t::cb_mem
```


Pointer to a memory location for the memory pool control block object. This can optionally be used for custom memory management systems.\n
Default: `NULL` (uses kernel memory management).
