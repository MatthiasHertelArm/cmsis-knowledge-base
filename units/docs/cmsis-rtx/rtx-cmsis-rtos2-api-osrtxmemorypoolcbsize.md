---
id: "rtx-cmsis-rtos2-api-osrtxmemorypoolcbsize"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxMemoryPoolCbSize"
summary: "This macro exposes the minimum amount of memory needed for an RTX5 Memory Pool Control Block, see osMemoryPoolAttr_t::cb_mem and osMemoryPoolAttr_t::cb_size."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxMemoryPoolCbSize
```

 Memory Pool Control Block size

This macro exposes the minimum amount of memory needed for an RTX5 Memory Pool Control Block,
see osMemoryPoolAttr_t::cb_mem and osMemoryPoolAttr_t::cb_size.

Example:
```
// Used-defined memory for memory pool control block
static uint32_t mempool_cb[osRtxMemoryPoolCbSize/4U];
```
