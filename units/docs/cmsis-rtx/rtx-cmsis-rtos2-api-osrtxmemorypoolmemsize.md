---
id: "rtx-cmsis-rtos2-api-osrtxmemorypoolmemsize"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxMemoryPoolMemSize"
summary: "This macro exposes the minimum amount of memory needed for an RTX5 Memory Pool Memory, see osMemoryPoolAttrt::mpmem and osMemoryPoolAttrt::mpsize."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxMemoryPoolMemSize
```

 Memory Pool Memory size

This macro exposes the minimum amount of memory needed for an RTX5 Memory Pool Memory,
see osMemoryPoolAttr_t::mp_mem and osMemoryPoolAttr_t::mp_size.

Example:
```
// Maximum number of objects
#define OBJ_COUNT 8U
 
// Object type
typedef struct {
   uint32_t value1;
   uint8_t  value2;
} object_t;
 
// Used-defined memory for memory pool memory
static uint32_t mempool_mem[osRtxMemoryPoolMemSize(OBJ_COUNT, sizeof(object_t))/4U];
```
