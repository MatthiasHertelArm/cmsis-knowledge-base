---
id: "core-interrupts-and-exceptions-nvic-cmsis-vectab-virtual"
type: "concept"
domain: "core"
title: "Interrupts and Exceptions (NVIC): CMSIS_VECTAB_VIRTUAL"
summary: "When CMSIS_NVIC_VIRTUAL is defined, the functions in the table below must be replaced to virtualize the API access functions to the interrupt vector table. The NVIC vector table API should be implemented in a separate source module."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_nvic.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_nvic.txt"
license: "Apache-2.0"
mode: "V"
---

```c
CMSIS_VECTAB_VIRTUAL
```

When CMSIS_NVIC_VIRTUAL is defined, the functions in the table below must be replaced
to virtualize the API access functions to the interrupt vector table. The NVIC vector table API should be implemented
in a separate source module. This allows, for example, alternate implementations to relocate the vector table from flash to RAM on the first vector table update.

The original CMSIS-Core functions are always available, but prefixed with __NVIC.

Interrupt Vector Table Access  | CMSIS-Core Functions
-------------------------------|---------------------------------------------
NVIC_GetVector                 | __NVIC_GetVector
NVIC_SetVector                 | __NVIC_SetVector
