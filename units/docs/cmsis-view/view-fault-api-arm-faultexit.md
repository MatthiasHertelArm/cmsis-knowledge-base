---
id: "view-fault-api-arm-faultexit"
type: "concept"
domain: "trace"
title: "Fault API: ARM_FaultExit"
summary: "The default implementation will do a system reset."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_fault.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_fault.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_FaultExit
```


The default implementation will do a system reset.

If a system reset is not desired, you need to provide a custom implementation of this function with the desired functionality.

**Code** **Example** of overriding ARM_FaultExit function not to reset the system but to loop endlessly:
```
#include "ARM_Fault.h"

__attribute__((naked)) void ARM_FaultExit (void) {
  __ASM volatile (
    "b  .\n"
  );
}
```
