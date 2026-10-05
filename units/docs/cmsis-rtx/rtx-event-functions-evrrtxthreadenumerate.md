---
id: "rtx-event-functions-evrrtxthreadenumerate"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadEnumerate"
summary: "The event ThreadEnumerate is generated when the function osThreadEnumerate is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadEnumerate (osThreadId_t *thread_array, uint32_t array_items, uint32_t count)
```


The event **ThreadEnumerate** is generated when the function osThreadEnumerate is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **thread_array** : memory address of array for retrieving thread IDs.
  - **array_items** : maximum number of items in thread_array.
  - **count** : number of enumerated threads (0 in case of a failure).
