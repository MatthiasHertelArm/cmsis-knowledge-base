---
id: "view-fault-api-arm-faultsave"
type: "concept"
domain: "trace"
title: "Fault API: ARM_FaultSave"
summary: "Call from a fault handler to save current fault information into uninitialized RAM memory."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_fault.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_fault.txt"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_FaultSave
```


Call from a fault handler to save current fault information into uninitialized RAM memory.

Make sure that function is called without changing the Stack Pointer (SP) and Link Register (LR) registers.
This is usually done by branching directly to this function from the fault handler.

This function does not use stack or heap memories.

**Code** **Example**
```
#include "ARM_Fault.h"

__attribute__((naked)) void HardFault_Handler (void) {
  __ASM volatile (
    "b  ARM_FaultSave\n"
  );
}

__attribute__((naked)) void MemManage_Handler (void) {
  __ASM volatile (
    "b  ARM_FaultSave\n"
  );
}

__attribute__((naked)) void BusFault_Handler (void) {
  __ASM volatile (
    "b  ARM_FaultSave\n"
  );
}

__attribute__((naked)) void UsageFault_Handler (void) {
  __ASM volatile (
    "b  ARM_FaultSave\n"
  );
}
```
