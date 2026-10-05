---
id: "rtos2-event-flags-cb-mem"
type: "concept"
domain: "rtos"
title: "Event Flags: cb_mem"
summary: "Pointer to a memory for the event flag control block object. Refer to CMSISRTOSMemoryMgmtManual for more information."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osEventFlagsAttr_t::cb_mem
```


Pointer to a memory for the event flag control block object. Refer to CMSIS_RTOS_MemoryMgmt_Manual for more information.

Default: `NULL` to use CMSIS_RTOS_MemoryMgmt_Automatic for the event flag control block.
