---
id: "rtos2-process-isolation-assign-safety-class-to-an-rtos-object"
type: "concept"
domain: "rtos"
title: "Process Isolation: Assign Safety Class to an RTOS Object"
summary: "It is possible to create any objects regardless of the safety class after the kernel initialize with osKernelInitialize, but before the kernel is started with osKernelStart. This allows to setup a system before actually starting the RTOS kernel."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md#assign-safety-class-to-an-rtos-object"
license: "Apache-2.0"
mode: "V"
---

It is possible to create any objects regardless of the safety class after the kernel initialize with osKernelInitialize, but before the kernel is started with osKernelStart. This allows to setup a system before actually starting the RTOS kernel.

Threads of a higher safety class can create RTOS objects that belong to a lower or same safety class. For the object types listed below, the _attr_bits_ can have an optional safety class value that is assigned when the RTOS object is created with the __os<Object>New__ function. The macro osSafetyClass encodes the value for the _attr_bits_ field in the attr struct. For example:

```c
const osEventFlagsAttr_t evt_flags_attr = {
  .attr_bits = osSafetyClass(SAFETY_CLASS_SAFE_MODE_OPERATION)
};
osEventFlagsId_t evt_flags;
evt_flags = osEventFlagsNew(&evt_flags_attr);
```

The following object types support safety class assignment when creating an object with corresponding _os<Object>New_ function:

 - osThreadAttr_t  osThreadAttr_t Used in the osThreadNew function.
 - osEventFlagsAttr_t   osEventFlagsAttr_t Used in the osThreadNew function.
 - osTimerAttr_t  osTimerAttr_t Used in the osTimerNew function.
 - osMutexAttr_t  osMutexAttr_t Used in the osMutexNew function.
 - osSemaphoreAttr_t  osSemaphoreAttr_t Used in the osSemaphoreNew function.
 - osMemoryPoolAttr_t  osMemoryPoolAttr_t Used in the osMemoryPoolNew function.
 - osMessageQueueAttr_t  osMessageQueueAttr_t Used in the osMessageQueueNew function.

If safety class is not provided when creating the RTOS object then it inherits the safety class of the current running thread that creates the object. If the object is created before kernel is started and no safety class is provided, then it receives default safety class 0. This simplifies integration of third-party code that can be classified as non-safety critical.
