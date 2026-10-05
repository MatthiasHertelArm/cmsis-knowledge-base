---
id: "rtx-operation-low-power-operation"
type: "concept"
domain: "rtos"
title: "operation: Low-Power Operation"
summary: "The system thread osRtxIdleThread can be use to switch the system into a low-power mode."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#low-power-operation"
license: "Apache-2.0"
mode: "V"
---

The system thread `osRtxIdleThread` can be use to switch the system into a low-power mode. The easiest form to enter a low-power mode is the execution of the `__WFE` function that puts the processor into a sleep mode where it waits for an event.

**Code Example:**

```c
#include "RTE_Components.h"
#include CMSIS_device_header            /* Device definitions                 */
 
void osRtxIdleThread (void) {
  /* The idle demon is a system thread, running when no other thread is       */
  /* ready to run.                                                            */
 
  for (;;) {
    __WFE();                            /* Enter sleep mode                   */
  }
}
```

> **Note**
>
> - `__WFE()` is not available in every Cortex-M implementation. Check device manuals for availability.
