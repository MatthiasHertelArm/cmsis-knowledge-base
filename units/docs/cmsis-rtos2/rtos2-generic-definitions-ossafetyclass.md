---
id: "rtos2-generic-definitions-ossafetyclass"
type: "concept"
domain: "rtos"
title: "Generic Definitions: osSafetyClass"
summary: "The preprocessor macro osSafetyClass constructs attribute bitmask with safety class bits set to n."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osSafetyClass(n)
```

- `n`:        safety class value.
  Safety class value in attribute bit field format.


The preprocessor macro **osSafetyClass** constructs attribute bitmask with safety class bits set to _n._

**Code Example:**
```
/* Event Flags object attributes */
const osEventFlagsAttr_t ef_attr = {
  .name       = "EventFlags1",    // human readable object name
  .attr_bits  = osSafetyClass(2U) // assign object to safety class 2
};
```
