---
id: "rtos2-kernel-information-and-control-oskernelstate-t"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelState_t"
summary: "State of the kernel as retrieved by osKernelGetState. In case osKernelGetState fails or if it is called from an ISR, it will return osKernelError, otherwise it returns the kernel state."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osKernelState_t
```


State of the kernel as retrieved by osKernelGetState. In case **osKernelGetState** fails or if it is called from an ISR,
it will return `osKernelError,` otherwise it returns the kernel state.
